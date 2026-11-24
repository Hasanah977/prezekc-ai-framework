---
name: ui-ux-flow
description: >
  Design and review user journeys, navigation, screen inventories,
  interface states, and interaction contracts against an approved
  product and software requirements baseline. Use during P06 before
  development tasks are finalized, or when an approved UI flow changes.
version: 0.2.0
category: system-design
---

# UI/UX Flow Engineering

## Purpose

Define **how users move through the product and how interfaces respond** without inventing product features. The output is a reviewable flow specification, not automatically a finished visual design.

## Activate When

- User journeys, navigation, screen lists, or wireframe specifications are needed.
- A developer would otherwise have to guess validation messages, empty states, errors, loading, or permissions.
- A change affects user-facing navigation or interaction.

Do not activate for pure backend refactoring without user-visible impact.

## Required Inputs

1. Identifiable PRD and approved SRS baseline, or an explicitly authorized `DRAFT` prototype context.
2. Actor permissions, intended platform, supported devices, and relevant constraints.
3. Existing UI references and design system, where available.
4. Technical constraints from the SDD, where relevant.

If an input is missing, list the gap; do not invent user research or claim design approval.

## Procedure

1. **Identify actors and tasks.** Map each journey to SRS requirement IDs.
2. **Define entry and exit points.** Record prerequisites, success results, and recovery paths.
3. **Map navigation.** Describe screens, actions, branches, back behavior, and protected routes.
4. **Specify each screen.** Define fields, content, validation, control states, permissions, and feedback.
5. **Cover exceptional states.** Include loading, empty, offline, error, permission denied, confirmation, success, and retry *where applicable*.
6. **Check accessibility and responsiveness.** Choose relevant accessibility and device considerations rather than assuming universal suitability.
7. **Coordinate with System Architect.** Align screens with API/data behavior and SDD; flag inconsistencies instead of modifying SRS silently.
8. **Review with the owner.** Provide a small set of material decisions and request design approval before implementation baseline.

Use diagrams or clickable prototypes only when they materially improve understanding; a text flow may suffice.

## Deliverable

Use [UI/UX Flow Template](../../templates/ui-ux-flow.md). Include:

- Document control and status (`DRAFT`, `REVIEW`, `APPROVED`).
- Users, journeys, navigation flow, and screen inventory.
- Interaction and state matrix, accessibility considerations, and references to SRS IDs.
- Open decisions, verification evidence, and approval record.

## Completion Gate

- Every in-scope critical user journey is mapped to requirements.
- No unapproved feature, actor, or permission is introduced.
- Critical success, failure, and offline conditions are visible.
- Review outcome is reported; `APPROVED` must never be self-assigned.

## Handoff

Hand off approved flow references to `task-breakdown`, then `web-development` or `mobile-development`. Use [Next Action Protocol](../../core/next-action.md) to propose the next step and obtain the applicable decision.
