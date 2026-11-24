---
name: code-quality
description: >
  Review and improve clean code, modern stack-appropriate coding practices,
  architecture boundaries, maintainability, and safe refactoring with
  concrete tests and minimal authorized changes.
version: 0.3.0
category: development
---

# Clean Code, Modern Code & Safe Refactoring

## Purpose

Help developers produce maintainable software **without turning style preferences into blanket rewrites**. Clean Architecture is a context-sensitive design principle, not one prescribed folder layout.

## Activate When

- Reviewing changed code, preparing a nontrivial implementation, resolving maintainability issues, or refactoring.
- An existing AI-generated codebase requires assessment before changes.
- The user requests clean architecture, modern conventions, code review, or code simplification.

## Procedure

1. **Read narrowly:** discover relevant file names and call sites; read only necessary code and established repository conventions.
2. **Verify environment:** identify language/framework versions and supported APIs. Do not assume the latest syntax fits the project.
3. **Map behavior:** record current tests and invariants; locate the SRS, SDD, and task references, if available.
4. **Assess architecture:** module responsibilities, domain/application/infrastructure boundaries where useful, dependency direction, coupling, data ownership, and test seams. Avoid needless layers or abstractions.
5. **Assess code quality:** naming, cohesion, duplicated logic, complexity, error handling, type safety, testability, configuration, and deprecated APIs verified against the project's versions.
6. **Report a prioritized plan:** classify `BLOCKER`, `IMPORTANT`, or `OPTIONAL` and justify each recommendation with code evidence; do not change the whole repository by default.
7. **Approve significant refactors:** describe scope, risk, rollback plan, and how existing behavior will be protected.
8. **Implement in small units:** maintain public behavior unless change is explicitly authorized. Add characterization/regression tests where appropriate; TDD is encouraged for testable behavioral changes, not mandated for every edit.
9. **Run actual checks:** formatter, static analysis, tests, build, relevant integration and UI checks; record `NOT_RUN` when unavailable.
10. **Handoff:** summarize file changes, evidence, residual risk, and one recommended next step per [`core/next-action.md`](../../core/next-action.md).

## Quality Rules

- Prefer understandable code to clever code.
- Do not refactor solely to match one fashionable pattern.
- Do not claim 'modern' without checking toolchain compatibility.
- Do not claim a green test suite proves maintainability or architectural correctness.
- Never remove user customizations, approved design, or features to satisfy stylistic preferences.

## Output

Use [`templates/code-quality-review.md`](../../templates/code-quality-review.md). Keep traceability to requirements and the authorized task.
