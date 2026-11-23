
---
name: testing
description: >
  Plan, implement, execute, and report software verification
  against approved requirements. Use for unit, integration,
  system, API, UI, security, regression, and platform-specific
  testing, including defect investigation and release evidence.
---

# Software Testing

## Scope

Verify implemented software against approved requirements,
design contracts, and applicable acceptance criteria.

Testing establishes evidence of conformance within the scope
of executed checks. It does not establish correctness for
unexamined behavior.

Lifecycle phase: `P08`.

## Inputs

Required:

- Approved SRS baseline.
- Applicable design specification.
- Implemented software or an accessible build.
- Requirement Traceability Matrix.
- Defined verification environment.
- Applicable acceptance criteria.

Additional inputs:

- Source repository and change history.
- Existing test suites.
- Interface specifications.
- Test data.
- Platform configurations.
- Known defect register.

Missing prerequisites must be recorded before execution.

## Responsibilities

The Verification Engineer is responsible for test planning,
execution, defect reporting, and evidence assessment.

Development Engineers may implement tests and resolve defects.
They must not represent unexecuted tests as passing.

Approval authority remains defined by project governance.

## Procedure

### 1. Establish Verification Scope

Identify the requirements and components affected by the
implementation or change.

Determine:

- Required verification levels.
- Critical business rules.
- Authorization boundaries.
- Data integrity concerns.
- External dependencies.
- Target environments.
- Regression exposure.

Use the RTM to identify coverage obligations.

### 2. Review Testability

Inspect each applicable requirement for:

- Observable expected behavior.
- Preconditions.
- Inputs.
- Expected outputs.
- Failure conditions.
- Applicable quality thresholds.

Report ambiguous or contradictory requirements.

Do not invent acceptance thresholds to make a requirement
testable.

### 3. Prepare the Test Plan

Define:

- Test objectives.
- Test levels and methods.
- Execution environments.
- Test data requirements.
- Dependencies.
- Entry and exit criteria.
- Defect severity criteria.
- Evidence collection method.

Select tests according to requirement risk and change impact.

### 4. Derive Test Cases

Assign a stable identifier to each test case.

Use `TC-*` identifiers.

A test case must identify:

| Field | Requirement |
|---|---|
| ID | Unique test identifier |
| Requirement | Applicable SRS identifier |
| Objective | Behavior being verified |
| Preconditions | Required starting state |
| Input | Test data or action |
| Procedure | Reproducible execution steps |
| Expected Result | Observable acceptance condition |
| Environment | Applicable execution target |

Cover successful and unsuccessful behavior where relevant.

Do not derive test expectations from the implementation
when they conflict with the approved specification.

### 5. Prepare Test Environments

Verify:

- Required dependencies are available.
- Configuration is consistent with the test plan.
- Test data is isolated from production where applicable.
- External services are controlled or explicitly identified.
- Relevant platform versions are recorded.

Mocked or simulated integrations must be identified.

Results from a mocked environment do not establish
production integration behavior.

### 6. Execute Verification

Run applicable checks:

1. Static analysis and formatting.
2. Unit tests.
3. Integration tests.
4. API and contract tests.
5. System and end-to-end tests.
6. Security-focused checks.
7. Accessibility and UI checks.
8. Performance checks where required.
9. Regression tests.
10. Platform-specific tests.

The order may change according to project risk and
environment constraints.

Record actual commands, test versions, environment
details, and results.

### 7. Record Outcomes

Use the following execution states:

- `PASS`: Expected behavior was observed.
- `FAIL`: Observed behavior violates the expectation.
- `BLOCKED`: A prerequisite prevented execution.
- `NOT_RUN`: Execution was not attempted.
- `INCONCLUSIVE`: Evidence does not establish an outcome.

Do not substitute source inspection for runtime execution
unless the verification method permits inspection.

### 8. Manage Defects

Assign a stable `DEF-*` identifier.

Each defect record must include:

- Observed behavior.
- Expected behavior.
- Reproduction steps.
- Affected environment.
- Related requirement.
- Severity.
- Evidence.
- Current disposition.

Distinguish confirmed defects from suspected causes.

Retest corrected defects and assess regression exposure.

### 9. Evaluate Coverage

Compare executed verification against the RTM.

Identify:

- Requirements without tests.
- Tests without valid requirement references.
- Failed mandatory tests.
- Blocked test coverage.
- Unverified quality requirements.

Coverage percentages must be calculated from real records.

A high coverage percentage does not override a critical
failed requirement.

### 10. Prepare Verification Report

Report:

- Scope and tested baseline.
- Environment.
- Executed test cases.
- Results and evidence.
- Defect status.
- Coverage gaps.
- Residual risks.
- Release recommendation.

The recommendation must distinguish engineering evidence
from human authorization.

## Evidence Requirements

Verification evidence may include:

- Test runner output.
- Build logs.
- Static analysis reports.
- API response records.
- Screenshots.
- Device or simulator records.
- Performance measurements.
- Defect reproduction records.

Evidence must be attributable to the tested artifact
and execution environment.

Do not fabricate evidence or modify test output to
conceal failures.

## Completion Criteria

Verification is complete for the assigned scope when:

- Applicable tests have recorded outcomes.
- Required evidence is available.
- Defects have documented dispositions.
- RTM coverage is updated.
- Mandatory failures and blocked checks are disclosed.
- The verification report identifies release implications.

Test completion does not constitute release approval.

## Failure Handling

Stop the affected verification when:

- The target build cannot be identified.
- Required test data is unavailable.
- The environment is unsafe or unauthorized.
- Acceptance criteria materially conflict.
- Evidence integrity cannot be maintained.

Continue independent checks where feasible.

## Handoff

Deliver the verification report and updated RTM to the
designated release authority.

Include unresolved defects, blocked checks, and residual risks.

## References

- [Agent Contract](../../AGENTS.md)
- [Verification Engineer](../../agents/verification-engineer.md)
- [Verification Protocol](../../core/verification.md)
- [Governance](../../core/governance.md)
- [Workflow](../../core/workflow.md)
