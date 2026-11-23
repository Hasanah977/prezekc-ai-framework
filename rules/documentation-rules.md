
# PREZEKC AI — Documentation Standards

**Specification:** Engineering Documentation Rules
**Version:** 0.1.0
**Status:** Draft
**Applicability:** Framework and Project Documentation

## 1. Purpose

Establish consistent requirements for authoring,
maintaining, reviewing, and controlling engineering
documentation produced under PREZEKC AI.

Documents must communicate verified information,
technical decisions, and implementation obligations
without ambiguity or unsupported assertions.

## 2. Document Classification

Documentation is classified by purpose.

| Class | Examples |
|---|---|
| Governance | Approval and change-control records |
| Analysis | Existing-system and comparative reports |
| Requirements | Requirement analysis, PRD, SRS |
| Design | Architecture, UML, data models, API specifications |
| Implementation | Component and configuration documentation |
| Verification | Test plans, test cases, execution reports |
| Operations | Deployment, release, recovery records |
| Framework | Agent, skill, rule, and workflow specifications |

Each document must have an identifiable purpose
and applicable owner or governing role.

## 3. Writing Standard

Use professional technical English for framework
specifications unless project requirements prescribe
another language.

Prefer:

- Direct statements.
- Defined terminology.
- Explicit requirements.
- Concrete procedures.
- Identifiable inputs and outputs.
- Verifiable acceptance conditions.

Avoid:

- Promotional descriptions.
- Repetitive introductions.
- Unsupported assertions.
- Unnecessary metaphors.
- Informal commentary.
- Ambiguous obligations.
- Filler text.

Use `must` for mandatory obligations,
`should` for recommended practices, and
`may` for permitted alternatives.

Do not use mandatory language for behavior
that has not been authorized or specified.

## 4. Document Structure

Controlled engineering documents should provide
the following information where applicable:

1. Document identity.
2. Purpose and scope.
3. Source references.
4. Requirements or technical content.
5. Constraints and assumptions.
6. Verification criteria.
7. Open issues.
8. Approval state.
9. Revision history.

Use the relevant document template.

A section may be omitted when the template
permits omission and the reason is recorded.

Do not populate irrelevant sections with
fabricated material.

## 5. Document Control

Controlled artifacts must identify:

- Document ID.
- Project or framework scope.
- Version.
- Lifecycle status.
- Owner or responsible role.
- Source baseline where applicable.
- Verification state.
- Approval state.

Do not assign approval values without an
identifiable approval decision.

The existence of a document does not establish
that it is complete or approved.

## 6. Status and Approval

Maintain separate records for document progress,
verification, and approval.

Document lifecycle status may include:

- `DRAFT`
- `IN_REVIEW`
- `APPROVED`
- `SUPERSEDED`

Verification results must use the applicable
states defined in `core/verification.md`.

Do not conflate `PASS` with `APPROVED`.

Document approval is governed by
`core/governance.md`.

Local templates must not create independent
approval or authority models.

## 7. Requirement Identification

Use stable identifiers for controlled requirements.

Applicable identifier families include:

| Prefix | Purpose |
|---|---|
| `NEED-*` | Stakeholder need |
| `REQ-*` | Requirement analysis candidate |
| `PRD-FR-*` | Product functional requirement |
| `PRD-NFR-*` | Product quality requirement |
| `SRS-FR-*` | System functional requirement |
| `SRS-NFR-*` | System quality requirement |
| `BUS-*` | Business rule |
| `DES-*` | Design element |
| `TC-*` | Test case |
| `CHG-*` | Change request |

An identifier must not be reused for an
unrelated requirement or engineering artifact.

Approved identifiers must remain stable
across document revisions.

## 8. Requirement Statements

Requirements must be:

- Necessary.
- Unambiguous.
- Consistent.
- Feasible within stated constraints.
- Traceable to authorized origins.
- Verifiable at the appropriate level.

Separate product outcomes from technical behavior.

PRD requirements describe intended product capabilities
and acceptance outcomes.

SRS requirements define observable system behavior
and objectively assessable quality properties.

Implementation decisions belong to design documents
unless explicitly mandated by approved requirements.

## 9. Evidence and References

Material findings require identifiable sources.

