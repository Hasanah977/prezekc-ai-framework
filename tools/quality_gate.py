#!/usr/bin/env python3
"""Validate honest PREZEKC quality-evidence report structure, not software quality."""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

STATUSES = {'PASS', 'FAIL', 'NOT_RUN', 'BLOCKED'}


def check_report(value: object) -> list[str]:
    problems: list[str] = []
    if not isinstance(value, dict):
        return ['Report root must be a JSON object']
    for key in ('task_id', 'baseline', 'recommended_next_action'):
        if not isinstance(value.get(key), str) or not value[key].strip():
            problems.append(f'{key}: required non-empty string')
    for key in ('changed_files', 'open_risks'):
        if not isinstance(value.get(key), list) or any(not isinstance(x, str) for x in value.get(key, []) if isinstance(value.get(key), list)):
            problems.append(f'{key}: required list of strings')
    checks = value.get('checks')
    if not isinstance(checks, list) or not checks:
        problems.append('checks: required nonempty list of check objects')
        return problems
    for index, item in enumerate(checks, 1):
        prefix = f'checks[{index}]'
        if not isinstance(item, dict):
            problems.append(f'{prefix}: expected object')
            continue
        if not isinstance(item.get('name'), str) or not item['name'].strip():
            problems.append(f'{prefix}.name: required')
        status = item.get('status')
        if not isinstance(status, str) or status not in STATUSES:
            problems.append(f'{prefix}.status: must be one of {", ".join(sorted(STATUSES))}')
        evidence = item.get('evidence')
        if not isinstance(evidence, str) or not evidence.strip():
            problems.append(f'{prefix}.evidence: required, including for NOT_RUN/BLOCKED')
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description='Check PREZEKC quality-evidence report structure (not actual code quality)')
    parser.add_argument('report', type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.report.read_text(encoding='utf-8-sig'))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(f'ERROR: cannot read report: {exc}', file=sys.stderr)
        return 2
    errors = check_report(data)
    for item in errors:
        print(f'ERROR: {item}')
    if errors:
        print(f'Quality evidence structure: {len(errors)} error(s).')
        return 1
    print('Quality evidence structure: PASS (reported results have NOT been independently verified).')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
