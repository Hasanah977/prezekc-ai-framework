<p align="center">
  <img src="assets/logo-pcs-3d.png" alt="PREZEKC AI Framework logo" width="220">
</p>

<h1 align="center">PREZEKC AI</h1>

<p align="center">
  <b>Engineering discipline for AI-assisted software development</b><br>
  <sub>A requirements-driven, skill-based framework that guides your AI coding assistant<br>
  through approved requirements, structured design, controlled changes, and evidence-based verification,<br>
  with consequential decisions kept in human hands.</sub>
</p>

<p align="center">
  <a href="https://github.com/Hasanah977/prezekc-ai-framework/stargazers"><img src="https://img.shields.io/github/stars/Hasanah977/prezekc-ai-framework?style=for-the-badge&logo=github&logoColor=white&label=Stars&color=ffd33d" alt="GitHub stars"></a>
  <a href="https://github.com/Hasanah977/prezekc-ai-framework/forks"><img src="https://img.shields.io/github/forks/Hasanah977/prezekc-ai-framework?style=for-the-badge&logo=github&logoColor=white&label=Forks&color=8250df" alt="GitHub forks"></a>
  <a href="https://github.com/Hasanah977/prezekc-ai-framework/issues"><img src="https://img.shields.io/github/issues/Hasanah977/prezekc-ai-framework?style=for-the-badge&logo=github&logoColor=white&label=Issues%20Open&color=e11d48" alt="Open issues"></a>
  <a href="https://github.com/Hasanah977/prezekc-ai-framework/commits/main"><img src="https://img.shields.io/github/last-commit/Hasanah977/prezekc-ai-framework?style=for-the-badge&logo=git&logoColor=white&label=Last%20Commit&color=0284c7" alt="Last commit"></a>
</p>

<p align="center">
  <a href="CHANGELOG.md"><img src="https://img.shields.io/badge/Release-v0.3.0-blue.svg?style=for-the-badge&logo=git&logoColor=white" alt="Release v0.3.0"></a>
  <a href="https://github.com/Hasanah977/prezekc-ai-framework/actions"><img src="https://img.shields.io/github/actions/workflow/status/Hasanah977/prezekc-ai-framework/framework-validation.yml?branch=main&label=framework%20validation&style=for-the-badge&logo=githubactions&logoColor=white" alt="Framework validation workflow status"></a>
  <a href="#9-quick-start"><img src="https://img.shields.io/badge/Python-3.12%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.12 or later"></a>
  <a href="#13-license"><img src="https://img.shields.io/badge/License-Not%20selected-lightgrey?style=for-the-badge" alt="License not selected"></a>
</p>

<p align="center">
  <a href="#5-engineering-skills"><img src="https://img.shields.io/badge/Skills-15-0891b2?style=for-the-badge&logo=bookstack&logoColor=white" alt="15 engineering skills"></a>
  <a href="#4-the-engineering-lifecycle"><img src="https://img.shields.io/badge/Phases-9-4f46e5?style=for-the-badge&logo=target&logoColor=white" alt="9 engineering phases"></a>
  <a href="#6-engineering-roles"><img src="https://img.shields.io/badge/Roles-6-7c3aed?style=for-the-badge&logo=teamspeak&logoColor=white" alt="6 engineering roles"></a>
  <a href="#7-requirements-import-mode"><img src="https://img.shields.io/badge/Requirements-Import%20First-0f766e?style=for-the-badge&logo=markdown&logoColor=white" alt="Import-first requirements"></a>
</p>

<p align="center">
  <a href="docs/engineering-quality.md"><img src="https://img.shields.io/badge/Quality-Clean%20Code-0369a1?style=for-the-badge&logo=codacy&logoColor=white" alt="Clean code and architecture"></a>
  <a href="skills/security-review/SKILL.md"><img src="https://img.shields.io/badge/Security-Review%20Skill-475569?style=for-the-badge&logo=hackthebox&logoColor=white" alt="Security review skill"></a>
  <a href="#2-the-problem-prezekc-solves"><img src="https://img.shields.io/badge/Human-Approval%20Gates-d97706?style=for-the-badge&logo=checkmarx&logoColor=white" alt="Human approval gates"></a>
  <a href="#11-scope-and-limitations"><img src="https://img.shields.io/badge/Platforms-Web%20%7C%20Android%20%7C%20iOS-3ddc84?style=for-the-badge&logo=android&logoColor=white" alt="Web, Android, and iOS projects"></a>
</p>

