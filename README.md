<p align="center">
  <img src="assets/logo-pcs-3d.png" alt="PREZEKC AI Framework" width="150">
</p>

<h1 align="center">PREZEKC AI Framework</h1>

<p align="center">
  <strong>Engineering discipline for AI-assisted software development.</strong><br>
  <sub>Plan with requirements. Build with structure. Verify with evidence.<br>
  Keep consequential decisions in human hands.</sub>
</p>

<p align="center">
  <a href="https://github.com/Hasanah977/prezekc-ai-framework"><img alt="PREZEKC v0.3.0" src="https://img.shields.io/badge/VERSION-v0.3.0-2563eb?style=for-the-badge"></a>
  <a href="#engineering-skills"><img alt="15 engineering skills" src="https://img.shields.io/badge/SKILLS-15-0891b2?style=for-the-badge"></a>
  <a href="#the-engineering-lifecycle"><img alt="9 engineering phases" src="https://img.shields.io/badge/PHASES-9-4f46e5?style=for-the-badge"></a>
  <a href="#engineering-roles"><img alt="6 engineering roles" src="https://img.shields.io/badge/ROLES-6-7c3aed?style=for-the-badge"></a>
</p>

<p align="center">
  <a href="docs/import-mode.md"><img alt="PRD and SRS Import Mode" src="https://img.shields.io/badge/REQUIREMENTS-IMPORT%20FIRST-0f766e?style=for-the-badge"></a>
  <a href="docs/engineering-quality.md"><img alt="Engineering quality" src="https://img.shields.io/badge/QUALITY-CLEAN%20CODE-0369a1?style=for-the-badge"></a>
  <a href="skills/security-review/SKILL.md"><img alt="Security review" src="https://img.shields.io/badge/SECURITY-REVIEW-475569?style=for-the-badge"></a>
  <a href="https://github.com/Hasanah977/prezekc-ai-framework/actions"><img alt="GitHub Actions" src="https://img.shields.io/badge/CI-GITHUB%20ACTIONS-1f2937?style=for-the-badge&logo=githubactions&logoColor=white"></a>
</p>

<p align="center">
  <a href="#quick-start">Quick Start</a> ·
  <a href="#how-prezekc-works">How It Works</a> ·
  <a href="#requirements-import-mode">Import Mode</a> ·
  <a href="#engineering-skills">Skills</a> ·
  <a href="#verification">Verification</a> ·
  <a href="#documentation">Documentation</a>
</p>

---

## What is PREZEKC?

**PREZEKC AI Framework** is a **requirements-driven, skill-based software engineering framework** for developers who use AI coding assistants. It guides the assistant through understanding a project, working from approved requirements and designs, making controlled changes, and verifying the result before moving on.

PREZEKC is **not a new AI model, an autonomous multi-agent runtime, or a one-click app generator**. It is a reusable set of engineering contracts, workflows, templates, skills, and Python validation utilities. Your AI assistant or development team carries out the work; PREZEKC provides the operating discipline.

> **In one sentence:** PREZEKC helps you use AI to build software deliberately—not just generate code quickly.

### The problem it addresses

AI-assisted coding can accelerate delivery, but speed alone cannot tell you whether the resulting application meets the right requirements, follows its design, preserves existing behavior, or has actually passed testing. Common failure modes include:

- Starting implementation before the problem and scope are understood.
- Generating features that were never requested or approved.
- Creating inconsistent interfaces and hard-to-maintain code.
- Losing the connection between requirements, design, implementation, and tests.
- Declaring work complete without running the necessary checks.
- Leaving a beginner unsure about what to do next.

PREZEKC addresses these risks through **traceability, explicit human approvals, task-specific skills, and evidence-based handoffs**. It guides engineering practice; it does not guarantee defect-free or secure software.

## What you get

