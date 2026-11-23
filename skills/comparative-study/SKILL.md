---
name: comparative-study
description: >
  Conduct evidence-based comparisons of existing software systems,
  products, and alternative operational solutions. Use when requested
  to perform a comparative study, evaluate similar systems, analyze
  existing product capabilities, assess solution gaps, or establish
  research-backed opportunities for a proposed system.
  Produces a Comparative Study Report and evidence matrix.
version: 0.1.0
category: research
---

# Comparative System Study

## Purpose

Evaluate comparable systems or operational solutions using
consistent criteria and traceable evidence.

The purpose of comparison is to inform engineering decisions,
not to prove that the proposed system is superior.

This skill supports Phase P02 of the PREZEKC AI lifecycle.

## When to Use

Activate this skill when the task requires:

- Finding existing solutions to a defined problem.
- Comparing applications or information systems.
- Evaluating documented functionality.
- Identifying implementation or operational limitations.
- Examining alternative approaches.
- Supporting product research before requirement definition.

Do not use this skill as a substitute for stakeholder interviews,
requirement approval, or system architecture decisions.

## Required Context

Required inputs:

| Input | Requirement |
|---|---|
| Research objective | Question the comparison must answer |
| Problem context | Problem or need motivating the study |
| Evaluation scope | Capabilities or characteristics to assess |

Preferred upstream artifact:

`Existing System Analysis Report`

Optional inputs:

- Existing system documentation.
- Stakeholder requirements.
- Product documentation.
- Vendor specifications.
- Academic literature.
- Public technical references.
- Demonstration or trial access.

If no reliable comparison sources are available,
record the search limitations.

## Source Evaluation Policy

Prefer primary sources where available:

1. Official product documentation.
2. Publicly accessible product functionality.
3. Technical specifications.
4. Published research and evaluations.
5. Credible independent analysis.

Community reports may provide useful context but must
be distinguished from independently verified behavior.

For time-sensitive features, record the source date
or inspection date where available.

Never infer the current state of a product solely from
outdated documentation without disclosing the limitation.

## Evidence Classification

Each evaluated claim must be classified as:

- `CONFIRMED`: Direct evidence supports the claim.
- `REPORTED`: A source reports the claim.
- `INFERRED`: Derived from evidence but not directly verified.
- `UNKNOWN`: Evidence is insufficient.
- `NOT_APPLICABLE`: Criterion does not apply.

Use `NOT_DOCUMENTED` when available documentation does
not address a feature.

Do not equate `NOT_DOCUMENTED` with `ABSENT`.

## Workflow

### Step 1 — Define the Research Question

Translate the project problem into explicit questions.

Determine:

- What needs to be compared?
- Why is the comparison necessary?
- Which users or workflows are relevant?
- Which decisions should the findings inform?
- Which constraints must be considered?

Avoid comparison criteria unrelated to the stated problem.

### Step 2 — Select Comparison Candidates

Identify candidate systems or alternatives.

Selection should consider:

- Similarity of purpose.
- Similarity of target users.
- Functional relevance.
- Operational context.
- Availability of reliable evidence.

Document why each candidate was included.

Do not fabricate systems to reach a target number
of comparison candidates.

If the available candidates are insufficient,
state the limitation and continue with supported evidence.

### Step 3 — Establish Evaluation Criteria

Define criteria before evaluating candidates.

Possible dimensions include:

- Functional capability.
- Process compatibility.
- Information management.
- Reporting and analytics.
- User experience.
- Accessibility.
- Integration capability.
- Security and privacy.
- Deployment constraints.
- Maintainability.

Use only criteria relevant to the research objective.

Define each criterion consistently so that
different systems can be evaluated fairly.

### Step 4 — Collect and Register Sources

For each source, record:

```yaml
source_id: SRC-001
system_id: SYS-001
source_type: OFFICIAL_DOCUMENTATION
title: "Source title"
location: "Source URL or document reference"
published_at: null
accessed_at: null
relevant_claims: []
limitations: []
```

Use actual source information.

Do not invent publication dates, URLs, or authors.

Unavailable details must remain null or UNKNOWN.

### Step 5 — Evaluate Each Candidate

Assign a stable system identifier.

For every criterion:

1. Inspect the available source material.
2. Extract relevant factual claims.
3. Classify evidence strength.
4. Document capabilities supported by evidence.
5. Identify confirmed limitations.
6. Record information gaps.
7. Preserve source references.

