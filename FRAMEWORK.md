
# PREZEKC AI — Framework Architecture

> Version 0.1.0 | Architecture and Engineering Specification
>
> Classification: Universal AI-Assisted Project Engineering Framework
>
> Status: Initial Specification

PREZEKC AI defines a requirements-driven operating framework for AI-assisted system analysis, research, software engineering, and project delivery.

The framework establishes a consistent relationship between problem evidence, product requirements, software specifications, system design, implementation, and verification.

This document describes the framework architecture, component boundaries, lifecycle dependencies, artifact contracts, and extension model.

Implementation-specific instructions are maintained in the corresponding operating protocols.

---

## 1. Architectural Scope

PREZEKC AI operates as an engineering governance and workflow framework rather than a programming-language-specific application framework.

It defines how AI assistants should interpret project context, coordinate engineering tasks, produce controlled deliverables, and verify outcomes against established requirements.

### 1.1 Objectives

The architecture is designed to:

1. Establish evidence-based problem analysis before solution development.
2. Standardize requirements documentation across different project types.
3. Preserve the relationship between PRD and derived SRS requirements.
4. Maintain traceability from approved requirements to implementation and tests.
5. Separate human authority from AI execution responsibilities.
6. Support reusable workflows, agent roles, and engineering skills.
7. Accommodate web, Android, iOS, and cross-platform development.
8. Enforce verification before reporting successful completion.
9. Maintain project continuity through durable context and decision records.

### 1.2 Architectural Constraints

PREZEKC AI must remain:

- **Technology-agnostic:** No mandatory programming language or application stack.
- **Model-independent:** No dependency on a single AI model or provider.
- **Requirements-driven:** Engineering decisions must reference established requirements.
- **Evidence-based:** Findings and verification claims must have identifiable support.
- **Human-governed:** Consequential decisions require appropriate human authorization.
- **Modular:** Specialized capabilities must be separable from core governance.
- **Traceable:** Requirements and controlled changes must preserve stable references.
- **Incremental:** Projects may progress iteratively without bypassing required controls.

These constraints apply to all framework extensions.

---

## 2. Logical Architecture

PREZEKC AI separates project authority, execution coordination, engineering capabilities, artifact management, and verification.

```text
+----------------------------------------------------------+
|                      PROJECT OWNER                       |
|          Objectives | Scope | Decisions | Approval        |
+-----------------------------+----------------------------+
                              |
                              v
+----------------------------------------------------------+
|                     PROJECT CONTEXT                      |
|       Requirements | Decisions | Tasks | Constraints      |
+-----------------------------+----------------------------+
                              |
                              v
+----------------------------------------------------------+
|                    AI ORCHESTRATOR                       |
|      Task Routing | Dependencies | Execution Control     |
+-------------+--------------------+-----------------------+
              |                    |
              v                    v
+-------------------------+  +-----------------------------+
|    GOVERNANCE LAYER     |  |       WORKFLOW LAYER        |
| Authority & Permissions |  | Lifecycle & Phase Control   |
| Approval & Change Rules |  | Entry & Exit Conditions     |
+-------------+-----------+  +--------------+--------------+
              |                             |
              +--------------+--------------+
                             |
                             v
+----------------------------------------------------------+
|                    EXECUTION LAYER                       |
|                                                          |
|       AGENTS          SKILLS          TEMPLATES           |
|       Roles           Procedures      Artifact Formats    |
+-----------------------------+----------------------------+
                              |
                              v
+----------------------------------------------------------+
|                    ARTIFACT LAYER                        |
|       Analysis | PRD | SRS | Design | Code | Tests         |
+-----------------------------+----------------------------+
                              |
                              v
+----------------------------------------------------------+
|                   VERIFICATION LAYER                     |
|     Evidence | Validation | Traceability | Quality        |
+-----------------------------+----------------------------+
                              |
                              v
+----------------------------------------------------------+
|                   HUMAN ACCEPTANCE                       |
|             Review | Approval | Release Control          |
+----------------------------------------------------------+
```

This is the intended logical architecture.

In version 0.1.0, the architecture is represented through Markdown-based specifications and operating contracts.

A standalone orchestration runtime, executable agent engine, and automated validation pipeline have not yet been implemented.

