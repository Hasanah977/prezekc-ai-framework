# PREZEKC v0.3.0 — Engineering Quality Guide

PREZEKC's goal is **controlled, maintainable software engineering with an AI coding assistant**, not generating the largest possible volume of code.

## What stays unchanged

- P01–P09 and the six engineering role contracts.
- Import-first PRD/SRS and separate human approval gates.
- SDD / UI/UX Flow → Task Breakdown → implementation → verification.
- The owner decides when to move between material phases and accepts significant refactors.

## What v0.3.0 adds

- [`ui-design`](../skills/ui-design/SKILL.md): visual direction, component states, accessibility and responsive review.
- [`security-review`](../skills/security-review/SKILL.md): authorized defensive review and risk evidence.
- [`code-quality`](../skills/code-quality/SKILL.md): clean architecture, modern stack practices, safe refactoring and maintainability.
- [`core/engineering-quality.md`](../core/engineering-quality.md): shared quality/evidence rules.
- [`quality_gate.py`](../tools/quality_gate.py): a lightweight checker for **evidence reports**, not a security analyzer.

## Application Examples

### A. Build a login feature

1. Locate the approved SRS and UI flow for login; identify roles and validation.
2. Inspect auth architecture and current dependencies.
3. Use web/mobile-development plus `code-quality`; apply `ui-design` for changed screens and `security-review` for auth risks.
4. Implement the authorized task, add tests, and run available checks.
5. Record evidence, remaining risks, and request the next user decision.

### B. Repair an existing AI-generated application

1. Inspect repository **read-only**. Identify current stack, tests, entry points and design decisions.
2. Report evidence-backed issues, priorities and a small improvement plan.
3. Obtain approval before restructuring modules or changing externally visible behavior.
4. Refactor in small increments with regression tests; explain the results in plain Indonesian if the user uses Indonesian.

## Quality Evidence JSON

A JSON report can use this simple schema:

```json
{
  "task_id": "TASK-014",
  "baseline": "SRS-1.0 / SDD-1.0",
  "changed_files": ["lib/features/auth/login_page.dart"],
  "checks": [
    {"name": "Static analysis", "status": "PASS", "evidence": "flutter analyze: no issues"},
    {"name": "Device test", "status": "NOT_RUN", "evidence": "No device available"}
  ],
  "open_risks": ["Real-device behavior not verified"],
  "recommended_next_action": "Run login tests on an Android device"
}
```

Illustrative entries above are **not actual test results**.

Run the report structure validator:

```powershell
python tools/quality_gate.py path/to/quality-report.json
```

It checks honest status/evidence formatting. It **does not** execute tests, check UI visually, audit security, or approve release.
