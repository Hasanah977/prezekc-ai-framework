---
name: task-breakdown
description: >
  Decompose approved requirements, system design, and user flows into
  small, sequenced implementation tasks with dependencies, acceptance
  criteria, required evidence, and explicit handoff decisions. Use
  before P07 and after approved scope changes.
version: 0.2.0
category: implementation-planning
---

# Task Breakdown Engineering

## Purpose

Translate an approved design into **small, verifiable units of work**. A task list is not proof that development has occurred.

## Activation

- Starting P07 after design approval.
- Planning implementation of a feature, refactor, or maintenance change.
- Replanning due to changed requirements or verified defects.

## Preconditions

- Approved SRS and SDD baselines, or a clearly labeled, explicitly authorized prototype scope.
- UI/UX Flow for affected user journeys, if applicable.
- Platform, repository constraints, and verification tools.
- Identifiable open decisions and blockers.

Stop and request missing decisions before committing to implementation tasks that depend on them.

## Procedure

1. Enumerate in-scope SRS IDs and design/UI flow references.
2. Break work into coherent increments, each with one demonstrable result.
3. Record task ID, objective, owner role, prerequisites, dependencies, files/components if known, acceptance criteria, and tests.
4. Order tasks by dependencies and risk. Identify the critical path and parallelizable tasks without inventing staff availability.
5. Include error handling, security/privacy work, migration, tests, and integration only when relevant to the approved scope.
6. Assign status `TODO`, `IN_PROGRESS`, `BLOCKED`, `READY_FOR_REVIEW`, or `DONE` based on verified evidence. Never mark all tasks done at planning time.
7. Review scope, ordering, and effort assumptions with the owner. Do not create unsupported time or cost commitments.
8. At execution time, authorize an agreed task or batch, apply the smallest complete change, verify, and report actual results.

## Deliverable

Use [Task Breakdown Template](../../templates/task-breakdown.md). Link tasks to SRS/SDD/UI flow IDs. Include acceptance criteria, verification plan, blockers, and approval status.

## Quality Gate

- Every mandatory implementation requirement has at least one task or an explicit justified exception.
- Each task has a testable completion condition and dependencies.
- No design or product decision is silently invented.
- Planning approval and task completion are separate.

## Handoff

Offer a recommended first task with reasons and request authorization according to [Next Action Protocol](../../core/next-action.md). Subsequent tasks use the same report and decision loop.
