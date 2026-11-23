---
name: system-design
description: >
  Transform an approved Software Requirements Specification into
  an implementable system design. Use when defining software
  architecture, components, UML diagrams, data models, database
  schemas, API contracts, UI/UX specifications, security boundaries,
  deployment topology, or platform-specific design decisions.
  Preserves SRS-to-design traceability and produces a controlled
  System Design Specification for implementation.
version: 0.1.0
category: system-engineering
---

# System Design Engineering

## Purpose

Translate an approved Software Requirements Specification
(SRS) into a coherent, implementable, and verifiable
technical design.

The design must describe how the system will satisfy
established requirements without changing their
approved meaning or introducing unsupported capabilities.

This skill implements Phase P06 of the PREZEKC AI
engineering lifecycle.

System design is a controlled engineering activity,
not an unrestricted architecture-generation task.

## Activation

Use this skill when:

- Preparing a System Design Specification.
- Translating SRS requirements into architecture.
- Designing software components and responsibilities.
- Creating relevant UML or process diagrams.
- Designing conceptual and physical data models.
- Defining database structures and constraints.
- Specifying API and integration contracts.
- Designing application navigation and UI/UX.
- Establishing web or mobile architecture.
- Reviewing an existing design against an approved SRS.
- Revising architecture after an authorized change.

Do not use this skill to:

- Generate an SRS from product requirements.
- Add product capabilities without authorization.
- Replace approved business rules.
- Write production implementation code.
- Approve its own architecture baseline.
- Claim platform compatibility without verification.

For requirements decomposition, use `prd-to-srs`.

For implementation, hand off to `development-engineer`.

## Preconditions

A controlled system design requires:

- Approved SRS baseline.
- Identifiable SRS version.
- Recorded approval authority.
- Requirement Traceability Matrix.
- Project objectives and scope.
- Known technical and operational constraints.
- Target platform information.

Conditional inputs:

- Approved PRD.
- Existing architecture documentation.
- Existing source code.
- Existing database schema.
- External integration specifications.
- Security and privacy policies.
- UI/UX references.
- Infrastructure constraints.
- Approved Architecture Decision Records.
- Approved change requests.

If the SRS has not been approved, exploratory design
may be prepared when explicitly requested.

Such output must remain `DRAFT` and must not become
an implementation baseline.

## Design Invariants

The following rules are mandatory:

1. Every design decision must have a valid justification.
2. Mandatory SRS requirements must receive design coverage.
3. The design must preserve approved business rules.
4. Component responsibilities must remain identifiable.
5. Data and interface contracts must remain consistent.
6. Security boundaries must reflect approved requirements.
7. Unsupported product capabilities must not be introduced.
8. Architectural assumptions must remain explicit.
9. Requirement identifiers must remain stable.
10. Verification and human approval remain independent.

Design elements may satisfy multiple SRS requirements.

A single SRS requirement may require multiple design elements.

All relationships must be recorded explicitly.

## Design Artifact Model

Use the following identifier conventions:

| Identifier | Artifact |
|---|---|
| `SRS-FR-*` | Functional system requirement |
| `SRS-NFR-*` | Non-functional system requirement |
| `DES-*` | Design element |
| `CMP-*` | Software component |
| `DATA-*` | Data entity or data model element |
| `API-*` | Interface contract |
| `UI-*` | User interface element or screen |
| `ADR-*` | Architecture Decision Record |
| `CHG-*` | Controlled change request |
| `TC-*` | Test case |

Identifiers are references, not substitutes
for complete specifications.

Approved identifiers must not be reassigned
to unrelated artifacts.

## Procedure

### SD01 — Validate the SRS Baseline

Inspect the source specification before making
architectural decisions.

Confirm:

- SRS document identifier and version.
- Approval record.
- Functional requirement inventory.
- Non-functional requirements.
- Approved business rules.
- Required data and integrations.
- Security and access constraints.
- Target operating environments.
- Known dependencies.
- Unresolved requirement issues.

Do not silently resolve contradictory requirements
through architectural choices.

Escalate material conflicts to the
Requirements Engineer or Project Owner.

### SD02 — Establish the System Context

Identify the system boundary and its environment.

Document:

- Internal responsibilities.
- External actors.
- External systems and services.
- Information exchanges.
- Trust boundaries.
- Operational environments.
- Deployment constraints.
- Platform targets.