> **What PREZEKC is, and is not.** PREZEKC is a set of engineering contracts, workflows, templates, skills, and Python validation utilities. It is **not** an AI model, an autonomous multi-agent runtime, or a one-click app generator. Your AI assistant or development team carries out the work. PREZEKC supplies the operating discipline, and its skills take effect only when the assistant actually reads and follows them.

<p align="center">
  <b>Jump to:</b>
  <a href="#1-what-is-prezekc">What it is</a> ·
  <a href="#2-the-problem-prezekc-solves">Problem</a> ·
  <a href="#3-how-it-works">How it works</a> ·
  <a href="#4-the-engineering-lifecycle">Lifecycle</a> ·
  <a href="#5-engineering-skills">Skills</a> ·
  <a href="#7-requirements-import-mode">Import mode</a> ·
  <a href="#9-quick-start">Quick start</a> ·
  <a href="#12-documentation">Docs</a>
</p>

---

## 1. What is PREZEKC?

**PREZEKC AI Framework** helps you use an AI coding assistant to build software deliberately, not just quickly. It guides the assistant through five habits:

1. **Understand** the project and its problem before writing code.
2. **Work from approved requirements** (PRD, SRS) and an approved design.
3. **Make small, controlled changes** broken into reviewable tasks.
4. **Verify with evidence**, separating what passed, failed, was blocked, or was never run.
5. **Ask you** before any consequential decision or phase change.

It is built for developers, students, and teams who use AI assistants and want a repeatable process instead of ad-hoc prompting. You do not need to know the whole software process in advance: when you are unsure, the assistant recommends a next step and explains why.

> **In one sentence:** PREZEKC turns "ask the AI to build it" into "plan with requirements, build with structure, verify with evidence."

---

## 2. The problem PREZEKC solves

AI-assisted coding is fast, but speed alone does not tell you whether the result meets the right requirements, follows its design, preserves existing behavior, or has actually been tested.

| Without a framework | With PREZEKC |
|:---|:---|
| Implementation starts before the problem and scope are understood | Analysis comes first, with evidence and open questions recorded |
| The AI adds features nobody requested or approved | Every feature traces to an approved requirement |
| Requirements, design, code, and tests drift apart | A requirement traceability matrix (RTM) links them |
| Interfaces and structure become inconsistent | Design, UI/UX flow, and code-quality skills set shared rules |
| Work is declared done without running checks | Reports state which checks ran and which did not |
| A beginner is unsure what to do next | The assistant recommends one next step and asks for your decision |

PREZEKC guides engineering practice. It does **not** guarantee defect-free or secure software.

---

## 3. How it works

```text
Your idea or existing project
            |
            v
    Understand the context
            |
            v
      PRD  ->  SRS
  (import or author; review and approve)
            |
            v
     SDD / System Design
          + UI/UX Flow
            |
            v
        Task Breakdown
            |
            v
   Implement the approved task
            |
            v
 Code quality | UI | Security | Tests
            |
            v
 Evidence report + human decision
            |
            v
  Recommended next action / release
```

PREZEKC does **not** require every task to restart the full lifecycle. For an existing application, the assistant inspects the current code and project records, identifies the relevant task and baseline, and loads only the skills it needs.

### Five key engineering artifacts

| Artifact | Answers | Covers |
|:---|:---|:---|
| **PRD**, Product Requirements Document | What and why? | Product goals, users, features, scope, and high-level flows |
| **SRS**, Software Requirements Specification | What must the system do? | Observable behavior, validation, business rules, permissions, constraints |
| **SDD**, Software Design Document | How will it be built? | Architecture, database, APIs, interfaces, backend structure |
| **UI/UX Flow** | How will people use it? | Screen journeys, navigation, form states, errors, loading, accessibility |
| **Task Breakdown** | What do we build first? | Tasks, dependencies, priorities, acceptance criteria, verification plans |

PRD and SRS may be produced outside PREZEKC. Importing them **never substitutes for human review and approval**.

---

## 4. The engineering lifecycle

The framework defines nine phases, P01 to P09.

| Phase | Focus | Typical output |
|:---:|:---|:---|
| **P01** | System Analysis | Existing-system analysis |
| **P02** | Comparative Study | Comparative findings |
| **P03** | Requirement Analysis | Stakeholder needs and constraints |
| **P04** | Product Requirements | PRD and approval record |
| **P05** | Software Requirements | SRS and RTM |
| **P06** | System Design | SDD and relevant UI/UX flow |
| **P07** | Implementation | Code and task records |
| **P08** | Verification | Test evidence and review findings |
| **P09** | Deployment and Maintenance | Release and maintenance records |

