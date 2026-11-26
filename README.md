<p align="center">
  <img src="assets/logo-pcs-3d.png" alt="PREZEKC AI logo" width="140">
</p>

<h1 align="center">PREZEKC AI</h1>

<p align="center">
  <b>Give your AI coding assistant a process, not just a prompt</b><br>
  <sub>A requirements-driven framework of skills, templates, and validators that walks your assistant<br>
  from idea to verified code, one stage at a time, with you making the calls that matter.</sub>
</p>

<p align="center">
  <a href="CHANGELOG.md"><img src="https://img.shields.io/badge/Release-v0.3.0-blue.svg?style=for-the-badge&logo=git&logoColor=white" alt="Release v0.3.0"></a>
  <a href="https://github.com/Hasanah977/prezekc-ai-framework/actions"><img src="https://img.shields.io/github/actions/workflow/status/Hasanah977/prezekc-ai-framework/framework-validation.yml?branch=main&label=framework%20validation&style=for-the-badge&logo=githubactions&logoColor=white" alt="Framework validation workflow status"></a>
  <a href="#5-quick-start"><img src="https://img.shields.io/badge/Python-3.12%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.12 or later"></a>
  <a href="#9-license"><img src="https://img.shields.io/badge/License-Not%20selected-lightgrey?style=for-the-badge" alt="License not selected"></a>
</p>

> **The short version.** PREZEKC is a set of rules, skills, templates, and small Python checkers that live in a repository. It is not an AI model and not an autonomous agent. Your assistant does the work, PREZEKC keeps the work in order, and it only helps as much as the assistant actually follows it.

<p align="center">
  <b>Jump to:</b>
  <a href="#1-what-prezekc-is">What it is</a> ·
  <a href="#2-the-problem-it-solves">Problem</a> ·
  <a href="#3-your-first-workflow">First workflow</a> ·
  <a href="#4-whats-inside">What's inside</a> ·
  <a href="#5-quick-start">Quick start</a> ·
  <a href="#6-import-mode">Import mode</a> ·
  <a href="#8-documentation-and-contributing">Docs</a>
</p>

---

## 1. What PREZEKC is

You give your assistant a goal once. From there it works stage by stage: it explains what it did, shows its evidence, asks what it needs to know, and recommends the next step. You answer "continue" or "fix this part". That loop is the whole idea.

PREZEKC is built for students, developers, and small teams who use AI assistants and are tired of long prompts that go in circles.

---

## 2. The problem it solves

| Instead of | PREZEKC gives you |
|:---|:---|
| Pasting a long prompt every session | Rules and skills that live in the repo, so the assistant reads them itself |
| The AI jumping straight to code | Analysis and requirements first |
| Features nobody asked for | Every feature traced to an approved requirement (PRD, SRS, RTM) |
| Wondering what to do next | A short report at each stage, with one recommended next step |
| "Done" with no proof | Reports that say which checks ran, passed, failed, or never ran |
| The AI deciding everything | Your approval at the points that matter |

The assistant also loads only the skill it needs for the current stage, instead of reading everything at once.

---

## 3. Your first workflow

```text
You:  I want a web app for renting traditional clothing. Help me build it.
```

What happens next:

| Step | Stage | What the assistant does | What you do |
|:---:|:---|:---|:---|
| 1 | **Understand** (P01 to P03) | Studies the problem, compares alternatives, lists needs and constraints | Answer a few questions |
| 2 | **PRD** (P04) | Writes or imports the product requirements | **Approve** or ask for changes |
| 3 | **SRS and RTM** (P05) | Turns the PRD into testable requirements and links them back | **Approve** or ask for changes |
| 4 | **Design** (P06) | Proposes architecture, database, APIs, and UI/UX flow | **Approve** the architecture |
| 5 | **Tasks** | Splits the design into small tasks with acceptance criteria | Pick what comes first |
| 6 | **Build** (P07) | Implements one task, following the code-quality skill | Review |
| 7 | **Verify** (P08) | Runs checks, reviews security, reports honestly | Continue or revise |
| 8 | **Release** (P09) | Prepares release and maintenance records | **Approve** the release |

Every stage ends with the same short report:

```text
Completed             : What changed and why
Evidence              : Checks that actually ran and their results
Limitations           : What remains uncertain, blocked, or untested
Recommended next step : One practical action with a short reason
Decision              : Continue, revise, or choose another direction?
```

Small changes do not restart the whole lifecycle. On an existing project, the assistant inspects the code, finds the relevant task and baseline, and loads only what it needs.

---

## 4. What's inside

| Part | What it is | Where |
|:---|:---|:---|
| **15 skills** | Task-focused instructions the assistant loads one at a time | [`skills/`](skills/) |
| **6 roles** | Responsibilities (not six separate AIs): Research Analyst, System Analyst, Requirements Engineer, System Architect, Development Engineer, Verification Engineer | [`AGENTS.md`](AGENTS.md) |
| **Templates** | Standard formats for PRD, SRS, RTM, and analysis documents | [`templates/`](templates/) |
| **4 Python tools** | Check structure, extract requirements, validate traceability, check quality reports | [`tools/`](tools/) |
| **Governance** | Who decides what, and how work moves between stages | [`core/`](core/) |

<details>
<summary><b>The 15 skills</b></summary>

<br>

