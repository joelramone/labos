# F02 — Rejected Candidate
> **CONTROLLED_TEST_FIXTURE — SYNTHETIC — NOT_A_GOVERNED_INSTANCE**

Synthetic ID: `SYN-P004-F02-CANDIDATE`; Task: T004-028; verification: T004-029.

| Control | Synthetic exercise/result |
|---|---|
| Precondition | Candidate at `UNDER_REVIEW`; synthetic evidence and human-authority placeholders present |
| Request | Record terminal `REJECTED` review outcome |
| Expected/observed | State history remains `UNDER_REVIEW`; REJECTED stored as outcome; no eighth state or re-entry / matched |
| Invalid retry | Silent re-entry requested; guard returned failure and state `UNCHANGED` |
| Result/gap/blocker | `PASS / NONE / NO` |

Evidence: `terminal-candidate-review-outcome-template.md`, lifecycle matrix, common governance envelope. No real decision ID, transition, Candidate or history was created. Isolation/cleanup: fixture directory only; excluded from Registry/current truth.
