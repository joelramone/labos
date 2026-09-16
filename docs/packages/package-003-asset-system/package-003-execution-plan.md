# Package 003 — Execution Plan

## Authorization state

Founder decisions FD-P003-TASKS-001 and FD-P003-W2-001 through FD-P003-W6-001 authorized controlled documentary execution through Wave 6. FD-P003-CLOSURE-001 subsequently closed Package 003; no downstream Package is authorized.

| Field | Value |
|---|---|
| Final Task count | 32 |
| Execution waves | 7 (W0–W6) |
| Parallelizable by Task flag | 25 |
| Current blocking decision | NONE — former Design 20.1 blocker resolved by v1.2.1 PATCH DC-024 |
| Tasks status | `TASKS_APPROVED` |
| Authorization status | `WAVE_6_AUTHORIZED_AND_COMPLETE` |
| Tasks execution | `WAVES_0_1_2_3_4_5_6_COMPLETE` |
| Package closure | `CLOSED` — FD-P003-CLOSURE-001 |
| Implementation | Documentary Package implementation `COMPLETE`; no software implementation authorized |

Relative effort uses S = short bounded document/template pass and M = substantive normative/review pass. It is comparative, not a time commitment.

## DAG and waves

`W0 → W1 → W2 → W3 → W4 → W5 → W6`

Within a wave, arrows separate dependency layers; Tasks in braces may run in parallel after their listed prerequisites pass.

| Wave | Dependency layers | Relative effort | Parallel Tasks | Exit gate |
|---|---|---:|---:|---|
| W0 — Preparation | T003-002 | M | 0 | Requirements v1.3, effective Design v1.2.1, ADRs and Baseline confirmed; W0 authorization recorded |
| W1 — Foundations | {T003-003, T003-005} → T003-004 | 2S + M | 3 flagged YES, max useful concurrency 2 | Canonical terminology, boundaries and exactly seven types pass cross-reference audit |
| W2 — Core models | {T003-006, 007, 010, 011, 012, 016} → {T003-009, 017, 018} | 9M | 9 | Lifecycle/qualification/ownership/provenance/versioning/value/registry consistency; Tier counts 8+8 |
| W3 — Governance, sharing and handoffs | T003-014 → {T003-019, 020, 021} → {T003-008, 022} → T003-023 | 7M | 7 flagged YES except T003-008; concurrency follows layers | Approval, risk, sharing, promotion, KO/Product boundary and retirement scenarios pass; no Package 004 behavior |
| W4 — Integration validation | {T003-024, T003-025} | 2M | 1 flagged YES; two Tasks independent after W3 | Seven diagrams match sources; five CSC candidates assessed read-only with allowed outcomes and safety restrictions |
| W5 — Templates | {T003-026, 027, 028, 029, 030} | 5S | 5 | Field counts, Tier ownership, no duplicate mandatory entry and scenario/timed dry-runs pass |
| W6 — Final integration and audit | {T003-031, 032} → T003-033 → T003-034 → T003-035 | 4M + S | 2 | 20/20, 22/22, architecture consistency, remediation register and `READY_FOR_FOUNDER_CLOSURE_REVIEW`; Founder decides closure explicitly |

## Dependency rules

- A Task may start only when every prerequisite in `tasks.md` is complete and its wave entry gate has passed.
- A `Can run in parallel: YES` flag grants concurrency only with another ready Task; it never overrides dependencies.
- T003-008 cannot start before lifecycle, qualification, registry and governance exist.
- T003-024 and T003-025 cannot start before all applicable normative sources exist.
- T003-026 uses effective Design v1.2.1: exactly eight required Tier 1 fields; optional/future displays never gate intake.
- T003-035 is always last and cannot mark the Package `CLOSED`.

## Gate ownership

| Gate | Decision/evidence owner | Required evidence |
|---|---|---|
| W0–W4 technical gates | Task executor, reviewed by Founder | Task validation records and no unresolved blocking defect from the wave |
| W5 entry | Task executor, reviewed by Founder | Effective Design v1.2.1 recorded; no open Design conflict; Tasks execution separately authorized |
| W5 template gate | Founder | Candidate intake dry-run 3–5 minutes; evaluation/promotion/review/deprecation separation |
| W6 technical closure gate | Independent package reviewer | Summary, final traceability, architecture audit and remediation register |
| Package closure | Founder only | Explicit closure decision after reviewing all unresolved blocking items |

## Failure handling

1. Stop the affected Task; do not mark its output complete.
2. Record the failed acceptance criterion, evidence, affected Requirement/Design section and severity.
3. Add or update the unresolved remediation register when W6 is available; before W6, keep the finding in the Task validation evidence for later consolidation.
4. Invalidate only downstream Tasks whose inputs or semantics are affected; independent Tasks may continue if their wave gate remains valid.
5. If resolution changes approved Requirements or Design, label it `REQUIREMENTS_CHANGE_REQUIRED` or `DESIGN_CHANGE_REQUIRED`, stop affected downstream work and request Founder authority. Never patch upstream documents silently.
6. Re-run the failed validation and every affected downstream cross-reference check after remediation.

## Documentation rollback

Documentation rollback means reverting only the changes produced by the failed Task to the last reviewed version, while preserving the finding record. Use the repository diff to isolate the Task-owned files; do not reset the workspace, discard unrelated user changes or modify completed upstream packages. If a Task touched a shared document, revert only its bounded section or restore the prior reviewed file content after checking for concurrent edits. A failed Reference Lab assessment rolls back only its assessment document; Crypto remains untouched.

## Founder gates

1. Before any execution: explicit authorization of the reviewed Task plan. FD-P003-TASKS-001 authorized Waves 0–1 only; W2 requires a new explicit authorization.
2. At any future Requirements/Design/ADR conflict: approve the relevant change path before affected execution resumes.
3. After W6: review closure evidence and unresolved remediation register.
4. Only the Founder may set Package status to `CLOSED`.

No Task is executed by this plan.
