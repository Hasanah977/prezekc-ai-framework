---
name: security-review
description: >
  Conduct authorized defensive application security reviews for web and mobile
  projects: access control, input handling, secrets, dependencies, secure
  storage, data exposure, configuration, and remediation evidence.
version: 0.3.0
category: verification
---

# Defensive Security Review

## Purpose

Identify and reduce application security risks with **scoped, evidence-based, authorized** reviews. A review is not a security certification or proof that a system is vulnerability-free.

## Activate When

- A task affects authentication, authorization, user data, API inputs, database access, storage, integrations, or deployment configuration.
- The owner requests a security check or a release is approaching.
- An incident, suspected defect, or sensitive-data handling change requires review.

## Authorization & Safety Boundaries

- Inspect only the current project and systems explicitly authorized by the owner.
- Prefer static review and local tests. No intrusive scanning of third-party/live targets without clear permission and scope.
- Never print credentials, private keys, access tokens, or actual sensitive user records in reports.
- Do not fabricate an exploitation demonstration to make a finding appear confirmed.

## Review Procedure

1. **Scope & assets:** document app stack, data sensitivity, entry points, trust boundaries, and permitted tools.
2. **Threat-informed inventory:** check broken object-level authorization, role access, validation, injection surfaces, authentication/session handling, CSRF where relevant, sensitive storage, secrets, logs, dependency advisories, and production configuration.
3. **Evidence:** identify precise file/line/behavior and what was actually observed; distinguish `CONFIRMED`, `POTENTIAL`, and `NOT_ASSESSED` findings.
4. **Risk & mitigation:** use a qualitative severity with impact and likelihood rationale. Avoid unsupported numerical security scores.
5. **Fix within scope:** coordinate with development; prefer minimal changes, preserve approved behavior, and add regression tests for confirmed weaknesses.
6. **Retest:** record exact commands, outputs, and outstanding limitations. Distinguish `PASS`, `FAIL`, `NOT_RUN`, `BLOCKED`.
7. **Handoff:** request owner review for high-risk changes and provide one recommended next action.

## Examples of Stack-Aware Review

- Web: server-side authorization, session and CSRF protections, escaping, error exposure, dependency advisories.
- Mobile/offline: secure local storage, cache lifecycle, account separation, synchronization authorization, privacy-safe diagnostics.
- APIs: object-level access checks, validation, rate limits where required, safe error responses, secrets and transport.

## Output

Use [`templates/security-review.md`](../../templates/security-review.md). Do not use offensive exploits or autonomous penetration-testing infrastructure as a default dependency.
