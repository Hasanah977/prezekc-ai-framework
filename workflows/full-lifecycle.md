
# PREZEKC AI — Full Engineering Lifecycle

## 1. Purpose

Define the execution sequence, artifact dependencies, and handoff conditions for engineering work performed under PREZEKC AI.

This workflow coordinates the framework's nine lifecycle phases.

Governance and verification requirements are defined by `core/governance.md` and `core/verification.md`. This workflow does not override those specifications.

## 2. Applicability

Use this workflow for projects requiring an end-to-end engineering process, including:

- Web applications.
- Backend services.
- Native Android applications.
- Native iOS applications.
- Cross-platform applications.

For an existing project, identify the available approved baselines before determining the necessary entry phase.

Do not recreate upstream artifacts solely to complete a documentation sequence.

## 3. Project Initialization

Before beginning lifecycle work, establish:

| Item | Required Information |
|---|---|
| Project identity | Name and objective |
| Project owner | Authorized decision authority |
| Repository | Location and current state |
| Delivery target | Web, Android, iOS, cross-platform, or backend |
| Existing artifacts | Documents, source, design, and tests |
| Constraints | Known technical and operational limitations |
| Execution environment | Available tools and permissions |

Record unavailable information as an open issue when it affects execution.

## 4. Lifecycle Stages

| Phase | Responsible Role | Procedure | Primary Artifact |
|---|---|---|---|
| P01 | System Analyst | `system-analysis` | Existing System Analysis |
| P02 | Research Analyst | `comparative-study` | Comparative Study Report |
| P03 | Requirements Engineer | `requirement-analysis` | Requirement Analysis Document |
| P04 | Requirements Engineer | `prd-generation` | PRD |
| P05 | Requirements Engineer | `prd-to-srs` | SRS and RTM |
| P06 | System Architect | `system-design` | System Design Specification |
| P07 | Development Engineer | `web-development` or `mobile-development` | Implementation |
| P08 | Verification Engineer | `testing` | Verification Report |
| P09 | Authorized release roles | `deployment` | Release and Operational Records |

The complete skill path follows the pattern `skills/<skill-name>/SKILL.md`.

## 5. Execution Sequence

### P01 — Existing System Analysis

**Entry conditions**

- Investigation objective is identifiable.
- Current process or system boundary can be established.
- Available evidence sources are identified.

**Execution**

1. Examine existing operations.
2. Identify stakeholders and responsibilities.
3. Reconstruct current workflows.
4. Register problems and constraints.
5. Evaluate evidence gaps.
6. Verify the analysis report.

**Output**

- Existing System Analysis Report.
- Problem Register.
- Evidence and Assumption Registers.

**Exit condition**

Findings and limitations are recorded sufficiently to support subsequent analysis.

### P02 — Comparative Study

**Entry conditions**

- Research objective is established.
- Relevant problem context is available.

**Execution**

1. Select comparison candidates.
2. Define evaluation criteria.
3. Inspect relevant sources.
4. Record evidence-backed findings.
5. Identify supported gaps.
6. Verify research conclusions.

**Output**

- Comparative Study Report.
- Source Register.
- Comparison Matrix.
- Gap Register.

**Exit condition**

Comparison conclusions are traceable to identifiable evidence.

### P03 — Requirement Analysis

**Entry conditions**

- Problem context is available.
- Relevant stakeholder information can be identified.
- Existing research findings are accessible where applicable.

**Execution**

1. Consolidate source findings.
2. Identify stakeholder needs.
3. Record business rules.
4. Classify requirement candidates.
5. Establish priorities and dependencies.
6. Register conflicts and open decisions.
7. Review requirement origins.

**Output**

- Requirement Analysis Document.
- Requirement Inventory.
- Source and Dependency Registers.

**Exit condition**

Requirement candidates and unresolved decisions are available for product definition.

### P04 — Product Requirements

**Entry conditions**

- Project objectives are established.
- Relevant needs and scope constraints are available.

**Execution**

1. Define product goals.
2. Establish intended users and scope.
3. Define product requirements.
4. Record priorities and acceptance outcomes.
5. Review source traceability.
6. Submit the PRD for authorization.

**Output**

- Product Requirements Document.
- PRD Requirement Register.
- Approval Record.

**Exit condition**

An approved PRD baseline exists before final SRS derivation.

An unapproved PRD may support exploratory work but not final requirements baselining.

### P05 — Software Requirements

**Entry conditions**

- Approved PRD baseline is available.
- PRD requirement identifiers are stable.

**Execution**

1. Validate the source baseline.
2. Extract approved requirements.
3. Define system boundaries.
4. Decompose product requirements.
5. Define functional and quality requirements.
6. Establish acceptance criteria.
7. Generate the RTM.
8. Verify SRS coverage and consistency.
9. Submit the SRS for authorization.

**Output**

- Software Requirements Specification.
- Requirement Traceability Matrix.
- Requirements Coverage Report.

**Exit condition**

An approved SRS baseline is available for controlled system design.

### P06 — System Design

**Entry conditions**

