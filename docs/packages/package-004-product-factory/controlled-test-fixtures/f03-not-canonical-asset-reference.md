# F03 — NOT_CANONICAL Asset Reference
> **CONTROLLED_TEST_FIXTURE — SYNTHETIC — NOT_A_GOVERNED_INSTANCE**

Synthetic ID: `SYN-P004-F03-ASSET-REF` (not ASSET-1/2/3); Task: T004-028; verification: T004-030.

| Input/control | Synthetic result |
|---|---|
| Asset state | `VALIDATED / NOT_CANONICAL` |
| P003 operation | `READ / REFERENCE / CONSUME DECISION` only |
| Expected/observed eligibility | `REFERENCE_ONLY / NOT_ATTACHABLE` / matched |
| Attempted attachment | Refused; no attachment or Asset/Product mutation |
| Result/gap/blocker | `PASS / NONE / NO` |

Evidence: `p003-attachment-eligibility-reference-contract.md`. Prohibited: WRITE, OVERRIDE, RECOMPUTE, PROMOTE, DOWNGRADE, ALTER_HANDOFF, ALTER_ASSET_AUTHORITY. Isolated synthetic reference; never an Asset/SOT/Registry entry.
