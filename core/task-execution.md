# Task Execution and Evidence Contract

> PREZEKC AI Framework v0.2.0 — Execution protocol

## Task Entry

Resolve the task objective, authorized scope, requirements, design/flow references, file ownership, existing changes, relevant skill, and verification method. Prefer the smallest complete change; do not read or rewrite unrelated documents.

## Execution Sequence

1. **Inspect** repository state and required references.
2. **Plan** the task and identify risks, unresolved decisions, and expected verification.
3. **Authorize** any scope extension, destructive operation, or other gated decision.
4. **Implement** within the authorized file/component scope, preserving user changes.
5. **Verify** with real checks that are available and applicable.
6. **Report and hand off** using [Human-Guided Next Action Protocol](next-action.md).

## Evidence States

`PASS`: test was run and met its criteria.

`FAIL`: test ran but did not meet criteria.

`NOT_RUN`: verification was not performed.

`BLOCKED`: prerequisite was unavailable or prevented the check.

`NOT_APPLICABLE`: check does not apply and justification is recorded.

Use the distinction in [Verification Protocol](verification.md): a successful check is not owner approval.

## Minimum Task Record

```yaml
id: TASK-001
status: READY_FOR_REVIEW
requirements: [SRS-FR-001.1]
changed_files: []
verification:
  - check: unit_tests
    status: NOT_RUN
    evidence: "Not executed"
owner_approval: PENDING
```

A sample is illustrative and is not a validated record of a real project.