Distinguish system-owned behavior from
responsibilities belonging to external services.

Do not assume an integration exists merely because
a comparable product implements it.

### SD03 — Extract Architecture Drivers

Identify requirements that materially influence
the architecture.

Architecture drivers may include:

- Functional complexity.
- Security and privacy.
- Data consistency.
- Availability and reliability.
- Performance and scalability.
- Offline operation.
- Integration constraints.
- Accessibility.
- Platform compatibility.
- Maintainability.
- Deployment limitations.

Trace each driver to an approved SRS requirement
or an authorized technical constraint.

Do not invent numerical performance targets.

If a critical quality target is unavailable,
register the unresolved decision.

### SD04 — Evaluate Architecture Alternatives

Identify reasonable architectural approaches.

Evaluate alternatives using criteria derived
from the project requirements.

Typical considerations include:

- Requirement coverage.
- Architectural complexity.
- Maintainability.
- Operational cost.
- Security.
- Performance characteristics.
- Integration compatibility.
- Team capabilities.
- Deployment environment.
- Long-term extensibility.

Document the rationale for the recommended option.

Avoid introducing microservices, distributed systems,
message brokers, or other infrastructure solely
because they appear architecturally sophisticated.

Choose the simplest architecture that adequately
satisfies established constraints.

### SD05 — Define the Architecture

Specify the selected logical architecture.

The design must identify:

- Architectural style.
- Major subsystems.
- System layers.
- Component boundaries.
- Dependency direction.
- Communication mechanisms.
- Data ownership.
- Error boundaries.
- Relevant external services.

A component must have a clear responsibility.

Do not distribute the same authoritative business
logic across unrelated components without justification.

### SD06 — Design Software Components

Assign stable component identifiers.

For each significant component, record:

```yaml
component_id: CMP-001
name: "Component name"
responsibility: "Primary responsibility"
related_requirements:
  - SRS-FR-001.1
inputs: []
outputs: []
dependencies: []
owned_data: []
failure_conditions: []
status: PROPOSED
```

Component definitions must describe observable
responsibilities and explicit interfaces.

Avoid speculative components that are not required
by the approved architecture.

### SD07 — Model System Behavior

Develop behavioral models where they clarify
requirements and implementation responsibilities.

Supported diagram types include:

- Use Case Diagram.
- Activity Diagram.
- Sequence Diagram.
- State Machine Diagram.
- Component Diagram.
- Deployment Diagram.
- Data Flow Diagram.

Select diagrams based on the actual problem.

For each diagram, specify:

- Diagram identifier.
- Purpose.
- Participating actors or components.
- Relevant SRS requirements.
- Assumptions.
- Expected behavior.
- Exceptional behavior where applicable.

Diagram content must agree with the SRS.

Do not invent process steps to complete a diagram.

### SD08 — Design the Data Model

Derive data structures from approved
data and functional requirements.

Identify:

1. Data entities.
2. Attributes and data types.
3. Primary identifiers.
4. Relationships and cardinalities.
5. Uniqueness constraints.
6. Referential integrity.
7. Validation constraints.
8. Ownership and access boundaries.
9. Retention and deletion requirements.
10. Relevant indexing and performance concerns.

Distinguish conceptual entities from
physical database implementation.

Produce an ERD when relational data relationships
are relevant to the system.

Do not force relational modeling onto projects
that use another justified persistence model.

### SD09 — Define Database Architecture

Where persistent storage is required, specify:

- Database technology and rationale.
- Logical schema.
- Tables or collections.
- Keys and constraints.
- Transaction boundaries.
- Migration considerations.
- Data consistency requirements.
- Backup and recovery concerns.
- Access controls.

Database implementation must remain consistent
with the conceptual data model.

Avoid adding fields or entities that introduce
unsupported business behavior.

### SD10 — Specify API and Integration Contracts

For each required external or internal interface,
define:

- Interface identifier.
- Owning component.
- Purpose.
- Authentication and authorization.
- Input contract.
- Output contract.
- Validation behavior.
- Error conditions.
- Data format.
- Relevant compatibility requirements.
- Related SRS identifiers.

Example interface specification:

```yaml
interface_id: API-001
name: "Example interface"
owner: CMP-001
method: GET
path: "/example"
authentication: REQUIRED
authorization: "Approved access policy"
request_schema: null
response_schema: null
error_conditions: []
related_requirements:
  - SRS-FR-001.1
status: PROPOSED
```

The example defines a documentation structure,
not an implemented endpoint.

Choose concrete URLs, response codes, and schemas
only when supported by the approved design context.

### SD11 — Define Security Architecture

Identify security boundaries across:

- Authentication.
- Authorization.
- Sensitive data access.
- Data storage.
- External communication.
- Session management.
- Input validation.
- Audit logging.
- Error disclosure.
- Secret management.

Security mechanisms must correspond to
identified risks, policies, and system requirements.

Do not assume that authentication alone
provides sufficient authorization.

For sensitive systems, document applicable
privacy and data protection requirements.

### SD12 — Design UI/UX

When the system includes user interfaces,
derive screen and interaction requirements
from approved SRS behavior.

Specify:

- Information architecture.
- Navigation structure.
- User roles and available views.
- Screen responsibilities.
- Forms and validation.
- Loading states.
- Empty states.
- Success and error states.
- Confirmation interactions.
- Accessibility.
- Responsive or adaptive behavior.

Use stable identifiers:

```text
UI-001
UI-002
UI-003
```

Each significant screen or interaction must
reference relevant system requirements.

Visual preferences may inform design decisions,
but must not override accessibility or required
system behavior.

Do not assume the user has approved an interface
because a mockup has been generated.

### SD13 — Apply Platform-Specific Design

Select platform requirements based on the
approved project profile.

#### Web

Consider:

- Frontend and backend boundaries.
- Client-server communication.
- Responsive layouts.
- Browser compatibility.
- Authentication and session handling.
- API integration.
- Caching and data consistency.
- Deployment architecture.

#### Android

Consider:

- Application structure.
- Android lifecycle behavior.
- Navigation.
- Device permissions.
- Local storage.
- API integration.
- Offline requirements.
- SDK compatibility.
- Build and distribution constraints.

#### iOS

Consider:

- Application structure.
- iOS lifecycle behavior.
- Navigation.
- Device permissions.
- Local storage.
- API integration.
- SDK compatibility.
- Signing and distribution constraints.

#### Cross-Platform

Evaluate:

- Shared code boundaries.
- Native platform integrations.
- Platform-specific permissions.
- Navigation conventions.
- Device compatibility.
- Build configuration.
- Independent Android and iOS verification.

A shared codebase does not establish equivalent
runtime behavior across platforms.

#### Backend/API

Consider:

- Service boundaries.
- Interface contracts.
- Data persistence.
- Authentication and authorization.
- Transaction consistency.
- Observability.
- Fault handling.
- Operational deployment.

Do not include platform-specific components
that the project does not require.

### SD14 — Define Deployment Architecture

Specify the intended deployment environment.

Where applicable, document:

- Application runtime.
- Infrastructure components.
- Network boundaries.
- Database services.
- External integrations.
- Configuration management.
- Secrets handling.
- Monitoring.
- Backup and recovery.
- Release dependencies.

Differentiate planned deployment from
verified operational infrastructure.

Do not claim deployment readiness from
an architecture diagram alone.

### SD15 — Record Architecture Decisions

Create Architecture Decision Records
for consequential technical decisions.

Use the following structure:

```yaml
decision_id: ADR-001
title: "Decision title"
status: PROPOSED
context: "Problem and constraints"
related_requirements: []
alternatives: []
selected_option: null
rationale: null
consequences: []
approved_by: null
```

A decision is not approved merely because
the System Architect recommends it.

Significant changes to approved architecture
must follow the change-control protocol.

### SD16 — Update Requirement Traceability

Map each significant design element
to its originating system requirements.

Example:

```text
SRS-FR-001.1
      |
      +-- DES-001
      |      |
      |      +-- CMP-001
      |
      +-- UI-001
```

Update the Requirement Traceability Matrix.

Record:

- SRS requirement.
- Design element.
- Component reference.
- Data reference where applicable.
- Interface or UI reference where applicable.
- Coverage status.
- Unresolved gaps.

Implementation and test references may remain
`PENDING` until their artifacts exist.

Do not create fictitious implementation
or test references to complete the matrix.

### SD17 — Perform Design Review

Evaluate the resulting design for:

1. SRS conformance.
2. Functional coverage.
3. Quality attribute coverage.
4. Component responsibility consistency.
5. Data model integrity.
6. Interface compatibility.
7. Security boundaries.
8. Failure and exception handling.
9. Platform compatibility.
10. Deployment feasibility.
11. Requirement traceability.
12. Open decisions and assumptions.

Use the design verification gate defined in
`core/verification.md`.

Resolve or disclose material inconsistencies.

### SD18 — Submit for Approval

Set the System Design Specification to
`IN_REVIEW` when mandatory checks are complete.

The Project Owner or designated technical
authority must approve consequential
architecture decisions.

A verified design is not automatically
an approved implementation baseline.

## Output Contract

Primary artifact:

`System Design Specification`

Required supporting artifact:

`Updated Requirement Traceability Matrix`

Conditional artifacts:

- Architecture Decision Records.
- System Context Diagram.
- Component Diagram.
- Use Case Diagram.
- Activity Diagram.
- Sequence Diagram.
- State Machine Diagram.
- Entity Relationship Diagram.
- Logical Database Schema.
- API Contract Specification.
- UI/UX Specification.
- Deployment Diagram.
- Security Architecture.
- Architecture Risk Register.

Generate only the artifacts relevant to
approved system requirements.

Use `templates/system-design.md` as the
primary document structure.

## Quality Gate

The design is ready for review when:

- [ ] An approved SRS baseline is referenced.
- [ ] System boundaries are defined.
- [ ] Architecture drivers are identified.
- [ ] Major architectural decisions have rationale.
- [ ] Components have explicit responsibilities.
- [ ] Relevant behavior is modeled consistently.
- [ ] Data structures satisfy applicable requirements.
- [ ] Interface contracts are defined where required.
- [ ] Security boundaries are considered.
- [ ] UI/UX design covers applicable user interactions.
- [ ] Target platform constraints are documented.
- [ ] Deployment assumptions are explicit.
- [ ] Mandatory SRS requirements have design coverage.
- [ ] Unapproved product capabilities are absent.
- [ ] Remaining risks and open issues are recorded.
- [ ] Applicable verification checks pass.

A passing quality gate permits submission
for human review.

It does not constitute architecture approval.

## Failure Handling

Return `BLOCKED` for finalization when:

- Approved SRS is unavailable.
- Critical system requirements contradict each other.
- Mandatory business rules are unresolved.
- Essential integration contracts cannot be established.
- Critical architecture constraints remain unknown.
- Necessary scope changes lack authorization.

Return `PARTIAL` when a useful provisional design
can be produced but mandatory verification
or approval remains incomplete.

Do not invent architecture decisions to
conceal missing requirements.

## Worked Example

Illustrative SRS requirement:

```yaml
id: SRS-FR-001.2
statement: >
  The system shall retrieve consolidated records
  for the reporting period selected by an
  authorized reporting user.
status: APPROVED
```

Possible design element:

```yaml
design_id: DES-001
name: "Reporting Query Flow"
related_requirements:
  - SRS-FR-001.2
components:
  - CMP-001
interfaces:
  - API-001
status: PROPOSED
```

Possible component:

```yaml
component_id: CMP-001
name: "Reporting Service"
responsibility: >
  Coordinate authorized retrieval of
  consolidated reporting records.
related_requirements:
  - SRS-FR-001.2
status: PROPOSED
```

These records demonstrate traceability.

They do not establish a real architecture,
working API, database implementation,
or verified application behavior.

## Handoff

Next role:

`development-engineer`

Required handoff:

```yaml
skill: system-design
source_artifact: SRS
source_version: "1.0"
output_artifacts:
  - system-design-specification
  - requirement-traceability-matrix
design_status: IN_REVIEW
verification_status: NOT_RUN
architecture_decisions: []
unresolved_issues: []
approved_by: null
```

Replace placeholders with actual records.

Implementation against a final baseline requires
the applicable approved SRS and design.

## Governing Specifications

- [Agent Operating Contract](../../AGENTS.md)
- [Framework Architecture](../../FRAMEWORK.md)
- [System Architect](../../agents/system-architect.md)
- [Governance Protocol](../../core/governance.md)
- [Workflow Protocol](../../core/workflow.md)
- [Verification Protocol](../../core/verification.md)
