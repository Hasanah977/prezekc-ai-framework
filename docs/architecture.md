
# PREZEKC AI — Framework Architecture

**Specification:** Internal Architecture
**Version:** 0.1.0
**Status:** Draft
**Scope:** Framework Structure and Component Integration

## 1. Purpose

This document defines the internal organization of PREZEKC AI,
the responsibilities of its components, and the relationships
between engineering activities and their artifacts.

It supplements `FRAMEWORK.md` with repository-level
architecture and integration requirements.

Authority, lifecycle transitions, and verification policy
remain defined by the corresponding core specifications.

## 2. Architecture Model

PREZEKC AI is a repository-based engineering framework
composed of instructions, operational procedures, document
templates, workflow definitions, and validation utilities.

The framework separates five concerns:

1. Governance and execution authority.
2. Engineering role responsibilities.
3. Task-specific procedures.
4. Lifecycle orchestration.
5. Artifact verification and traceability.

The separation prevents project-specific decisions from
being embedded in reusable framework instructions.

### 2.1 Component Responsibilities

| Component | Responsibility |
|---|---|
| `AGENTS.md` | Agent operating contract |
| `FRAMEWORK.md` | Framework-wide engineering specification |
| `core/` | Governance, lifecycle, and verification protocols |
| `agents/` | Engineering role contracts |
| `skills/` | Task-specific execution procedures |
| `rules/` | Cross-cutting operational and documentation rules |
| `templates/` | Engineering artifact structures |
| `workflows/` | Project delivery sequences |
| `docs/` | Supporting architectural documentation |
| `tools/` | Executable framework utilities |
| `tests/` | Automated tests for framework utilities |

Components must reference existing authoritative rules
rather than independently redefining them.

## 3. Repository Structure

```text
prezekc-ai-framework/
├── AGENTS.md
├── FRAMEWORK.md
├── README.md
├── core/
│   ├── governance.md
│   ├── workflow.md
│   └── verification.md
├── agents/
├── skills/
│   └── <skill-name>/
│       └── SKILL.md
├── rules/
│   ├── global-rules.md
│   └── documentation-rules.md
├── templates/
├── workflows/
├── docs/
│   └── architecture.md
├── tools/
│   └── validate_framework.py
└── tests/
    └── test_validate_framework.py
```

The structure identifies component locations.
Individual files are maintained according to their
respective contracts.

Additional modules require a defined responsibility,
integration point, and maintenance owner.

## 4. Execution Model

PREZEKC AI defines how engineering work is conducted.
It does not independently provide an autonomous agent
runtime, persistent execution service, or deployment engine.

Execution requires an AI assistant or engineering operator
capable of accessing the relevant repository, project
artifacts, and authorized tools.

The execution sequence is:

1. Read the operating contract.
2. Identify the requested engineering activity.
3. Establish the applicable project context.
4. Load the relevant role and skill specifications.
5. Verify required inputs and permissions.
6. Execute the defined procedure.
7. Produce the required artifacts.
8. Perform applicable verification.
9. Report results, limitations, and unresolved decisions.

Tool availability must be established in the active
execution environment.

A documented procedure must not be represented as an
implemented automation unless an executable mechanism
exists and has been verified.

## 5. Governance and Authority

The operating contract establishes general agent behavior.

Governance determines:

- Decision authority.
- Approval requirements.
- Baseline ownership.
- Change authorization.
- Escalation conditions.

Lifecycle protocols determine permitted transitions
between engineering phases.

Verification protocols establish evidence requirements
and acceptance checks.

In the event of conflicting instructions, execution
must follow the applicable authority rules in
`core/governance.md`.

Agents and skills cannot grant themselves additional
authority through local instructions.

## 6. Engineering Roles

The framework defines six engineering roles.

| Role | Responsibility |
|---|---|
| Research Analyst | Comparative research and source evaluation |
| System Analyst | Existing-system and operational analysis |
| Requirements Engineer | Requirement analysis, PRD, SRS, and traceability |
| System Architect | Technical architecture and system design |
| Development Engineer | Software implementation and developer testing |
| Verification Engineer | Independent verification and evidence assessment |

Role definitions reside in `agents/`.

A role specifies accountability and operating limits.
A skill specifies the procedure for an assigned activity.

One operator may perform multiple roles when permitted.
Required approval authority must remain identifiable.

## 7. Skill Architecture

Each skill resides in a dedicated directory.

```text
skills/
└── system-analysis/
    └── SKILL.md
```

A skill file must provide machine-readable frontmatter
followed by an operational procedure.

Minimum metadata:

```yaml
---
name: system-analysis
description: >
  Analyze current-state business processes and document
  evidence-backed operational findings.
---
```

The directory name and declared skill name must match.

A skill should establish:

- Activation conditions.
- Required inputs.
- Execution procedure.
- Output contract.
- Verification requirements.
- Failure handling.
- Applicable references.

