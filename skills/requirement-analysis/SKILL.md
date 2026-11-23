
---
name: requirement-analysis
description: >
  Elicit, analyze, classify, prioritize, and validate stakeholder,
  business, functional, data, and quality needs. Use when identifying
  system requirements, reviewing user needs, resolving requirement
  conflicts, prioritizing capabilities, defining scope, or preparing
  evidence-backed input for a Product Requirements Document (PRD).
  Produces a Requirement Analysis Document and requirement inventory.
version: 0.1.0
category: requirements-engineering
---

# Requirement Analysis

## Purpose

Transform documented problems, research findings, and
stakeholder input into a structured inventory of needs
that can support product requirements engineering.

This skill establishes what the project needs to achieve
before determining how the software will implement it.

The output provides the evidence and requirement baseline
candidates for PRD generation.

This skill supports Phase P03 of the PREZEKC AI lifecycle.

## When to Use

Activate this skill when:

- Analyzing stakeholder needs.
- Identifying business and user requirements.
- Defining scope and operational constraints.
- Prioritizing proposed capabilities.
- Resolving conflicting requirements.
- Preparing requirements for PRD development.
- Reviewing an existing requirements inventory.

Do not use this skill to generate final SRS specifications
or make architectural decisions.

Use `prd-generation` after the requirements have been
analyzed and reviewed.

## Required Context

Required inputs:

| Input | Requirement |
|---|---|
| Project objective | The outcome the project is intended to support |
| Problem evidence | Identified operational or user problems |
| Stakeholder context | Relevant users and decision owners |
| Available constraints | Known scope and operational boundaries |

Preferred upstream artifacts:

- Existing System Analysis Report.
- Comparative Study Report.
- Problem Register.
- Stakeholder Register.
- Research Gap Register.

Direct stakeholder input may supplement these artifacts.

Missing upstream reports do not justify inventing findings.

## Requirement Sources

Use explicit source classifications:

- `STAKEHOLDER`: Interview, workshop, or direct input.
- `SYSTEM_ANALYSIS`: Current-state problem evidence.
- `COMPARATIVE_STUDY`: Relevant research findings.
- `POLICY`: Documented organizational or regulatory rule.
- `TECHNICAL_CONSTRAINT`: Verified system limitation.
- `APPROVED_DECISION`: Recorded project-owner decision.

Comparative findings may justify investigation but do
not independently establish stakeholder demand.

## Workflow

### Step 1 — Establish Requirements Scope

Identify:

- Project objectives.
- In-scope processes.
- Out-of-scope activities.
- Relevant stakeholder groups.
- Existing system constraints.
- Dependencies and unresolved decisions.

Document the source of each scope boundary.

### Step 2 — Consolidate Source Findings

Review available upstream artifacts.

Extract:

- Confirmed operational problems.
- Stakeholder concerns.
- Business objectives.
- Observed process constraints.
- Research gaps.
- Relevant policy obligations.

Remove duplicate statements without losing
their original source references.

Preserve conflicts for explicit review.

### Step 3 — Identify Stakeholder Needs

Define needs in terms of outcomes and activities.

For every need, record:

- Stable identifier.
- Stakeholder.
- Need statement.
- Problem or objective.
- Source reference.
- Expected outcome.
- Current validation status.

Use the identifier convention:

```text
NEED-001
NEED-002
NEED-003
```

Do not immediately translate every need
into a specific UI screen or technology.

### Step 4 — Identify Business Rules

Extract documented rules governing the process.

Examples of rule categories:

- Eligibility.
- Authorization.
- Approval.
- Validation.
- Calculation.
- Workflow transitions.
- Record retention.
- Audit requirements.

Assign stable identifiers:

```text
BUS-001
BUS-002
```

Business rules must have an identifiable
source or recorded approval.

### Step 5 — Classify Requirement Candidates

Classify requirements into:

| Classification | Purpose |
|---|---|
| `BUSINESS` | Organizational outcome or obligation |
| `USER` | Stakeholder task or expected outcome |
| `FUNCTIONAL` | Candidate system capability |
| `QUALITY` | Required quality characteristic |
| `DATA` | Information collection or management need |
| `INTERFACE` | External interaction or integration need |
| `CONSTRAINT` | Limitation affecting the solution |

A requirement may have multiple related concerns,
but its primary classification must be explicit.

### Step 6 — Establish Requirement Records

Use a structured inventory.

```yaml
requirement_id: REQ-001
title: "Requirement title"
type: USER
statement: "Required stakeholder outcome"
source_ids:
  - NEED-001
stakeholders: []
priority: UNASSESSED
validation_status: PROPOSED
dependencies: []
acceptance_outcome: null
assumptions: []
```

`REQ-*` identifiers are provisional analysis IDs.

Approved PRD requirements receive their own
`PRD-FR-*` or `PRD-NFR-*` identifiers.

Preserve the relationship between analysis
requirements and subsequent PRD requirements.

### Step 7 — Prioritize Requirements

Use an agreed prioritization method.

MoSCoW may be used when appropriate:

- `MUST`: Essential for the agreed project outcome.
- `SHOULD`: Important but not essential for the first release.
- `COULD`: Useful when scope and resources permit.
- `WONT_NOW`: Excluded from the current delivery scope.

Evaluate priorities using:

- Stakeholder impact.
- Problem severity.
- Business value.
- Dependencies.
- Legal or policy obligations.
- Implementation feasibility.
- Resource constraints.

