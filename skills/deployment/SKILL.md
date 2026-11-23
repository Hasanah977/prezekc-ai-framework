---
name: deployment
description: >
  Prepare, authorize, execute, verify, and document software
  deployments. Use for web releases, backend services, database
  migrations, Android distribution, iOS distribution, rollback
  planning, and post-deployment validation.
---

# Software Deployment

## Scope

Deploy verified software to an authorized target environment
using a controlled and recoverable release procedure.

Lifecycle phase: `P09`.

A successful deployment command does not establish
operational readiness.

## Preconditions

Required:

- Identifiable release artifact or source revision.
- Approved deployment target.
- Applicable verification report.
- Release acceptance criteria.
- Authorized release decision.
- Deployment and rollback procedure.
- Configuration and dependency inventory.

Additional requirements depend on the target platform.

Do not modify production infrastructure or release software
without explicit authorization.

## Release Identification

Every release must identify:

- Project and release version.
- Source revision.
- Build artifact.
- Target environment.
- Applicable requirements baseline.
- Verification reference.
- Release approver.
- Deployment operator.

Use immutable artifact references where supported.

Do not deploy an artifact whose provenance cannot
be established.

## Procedure

### 1. Review Release Readiness

Evaluate:

- Verification results.
- Open defects.
- Security findings.
- Dependency risks.
- Data migration requirements.
- Infrastructure compatibility.
- Rollback feasibility.
- Monitoring readiness.

Block the release when mandatory acceptance conditions
are not satisfied.

A documented exception requires the appropriate authority.

### 2. Prepare the Target Environment

Verify:

- Runtime and dependency compatibility.
- Configuration availability.
- Required service connections.
- Network and access controls.
- Secret provisioning.
- Storage requirements.
- Monitoring configuration.
- Recovery prerequisites.

Do not copy development credentials into production.

### 3. Prepare Data Changes

For database or persistent data changes:

1. Inspect the current schema and migration history.
2. Determine compatibility with existing application versions.
3. Identify destructive or irreversible operations.
4. Establish backup and recovery requirements.
5. Determine migration ordering.
6. Verify the migration procedure in an appropriate environment.

Do not run destructive production migrations without
specific authorization and recovery planning.

### 4. Prepare the Release Artifact

Build using the approved toolchain.

Confirm:

- Intended source revision.
- Required environment configuration.
- Dependency resolution.
- Artifact identity.
- Relevant build verification.
- Signing requirements where applicable.

Record artifact checksums or immutable identifiers
when supported by the delivery platform.

### 5. Establish Rollback or Recovery

Document the recovery procedure before deployment.

Include:

- Conditions that trigger rollback.
- Responsible operator.
- Previous known-good application version.
- Data compatibility constraints.
- Restoration prerequisites.
- Verification after recovery.

If rollback is not feasible, document the limitation
and obtain explicit authorization before proceeding.

### 6. Execute Deployment

Follow the approved environment-specific procedure.

Record:

- Execution time.
- Operator.
- Commands or deployment actions.
- Artifact version.
- Configuration revision.
- Migration results.
- Immediate deployment outcome.

Stop on unexpected behavior that threatens data
integrity, security, or service availability.

### 7. Verify the Deployment

Perform applicable post-deployment checks:

- Application availability.
- Startup and health checks.
- Critical functional paths.
- Database connectivity.
- Authentication and authorization.
- External integration connectivity.
- Logging and monitoring.
- Error rates and operational alerts.

Use actual observations.

Do not mark production behavior as verified
based only on staging results.

### 8. Resolve Deployment Failures

When mandatory post-deployment checks fail:

1. Record the failure.
2. Determine operational impact.
3. Initiate approved rollback or recovery.
4. Preserve evidence.
5. Verify the recovered environment.
6. Report the release disposition.

Do not improvise destructive recovery commands.

### 9. Close the Release

Publish the release record only after its final
disposition has been established.

Record:

- Deployed version.
- Environment.
- Verification evidence.
- Known limitations.
- Incident or rollback references.
- Approval and closure status.

## Web and Backend Targets

Account for:

- Application runtime.
- Reverse proxy and network configuration.
- TLS termination.
- Environment variables and secrets.
- Database connectivity.
- Background processing.
- Cache compatibility.
- Health monitoring.
- Data migrations.

Implementation details depend on the approved architecture.

## Android Targets

Account for:

- Application identifier.
- Version code and version name.
- Release build configuration.
- Signing configuration.
- Supported SDK range.
- Required permissions.
- Distribution channel.
- Store policy and review requirements.

Distribution is complete only when the relevant channel
confirms the intended release state.

Do not infer publication from a successful package build.

## iOS Targets

Account for:

- Bundle identifier.
- Version and build number.
- Signing certificates.
- Provisioning configuration.
- Entitlements.
- Supported iOS versions.
- Distribution channel.
- Store review requirements.

Native iOS signing and distribution require an appropriate
Apple development environment and authorized credentials.

Do not claim a release was published before confirmation.

## Completion Criteria

A deployment is complete when:

- The approved artifact reached the intended environment.
- Required post-deployment checks have recorded outcomes.
- Data changes have been assessed and verified.
- Monitoring and recovery status are documented.
- Release disposition is recorded.
- The appropriate authority has accepted the outcome.

An unsuccessful deployment must remain recorded
even when rollback succeeds.

## Failure Handling

Return `BLOCKED` when:

- Release authorization is missing.
- Artifact provenance is uncertain.
- Mandatory verification has failed.
- Critical environment dependencies are unavailable.
- Necessary recovery measures are absent.
- Signing or distribution prerequisites are unavailable.

Do not bypass release gates to complete a deployment.

## Deliverables

- Release Manifest.
- Deployment Execution Record.
- Post-Deployment Verification Report.
- Migration Record, if applicable.
- Rollback or Recovery Record, if applicable.
- Updated release status.

## References

- [Agent Contract](../../AGENTS.md)
- [Governance](../../core/governance.md)
- [Workflow](../../core/workflow.md)
- [Verification](../../core/verification.md)