| Capability | What it means in practice |
|:--|:--|
| **Requirements-first workflow** | Work from PRD, SRS, and a requirement traceability matrix (RTM), with recorded approval states. |
| **Import-first documents** | Prepare PRD/SRS in another editor or AI, then bring supported Markdown into PREZEKC for structural and traceability checks. |
| **System design** | Describe architecture, database, APIs, component boundaries, and backend structure before implementation. |
| **UI/UX flow and UI design** | Define journeys, screens, interaction states, visual consistency, and accessibility checks. |
| **Task breakdown** | Split approved designs into small, reviewable tasks with dependencies and acceptance criteria. |
| **Clean Architecture & Clean Code** | Apply maintainable module boundaries, modern coding practices, and safe refactoring without forcing unnecessary complexity. |
| **Security review** | Guide defensive checks for access control, input handling, secrets, dependencies, and sensitive data. |
| **Verification with evidence** | Distinguish checks that passed, failed, were blocked, or were not run. |
| **Human-guided next actions** | Explain completed work, recommend a sensible next step, and ask before consequential transitions. |

## How PREZEKC works

```text
Your idea or existing project
            │
            ▼
    Understand the context
            │
            ▼
      PRD  →  SRS
  (import or author; review and approve)
            │
            ▼
     SDD / System Design
          + UI/UX Flow
            │
            ▼
        Task Breakdown
            │
            ▼
   Implement the approved task
            │
            ▼
 Code quality • UI • Security • Tests
            │
            ▼
 Evidence report + human decision
            │
            ▼
  Recommended next action / release
```

PREZEKC does **not** require every task to restart the complete lifecycle. For existing applications, the assistant should inspect the current code and available project records, identify the relevant task and baseline, and load only the necessary skills.

### Five key engineering artifacts

| Artifact | Answers | Covers |
|:--|:--|:--|
| **PRD — Product Requirements Document** | **What and why?** | Product goals, users, features, scope, and high-level flows. |
| **SRS — Software Requirements Specification** | **What must the system do?** | Observable behavior, validation, business rules, permissions, and constraints. |
| **SDD — Software Design Document** | **How will it be built?** | Architecture, database, APIs, interfaces, and backend structure. |
| **UI/UX Flow** | **How will people use it?** | Screen journeys, navigation, form states, errors, loading, and accessibility considerations. |
| **Task Breakdown** | **What do we build first?** | Tasks, dependencies, priorities, acceptance criteria, and verification plans. |

PRD/SRS may be produced outside PREZEKC. Importing them **never substitutes for human review or approval**.

## The engineering lifecycle

The framework defines nine engineering phases (P01–P09):

| Phase | Focus | Typical output |
|:--:|:--|:--|
| **P01** | System Analysis | Existing-system analysis |
| **P02** | Comparative Study | Comparative findings |
| **P03** | Requirement Analysis | Stakeholder needs and constraints |
| **P04** | Product Requirements | PRD and approval record |
| **P05** | Software Requirements | SRS and RTM |
| **P06** | System Design | SDD and relevant UI/UX flow |
| **P07** | Implementation | Code and task records |
| **P08** | Verification | Test evidence and review findings |
| **P09** | Deployment & Maintenance | Release and maintenance records |

Task Breakdown connects approved design to implementation. A project's size, risks, and existing artifacts determine how much documentation and review are appropriate; phase requirements and approval boundaries remain governed by [`AGENTS.md`](AGENTS.md) and [`core/workflow.md`](core/workflow.md).

## Engineering skills

PREZEKC v0.3.0 contains **15 task-oriented skill definitions**. An assistant should select the skill relevant to the current work instead of loading everything into context.

| Area | Skills |
|:--|:--|
| **Discovery & requirements** | [`system-analysis`](skills/system-analysis/SKILL.md), [`comparative-study`](skills/comparative-study/SKILL.md), [`requirement-analysis`](skills/requirement-analysis/SKILL.md), [`prd-generation`](skills/prd-generation/SKILL.md), [`prd-to-srs`](skills/prd-to-srs/SKILL.md) |
| **Design & planning** | [`system-design`](skills/system-design/SKILL.md), [`ui-ux-flow`](skills/ui-ux-flow/SKILL.md), [`ui-design`](skills/ui-design/SKILL.md), [`task-breakdown`](skills/task-breakdown/SKILL.md) |
| **Development & quality** | [`web-development`](skills/web-development/SKILL.md), [`mobile-development`](skills/mobile-development/SKILL.md), [`code-quality`](skills/code-quality/SKILL.md), [`security-review`](skills/security-review/SKILL.md), [`testing`](skills/testing/SKILL.md) |
| **Delivery** | [`deployment`](skills/deployment/SKILL.md) |

