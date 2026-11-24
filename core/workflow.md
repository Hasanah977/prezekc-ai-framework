
# PREZEKC AI — Engineering Workflow Protocol

> Version 0.1.0 | Project Lifecycle Specification

This specification defines the execution lifecycle for projects
operating under PREZEKC AI.

The lifecycle is requirements-driven, evidence-based, and
adaptable to software engineering, system analysis, research,
and related project disciplines.

For new software projects, PRD-to-SRS engineering is a
mandatory dependency unless an authorized project-specific
exception has been recorded.

## 1. Workflow Contract

Every workflow phase must define:

| Field | Description |
|---|---|
| `phase_id` | Stable identifier for the lifecycle phase. |
| `objective` | Outcome the phase must establish. |
| `inputs` | Required information and upstream artifacts. |
| `activities` | Procedures performed during execution. |
| `outputs` | Expected engineering deliverables. |
| `entry_gate` | Conditions required before execution. |
| `exit_gate` | Conditions required for completion. |
| `owner` | Responsible human or logical agent role. |

A phase must not be marked complete solely because an
output file was generated.

Completion requires applicable validation and any mandatory
human approvals.

## 2. Project Classification

Before selecting a workflow, establish the project profile.

Required classification fields:

```yaml
project:
  name: "Project name"
  type: SOFTWARE_DEVELOPMENT
  objective: "Primary project objective"

  platforms:
    - WEB
    - ANDROID
    - IOS

  existing_system: UNKNOWN
  requirements_status: NOT_ESTABLISHED
  stakeholders: []
  constraints: []
  expected_deliverables: []
```

Supported project types:

- `SOFTWARE_DEVELOPMENT`
- `SYSTEM_ANALYSIS`
- `ACADEMIC_RESEARCH`
- `DOCUMENTATION`
- `MAINTENANCE`
- `OTHER`

Supported software targets:

- `WEB`
- `ANDROID`
- `IOS`
- `CROSS_PLATFORM`
- `BACKEND_API`

The classification determines applicable phases,
specialized skills, and verification requirements.

Unknown information must be recorded as unknown,
not completed using unsupported assumptions.

## 3. Standard Lifecycle

```text
PROJECT INTAKE
      |
      v
[01] EXISTING SYSTEM ANALYSIS
      |
      v
[02] COMPARATIVE STUDY
      |
      v
[03] REQUIREMENT ANALYSIS
      |
      v
[04] PRODUCT REQUIREMENTS (PRD)
      |
      v
   OWNER APPROVAL
      |
      v
[05] SOFTWARE REQUIREMENTS (SRS)
      |
      v
   OWNER APPROVAL
      |
      v
[06] SYSTEM DESIGN
      |
      v
   DESIGN APPROVAL
      |
      v
[07] IMPLEMENTATION
      |
      v
[08] TESTING AND VERIFICATION
      |
      v
   RELEASE APPROVAL
      |
      v
[09] DEPLOYMENT AND MAINTENANCE
```

This represents the default lifecycle.

Phases may be revisited when new evidence, stakeholder
decisions, or verification failures require revision.

Project-specific omissions require a documented justification.

## 4. Phase 01 — Existing System Analysis

**Objective:** Establish an evidence-based description of the
current system or business process.

**Entry conditions:**

- Project objective is identifiable.
- Relevant stakeholders or source material are available,
  or their absence has been documented.

**Procedure:**

1. Identify the organizational or operational context.
2. Identify actors and their responsibilities.
3. Map the current process and information flow.
4. Identify tools, records, and existing integrations.
5. Record observed problems and operational constraints.
6. Distinguish symptoms from possible root causes.
7. Assess impact on stakeholders and outcomes.
8. Identify uncertainties requiring further investigation.

**Deliverable:** Existing System Analysis Report.

**Exit conditions:**

- Current-state processes are documented.
- Actor responsibilities are identifiable.
- Significant problems are linked to available evidence.
- Unsupported claims are classified as assumptions.
- Information gaps and limitations are explicit.

If no existing system is available, document the current
manual process or establish that the project is a greenfield
initiative. Do not invent an existing system.

## 5. Phase 02 — Comparative Study

**Objective:** Evaluate relevant existing solutions against
consistent criteria.

**Entry conditions:**

- The target problem has been defined.
- Comparison objectives and evaluation criteria are available.

**Procedure:**

