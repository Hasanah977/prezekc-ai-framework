# System Design Specification — Reporting Access (Simulation)

## Document Control

| Field | Value |
|---|---|
| Document ID | SDS |
| Version | 0.1 |
| Status | DRAFT — SIMULATION |
| Source SRS | 1.0 |
| Approval | NOT APPROVED FOR IMPLEMENTATION |

## Architecture

A reporting UI delegates requests to a reporting service. The service checks access policy and queries a reporting repository. This is a proposed logical design, not an implemented system.

## Component Register

| ID | Responsibility | SRS Source |
|---|---|---|
| CMP-001 | Period selector UI | SRS-FR-001.1 |
| CMP-002 | Reporting service | SRS-FR-001.2; SRS-FR-001.3 |
| CMP-003 | Record repository interface | SRS-FR-001.2 |

## Design Elements

| ID | Definition | SRS Source |
|---|---|---|
| DES-001 | Period selection flow from reporting UI to service | SRS-FR-001.1 |
| DES-002 | Reporting service queries selected period through repository | SRS-FR-001.2 |
| DES-003 | Authorization check before repository access | SRS-FR-001.3 |

## Data Model

- DATA-001: ReportingPeriod, identifier and allowed period range (proposed).
- DATA-002: ConsolidatedRecord, belongs to a ReportingPeriod (proposed).
- No physical schema is approved in this simulation.

## Interface Contract

- API-001: Period-scoped retrieval request; exact method, URI, payload, and error codes require specification before implementation.

## Open Issues

- Define actual role/permission policy and denied-request behavior.
- Define data retention, record fields, and update ownership.
- Authorize design and establish test cases before implementation.
