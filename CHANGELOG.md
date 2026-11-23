# Changelog

All notable changes to PREZEKC AI Framework are documented in this file.

The framework follows [Semantic Versioning](https://semver.org/) for its published releases.

## [0.1.0] - 2026-11-23

**Release status:** Pending final CI verification and release authorization.

### Added

**Governance and roles**

- Agent operating contract and engineering governance protocols.
- Six engineering role specifications.

**Engineering skills**

- System analysis.
- Comparative study.
- Requirement analysis.
- PRD generation.
- PRD-to-SRS transformation.
- System design.
- Web and mobile development.
- Testing.
- Deployment.

**Templates and workflows**

- Document templates for analysis, requirements, traceability, and system design.
- Full-lifecycle, web, and mobile delivery workflows.

**Validation and tooling**

- Structural repository and skill validation utilities.
- Requirements traceability validator.
- Markdown-to-JSON requirement extraction.
- Automated framework validation through GitHub Actions.

**Tests**

- Unit tests for structural validation, requirements validation, and document extraction.
- Simulated engineering acceptance test covering requirements and design traceability.

### Verification

The following local checks were reported successful:

| Check | Result |
|---|---|
| Framework structural validation | 0 errors, 0 warnings |
| Requirements validation | 0 errors, 0 warnings |
| Automated unit tests | 31 passed |
| Acceptance example extraction and validation | Passed |
| Git whitespace validation | Passed |

CI confirmation for the final release commit must be recorded before publication.

### Limitations

**Runtime**

- The framework does not provide an autonomous agent runtime.
- Engineering procedures require a compatible AI assistant or human operator.

**Validation**

- Markdown extraction requires the supported document structure.
- Automated validation does not replace semantic requirements review.
- Approval records are not independently authenticated.

**Delivery**

- Mobile build and production deployment capabilities depend on the target project's environment and toolchain.
- The acceptance example uses simulated project evidence and approval records.