Maintain separation between product functionality
and organization-specific implementation outcomes.

### Step 6 — Build the Comparison Matrix

Use an evidence-backed matrix.

Minimum structure:

| System | Criterion | Finding | Evidence | Source |
|---|---|---|---|---|
| SYS-001 | C-001 | Confirmed capability | CONFIRMED | SRC-001 |
| SYS-002 | C-001 | Not documented | UNKNOWN | SRC-002 |

A matrix cell must not be filled with an unsupported
yes/no determination.

If numerical scoring is necessary, establish and
document the scoring rubric before assigning scores.

Do not invent performance metrics or rankings.

### Step 7 — Analyze Relevant Gaps

Compare candidate capabilities against the project
problem and available stakeholder needs.

For each gap, identify:

- Gap identifier.
- Related problem or need.
- Relevant comparison finding.
- Supporting source.
- Potential implication.
- Confidence level.
- Additional validation required.

A comparative gap is not automatically
an approved product requirement.

### Step 8 — Formulate Research Conclusions

Conclusions must answer the research objective.

Separate:

- Established findings.
- Evidence limitations.
- Relevant capabilities.
- Confirmed gaps.
- Potential design opportunities.
- Questions requiring stakeholder validation.

Avoid unsupported claims of superiority,
novelty, cost savings, or performance improvement.

### Step 9 — Produce the Comparative Report

Required document structure:

```text
Comparative Study Report
├── Document Control
├── Research Objective
├── Scope and Methodology
├── Candidate Selection
├── Evaluation Criteria
├── Source Register
├── Individual System Assessments
├── Comparative Matrix
├── Gap Analysis
├── Research Findings
├── Limitations and Uncertainty
└── Implications for Requirement Analysis
```

Use `templates/comparative-study.md` when available.

### Step 10 — Verify Findings

Check every material conclusion against
its originating sources.

Resolve contradictory evidence where possible.
Otherwise preserve the conflict explicitly.

## Output Contract

Primary artifact:

`Comparative Study Report`

Supporting artifacts:

- Candidate Register.
- Source Register.
- Evaluation Criteria Register.
- Comparison Matrix.
- Gap Analysis Register.
- Research Limitations.

All referenced systems and sources must be identifiable.

## Quality Gate

The report is ready for review only when:

- [ ] Research questions are explicit.
- [ ] Candidate selection is justified.
- [ ] Comparison criteria are consistent.
- [ ] Material claims contain source references.
- [ ] Evidence classifications are accurate.
- [ ] Missing information is not treated as feature absence.
- [ ] Verified limitations are separated from assumptions.
- [ ] Conclusions follow from the recorded evidence.
- [ ] Relevant gaps reference the project problem.
- [ ] Unresolved uncertainties are disclosed.

## Failure Handling

Return `BLOCKED` when reliable evidence is unavailable
for a critical comparison decision.

Return `PARTIAL` when only part of the comparison
can be supported.

Do not replace inaccessible primary documentation
with invented feature descriptions.

## Worked Example

Illustrative research question:

"How do existing systems support administrative
reporting workflows?"

Example evidence record:

```yaml
system_id: SYS-001
criterion_id: C-REPORTING
finding: "Documentation describes CSV export"
evidence_status: REPORTED
source_id: SRC-001
limitation: "Export behavior was not tested"
```

A second candidate with no reporting documentation
must be marked `NOT_DOCUMENTED`, not "no export feature."

Potential opportunity:

```yaml
gap_id: GAP-001
related_problem: PROB-001
finding: "Reporting requirements require further validation"
status: PROPOSED
evidence:
  - SRC-001
requires_stakeholder_review: true
```

These records illustrate the format only.
They are not factual claims about real products.

## Handoff

Next skill:

`requirement-analysis`

Handoff record:

```yaml
skill: comparative-study
status: IN_REVIEW
primary_artifact: comparative-study
candidate_ids: []
source_ids: []
gap_ids: []
unresolved_findings: []
verification_status: NOT_RUN
```

Research findings must remain distinguishable
from approved stakeholder requirements.

## Governing Specifications

- [Agent Operating Contract](../../AGENTS.md)
- [Research Analyst](../../agents/research-analyst.md)
- [Governance Protocol](../../core/governance.md)
- [Workflow Protocol](../../core/workflow.md)
- [Verification Protocol](../../core/verification.md)
