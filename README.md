<div align="center">

# PREZEKC AI

**A skill-driven engineering workflow for AI coding agents.**

Understand the problem. Preserve the requirements. Design the experience. Build in controlled steps. Verify what actually works.

**v0.2.0 · Development Candidate**

[![Framework Validation](https://github.com/Hasanah977/prezekc-ai-framework/actions/workflows/framework-validation.yml/badge.svg)](https://github.com/Hasanah977/prezekc-ai-framework/actions/workflows/framework-validation.yml)
![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-development%20candidate-orange)

[Install](#installation) · [How It Works](#how-it-works) · [Import Requirements](#requirements-import) · [Agent Skills](#agent-skills) · [Documentation](#documentation)

</div>

---

## Why PREZEKC?

An AI assistant can write code, but code alone does not show whether the system meets a real need. Without a consistent operating method, the assistant may skip analysis, invent features, assume an interface, or report a task as complete before testing it.

**PREZEKC AI is an engineering operating framework, not a new AI model or autonomous runtime.** It gives a compatible AI coding assistant explicit rules for making decisions, selecting skills, working from approved artifacts, limiting changes, and reporting verifiable results.

Its core commitments are straightforward:

- **Requirements before guesses.** Product intent and system behavior are established before production implementation.
- **Import before regenerate.** Reuse PRD and SRS written in external tools; generate new documents only when requested.
- **Design before coding.** Define system architecture, user journeys, screens, and interaction states before implementation tasks.
- **Skills on demand.** Load the relevant agent role and skill instead of the entire framework for every task.
- **Small, traceable tasks.** Implement authorized increments tied to requirements and design.
- **Evidence, then decisions.** Report real checks, recommend the next action, and ask for human decisions at meaningful checkpoints.

## How It Works

PREZEKC retains its engineering lifecycle **P01–P09** while adding an explicit design-to-task handoff:

```text
Idea / Existing Project
        |
        v
  Project Intake
        |
        v
P01 System Analysis --> P02 Comparative Study
        |
        v
P03 Requirement Analysis
        |
        v
P04 PRD (Import-First or Optional Authoring)
        |
   Owner Approval
        v
P05 SRS + RTM (Import-First or Optional Authoring)
        |
   Owner Approval
        v
P06 SDD / System Design <--> UI/UX Flow
        |
   Design Approval
        v
Task Breakdown
        |
        v
P07 Implementation -> P08 Verification
        |
   Release Approval
        v
P09 Deployment & Maintenance
```

**PRD** defines product goals, users, features, scope, and user flows at the product level. **SRS** specifies testable behavior, validation, permissions, failure handling, and quality requirements. **SDD** defines architecture, data models, API contracts, integration, and backend components. **UI/UX Flow** establishes journeys, navigation, screens, and interaction states. **Task Breakdown** turns approved design into ordered, verifiable implementation work.

Artifacts are not self-approving. Validation results and **human authorization are separate conditions**. For existing projects, the assistant first inspects approved baselines and begins from the relevant activity rather than mechanically recreating every phase.

### Human-Guided Next Actions

At meaningful checkpoints, the agent provides:

1. **Completed:** what actually changed or was produced.
2. **Verified:** checks run and their real results; identify checks not run.
3. **Open:** remaining issues, risks, and decisions.
4. **Recommended:** one next step and why it is appropriate.
5. **Decision:** ask whether the owner wants to proceed, review, or choose another direction.

The assistant should **recommend** a sensible next action when the owner is unsure. It must not treat its own recommendation as approval. See the [Next Action Protocol](core/next-action.md).

## Agent Skills

PREZEKC v0.2.0 provides **12 engineering skills**, invoked as needed:

| Skill | Use it when |
|---|---|
| [`system-analysis`](skills/system-analysis/SKILL.md) | Investigating a current process, stakeholders, problems, and evidence |
| [`comparative-study`](skills/comparative-study/SKILL.md) | Comparing credible approaches and solutions |
| [`requirement-analysis`](skills/requirement-analysis/SKILL.md) | Eliciting and refining needs and constraints |
| [`prd-generation`](skills/prd-generation/SKILL.md) | Importing/reviewing a PRD or optionally authoring one |
| [`prd-to-srs`](skills/prd-to-srs/SKILL.md) | Importing/reviewing an SRS and RTM, or optionally deriving them from an approved PRD |
| [`system-design`](skills/system-design/SKILL.md) | Defining an implementable SDD, architecture, data, and APIs |
| [`ui-ux-flow`](skills/ui-ux-flow/SKILL.md) | Specifying user journeys, navigation, screens, and UI states |
| [`task-breakdown`](skills/task-breakdown/SKILL.md) | Planning small, sequenced tasks with acceptance criteria |
| [`web-development`](skills/web-development/SKILL.md) | Implementing web application changes |
| [`mobile-development`](skills/mobile-development/SKILL.md) | Implementing Android, iOS, or cross-platform application changes |
| [`testing`](skills/testing/SKILL.md) | Creating and executing applicable verification |
| [`deployment`](skills/deployment/SKILL.md) | Preparing and controlling releases and operational handoff |

Six logical engineering roles govern work: Research Analyst, System Analyst, Requirements Engineer, System Architect, Development Engineer, and Verification Engineer. They are **role contracts**, not six independent running AI instances.

## Installation

PREZEKC is distributed as a **Git repository**; it does not currently support `npx prezekc-ai init` or `pip install prezekc-ai`.

**Prerequisites:** Git, Python 3.12+, and an AI assistant with access to local project files.

### 1. Clone the framework

```powershell
git clone https://github.com/Hasanah977/prezekc-ai-framework.git
cd prezekc-ai-framework
```

### 2. Verify the framework

```powershell
python tools/validate_framework.py --strict
python -m unittest discover -s tests -v
```

### 3. Install into one project

Create or select a separate **existing** project folder, then run from the PREZEKC repository:

```powershell
python tools/prezekc.py init --project "D:\Projects\my-app"
```

The initializer copies framework instructions/tools into `my-app/.prezekc/framework/` and creates a root `AGENTS.md` **only if none exists**. It refuses to overwrite an existing framework installation or project rules. The framework repository remains separate; the IDE needs to open **only `my-app`**.

> The initializer provides a portable local reference. Automatic instruction discovery varies by coding assistant, so explicitly ask the agent to read the project `AGENTS.md` if it has not done so.

For caveats and updates, see the [Single-Project Installation Guide](docs/installation.md).

### 4. Start your AI assistant

In the target project's chat or agent mode:

```text
Use PREZEKC AI from .prezekc/framework for this project.
Read the project AGENTS.md, the relevant core protocol,
and only the role contract and SKILL.md needed for my task.

Inspect existing files, requirements, and approvals first.
Do not invent features, approval records, or test results.
After a meaningful task, show actual verification,
recommend the best next action, and ask for my decision.
```

## Requirements Import

**PRD and SRS remain first-class requirements artifacts.** Import Mode is the preferred method when documents have already been written by the owner or an external AI/editor.

1. Draft PRD using [`templates/prd.md`](templates/prd.md), with goals, users, scope, features, and product-level flows.
2. Import its **supported Markdown** representation; review sources, IDs, and semantics. The owner **approves the PRD** before it is used as the authoritative SRS baseline.
3. Draft SRS using [`templates/srs.md`](templates/srs.md) and the approved PRD; create an [`RTM`](templates/requirement-traceability-matrix.md).
4. Import and validate both. The owner **approves the SRS separately** before design becomes the implementation baseline.

The existing Python extraction utilities do **not** ingest arbitrary PDF/DOCX files directly; convert external documents faithfully to the supported Markdown format first. Import is not a substitute for human requirements review.

### Run extraction

From the framework repository, using the supplied fixture documents:

```powershell
python tools/extract_requirements.py `
  --prd examples/markdown/prd.md `
  --srs examples/markdown/srs.md `
  --rtm examples/markdown/rtm.md `
  --output build/requirements
```

### Validate mappings

```powershell
python tools/validate_requirements.py `
  --prd build/requirements/prd.json `
  --srs build/requirements/srs.json `
  --rtm build/requirements/rtm.json `
  --strict
```

Choose a fresh output directory for each extraction. The extractor does not overwrite an existing manifest. Use your own approved documents instead of the fixtures for real work.

See the detailed [Import-First Guide](docs/import-mode.md).

## Design, UI/UX, and Task Planning

| Artifact | Primary questions | Template |
|---|---|---|
| **SDD** | How do components, database, API, security, and backend work? | [System Design](templates/system-design.md) |
| **UI/UX Flow** | What does each actor see and do, including error and offline states? | [UI/UX Flow](templates/ui-ux-flow.md) |
| **Task Breakdown** | What is the smallest demonstrable increment, in what order, and how will it be checked? | [Task Breakdown](templates/task-breakdown.md) |

System design and interface flow may be refined iteratively. Both must remain consistent with approved requirements. Diagrams are optional when tables or prose convey the decision more clearly.

## Verification

PREZEKC includes three Python utilities:

- `tools/validate_framework.py` — repository structure, skill metadata, and local references.
- `tools/extract_requirements.py` — supported Markdown PRD/SRS/RTM to JSON.
- `tools/validate_requirements.py` — supported identifiers, baselines, coverage, and traceability.

Validation is also configured through [GitHub Actions](https://github.com/Hasanah977/prezekc-ai-framework/actions/workflows/framework-validation.yml).

The v0.1.0 baseline was reported to pass **31 unit tests** locally, with framework and requirements validations reporting zero errors and warnings. **v0.2.0 remains a development candidate** until its new/updated checks pass on the final release commit and the release is authorized. Do not treat that earlier result as verification of the new release.

Automated checks do not prove semantic correctness, production suitability, actual user approval, or successful application deployment.

## Documentation

- [Agent Operating Contract](AGENTS.md)
- [Framework Specification](FRAMEWORK.md)
- [Governance](core/governance.md) · [Workflow](core/workflow.md) · [Verification](core/verification.md)
- [Import-First PRD/SRS](docs/import-mode.md)
- [Human-Guided Next Actions](core/next-action.md)
- [Task Execution Contract](core/task-execution.md)
- [Single-Project Installation](docs/installation.md)
- [Full Lifecycle](workflows/full-lifecycle.md) · [Web](workflows/web-application.md) · [Mobile](workflows/mobile-application.md)

## Contributing

Bug reports and engineering feedback are welcome via [GitHub Issues](https://github.com/Hasanah977/prezekc-ai-framework/issues). Proposals that affect approval gates or scope control require explicit review. Run the available checks and report their outputs before submitting changes.

## License

**No open-source license has been granted for this repository at this time.** The respective copyright holders retain their rights. Public GitHub visibility does not, by itself, authorize reuse or redistribution beyond applicable law and platform terms. Licensing may be established in a later release.

---

<div align="center">

**PREZEKC AI · v0.2.0 Development Candidate**

*Skill-driven execution. Import-first requirements. Human-guided decisions. Verifiable outcomes.*

</div>