1. Identify relevant systems or alternative approaches.
2. Collect verifiable information about each candidate.
3. Define common comparison criteria.
4. Evaluate capabilities and documented limitations.
5. Distinguish confirmed limitations from missing information.
6. Analyze relevant gaps against project requirements.
7. Record findings and their supporting sources.

**Deliverable:** Comparative Study Report.

**Exit conditions:**

- Comparison criteria are explicit and consistently applied.
- Referenced systems are identifiable.
- Material findings have traceable sources.
- Conclusions are supported by available evidence.
- Missing or inaccessible information is disclosed.

The absence of documented functionality does not by itself
prove that an existing system lacks that functionality.

## 6. Phase 03 — Requirement Analysis

**Objective:** Establish a structured account of stakeholder,
business, data, and operational needs.

**Entry conditions:**

- Relevant problem evidence or stakeholder input exists.
- Critical uncertainties are identified.

**Procedure:**

1. Identify stakeholders and user groups.
2. Extract needs from available evidence.
3. Distinguish user needs from proposed implementations.
4. Identify business rules and operational constraints.
5. Establish requirement priorities.
6. Resolve or document conflicting expectations.
7. Identify dependencies and acceptance concerns.
8. Define the initial requirement inventory.

**Deliverable:** Requirement Analysis Document.

**Exit conditions:**

- Requirements have identifiable sources.
- Priorities and constraints are documented.
- Material ambiguities are addressed or flagged.
- The requirement inventory is suitable for product definition.

## 7. Phase 04 — Product Requirements Document

**Objective:** Define the intended product, its scope,
target users, and measurable outcomes.

**Entry conditions:**

- Requirement analysis is available.
- Product goals and stakeholders are identifiable.

**Procedure:**

1. Define the product vision and problem statement.
2. Identify primary users and use cases.
3. Establish goals, non-goals, and scope boundaries.
4. Define product capabilities.
5. Assign stable requirement identifiers.
6. Define priorities and dependencies.
7. Establish product-level acceptance criteria.
8. Identify constraints, assumptions, and risks.
9. Validate consistency with requirement analysis.
10. Submit the PRD for review and approval.

**Deliverable:** Product Requirements Document.

**Exit conditions:**

- Required PRD sections are complete.
- Requirements are traceable to identified needs.
- Scope and exclusions are explicit.
- Material conflicts are resolved or documented.
- Verification checks pass.
- Human approval is recorded.

An approved PRD becomes the product baseline used by
downstream requirements engineering.

## 8. Phase 05 — PRD-to-SRS Engineering

**Objective:** Transform an approved PRD into a complete,
consistent, and testable software specification.

This phase is a controlled decomposition process,
not a general-purpose document rewrite.

### 8.1 Required Inputs

- Approved PRD version and baseline identifier.
- Product requirement inventory.
- Applicable business rules.
- Known data and integration constraints.
- Approved project scope.

### 8.2 Decomposition Procedure

For each approved PRD requirement:

1. Identify the intended product capability.
2. Determine participating actors and system boundaries.
3. Identify initiating events and preconditions.
4. Specify expected system behavior.
5. Define required inputs and observable outputs.
6. Document validation and failure conditions.
7. Identify authorization and data constraints.
8. Extract relevant non-functional requirements.
9. Specify testable acceptance criteria.
10. Create requirement traceability relationships.

Continue until all mandatory product requirements
are covered or explicitly marked as unresolved.

### 8.3 Identifier Convention

```text
PRD-FR-001      Product functional requirement
PRD-NFR-001     Product quality requirement

SRS-FR-001.1    Derived functional requirement
SRS-FR-001.2    Additional derived requirement
SRS-NFR-001     System quality requirement

DES-001         Design element
TC-001          Test case
CHG-001         Change request
```

Identifiers must remain stable after baseline approval.

Use explicit traceability relationships for SRS requirements
that originate from multiple PRD requirements.

### 8.4 Decomposition Example

Approved PRD requirement:

```text
ID: PRD-FR-001

Requirement:
Users must be able to register an account
using an email address and password.
```

Derived SRS requirements:

```text
ID: SRS-FR-001.1
Parent: PRD-FR-001

The system shall provide an account registration
interface accepting an email address and password.
```

```text
ID: SRS-FR-001.2
Parent: PRD-FR-001

The system shall reject registration attempts
containing an invalid email address format.
```