### Engineering roles

The repository also defines **six logical engineering roles**: Research Analyst, System Analyst, Requirements Engineer, System Architect, Development Engineer, and Verification Engineer.

These roles describe **responsibilities**, not six independently running AI workers. One compatible AI assistant may handle several roles sequentially.

## Quick start

### Prerequisites

- Git and Python (for local validation and the included CLI).
- A terminal and an AI coding assistant with access to the relevant project files, or an engineer following the procedures manually.
- The development tools required by your target application (for example, Flutter, PHP, Go, or Node.js).

PREZEKC itself is **repository-distributed**. There is no required npm or PyPI package and no need to install a dedicated AI model.

### 1. Get the framework

```powershell
git clone https://github.com/Hasanah977/prezekc-ai-framework.git
cd prezekc-ai-framework
```

### 2. Verify the framework

```powershell
python tools/validate_framework.py --strict
python -m unittest discover -s tests -v
```

Do not infer a passing result from this README. Use the **actual terminal output** from your environment.

### 3. Initialize a single project

From the PREZEKC repository, run the project initializer with the path to **your application**, for example:

```powershell
python tools/prezekc.py init --project "D:\Projects\my-application"
```

The initializer is intended to make PREZEKC's project instructions available within the application folder. Inspect its output and any existing project instructions; do not overwrite previous configuration or user files without approval. See [installation details](docs/installation.md).

**Use one project workspace:** open your application folder in VS Code or another coding environment. You do not need to combine the framework and application into a multi-root workspace.

### 4. Give your AI assistant its first instruction

```text
Use PREZEKC AI Framework for this project.

1. Locate and read the installed PREZEKC AGENTS.md and FRAMEWORK.md.
2. Follow the relevant governance and workflow rules.
3. Inspect the existing project without modifying any files yet.
4. Load only the engineering skill relevant to our current task.
5. Report the current state, important gaps, and one recommended next step.
6. Explain findings in clear, concise Indonesian.
7. Ask for my decision before major changes or phase transitions.

Do not invent missing files, approvals, tests, or requirements.
```

**Using Gemini on the web?** A GitHub attachment may help Gemini analyze framework documentation, but it does not by itself grant access to files on your Windows computer or execute commands inside your project. For direct code changes, use an AI coding environment with workspace access.

## Requirements Import Mode

PRD and SRS **remain core engineering artifacts**. You may write them in Google Docs, another AI tool, or an editor, then import the supported Markdown documents instead of asking your coding assistant to regenerate them.

**Recommended sequence:** external PRD draft → import and inspect → **PRD approval** → SRS draft based on approved PRD → SRS/RTM import and validation → **SRS approval** → design and implementation.

Use the supplied templates as a formatting guide. The existing Python utilities operate on **supported Markdown structure**, not arbitrary Word/PDF files.

### Validate a sample requirements package

The repository includes sample documents to practice the workflow:

```powershell
python tools/extract_requirements.py `
  --prd examples/markdown/prd.md `
  --srs examples/markdown/srs.md `
  --rtm examples/markdown/rtm.md `
  --output build/requirements
```

Then validate the extracted manifests:

```powershell
python tools/validate_requirements.py `
  --prd build/requirements/prd.json `
  --srs build/requirements/srs.json `
  --rtm build/requirements/rtm.json `
  --strict
```

Choose a **new output directory** when rerunning extraction because the extractor does not overwrite existing output files. The validators can check supported IDs, baseline relationships, coverage, and traceability; **they cannot independently establish that stakeholder requirements are semantically correct**.

Read the [Import Mode guide](docs/import-mode.md) before using project-owned documents.

## Clean Architecture, code quality & security

PREZEKC v0.3.0 extends the engineering process with targeted quality procedures:

