#!/usr/bin/env python3
"""PREZEKC single-project bootstrap. Python standard library only.

Usage: python tools/prezekc.py init --project PATH
"""
from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

SOURCE_DIRS = ('agents', 'core', 'rules', 'skills', 'templates', 'workflows', 'tools', 'docs')
SOURCE_FILES = ('AGENTS.md', 'FRAMEWORK.md', 'README.md')
ENTRY = '''# PREZEKC — Project Agent Entry Point

This project uses PREZEKC as an engineering operating framework.

1. Read `.prezekc/framework/AGENTS.md` for authoritative operating constraints.
2. Read the relevant protocol in `.prezekc/framework/core/`.
3. Load only the role and `SKILL.md` needed for the current task.
4. Reuse approved PRD, SRS, SDD, and UI/UX Flow artifacts; do not regenerate them without permission.
5. Never fabricate approval, test results, stakeholder evidence, or project progress.
6. After meaningful task completion, provide actual verification, one recommended next action, and a decision question.
7. Do not modify `.prezekc/framework/` during ordinary application work.

If an instruction conflicts with project safety requirements, stop and ask the owner.
'''


def init(project: Path, source: Path) -> int:
    project = project.resolve()
    source = source.resolve()
    if not project.is_dir():
        print(f'ERROR: Project directory does not exist: {project}', file=sys.stderr)
        return 2
    if not (source / 'AGENTS.md').is_file() or not (source / 'tools' / 'validate_framework.py').is_file():
        print('ERROR: Run from an unpacked PREZEKC framework repository.', file=sys.stderr)
        return 2
    destination = project / '.prezekc' / 'framework'
    if destination.exists():
        print(f'ERROR: Framework target already exists; no files overwritten: {destination}', file=sys.stderr)
        return 2
    if project == source or source in project.parents or project in source.parents:
        print('ERROR: Source and target directories must be separate; no files copied.', file=sys.stderr)
        return 2
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.mkdir()
    try:
        for dirname in SOURCE_DIRS:
            source_dir = source / dirname
            if source_dir.is_dir():
                shutil.copytree(source_dir, destination / dirname,
                                ignore=shutil.ignore_patterns('__pycache__', '.pytest_cache', 'build', '*.pyc'))
        for filename in SOURCE_FILES:
            if (source / filename).is_file():
                shutil.copy2(source / filename, destination / filename)
    except Exception as exc:
        shutil.rmtree(destination, ignore_errors=True)
        print(f'ERROR: Bootstrap failed: {exc}', file=sys.stderr)
        return 2
    entry = project / 'AGENTS.md'
    if entry.exists():
        print('NOTICE: Existing root AGENTS.md preserved. Add PREZEKC reference manually.')
    else:
        entry.write_text(ENTRY, encoding='utf-8')
        print('CREATED: AGENTS.md')
    print(f'INSTALLED: {destination}')
    print('NEXT: Open only your project folder and ask the assistant to read AGENTS.md.')
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description='PREZEKC AI project bootstrap')
    sub = parser.add_subparsers(dest='command', required=True)
    p = sub.add_parser('init', help='Install PREZEKC reference into an existing project directory')
    p.add_argument('--project', required=True, type=Path, help='Existing target project directory')
    args = parser.parse_args(argv)
    if args.command == 'init':
        return init(args.project, Path(__file__).resolve().parents[1])
    return 2


if __name__ == '__main__':
    raise SystemExit(main())
