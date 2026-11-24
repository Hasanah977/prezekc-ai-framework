# Human-Guided Next Action Protocol

> PREZEKC AI Framework v0.2.0 — Agent operating extension

## Objective

Make every meaningful task handoff understandable to the project owner. The agent must explain progress and recommend a next action, without silently crossing an approval boundary.

## When to Apply

At a phase boundary, an approved task/batch completion, a material blocker, an architecture or scope decision, or when the user asks what to do next. Do not interrupt every trivial editing step already authorized inside one task.

## Required Closing Report

Use this compact structure. Omit inapplicable details, but do not fabricate evidence.

1. **Completed:** actual deliverables and relevant file paths; distinguish partial work.
2. **Verified:** command/test, actual result, and `PASS`, `FAIL`, `NOT_RUN`, `BLOCKED`, or `NOT_APPLICABLE`.
3. **Open:** defects, missing information, unresolved risks, and pending approvals.
4. **Recommended next action:** one concrete action with a brief reason and prerequisite.
5. **Decision requested:** ask whether the owner wants to proceed, review/revise, or choose a different action. If the owner does not know, explain the recommended option in plain language.

## Decision Rules

- Never infer `OWNER_APPROVED` from silence, praise, successful tool execution, or validator success.
- For material irreversible actions, ask specific approval even if adjacent work was approved.
- Where no approval is needed and the owner authorized a multi-step task, finish that task before asking.
- If next-step prerequisites are unmet, recommend resolving them instead of proceeding.
- Do not claim to have changed project state without a real file change or verified event.
- A recommended action is not an authorized action.

## Example

**Completed:** `docs/design/sdd.md` drafted; no implementation files changed.

**Verified:** Markdown links PASS; architecture review NOT_RUN.

**Open:** API authentication choice and design approval pending.

**Recommended next action:** review authentication choice and SDD, then draft UI/UX Flow because user-facing journeys remain undefined.

**Decision:** Would you like to review the SDD first, or should I explain the options?
