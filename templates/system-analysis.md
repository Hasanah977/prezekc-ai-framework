
# Existing System Analysis Report

## Document Control

| Field | Value |
|---|---|
| Document ID | ESA-[PROJECT] |
| Project | [Project name] |
| Version | 0.1 |
| Status | DRAFT |
| Responsible Role | System Analyst |
| Prepared By | [Name or agent] |
| Date | [YYYY-MM-DD] |
| Verification Status | NOT_RUN |
| Approval Reference | PENDING |

## 1. Objective and Scope

### 1.1 Investigation Objective

[State the operational problem or system being investigated and the decisions this analysis must support.]

### 1.2 System Boundary

**Included processes:** [List]

**Excluded processes:** [List]

**Organizational context:** [Description]

**External dependencies:** [List]

### 1.3 Investigation Limitations

[Record inaccessible systems, unavailable participants, incomplete records, and other limitations.]

## 2. Evidence and Methodology

### 2.1 Investigation Methods

[Identify the methods actually used: observation, interview, document inspection, system inspection, or other authorized methods.]

### 2.2 Evidence Register

| Evidence ID | Type | Source | Date | Relevant Finding | Reliability |
|---|---|---|---|---|---|
| EVD-001 | [Type] | [Reference] | [Date or UNKNOWN] | [Finding] | [Assessment] |

Classify findings according to the evidence model defined in `skills/system-analysis/SKILL.md`.

Do not record an investigation method as completed unless it was performed.

## 3. Stakeholder Analysis

| Stakeholder ID | Role | Responsibility | Information Used | Evidence |
|---|---|---|---|---|
| STK-001 | [Role] | [Responsibility] | [Information] | [Evidence ID] |

### 3.1 Stakeholder Responsibilities

[Describe actual responsibilities and distinguish them from proposed future roles.]

### 3.2 Stakeholder Concerns

[Record concerns with their source and verification status.]

## 4. Existing System

### 4.1 Operational Overview

[Describe the current operating environment, system purpose, and existing tools.]

### 4.2 Current-State Workflow

| Step | Trigger or Input | Activity | Actor | Output | Evidence |
|---|---|---|---|---|---|
| 1 | [Trigger] | [Activity] | [Actor] | [Output] | [Evidence ID] |

### 4.3 Decision Points

| Decision ID | Condition | Responsible Actor | Result | Evidence |
|---|---|---|---|---|
| DEC-001 | [Condition] | [Actor] | [Outcome] | [Evidence ID] |

### 4.4 Exception and Rework Paths

[Document observed or source-backed failure handling, repeated work, and process exceptions.]

### 4.5 Process Diagram

**Diagram reference:** [File path, link, or NOT_AVAILABLE]

**Related evidence:** [Evidence IDs]

Do not invent process steps to complete the diagram.

## 5. Information and Data Flows

| Flow ID | Information | Origin | Destination | Storage or Transfer | Evidence |
|---|---|---|---|---|---|
| FLOW-001 | [Data] | [Source] | [Destination] | [Method] | [Evidence ID] |

### 5.1 Data Quality and Integrity

[Describe known validation, consistency, duplication, or completeness issues.]

### 5.2 Access and Privacy

[Document observed access boundaries, sensitive information, and applicable constraints.]

## 6. Problem Register

| Problem ID | Description | Affected Process | Impact | Evidence | Confidence |
|---|---|---|---|---|---|
| PROB-001 | [Problem] | [Process] | [Impact or UNKNOWN] | [Evidence ID] | [Assessment] |

### 6.1 Problem Analysis

#### PROB-001 — [Problem Title]

**Observed or reported condition:** [Statement]

**Affected stakeholders:** [Stakeholder IDs]

**Operational impact:** [Supported impact]

**Potential causes:** [Causes and evidence status]

**Evidence gaps:** [Missing information]

**Verification status:** [Status]

Distinguish confirmed causes from hypotheses. Do not fabricate processing times, costs, or incident frequencies.

## 7. Constraints and Dependencies

| Constraint ID | Description | Source | Impact | Status |
|---|---|---|---|---|
| CON-001 | [Constraint] | [Source ID] | [Impact] | [Confirmed or unverified] |

## 8. Assumptions and Open Questions

| ID | Description | Impact | Required Evidence | Owner |
|---|---|---|---|---|
| ASM-001 | [Assumption] | [Impact] | [Evidence] | [Owner] |
| ISSUE-001 | [Question] | [Impact] | [Decision or evidence] | [Owner] |

## 9. Findings

[Summarize supported findings without introducing unapproved product requirements.]

### 9.1 Confirmed Findings

[Reference evidence and problem IDs.]

### 9.2 Provisional Findings

[Record uncertain findings and required validation.]

### 9.3 Implications for Subsequent Analysis

[Identify problems and operational constraints to be examined through comparative study or requirement analysis.]

## 10. Verification Record

| Check | Result | Evidence |
|---|---|---|
| Investigation scope established | NOT_RUN | [Reference] |
| Stakeholder coverage reviewed | NOT_RUN | [Reference] |
| Current-state workflow reviewed | NOT_RUN | [Reference] |
| Problem evidence reviewed | NOT_RUN | [Reference] |
| Assumptions and gaps documented | NOT_RUN | [Reference] |

**Overall verification:** NOT_RUN

**Unresolved findings:** [Issue IDs]

## 11. Review and Approval

| Field | Value |
|---|---|
| Review Status | PENDING |
| Reviewer | [Authorized reviewer] |
| Decision | PENDING |
| Decision Date | [Date or PENDING] |
| Decision Reference | [Reference] |

## 12. Handoff

**Next activities:** Comparative Study; Requirement Analysis

**Problem references:** [Problem IDs]

**Evidence references:** [Evidence IDs]

**Outstanding issues:** [Issue IDs]

**Handoff status:** PENDING

## 13. Revision History

| Version | Date | Change | Author |
|---|---|---|---|
| 0.1 | [YYYY-MM-DD] | Initial draft | [Author] |
