# Import-First Requirements Workflow

> PREZEKC AI Framework v0.2.0 — P04/P05 operating guidance

## Why Import-First?

PRD and SRS remain essential engineering artifacts. PREZEKC does not require its AI coding assistant to author their long-form text when the owner can provide a document created elsewhere. Existing approved documents must be reused rather than regenerated.

Import-first can reduce *coding-agent context consumption*. It does not establish total token or monetary savings without measurement.

## P04 — PRD

1. Use [PRD Template](../templates/prd.md) to guide an external editor or AI assistant.
2. Inspect provenance: product problem, target users, goals, scope, flows, acceptance outcomes, and requirement IDs.
3. Save a **supported Markdown** version in the project as `docs/requirements/prd.md` (name may vary).
4. Review semantic consistency and gaps. Current Python validators cannot independently authenticate sources or prove requirements are correct.
5. Record explicit owner approval and version **before** using PRD as the authoritative baseline for SRS finalization.

## P05 — SRS and RTM

1. Use the **approved** PRD as the SRS source, even when authoring externally.
2. Follow [SRS Template](../templates/srs.md) and [RTM Template](../templates/requirement-traceability-matrix.md).
3. Import SRS and RTM in supported Markdown format. Keep identifiers and PRD baseline references stable.
4. Run the [requirements extraction and validation tools](../README.md#requirements-import).
5. Review requirements behavior, validation, security, access, errors, and traceability. Human review remains essential.
6. Record SRS approval separately from PRD approval. Only approved baselines advance to controlled SDD/implementation.

## Mode Selection

- `IMPORT` (preferred): user supplies document(s). Inspect/review/validate, do not rewrite without authorization.
- `AUTHOR` (optional): assist writing with the existing skill; document remains draft until approved.
- `REVISE`: controlled change to an existing baseline, with impact assessment and new approval as needed.

If a document was created as PDF or DOCX, first produce a faithful Markdown version compatible with the parser; direct arbitrary PDF/DOCX parsing is **not** provided by the v0.1.0 extraction tool.

## Required Safeguards

- Never silently invent an approval record or set `APPROVED` merely to satisfy validation.
- No PRD approval means no final authoritative SRS baseline.
- No SRS approval means no approved implementation baseline; exploratory drafts must be explicitly labeled.
- Extraction success is **not** semantic validation.
- For sensitive content, review what may be sent to external AI systems.

## Next Step

Use the [Next Action Protocol](../core/next-action.md) to recommend review, approval, or P06 and ask the owner at the appropriate boundary.