```text
ID: SRS-FR-001.3
Parent: PRD-FR-001

The system shall reject registration attempts
using an email address already associated
with an existing account.
```

```text
ID: SRS-FR-001.4
Parent: PRD-FR-001

The system shall store account passwords using
a suitable one-way password hashing mechanism.
```

Acceptance criteria and implementation-independent
verification methods must be defined for each requirement.

### 8.5 Traceability Validation

The transformation must detect:

- Approved PRD requirements without SRS coverage.
- SRS requirements without valid originating requirements.
- Duplicate or unstable identifiers.
- Conflicting requirements.
- Untestable statements.
- Unapproved product scope expansion.
- Missing quality or failure requirements.

An unsupported product capability must be proposed
through change control, not inserted silently.

### 8.6 Deliverables

- Software Requirements Specification.
- Requirement Traceability Matrix.
- Unresolved Requirement Register.
- Requirements Verification Report.

### 8.7 Exit Conditions

- Mandatory PRD requirements are accounted for.
- SRS statements are clear and testable.
- Traceability relationships are valid.
- Material contradictions are resolved.
- Unapproved scope additions are excluded.
- Verification checks pass.
- Human approval is recorded.

The approved SRS becomes the system specification baseline.

## 9. Phase 06 — System Design

**Objective:** Produce an implementable technical design
consistent with the approved SRS.

**Entry conditions:**

- Approved SRS is available.
- Relevant constraints and integrations are known.

**Procedure:**

1. Select an architecture based on system requirements.
2. Define components and their responsibilities.
3. Identify data structures and persistence requirements.
4. Specify interfaces and external integrations.
5. Model significant interactions and workflows.
6. Develop relevant UML and ERD artifacts.
7. Specify authentication and authorization boundaries.
8. Define UI/UX behavior and accessibility concerns.
9. Document technology decisions and trade-offs.
10. Map design elements to SRS requirements.

**Deliverable:** System Design Specification.

**Exit conditions:**

- Significant requirements have corresponding design coverage.
- Interfaces and data contracts are consistent.
- Technical decisions have documented rationale.
- Major architectural risks are identified.
- Required design verification and approval are complete.

Not every project requires every diagram type.
Omissions must be justified based on project relevance.

## 10. Phase 07 — Implementation

**Objective:** Build the specified software without introducing
unapproved changes to product behavior.

**Entry conditions:**

- Approved requirements and design are available.
- Development environment is identified.
- Implementation scope is defined.

**Procedure:**

1. Inspect the relevant repository and dependencies.
2. Establish an implementation plan.
3. Select the smallest complete implementation scope.
4. Implement requirements according to their priority.
5. Preserve existing contracts unless changes are approved.
6. Handle relevant validation and failure conditions.
7. Add or update associated tests.
8. Inspect the changes for unintended side effects.
9. Record implementation status and limitations.

**Deliverables:**

- Source code.
- Build configuration.
- Relevant tests.
- Implementation records.

**Exit conditions:**

- Required changes are implemented.
- Applicable build or validation checks are executed.
- Known failures and limitations are documented.
- Implemented features remain traceable to specifications.

Exploratory prototypes must be labeled separately from
production-ready implementation.

## 11. Phase 08 — Testing and Verification

**Objective:** Determine whether implementation satisfies
approved requirements and release criteria.

**Entry conditions:**

- Implemented artifacts are available.
- Applicable requirements and acceptance criteria exist.
- A suitable verification environment is identified.

**Procedure:**

1. Establish test coverage from the SRS and RTM.
2. Execute applicable unit and integration tests.
3. Perform functional verification.
4. Evaluate applicable non-functional requirements.
5. Review security and data-handling behavior.
6. Perform platform-specific checks.
7. Record expected and actual results.
8. Classify defects and unresolved risks.
9. Reverify affected behavior after corrections.
10. Prepare the verification report.

**Deliverable:** Verification and Test Report.

**Exit conditions:**

- Mandatory acceptance criteria have evidence.
- Critical failures are resolved or handled under an
  explicitly approved risk process.
- Test results and limitations are documented.
- Release readiness is evaluated.
- Required human acceptance is recorded.

See [Verification Protocol](verification.md).

## 12. Phase 09 — Deployment and Maintenance

**Objective:** Release verified software through an approved,
controlled process and maintain operational continuity.

**Entry conditions:**