Skills must not redefine approval authority or
requirements baselines.

## 8. Lifecycle Architecture

The framework organizes engineering work into nine phases.

| Phase | Activity | Primary Output |
|---|---|---|
| P01 | System Analysis | Existing System Analysis |
| P02 | Comparative Study | Comparative Study Report |
| P03 | Requirement Analysis | Requirement Analysis Document |
| P04 | Product Requirements | PRD |
| P05 | Software Requirements | SRS and RTM |
| P06 | System Design | System Design Specification |
| P07 | Implementation | Source and build artifacts |
| P08 | Verification | Verification evidence and report |
| P09 | Deployment and Maintenance | Release and operational records |

The lifecycle is governed by `core/workflow.md`.

Project workflows may define platform-specific activities
without changing mandatory baseline requirements.

Iteration and change requests must preserve traceability
to the affected approved artifacts.

## 9. Artifact Dependencies

The primary engineering artifact chain is:

```text
System Analysis
       |
       v
Comparative Study
       |
       v
Requirement Analysis
       |
       v
      PRD
       |
       v
      SRS
       |
       v
System Design
       |
       v
Implementation
       |
       v
Verification
       |
       v
Deployment
```

This diagram represents the principal documentation
and delivery sequence.

Earlier artifacts may be revised through authorized
change control.

Not every operational task requires regeneration of
all preceding artifacts. Impact assessment determines
the required work.

## 10. Requirements Traceability

The Requirement Traceability Matrix records
relationships between engineering artifacts.

The minimum relationship model is:

```text
Requirement Source
       |
       v
PRD Requirement
       |
       v
SRS Requirement
       |
       v
Design Element
       |
       v
Implementation Reference
       |
       v
Test Case
```

A requirement may have multiple downstream mappings.
A downstream artifact may satisfy multiple requirements.

Mappings must reference actual artifacts.

Unavailable design, implementation, or test references
remain pending until the relevant artifacts exist.

The RTM is a traceability record, not evidence that
an unexecuted verification has passed.

## 11. Document Templates

Templates define the expected structure of engineering
artifacts.

They do not independently establish:

- Requirement validity.
- Stakeholder approval.
- Architecture correctness.
- Implementation conformance.
- Test success.

An instantiated template must include project-specific
content and supporting evidence.

The responsible skill determines how the document is
prepared and reviewed.

## 12. Project Integration

PREZEKC AI may be applied to an existing repository
or a newly initiated software project.

Integration requires:

1. Identification of the target repository.
2. Inspection of existing architecture and conventions.
3. Identification of available project documentation.
4. Selection of applicable skills and workflow.
5. Establishment of project-specific constraints.
6. Confirmation of available tools and permissions.

Framework instructions must not override project
requirements without authorization.

Existing systems require change-impact assessment
before implementation.

## 13. Platform Boundaries

The framework supports delivery procedures for:

- Web applications.
- Backend services.
- Native Android applications.
- Native iOS applications.
- Cross-platform mobile applications.

Platform-specific design and verification remain
separate from common requirements engineering.

Cross-platform implementation does not imply
equivalent runtime behavior on every target.

Compatibility claims require platform-specific evidence.

## 14. Validation Architecture

Executable validation utilities are maintained in `tools/`.

Automated tests for those utilities reside in `tests/`.

The initial framework validator checks structural
properties including:

- Required repository elements.
- Skill frontmatter.
- Skill naming consistency.
- Local Markdown references.
- Basic document structure.

Validation coverage is limited to implemented checks.

Structural validation does not establish semantic
correctness, document approval, or implementation quality.

Additional validators must define their inputs,
expected outputs, failure conditions, and test coverage.

## 15. Extension Requirements

A new framework component must have:

- A distinct responsibility.
- An identifiable owner or governing role.
- Defined input and output contracts.
- Integration with existing components.
- Applicable validation requirements.
- Documentation references that resolve correctly.

Before introducing a component, verify that its function
is not already provided by an existing module.

Avoid unnecessary duplication of lifecycle instructions.

## 16. Architectural Constraints

The framework must remain:

- Independent of a single programming language.
- Applicable to multiple software delivery platforms.
- Explicit about tool and environment dependencies.
- Traceable across requirements and implementation.
- Compatible with human approval and review.
- Verifiable through recorded evidence.
- Extensible without redefining core authority.

An architectural change affecting these constraints
requires review under the governance protocol.

## 17. Related Specifications

- [Framework Specification](../FRAMEWORK.md)
- [Agent Operating Contract](../AGENTS.md)
- [Governance Protocol](../core/governance.md)
- [Workflow Protocol](../core/workflow.md)
- [Verification Protocol](../core/verification.md)
- [Global Rules](../rules/global-rules.md)
- [Documentation Rules](../rules/documentation-rules.md)
