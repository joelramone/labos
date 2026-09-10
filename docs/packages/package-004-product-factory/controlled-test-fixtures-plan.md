# Package 004 — Controlled Test Fixtures Plan

All fixtures are future documentary artifacts classified `CONTROLLED_TEST_FIXTURE`. They are non-authoritative, synthetic and prohibited from creating real Candidates, Products, Assets, attachments, approvals, demand evidence or commercialization claims.

| Fixture | Scenario | Expected governed result | Primary verification Task |
|---|---|---|---|
| F01 | Complete simple Candidate proposal | Recordable only as CANDIDATE; no approval/attachment effect | T004-028/031 |
| F02 | Candidate receives terminal rejection | State history remains UNDER_REVIEW with REJECTED outcome; no eighth state/re-entry | T004-028/029 |
| F03 | VALIDATED / NOT_CANONICAL Asset reference | `REFERENCE_ONLY / NOT_ATTACHABLE` | T004-028/030 |
| F04 | Synthetic CANONICAL Asset with complete P003 handoff | `ELIGIBLE_FOR_GOVERNED_ATTACHMENT`; Product fit still separately decided | T004-028/030 |
| F05 | Readiness mandatory control fails | `NOT_READY`; lifecycle unchanged | T004-028/029 |
| F06 | Readiness evidence passes | Readiness result can support human READY transition; Product remains unapproved | T004-028/029 |
| F07 | Human-approved but not activated Product | `APPROVED`, not ACTIVE/Public/commercial | T004-028/029 |
| F08 | Active Product with private sharing decision | ACTIVE but not PUBLIC | T004-028/030 |
| F09 | Upstream licence restricts distribution | Product/package/sharing effective scope preserves the restriction | T004-028/030 |
| F10 | Complete Product→Revenue dossier | Handoff record only; no price/payment/transaction/revenue/P005 activation | T004-028/030 |

Additional variants required by T004-030 cover P003 CANDIDATE/UNDER_REVIEW → NOT_COMPOSABLE and CANONICAL with incomplete handoff → NOT_ELIGIBLE. ASSET-1/2/3 may be cited read-only only for their existing `VALIDATED / NOT_CANONICAL / NOT_ATTACHABLE` outcome; no fixture impersonates or modifies them.

Fixture execution is `NOT_AUTHORIZED`.

