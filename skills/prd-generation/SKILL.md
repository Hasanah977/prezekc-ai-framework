---
name: prd-generation
description: >
  Produce a structured Product Requirements Document from validated
  stakeholder needs, system analysis, comparative findings, and
  project constraints. Use when defining product goals, scope,
  target users, capabilities, priorities, user stories, and
  acceptance outcomes. Preserves requirement provenance and
  prepares a controlled PRD baseline for SRS engineering.
version: 0.1.0
category: requirements-engineering
---

# Product Requirements Engineering

## Purpose

Transform analyzed stakeholder needs into a coherent,
reviewable Product Requirements Document (PRD).

The PRD defines the intended product, the problems it
addresses, and the outcomes it must achieve.

It must not prescribe implementation details unless
they are explicit product or operational constraints.

This skill implements Phase P04 of the PREZEKC AI
engineering lifecycle.

## Activation

Use this skill when:

- Creating a PRD for a new software product.
- Formalizing product requirements from analysis.
- Defining product scope and feature priorities.
- Preparing product requirements for stakeholder review.
- Revising an existing PRD under change control.

Do not activate this skill to generate an SRS,
select a system architecture, or implement software.

For technical requirement decomposition, use
`prd-to-srs` after PRD approval.

## Preconditions

The following information must be available:

- Project objectives and problem context.
- Identifiable stakeholder or user needs.
- Requirements analysis or equivalent evidence.
- Scope constraints and known dependencies.

Preferred inputs:

- Existing System Analysis Report.
- Comparative Study Report.
- Requirement Analysis Document.
- Requirement Inventory.
- Stakeholder Register.
- Business Rule Register.

Missing upstream artifacts must be reported.

Do not fabricate system analysis, interviews,
comparative findings, or stakeholder approval.

## Source Integrity

Every significant product requirement must reference
an identifiable need, business rule, or approved decision.

Permitted source references include:

- `NEED-*`
- `REQ-*`
- `BUS-*`
- `PROB-*`
- `GAP-*`
- Approved stakeholder decisions.

Research gaps may motivate product investigation,
but they do not independently establish product demand.

## Procedure

### PRD01 — Resolve Product Context

Establish:

1. Product purpose.
2. Target users.
3. Stakeholder objectives.
4. Current problems.
5. Operating environment.
6. Known constraints.
7. Expected outcomes.

Separate verified facts from proposed assumptions.

### PRD02 — Define Product Outcomes

Translate stakeholder needs into product goals.

Each goal should explain:

- What outcome is required.
- Who benefits.
- Why the outcome matters.
- How success may be evaluated.

Do not invent numerical success targets.

If measurable thresholds are unavailable, mark
them as requiring stakeholder definition.

### PRD03 — Establish Scope

Define:

- In-scope capabilities.
- Explicit exclusions.
- External dependencies.
- Operational constraints.
- Release boundaries.

Scope must reflect documented needs and
authorized project decisions.

Unapproved capabilities remain proposals.

### PRD04 — Identify Product Capabilities

Consolidate validated needs into product-level
capabilities without losing source references.

Use stable identifiers:

```text
PRD-FR-001
PRD-FR-002
PRD-FR-003
```

Product-level quality requirements use:

```text
PRD-NFR-001
PRD-NFR-002
```

Do not reuse identifiers for unrelated requirements.

### PRD05 — Define Requirement Records

Each product requirement must contain:

```yaml
id: PRD-FR-001
title: "Product capability"
statement: "Required product outcome"
source_ids:
  - REQ-001
target_users: []
priority: UNASSESSED
rationale: "Reason for the requirement"
acceptance_outcomes: []
dependencies: []
status: PROPOSED
```

Requirement statements must remain understandable
without referencing implementation source code.

### PRD06 — Establish User Stories

Where appropriate, represent user interactions
using the following structure:

```text
As a <user role>,
I want <capability>,
so that <expected benefit>.
```

User stories must support documented requirements.

Do not use user stories as substitutes for
business rules or acceptance criteria.

### PRD07 — Prioritize Requirements

Use the prioritization method established during
requirement analysis.

When MoSCoW is used:

- `MUST`
- `SHOULD`
- `COULD`
- `WONT_NOW`

