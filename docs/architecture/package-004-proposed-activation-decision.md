# Package 004 — Proposed Activation Decision

## Status

`PROPOSED_ONLY`

This document has no activation effect and does not authorize Requirements, Design, Tasks or implementation.

| Field | Proposed value |
|---|---|
| Package | Package 004 — Product Factory |
| Current state | `DORMANT / CONDITIONAL / NOT_AUTHORIZED` |
| Trigger | `AT_LEAST_3_ASSETS_IN_VALIDATED` |
| Trigger evidence | ASSET-1, ASSET-2 and ASSET-3 have authoritative VALIDATED decisions; 3/3 |
| Trigger status | `SATISFIED` |
| Readiness verdict | `PACKAGE_004_READY_WITH_CONDITIONS` |
| Proposed next state | `AUTHORIZED_FOR_REQUIREMENTS` |
| Architecture impact | `EXTENDS_BASELINE`; no baseline semantic modification |
| Founder decision required | YES |
| First action after approval | `PACKAGE_004_REQUIREMENTS` |

## Upstream dependencies

Packages 000, 001, 001A, 002, 002A and 003 are complete/closed and supply the Foundation, research/evidence, Lab integration, Knowledge, architecture/change-control and Asset/handoff contracts needed to begin Product Factory specification. They remain closed and are consumed by reference.

## Conditions and restrictions

1. Authorization must be limited to Requirements; Design, Tasks, implementation and full Package activation remain separate gates.
2. `VALIDATED` Assets satisfy the roadmap activation trigger, but none of ASSET-1/2/3 is CANONICAL or eligible for immediate Product attachment under Package 003.
3. No Product Candidate, Product, attachment, commercialization or Public sharing is created by the activation decision.
4. Package 003 retains Asset lifecycle, ownership, source, version and handoff authority.
5. Package 005 retains pricing, revenue execution, transactions and revenue lifecycle; it remains dormant.
6. Package 006, Package 007, persistence, Historical Truth implementation, RAG, MCP and agents remain dormant/not authorized and are not dependencies.
7. Product Factory must support manual-first, human-governed operation.
8. ASSET-1/2/3 restrictions, projected value/reuse and provenance/licensing limits must flow into any future Product evaluation.
9. Human Performance remains paused.
10. Any conflict with frozen upstream semantics follows architecture change control; this decision itself requires no ADR.

## Risks

Primary non-blocking risks are scope creep, premature Asset composition, one-Lab evidence concentration, conflation of Product validation with commercialization, and accidental infrastructure/AI dependency. Mitigations are phase gates, explicit boundaries, attachment eligibility checks and human authority.

## Proposed Founder action

Exact next governance action: `PACKAGE_004_ACTIVATION_DECISION`.

If approved, that separate record should identify the Founder, date, Package, justification, baseline, conditions and state change to `AUTHORIZED_FOR_REQUIREMENTS`. Only then may `PACKAGE_004_REQUIREMENTS` begin. This proposal does not make that decision.