Task Breakdown connects approved design to implementation. Project size, risk, and existing artifacts determine how much documentation and review is appropriate. Phase requirements and approval boundaries remain governed by [`AGENTS.md`](AGENTS.md) and [`core/workflow.md`](core/workflow.md).

---

## 5. Engineering skills

PREZEKC v0.3.0 contains **15 task-oriented skills**. The assistant selects the one relevant to the current work instead of loading everything into context.

| Area | Skills |
|:---|:---|
| **Discovery and requirements** | [`system-analysis`](skills/system-analysis/SKILL.md) · [`comparative-study`](skills/comparative-study/SKILL.md) · [`requirement-analysis`](skills/requirement-analysis/SKILL.md) · [`prd-generation`](skills/prd-generation/SKILL.md) · [`prd-to-srs`](skills/prd-to-srs/SKILL.md) |
| **Design and planning** | [`system-design`](skills/system-design/SKILL.md) · [`ui-ux-flow`](skills/ui-ux-flow/SKILL.md) · [`ui-design`](skills/ui-design/SKILL.md) · [`task-breakdown`](skills/task-breakdown/SKILL.md) |
| **Development and quality** | [`web-development`](skills/web-development/SKILL.md) · [`mobile-development`](skills/mobile-development/SKILL.md) · [`code-quality`](skills/code-quality/SKILL.md) · [`security-review`](skills/security-review/SKILL.md) · [`testing`](skills/testing/SKILL.md) |
| **Delivery** | [`deployment`](skills/deployment/SKILL.md) |

---

## 6. Engineering roles

Six logical roles describe **responsibilities**, not six independently running AI workers. One compatible assistant may perform several roles in sequence.

| Role | Responsibility |
|:---|:---|
| Research Analyst | Comparative research and evidence evaluation |
| System Analyst | Current-state processes, stakeholders, and problems |
| Requirements Engineer | Requirements analysis, PRD, SRS, and traceability |
| System Architect | Architecture, components, data, and interface design |
| Development Engineer | Implementation and developer-level verification |
| Verification Engineer | Independent verification, defect reporting, evidence assessment |

---

## 7. Requirements Import Mode

PRD and SRS remain core artifacts, but writing long requirement documents consumes many tokens. You may write them in Google Docs, another AI tool, or an editor, then import the supported Markdown instead of asking your coding assistant to regenerate them.

**Recommended sequence:**

```text
External PRD draft -> import and inspect -> PRD approval
   -> SRS draft from approved PRD -> SRS/RTM import and validation
   -> SRS approval -> design and implementation
```

Use the supplied templates as a formatting guide. The Python utilities read **supported Markdown structure**, not arbitrary Word or PDF files.

### Try it with the sample package

```powershell
python tools/extract_requirements.py `
  --prd examples/markdown/prd.md `
  --srs examples/markdown/srs.md `
  --rtm examples/markdown/rtm.md `
  --output build/requirements

python tools/validate_requirements.py `
  --prd build/requirements/prd.json `
  --srs build/requirements/srs.json `
  --rtm build/requirements/rtm.json `
  --strict
```

Choose a **new output directory** when you rerun extraction, because the extractor does not overwrite existing files. The validators check supported IDs, baseline relationships, coverage, and traceability. They **cannot** establish that stakeholder requirements are semantically correct.

Read the [Import Mode guide](docs/import-mode.md) before using project-owned documents.

---

## 8. Quality, architecture, and security

| Area | What the framework asks for |
|:---|:---|
| **Clean Architecture** | Boundaries and dependency direction suited to the project's scale. No unnecessary layers or speculative abstractions. |
| **Modern code** | Supported APIs and conventions for the actual language, framework, and versions in use. |
| **Clean code** | Readable, maintainable code, no harmful duplication, small and justified changes. |
| **UI quality** | Approved design decisions preserved, with responsive layout, accessibility, and real interaction states checked. |
| **Security review** | Defensive checks for access control, input handling, secrets, dependencies, and sensitive data, with evidence and limits documented. |
| **Testing and refactoring** | Relevant automated checks and regression coverage. An unrun check is never reported as passed. |

These are review and execution procedures, not proof that an application meets every quality or security standard. See [Engineering Quality](docs/engineering-quality.md), the [Code Quality skill](skills/code-quality/SKILL.md), and the [Security Review skill](skills/security-review/SKILL.md).