Preserve stakeholder rationale.

Dependencies and mandatory regulatory obligations
must be considered before assigning priorities.

### PRD08 — Define Acceptance Outcomes

Each required capability must have observable
product-level acceptance outcomes.

Acceptance outcomes should describe what must
be achieved, not prescribe internal implementation.

Avoid vague statements such as:

- "The application must be excellent."
- "The interface should be modern."
- "The system should work perfectly."

Replace them with verifiable outcomes or
record the missing acceptance decision.

### PRD09 — Identify Risks and Assumptions

Record:

- Product risks.
- External dependencies.
- Unresolved business decisions.
- Evidence gaps.
- Feasibility assumptions.
- Scope limitations.

A risk is not automatically a requirement.

### PRD10 — Assemble the Document

Use `templates/prd.md` as the document structure.

Preserve:

- Requirement identifiers.
- Source references.
- Approval status.
- Document version.
- Unresolved decisions.

Do not silently omit unsupported sections.

### PRD11 — Validate the PRD

Check:

1. Objective and scope consistency.
2. Stakeholder coverage.
3. Source traceability.
4. Requirement completeness.
5. Identifier uniqueness.
6. Priority consistency.
7. Acceptance outcome quality.
8. Contradictions and ambiguities.
9. Unsupported capability additions.
10. Open issues.

Apply the PRD verification gate defined in
`core/verification.md`.

### PRD12 — Submit for Approval

Set the document to `IN_REVIEW` when ready.

Only the designated human owner may establish
the `APPROVED` baseline.

A verified draft remains unapproved until the
owner's decision is recorded.

## Output Contract

Primary artifact:

`Product Requirements Document`

Supporting artifacts:

- Product Requirement Register.
- Product Scope Register.
- Requirement Source Mapping.
- PRD Verification Report.
- Open Decision Register.

The document must identify its source analysis
and current approval status.

## Quality Gate

The PRD is ready for review when:

- [ ] The product problem is clearly defined.
- [ ] Goals are aligned with stakeholder needs.
- [ ] Target users are identifiable.
- [ ] Scope and exclusions are explicit.
- [ ] Capabilities have stable identifiers.
- [ ] Product requirements have valid sources.
- [ ] Priorities and dependencies are documented.
- [ ] Acceptance outcomes are observable.
- [ ] Assumptions and risks are disclosed.
- [ ] Material contradictions are resolved or flagged.
- [ ] No unsupported product scope has been introduced.

A passing quality gate permits submission for review.
It does not establish approval.

## Failure Handling

Return `BLOCKED` for baseline approval when:

- Critical stakeholder needs cannot be established.
- Product scope is materially contradictory.
- Required business decisions are missing.
- Mandatory requirements lack legitimate origins.

Return `PARTIAL` when a draft can be prepared
but important validation remains outstanding.

Preserve unresolved questions in the output.

## Example

Source need:

```yaml
need_id: NEED-001
statement: >
  Authorized reporting personnel need access
  to consolidated records.
validation_status: VALIDATED
```

Derived product requirement:

```yaml
id: PRD-FR-001
title: "Consolidated Record Access"
statement: >
  The product shall enable authorized reporting
  personnel to access consolidated records
  for a selected reporting period.
source_ids:
  - NEED-001
priority: UNASSESSED
acceptance_outcomes:
  - >
    Authorized reporting personnel can retrieve
    records associated with a selected period.
status: PROPOSED
```

This requirement does not prescribe the database,
API framework, programming language, or UI library.

## Handoff

Next skill:

`prd-to-srs`

Required handoff:

```yaml
skill: prd-generation
artifact: PRD
version: "0.1"
approval_status: IN_REVIEW
verification_status: NOT_RUN
requirement_ids: []
open_issues: []
```

Replace example values with actual project records.

Do not request final SRS decomposition until
the PRD baseline has been approved.

## Governing Specifications

- [Agent Operating Contract](../../AGENTS.md)
- [Requirements Engineer](../../agents/requirements-engineer.md)
- [Governance Protocol](../../core/governance.md)
- [Workflow Protocol](../../core/workflow.md)
- [Verification Protocol](../../core/verification.md)
