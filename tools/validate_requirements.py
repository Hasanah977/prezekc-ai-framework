#!/usr/bin/env python3
"""Validate structured PREZEKC PRD, SRS, and RTM records (stdlib only)."""

import argparse
import json
import re
import sys
from pathlib import Path

PRD_ID = re.compile(r"^PRD-(?:FR|NFR)-\d{3,}$")
SRS_ID = re.compile(r"^SRS-(?:FR-\d{3,}\.\d+|NFR-\d{3,})$")
DES_ID = re.compile(r"^DES-\d{3,}$")
TEST_ID = re.compile(r"^TC-\d{3,}$")


def load_json(path, label, errors):
    try:
        value = json.loads(Path(path).read_text(encoding="utf-8-sig"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        errors.append(f"{label}: cannot read valid JSON: {exc}")
        return None
    if not isinstance(value, dict):
        errors.append(f"{label}: root must be a JSON object")
        return None
    return value


def registry(document, key, pattern, label, errors):
    entries = document.get(key)
    if not isinstance(entries, list):
        errors.append(f"{label}: '{key}' must be an array")
        return {}
    found = {}
    for index, entry in enumerate(entries):
        if not isinstance(entry, dict):
            errors.append(f"{label}: {key}[{index}] must be an object")
            continue
        ident = entry.get("id")
        if not isinstance(ident, str) or not pattern.fullmatch(ident):
            errors.append(f"{label}: {key}[{index}] has an invalid ID: {ident!r}")
            continue
        if ident in found:
            errors.append(f"{label}: duplicate ID {ident}")
        else:
            found[ident] = entry
    return found


def string_list(value, field, label, errors):
    if not isinstance(value, list) or any(not isinstance(v, str) or not v.strip() for v in value):
        errors.append(f"{label}: '{field}' must be an array of nonempty strings")
        return []
    if len(value) != len(set(value)):
        errors.append(f"{label}: '{field}' contains duplicates")
    return value


def validate(prd, srs, rtm, design=None, tests=None):
    errors, warnings = [], []
    for label, doc, expected in (("PRD", prd, "PRD"), ("SRS", srs, "SRS"), ("RTM", rtm, "RTM")):
        if doc.get("document_id") != expected:
            errors.append(f"{label}: document_id must be '{expected}'")
        if not isinstance(doc.get("version"), str) or not doc["version"].strip():
            errors.append(f"{label}: missing nonempty version")

    approval = prd.get("approval")
    if prd.get("status") != "APPROVED" or not isinstance(approval, dict) or any(
        not isinstance(approval.get(field), str) or not approval[field].strip()
        for field in ("approved_by", "decision_reference")
    ):
        errors.append("PRD: approved baseline requires status APPROVED and approval details")
    if srs.get("source_prd_version") != prd.get("version"):
        errors.append("SRS: source_prd_version does not match PRD version")
    if rtm.get("source_prd_version") != prd.get("version"):
        errors.append("RTM: source_prd_version does not match PRD version")
    if rtm.get("source_srs_version") != srs.get("version"):
        errors.append("RTM: source_srs_version does not match SRS version")
    if srs.get("status") != "APPROVED":
        warnings.append("SRS: baseline is not APPROVED; mappings are provisional")

    prd_records = registry(prd, "requirements", PRD_ID, "PRD", errors)
    srs_records = registry(srs, "requirements", SRS_ID, "SRS", errors)
    links = set()
    for sid, requirement in srs_records.items():
        parents = string_list(requirement.get("parent_requirements"), "parent_requirements", sid, errors)
        if not parents:
            errors.append(f"{sid}: no originating PRD requirement")
        for parent in parents:
            if parent not in prd_records:
                errors.append(f"{sid}: unknown parent requirement {parent}")

    mappings = rtm.get("mappings")
    if not isinstance(mappings, list):
        errors.append("RTM: 'mappings' must be an array")
        mappings = []

    design_records = registry(design, "design_elements", DES_ID, "DESIGN", errors) if design is not None else None
    test_records = registry(tests, "test_cases", TEST_ID, "TESTS", errors) if tests is not None else None
    for index, row in enumerate(mappings):
        label = f"RTM: mappings[{index}]"
        if not isinstance(row, dict):
            errors.append(f"{label} must be an object")
            continue
        pid, sid = row.get("prd_id"), row.get("srs_id")
        if not isinstance(pid, str) or pid not in prd_records:
            errors.append(f"{label}: unknown PRD ID {pid!r}")
        if not isinstance(sid, str) or sid not in srs_records:
            errors.append(f"{label}: unknown SRS ID {sid!r}")
        if isinstance(pid, str) and isinstance(sid, str):
            if (pid, sid) in links:
                errors.append(f"{label}: duplicate mapping {pid} -> {sid}")
            links.add((pid, sid))
            if sid in srs_records and pid not in (srs_records[sid].get("parent_requirements") if isinstance(srs_records[sid].get("parent_requirements"), list) else []):
                errors.append(f"{label}: mapping contradicts {sid} parent_requirements")
        for field, pattern, known in (("design_ids", DES_ID, design_records), ("test_ids", TEST_ID, test_records)):
            for ident in string_list(row.get(field, []), field, label, errors):
                if not pattern.fullmatch(ident):
                    errors.append(f"{label}: invalid {field} reference {ident}")
                elif known is None:
                    errors.append(f"{label}: {ident} cannot be verified without its registry")
                elif ident not in known:
                    errors.append(f"{label}: unknown {field} reference {ident}")

    for sid, record in srs_records.items():
        for parent in record.get("parent_requirements", []):
            if parent in prd_records and (parent, sid) not in links:
                errors.append(f"RTM: missing mapping {parent} -> {sid}")
    for pid, record in prd_records.items():
        covered = any(parent == pid for parent, _ in links)
        if not covered:
            priority = record.get("priority")
            if priority == "MUST":
                errors.append(f"PRD: mandatory requirement {pid} has no SRS coverage")
            else:
                warnings.append(f"PRD: {pid} has no SRS coverage (priority={priority!r})")
    return errors, warnings


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prd", required=True, type=Path)
    parser.add_argument("--srs", required=True, type=Path)
    parser.add_argument("--rtm", required=True, type=Path)
    parser.add_argument("--design", type=Path, help="Optional JSON design registry")
    parser.add_argument("--tests", type=Path, help="Optional JSON test-case registry")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as failures")
    args = parser.parse_args(argv)
    errors = []
    documents = {
        "prd": load_json(args.prd, "PRD", errors),
        "srs": load_json(args.srs, "SRS", errors),
        "rtm": load_json(args.rtm, "RTM", errors),
    }
    if args.design is not None:
        documents["design"] = load_json(args.design, "DESIGN", errors)
    if args.tests is not None:
        documents["tests"] = load_json(args.tests, "TESTS", errors)
    warnings = []
    if not errors:
        errors, warnings = validate(**documents)
    for finding in errors:
        print(f"ERROR: {finding}")
    for finding in warnings:
        print(f"WARNING: {finding}")
    print(f"Requirements validation: {len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors or (args.strict and warnings) else 0


if __name__ == "__main__":
    sys.exit(main())
