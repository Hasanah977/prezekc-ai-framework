<div align="center">

# PREZEKC AI Framework

[![Framework Validation](https://github.com/Hasanah977/prezekc-ai-framework/actions/workflows/framework-validation.yml/badge.svg)](https://github.com/Hasanah977/prezekc-ai-framework/actions/workflows/framework-validation.yml)
[![Release](https://img.shields.io/badge/release-v0.1.0_RC-orange.svg)](CHANGELOG.md)
[![Python](https://img.shields.io/badge/python-3.12%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
![Platforms](https://img.shields.io/badge/platform-web%20%7C%20android%20%7C%20ios-3DDC84)
![Stars](https://img.shields.io/github/stars/Hasanah977/prezekc-ai-framework?logo=github)
![Last Commit](https://img.shields.io/github/last-commit/Hasanah977/prezekc-ai-framework)

A structured engineering framework for building software with AI assistance, from system analysis and requirements definition to architecture, implementation, verification, and delivery.

**Requirements-driven engineering. Controlled execution. Verifiable outcomes.**

[📖 **Read the documentation →**](#documentation)

[Getting Started](#installation) · [How It Works](#how-it-works) · [Usage](#usage) · [Report an Issue](https://github.com/Hasanah977/prezekc-ai-framework/issues)

</div>

---

## Contents

- [Why PREZEKC?](#why-prezekc)
- [Features](#features)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [Verification](#verification)
- [Design Boundaries](#design-boundaries)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

---

## Why PREZEKC?

AI coding assistants can generate software quickly, but code generation alone does not establish that a system satisfies its requirements.

Product scope may be unclear, requirements may change without authorization, implementation decisions may diverge from specifications, and successful code generation may be mistaken for verified delivery.

**PREZEKC AI addresses these problems by introducing a controlled engineering process around AI-assisted development.**

The framework establishes:

- **Analysis before implementation.** Understand the existing process, stakeholders, and underlying problems before defining features.
- **Requirements as the source of truth.** Derive system behavior from documented product requirements rather than unsupported assumptions.
- **Traceability across artifacts.** Maintain explicit relationships between PRD, SRS, system design, implementation, and verification.
- **Human-controlled decisions.** Keep approval of scope, requirements, architecture, and production releases with authorized project owners.
- **Evidence-based verification.** Support completion claims with recorded checks, test results, and identifiable evidence.
- **Technology-independent workflows.** Apply consistent engineering procedures across web, backend, Android, iOS, and cross-platform projects.

PREZEKC is designed for software engineers, system analysts, researchers, students, and development teams using AI assistants as part of their engineering workflow.

## Features

### Engineering Lifecycle

PREZEKC defines nine connected engineering phases:

| Phase | Activity | Deliverable |
|---|---|---|
| P01 | System Analysis | Existing System Analysis Report |
| P02 | Comparative Study | Comparative Study Report |
| P03 | Requirement Analysis | Requirement Analysis Document |
| P04 | Product Requirements | Product Requirements Document |
| P05 | Software Requirements | Software Requirements Specification and RTM |
| P06 | System Design | Architecture and System Design Specification |
| P07 | Implementation | Application source and implementation records |
| P08 | Verification | Test evidence and verification report |
| P09 | Deployment & Maintenance | Release and operational records |

Each phase defines its inputs, responsibilities, execution procedure, and completion conditions.

### Engineering Agents

Six engineering roles coordinate the framework's responsibilities.

| Role | Responsibility |
|---|---|
| Research Analyst | Research and comparative evaluation |
| System Analyst | Existing-system investigation and problem analysis |
| Requirements Engineer | Requirements analysis, PRD, SRS, and traceability |
| System Architect | Architecture, components, data models, and interfaces |
| Development Engineer | Software implementation and developer-level verification |
| Verification Engineer | Independent verification and evidence assessment |

These are logical engineering roles. They do not imply six autonomous AI processes running independently.

### Reusable Engineering Skills

PREZEKC includes ten task-specific procedures:

- System Analysis
- Comparative Study
- Requirement Analysis
- PRD Generation
- PRD-to-SRS Engineering
- System Design
- Web Development
- Mobile Development
- Software Testing
- Deployment

Each skill defines prerequisites, execution steps, deliverables, verification conditions, and failure handling.

### Document Engineering

The framework provides controlled templates for:

- Existing System Analysis
- Comparative Study
- Requirement Analysis
- Product Requirements Document (PRD)
- Software Requirements Specification (SRS)
- Requirement Traceability Matrix (RTM)
- System Design Specification

The documentation process preserves requirement identifiers and supports review of changes across related artifacts.

### Automated Validation

Three Python utilities implement the executable validation layer.

| Tool | Purpose |
|---|---|
| `validate_framework.py` | Verify repository structure, skill metadata, and local documentation references |
| `extract_requirements.py` | Extract supported PRD, SRS, and RTM Markdown into structured JSON |
| `validate_requirements.py` | Check requirement identifiers, baseline references, coverage, and traceability mappings |

The validation tools use the Python Standard Library. No additional Python packages are required for the documented checks.

## How It Works

PREZEKC combines engineering instructions with deterministic validation tools.

The operating model follows this sequence:

```text
Project Context
      |
      v
System & Requirement Analysis
      |
      v
Product Requirements (PRD)
      |
      | Human Approval
      v
Software Requirements (SRS)
      |
      | Human Approval
      v
System Design
      |
      | Design Review
      v
Implementation
      |
      v
Verification
      |
      | Release Authorization
      v
Deployment & Maintenance
```

The AI assistant follows the applicable role and skill instructions. The project owner remains responsible for consequential approval decisions.

For requirements engineering, PREZEKC maintains a traceable relationship between product intent and system behavior.

**Example:** a product requirement establishes that authorized reporting personnel must be able to access consolidated records for a selected period.

```text
PRD-FR-001  Consolidated record access
    |
    +-- SRS-FR-001.1  Reporting-period selection
    |
    +-- SRS-FR-001.2  Record retrieval
    |
    +-- SRS-FR-001.3  Access authorization
```

The Requirement Traceability Matrix records these relationships and connects them to subsequent design and verification artifacts.

The Python validators examine the supported requirement mappings. They do not independently determine whether the underlying business requirement is correct.

## Installation

PREZEKC is distributed as a Git repository, not as a PyPI package.

Installation consists of obtaining the framework, validating its contents, and making its instructions available to the AI assistant or engineering team.

### Requirements

- Git
- Python 3.12 or later
- A terminal or development environment
- An AI assistant or engineering operator capable of reading repository instructions

Additional tools such as Node.js, PHP, Go, Android SDK, or Xcode are only required when the target software project uses them.

### 1. Clone PREZEKC

```bash
git clone https://github.com/Hasanah977/prezekc-ai-framework.git
cd prezekc-ai-framework
```

For a specific published release, check out its Git tag once that release is available:

```bash
git fetch --tags
git checkout v0.1.0
```

Until the tag is published, use the `main` branch for the release candidate.

### 2. Verify the Installation

Run the framework validator:

```bash
python tools/validate_framework.py --strict
```

Run the automated tests:

```bash
python -m unittest discover -s tests -v
```

The checks should complete successfully before the framework is used as a validated local baseline.

### 3. Connect PREZEKC to Your Project

PREZEKC does not require a global installer or changes to your application dependencies.

For a new or existing software project, keep the framework repository available alongside the target project.

Example:

```text
workspace/
    prezekc-ai-framework/
    my-application/
```

Open the project in your development environment and provide the AI assistant with access to the framework instructions.

The recommended reading order is:

1. `AGENTS.md`: agent operating contract.
2. `core/governance.md`: authority and change control.
3. `core/workflow.md`: lifecycle requirements.
4. The relevant file in `agents/`.
5. The required `skills/<skill-name>/SKILL.md`.

The framework can also be copied into a project as a self-contained reference directory. Preserve relative file paths so links between its specifications remain valid.

> **Note:** PREZEKC does not automatically register its skills in every AI assistant. How instructions are attached or loaded depends on the assistant or development environment being used.

## Usage

### Starting a New Project

Start by providing the project objective and identifying the intended software platform.

An example instruction to an AI assistant:

```text
Use PREZEKC AI Framework as the engineering procedure
for this project.

Read the framework's AGENTS.md and core protocols.

Begin with System Analysis. Identify the current process,
stakeholders, known problems, evidence, and information gaps.

Do not introduce unapproved product requirements or
proceed to implementation before the applicable
requirements and design baselines are established.
```

The assistant should apply the relevant analysis skill, produce the required artifact, and report unresolved findings.

Continue to the next phase when its prerequisites are satisfied.

### Working with an Existing Project

PREZEKC can be applied without rebuilding the project from the beginning.

The operating procedure is:

1. Inspect the current repository and project documentation.
2. Identify existing approved requirements and design baselines.
3. Determine the requested change and affected components.
4. Apply the relevant engineering skill.
5. Evaluate downstream impact.
6. Verify the completed change.

Existing code, design conventions, and user changes must be preserved unless modification is authorized.

### Extracting PRD, SRS, and RTM

The document extraction tool converts supported Markdown artifacts into JSON manifests for deterministic validation.

Example using the included fixtures:

```bash
python tools/extract_requirements.py \
  --prd examples/markdown/prd.md \
  --srs examples/markdown/srs.md \
  --rtm examples/markdown/rtm.md \
  --output build/requirements
```

The output contains:

```text
build/requirements/prd.json
build/requirements/srs.json
build/requirements/rtm.json
```

The extractor does not overwrite existing manifests. Choose a new output directory for subsequent runs.

Validate the generated manifests:

```bash
python tools/validate_requirements.py \
  --prd build/requirements/prd.json \
  --srs build/requirements/srs.json \
  --rtm build/requirements/rtm.json \
  --strict
```

A successful check reports:

```text
Requirements validation: 0 error(s), 0 warning(s)
```

### Running the Acceptance Example

The repository includes a simulated engineering example covering system analysis, requirements, and design traceability.

Run the automated tests:

```bash
python -m unittest discover -s tests -v
```

Extract the acceptance requirements:

```bash
python tools/extract_requirements.py \
  --prd examples/acceptance/prd.md \
  --srs examples/acceptance/srs.md \
  --rtm examples/acceptance/rtm.md \
  --output build/acceptance
```

Validate the extracted requirements and design references:

```bash
python tools/validate_requirements.py \
  --prd build/acceptance/prd.json \
  --srs build/acceptance/srs.json \
  --rtm build/acceptance/rtm.json \
  --design examples/acceptance/design.json \
  --strict
```

The acceptance scenario uses simulated engineering documents and approval records. It validates supported structural and traceability conditions, not the correctness of a production application.

## Verification

PREZEKC uses automated tests and GitHub Actions to verify supported framework behavior.

The v0.1.0 release candidate was assessed locally with the following reported results:

| Check | Result |
|---|---|
| Framework structural validation | 0 errors, 0 warnings |
| Requirements and traceability validation | 0 errors, 0 warnings |
| Automated unit tests | 31 passed |
| Markdown-to-JSON extraction | Passed |
| Acceptance example validation | Passed |
| Git whitespace verification | Passed |

GitHub Actions executes the configured validation workflow on repository changes.

[View Framework Validation →](https://github.com/Hasanah977/prezekc-ai-framework/actions/workflows/framework-validation.yml)

Verification results apply to the tested artifacts and environments. They do not establish universal correctness, production readiness, or approval of unreviewed requirements.

## Design Boundaries

PREZEKC v0.1.0 provides engineering procedures and executable validation utilities.

It does not provide:

- An autonomous multi-agent execution runtime.
- Automatic generation of complete software projects without external AI assistance.
- Independent authentication of stakeholder approval records.
- General-purpose semantic validation of arbitrary requirements documents.
- Guaranteed Android, iOS, or production deployment compatibility.

The available Python tools focus on deterministic validation of supported document structures and requirements mappings.

Project-specific implementation, security assessment, platform testing, and release authorization remain separate engineering responsibilities.

## Documentation

| Document | Description |
|---|---|
| [Agent Operating Contract](AGENTS.md) | Agent authority, behavior, and handoff requirements |
| [Framework Specification](FRAMEWORK.md) | Core framework definition |
| [Framework Architecture](docs/architecture.md) | Internal architecture and component integration |
| [Governance](core/governance.md) | Approval authority and change control |
| [Engineering Workflow](core/workflow.md) | Lifecycle requirements |
| [Verification Protocol](core/verification.md) | Verification policies and evidence requirements |
| [Full Lifecycle](workflows/full-lifecycle.md) | End-to-end engineering procedure |
| [Web Application Workflow](workflows/web-application.md) | Web delivery process |
| [Mobile Application Workflow](workflows/mobile-application.md) | Android and iOS delivery process |
| [Changelog](CHANGELOG.md) | Version history and release notes |

## Contributing

Bug reports, documentation corrections, validation improvements, and engineering feedback may be submitted through [GitHub Issues](https://github.com/Hasanah977/prezekc-ai-framework/issues).

Contributions should preserve existing engineering contracts, maintain requirement traceability where applicable, and pass the available validation checks.

Changes that alter governance, approval authority, or controlled engineering behavior require explicit review.

## License

Copyright (c) 2026 PREZEKC AI Framework contributors.

This project is currently distributed without an open-source license.

All rights are reserved by the respective copyright holders. Licensing terms will be established following the completion of the project's release and intellectual property review.

---

<div align="center">

**PREZEKC AI Framework** · v0.1.0 Release Candidate

</div>