# F09 — Licensing Restriction Propagation
> **CONTROLLED_TEST_FIXTURE — SYNTHETIC — NOT_A_GOVERNED_INSTANCE**

Synthetic ID: `SYN-P004-F09-RESTRICTION`; Task: T004-028; verification: T004-030.

| Control | Synthetic exercise/result |
|---|---|
| Upstream constraint | Internal-use-only licence; no external distribution |
| Requested downstream scope | Public distribution |
| Intersection | Licensing/usage/sharing/distribution restricted to internal use; dependency/risk constraints retained |
| Expected/observed | Public scope denied; conflict visible; fail closed / matched |
| Result/gap/blocker | `PASS / NONE / NO` |

Evidence: composition, packaging, risk and sharing artifacts. No restriction was altered or real source accessed/mutated.
