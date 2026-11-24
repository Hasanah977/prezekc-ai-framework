---
name: ui-design
description: >
  Design and review visual UI quality for web and mobile applications,
  preserving approved UI/UX flows, existing design systems, accessibility,
  responsive behavior, and testable interaction states. Use when visual
  styling, components, layouts, or usability quality are in scope.
version: 0.3.0
category: system-design
---

# UI Design & Experience Quality

## Purpose

Create and review purposeful, coherent, accessible interfaces **without overriding approved visual references or inventing features**. This skill complements [`ui-ux-flow`](../ui-ux-flow/SKILL.md): the latter defines interactions; this skill defines visual and component execution.

## Activate When

- The task changes layouts, styles, components, responsiveness, or interface polish.
- Visual inconsistency or generic, repetitive AI-generated design must be reviewed.
- The user asks to match a screenshot, Figma reference, or existing design system.

Do not activate for backend-only work.

## Required Inputs

- Approved PRD/SRS and UI/UX flow **when available and applicable**; otherwise state that the work is a draft.
- Existing brand guidelines, screenshot references, component library, and responsive targets.
- Accessibility expectations and relevant device/platform constraints.

## Workflow

1. **Inspect first:** identify existing tokens, components, UI references, and states. Never silently replace established styling.
2. **Clarify intent:** document information hierarchy, density, contrast, typography, and interaction priorities. Avoid arbitrary trendy patterns.
3. **Specify reusable components:** states (default, hover where relevant, focus, disabled, loading, error, success), variants, and responsibilities.
4. **Respect requirements:** screen content, role permissions, form behavior, validation, and journeys trace to approved inputs.
5. **Implement incrementally:** limit changes to authorized screens; retain original text, data, and behavior unless explicitly changed.
6. **Review device behavior:** test actual relevant viewport sizes and device orientations; do not claim responsiveness from CSS inspection alone.
7. **Review accessibility:** semantic structure, accessible names, contrast, focus order, keyboard interaction where applicable, scalable text, and reduced motion.
8. **Verify visually:** use screenshots or user/device review when tools permit; otherwise mark visual checks `NOT_RUN`.
9. **Report:** include deviations, evidence, unresolved choices, and one recommended next step. Use [`next-action`](../../core/next-action.md).

## Do Not

- Force one aesthetic template on every product.
- Change approved UI/UX without a change decision.
- Claim WCAG compliance without sufficient evidence.
- Add decorative animations at the cost of usability or performance.

## Output

Use [`templates/ui-design-review.md`](../../templates/ui-design-review.md). Record source references, component inventory, states, viewport coverage, accessibility findings, evidence, and owner decisions.