Do not classify a requirement as `MUST`
solely because it was suggested by an AI agent.

Record prioritization rationale.

### Step 8 — Analyze Dependencies and Conflicts

Identify:

- Requirements depending on other capabilities.
- Contradictory stakeholder expectations.
- Conflicting business rules.
- Incompatible data requirements.
- Scope inconsistencies.
- Unresolved decisions.
- Resource or feasibility constraints.

Assign an issue identifier to unresolved findings.

```text
ISSUE-001
ISSUE-002
```

A contradiction must not be silently resolved
through an arbitrary implementation choice.

### Step 9 — Assess Feasibility and Risk

Assess potential constraints involving:

- Technical feasibility.
- Operational change.
- Data availability.
- Security and privacy.
- Integration dependencies.
- Maintenance burden.
- Platform compatibility.
- Team capability.
- Regulatory requirements.

Record assessments as provisional when detailed
technical evaluation has not yet occurred.

Do not invent budgets, deadlines, or performance targets.

### Step 10 — Define Acceptance Outcomes

Each requirement candidate should have an observable
outcome that demonstrates its intended value.

Example:

Need:

"Authorized personnel need access to consolidated records."

Possible acceptance outcome:

"An authorized user can retrieve the approved consolidated
record for the selected reporting period."

The outcome does not yet prescribe an API endpoint,
database schema, or implementation technology.

Technical acceptance criteria are refined during
PRD and SRS engineering.

### Step 11 — Validate With Stakeholders

Review:

1. Requirement meaning.
2. Business relevance.
3. Priority.
4. Source accuracy.
5. Scope alignment.
6. Dependencies.
7. Conflicting expectations.
8. Acceptance outcomes.

Record decisions and unresolved feedback.

A proposed requirement must not be marked approved
merely because no objection was received.

### Step 12 — Produce the Analysis Document

Required structure:

```text
Requirement Analysis Document
├── Document Control
├── Project Objectives
├── Scope and Constraints
├── Source and Evidence Register
├── Stakeholder Analysis
├── Problem-to-Need Mapping
├── Business Rules
├── Requirement Inventory
├── Requirement Classification
├── Prioritization
├── Dependencies and Conflicts
├── Feasibility and Risk
├── Acceptance Outcomes
├── Open Issues
└── PRD Preparation Handoff
```

Use `templates/requirement-analysis.md` when available.

## Output Contract

Primary artifact:

`Requirement Analysis Document`

Supporting artifacts:

- Stakeholder Need Register.
- Business Rule Register.
- Requirement Inventory.
- Requirement Prioritization Matrix.
- Dependency and Conflict Register.
- Requirement Source Matrix.
- Open Issue Register.

Every major requirement must retain
a reference to its originating evidence or decision.

## Quality Gate

The document is ready for PRD preparation when:

- [ ] Project objectives and scope are identifiable.
- [ ] Relevant stakeholders are documented.
- [ ] Significant needs have source references.
- [ ] Requirements use stable provisional identifiers.
- [ ] Requirements are classified consistently.
- [ ] Priorities have documented rationale.
- [ ] Business rules have identifiable origins.
- [ ] Dependencies and conflicts are recorded.
- [ ] Material assumptions remain distinguishable.
- [ ] Acceptance outcomes are understandable.
- [ ] No unsupported product commitments are introduced.
- [ ] Open issues and validation status are reported.

A passing internal review does not authorize
PRD baseline approval.

## Failure Handling

Return `BLOCKED` when:

- Essential stakeholder requirements conflict.
- The project scope cannot be established.
- Critical business rules lack authoritative decisions.
- Required evidence is insufficient for consequential
  requirement conclusions.

Return `PARTIAL` when a provisional inventory can be
prepared but important validation is outstanding.

Continue non-conflicting analysis where possible.

## Worked Example

Illustrative input:

```yaml
problem_id: PROB-001
description: "Manual consolidation may delay reporting"
evidence_status: USER_SUPPLIED
```

Derived stakeholder need:

```yaml
need_id: NEED-001
stakeholder: "Reporting officer"
statement: "Access consolidated reporting information"
source_ids:
  - PROB-001
validation_status: PROPOSED
```

Provisional requirement candidate:

```yaml
requirement_id: REQ-001
type: USER
statement: >
  Authorized reporting personnel need to retrieve
  consolidated records for a reporting period.
source_ids:
  - NEED-001
priority: UNASSESSED
validation_status: PROPOSED
```

The need and requirement must be validated.

The example does not establish a database design,
automatic report generator, processing-time reduction,
or implementation technology.

Those decisions require subsequent requirements
and design analysis.

## Handoff to PRD Engineering

Next skill:

`prd-generation`

Handoff record:

```yaml
skill: requirement-analysis
status: IN_REVIEW
primary_artifact: requirement-analysis
validated_need_ids: []
requirement_ids: []
unresolved_issues: []
verification_status: NOT_RUN
prd_readiness: PENDING_REVIEW
```

The Requirements Engineer must review unresolved
issues before incorporating requirements into a PRD.

PRD generation must preserve requirement origins
and must not silently expand approved project scope.

## Governing Specifications

- [Agent Operating Contract](../../AGENTS.md)
- [Requirements Engineer](../../agents/requirements-engineer.md)
- [Governance Protocol](../../core/governance.md)
- [Workflow Protocol](../../core/workflow.md)
- [Verification Protocol](../../core/verification.md)
