---
name: mobile-development
description: >
  Implement and maintain native or cross-platform mobile
  applications targeting Android and iOS. Use for application
  architecture, device integration, navigation, local storage,
  API integration, platform builds, and mobile verification.
---

# Mobile Development

Implement mobile applications in accordance with approved
software requirements, platform constraints, and architecture.

Supported targets include Android, iOS, and cross-platform
applications using an approved technology stack.

This skill operates within lifecycle phase `P07`.

## Preconditions

Required:

- Approved SRS and System Design Specification.
- Defined mobile platform targets.
- Approved technology and application architecture.
- Implementation scope and acceptance criteria.
- Available SDK, build tools, and test environments.

Determine whether the project requires:

- Android only.
- iOS only.
- Independent native applications.
- A shared cross-platform implementation.

Do not assume cross-platform development is appropriate
without evaluating system requirements.

## Platform Selection

Use the technology selected during architecture approval.

Native development may use:

- Kotlin and the Android SDK.
- Swift and the iOS SDK.

Cross-platform development may use:

- Flutter.
- React Native.
- Another approved framework.

These are supported approaches, not mandatory dependencies.

Architecture decisions must account for native integrations,
runtime behavior, operational constraints, and maintainability.

## Implementation Procedure

### 1. Inspect the Application

Identify:

- Project structure and module ownership.
- Dependency and SDK versions.
- Application entry points.
- State management conventions.
- Navigation architecture.
- Network and persistence layers.
- Platform-specific modules.
- Build and signing configuration.
- Existing test infrastructure.

Preserve established application conventions.

### 2. Establish Platform Contracts

For each target platform, determine:

- Minimum supported operating system.
- Required device capabilities.
- Permission requirements.
- Application lifecycle behavior.
- Network connectivity assumptions.
- Offline behavior, if specified.
- Data storage and protection requirements.
- Distribution constraints.

Do not invent compatibility guarantees.

### 3. Implement Application Behavior

Implement approved features according to their SRS mappings.

Maintain clear boundaries between:

- Presentation.
- Application state.
- Business behavior.
- Data access.
- External services.
- Platform-specific integrations.

Use existing architectural conventions unless an approved
change requires otherwise.

### 4. Implement Navigation and UI

Follow the approved mobile UI/UX specification.

Account for:

- Screen navigation.
- Back navigation and restoration.
- Loading and empty states.
- Input validation.
- Success and failure feedback.
- Accessibility.
- Different screen dimensions.
- Platform interaction conventions.

Do not assume Android and iOS share identical navigation
or permission behavior.

### 5. Implement Data and Network Operations

Where applicable:

- Validate external data.
- Handle connection failures and timeouts.
- Preserve data consistency.
- Avoid duplicate submissions or transactions.
- Protect authentication credentials.
- Respect data retention requirements.
- Implement offline behavior only when specified.

Sensitive information must not be exposed through logs,
insecure storage, or unintended application state.

### 6. Integrate Device Capabilities

Device integrations may include camera, location,
notifications, local files, biometrics, or sensors.

Only request capabilities required by the approved SRS.

For each integration:

1. Identify the relevant requirement.
2. Determine the platform permissions.
3. Implement unavailable or denied-permission behavior.
4. Handle lifecycle and interruption conditions.
5. Verify behavior on the applicable platform.

Do not request unnecessary device permissions.

### 7. Maintain Native Boundaries

For cross-platform applications, isolate platform-specific
behavior behind documented interfaces when appropriate.

Do not duplicate shared business behavior without
an architectural justification.

Platform-specific modules must preserve their intended
contracts with the shared application layer.

### 8. Implement Tests

Test coverage should address:

- Business logic.
- Application state.
- Navigation behavior.
- Input validation.
- Data persistence.
- Network errors.
- Authorization.
- Platform integrations.
- Relevant regression scenarios.

Tests must be mapped to applicable SRS requirements.

## Android Verification

When Android is a target, evaluate:

- Dependency resolution.
- Android build completion.
- Package installation.
- Application startup.
- Supported SDK behavior.
- Permission handling.
- Navigation and lifecycle behavior.
- Network and storage operations.
- Relevant device compatibility.

Record whether verification occurred on an emulator,
physical device, or through build-only checks.

Do not infer runtime correctness from a successful build.

## iOS Verification

When iOS is a target, evaluate:

- Dependency resolution.
- iOS build completion.
- Simulator or device installation.
- Application startup.
- Supported iOS behavior.
- Permission handling.
- Navigation and lifecycle behavior.
- Network and storage operations.
- Signing and distribution constraints.

A compatible Apple build environment may be required
for native compilation and signing.

If the required environment is unavailable, record
the affected verification as `BLOCKED` or `NOT_RUN`.

Do not claim iOS compatibility based on Android results.

## Cross-Platform Verification

Maintain separate verification records for Android and iOS.

Shared test results may support common business logic,
but do not replace platform-specific build and runtime checks.

Report platform outcomes independently.

## Release Boundaries

Production distribution requires:

- Applicable build verification.
- Required functional and security checks.
- Platform-specific release configuration.
- Signing and distribution prerequisites.
- Review of unresolved defects.
- Human release authorization.

Do not publish an application or distribute production
builds without the required approval.

## Deliverables

Provide:

- Mobile application source changes.
- Platform configuration changes.
- Relevant automated tests.
- Build and verification records.
- Platform compatibility findings.
- Updated requirement mappings.
- Known limitations.

Implementation and verification evidence must be
recorded separately for each required platform.

## Completion Criteria

The assigned scope is complete when:

- Approved requirements are implemented.
- Application behavior matches the relevant design.
- Applicable tests have acceptable results.
- Required platform checks are recorded.
- No mandatory unresolved failures are concealed.
- Requirement traceability is current.
- Remaining compatibility limitations are explicit.

A platform cannot be reported as verified when its
mandatory checks have not been executed.

## Failure Handling

Stop the affected work when:

- Required authorization is missing.
- Approved platform requirements conflict.
- Necessary device capabilities cannot be supported.
- Critical integrations cannot be verified.
- Implementation requires unapproved scope expansion.

Continue independent, safe work where possible.

## Handoff

Transfer the implementation to the Verification Engineer.

Include:

- Requirement identifiers.
- Changed application components.
- Android verification status.
- iOS verification status.
- Executed tests and evidence.
- Outstanding defects.
- Environment limitations.

Do not combine separate platform results into an
unsupported overall success claim.

## Governing Specifications

- [Agent Contract](../../AGENTS.md)
- [Development Engineer](../../agents/development-engineer.md)
- [Governance](../../core/governance.md)
- [Workflow](../../core/workflow.md)
- [Verification](../../core/verification.md)

<!-- PREZEKC-V030-EXTENSION: DO NOT DUPLICATE -->
## v0.3.0 — Modern Mobile Code Quality

Check installed SDK, language, and library versions before using APIs. Keep state, domain logic, storage, and network/synchronization responsibilities appropriately separated. Use [code-quality](../code-quality/SKILL.md) for substantive changes, [ui-design](../ui-design/SKILL.md) for visuals, and [security-review](../security-review/SKILL.md) when handling login, permissions, local data, or sync. Prefer unit/widget/integration tests based on available devices and project stack; mark missing device checks `NOT_RUN`.