- **Clean Architecture:** use appropriate boundaries and dependency direction for the scale of the project. Avoid unnecessary layers and speculative abstractions.
- **Modern Code:** choose supported APIs and conventions for the actual language, framework, and versions in use.
- **Clean Code:** make code readable and maintainable, remove harmful duplication, and prefer small, justified changes.
- **UI quality:** preserve approved design decisions while checking responsive layouts, accessibility, and real interaction states.
- **Security review:** investigate applicable risks defensively and document evidence, impact, and unresolved limitations.
- **Testing and refactoring:** use relevant automated checks and regression coverage; do not report an unrun check as a pass.

These are engineering **review and execution procedures**, not proof that an application automatically satisfies every quality or security standard.

See [Engineering Quality](docs/engineering-quality.md), [Code Quality Skill](skills/code-quality/SKILL.md), and [Security Review Skill](skills/security-review/SKILL.md).

## Verification

The framework provides deterministic utilities for supported repository and requirements checks:

| Tool | Role |
|:--|:--|
| `tools/validate_framework.py` | Checks framework structure, skill metadata, and local links. |
| `tools/extract_requirements.py` | Extracts supported PRD/SRS/RTM Markdown into JSON. |
| `tools/validate_requirements.py` | Checks supported requirement IDs, baselines, and traceability. |
| `tools/quality_gate.py` | Checks the structure and evidence rules of supported quality reports. |

Use the included automated tests to detect regressions in these mechanisms. A passing framework test does **not** mean the software being built has passed its own unit, integration, security, UI, or device testing.

### Human-guided handoff

At a meaningful task boundary, the assistant should report:

```text
Completed  : What changed and why
Evidence   : Checks that actually ran and their results
Limitations: What remains uncertain, blocked, or untested
Recommended next step: One practical action with a short reason
Decision   : Continue, revise, or choose another direction?
```

If the user is unsure, the assistant should **recommend** a next action and explain why, rather than forcing the user to know the entire development process in advance.

## Scope and limitations

PREZEKC is a **framework for guiding AI-assisted engineering**, not a runtime with guaranteed autonomous agents, universal tool access, or automatic production deployment. Its skills take effect only when the AI assistant or engineer actually reads and follows them.

The framework does not independently verify human identity or approvals, prove semantic correctness of arbitrary requirements, guarantee secure code, or promise token savings without measurement. Build, platform, and production-readiness claims require **project-specific evidence**.

## Documentation

| Start here | Purpose |
|:--|:--|
| [`AGENTS.md`](AGENTS.md) | Authority, agent conduct, and handoff rules |
| [`FRAMEWORK.md`](FRAMEWORK.md) | Framework concepts and operating model |
| [`docs/installation.md`](docs/installation.md) | Installation and single-project setup |
| [`docs/import-mode.md`](docs/import-mode.md) | PRD/SRS import-first workflow |
| [`docs/engineering-quality.md`](docs/engineering-quality.md) | Clean code, UI quality, and security reviews |
| [`core/next-action.md`](core/next-action.md) | Recommendations and human decisions |
| [`core/task-execution.md`](core/task-execution.md) | Planning, execution, and evidence-based reporting |
| [`docs/releases/v0.3.0-release-notes.md`](docs/releases/v0.3.0-release-notes.md) | v0.3.0 changes |
| [`CHANGELOG.md`](CHANGELOG.md) | Version history |

## Contributing and feedback

Issue reports, corrections, and engineering feedback are welcome via [GitHub Issues](https://github.com/Hasanah977/prezekc-ai-framework/issues). Proposed changes should preserve existing approval boundaries, avoid unsupported claims, and pass the applicable validation checks.

## License and usage rights

**No open-source license is currently included in this repository.** All rights remain reserved by the applicable copyright holders unless and until an explicit license is published. Public repository visibility alone does not grant permission to redistribute or modify its contents beyond applicable legal rights.

---

<p align="center">
  <strong>PREZEKC AI Framework</strong><br>
  <sub>Requirements-driven · Skill-based · Human-guided · Evidence-verified</sub>
</p>
