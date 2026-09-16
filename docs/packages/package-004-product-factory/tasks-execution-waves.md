# Package 004 — Proposed Execution Waves

## Authority

These waves organize the Task DAG. W0–W7 are `COMPLETE` under their recorded authorizations and execution evidence. W7 evidence is in `wave-7-execution-record.md`; Package closure remains separate.

| Wave | Current authorization |
|---|---|
| W0 | `COMPLETE` |
| W1 | `COMPLETE` |
| W2 | `COMPLETE` |
| W3 | `COMPLETE` |
| W4 | `COMPLETE` |
| W5 | `COMPLETE` |
| W6 | `COMPLETE` |
| W7 | `COMPLETE` |

| Wave | Purpose | Tasks | Internal ordering | Exit evidence |
|---|---|---|---|---|
| W0 | Preconditions/integrity | T004-001 | Sequential | Approved baselines, boundaries and initial integrity snapshot |
| W1 | Core Product/Candidate/governance | T004-002–005 | T002/T003/T004 parallel after W0; T005 after T003/T004 | Identity, Candidate, common decision, owner/SOT contracts consistent |
| W2 | Composition/upstream/delivery inputs | T004-006–010 | T006; T007/T008; T009; T010 when its sources complete | P003 read-only interface, dependencies, packaging and provenance consistent |
| W3 | Evidence/readiness | T004-011–015 | T011–T014 parallel as ready; T015 last | Quality/risk/value/demand distinct; readiness matrix complete |
| W4 | Lifecycle/version/Registry | T004-016–020 | T016/T019; T017/T018; T020 last | Seven states, REJECTED outcome, approvals/version/history integrated |
| W5 | Sharing/review/retirement/boundaries/manual | T004-021–027 | T021/T022/T025; T023/T026; T024; T027 last | Full manual procedure and P005 boundary complete |
| W6 | Controlled fixtures/verification | T004-028–031 | T028; T029/T030/T031 parallel | Planned controlled evidence covers governance, boundaries and operability |
| W7 | Final audit/closure preparation | T004-032 | Sequential | Reconciled package evidence; at most READY_FOR_FOUNDER_CLOSURE_REVIEW |

## Wave-control rules

1. Founder authorizes each wave explicitly; authorization is never inherited from plan approval.
2. A failed Task becomes BLOCKED, records evidence and blocks only affected dependents.
3. Independent Tasks in an authorized wave may continue only when their sources remain valid.
4. Any Requirements/Design/frozen-architecture change stops the affected branch for change control.
5. W7 cannot mark Package 004 CLOSED; closure remains a separate Founder act.

W0/T004-001 through W7/T004-032 are COMPLETE. Package 004 is `CLOSED` under `FD-P004-CLOSURE-001`; implementation and downstream Packages remain unauthorized/dormant.
