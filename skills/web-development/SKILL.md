---
name: web-development
description: >
  Implement and maintain web applications against approved
  software requirements and architecture. Use for frontend,
  backend, API, database, authentication, integration,
  responsive interfaces, and web application maintenance.
---

# Web Development

Implement web applications against the approved SRS and System
Design Specification. Preserve established interfaces, data
contracts, and existing behavior outside the assigned scope.

This skill operates within lifecycle phase `P07`.

## Preconditions

Before implementation, establish:

- Approved SRS and applicable requirement identifiers.
- Approved architecture or authorized maintenance baseline.
- Defined implementation scope and acceptance criteria.
- Existing repository state and technology stack.
- Available development and verification environments.

If a required baseline is missing, restrict work to an
explicitly authorized prototype or investigation.

Do not classify exploratory output as production-ready.

## Repository Inspection

Inspect the relevant project structure before editing.

Determine:

1. Application entry points and module boundaries.
2. Framework versions and dependency constraints.
3. Routing, middleware, and authorization conventions.
4. Database schemas and migration history.
5. API contracts and external integrations.
6. Existing tests and build commands.
7. Uncommitted changes affecting the task.

Follow established project conventions unless a deviation
is required and justified.

Do not replace an existing architecture merely because
another technology is more familiar.

## Implementation Procedure

### 1. Establish Change Scope

Map the assigned requirements to affected components.

Identify:

- Required behavior.
- Input and output contracts.
- Authorization constraints.
- Relevant database operations.
- Failure and exception conditions.
- Expected verification coverage.

Record any requirement that cannot be implemented without
changing an approved contract.

### 2. Implement Backend Behavior

Where applicable:

- Keep business rules within designated application layers.
- Validate untrusted input at appropriate boundaries.
- Enforce authorization independently of UI visibility.
- Preserve transactional consistency.
- Handle integration failures explicitly.
- Return consistent error responses.
- Avoid unnecessary changes to public interfaces.

Database operations must respect approved schema and
migration requirements.

### 3. Implement Frontend Behavior

Where applicable:

- Follow approved UI/UX specifications.
- Preserve semantic structure and accessibility.
- Implement required responsive behavior.
- Represent loading, empty, success, and error states.
- Keep client-side validation consistent with server rules.
- Avoid exposing privileged data or operations.
- Preserve existing design conventions.

Do not introduce visual redesigns outside the assigned scope.

### 4. Maintain Interface Contracts

Changes to an API, database schema, or shared component must
account for its consumers.

Before modifying a shared contract:

1. Identify dependent components.
2. Assess backward compatibility.
3. Verify authorization and data integrity effects.
4. Update affected tests and documentation.
5. Obtain approval for breaking changes.

### 5. Implement Tests

Add or update tests according to the affected requirements.

Prioritize:

- Business-rule correctness.
- Authorization boundaries.
- Input validation.
- Data consistency.
- API contract behavior.
- Failure handling.
- Regression coverage.

Avoid tests that merely reproduce implementation details.

## Verification

Execute the applicable checks supported by the project.

Recommended order:

1. Formatting and static analysis.
2. Syntax or type checking.
3. Focused automated tests.
4. Integration tests.
5. Application build.
6. Browser and responsive verification.
7. Relevant security and regression checks.

Record the actual commands and results.

Do not report checks as passed if they were not executed.

A successful build does not establish complete functional
conformance.

## Change Discipline

- Prefer the smallest complete change.
- Preserve unrelated behavior.
- Do not overwrite uncommitted user changes.
- Do not introduce unnecessary dependencies.
- Do not commit credentials or sensitive data.
- Do not modify production resources without authorization.
- Do not substitute mock data for required real data.
- Do not claim runtime verification from source inspection.

When implementation reveals a requirements defect, report
the conflict through the established change-control process.

## Deliverables

Provide:

- Implemented source changes.
- Updated tests where applicable.
- Relevant configuration or migration changes.
- Requirement-to-implementation references.
- Verification results.
- Known limitations.

Each deliverable must identify its applicable requirement
baseline.

## Completion Criteria

The assigned scope is complete when:

- Required behavior has been implemented.
- Applicable interfaces remain consistent.
- Relevant tests and checks have acceptable results.
- No unresolved mandatory verification failures remain.
- Requirement traceability has been updated.
- Limitations and pending checks are disclosed.

Owner approval remains subject to the governance protocol.

## Failure Handling

Stop the affected operation when:

- Required authority is unavailable.
- Approved specifications conflict.
- A destructive operation lacks authorization.
- The change requires unapproved scope expansion.
- Critical dependencies prevent safe implementation.

Preserve completed work and report the blocking condition.

## Handoff

Transfer the implementation to the Verification Engineer
with the affected requirements, changed artifacts, executed
checks, evidence, and unresolved findings.

Do not assign `PASS` to unexecuted verification.

## Governing Specifications

- [Agent Contract](../../AGENTS.md)
- [Development Engineer](../../agents/development-engineer.md)
- [Governance](../../core/governance.md)
- [Workflow](../../core/workflow.md)
- [Verification](../../core/verification.md)

<!-- PREZEKC-V030-EXTENSION: DO NOT DUPLICATE -->
## v0.3.0 — Modern Web Code Quality

Verify actual language/framework/runtime versions before coding. Follow established project conventions, separation of concerns, safe input handling, and scoped updates. Activate [code-quality](../code-quality/SKILL.md) for substantive code changes, [ui-design](../ui-design/SKILL.md) for screen changes, and [security-review](../security-review/SKILL.md) for auth, sensitive data, public APIs, or deployment-risk changes. Run relevant checks, do not invent test results, and avoid unapproved UI redesign or dependencies.
