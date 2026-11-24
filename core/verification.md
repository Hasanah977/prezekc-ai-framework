
# PREZEKC AI — Verification and Quality Protocol

> Version 0.1.0 | Engineering Assurance Specification

This specification defines the verification requirements,
evidence standards, acceptance controls, and failure-reporting
rules applied to engineering deliverables under PREZEKC AI.

Verification establishes whether an artifact satisfies
defined criteria. It does not replace human authorization.

Agents must not report successful verification without
executing or inspecting the applicable evidence.

## 1. Verification Model

Each verification activity must establish:

1. The artifact being evaluated.
2. The applicable requirements or acceptance criteria.
3. The verification method.
4. The environment and tools used, where relevant.
5. The observed result.
6. Supporting evidence.
7. Remaining defects or limitations.
8. The resulting verification status.

Verification must be proportional to the artifact's
complexity, operational risk, and potential impact.

## 2. Verification Status

| Status | Definition |
|---|---|
| `PASS` | All applicable mandatory checks passed. |
| `PARTIAL` | Some checks passed; required coverage remains incomplete. |
| `FAIL` | At least one mandatory criterion failed. |
| `BLOCKED` | Verification cannot proceed due to a dependency or restriction. |
| `NOT_RUN` | The verification activity was not executed. |
| `N/A` | The criterion does not apply, with documented justification. |

`PASS` must not be assigned solely because an artifact
appears correct or because a similar test passed previously.

Approval is maintained independently using the
governance process.

## 3. Evidence Classification

Verification evidence may include:

| Type | Examples |
|---|---|
| `DOCUMENT_REVIEW` | Inspected content, cross-references, requirements. |
| `SOURCE_INSPECTION` | Code or configuration inspection. |
| `STATIC_ANALYSIS` | Linting, type checks, security analysis. |
| `BUILD_EXECUTION` | Actual build output and exit status. |
| `TEST_EXECUTION` | Test results and execution records. |
| `RUNTIME_OBSERVATION` | Verified application behavior. |
| `STAKEHOLDER_REVIEW` | Recorded review and acceptance decision. |

Evidence must identify what was checked and what
remains unverified.

An external citation supports a research claim but
does not establish software runtime correctness.

## 4. Verification Record Contract

Every substantive verification record should contain:

```yaml
verification_id: VER-001
artifact: "SRS"
artifact_version: "1.0"
baseline: "PRD v1.0"

method: DOCUMENT_REVIEW
criteria:
  - "All mandatory PRD requirements mapped"
  - "All SRS requirements are testable"

status: NOT_RUN
evidence: []
findings: []
limitations: []

reviewed_by: null
review_date: null
```

The example is a record schema, not an actual test result.

Evidence must never be fabricated to satisfy a required field.

## 5. Existing System Analysis Gate

The analysis report must establish:

- Identifiable current processes or system boundaries.
- Actors and responsibilities.
- Relevant information flows.
- Observed or reported operational problems.
- Sources supporting material findings.
- Explicit assumptions and evidence gaps.
- Constraints and potential impacts.

A claim presented as observed must have corresponding
inspection, interview, or documentary evidence.

When available evidence is insufficient, report the
affected findings as unresolved rather than verified.

## 6. Comparative Study Gate

Comparative analysis must be evaluated for:

- Identifiable comparison candidates.
- Relevant and consistent evaluation criteria.
- Traceable sources.
- Accurate representation of documented capabilities.
- Separation of verified findings and assumptions.
- Conclusions supported by the comparison.

A missing feature description is not conclusive
evidence that the feature does not exist.

Fabricated systems, references, or comparative
findings invalidate the affected analysis.

## 7. Requirement Analysis Gate

The requirement analysis must identify:

- Stakeholders and user groups.
- Requirement sources.
- Functional and operational needs.
- Relevant business rules.
- Data and integration needs.
- Priorities and dependencies.
- Conflicts and unresolved assumptions.
- Constraints affecting feasibility.

Requirements that are ambiguous or contradictory
must be flagged before baseline approval.

## 8. PRD Verification Gate

The PRD must satisfy the following mandatory criteria:

| ID | Verification Criterion |
|---|---|
| `PRD-V01` | Product objective and problem statement are defined. |
| `PRD-V02` | Stakeholders and target users are identified. |
| `PRD-V03` | Product scope and exclusions are explicit. |
| `PRD-V04` | Major product capabilities have stable identifiers. |
| `PRD-V05` | Capabilities are traceable to justified needs. |
| `PRD-V06` | Priorities and dependencies are documented. |
| `PRD-V07` | Acceptance outcomes are defined. |
| `PRD-V08` | Success criteria and constraints are identified. |
| `PRD-V09` | Material contradictions are resolved or flagged. |
| `PRD-V10` | Approval status and document version are recorded. |

