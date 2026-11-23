
# Requirement Analysis Document

## Document Control

| Field | Value |
|---|---|
| Document ID | RAD-[PROJECT] |
| Project | [Project name] |
| Version | 0.1 |
| Status | DRAFT |
| Responsible Role | Requirements Engineer |
| Prepared By | [Name or agent] |
| Date | [YYYY-MM-DD] |
| Source Analysis | [Document IDs and versions] |
| Verification Status | NOT_RUN |
| Approval Reference | PENDING |

## 1. Objectives and Scope

### 1.1 Project Objectives

[Identify the outcomes supported by the requirements analysis.]

### 1.2 Scope Boundary

**In scope:** [Processes, stakeholders, and operational concerns]

**Out of scope:** [Excluded activities]

**Constraints:** [Confirmed constraints and references]

### 1.3 Source Baseline

| Source Document | Version | Status | Reference |
|---|---|---|---|
| Existing System Analysis | [Version] | [Status] | [Reference] |
| Comparative Study | [Version] | [Status] | [Reference] |
| Stakeholder Decision | [Version or date] | [Status] | [Reference] |

List only sources that exist and were examined.

## 2. Stakeholder Register

| Stakeholder ID | Role | Responsibility | Requirement Interest | Source |
|---|---|---|---|---|
| STK-001 | [Role] | [Responsibility] | [Interest] | [Source ID] |

## 3. Problem-to-Need Mapping

| Problem ID | Evidence | Need ID | Stakeholder | Validation Status |
|---|---|---|---|---|
| PROB-001 | [Evidence ID] | NEED-001 | STK-001 | PROPOSED |

### 3.1 Stakeholder Needs

#### NEED-001 — [Need Title]

**Stakeholder:** [Stakeholder ID]

**Statement:** [Required outcome or operational need]

**Source:** [Evidence, problem, or decision reference]

**Expected outcome:** [Observable result]

**Validation status:** PROPOSED

Repeat for each identified need.

## 4. Business Rules

| Rule ID | Rule | Source | Affected Need | Status |
|---|---|---|---|---|
| BUS-001 | [Business rule] | [Source ID] | NEED-001 | PROPOSED |

Do not infer approval rules or eligibility restrictions from implementation conventions.

## 5. Requirement Inventory

### REQ-001 — [Requirement Title]

**Classification:** [BUSINESS / USER / FUNCTIONAL / QUALITY / DATA / INTERFACE / CONSTRAINT]

**Statement:** [Requirement candidate]

**Source IDs:** [Need, evidence, or decision references]

**Stakeholders:** [Stakeholder IDs]

**Priority:** UNASSESSED

**Priority rationale:** [Documented rationale or PENDING]

**Acceptance outcome:** [Observable outcome]

**Dependencies:** [Requirement IDs or None]

**Assumptions:** [Assumption IDs or None]

**Validation status:** PROPOSED

Repeat for each requirement candidate.

## 6. Classification Summary

| Requirement ID | Classification | Source | Status |
|---|---|---|---|
| REQ-001 | [Classification] | [Source IDs] | PROPOSED |

## 7. Prioritization

**Method:** [Selected method]

**Decision authority:** [Stakeholder or project owner]

| Requirement ID | Priority | Rationale | Decision Reference |
|---|---|---|---|
| REQ-001 | UNASSESSED | [Rationale or PENDING] | [Reference] |

Priority values must follow the selected method.

Do not assign mandatory status without a documented basis.

## 8. Dependencies and Conflicts

### 8.1 Dependency Register

| Dependency ID | Requirement | Depends On | Description |
|---|---|---|---|
| DEP-001 | REQ-001 | [Requirement or external dependency] | [Description] |

### 8.2 Conflict Register

| Issue ID | Affected Requirements | Conflict | Required Decision | Owner |
|---|---|---|---|---|
| ISSUE-001 | [IDs] | [Conflict] | [Decision] | [Owner] |

Unresolved conflicts must remain visible.

## 9. Feasibility and Risk

| Risk ID | Requirement | Risk or Constraint | Impact | Assessment Status |
|---|---|---|---|---|
| RISK-001 | REQ-001 | [Risk] | [Impact] | PROVISIONAL |

Distinguish preliminary feasibility assessment from validated technical findings.

## 10. Acceptance Outcomes

| Requirement ID | Expected Outcome | Validation Method | Open Decision |
|---|---|---|---|
| REQ-001 | [Outcome] | [Proposed method] | [Issue ID or None] |

Acceptance outcomes describe intended results, not necessarily the final implementation mechanism.

## 11. Assumptions and Open Issues

| ID | Description | Impact | Owner | Required Resolution |
|---|---|---|---|---|
| ASM-001 | [Assumption] | [Impact] | [Owner] | [Evidence] |
| ISSUE-002 | [Question] | [Impact] | [Owner] | [Decision] |

## 12. Requirement Source Matrix

| Requirement ID | Need ID | Problem ID | Comparative Gap | Other Evidence |
|---|---|---|---|---|
| REQ-001 | NEED-001 | PROB-001 | [Gap ID or N/A] | [Source IDs] |

References must identify actual source artifacts.

## 13. Validation and Review

| Review Item | Result | Evidence |
|---|---|---|
| Scope consistency | NOT_RUN | [Reference] |
| Source traceability | NOT_RUN | [Reference] |
| Stakeholder coverage | NOT_RUN | [Reference] |
| Requirement clarity | NOT_RUN | [Reference] |
| Priority justification | NOT_RUN | [Reference] |
| Dependency and conflict review | NOT_RUN | [Reference] |

**Overall verification:** NOT_RUN

**Stakeholder review:** PENDING

**Approval status:** PENDING

## 14. PRD Handoff

**Target artifact:** Product Requirements Document

**Validated needs:** [Need IDs]

**Requirement candidates:** [REQ IDs]

**Approved business rules:** [BUS IDs]

**Open decisions:** [Issue IDs]

**PRD readiness:** PENDING_REVIEW

Provisional requirement candidates must not be represented as approved PRD requirements.

## 15. Revision History

| Version | Date | Change | Author |
|---|---|---|---|
| 0.1 | [YYYY-MM-DD] | Initial draft | [Author] |
