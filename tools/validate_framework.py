#!/usr/bin/env python3
"""Validate PREZEKC AI repository structure, skill headers, and local links."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urlsplit

CORE_FILES = (
    'AGENTS.md', 'FRAMEWORK.md', 'README.md',
    'core/governance.md', 'core/workflow.md', 'core/verification.md',
)
EXPECTED_SKILLS = (
    'system-analysis', 'comparative-study', 'requirement-analysis',
    'prd-generation', 'prd-to-srs', 'system-design',
    'web-development', 'mobile-development', 'testing', 'deployment',
    'ui-ux-flow', 'task-breakdown',
    'ui-design',
    'security-review',
    'code-quality',
)
EXPECTED_TEMPLATES = (
    'prd.md', 'srs.md', 'requirement-traceability-matrix.md',
    'system-design.md',
    'ui-ux-flow.md', 'task-breakdown.md',
    'ui-design-review.md',
    'security-review.md',
    'code-quality-review.md',
)
LINK_RE = re.compile(r'(?<!!)\[[^\]\n]+\]\((<[^>]+>|[^)]+)\)')
HEADING_RE = re.compile(r'^\s{0,3}#{1,6}\s+\S', re.MULTILINE)
NAME_RE = re.compile(r'^[a-z][a-z0-9]*(?:-[a-z0-9]+)*$')

@dataclass(frozen=True)
class Finding:
    severity: str
    path: str
    message: str


def strip_fences(content: str) -> str:
    result = []
    in_fence = False
    delimiter = ''
    for line in content.splitlines(keepends=True):
        match = re.match(r'^\s{0,3}(`{3,}|~{3,})', line)
        if match:
            marker = match.group(1)
            if not in_fence:
                in_fence = True
                delimiter = marker[0]
            elif marker[0] == delimiter:
                in_fence = False
            result.append('\n')
        elif in_fence:
            result.append('\n')
        else:
            result.append(line)
    return ''.join(result)


def frontmatter(content: str) -> dict[str, str] | None:
    lines = content.lstrip('\ufeff').splitlines()
    if not lines or lines[0].strip() != '---':
        return None
    values: dict[str, str] = {}
    key = None
    for line in lines[1:]:
        if line.strip() == '---':
            return values
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        match = re.match(r'^([A-Za-z][A-Za-z0-9_-]*):\s*(.*)$', line)
        if match:
            key = match.group(1)
            if key in values:
                return None
            values[key] = match.group(2).strip().strip('"\'')
        elif key and line[:1].isspace():
            if values[key] not in ('>', '|'):
                values[key] += ' ' + line.strip()
            else:
                values[key] = line.strip()
        else:
            return None
    return None


def link_target(raw: str) -> str:
    target = raw.strip()
    if target.startswith('<'):
        return target[1:].split('>', 1)[0]
    return target.split(maxsplit=1)[0]


def validate(root: Path, strict: bool = False) -> list[Finding]:
    root = root.resolve()
    findings: list[Finding] = []
    seen_names: dict[str, str] = {}

    def report(level: str, path: Path | str, message: str) -> None:
        label = path.as_posix() if isinstance(path, Path) else path
        findings.append(Finding(level, label, message))

    for item in CORE_FILES:
        if not (root / item).is_file():
            report('ERROR', item, 'Required framework document is missing')

    if strict:
        for skill in EXPECTED_SKILLS:
            path = Path('skills') / skill / 'SKILL.md'
            if not (root / path).is_file():
                report('ERROR', path, 'Expected skill is missing')
        for template in EXPECTED_TEMPLATES:
            path = Path('templates') / template
            if not (root / path).is_file():
                report('ERROR', path, 'Expected template is missing')

    markdown_files = sorted(root.rglob('*.md'))
    markdown_files = [p for p in markdown_files if not any(x in {'.git', '.venv', 'node_modules'} for x in p.relative_to(root).parts)]
    for file in markdown_files:
        relative = file.relative_to(root)
        content = file.read_text(encoding='utf-8-sig')
        visible = strip_fences(content)
        if not HEADING_RE.search(visible):
            report('WARNING', relative, 'No Markdown heading found')
        if file.name == 'SKILL.md' and 'skills' in relative.parts:
            metadata = frontmatter(content)
            if metadata is None:
                report('ERROR', relative, 'Missing or invalid YAML-style frontmatter')
            else:
                name = metadata.get('name', '')
                description = metadata.get('description', '').strip()
                if not NAME_RE.fullmatch(name):
                    report('ERROR', relative, 'Skill name must use lowercase kebab-case')
                elif name != file.parent.name:
                    report('ERROR', relative, 'Skill name does not match directory name')
                if not description or description in {'>', '|'}:
                    report('ERROR', relative, 'Skill description is empty')
                if name in seen_names:
                    report('ERROR', relative, f'Duplicate skill name in {seen_names[name]}')
                elif name:
                    seen_names[name] = relative.as_posix()
        for match in LINK_RE.finditer(visible):
            target = link_target(match.group(1))
            if not target or target.startswith(('#', 'mailto:', 'tel:')):
                continue
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or target.startswith('//'):
                continue
            if not parsed.path:
                continue
            destination = (file.parent / unquote(parsed.path)).resolve()
            if not destination.is_relative_to(root):
                report('WARNING', relative, f'Local link leaves repository: {target}')
            elif not destination.exists():
                report('ERROR', relative, f'Broken local link: {target}')
    return sorted(findings, key=lambda x: (x.path, x.severity, x.message))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument('--strict', action='store_true', help='Require the planned skills and templates')
    args = parser.parse_args()
    if not args.root.is_dir():
        parser.error(f'Not a directory: {args.root}')
    findings = validate(args.root, strict=args.strict)
    for finding in findings:
        print(f'{finding.severity}: {finding.path}: {finding.message}')
    errors = sum(f.severity == 'ERROR' for f in findings)
    warnings = sum(f.severity == 'WARNING' for f in findings)
    print(f'Validation complete: {errors} error(s), {warnings} warning(s)')
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