The PRD must pass applicable checks before submission
for baseline approval.

Passing verification does not automatically establish
human approval.

## 9. SRS Verification Gate

The SRS must reference an approved PRD baseline.

Mandatory criteria:

| ID | Verification Criterion |
|---|---|
| `SRS-V01` | Approved PRD version is referenced. |
| `SRS-V02` | Functional requirements have unique identifiers. |
| `SRS-V03` | Non-functional requirements are specified. |
| `SRS-V04` | Actors and authorization boundaries are defined. |
| `SRS-V05` | Inputs, outputs, and system behavior are identifiable. |
| `SRS-V06` | Relevant validation and failure behavior are documented. |
| `SRS-V07` | Business rules and interfaces are specified. |
| `SRS-V08` | Requirements are measurable or objectively testable. |
| `SRS-V09` | PRD-to-SRS traceability is complete or exceptions approved. |
| `SRS-V10` | Unapproved scope expansion is absent. |

Each requirement must be:

- Clear.
- Unambiguous.
- Consistent.
- Feasible within documented constraints.
- Verifiable.
- Traceable to an approved source.

Non-functional requirements containing numerical targets
must specify measurement conditions and methods.

Statements such as "the system must be fast" are
insufficient without measurable acceptance criteria.

## 10. Requirement Traceability Verification

The Requirement Traceability Matrix must preserve
relationships across the engineering lifecycle.

```text
PRODUCT REQUIREMENT
        |
        v
SYSTEM REQUIREMENT
        |
        v
DESIGN ELEMENT
        |
        v
IMPLEMENTATION
        |
        v
TEST CASE
```

The verification process must detect:

- Missing PRD-to-SRS mappings.
- Unsupported SRS additions.
- Duplicate requirement identifiers.
- Conflicting requirement definitions.
- Design elements without justified requirements.
- Requirements without planned test coverage.
- Tests that do not correspond to defined behavior.
- Broken references after approved changes.

### 10.1 Coverage Rules

During SRS preparation:

- Mandatory PRD requirements must have SRS coverage.
- Unresolved requirements must be explicitly recorded.
- Design and test mappings may remain pending.

During design:

- Applicable SRS requirements must have design coverage.
- Unmapped requirements must be reported.

During implementation:

- Implemented behavior must reference relevant requirements.
- Requirement-related test coverage must be established.

Before final acceptance:

- Mandatory requirements require verification evidence.
- Exceptions must be explicitly approved and documented.

### 10.2 Coverage Reporting

Coverage must distinguish:

- Covered requirements.
- Uncovered requirements.
- Approved exceptions.
- Not-applicable requirements.

A complete document is not necessarily a complete
or verified implementation.

## 11. System Design Verification Gate

The design must be checked against the approved SRS.

Required concerns include:

- Architectural completeness.
- Component responsibility boundaries.
- Data model consistency.
- Interface compatibility.
- Authentication and authorization.
- External integration behavior.
- Failure handling and recovery.
- UI/UX requirements where applicable.
- Technology justification.
- Requirement traceability.

Design documents must distinguish planned architecture
from implemented architecture.

Diagrams must reflect the intended system behavior
and must not contradict textual specifications.

## 12. Implementation Verification Gate

Before accepting an implementation change, verify:

1. The change is within the approved task scope.
2. Relevant requirements are identified.
3. Existing behavior and dependencies were considered.
4. The implementation satisfies applicable specifications.
5. Validation and error handling are implemented as needed.
6. Relevant tests have been executed where possible.
7. Unrelated behavior remains unaffected.
8. No secrets or sensitive data were introduced.
9. Known failures and limitations are documented.

Verification should begin with focused checks and expand
to integration or regression coverage according to risk.

A successful build does not establish functional correctness.

A successful unit test does not establish production readiness.

## 13. Platform Verification

Platform-specific verification must correspond to the
approved application targets.

### 13.1 Web

Applicable checks may include:

- Application build.
- Frontend and backend integration.
- Authentication and access control.
- API contract behavior.
- Responsive layout.
- Browser compatibility.
- Accessibility requirements.
- Data integrity.
- Error handling.
- Security checks.

### 13.2 Android

Applicable checks may include:

- Android build completion.
- Installation on supported devices or emulators.
- Navigation and lifecycle behavior.
- Device permission handling.
- API connectivity.
- Offline behavior where specified.
- Error and crash handling.
- Compatibility against supported Android versions.