---

## 3. Core Components

### 3.1 Project Owner

The Project Owner is the designated human authority responsible for accepting requirements, approving consequential changes, and determining project completion.

Responsibilities include:

- Defining project objectives and constraints.
- Confirming project scope.
- Approving PRD and SRS baselines.
- Evaluating material changes.
- Accepting architecture decisions.
- Authorizing production releases.
- Reviewing unresolved risks.

AI-generated recommendations do not replace owner decisions.

### 3.2 Project Context

Project Context contains the information required to execute engineering tasks consistently across sessions and tools.

Minimum context includes:

| Record | Purpose |
|---|---|
| Project Profile | Project identity, type, objectives, and platform targets. |
| Requirement Baseline | Current approved PRD and SRS references. |
| Decision Register | Architectural and product decisions with rationale. |
| Task Register | Active tasks, ownership, dependencies, and status. |
| Change Register | Controlled changes and affected artifacts. |
| Verification Register | Checks performed, evidence, and unresolved findings. |

Context must be recoverable from durable project artifacts.

Conversation history may provide supplementary information but must not be treated as the authoritative source of implemented behavior.

### 3.3 AI Orchestrator

The AI Orchestrator is responsible for coordinating the selected engineering workflow.

Responsibilities:

1. Resolve the active project context.
2. Classify the requested task.
3. Identify applicable governance constraints.
4. Select the appropriate workflow and skills.
5. Determine required input artifacts.
6. Evaluate task dependencies.
7. Coordinate logical agent responsibilities.
8. Route generated artifacts to verification.
9. Report outcomes and unresolved conditions.

The orchestrator must not bypass approval gates to complete downstream tasks.

At the current development stage, orchestration is a procedural contract executed through a compatible AI assistant.

### 3.4 Governance Layer

The Governance Layer defines authority, approval, and change-control boundaries.

It determines whether a requested operation may proceed and whether additional authorization is required.

Its responsibilities include:

- Operation classification.
- Approval enforcement.
- Requirements baseline protection.
- Controlled change assessment.
- Security and confidentiality constraints.
- Decision accountability.

The authoritative governance specification is maintained in:

`core/governance.md`

### 3.5 Workflow Layer

The Workflow Layer defines engineering phases and their dependencies.

Each phase must declare:

- Objective.
- Required inputs.
- Entry conditions.
- Execution procedure.
- Expected outputs.
- Verification requirements.
- Exit conditions.
- Required approval.

Workflow execution may be iterative, but dependency and approval requirements remain enforceable.

The authoritative workflow specification is maintained in:

`core/workflow.md`

### 3.6 Execution Layer

The Execution Layer consists of agents, skills, and templates.

These components have distinct responsibilities.

**Agents** define engineering roles and accountability boundaries.

**Skills** define reusable task procedures, inputs, outputs, and failure handling.

**Templates** define the expected structure of controlled engineering deliverables.

An agent may invoke multiple skills during a task.

Multiple logical agent roles may be performed sequentially by a single AI assistant.

The framework must not assume independent multi-agent execution unless the underlying platform explicitly supports it.

### 3.7 Artifact Layer

The Artifact Layer contains the engineering outputs produced during the project lifecycle.

Artifacts may include:

- Existing System Analysis.
- Comparative Study.
- Requirement Analysis.
- Product Requirements Document.
- Software Requirements Specification.
- Requirement Traceability Matrix.
- System Design Specification.
- Source Code.
- Test Cases.
- Verification Reports.
- Deployment Records.

Controlled artifacts must preserve identifiable versions and lifecycle status.

### 3.8 Verification Layer

The Verification Layer determines whether deliverables satisfy applicable requirements and acceptance criteria.

It validates:

- Document completeness and consistency.
- Research evidence integrity.
- Requirement traceability.
- Specification testability.
- Design conformance.
- Implementation behavior.
- Platform-specific compatibility.
- Test execution results.
- Release readiness.

Verification does not establish human approval.

The authoritative verification specification is maintained in:

`core/verification.md`

---

## 4. Engineering Lifecycle

PREZEKC AI defines nine standard engineering phases.

