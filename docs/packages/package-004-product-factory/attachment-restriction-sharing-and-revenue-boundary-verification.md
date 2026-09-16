# Attachment, Restriction, Sharing and Revenue Boundary Verification
> **CONTROLLED_VERIFICATION — SYNTHETIC EVIDENCE ONLY — NOT_A_GOVERNED_INSTANCE**

Task: `T004-030`. Sources: composition/eligibility/dependency/packaging/risk/sharing/handoff artifacts, P003 read-only boundary, F03/F04/F07–F10. Method: route each synthetic request through eligibility/restriction/sharing/handoff decision tables and compare source state before/after.

| Control | Fixture | Expected | Observed controlled result | Result | Evidence | Gap | Blocker |
|---|---|---|---|---|---|---|---|
| E01 not canonical | F03 | VALIDATED/NOT_CANONICAL → REFERENCE_ONLY/NOT_ATTACHABLE | Exact mapping returned; attachment refused | PASS | F03, eligibility contract | None | No |
| E02 canonical complete | F04 | Synthetic CANONICAL + complete handoff → ELIGIBLE_FOR_GOVERNED_ATTACHMENT | Exact mapping returned; Product fit separate; no attachment | PASS | F04, eligibility contract | None | No |
| E03 pre-canonical variant | synthetic matrix row | CANDIDATE/UNDER_REVIEW → NOT_COMPOSABLE | Both states returned NOT_COMPOSABLE | PASS | eligibility contract | None | No |
| E04 incomplete-handoff variant | synthetic matrix row | CANONICAL + incomplete handoff → NOT_ELIGIBLE | Missing handoff evidence named; eligibility denied | PASS | eligibility contract | Expected gap | No |
| E05 real Asset refusal | read-only ASSET-1/2/3 references | Remain VALIDATED/NOT_CANONICAL/NOT_ATTACHABLE | Before/after documentary references identical; no writes | PASS | P003 boundary records, W5/W6 records | None | No |
| P01 P003 operations | F03/F04 | READ/REFERENCE/CONSUME only | WRITE/OVERRIDE/RECOMPUTE/PROMOTE/DOWNGRADE/ALTER_* requests refused | PASS | eligibility contract | None | No |
| X01 restriction intersection | F09 | Most restrictive licensing/usage/sharing/distribution/dependency/risk scope | Public request reduced to internal-use-only; conflict visible | PASS | F09, sharing check | None | No |
| S01 approval/sharing | F07 | APPROVED does not grant sharing/activation | No sharing or activation record inferred | PASS | F07 | None | No |
| S02 active/publication | F08 | ACTIVE does not imply PUBLIC/commercial/Revenue | Private audience retained; Public request denied | PASS | F08 | None | No |
| V01 P005 dossier | F10 | Documentary readiness only | Result remained READY_FOR_GOVERNED_HANDOFF_DECISION; P005 DORMANT | PASS | F10, handoff dossier | None | No |
| V02 Revenue exclusions | F10 | No pricing/sales/payment/transaction/accounting/revenue/optimization | All eight operation checks absent/prohibited | PASS | handoff exclusion matrix | None | No |

Summary: `PASS 11 / FAIL 0 / GAP 0 / BLOCKERS 0`. The incomplete-handoff gap is intentional scenario input. Real attachments, Asset mutations, restriction changes, sharing/publication and Revenue operations: `0`. Package 005 activation: `NO`.

Traceability: T004-030; R04–R06, R12, R17–R18, R21–R22 and corresponding AC; C03, C04, C08, C11, C14, C16, C18, C19; P004-D005–D006, D008, D012, D015.
