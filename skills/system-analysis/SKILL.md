
---
name: system-analysis
description: >
  Analyze an existing system, manual workflow, or operational process.
  Use when examining current-state workflows, stakeholders, process
  problems, information flows, operational constraints, or root causes.
  Produces an evidence-backed Existing System Analysis Report suitable
  for comparative research and requirements analysis.
version: 0.1.0
category: system-analysis
---

# Existing System Analysis

## Purpose

Establish an evidence-based understanding of how a system or
operational process currently works, where problems occur,
and which constraints affect its performance.

Analyze the current state before proposing a future solution.

This skill supports Phase P01 of the PREZEKC AI lifecycle.

## When to Use

Activate this skill when the task involves:

- Analyzing an existing information system.
- Documenting a manual or partially automated process.
- Identifying operational problems and affected stakeholders.
- Investigating workflow inefficiencies.
- Establishing the current system boundary.
- Preparing the analysis required before product definition.

Do not use this skill to invent a new system architecture or
generate implementation code.

For a greenfield project with no existing system, investigate
the current business process or document that no predecessor
system exists.

## Required Context

Read the active project context and applicable governance
rules before starting.

Required information:

| Input | Requirement |
|---|---|
| Project objective | The purpose of the investigation |
| Target process | The system or operation under analysis |
| Available evidence | Documents, observations, or stakeholder input |

Optional information:

- Existing application documentation.
- Interviews and observation records.
- Business process diagrams.
- Operational procedures.
- Data samples.
- Known organizational constraints.

Missing information must be reported explicitly.

## Evidence Rules

Classify material statements according to the PREZEKC AI
evidence model.

- `OBSERVED`: Directly inspected or executed.
- `SOURCE_BACKED`: Supported by an identifiable source.
- `USER_SUPPLIED`: Reported by a stakeholder or project owner.
- `DERIVED`: Reasoned from documented inputs.
- `ASSUMPTION`: Not independently established.
- `UNKNOWN`: Insufficient available information.

Preserve the source of each important finding.

Stakeholder statements must not be represented as independently
observed behavior unless corroborated.

Do not fabricate interviews, measurements, process records,
or organizational practices.

## Workflow

### Step 1 — Establish the System Boundary

Identify:

1. Organizational or operational context.
2. Purpose of the existing process.
3. Primary and supporting actors.
4. External systems or organizations.
5. Inputs, outputs, and information boundaries.
6. Known operational and regulatory constraints.

Record uncertainty before proceeding.

### Step 2 — Identify Stakeholders

For each stakeholder, determine:

- Role and responsibility.
- Activities performed.
- Information received or produced.
- Systems or tools used.
- Operational dependencies.
- Problems reported.

Differentiate actual stakeholder responsibilities
from proposed future roles.

### Step 3 — Reconstruct the Current Workflow

Describe the process from initiation to completion.

Capture:

- Triggering event.
- Sequential activities.
- Decision points.
- Responsible actors.
- Data exchanges.
- Documents and records.
- Exceptions and rework.
- Process completion conditions.

Represent the process using structured text or a diagram
when source information is sufficient.

Mark unconfirmed steps rather than completing them
through inference.

### Step 4 — Examine Information and Data Flow

Identify information created, modified, transferred,
stored, and consumed during the process.

For each significant data flow, record:

- Data or document name.
- Source.
- Destination.
- Responsible actor.
- Storage or transfer method.
- Known validation requirements.
- Privacy and integrity concerns.

Do not assume database structures that have not been observed.

### Step 5 — Register Problems

Assign a stable identifier to each distinct problem.

Use the following structure:

```yaml
problem_id: PROB-001
description: "Problem statement"
affected_process: "Process reference"
affected_stakeholders: []
evidence:
  classification: UNKNOWN
  source_id: null
observed_impact: null
possible_cause: null
confidence: UNVERIFIED
```

Describe the problem separately from its possible cause.

Avoid proposing a feature as if it were an observed problem.

### Step 6 — Investigate Causes and Impacts

Evaluate each registered problem.

Determine:

1. The point in the workflow where it occurs.
2. The relevant operational conditions.
3. The impact on actors or process outcomes.
4. Whether the cause is observed or hypothetical.
5. Additional evidence needed to establish causality.

Use root-cause analysis only to the extent supported
by available evidence.

Quantitative impacts require recorded measurements
or an identifiable source.

### Step 7 — Identify Constraints and Dependencies

Document:

- Organizational policies.
- Technology limitations.
- Operational dependencies.
- Human resource constraints.
- Data availability.
- Security and privacy obligations.
- External integration constraints.

Separate confirmed constraints from assumptions.

### Step 8 — Produce the Analysis Report

Use the following document structure:

```text
Existing System Analysis
├── Document Control
├── Executive Summary
├── Objectives and Scope
├── Evidence and Methodology
├── System Context
├── Stakeholder Register
├── Current-State Workflow
├── Information and Data Flow
├── Problem Register
├── Root-Cause Assessment
├── Operational Constraints
├── Evidence Gaps and Assumptions
└── Findings and Handoff
```

Do not include unsupported performance improvements
or unapproved software requirements.

### Step 9 — Verify the Deliverable

Check the report against the verification criteria below.

Correct unsupported claims and incomplete references
before submitting the report for review.

## Output Contract

Primary artifact:

`Existing System Analysis Report`

Supporting artifacts:

- Stakeholder Register.
- Current-State Process Model.
- Information Flow Register.
- Problem Register.
- Assumption and Evidence Gap Register.

The output should be compatible with:

`templates/system-analysis.md`

If that template is unavailable, preserve the structure
defined in this skill and report the missing template.

## Quality Gate

The report is ready for review only when:

- [ ] The system boundary is identifiable.
- [ ] Relevant stakeholders and responsibilities are recorded.
- [ ] Current-state processes are documented.
- [ ] Significant information flows are identified.
- [ ] Problems have stable identifiers.
- [ ] Material findings contain evidence references.
- [ ] Causes are distinguished from hypotheses.
- [ ] Constraints and assumptions are explicit.
- [ ] No invented measurements or observations are present.
- [ ] Unresolved findings are documented.

A completed checklist does not constitute human approval.

## Failure Handling

Return `BLOCKED` when a critical process or decision cannot
be established from available evidence.

Return `PARTIAL` when useful analysis is available but
required coverage remains incomplete.

Do not manufacture missing findings to satisfy the report
structure.

## Worked Example

Illustrative input:

A stakeholder reports that monthly administrative records
are collected through paper forms and consolidated manually.

Permitted analysis:

```yaml
problem_id: PROB-001
description: "Manual consolidation may delay reporting"
affected_process: "Monthly reporting"
evidence:
  classification: USER_SUPPLIED
  source_id: INTERVIEW-001
observed_impact: null
possible_cause: "Repeated manual data transcription"
confidence: UNVERIFIED
```

The example records a reported concern without inventing
processing times, error rates, or confirmed root causes.

It does not justify prescribing an automated reporting
feature until the need has been evaluated.

## Handoff

Next skills:

- `comparative-study`
- `requirement-analysis`

The handoff must include:

```yaml
skill: system-analysis
status: IN_REVIEW
primary_artifact: existing-system-analysis
problem_ids: []
evidence_gaps: []
verification_status: NOT_RUN
```

Replace placeholders with actual recorded findings.

## Governing Specifications

- [Agent Operating Contract](../../AGENTS.md)
- [System Analyst](../../agents/system-analyst.md)
- [Governance Protocol](../../core/governance.md)
- [Workflow Protocol](../../core/workflow.md)
- [Verification Protocol](../../core/verification.md)
