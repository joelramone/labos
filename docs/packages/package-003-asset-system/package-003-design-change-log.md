# Package 003 — Design Change Log

## v1.1 — 2026-08-06 — Architectural review corrections

| Change ID | File/section | Change | Reason | Requirements trace |
|---|---|---|---|---|
| DC-001 | Design metadata | Version advanced from v1.0 to v1.1; status set to `DESIGN_REFINEMENT_REQUIRED` | Review found blocking Requirements contradictions | R19 |
| DC-002 | Data Models; 2.1 | Applied canonical 80-character name limit and documented conflict with R16.1 | Package 000 is authoritative under ADR-0001 | R1.2, R16.1, R19.1 |
| DC-003 | Data Models; 2.1 | Added `content_state` as separate intake metadata | Preserve Package 000 content maturity independently from Package 003 lifecycle | R1.2, R3.1, R13.1, R14.1, R16.6 |
| DC-004 | 3.1; 3.2 | Replaced reactivation state transitions with creation of a new CANDIDATE record | Closed forward-only transition set | R3.11, R3.12, R12.6 |
| DC-005 | 5.1 | Removed `VALIDATED → REJECTED` edge | Transition is not authorized by R3.11 | R3.11 |
| DC-006 | 9.2 | Fast path now verifies mandatory dimensions in the same lightweight act; unresolved exception recorded | Prevent silent waiver of R4 while retaining SOLO proportionality | R3.10, R4.1, R4.4, R5.5 |
| DC-007 | 10.2 | Restored seven-day consumer defect notification deadline | Design had weakened an explicit acceptance criterion | R9.5 |
| DC-008 | 21.2; 22.1; 22.4 | Corrected Tier 1 counts, validation limits and self-review claims | Restore internal consistency and distinguish traceability from conformance | R1, R16, R19 |
| DC-009 | New design review | Added complete architectural findings, coverage, conflicts, pending decisions and verdict | Required review evidence | R19 |

No Requirements, ADRs, Architecture Baseline, previous packages, Tasks or implementation files were modified.

## v1.2 — 2026-08-12 — Requirements v1.3 alignment

| Change ID | File/section | Change | Reason | Requirements trace |
|---|---|---|---|---|
| DC-010 | Design metadata/status | Advanced v1.1 → v1.2; Requirements base v1.3; approval remains pending | Reflect reconciled normative baseline without self-approval | R19 |
| DC-011 | Data Models; 2.1; 2.2 | Tier 1 exactly 8 owner fields; Tier 2 exactly 8 additional fields; asset_id system-assigned/refined | Resolve C1/C2 and cardinality | R1, R16 |
| DC-012 | Data Models; 2.1; 2.2 | Kept `content_state` and `estado_lifecycle` independent | Requirements v1.3 C2 | R3, R13, R14, R16 |
| DC-013 | 9.1–9.3 | Added `consumption_state`; separated authorized scope from effective consumption | Requirements v1.3 C4 | R5, R9, R15, R16 |
| DC-014 | 9.2 | Fast path verifies all five R4 dimensions in one lightweight act | Requirements v1.3 C3 | R4, R5 |
| DC-015 | 20; 21; 22; Design Status | Corrected templates, matrices, counts, coverage and status | Establish 20/20 coverage and zero unresolved conflicts | R1–R20 |
| DC-016 | Design review | Added reconciliation verification and sequential Founder approval gate | Preserve historical review while recording technical closure | R19 |

No Tasks or implementation were created. Design v1.2 remains pending Founder review after Requirements v1.3 approval.

## v1.2 final clarification set — 2026-08-12

| Change ID | Section(s) | Change | Reason | Requirements impact |
|---|---|---|---|---|
| DC-017 | Metadata; Introduction; Design Status | Updated Requirements baseline to v1.3 APPROVED and Design status to ready for Founder approval | Record sequential approval gate without self-approving Design | None |
| DC-018 | 2.2 | Corrected stale note: `fecha_de_creación` remains a Tier 2 field while preserving the initial intake date | Resolve D1 and align exactly with R16.2 | None |
| DC-019 | 3.1; 3.4; 5.1; 19; diagrams | Replaced Lab-Private-only Fast Path language with effective Level 1 eligibility | Resolve D2; include authorized LabOS-Shared Assets without active consumers | None |
| DC-020 | 3.5 | Expanded the orthogonal-dimension inventory without adding lifecycle states | Make the structural audit explicit | None |
| DC-021 | Introduction; Testing Strategy | Recorded Correctness Properties warning as `ACCEPTED_NON_BLOCKING` | Documentary governance has verifiable criteria but no executable PBT target | None |
| DC-022 | Design review | Added final review against approved Requirements v1.3 with verdict `DESIGN_APPROVE_WITH_NON_BLOCKING_NOTES` | Provide Founder decision evidence | None |

**Version decision:** Design remains v1.2. DC-017–DC-022 are compatible clarifications that remove internal contradictions and do not alter Requirements, lifecycle semantics, architectural invariants or scope. Founder Design approval remains pending. Tasks and implementation remain `NOT_AUTHORIZED`.

| DC-023 | Design metadata/status | Recorded explicit Founder approval and authorized Tasks generation only | Founder decision 2026-08-13 | None |

Design remains v1.2. Status is `DESIGN_APPROVED`; Tasks generation is authorized, while Tasks execution and Implementation remain `NOT_AUTHORIZED`.

## v1.2.1 — 2026-08-21 — Post-approval Tasks Review patch

| Change ID | Source | Affected section | Classification | Old behavior | Corrected behavior | Requirements impact | Architecture impact | Tasks impact | Approval impact |
|---|---|---|---|---|---|---|---|---|---|
| DC-024 | Package 003 Tasks Review F-001 | Design 20.1; metadata; Design Status | CLARIFIED / CORRECTED — PATCH | Candidate template listed mandatory preliminary qualification dimensions and evaluator notes in addition to Tier 1 intake | Candidate intake requires exactly the 8 Tier 1 owner fields; future metadata, reuse signal and evaluation links may appear only as OPTIONAL/NOT_YET_REQUIRED; qualification and Tier 2 completion belong to evaluation/promotion templates; no duplicate mandatory entry | NONE — restores exact R16.1/R16.2 behavior | NONE — no lifecycle, boundary, metadata-count or architectural decision changes | Resolves T003-026 blocker; permits final revalidation of the existing 32 Tasks | NONE — PATCH under architecture-change-control-v1.0; Founder reapproval not required |

Version mapping: Package Design versions use the compatible three-component PATCH convention defined by `architecture-change-control-v1.0.md`. v1.2 remains historically approved; v1.2.1 is the current effective Design. Tasks execution and Implementation remain `NOT_AUTHORIZED`.
