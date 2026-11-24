# PREZEKC v0.3.0 — Engineering Quality Contract

This contract **extends**, never overrides, the v0.2.0 import-first PRD/SRS lifecycle, P01–P09 phase governance, and human approval gates.

## Engineering Quality Pillars

1. **Clean Architecture:** cohesive modules and explicit boundaries appropriate to project scale, not mandatory layering for every application.
2. **Modern Code:** version-compatible patterns, predictable error handling, type-safe APIs where supported, and justified dependency changes.
3. **Clean Code:** readable names, low needless complexity, clear responsibilities, useful abstractions, and behavior-preserving refactors.
4. **UI Quality:** preserve approved UX and design references; inspect interaction states, responsiveness, accessibility, and visual coherence.
5. **Defensive Security:** authorization, secrets, validation, storage, privacy, dependencies, and deployment configuration; assess only authorized scope.
6. **Evidence:** record checks actually executed and unresolved risks; no made-up scores, passing tests, or approvals.

## Routing

- UI layout or visual component: [`ui-design`](../skills/ui-design/SKILL.md) and existing `ui-ux-flow` when navigation behavior changes.
- Auth, sensitive data, API access, deployment security: [`security-review`](../skills/security-review/SKILL.md).
- New or changed code, refactoring, technical debt: [`code-quality`](../skills/code-quality/SKILL.md), alongside the relevant development/testing skills.
- Architecture boundary change: existing [`system-design`](../skills/system-design/SKILL.md) + code-quality; obtain owner approval for material redesign.

Load only applicable skills. These are *role instructions*, not autonomous agents or an installed scanner. A proposed refactor does not authorize itself.

## Quality Gate

For each material task report:

- Requirement and design baseline used (or `NOT_AVAILABLE`).
- Files changed and scope confirmation.
- Formatting, static analysis, unit/integration, device/UI, and defensive security checks **as relevant**.
- Each result: `PASS`, `FAIL`, `NOT_RUN`, or `BLOCKED`, plus command/tool and evidence.
- Review findings: `CONFIRMED`, `POTENTIAL`, or `NOT_ASSESSED` as applicable.
- Residual risk, owner decision needed, and one recommended next step.

`PASS` is not equivalent to `OWNER_APPROVED`. A linter or a file existence check cannot prove code is clean, secure, or correct. Do not publish credentials or sensitive user data in evidence.