- Approved SRS is available.
- Applicable constraints and RTM are accessible.

**Execution**

1. Identify architecture drivers.
2. Evaluate relevant alternatives.
3. Define architecture and component responsibilities.
4. Design required behavior and data structures.
5. Specify APIs and integrations.
6. Specify UI/UX and platform behavior where applicable.
7. Record architecture decisions.
8. Update traceability.
9. Review and submit the design.

**Output**

- System Design Specification.
- Architecture Decision Records, where required.
- Updated RTM.

**Exit condition**

The applicable implementation design is approved.

### P07 — Implementation

**Entry conditions**

- Applicable requirements and design baselines are approved.
- Assigned implementation scope is established.
- Repository and execution environment are available.

**Execution**

1. Inspect the existing project.
2. Map requirements to implementation components.
3. Implement approved behavior.
4. Maintain interface and data integrity.
5. Add or update applicable developer tests.
6. Execute available development checks.
7. Update implementation references in the RTM.

**Output**

- Source changes.
- Configuration or migration changes, where applicable.
- Developer verification evidence.
- Updated RTM.

**Exit condition**

The assigned implementation is ready for independent verification.

### P08 — Verification

**Entry conditions**

- Identifiable implementation artifact is available.
- Relevant SRS requirements and acceptance criteria exist.
- Applicable execution environments are established.

**Execution**

1. Identify verification scope.
2. Derive and review test cases.
3. Execute applicable tests.
4. Record actual results.
5. Register confirmed defects.
6. Retest corrections where required.
7. Evaluate requirement coverage.
8. Prepare the verification report.

**Output**

- Verification Report.
- Test Execution Records.
- Defect Register.
- Updated RTM.

**Exit condition**

Mandatory verification conditions are satisfied or an authorized exception is recorded.

### P09 — Deployment and Maintenance

**Entry conditions**

- Release artifact is identifiable.
- Applicable verification has been reviewed.
- Deployment target and release authority are established.
- Recovery requirements have been assessed.

**Execution**

1. Confirm release readiness.
2. Prepare the target environment.
3. Verify migration and recovery procedures.
4. Deploy the approved artifact.
5. Execute post-deployment checks.
6. Record release disposition.
7. Monitor operational findings.
8. Process defects and change requests through applicable controls.

**Output**

- Release Manifest.
- Deployment Record.
- Post-Deployment Verification.
- Operational and Maintenance Records.

**Exit condition**

The release outcome is documented and accepted by the designated authority.

Maintenance continues as required; P09 is not a declaration that the software will require no further changes.

## 6. Baseline Management

Controlled baselines include:

- Approved PRD.
- Approved SRS.
- Approved System Design Specification.
- Authorized release artifact.

Each baseline must have an identifiable version and approval reference.

Verification success does not establish human approval.

A downstream phase must not silently alter an approved upstream baseline.

## 7. Traceability Requirements

Maintain mappings between:

1. Stakeholder needs and product requirements.
2. Product requirements and system requirements.
3. System requirements and design elements.
4. Design elements and implementation artifacts.
5. System requirements and verification evidence.

Update the RTM when authorized changes affect existing mappings.

Do not generate placeholder identifiers for nonexistent downstream artifacts.

## 8. Change Handling

When a proposed change affects an approved baseline:

1. Identify the change and its source.
2. Determine affected requirements.
3. Assess design and implementation impact.
4. Identify affected tests and release artifacts.
5. Obtain the required decision.
6. Update authorized documents and source.
7. Execute affected verification.
8. Record revised versions and outcomes.

The governing change-control rules remain authoritative.

## 9. Exception Handling

An incomplete phase may produce a provisional artifact.

Provisional artifacts must identify:

- Unverified assumptions.
- Missing decisions.
- Incomplete requirements.
- Blocked verification.
- Unsupported dependencies.

A provisional artifact must not be represented as an approved baseline.

Independent work may continue when permitted and technically safe.

## 10. Completion and Handoff

Every phase handoff must include:

| Field | Required Content |
|---|---|
| Phase | Completed lifecycle phase |
| Source | Input artifacts and versions |
| Output | Produced artifacts and versions |
| Verification | Checks performed and results |
| Approval | Required decision and current status |
| Traceability | Updated mappings |
| Open Issues | Unresolved findings |
| Next Activity | Receiving role or phase |

A receiving role must inspect the handoff before relying on its artifacts.

## 11. Related Workflows

Use the appropriate delivery specialization:

- [Web Application Workflow](web-application.md)
- [Mobile Application Workflow](mobile-application.md)

Specialized workflows may add platform checks and release requirements. They must not bypass mandatory lifecycle controls.

## 12. Governing References

- [Agent Operating Contract](../AGENTS.md)
- [Framework Specification](../FRAMEWORK.md)
- [Governance Protocol](../core/governance.md)
- [Workflow Protocol](../core/workflow.md)
- [Verification Protocol](../core/verification.md)
- [Global Rules](../rules/global-rules.md)
- [Documentation Rules](../rules/documentation-rules.md)
