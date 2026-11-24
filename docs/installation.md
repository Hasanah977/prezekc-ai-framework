# Install PREZEKC in a Single Project

PREZEKC is a repository-based engineering framework. It is **not** an npm package, PyPI package, or autonomous AI runtime.

## Requirements

- Git and Python 3.12+ for the documented tools.
- An AI coding assistant capable of reading local project files.
- The PREZEKC repository cloned locally.

## Preferred: Bootstrap a Separate Project

From the framework repository:

```powershell
python tools/prezekc.py init --project "D:\\Projects\\my-app"
```

This command creates `.prezekc/framework/` as a local copy of the framework instructions and tool set, and creates a **root** `AGENTS.md` only if one does not already exist. It refuses to overwrite existing project files. The framework source repository is not modified.

If the project already has `AGENTS.md`, do not overwrite it; instead merge the short PREZEKC entry-point instructions manually after reviewing the existing project rules.

## Start an Agent Session

Open **only** the target project folder in VS Code, Antigravity, or another compatible IDE. Ask the agent:

```text
Use PREZEKC in .prezekc/framework. Read AGENTS.md and the
relevant core protocol, role contract, and skill for this task.
Inspect existing project baselines and changes before acting.
Do not auto-approve documents or proceed past a gated decision.
Report real verification evidence and recommend one next step.
```

Agent discovery rules differ across platforms. A root `AGENTS.md` is a useful entry point, but **automatic activation is not guaranteed**; explicitly reference it if the assistant does not load it.

## Verification

```powershell
python .prezekc/framework/tools/validate_framework.py --strict
```

Run requirements tools from the project root with appropriate relative paths. See [Import Mode](import-mode.md).

## Updating

Re-run the bootstrap with a **fresh target** or manually review and replace the embedded framework after backing up the previous copy. The initializer deliberately will not overwrite `.prezekc/framework/` to protect local project changes.
