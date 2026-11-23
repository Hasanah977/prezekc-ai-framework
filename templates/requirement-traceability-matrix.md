
# Requirement Traceability Matrix

> PREZEKC AI | Requirements Traceability Record

## Document Control

| Field | Value |
|---|---|
| Document ID | RTM |
| Project | [Project Name] |
| Version | 0.1 |
| Status | DRAFT |
| PRD Baseline | [Approved PRD Version] |
| SRS Baseline | [SRS Version] |
| Last Reviewed | Pending |
| Verification | NOT_RUN |

## 1. Purpose

The Requirement Traceability Matrix (RTM) maintains
explicit relationships between approved requirements
and downstream engineering artifacts.

The RTM is used to identify:

- Missing requirement coverage.
- Unsupported system requirements.
- Incomplete design mappings.
- Missing implementation references.
- Missing test coverage.
- Changes requiring downstream revalidation.

## 2. Identifier Convention

| Type | Identifier |
|---|---|
| Product Requirement | PRD-FR-001 |
| Product Quality Requirement | PRD-NFR-001 |
| System Requirement | SRS-FR-001.1 |
| System Quality Requirement | SRS-NFR-001 |
| Design Element | DES-001 |
| Test Case | TC-001 |
| Change Request | CHG-001 |

Identifiers must remain stable after approval.

Requirements with multiple sources must record
all approved source references.

## 3. Traceability Register

| PRD ID | SRS ID | Design ID | Implementation | Test ID | Coverage |
|---|---|---|---|---|---|
| PRD-FR-001 | SRS-FR-001.1 | PENDING | PENDING | PENDING | SRS_MAPPED |
| PRD-FR-001 | SRS-FR-001.2 | PENDING | PENDING | PENDING | SRS_MAPPED |

The rows above illustrate the structure only.
Replace them with actual requirement relationships.

Do not invent design, implementation, or test references.

## 4. Additional Justifications

System requirements that do not originate directly
from a PRD requirement must reference an approved
technical, policy, or regulatory justification.

| SRS ID | Justification | Approval Reference |
|---|---|---|
| [SRS ID] | [Justification] | [Approval] |

An unapproved justification does not establish
a valid requirements baseline.

## 5. Coverage Evaluation

Evaluate coverage by lifecycle stage.

### During SRS Generation

- Every mandatory PRD requirement must be accounted for.
- Every SRS requirement must have an authorized origin.
- Missing mappings must be reported.

### During System Design

- Applicable SRS requirements must map to design elements.
- Missing design coverage must be identified.

### During Implementation

- Implemented components must reference applicable requirements.
- Known implementation gaps must be recorded.

### During Verification

- Mandatory requirements must have relevant test coverage.
- Failed or unexecuted tests must not be marked as passed.

## 6. Coverage Status

Use the following coverage values:

| Status | Meaning |
|---|---|
| UNMAPPED | No valid mapping exists. |
| SRS_MAPPED | The requirement has SRS coverage. |
| DESIGN_MAPPED | Design coverage has been established. |
| IMPLEMENTED | Implementation reference is available. |
| TEST_DEFINED | Relevant test coverage is defined. |
| VERIFIED | Required verification evidence is available and passing. |
| EXCEPTION_APPROVED | An exception has explicit authorization. |

Coverage status describes the recorded relationship
and must not substitute for artifact approval.

## 7. Change Impact Register

| Change ID | Source Requirement | Affected Artifacts | Review Status |
|---|---|---|---|
| CHG-001 | [Requirement] | [Artifacts] | PROPOSED |

When approved requirements change:

1. Identify the changed source requirement.
2. Locate dependent SRS requirements.
3. Identify related design elements.
4. Identify affected implementation components.
5. Identify affected test cases.
6. Update impacted artifacts.
7. Execute applicable reverification.
8. Record the resulting baseline versions.

## 8. Verification Checklist

- [ ] Requirement identifiers are unique.
- [ ] Source references are valid.
- [ ] Mandatory PRD requirements are accounted for.
- [ ] SRS requirements have authorized origins.
- [ ] No fabricated downstream mappings are present.
- [ ] Coverage states match available artifacts.
- [ ] Exceptions have approval references.
- [ ] Change impacts are documented.
- [ ] Unresolved coverage gaps are reported.

## 9. Verification Record

| Field | Value |
|---|---|
| Verification ID | Pending |
| Method | DOCUMENT_REVIEW |
| Status | NOT_RUN |
| Findings | Pending |
| Evidence | Pending |
| Reviewed By | Pending |
| Review Date | Pending |

## 10. Revision History

| Version | Date | Description | Author |
|---|---|---|---|
| 0.1 | [YYYY-MM-DD] | Initial draft | [Author] |