| Area | Skills |
|:---|:---|
| **Discovery and requirements** | [`system-analysis`](skills/system-analysis/SKILL.md) · [`comparative-study`](skills/comparative-study/SKILL.md) · [`requirement-analysis`](skills/requirement-analysis/SKILL.md) · [`prd-generation`](skills/prd-generation/SKILL.md) · [`prd-to-srs`](skills/prd-to-srs/SKILL.md) |
| **Design and planning** | [`system-design`](skills/system-design/SKILL.md) · [`ui-ux-flow`](skills/ui-ux-flow/SKILL.md) · [`ui-design`](skills/ui-design/SKILL.md) · [`task-breakdown`](skills/task-breakdown/SKILL.md) |
| **Development and quality** | [`web-development`](skills/web-development/SKILL.md) · [`mobile-development`](skills/mobile-development/SKILL.md) · [`code-quality`](skills/code-quality/SKILL.md) · [`security-review`](skills/security-review/SKILL.md) · [`testing`](skills/testing/SKILL.md) |
| **Delivery** | [`deployment`](skills/deployment/SKILL.md) |

</details>

<details>
<summary><b>The 4 Python tools</b></summary>

<br>

| Tool | What it checks |
|:---|:---|
| `tools/validate_framework.py` | Framework structure, skill metadata, local links |
| `tools/extract_requirements.py` | Turns supported PRD, SRS, and RTM Markdown into JSON |
| `tools/validate_requirements.py` | Requirement IDs, baselines, and traceability |
| `tools/quality_gate.py` | Structure and evidence rules of quality reports |

A passing framework check says nothing about the app you are building. That app still needs its own tests.

</details>

---

## 5. Quick start

**You need:** Git, Python, a terminal, and an AI coding assistant that can read your project files (or an engineer following the steps by hand). PREZEKC is distributed as a repository, so there is no package to install.

**1. Get the framework**

```powershell
git clone https://github.com/Hasanah977/prezekc-ai-framework.git
cd prezekc-ai-framework
```

**2. Check that it works**

```powershell
python tools/validate_framework.py --strict
python -m unittest discover -s tests -v
```

Read the real terminal output. Do not assume a pass.

**3. Set up your project**

```powershell
python tools/prezekc.py init --project "D:\Projects\my-application"
```

This makes PREZEKC's instructions available inside your application folder. Check its output first, and do not overwrite existing configuration without approval. More in the [installation guide](docs/installation.md). Open only your application folder in your editor.

**4. Give your assistant its first instruction**

```text
Use PREZEKC AI Framework for this project.

1. Read the installed AGENTS.md and FRAMEWORK.md.
2. Inspect the project without changing any files yet.
3. Load only the skill relevant to our current task.
4. Report the current state, the main gaps, and one recommended next step.
5. Ask for my decision before major changes or phase transitions.

Do not invent missing files, approvals, tests, or requirements.
```

> **Using Gemini on the web?** Attaching the GitHub repo lets Gemini read the framework documents, but it cannot reach files on your computer or run commands in your project. For direct code changes, use an assistant with workspace access.

---

## 6. Import mode

Writing a long PRD or SRS eats tokens. You do not have to do it inside PREZEKC. Write them in Google Docs, another AI tool, or any editor, then bring the supported Markdown in:

```text
External PRD draft -> import and inspect -> approve PRD
   -> SRS draft from the approved PRD -> import and validate -> approve SRS
   -> design and implementation
```

Try it with the included samples:

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

Use a new output folder each time, because the extractor does not overwrite files. The tools read the supported Markdown format, not Word or PDF. They can check IDs and links between requirements, but they cannot tell you whether the requirements themselves are right. Importing never replaces human review. Details are in the [Import Mode guide](docs/import-mode.md).

---

## 7. What it will not do

- Guarantee bug-free or secure software.
- Check who actually approved something, or prove your requirements are correct.
- Run by itself. Its skills only work when your assistant reads and follows them.
- Promise token savings. That would need measuring, and it has not been done yet.

Build, platform, and release claims for your own app need your own evidence.

---

## 8. Documentation and contributing

| Start here | What you will find |
|:---|:---|
| [`AGENTS.md`](AGENTS.md) | Authority, assistant conduct, and handoff rules |
| [`FRAMEWORK.md`](FRAMEWORK.md) | Concepts and operating model |
| [`docs/installation.md`](docs/installation.md) | Setup for a single project |
| [`docs/import-mode.md`](docs/import-mode.md) | The import-first PRD and SRS workflow |
| [`docs/engineering-quality.md`](docs/engineering-quality.md) | Clean code, UI quality, and security reviews |
| [`core/next-action.md`](core/next-action.md) | How recommendations and decisions work |
| [`core/task-execution.md`](core/task-execution.md) | Planning, execution, and reporting |
| [`CHANGELOG.md`](CHANGELOG.md) | Version history |

Found a mistake or have feedback? Open an issue on [GitHub Issues](https://github.com/Hasanah977/prezekc-ai-framework/issues). Changes should keep the approval boundaries, avoid unsupported claims, and pass the validation checks.

---

## 9. License

No open-source license is included yet. Until one is published, all rights stay with the copyright holders, and public visibility alone does not give anyone permission to redistribute or modify the contents beyond what the law already allows.

---

<p align="center">
  <img src="assets/logo-pcs-3d.png" alt="PREZEKC" width="56"><br>
  <b>PREZEKC AI</b><br>
  <sub>Requirements-driven · Skill-based · Human-guided · Evidence-verified</sub>
</p>