| ID | Phase | Primary Output |
|---|---|---|
| `P01` | Existing System Analysis | System Analysis Report |
| `P02` | Comparative Study | Comparative Study Report |
| `P03` | Requirement Analysis | Requirement Analysis Document |
| `P04` | Product Requirements | PRD |
| `P05` | Software Requirements | SRS and RTM |
| `P06` | System Design | System Design Specification |
| `P07` | Implementation | Source Code and Build Artifacts |
| `P08` | Testing and Verification | Verification Report |
| `P09` | Deployment and Maintenance | Release and Maintenance Records |

### 4.1 Phase Dependencies

For new software projects, the default dependency chain is:

```text
P01 -> P02 -> P03 -> P04 -> P05 -> P06 -> P07 -> P08 -> P09
                        |     |     |                 |
                        v     v     v                 v
                    APPROVE APPROVE APPROVE        RELEASE
                      PRD    SRS   DESIGN         APPROVAL
```

Project-specific workflows may adapt the sequence when justified.

An analysis-only project may terminate before implementation.

A maintenance project may begin with existing approved requirements and proceed through impact analysis, controlled modification, and regression verification.

Omitted phases must be documented as not applicable rather than silently skipped.

### 4.2 Lifecycle Invariants

The following invariants apply to software projects:

1. Product requirements must have identifiable origins.
2. Final SRS baselines require an approved PRD.
3. Final system design must conform to the approved SRS.
4. Implementation must preserve approved requirement intent.
5. Material changes require impact analysis.
6. Verification claims require corresponding evidence.
7. Production deployment requires authorization.

Prototypes may be created before final baseline approval when explicitly classified as exploratory work.

---

## 5. Requirements Engineering Architecture

Requirements engineering is the principal capability of PREZEKC AI.

The framework separates product intent from system behavior and preserves traceability between them.

### 5.1 Requirements Model

```text
STAKEHOLDER NEED
        |
        v
PRODUCT REQUIREMENT
        |
        v
SYSTEM REQUIREMENT
        |
        v
DESIGN ELEMENT
        |
        v
IMPLEMENTATION COMPONENT
        |
        v
TEST CASE
        |
        v
VERIFICATION EVIDENCE
```

Each transition represents a defined engineering relationship.

A downstream artifact must not introduce unsupported product behavior.

### 5.2 Product Requirements Document

The PRD defines:

- Product purpose and problem statement.
- Stakeholder and user objectives.
- Scope and exclusions.
- Product capabilities.
- Priorities and dependencies.
- Acceptance outcomes.
- Success metrics.
- Constraints and assumptions.

The approved PRD establishes the product requirements baseline.

### 5.3 Software Requirements Specification

The SRS defines:

- Functional system behavior.
- Non-functional requirements.
- Actors and authorization boundaries.
- Inputs, outputs, and validation.
- Business rules.
- Data requirements.
- External interfaces.
- Failure handling.
- Testable acceptance criteria.

The SRS must reference the approved PRD baseline from which it was derived.

### 5.4 PRD-to-SRS Transformation

The transformation process consists of:

```text
APPROVED PRD
     |
     v
REQUIREMENT EXTRACTION
     |
     v
REQUIREMENT CLASSIFICATION
     |
     v
SYSTEM REQUIREMENT DECOMPOSITION
     |
     v
ACCEPTANCE CRITERIA DEFINITION
     |
     v
TRACEABILITY MAPPING
     |
     v
CONSISTENCY VERIFICATION
     |
     v
SRS REVIEW
     |
     v
APPROVED SRS
```

The transformation must preserve the semantic intent of the parent PRD requirements.

Additional technical details may be derived where necessary to specify system behavior.

New product capabilities must be submitted through change control rather than silently added to the SRS.

### 5.5 Requirement Identifiers

PREZEKC AI defines the following identifier convention:

| Prefix | Artifact |
|---|---|
| `PRD-FR` | Product functional requirement |
| `PRD-NFR` | Product-level non-functional requirement |
| `SRS-FR` | System functional requirement |
| `SRS-NFR` | System non-functional requirement |
| `DES` | Design element |
| `TC` | Test case |
| `CHG` | Change request |
| `VER` | Verification record |

Example relationship:

```text
PRD-FR-001
    |
    +-- SRS-FR-001.1
    |       |
    |       +-- DES-001
    |               |
    |               +-- TC-001
    |
    +-- SRS-FR-001.2
            |
            +-- DES-002
                    |
                    +-- TC-002
```

Identifiers must remain stable across approved document revisions.

A requirement may reference multiple originating requirements or design elements.

Traceability relationships must be recorded explicitly rather than inferred from identifier similarity.

### 5.6 Traceability Matrix

The Requirement Traceability Matrix (RTM) records dependencies between approved requirements and downstream artifacts.

Minimum logical fields:

| Field | Description |
|---|---|
| Requirement ID | Unique identifier of the tracked requirement. |
| Source ID | Originating requirement or approved justification. |
| Baseline Version | Applicable approved document version. |
| Design Reference | Corresponding design element. |
| Implementation Reference | Associated implementation component. |
| Test Reference | Verification or test case reference. |
| Coverage Status | Current traceability coverage. |

A missing relationship must be reported as a traceability finding.

The framework must not invent references to satisfy coverage requirements.

---

## 6. Agent Architecture

Agent definitions establish responsibilities without requiring independent AI processes.

| Agent | Responsibility | Primary Artifacts |
|---|---|---|
| Research Analyst | Evaluate existing solutions and supporting evidence. | Comparative Study |
| System Analyst | Analyze processes, stakeholders, and operational problems. | System Analysis, Requirements |
| Requirements Engineer | Define and decompose product and system requirements. | PRD, SRS, RTM |
| System Architect | Translate approved specifications into technical designs. | Architecture, UML, ERD, API Design |
| Development Engineer | Implement approved system behavior. | Source Code, Builds |
| Verification Engineer | Evaluate conformance and quality. | Test Cases, Verification Reports |

### 6.1 Agent Contract

Every agent definition must establish:

```yaml
agent:
  id: requirements-engineer
  role: "Requirements Engineer"
  objective: "Produce and validate requirements specifications"

  required_inputs:
    - "Approved requirements or analysis artifacts"

  outputs:
    - "Controlled requirements documents"

  constraints:
    - "Preserve approved scope"
    - "Maintain traceability"

  verification:
    - "Check requirement consistency"
    - "Check document completeness"

  escalation:
    - "Unapproved scope change"
    - "Missing critical requirements"
```

This structure defines a logical interface.

An executable agent runtime is not implied.

### 6.2 Responsibility Boundaries

Agents must not approve their own work on behalf of the project owner.

The Requirements Engineer may identify missing product capabilities but cannot independently authorize scope expansion.

The Development Engineer may implement approved behavior but cannot redefine requirements to simplify implementation.

The Verification Engineer must report observed failures rather than adjusting acceptance criteria to produce a passing result.

---

## 7. Skill Architecture

Skills are reusable execution procedures associated with defined engineering activities.

A skill must declare:

- Identifier and purpose.
- Required inputs.
- Preconditions.
- Execution procedure.
- Expected outputs.
- Verification criteria.
- Failure and escalation conditions.

Example skill definition:

```yaml
skill:
  id: prd-to-srs
  version: "0.1.0"

  purpose: "Derive testable SRS requirements from an approved PRD"

  preconditions:
    - "PRD baseline is approved"
    - "Requirement identifiers are available"

  inputs:
    - "Approved PRD"
    - "Business rules"
    - "Project constraints"

  outputs:
    - "SRS draft"
    - "Requirement Traceability Matrix"
    - "Unresolved requirement register"

  failure_conditions:
    - "Missing PRD approval"
    - "Unresolvable requirement contradiction"
    - "Unsupported scope expansion"
```

Skill execution must comply with global governance and the active workflow.

Project-specific skills may extend the framework without modifying core operating rules.

---

## 8. Artifact Management

Controlled artifacts require explicit identity and version information.

### 8.1 Artifact Metadata

Recommended metadata:

```yaml
artifact:
  id: SRS
  title: "Software Requirements Specification"
  version: "1.0"
  status: DRAFT

  source_baseline:
    document: PRD
    version: "1.0"

  owner: "Project Owner"
  approved_by: null

  verification_status: NOT_RUN
```

The example describes an artifact contract, not an existing automated parser.

### 8.2 Artifact States

Document approval states:

- `DRAFT`
- `IN_REVIEW`
- `CHANGES_REQUESTED`
- `APPROVED`
- `SUPERSEDED`
- `REJECTED`

Verification states:

- `PASS`
- `PARTIAL`
- `FAIL`
- `BLOCKED`
- `NOT_RUN`
- `N/A`

Approval and verification states must be managed independently.

### 8.3 Baseline Integrity

Approved document versions must remain identifiable after revision.

Changes affecting approved requirements must trigger downstream impact analysis.

Historical requirement relationships must not be removed solely to simplify current documentation.

---

## 9. Platform Architecture

PREZEKC AI supports platform-specific engineering workflows while preserving a common requirements and governance model.

### 9.1 Web Applications

Web workflows may include:

- Frontend architecture.
- Backend services.
- Database design.
- API contracts.
- Authentication and authorization.
- Responsive UI.
- Browser compatibility.
- Deployment and operational verification.

### 9.2 Android Applications

Android workflows may include:

- Native or cross-platform architecture.
- SDK and dependency configuration.
- Device permissions.
- Application lifecycle handling.
- API and local storage integration.
- Build generation.
- Emulator and device verification.

### 9.3 iOS Applications

iOS workflows may include:

- Native or cross-platform architecture.
- Xcode and SDK configuration.
- Device permissions.
- Application lifecycle handling.
- API and local storage integration.
- Build and signing verification.
- Simulator and device verification.

### 9.4 Cross-Platform Applications

Cross-platform development may use a shared codebase when compatible with approved requirements.

Technology selection must consider:

- Platform-specific functionality.
- Native integration requirements.
- Performance constraints.
- Team capability.
- Maintenance cost.
- Build and distribution requirements.

Android and iOS verification must remain independent.

Successful execution on one platform does not establish compatibility with another.

---

## 10. Verification Architecture

Verification is performed against explicit criteria and recorded evidence.

### 10.1 Verification Gates

| Gate | Subject | Minimum Requirement |
|---|---|---|
| `VG-01` | System Analysis | Evidence integrity and process completeness |
| `VG-02` | Comparative Study | Source validity and comparison consistency |
| `VG-03` | Requirement Analysis | Stakeholder and requirement coverage |
| `VG-04` | PRD | Scope consistency and acceptance criteria |
| `VG-05` | SRS | Testability and PRD traceability |
| `VG-06` | System Design | Conformance to approved SRS |
| `VG-07` | Implementation | Functional and implementation verification |
| `VG-08` | Release | Platform checks and release authorization |

A verification gate evaluates an artifact against its criteria.

The associated workflow exit condition may additionally require human approval.

### 10.2 Evidence Rules

Agents must distinguish between:

- Document inspection.
- Static analysis.
- Build execution.
- Automated test execution.
- Runtime observation.
- Human acceptance.

A verification claim must identify the method actually used.

Passing static analysis does not demonstrate runtime correctness.

Passing a build does not demonstrate that all acceptance criteria are satisfied.

### 10.3 Failure Handling

When mandatory verification fails:

1. Record the failed criterion.
2. Identify the affected artifact.
3. Determine the failure severity.
4. Identify the originating requirement where possible.
5. Define the required correction.
6. Reverify affected behavior.
7. Preserve the resulting evidence.

Unresolved mandatory failures must not be reported as successful completion.

---

## 11. Change Propagation

Change management maintains consistency between approved requirements and downstream engineering artifacts.

```text
CHANGE REQUEST
      |
      v
IMPACT ANALYSIS
      |
      v
OWNER APPROVAL
      |
      v
BASELINE REVISION
      |
      v
DEPENDENCY UPDATE
      |
      v
REVERIFICATION
      |
      v
CHANGE RECORD
```

Change impact assessment must consider:

- Product requirements.
- Software requirements.
- System architecture.
- Data contracts.
- User interfaces.
- Implementation components.
- Test coverage.
- Deployment compatibility.

Only affected artifacts should be modified unless a broader change is explicitly approved.

---

## 12. Framework Extensibility

PREZEKC AI supports extensions through project-specific agents, skills, workflows, rules, and templates.

Extensions must:

1. Preserve core governance constraints.
2. Declare their applicable project scope.
3. Define required inputs and outputs.
4. Identify dependencies.
5. Specify verification criteria.
6. Avoid conflicting requirement identifier conventions.
7. Document compatibility assumptions.

