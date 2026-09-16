# Registry, Provenance, Manual Operation and Domain Neutrality Verification
> **CONTROLLED_VERIFICATION — SYNTHETIC EVIDENCE ONLY — NOT_A_GOVERNED_INSTANCE**

Task: `T004-031`. Sources: Candidate/Product/ownership/provenance/value/demand/version/Registry/review/AI/domain/manual artifacts and F01. Method: populate only transient synthetic comparison rows, resolve each requested answer through references, inject conflicts/missing links, and walk the manual procedure without creating a Registry instance.

| Control | Fixture/scenario | Expected | Observed controlled result | Result | Evidence | Gap | Blocker |
|---|---|---|---|---|---|---|---|
| G01 Candidate representation | F01 | Candidate current view answerable without Product/approval/attachment | Required fields resolved from F01; no Registry insertion | PASS | F01, Registry contract | None | No |
| G02 Registry boundaries | synthetic query | Product Registry ≠ Asset Registry/evidence store/Revenue Engine | Each query routed to distinct authoritative reference; no copied authority | PASS | Registry contract | None | No |
| G03 SOT conflict | injected conflict | Product SOT ≠ Asset SOT; conflict blocks update | Duplicate/ambiguous SOT row rejected and named | PASS | ownership/SOT, Registry contract | Expected conflict | No |
| G04 truth/history | injected supersession | Current Truth ≠ immutable Historical Truth | Current pointer changed only in simulation; prior row retained/link required | PASS | Registry/review contracts | None | No |
| P01 complete lineage | F01 synthetic links | Source authority, exact versions and known links visible | Query followed Candidate/source/version references end-to-end | PASS | provenance template, F01 | None | No |
| P02 missing lineage | injected missing link | Missing/unknown remains explicit | Result `MISSING — source link`; completeness not fabricated | PASS | provenance template | Expected gap | No |
| V01 version impact | synthetic changed dependency | Review required; no automatic version/readiness/lifecycle change | Impact row returned REVIEW_REQUIRED only | PASS | version and review artifacts | None | No |
| M01 manual tabletop | F01 | Documentary path works without platform | 22-step procedure resolved roles/inputs/outputs/guards; stopped before real decision creation | PASS | manual procedure | None | No |
| M02 infrastructure absence | tabletop | No database/API/UI/persistence/workflow/agents required | Every lookup/decision path remained file/reference based | PASS | manual procedure, Registry contract | None | No |
| D01 form neutrality | neutral comparison | No software/SaaS/trading/AI/digital/physical/cardinality requirement | Core fields accepted neutral offering and one/many-input descriptions without semantic change | PASS | domain profile, Product template | None | No |
| D02 domain trigger | synthetic first-domain flag | First real cross-domain Candidate requires DOMAIN_NEUTRALITY_REVIEW | Trigger returned REVIEW_REQUIRED; no Candidate created | PASS | domain profile | None | No |
| Q01 dimension separation | synthetic cross-check | Quality/Risk/Readiness/Value/Demand and Asset/Product dimensions distinct | References remained separate; no field advanced another; Value enum stayed HYPOTHESIZED/EVIDENCED/DEMONSTRATED | PASS | T004-011–015 artifacts | None | No |
| F01 freshness | stale synthetic source | Review/freshness does not transition lifecycle | REVIEW_REQUIRED returned; state unchanged | PASS | review/freshness artifact | Expected stale source | No |

Summary: `PASS 13 / FAIL 0 / GAP 0 / BLOCKERS 0`. Injected conflicts/missing/stale inputs are expected negative cases, not unresolved verification gaps. Real Registry entries, Products/Candidates, validation activity and infrastructure: `0`.

Traceability: T004-031; R01–R02, R08–R10, R13–R14, R19, R23, R25 and corresponding AC; C01, C02, C09, C10, C12, C13, C15, C20; P004-D001–D002, D006, D010–D014.
