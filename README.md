<div align="center">

# PREZEKC AI Framework

**Requirements-Driven AI-Assisted Software Engineering**

![Version](https://img.shields.io/badge/version-0.1.0-blue?style=flat-square)
![Release](https://img.shields.io/badge/release-candidate-orange?style=flat-square)
![Python](https://img.shields.io/badge/python-3.12%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Platforms](https://img.shields.io/badge/platform-web%20%7C%20android%20%7C%20ios-3DDC84?style=flat-square)
[![CI](https://img.shields.io/github/actions/workflow/status/Hasanah977/prezekc-ai-framework/framework-validation.yml?style=flat-square&label=CI&logo=githubactions&logoColor=white)](https://github.com/Hasanah977/prezekc-ai-framework/actions)
![Stars](https://img.shields.io/github/stars/Hasanah977/prezekc-ai-framework?style=flat-square&logo=github)
![Last Commit](https://img.shields.io/github/last-commit/Hasanah977/prezekc-ai-framework?style=flat-square)

A repository-based engineering framework for managing software development from system analysis<br>
through requirements specification, architecture, implementation, verification, and delivery.

[📖 Overview](#overview) · [🧭 Lifecycle](#engineering-lifecycle) · [🛠️ Validation Tools](#validation-tools) · [🚀 Getting Started](#getting-started) · [🗺️ Roadmap](#development-roadmap)

</div>

---

PREZEKC AI provides engineering contracts, reusable procedures, document templates, controlled workflows, and executable validation utilities.

The framework is technology-agnostic and operates with compatible AI assistants or engineering teams. It does not include an autonomous agent runtime.

## Contents

- [Overview](#overview)
- [Engineering Lifecycle](#engineering-lifecycle)
- [Framework Architecture](#framework-architecture)
- [Engineering Roles](#engineering-roles)
- [Skills and Workflows](#skills-and-workflows)
- [Requirements Engineering](#requirements-engineering)
- [Validation Tools](#validation-tools)
- [Getting Started](#getting-started)
- [Repository Structure](#repository-structure)
- [Verification and Release Status](#verification-and-release-status)
- [Limitations](#limitations)
- [Development Roadmap](#development-roadmap)
- [Documentation](#documentation)
- [License](#license)

---

## Overview

AI-assisted software development requires more than generating source code. Requirements must originate from identifiable needs, technical decisions must remain consistent with approved specifications, and deliverables must be supported by verification evidence.

PREZEKC AI establishes a controlled operating model based on six principles:

| Principle | Requirement |
|---|---|
| Evidence-Based Analysis | Findings must be supported by identifiable sources or observations. |
| Requirements-Driven Development | Product capabilities must originate from documented needs or approved decisions. |
| Human Authority | Project owners retain control over scope, baselines, architecture approval, and releases. |
| Requirement Traceability | Dependencies between requirements and engineering artifacts must be maintained. |
| Controlled Change | Changes to approved baselines require impact assessment and authorization. |
| Verified Delivery | Completion claims must be supported by recorded verification results. |

The framework separates engineering procedures from project-specific implementation decisions.

## Engineering Lifecycle

PREZEKC AI defines nine engineering phases.

| Phase | Activity | Primary Deliverable |
|---|---|---|
| P01 | Existing System Analysis | Existing System Analysis Report |
| P02 | Comparative Study | Comparative Study Report |
| P03 | Requirement Analysis | Requirement Analysis Document |
| P04 | Product Requirements | Product Requirements Document (PRD) |
| P05 | Software Requirements | Software Requirements Specification (SRS) and RTM |
| P06 | System Design | System Design Specification |
| P07 | Implementation | Source code and build artifacts |
| P08 | Verification | Test results and verification report |
| P09 | Deployment and Maintenance | Release and operational records |

The principal artifact dependency is:

```text
Existing System Analysis
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
     Owner Approval
          |
          v
         SRS
          |
     Owner Approval
          |
          v
    System Design
          |
     Design Approval
          |
          v
   Implementation
          |
          v
     Verification
          |
   Release Authorization
          |
          v
Deployment and Maintenance
```

The sequence represents the controlled delivery model. Iteration and maintenance changes are permitted through the applicable change-control procedure.

For existing projects, the required entry phase is determined by the available approved baselines and the scope of the requested change.

See [Full Engineering Lifecycle](workflows/full-lifecycle.md).

## Framework Architecture

PREZEKC AI separates framework authority from execution procedures and verification.

| Layer | Location | Responsibility |
|---|---|---|
| Operating Contract | `AGENTS.md` | Agent behavior, authority boundaries, and reporting |
| Framework Specification | `FRAMEWORK.md` | Engineering model and framework principles |
| Core Protocols | `core/` | Governance, lifecycle, and verification rules |
| Engineering Roles | `agents/` | Responsibilities and handoff contracts |
| Engineering Skills | `skills/` | Task-specific execution procedures |
| Operating Rules | `rules/` | Shared engineering and documentation rules |
| Document Templates | `templates/` | Standard artifact structures |
| Delivery Workflows | `workflows/` | Lifecycle and platform-specific sequences |
| Validation Utilities | `tools/` | Executable structural and requirements checks |
| Automated Tests | `tests/` | Verification of validation utilities |
| Examples | `examples/` | Test fixtures and engineering examples |

Specifications define the required behavior. Python utilities implement only the checks explicitly supported by their code.

The framework does not assume that an AI assistant can access external systems, execute commands, or deploy software unless those capabilities are available and authorized in its execution environment.

See [Internal Architecture](docs/architecture.md).

## Engineering Roles

Six logical engineering roles are defined.

| Role | Responsibility |
|---|---|
| [Research Analyst](agents/research-analyst.md) | Comparative research and evidence evaluation |
| [System Analyst](agents/system-analyst.md) | Current-state processes, stakeholders, and problem analysis |
| [Requirements Engineer](agents/requirements-engineer.md) | Requirements analysis, PRD, SRS, and traceability |
| [System Architect](agents/system-architect.md) | Architecture, system components, data, and interface design |
| [Development Engineer](agents/development-engineer.md) | Implementation and developer-level verification |
| [Verification Engineer](agents/verification-engineer.md) | Independent verification, defect reporting, and evidence assessment |

Roles are operating contracts rather than independently running processes.

A compatible AI assistant may perform multiple roles sequentially, subject to the applicable governance rules.

## Skills and Workflows

### Engineering Skills

The framework provides ten reusable skills.

| Skill | Location | Primary Function |
|---|---|---|
| System Analysis | `skills/system-analysis/` | Existing-system investigation |
| Comparative Study | `skills/comparative-study/` | Evidence-based solution comparison |
| Requirement Analysis | `skills/requirement-analysis/` | Stakeholder needs and requirement candidates |
| PRD Generation | `skills/prd-generation/` | Product requirements preparation |
| PRD-to-SRS | `skills/prd-to-srs/` | Controlled software requirement decomposition |
| System Design | `skills/system-design/` | Architecture and design specification |
| Web Development | `skills/web-development/` | Web application implementation |
| Mobile Development | `skills/mobile-development/` | Android, iOS, and cross-platform implementation |
| Testing | `skills/testing/` | Test planning, execution, and reporting |
| Deployment | `skills/deployment/` | Controlled release and deployment procedures |

Each skill contains a `SKILL.md` defining its activation conditions, inputs, procedure, deliverables, verification requirements, and failure handling.

### Delivery Workflows

| Workflow | Document |
|---|---|
| Full Engineering Lifecycle | [full-lifecycle.md](workflows/full-lifecycle.md) |
| Web Application Delivery | [web-application.md](workflows/web-application.md) |
| Mobile Application Delivery | [mobile-application.md](workflows/mobile-application.md) |

Workflows coordinate engineering activities. Skills define how individual activities are performed.

## Requirements Engineering

Requirements engineering is a central component of PREZEKC AI.

### Product Requirements Document

The PRD establishes product objectives, scope, target users, priorities, capabilities, and acceptance outcomes.

A PRD must have an identifiable approval record before it becomes the authoritative source for final SRS generation.

### Software Requirements Specification

The SRS describes observable and testable system behavior derived from the approved PRD.

Requirements may address functional behavior, quality attributes, data, interfaces, validation, authorization, and failure conditions.

### Requirement Traceability Matrix

The RTM preserves relationships between engineering artifacts.

```text
PRD-FR-001
    |
    +-- SRS-FR-001.1
    |       |
    |       +-- DES-001
    |               |
    |               +-- Implementation Reference
    |               |
    |               +-- TC-001
    |
    +-- SRS-FR-001.2
```

Every mandatory PRD requirement must be accounted for during SRS decomposition.

Every SRS requirement must have an authorized origin.

Missing downstream artifacts remain pending. Traceability references must not be fabricated to imply completed implementation or verification.

### Document Templates

The repository includes templates for:

- Existing System Analysis.
- Comparative Study.
- Requirement Analysis.
- PRD.
- SRS.
- Requirement Traceability Matrix.
- System Design.

Templates define structure. They do not independently establish requirement correctness, technical feasibility, or stakeholder approval.

## Validation Tools

PREZEKC AI includes three Python validation utilities.

| Utility | Responsibility |
|---|---|
| `validate_framework.py` | Repository structure, skill metadata, and local Markdown references |
| `extract_requirements.py` | Controlled extraction of PRD, SRS, and RTM Markdown into JSON |
| `validate_requirements.py` | Requirements identifiers, baselines, coverage, and traceability mappings |

These utilities use the Python Standard Library.

### Framework Validation

```bash
python tools/validate_framework.py --strict
```

The validator checks structural properties of the framework repository.

### Requirements Extraction

```bash
python tools/extract_requirements.py \
  --prd examples/markdown/prd.md \
  --srs examples/markdown/srs.md \
  --rtm examples/markdown/rtm.md \
  --output build/requirements
```

The extractor reads the supported Markdown structure and writes JSON manifests.

The output directory must not contain existing manifests with the same names. Use a new directory for subsequent extraction runs.

### Requirements Validation

```bash
python tools/validate_requirements.py \
  --prd build/requirements/prd.json \
  --srs build/requirements/srs.json \
  --rtm build/requirements/rtm.json \
  --strict
```

The validator checks supported requirements relationships, identifier consistency, baseline references, and recorded coverage.

It does not independently determine whether a stakeholder requirement is correct or whether an approval record is authentic.

### Automated Tests

```bash
python -m unittest discover -s tests -v
```

Unit tests cover framework validation, requirements validation, Markdown extraction, and the included acceptance fixtures.

### Continuous Integration

GitHub Actions runs automated checks for the framework and requirements pipeline on configured repository events.

- Workflow configuration: [`.github/workflows/framework-validation.yml`](.github/workflows/framework-validation.yml)
- [View CI results](https://github.com/Hasanah977/prezekc-ai-framework/actions)

CI checks are evidence of the behavior they execute. They do not replace engineering review or release authorization.

## Getting Started

### Prerequisites

- Git.
- Python 3.12 or later.
- A compatible development environment.
- An AI assistant or engineering operator capable of following repository instructions.

Project-specific SDKs, frameworks, databases, and deployment tools are required only when the target project uses them.

### 1. Clone the Repository

```bash
git clone https://github.com/Hasanah977/prezekc-ai-framework.git
cd prezekc-ai-framework
```

### 2. Read the Operating Specifications

Start with:

1. [Agent Operating Contract](AGENTS.md)
2. [Framework Specification](FRAMEWORK.md)
3. [Governance Protocol](core/governance.md)
4. [Workflow Protocol](core/workflow.md)
5. [Verification Protocol](core/verification.md)

### 3. Validate the Framework

```bash
python tools/validate_framework.py --strict
python -m unittest discover -s tests -v
```

Both commands must complete successfully before relying on the repository as a verified framework baseline.

### 4. Select the Engineering Activity

Choose the applicable skill or workflow based on the task.

For example, an initial system investigation uses `skills/system-analysis/SKILL.md`.

Requirements decomposition uses `skills/prd-to-srs/SKILL.md`.

Implementation uses the relevant web or mobile development skill after the required baselines have been established.

### 5. Establish Project Context

Before execution, identify the project objective, existing artifacts, applicable requirements, current repository state, available tools, and approval authority.

Do not assume that a project has an approved PRD, SRS, or design merely because a corresponding template exists.

## Repository Structure

```text
prezekc-ai-framework/
├── .github/
│   └── workflows/
│       └── framework-validation.yml
├── agents/
│   ├── research-analyst.md
│   ├── system-analyst.md
│   ├── requirements-engineer.md
│   ├── system-architect.md
│   ├── development-engineer.md
│   └── verification-engineer.md
├── core/
│   ├── governance.md
│   ├── workflow.md
│   └── verification.md
├── docs/
│   └── architecture.md
├── examples/
│   ├── acceptance/
│   └── markdown/
├── rules/
│   ├── global-rules.md
│   └── documentation-rules.md
├── skills/
│   ├── system-analysis/
│   ├── comparative-study/
│   ├── requirement-analysis/
│   ├── prd-generation/
│   ├── prd-to-srs/
│   ├── system-design/
│   ├── web-development/
│   ├── mobile-development/
│   ├── testing/
│   └── deployment/
├── templates/
│   ├── system-analysis.md
│   ├── comparative-study.md
│   ├── requirement-analysis.md
│   ├── prd.md
│   ├── srs.md
│   ├── requirement-traceability-matrix.md
│   └── system-design.md
├── tests/
├── tools/
│   ├── validate_framework.py
│   ├── extract_requirements.py
│   └── validate_requirements.py
├── workflows/
│   ├── full-lifecycle.md
│   ├── web-application.md
│   └── mobile-application.md
├── AGENTS.md
├── FRAMEWORK.md
├── README.md
└── CHANGELOG.md
```

The tree describes the v0.1.0 release candidate. Release documentation and acceptance fixtures must be committed before publication.

Generated output under `build/` is not part of the framework source baseline.

## Verification and Release Status

### Local Verification

The following results were reported during the v0.1.0 release assessment:

| Check | Result |
|---|---|
| Framework structural validation | 0 errors, 0 warnings |
| Requirements manifest validation | 0 errors, 0 warnings |
| Automated unit tests | 31 passed |
| Markdown-to-JSON integration | Passed |
| Acceptance fixture traceability | Passed |
| Git whitespace validation | Passed |

The acceptance scenario uses simulated evidence and approval records. It validates structural relationships and supported requirements mappings, not the substantive correctness of an independently developed software system.

### Release State

| | |
|---|---|
| **Version** | `0.1.0` |
| **State** | Release Candidate |
| **Published release** | Pending |

The final release requires successful CI on the release commit, documentation review, and recorded authorization before publication of the `v0.1.0` tag.

## Limitations

PREZEKC AI v0.1.0 has the following boundaries:

- It does not include an autonomous multi-agent execution runtime.
- Skills and workflows are specifications executed by compatible assistants or engineering operators.
- PRD-to-SRS decomposition is defined procedurally; the Python pipeline extracts and validates supported structures rather than autonomously generating complete SRS content.
- Markdown parsing requires the supported document conventions.
- Structural validation does not guarantee semantic correctness.
- Approval metadata is checked for consistency but is not independently authenticated.
- System design quality requires engineering review.
- Web, Android, and iOS implementation depends on the project toolchain.
- Platform compatibility, application security, and production deployment require project-specific verification.
- The included acceptance test is a simulation, not evidence of a deployed application.

These limitations define the current release boundary.

## Development Roadmap

| Milestone | Status |
|---|---|
| Engineering governance and agent contracts | ✅ Implemented |
| System analysis and research skills | ✅ Implemented |
| Requirements engineering skills and templates | ✅ Implemented |
| PRD-to-SRS procedure and RTM | ✅ Implemented |
| System design skill and template | ✅ Implemented |
| Web and mobile delivery workflows | ✅ Implemented |
| Testing and deployment procedures | ✅ Implemented |
| Framework structure validator | ✅ Implemented |
| Requirements traceability validator | ✅ Implemented |
| Markdown-to-JSON extraction | ✅ Implemented |
| Automated CI checks | ✅ Implemented |
| Simulated acceptance test | 🟢 Locally verified |
| v0.1.0 release documentation and authorization | 🟡 Pending |
| Autonomous agent orchestration | ⚪ Future development |
| Broader semantic requirements validation | ⚪ Future development |
| Multi-project evaluation | ⚪ Future development |

"Implemented" refers to the corresponding repository artifact or utility. It does not imply that every engineering workflow has been executed against a production project.

## Documentation

| Reference | Description |
|---|---|
| [AGENTS.md](AGENTS.md) | Agent operating contract |
| [FRAMEWORK.md](FRAMEWORK.md) | Framework engineering specification |
| [Architecture](docs/architecture.md) | Internal component architecture |
| [Governance](core/governance.md) | Approval and authority rules |
| [Workflow Protocol](core/workflow.md) | Lifecycle transitions |
| [Verification Protocol](core/verification.md) | Verification rules |
| [Global Rules](rules/global-rules.md) | Shared operational constraints |
| [Documentation Standards](rules/documentation-rules.md) | Engineering document conventions |
| [Full Lifecycle](workflows/full-lifecycle.md) | End-to-end delivery sequence |

## License

No license has been selected for this repository.

Until a license is published, public access to the source code does not by itself grant permission to use, modify, or redistribute it.

---

<div align="center">

**PREZEKC AI Framework** · v0.1.0 Release Candidate

</div>