### 13.3 iOS

Applicable checks may include:

- iOS build completion.
- Installation on supported simulators or devices.
- Navigation and lifecycle behavior.
- Platform permission handling.
- API connectivity.
- Error and crash handling.
- Compatibility against supported iOS versions.
- Signing and distribution requirements.

### 13.4 Cross-Platform

Android and iOS verification must be recorded separately.

Shared code does not establish equivalent behavior
across operating systems.

When an iOS or Android verification environment
is unavailable, mark the affected checks as `BLOCKED`
or `NOT_RUN`, as appropriate.

Never substitute successful execution on one platform
for unperformed verification on another.

## 14. Test Case Contract

Test cases should contain:

```yaml
test_id: TC-001
requirement_ids:
  - SRS-FR-001.2

objective: "Reject invalid email input"
environment: "Test environment"

preconditions:
  - "Registration interface is accessible"

steps:
  - "Open registration interface"
  - "Enter invalid email format"
  - "Submit registration"

expected_result: "Registration is rejected"

actual_result: null
status: NOT_RUN
evidence: []
executed_by: null
executed_at: null
```

Do not populate actual results until the test is executed.

Failed tests must remain visible until corrected
and successfully reverified.

## 15. Defect Severity

| Level | Definition |
|---|---|
| `CRITICAL` | Severe security, safety, or data integrity failure. |
| `HIGH` | Mandatory functionality is unavailable or seriously impaired. |
| `MEDIUM` | Functionality is degraded with limited operational impact. |
| `LOW` | Minor defect without significant functional impact. |

Severity and business priority are separate classifications.

Unresolved critical or high-severity defects normally
block production acceptance.

Any exception must follow explicit risk acceptance
under applicable governance rules.

## 16. Regression and Change Verification

After an approved change:

1. Identify affected requirements.
2. Inspect downstream traceability relationships.
3. Determine impacted components.
4. Update affected test cases.
5. Execute relevant regression checks.
6. Record the verification results.
7. Report uncovered or blocked scenarios.

Do not assume unchanged behavior remains correct
when its dependencies or contracts have changed.

## 17. Release Verification Gate

A release candidate must not be reported as ready
unless the required release criteria are satisfied.

Minimum release considerations:

- Approved requirements and release scope.
- Required functional verification.
- Applicable security checks.
- Platform-specific build and runtime evidence.
- Data migration and recovery readiness, if relevant.
- Unresolved defect assessment.
- Deployment and rollback procedures.
- Human release authorization.

An approved release may still fail during deployment.
Post-deployment verification is therefore required.

## 18. Verification Handoff

Every material verification activity must produce
a concise, evidence-based report.

Recommended format:

```text
Verification ID : VER-001
Artifact        : <name and version>
Baseline        : <approved reference>
Scope           : <verified behavior>
Methods         : <checks performed>
Evidence        : <actual results or references>
Status          : PASS | PARTIAL | FAIL | BLOCKED | NOT_RUN
Open Issues     : <remaining findings>
Reviewer        : <responsible person or agent>
```

Do not use `PASS` when mandatory verification
has not been executed.

Do not describe unapproved documents as accepted baselines.

A verification report must accurately reflect
the work performed and its limitations.

---

## Related Specifications

- [Agent Operating Contract](../AGENTS.md)
- [Framework Architecture](../FRAMEWORK.md)
- [Governance Protocol](governance.md)
- [Workflow Protocol](workflow.md)

**PREZEKC AI Verification and Quality Protocol — v0.1.0**

<!-- PREZEKC-V020-EXTENSION: DO NOT DUPLICATE -->
## v0.2.0 — Artifact-Specific Quality and Handoff Gates

- **Imported PRD/SRS:** Validate supported structure, IDs, baseline relationships, and RTM references; conduct a separate human content review for completeness, intent, contradictions, and feasibility. Machine validation does not authenticate approval.
- **SDD:** Check required architecture/data/API/security decisions against approved SRS IDs and record unverified design decisions.
- **UI/UX Flow:** Check role permissions, navigation, critical interface states, errors and recovery, and traceability to in-scope requirements.
- **Task Breakdown:** Check scope coverage, dependency ordering, acceptance criteria, test plan, and that tasks are not marked completed from planning alone.
- **Implementation:** Record changed files, commands executed, test outputs, and explicit `NOT_RUN` or `BLOCKED` statuses when checks cannot be completed.

Use the evidence semantics in [Task Execution Contract](task-execution.md) and the decision handoff in [Next Action Protocol](next-action.md). `VERIFICATION_PASS` never equals `OWNER_APPROVED`.
