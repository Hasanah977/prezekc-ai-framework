---
name: prd-to-srs
description: >
  Transform an approved Product Requirements Document into a
  testable Software Requirements Specification. Use when
  decomposing product requirements into functional and
  non-functional system requirements, defining system behavior,
  detecting requirements gaps, and creating a traceability matrix.
  Requires an approved PRD baseline for final SRS generation.
version: 0.1.0
category: requirements-engineering
---

# PRD-to-SRS Requirements Engineering

## Purpose

Derive a complete and verifiable Software Requirements
Specification (SRS) from an approved PRD baseline.

Preserve product intent while defining observable
system behavior, constraints, interfaces, validation,
and acceptance criteria.

This skill implements Phase P05 of the PREZEKC AI lifecycle.

Transformation is controlled requirements decomposition,
not unrestricted rewriting.

## Activation

Use this skill when:

- Deriving an SRS from an approved PRD.
- Decomposing product capabilities into system behavior.
- Specifying functional and non-functional requirements.
- Establishing PRD-to-SRS traceability.
- Reviewing SRS coverage against a product baseline.
- Revising an SRS after an approved PRD change.

Do not use this skill to invent product features,
approve requirements, or directly implement software.

## Preconditions

Required for a controlled SRS baseline:

- Approved PRD.
- Identifiable PRD version.
- Recorded approval authority.
- Stable PRD requirement identifiers.
- Applicable business rules and constraints.

Conditional inputs:

- Requirement Analysis Document.
- Data and integration requirements.
- System context.
- Security and privacy obligations.
- Existing SRS baseline.
- Approved change requests.

If PRD approval is missing, the agent may prepare
a provisional specification when requested.

Such output must be labeled `DRAFT` and must not
be used as a final approved baseline.

## Transformation Invariants

The transformation must preserve the following:

1. Every mandatory PRD requirement is accounted for.
2. Every SRS requirement has an authorized origin.
3. SRS requirements do not contradict approved product intent.
4. Requirement identifiers are stable and unique.
5. Each system requirement is objectively verifiable.
6. Missing decisions are visible rather than invented.
7. New product capabilities require change control.
8. Approval and verification remain separate.

A single PRD requirement may produce multiple SRS requirements.

An SRS requirement may trace to multiple PRD requirements.
Store those relationships explicitly.

## Procedure

### SRS01 — Validate PRD Baseline

Inspect:

- PRD identifier and version.
- Approval record.
- Requirement inventory.
- Product scope.
- Exclusions.
- Business rules.
- Outstanding decisions.

Do not continue to final SRS generation if an
essential prerequisite is missing.

### SRS02 — Extract Approved Requirements

Create a source requirement inventory.

For each requirement, retain:

- Requirement ID.
- Statement.
- Rationale.
- Priority.
- Source references.
- Acceptance outcomes.
- Dependencies.
- Approval status.

Do not modify the wording of the approved PRD
while extracting its requirements.

### SRS03 — Establish System Boundary

Define the system context relevant to the PRD.

Identify:

- Actors and user roles.
- External systems.
- Data exchanges.
- System responsibilities.
- Operational constraints.
- Trust and authorization boundaries.

Distinguish system responsibility from
responsibilities belonging to external services.

### SRS04 — Decompose Functional Requirements

For each applicable PRD capability, identify:

1. Trigger or initiating event.
2. Participating actor.
3. Preconditions.
4. Required input.
5. Processing rules.
6. Observable output.
7. Validation behavior.
8. Error conditions.
9. Authorization requirements.
10. Postconditions.

Create system-level requirements only when
their behavior is justified by the parent PRD
or an approved technical constraint.

### SRS05 — Define Atomic Requirements

Prefer requirements expressing one independently
verifiable behavior.

Use the convention:

```text
SRS-FR-001.1
SRS-FR-001.2
SRS-FR-001.3
```

Each requirement must contain:

```yaml
id: SRS-FR-001.1
title: "Requirement title"
statement: "The system shall..."
parent_requirements:
  - PRD-FR-001
actors: []
preconditions: []
inputs: []
expected_behavior: null
outputs: []
error_conditions: []
acceptance_criteria: []
verification_method: TEST
status: DRAFT
```

Do not assign a passing verification status
to a requirement that has not been examined.

### SRS06 — Define Non-Functional Requirements

Evaluate relevant quality attributes:

- Performance.
- Availability.
- Reliability.
- Security.
- Privacy.
- Accessibility.
- Usability.
- Compatibility.
- Maintainability.
- Data integrity.
- Recoverability.

Use the identifier convention:

```text
SRS-NFR-001
SRS-NFR-002
```

A non-functional requirement must specify
an objectively assessable property.

When thresholds or measurements are required,
record:

- The target.
- Measurement conditions.
- Evaluation method.
- Approved origin of the target.

Do not invent numerical service levels.

If a target is unknown, register an open decision
instead of presenting an arbitrary value.

### SRS07 — Specify Interfaces and Data

Define requirements governing:

- User interfaces.
- External APIs.
- System integrations.
- Data validation.
- Data access.
- Data retention.
- Import and export.
- Error responses.

Avoid prematurely prescribing internal architecture.

Interface implementation decisions belong to
System Design unless explicitly constrained by
approved requirements.

### SRS08 — Specify Business Rules

Preserve approved rules and their source references.

Each significant rule should identify:

- Rule ID.
- Origin.
- Condition.
- Required behavior.
- Exceptions.
- Related SRS requirements.

Do not invent eligibility, approval,
calculation, or access policies.

### SRS09 — Define Acceptance Criteria

For each requirement, define observable
conditions that establish conformance.

Acceptance criteria must be:

- Specific.
- Reproducible.
- Consistent.
- Technically feasible.
- Traceable to the requirement.

Test cases may be derived later.
Do not claim tests exist unless their artifacts
have actually been produced.

### SRS10 — Construct Traceability

Build a Requirement Traceability Matrix.

Use `templates/requirement-traceability-matrix.md`
when available.

Track relationships across:

```text
PRD Requirement
       |
       v
SRS Requirement
       |
       v
Design Element
       |
       v
Implementation
       |
       v
Test Case
```

During SRS generation, design, implementation,
and test references may remain `PENDING`.

Do not invent downstream artifact identifiers
to produce an apparently complete matrix.

### SRS11 — Detect Requirement Defects

Inspect for:

- Uncovered PRD requirements.
- Orphan SRS requirements.
- Duplicate identifiers.
- Contradictory requirements.
- Untestable statements.
- Unsupported quality targets.
- Missing failure conditions.
- Unauthorized scope expansion.
- Inconsistent business rules.
- Unresolved technical assumptions.

Record findings in an unresolved requirement register.

### SRS12 — Handle Scope Changes

When decomposition reveals a product capability
not covered by the approved PRD:

1. Record the proposed capability.
2. Identify its justification.
3. Assess possible impact.
4. Create a change request.
5. Request owner approval.
6. Update the PRD baseline if approved.
7. Repeat affected decomposition and validation.

Do not silently add the capability to the SRS.

### SRS13 — Produce the SRS

Use `templates/srs.md`.

The document must reference:

- Source PRD baseline.
- Requirements inventory.
- Business rules.
- Applicable constraints.
- Traceability matrix.
- Open issues.
- Verification status.
- Approval status.

### SRS14 — Execute SRS Quality Gate

Apply the SRS verification requirements
defined in `core/verification.md`.

A passing quality gate indicates that the
document is ready for human review.

It does not establish owner approval.

## Output Contract

Primary artifacts:

- Software Requirements Specification.
- Requirement Traceability Matrix.

Supporting artifacts:

- SRS Requirement Register.
- Requirement Coverage Report.
- Unresolved Requirement Register.
- Change Impact Report.
- SRS Verification Report.

All artifacts must reference the same
approved PRD baseline.

## Quality Gate

The SRS is ready for approval review when:

- [ ] Source PRD approval is recorded.
- [ ] PRD requirements have stable identifiers.
- [ ] Mandatory PRD requirements have SRS coverage.
- [ ] Every SRS requirement has a legitimate origin.
- [ ] Functional behavior is observable.
- [ ] Non-functional requirements are objectively assessable.
- [ ] Validation and failure behavior are documented.
- [ ] Business rules and interfaces are consistent.
- [ ] Requirements are independently testable.
- [ ] Duplicate identifiers are absent.
- [ ] Unapproved scope additions are absent.
- [ ] Traceability mappings are valid.
- [ ] Unresolved issues are reported.
- [ ] Applicable verification checks pass.

The `APPROVED` document state requires human acceptance.

## Failure Handling

Return `BLOCKED` for finalization when:

- The approved PRD baseline is unavailable.
- Mandatory source requirements conflict.
- Critical business rules are unresolved.
- Unauthorized scope expansion is necessary.
- Mandatory traceability cannot be established.

Return `PARTIAL` when useful decomposition is possible
but essential validation remains incomplete.

Do not replace missing requirements with
assumptions disguised as system behavior.

## Worked Example

Approved PRD requirement:

```yaml
id: PRD-FR-001
statement: >
  Authorized reporting personnel can access
  consolidated records for a selected period.
status: APPROVED
```

Derived SRS requirements:

```yaml
id: SRS-FR-001.1
statement: >
  The system shall allow authorized reporting
  personnel to select an available reporting period.
parent_requirements:
  - PRD-FR-001
status: DRAFT
```

```yaml
id: SRS-FR-001.2
statement: >
  The system shall retrieve consolidated records
  corresponding to the selected reporting period.
parent_requirements:
  - PRD-FR-001
status: DRAFT
```

```yaml
id: SRS-FR-001.3
statement: >
  The system shall deny retrieval requests from
  users without reporting access authorization.
parent_requirements:
  - PRD-FR-001
status: DRAFT
```

These examples are illustrative specifications.
They are not records of a real approved project.

## Handoff

Next phase:

`system-design`

Handoff contract:

```yaml
skill: prd-to-srs
source_artifact: PRD
source_version: "1.0"
output_artifacts:
  - SRS
  - RTM
srs_status: IN_REVIEW
verification_status: NOT_RUN
unresolved_requirements: []
approved_by: null
```

Final system design must use an approved SRS.

## Governing Specifications

- [Agent Operating Contract](../../AGENTS.md)
- [Requirements Engineer](../../agents/requirements-engineer.md)
- [Governance Protocol](../../core/governance.md)
- [Workflow Protocol](../../core/workflow.md)
- [Verification Protocol](../../core/verification.md)

<!-- PREZEKC-V020-EXTENSION: DO NOT DUPLICATE -->
## v0.2.0 — Import-First SRS/RTM Operating Mode

**Default when SRS or RTM exists: `IMPORT`.** Confirm the PRD baseline is actually approved. Review external SRS/RTM against the approved PRD, preserve identifiers and versions, and check behavior, validation, error handling, authorization, nonfunctional requirements, and bidirectional mapping. See [Import-First Guide](../../docs/import-mode.md).

**Optional `AUTHOR` mode:** Derive a draft SRS/RTM from an approved PRD only when requested; do not regenerate documents that the owner supplied. A provisional specification must remain `DRAFT` without PRD approval. `REVISE` follows controlled baseline change procedures.

Use the existing extractor and validator for supported Markdown/JSON structure; a green result is not semantic correctness or human approval. SRS must be separately owner-approved before it becomes the controlled P06 baseline. Apply [Next Action Protocol](../../core/next-action.md) at handoff.
