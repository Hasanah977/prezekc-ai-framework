
# Web Application Delivery Workflow

## Purpose

Define the controlled delivery process for web applications
developed under the PREZEKC AI Framework.

This workflow coordinates requirements engineering, design,
implementation, verification, and deployment.

It does not prescribe a programming language or web framework.

## Applicability

Use for:

- Public-facing websites.
- Administrative applications.
- Transactional web systems.
- Web applications backed by APIs.
- Backend services with web interfaces.

For API-only systems, omit non-applicable UI activities
and document the exclusion.

## Roles

| Role | Responsibility |
|---|---|
| Research Analyst | Comparative research and evidence |
| System Analyst | Current-state analysis |
| Requirements Engineer | Requirements, PRD, SRS, traceability |
| System Architect | Architecture and design |
| Development Engineer | Implementation and developer tests |
| Verification Engineer | Independent verification and reporting |
| Project Owner | Scope, baseline, and release decisions |

One person may fulfill multiple roles when permitted.
Approval authority must remain explicit.

## Stage 1 — System Analysis

**Skill:** `system-analysis`

**Entry:** Project objective and investigation scope identified.

**Activities:**

1. Examine existing workflows and stakeholders.
2. Identify system boundaries and information flows.
3. Record operational problems.
4. Document evidence and uncertainty.

**Output:** Existing System Analysis Report.

**Exit:** Findings and unresolved evidence gaps are recorded.

## Stage 2 — Comparative Study

**Skill:** `comparative-study`

**Entry:** Relevant problem context established.

**Activities:**

1. Select comparable systems.
2. Define evaluation criteria.
3. Examine reliable sources.
4. Record capability comparisons.
5. Identify supported gaps and limitations.

**Output:** Comparative Study Report.

**Exit:** Conclusions are traceable to documented evidence.

## Stage 3 — Requirement Analysis

**Skill:** `requirement-analysis`

**Entry:** Available project findings and stakeholder input.

**Activities:**

1. Consolidate user and business needs.
2. Define scope and constraints.
3. Classify requirement candidates.
4. Identify priorities and dependencies.
5. Resolve or record conflicts.

**Output:** Requirement Analysis Document.

**Exit:** Requirement candidates are ready for PRD engineering.

## Stage 4 — Product Requirements

**Skill:** `prd-generation`

**Entry:** Requirements analysis available.

**Activities:**

1. Define product goals and target users.
2. Establish scope and exclusions.
3. Document product capabilities.
4. Define acceptance outcomes.
5. Verify consistency and traceability.
6. Submit the PRD for approval.

**Output:** Product Requirements Document.

**Exit:** Approved PRD baseline.

Do not proceed to final SRS engineering without
the required PRD approval.

## Stage 5 — Software Requirements

**Skill:** `prd-to-srs`

**Entry:** Approved PRD baseline.

**Activities:**

1. Extract approved requirements.
2. Define system boundaries.
3. Decompose functional requirements.
4. Specify quality and interface requirements.
5. Define acceptance criteria.
6. Establish PRD-to-SRS traceability.
7. Verify and submit the specification.

**Outputs:**

- Software Requirements Specification.
- Requirement Traceability Matrix.

**Exit:** Approved SRS baseline.

## Stage 6 — System Design

**Skill:** `system-design`

**Entry:** Approved SRS and current RTM.

**Activities:**

1. Establish architecture drivers.
2. Evaluate technical alternatives.
3. Define component responsibilities.
4. Design data structures and persistence.
5. Specify API and integration contracts.
6. Design UI/UX where applicable.
7. Define security and deployment architecture.
8. Update design traceability.

**Outputs:**

- System Design Specification.
- Architecture Decision Records, where required.
- Updated RTM.

**Exit:** Approved implementation design.

## Stage 7 — Implementation

**Skill:** `web-development`

**Entry:** Approved design and assigned implementation scope.

**Activities:**

1. Inspect the repository and existing conventions.
2. Map requirements to affected components.
3. Implement backend and frontend changes.
4. Apply database migrations where authorized.
5. Maintain interface and data contracts.
6. Implement applicable developer tests.
7. Record implementation references in the RTM.

**Outputs:**

- Source changes.
- Migrations and configuration changes, where applicable.
- Developer test results.
- Updated RTM.

**Exit:** Implementation ready for independent verification.

## Stage 8 — Verification

**Skill:** `testing`

**Entry:** Identifiable build and applicable requirements.

**Activities:**

1. Establish verification scope.
2. Prepare and execute test cases.
3. Verify functional and quality requirements.
4. Check security and authorization.
5. Evaluate browser and responsive behavior.
6. Record defects and test evidence.
7. Review requirement coverage.

**Outputs:**

- Verification Report.
- Defect Register.
- Updated RTM.

**Exit:** Mandatory verification conditions satisfied
or an authorized exception recorded.

## Stage 9 — Deployment

**Skill:** `deployment`

**Entry:** Release-ready artifact and release authorization.

**Activities:**

1. Review release readiness.
2. Prepare target infrastructure.
3. Verify configuration and migration prerequisites.
4. Establish rollback or recovery.
5. Deploy the approved artifact.
6. Execute post-deployment checks.
7. Record final release disposition.

**Outputs:**

- Release Manifest.
- Deployment Record.
- Post-Deployment Verification Report.

**Exit:** Release accepted by the designated authority.

## Change Control

Requirements changes must be reviewed against the
approved baseline before implementation.

For each approved change:

1. Identify affected PRD and SRS requirements.
2. Assess design and interface impacts.
3. Identify affected implementation components.
4. Update relevant tests.
5. Execute required reverification.
6. Record revised artifact versions.

Emergency changes remain subject to the applicable
governance and evidence requirements.

## Delivery Conditions

The workflow is complete only when:

- Required baselines have recorded approval.
- Implementation conforms to the applicable design.
- Mandatory verification evidence is available.
- Requirement traceability is current.
- Deployment status is recorded.
- Outstanding risks and exceptions are disclosed.

An incomplete stage must not be represented as complete.

## References

- [Framework Architecture](../FRAMEWORK.md)
- [Governance](../core/governance.md)
- [Workflow Protocol](../core/workflow.md)
- [Verification Protocol](../core/verification.md)