---

## 9. Quick start

### Prerequisites

- Git and Python.
- A terminal and an AI coding assistant with access to your project files, or an engineer following the procedures manually.
- Whatever tools your target application needs (for example Flutter, PHP, Go, or Node.js).

PREZEKC is **distributed as a repository**. No npm or PyPI package and no dedicated AI model is required.

### Step 1: Get the framework

```powershell
git clone https://github.com/Hasanah977/prezekc-ai-framework.git
cd prezekc-ai-framework
```

### Step 2: Verify the framework

```powershell
python tools/validate_framework.py --strict
python -m unittest discover -s tests -v
```

Do not assume a pass from this README. Use the actual terminal output from your environment.

### Step 3: Initialize one project

```powershell
python tools/prezekc.py init --project "D:\Projects\my-application"
```

The initializer makes PREZEKC's project instructions available inside your application folder. Inspect its output and any existing project instructions, and do not overwrite earlier configuration or user files without approval. Details: [installation guide](docs/installation.md).

Open **only your application folder** in VS Code or your coding environment. You do not need a multi-root workspace.

### Step 4: Give your assistant its first instruction

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

> **Using Gemini on the web?** An attached GitHub repository helps Gemini analyze the framework documents, but it does not give Gemini access to files on your computer or let it run commands in your project. For direct code changes, use an AI coding environment with workspace access.

---

## 10. Verification

Deterministic utilities cover supported repository and requirements checks.

| Tool | Role |
|:---|:---|
| `tools/validate_framework.py` | Checks framework structure, skill metadata, and local links |
| `tools/extract_requirements.py` | Extracts supported PRD, SRS, and RTM Markdown into JSON |
| `tools/validate_requirements.py` | Checks supported requirement IDs, baselines, and traceability |
| `tools/quality_gate.py` | Checks the structure and evidence rules of supported quality reports |

The automated tests detect regressions in these mechanisms. A passing framework test does **not** mean the software you are building has passed its own unit, integration, security, UI, or device testing.

### Human-guided handoff

At a meaningful task boundary, the assistant reports:

```text
Completed             : What changed and why
Evidence              : Checks that actually ran and their results
Limitations           : What remains uncertain, blocked, or untested
Recommended next step : One practical action with a short reason
Decision              : Continue, revise, or choose another direction?
```

---

## 11. Scope and limitations

PREZEKC is a framework for guiding AI-assisted engineering. It is not a runtime with guaranteed autonomous agents, universal tool access, or automatic production deployment.

It does **not**:

- Independently verify human identity or approvals.
- Prove that arbitrary requirements are semantically correct.
- Guarantee secure or defect-free code.
- Promise token savings without measurement.

Build, platform, and production-readiness claims require **project-specific evidence**.

---

## 12. Documentation

| Start here | Purpose |
|:---|:---|
| [`AGENTS.md`](AGENTS.md) | Authority, agent conduct, and handoff rules |
| [`FRAMEWORK.md`](FRAMEWORK.md) | Framework concepts and operating model |
| [`docs/installation.md`](docs/installation.md) | Installation and single-project setup |
| [`docs/import-mode.md`](docs/import-mode.md) | PRD and SRS import-first workflow |
| [`docs/engineering-quality.md`](docs/engineering-quality.md) | Clean code, UI quality, and security reviews |
| [`core/next-action.md`](core/next-action.md) | Recommendations and human decisions |
| [`core/task-execution.md`](core/task-execution.md) | Planning, execution, and evidence-based reporting |
| [`docs/releases/v0.3.0-release-notes.md`](docs/releases/v0.3.0-release-notes.md) | What changed in v0.3.0 |
| [`CHANGELOG.md`](CHANGELOG.md) | Version history |

### Contributing and feedback

Issue reports, corrections, and engineering feedback are welcome through [GitHub Issues](https://github.com/Hasanah977/prezekc-ai-framework/issues). Proposed changes should preserve existing approval boundaries, avoid unsupported claims, and pass the applicable validation checks.

---

## 13. License

**No open-source license is currently included in this repository.** All rights remain reserved by the applicable copyright holders unless and until an explicit license is published. Public visibility alone does not grant permission to redistribute or modify its contents beyond applicable legal rights.

---

<p align="center">
  <img src="assets/logo-pcs-3d.png" alt="PREZEKC" width="64"><br>
  <b>PREZEKC AI Framework</b><br>
  <sub>Requirements-driven · Skill-based · Human-guided · Evidence-verified</sub>
</p>