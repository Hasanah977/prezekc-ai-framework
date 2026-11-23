
# Mobile Application Delivery Workflow

## Purpose

Define the controlled delivery process for Android, iOS,
and cross-platform mobile applications under PREZEKC AI.

Shared requirements and application logic may be reused.
Platform-specific conformance must be assessed independently.

## Applicability

This workflow supports:

- Native Android applications.
- Native iOS applications.
- Cross-platform Android and iOS applications.
- Mobile applications with backend API integrations.

The target platforms and development approach must be
established through approved project requirements and design.

## Roles

| Role | Responsibility |
|---|---|
| Research Analyst | Comparative research |
| System Analyst | Operational and stakeholder analysis |
| Requirements Engineer | Requirements and specification baselines |
| System Architect | Mobile architecture and platform decisions |
| Development Engineer | Application implementation |
| Verification Engineer | Test coverage and platform verification |
| Project Owner | Scope, approval, and release authority |

## Stage 1 — System Analysis

**Skill:** `system-analysis`

Identify current processes, users, operational conditions,
available evidence, and relevant problems.

**Output:** Existing System Analysis Report.

**Exit:** Current-state findings are documented.

## Stage 2 — Comparative Study

**Skill:** `comparative-study`

Evaluate relevant mobile products or alternative solutions.

Examine supported capabilities, workflow constraints,
platform behavior, and documented limitations.

**Output:** Comparative Study Report.

**Exit:** Research conclusions have traceable sources.

## Stage 3 — Requirement Analysis

**Skill:** `requirement-analysis`

Identify:

- User and business needs.
- Device and platform constraints.
- Connectivity assumptions.
- Data protection obligations.
- Required integrations.
- Accessibility needs.
- Relevant offline scenarios.

Do not introduce device capabilities without
a supporting stakeholder need.

**Output:** Requirement Analysis Document.

**Exit:** Requirement candidates are ready for PRD development.

## Stage 4 — Product Requirements

**Skill:** `prd-generation`

Define:

- Product objectives.
- Target users.
- Supported platforms.
- Product capabilities.
- Release scope.
- Acceptance outcomes.
- Known constraints.

**Output:** Product Requirements Document.

**Exit:** Approved PRD baseline.

## Stage 5 — Software Requirements

**Skill:** `prd-to-srs`

Define verifiable requirements for:

- Application behavior.
- Authentication and authorization.
- Navigation and validation.
- Data management.
- Network operations.
- Device integrations.
- Permissions.
- Platform compatibility.
- Offline behavior, if required.
- Error and recovery conditions.

**Outputs:**

- Software Requirements Specification.
- Requirement Traceability Matrix.

**Exit:** Approved SRS baseline.

## Stage 6 — Mobile System Design

**Skill:** `system-design`

Evaluate the approved implementation approach:

- Native Android.
- Native iOS.
- Shared cross-platform architecture.

Design the application according to the approved SRS.

Required design concerns may include:

1. Application layers and component responsibilities.
2. Navigation and application state.
3. Local and remote data boundaries.
4. API contracts.
5. Authentication and secure storage.
6. Lifecycle behavior.
7. Device permissions.
8. Offline synchronization.
9. Platform-specific UI behavior.
10. Build and distribution architecture.

**Outputs:**

- System Design Specification.
- Relevant architecture and interface specifications.
- Updated RTM.

**Exit:** Approved mobile implementation design.

## Stage 7 — Implementation

**Skill:** `mobile-development`

Inspect the project and implement the assigned features.

Maintain:

- Approved component boundaries.
- Platform-specific integration contracts.
- Required UI and interaction behavior.
- Data validation.
- Network failure handling.
- Authorization and data protection.
- Existing architecture conventions.

Cross-platform implementations must distinguish shared
application logic from native platform behavior.

**Outputs:**

- Application source changes.
- Platform configurations.
- Developer tests.
- Updated RTM.

**Exit:** Implementation ready for verification.

## Stage 8 — Android Verification

**Skill:** `testing`

Required when Android is a target.

Evaluate applicable:

- Android build.
- Installation and startup.
- Supported SDK compatibility.
- Application navigation.
- Lifecycle handling.
- Permission behavior.
- Local persistence.
- API integration.
- Functional test coverage.
- Device-specific behavior.

Record emulator and physical-device results separately
when both environments are used.

**Output:** Android Verification Record.

**Exit:** Required Android checks satisfy release criteria.

## Stage 9 — iOS Verification

**Skill:** `testing`

Required when iOS is a target.

Evaluate applicable:

- iOS build.
- Installation and startup.
- Supported iOS compatibility.
- Application navigation.
- Lifecycle handling.
- Permission behavior.
- Local persistence.
- API integration.
- Functional test coverage.
- Device-specific behavior.

Identify simulator, physical-device, and build-only checks.

An unavailable Apple build environment must be recorded
as a verification limitation.

**Output:** iOS Verification Record.

**Exit:** Required iOS checks satisfy release criteria.

## Stage 10 — Cross-Platform Assessment

Required when the project targets both Android and iOS.

Review:

- Shared functional behavior.
- Platform-specific differences.
- Supported operating system versions.
- Native integrations.
- UI consistency where specified.
- Known platform defects.
- Independent verification outcomes.

A passing Android result does not establish iOS conformance,
and the reverse is equally true.

**Output:** Cross-Platform Compatibility Assessment.

**Exit:** Mandatory target-platform coverage is accounted for.

## Stage 11 — Release Preparation

**Skill:** `deployment`

Prepare release artifacts for the approved distribution channels.

Android may require:

- Signed release artifact.
- Version code and version name.
- Distribution configuration.
- Required store declarations.

iOS may require:

- Signed application archive.
- Bundle identifier and version.
- Provisioning and entitlements.
- Authorized distribution access.

Store policies and publication status must be verified
against the relevant distribution platform.

**Output:** Release Readiness Record.

**Exit:** Release authorization obtained.

## Stage 12 — Distribution and Validation

**Skill:** `deployment`

Execute the authorized distribution procedure.

Record:

- Artifact identifiers.
- Target channels.
- Submitted versions.
- Distribution status.
- Installation verification.
- Post-release findings.

A store submission does not establish publication.

**Outputs:**

- Distribution Record.
- Platform Release Status.
- Post-Release Verification Report.

**Exit:** Final release disposition recorded.

## Change Control

Changes affecting shared or native modules must be
evaluated for each supported platform.

Update the affected:

- Requirements.
- Architecture.
- Native integration contracts.
- Shared components.
- Platform configuration.
- Tests.
- Release artifacts.

Reverification must cover the platforms affected
by the change.

## Delivery Conditions

Delivery is complete when:

- Required baselines are approved.
- Assigned functionality is implemented.
- Mandatory Android verification is complete, if applicable.
- Mandatory iOS verification is complete, if applicable.
- Cross-platform constraints are accounted for.
- Applicable release authorization is recorded.
- Distribution status is confirmed.
- Traceability and residual risks are documented.

## References

- [Framework Architecture](../FRAMEWORK.md)
- [Governance](../core/governance.md)
- [Workflow Protocol](../core/workflow.md)
- [Verification Protocol](../core/verification.md)
