# Package 004 — Task Dependency Graph

## Dependency DAG

```mermaid
flowchart TD
  T001[T004-001 Baselines] --> W1{W1 Core}
  W1 --> T002[T004-002 Candidate]
  W1 --> T003[T004-003 Product]
  W1 --> T004[T004-004 Governance record]
  T003 --> T005[T004-005 Ownership / SOT]
  T003 --> T006[T004-006 Composition]
  T004 --> T005
  T006 --> T007[T004-007 P003 eligibility]
  T006 --> T008[T004-008 Dependencies]
  T007 --> T009[T004-009 Packaging]
  T008 --> T009
  T002 --> T010[T004-010 Provenance]
  T005 --> T010
  T006 --> T011[T004-011 Quality]
  T004 --> T012[T004-012 Risk]
  T006 --> T012
  T003 --> T013[T004-013 Value]
  T003 --> T014[T004-014 Demand]
  T009 --> T015[T004-015 Readiness]
  T010 --> T015
  T011 --> T015
  T012 --> T015
  T013 --> T015
  T014 --> T015
  T015 --> T016[T004-016 Lifecycle]
  T002 --> T017[T004-017 REJECTED]
  T016 --> T017
  T016 --> T018[T004-018 Approval / activation]
  T006 --> T019[T004-019 Version]
  T008 --> T019
  T017 --> T020[T004-020 Registry]
  T018 --> T020
  T019 --> T020
  T020 --> T021[T004-021 Sharing]
  T020 --> T022[T004-022 Review]
  T022 --> T023[T004-023 Retirement]
  T021 --> T024[T004-024 P005 handoff]
  T004 --> T025[T004-025 AI matrix]
  T011 --> T026[T004-026 Domain extension]
  T012 --> T026
  T022 --> T026
  T024 --> T027[T004-027 Manual procedure]
  T023 --> T027
  T025 --> T027
  T026 --> T027
  T027 --> T028[T004-028 Fixtures]
  T028 --> T029[T004-029 Lifecycle verification]
  T028 --> T030[T004-030 Boundary verification]
  T028 --> T031[T004-031 Registry/manual verification]
  T029 --> T032[T004-032 Final audit]
  T030 --> T032
  T031 --> T032
```

The diagram shows material sequencing; `tasks.md` is authoritative for complete prerequisite lists.

## DAG audit

| Control | Result |
|---|---|
| Tasks represented | `32/32` |
| Dependency cycles | `0` |
| Orphan Tasks | `0` |
| Tasks with undeclared upstream semantic dependency | `0` |
| Wave gate bypasses | `0` |

Critical blocking sequence:

`T004-001 → T004-003/004 → T004-006 → T004-008/009/010/011/012/013/014 → T004-015 → T004-016/018 → T004-020 → T004-021/022/023/024/025/026 → T004-027 → T004-028 → T004-029/030/031 → T004-032`.

Parallel branches exist inside W1–W6, but a Task is ready only when every dependency in its Task contract is COMPLETE and its wave is explicitly authorized. No wave is authorized here.