- Release candidate has completed mandatory verification.
- Deployment environment and procedures are identified.
- Release authorization is recorded.

**Procedure:**

1. Inspect deployment configuration and dependencies.
2. Establish backup and recovery procedures where relevant.
3. Evaluate migration and compatibility risks.
4. Execute the approved release procedure.
5. Verify operational behavior after deployment.
6. Record release results and incidents.
7. Monitor operational failures and relevant metrics.
8. Maintain change and maintenance records.

**Deliverables:**

- Released application.
- Deployment record.
- Post-release verification evidence.
- Maintenance log.

**Exit conditions:**

- Required release checks pass.
- Operational limitations are documented.
- Recovery procedures are available where applicable.
- Deployment results are communicated to the owner.

## 13. Platform-Specific Workflow Adaptation

Platform requirements are derived from the approved SRS.

| Target | Required verification concerns |
|---|---|
| Web | Browser behavior, API integration, accessibility, responsive layout, deployment environment. |
| Android | Android builds, permissions, supported devices, runtime behavior. |
| iOS | iOS builds, permissions, signing, supported devices, runtime behavior. |
| Cross-platform | Shared functionality and independent Android/iOS verification. |
| Backend/API | Interface contracts, authorization, data integrity, integration and operational behavior. |

Cross-platform source-code reuse is not equivalent to
cross-platform runtime verification.

When required platform tooling is unavailable, mark
the corresponding checks as unverified.

## 14. Workflow State Management

Task execution states:

| State | Meaning |
|---|---|
| `TODO` | Work has not started. |
| `IN_PROGRESS` | Work is actively being performed. |
| `IN_REVIEW` | Output is awaiting evaluation. |
| `CHANGES_REQUESTED` | Review identified required corrections. |
| `BLOCKED` | A required dependency or authorization is missing. |
| `DONE` | All completion conditions have been satisfied. |

Artifact approval and verification are maintained separately
from task execution states.

An artifact may be technically verified while its associated
task remains in review for human acceptance.

## 15. Iteration and Change Propagation

The lifecycle is iterative, not strictly linear.

When upstream requirements change:

1. Identify the originating requirement.
2. Register or reference the approved change request.
3. Determine affected downstream artifacts.
4. Update the applicable specification baseline.
5. Revise design and implementation as required.
6. Update test coverage.
7. Reverify impacted outcomes.
8. Record the revised status.

Do not regenerate unrelated artifacts merely because an
upstream document has changed.

## 16. Phase Handoff

Each completed phase must provide a handoff record:

```yaml
phase_id: PHASE-05
phase_name: PRD_TO_SRS
input_baseline: "PRD v1.0"
outputs:
  - "SRS v1.0"
  - "Requirement Traceability Matrix"
verification_status: PASS
approval_status: APPROVED
open_issues: []
next_phase: SYSTEM_DESIGN
```

A phase cannot be reported as complete when mandatory
entry or exit conditions remain unsatisfied.

This format defines the intended reporting contract;
automated workflow execution is not yet implemented.

---

## Related Specifications

- [Agent Operating Contract](../AGENTS.md)
- [Framework Architecture](../FRAMEWORK.md)
- [Governance Protocol](governance.md)
- [Verification Protocol](verification.md)

**PREZEKC AI Engineering Workflow Protocol — v0.1.0**

<!-- PREZEKC-V020-EXTENSION: DO NOT DUPLICATE -->
## v0.2.0 — Import-First Design-to-Execution Workflow

**P01–P09 remain the official phase identifiers.** Project intake is a pre-phase activity, not a newly numbered phase. P04 PRD and P05 SRS/RTM may be completed by importing documents prepared externally, provided format compatibility, review, version control, and separate human approval gates are satisfied. Internal document authoring is optional; baseline review is not.

For applicable software projects, P06 outputs include the SDD (architecture, data, API, backend and integration contracts) **and** UI/UX Flow for user-facing behavior. These may iterate together, but they must conform to the approved SRS. After design approval and before P07, use [Task Breakdown](../skills/task-breakdown/SKILL.md) to define ordered work, acceptance criteria, dependencies, and verification evidence.

At meaningful phase/task boundaries, use [Human-Guided Next Action](next-action.md): report work, checks, unresolved items, a single recommended next action, and the required owner decision. Do not ask after every trivial step within an already authorized task.

For import mechanics, follow [Import-First Guide](../docs/import-mode.md).