Record:

- Source identifier.
- Source title or description.
- Origin or location.
- Relevant date, when known.
- Supported claims.
- Applicable limitations.

Distinguish direct observations, stakeholder reports,
engineering inferences, and assumptions.

Do not fabricate citations or source metadata.

When evidence is contradictory, preserve the conflict
until it is resolved through an identifiable decision.

## 10. Traceability

Requirements documents must preserve relationships
to their originating evidence or approved decisions.

Design and implementation documentation must reference
applicable SRS requirements.

Verification artifacts must identify the requirements
and builds they examine.

Use the Requirement Traceability Matrix to maintain
cross-document mappings.

Do not invent downstream references for artifacts
that have not been created.

## 11. Diagrams

Use diagrams when they clarify system structure,
behavior, data, or deployment.

Each controlled diagram must identify:

- Purpose.
- Relevant requirements.
- Primary elements.
- Applicable assumptions.
- Source or editable representation.

Select the diagram type according to the information
being modeled.

Diagrams must not contradict accompanying specifications.

UML, ERD, and architecture diagrams must use
consistent identifiers and terminology.

Do not include decorative diagrams without
an engineering purpose.

## 12. Tables and Structured Records

Use tables for information that benefits from
consistent comparison or structured review.

Tables must have meaningful column headings.

Do not use tables to conceal missing information.

For structured records:

- Use consistent field names.
- Preserve identifier formats.
- State unknown values explicitly.
- Avoid unsupported default values.
- Distinguish examples from project data.

Machine-readable examples must use valid syntax
for the declared format.

## 13. Markdown Conventions

Framework documentation uses Markdown.

Requirements:

- One primary H1 heading per document.
- Descriptive hierarchical headings.
- Relative links for local repository files.
- Fenced code blocks with language identifiers.
- Consistent list formatting.
- No unresolved merge-conflict markers.
- No unnecessary trailing whitespace.

For `SKILL.md`, YAML frontmatter must begin
at the first character of the file.

Do not place blank lines or Markdown code fences
before the frontmatter delimiter.

Skill metadata must comply with the implemented
framework validator.

## 14. Source Code and Commands

Include code or commands only when they serve
a defined engineering purpose.

Commands must identify relevant execution context,
prerequisites, and side effects when consequential.

Do not represent illustrative code as an
implemented or tested component.

Avoid examples containing real credentials,
private tokens, or sensitive data.

When supplying replacement file contents, ensure
the output is complete for the stated file scope.

## 15. Version Control

Controlled document revisions must preserve
an identifiable change history.

Record significant changes to:

- Requirements.
- Scope.
- Approval decisions.
- Interfaces.
- Architecture.
- Acceptance criteria.
- Verification obligations.

Do not silently overwrite approved baselines.

Changes to approved documents require
the applicable change-control procedure.

## 16. Review Criteria

A document is ready for review when:

- Its scope is identifiable.
- Required sections are populated.
- Statements are internally consistent.
- Material claims have valid sources.
- Referenced artifacts are identifiable.
- Requirement IDs are consistent.
- Assumptions and open issues are visible.
- Unsupported conclusions have been removed.
- Applicable structural checks have passed.

Review readiness does not establish approval.

## 17. Validation

Run available framework validation tools
against modified documentation.

Current structural validation includes:

- Skill metadata checks.
- Repository structure checks.
- Local link checks.
- Basic Markdown structure checks.

Structural validation cannot determine whether
business requirements are correct or complete.

Semantic review remains the responsibility of
the assigned engineering role.

Do not report unimplemented validation checks
as completed.

## 18. Documentation Handoff

A document handoff must include:

- Artifact identifier and version.
- Source baseline.
- Current lifecycle state.
- Verification result.
- Approval state.
- Outstanding issues.
- Required receiving role or activity.

The receiving role must confirm that mandatory
prerequisites are satisfied before using the
document as an approved baseline.

## 19. Governing References

- [Agent Operating Contract](../AGENTS.md)
- [Framework Specification](../FRAMEWORK.md)
- [Governance Protocol](../core/governance.md)
- [Workflow Protocol](../core/workflow.md)
- [Verification Protocol](../core/verification.md)
- [Global Rules](global-rules.md)