Extensions may specialize the engineering process but must not silently override approved requirements or human approval gates.

### 12.1 Project Profiles

Project profiles determine which capabilities are applicable.

Example classifications:

- `SOFTWARE_DEVELOPMENT`
- `SYSTEM_ANALYSIS`
- `ACADEMIC_RESEARCH`
- `DOCUMENTATION`
- `MAINTENANCE`

A documentation-only project does not require application deployment.

A software project targeting Android and iOS must include platform-specific implementation and verification requirements.

---

## 13. Repository Organization

PREZEKC AI separates governance, execution procedures, artifact templates, and project documentation.

```text
prezekc-ai-framework/
|
|-- README.md
|-- AGENTS.md
|-- FRAMEWORK.md
|
|-- core/
|   |-- governance.md
|   |-- workflow.md
|   `-- verification.md
|
|-- agents/
|-- rules/
|-- skills/
|-- templates/
|-- workflows/
`-- docs/
```

Component ownership:

| Location | Responsibility |
|---|---|
| `AGENTS.md` | Global agent operating contract. |
| `FRAMEWORK.md` | Logical architecture and component interfaces. |
| `core/` | Governance, workflow, and verification protocols. |
| `agents/` | Engineering role definitions. |
| `rules/` | Specialized operating constraints. |
| `skills/` | Reusable task procedures. |
| `templates/` | Controlled engineering document structures. |
| `workflows/` | Project-specific execution configurations. |
| `docs/` | Supporting architecture and usage documentation. |

Repository structure may evolve as executable tooling is introduced.

Documentation must accurately distinguish implemented components from planned capabilities.

---

## 14. Implementation Boundaries

The initial PREZEKC AI release establishes the framework specification and operating model.

### 14.1 Defined in v0.1.0

- Framework architecture.
- Governance boundaries.
- Engineering lifecycle.
- Requirements transformation contract.
- Agent responsibility model.
- Verification principles.
- Project artifact conventions.

### 14.2 Planned Capabilities

- Executable workflow orchestration.
- Reusable operational agent definitions.
- PRD and SRS generation skills.
- Automated requirement extraction.
- PRD-to-SRS transformation tooling.
- Requirement traceability validation.
- System design generation workflows.
- Web and mobile development integrations.
- Automated quality gates.
- Multi-project framework evaluation.

Planned capabilities must not be represented as operational until implemented and verified.

---

## 15. Architectural Conformance

An implementation conforms to the PREZEKC AI architecture when it:

1. Respects the authority and approval model.
2. Uses defined workflow dependencies.
3. Preserves approved requirements baselines.
4. Maintains requirement traceability.
5. Applies relevant verification gates.
6. Records material changes and decisions.
7. Reports execution outcomes accurately.
8. Enforces platform-specific requirements when applicable.

Conformance must be evaluated through actual artifacts and recorded verification evidence.

The presence of framework documentation alone does not establish operational conformance.

---

## Related Specifications

- [Agent Operating Contract](AGENTS.md)
- [Governance Protocol](core/governance.md)
- [Engineering Workflow Protocol](core/workflow.md)
- [Verification and Quality Protocol](core/verification.md)

---

**PREZEKC AI Framework — Architecture Specification v0.1.0**

<!-- PREZEKC-V020-EXTENSION: DO NOT DUPLICATE -->
## v0.2.0 Operating Extension — Lightweight Agentic Engineering

PREZEKC preserves P01–P09, six logical engineering roles, and its controlled PRD → SRS → design dependency chain. v0.2.0 adds **import-first requirements**, an explicit **SDD + UI/UX Flow → Task Breakdown** handoff, **progressive skill loading**, and **human-guided next actions**.

PRD and SRS remain required controlled artifacts when applicable; they may be created using external editors or AI systems and then imported in the supported format. The validated content still requires semantic review and separate approvals. Optional authoring within PREZEKC remains supported.

See [Import-First](docs/import-mode.md), [Next Action](core/next-action.md), [UI/UX Flow](skills/ui-ux-flow/SKILL.md), and [Task Breakdown](skills/task-breakdown/SKILL.md).
