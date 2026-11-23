#!/usr/bin/env python3
"""Extract PREZEKC PRD, SRS, and RTM JSON manifests from controlled Markdown."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

PRD_ID = re.compile(r"PRD-(?:FR|NFR)-\d{3,}")
SRS_ID = re.compile(r"SRS-(?:FR-\d{3,}\.\d+|NFR-\d{3,})")
HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$")
PLACEHOLDER = re.compile(r"^\s*(?:\[[^\]]*\]|PENDING|NOT_RUN|UNKNOWN|N/A|NONE|[-—])\s*$", re.I)


class ExtractionError(ValueError):
    """A document cannot be extracted without guessing required information."""


def substantive(value: str | None) -> bool:
    return bool(value and value.strip() and not PLACEHOLDER.fullmatch(value.strip()))


def content_lines(text: str) -> list[str]:
    """Exclude fenced examples, which are not authoritative requirements."""
    result = []
    fence_char = None
    fence_length = 0
    for line in text.lstrip("\ufeff").splitlines():
        match = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if match:
            token = match.group(1)
            if fence_char is None:
                fence_char, fence_length = token[0], len(token)
            elif token[0] == fence_char and len(token) >= fence_length:
                fence_char, fence_length = None, 0
            result.append("")
        else:
            result.append("" if fence_char else line)
    return result


def sections(lines: list[str]) -> list[tuple[str, list[str]]]:
    result: list[tuple[str, list[str]]] = []
    current = ("", [])
    for line in lines:
        match = HEADING.match(line)
        if match:
            result.append(current)
            current = (match.group(1).strip(), [])
        else:
            current[1].append(line)
    result.append(current)
    return result


def table_rows(lines: list[str]) -> list[dict[str, str]]:
    """Read simple pipe tables; escaped pipe cells are supported."""
    rows = []
    for line in lines:
        if not line.strip().startswith("|"):
            continue
        cells = [cell.strip().replace(r"\|", "|") for cell in re.split(r"(?<!\\)\|", line.strip().strip("|"))]
        if all(re.fullmatch(r":?-{3,}:?", c or "") for c in cells):
            continue
        rows.append(cells)
    if len(rows) < 2:
        return []
    head = [h.casefold() for h in rows[0]]
    return [dict(zip(head, values)) for values in rows[1:] if len(values) == len(head)]


def document_controls(lines: list[str]) -> dict[str, str]:
    for title, section in sections(lines):
        if title.casefold() in {"document control", "document metadata"}:
            entries = table_rows(section)
            if not entries or not {"field", "value"}.issubset(entries[0]):
                raise ExtractionError("Document Control must contain a Field | Value table")
            fields = {}
            for entry in entries:
                name = entry["field"].casefold().strip()
                if name in fields:
                    raise ExtractionError(f"Document Control contains duplicate field: {name}")
                fields[name] = entry["value"].strip()
            return fields
    raise ExtractionError("Missing Document Control section")


def required(fields: dict[str, str], key: str, label: str) -> str:
    value = fields.get(key, "")
    if not substantive(value):
        raise ExtractionError(f"{label}: missing or placeholder {key}")
    return value.strip()


def named_section(lines: list[str], name: str) -> list[str]:
    for title, body in sections(lines):
        if title.casefold() == name.casefold() or re.fullmatch(r"\d+\.\s*" + re.escape(name), title, re.I):
            return body
    raise ExtractionError(f"Missing section: {name}")


def colon_fields(body: list[str]) -> dict[str, str]:
    fields: dict[str, str] = {}
    for line in body:
        match = re.match(r"^\s*(?:\*\*)?([A-Za-z][\w /-]*?):(?:\*\*)?\s*(.*)$", line)
        if match:
            key, value = match.groups()
            fields[key.strip().casefold()] = value.strip()
    return fields


def approval_data(lines: list[str]) -> dict[str, str]:
    """Only explicit approval metadata is valid; never infer approvals."""
    for title, body in sections(lines):
        if "approval record" in title.casefold():
            rows = table_rows(body)
            return {r["field"].casefold().strip(): r["value"].strip()
                    for r in rows if "field" in r and "value" in r}
    return {}


def norm_version(value: str) -> str:
    value = value.strip()
    match = re.fullmatch(r"(?:PRD|SRS)\s*(?:v(?:ersion)?\s*)?(\d+(?:\.\d+)*)", value, re.I)
    return match.group(1) if match else value


def extract_prd(text: str) -> dict:
    lines = content_lines(text)
    meta = document_controls(lines)
    version = required(meta, "version", "PRD")
    status = required(meta, "status", "PRD").upper()
    result = {"document_id": "PRD", "version": version, "status": status, "requirements": []}
    if status == "APPROVED":
        approval = approval_data(lines)
        approved_by = approval.get("approved by", meta.get("approved by", ""))
        decision = approval.get("decision", "")
        reference = approval.get("decision reference", "")
        approved_version = approval.get("approved version", "")
        if decision.upper() not in {"APPROVED", "ACCEPTED"}:
            raise ExtractionError("PRD: Approval Record must have Decision = APPROVED")
        if not substantive(approved_by) or not substantive(reference):
            raise ExtractionError("PRD: APPROVED requires Approved By and Decision Reference")
        if substantive(approved_version) and norm_version(approved_version) != version:
            raise ExtractionError("PRD: Approved Version does not match Document Control version")
        result["approval"] = {"approved_by": approved_by, "decision_reference": reference}
    used = set()
    for heading, body in sections(lines):
        match = re.match(r"^(PRD-(?:FR|NFR)-\d{3,})(?:\s*[—–-]\s*.+)?$", heading)
        if not match:
            continue
        ident = match.group(1)
        if ident in used:
            raise ExtractionError(f"PRD: duplicate requirement heading {ident}")
        used.add(ident)
        fields = colon_fields(body)
        statement = fields.get("statement", "")
        priority = fields.get("priority", "")
        if not substantive(statement) or not substantive(priority):
            raise ExtractionError(f"{ident}: Statement and Priority must be explicit")
        result["requirements"].append({"id": ident, "priority": priority.upper(), "statement": statement})
    if not result["requirements"]:
        raise ExtractionError("PRD: no PRD-FR/PRD-NFR requirement headings found")
    return result


def extract_srs(text: str) -> dict:
    lines = content_lines(text)
    meta = document_controls(lines)
    result = {"document_id": "SRS", "version": required(meta, "version", "SRS"),
              "status": required(meta, "status", "SRS").upper(),
              "source_prd_version": norm_version(required(meta, "source prd", "SRS")),
              "requirements": []}
    used = set()
    for heading, body in sections(lines):
        match = re.match(r"^(SRS-(?:FR-\d{3,}\.\d+|NFR-\d{3,}))(?:\s*[—–-]\s*.+)?$", heading)
        if not match:
            continue
        ident = match.group(1)
        if ident in used:
            raise ExtractionError(f"SRS: duplicate requirement heading {ident}")
        used.add(ident)
        fields = colon_fields(body)
        parent = fields.get("parent requirements", fields.get("source requirements", ""))
        parents = PRD_ID.findall(parent)
        if not parents or len(parents) != len(set(parents)):
            raise ExtractionError(f"{ident}: missing or duplicate Parent Requirements")
        if not substantive(fields.get("statement", "")):
            raise ExtractionError(f"{ident}: Statement must be explicit")
        result["requirements"].append({"id": ident, "parent_requirements": parents,
                                        "statement": fields["statement"]})
    if not result["requirements"]:
        raise ExtractionError("SRS: no SRS-FR/SRS-NFR requirement headings found")
    return result


def extract_rtm(text: str) -> dict:
    lines = content_lines(text)
    meta = document_controls(lines)
    result = {"document_id": "RTM", "version": required(meta, "version", "RTM"),
              "source_prd_version": norm_version(required(meta, "prd baseline", "RTM")),
              "source_srs_version": norm_version(required(meta, "srs baseline", "RTM")),
              "mappings": []}
    section = named_section(lines, "Traceability Register")
    rows = table_rows(section)
    if not rows:
        raise ExtractionError("RTM: Traceability Register must contain a nonempty table")
    used = set()
    for idx, row in enumerate(rows, 1):
        pid, sid = row.get("prd id", ""), row.get("srs id", "")
        if not PRD_ID.fullmatch(pid) or not SRS_ID.fullmatch(sid):
            raise ExtractionError(f"RTM row {idx}: invalid PRD ID or SRS ID")
        pair = (pid, sid)
        if pair in used:
            raise ExtractionError(f"RTM: duplicate mapping {pid} -> {sid}")
        used.add(pair)
        def extract_refs(value: str, prefix: str) -> list[str]:
            if not substantive(value):
                return []
            ids = [v.strip() for v in re.split(r"[,;]", value)]
            pattern = re.compile(r"DES-\d{3,}") if prefix == "design" else re.compile(r"TC-\d{3,}")
            if not all(pattern.fullmatch(item) for item in ids):
                raise ExtractionError(f"RTM row {idx}: invalid {prefix} references: {value}")
            return ids
        result["mappings"].append({"prd_id": pid, "srs_id": sid,
                                   "design_ids": extract_refs(row.get("design id", ""), "design"),
                                   "test_ids": extract_refs(row.get("test id", ""), "test")})
    return result


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prd", required=True, type=Path, help="Controlled PRD Markdown")
    parser.add_argument("--srs", required=True, type=Path, help="Controlled SRS Markdown")
    parser.add_argument("--rtm", required=True, type=Path, help="Controlled RTM Markdown")
    parser.add_argument("--output", required=True, type=Path, help="Destination directory for JSON manifests")
    args = parser.parse_args(argv)
    try:
        sources = {key: getattr(args, key).read_text(encoding="utf-8-sig") for key in ("prd", "srs", "rtm")}
        docs = {"prd": extract_prd(sources["prd"]),
                "srs": extract_srs(sources["srs"]),
                "rtm": extract_rtm(sources["rtm"])}
        paths = {name: args.output / f"{name}.json" for name in docs}
        if any(path.exists() for path in paths.values()):
            raise ExtractionError("Output JSON already exists; choose an empty output directory")
        args.output.mkdir(parents=True, exist_ok=True)
        for name, data in docs.items():
            paths[name].write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    except (OSError, UnicodeError, ExtractionError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    for name, path in paths.items():
        print(f"EXTRACTED {name.upper()}: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
