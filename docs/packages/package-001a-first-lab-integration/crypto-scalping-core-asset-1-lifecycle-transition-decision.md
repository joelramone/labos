# ASSET-1 — Lifecycle Transition Decision

## Authoritative decision record

| Field | Value |
|---|---|
| Decision ID | `FD-ASSET-1-VALIDATED-001` |
| Classification | `FOUNDER_DECISION` |
| Decisor | Fundador |
| Effective timestamp | `2026-09-02T11:58:23-03:00` |
| Asset ID | `ASSET-1` |
| Name | Framework de backtesting para estrategias de trading |
| Type | `Framework` |
| Owner | Joel Diaz / Lab Founder |
| Originating Lab | Crypto Scalping Core / `LABOS-REF-LAB-0001` |
| Initial lifecycle | `CANDIDATE` |
| Intermediate lifecycle | `UNDER_REVIEW` |
| Final lifecycle | `VALIDATED` |
| Founder decision | `APPROVE_ASSET_1_VALIDATED_TRANSITION` |
| Approval justification | Controlled deterministic evidence and independent review satisfy all ASSET-1 qualification, validation and elevated risk gates for the restricted software-framework scope. |
| CANONICAL | `NO / NOT_AUTHORIZED` |
| Package 004 | `NOT_AUTHORIZED` |

The justification is 10–280 characters and identifies the evidence-based reason. This record is the authoritative lifecycle act; the earlier proposed record remains historical `PROPOSED_ONLY` evidence.

## Pre-transition gate verification

| Gate | Required | Verified result |
|---|---|---|
| Candidate classification | PASS | PASS — coherent Framework Candidate |
| Tier 1 | 8/8 | 8/8 PASS |
| Qualification | 5/5 SATISFIED | 5/5 SATISFIED |
| VALIDATED criteria | 12/12 PASS | 12 PASS; 0 partial/fail/insufficient |
| Quality | PASS_WITH_RESTRICTIONS | PASS_WITH_RESTRICTIONS |
| Financial/trading risk | PASS_WITH_RESTRICTIONS | PASS_WITH_RESTRICTIONS |
| Controlled reproducibility | Documented evidence | `REPRODUCIBLE_WITH_DOCUMENTED_PREREQUISITES` |
| Blocking remediation | 0 | 0 |
| Founder decision | PRESENT | PRESENT — this decision |
| Duplicate VALIDATED/CANONICAL Asset | NONE | NONE found in current governance records |

Result: all mandatory gates hold. Transition is authorized.

## Lifecycle history

Both events belong to one approved governance action but retain separate ordinal records. Package 003 requires the intermediate state and establishes no minimum residence time in it.

| Sequence | Effective timestamp | Transition | Guard and evidence | Reason |
|---:|---|---|---|---|
| 0 | Prior governed state; preserved by Phase A/B/C records | Entry/presence in `CANDIDATE` | Candidate assessment and remediation history | Registered for possible reuse; exact original intake timestamp is not re-invented here |
| 1 | `2026-09-02T11:58:23-03:00` | `CANDIDATE → UNDER_REVIEW` | Tier 1 8/8; qualification 5/5; Founder initiates review; decision review and evidence matrix | Enter formal standard-path review after all five dimensions were satisfied |
| 2 | `2026-09-02T11:58:23-03:00` | `UNDER_REVIEW → VALIDATED` | Five base fields verified; concrete Forma B scenario; no duplicate; quality/risk gates passed with restrictions | Accept independent `RECOMMEND_VALIDATED` for the declared software scope |

This history must not be summarized as a direct Fast Path transition. ASSET-1 was not Fast Path eligible because of external dependencies and the elevated financial risk override.

## Evidence basis

- [Validation decision review](./crypto-scalping-core-asset-1-validation-decision-review.md): `RECOMMEND_VALIDATED`.
- [Validation evidence matrix](./crypto-scalping-core-asset-1-validation-evidence-matrix.md): Tier 1 8/8, qualification 5/5, criteria 12/12.
- [Controlled evidence](./crypto-scalping-core-asset-1-controlled-evidence.md): expected/observed MATCH, two repetitions, `DETERMINISTIC_MATCH`.
- [Phase C review](./asset-1-phase-c-controlled-evidence-review.md): `ASSET_1_PHASE_C_APPROVE_WITH_NON_BLOCKING_NOTES`.
- Phase B repository verification and independent review: approved with non-blocking notes.

## Preserved classifications and restrictions

| Concern | State after transition |
|---|---|
| Quality | `PASS_WITH_RESTRICTIONS` |
| Risk | `PASS_WITH_RESTRICTIONS` |
| Reproducibility | `REPRODUCIBLE_WITH_DOCUMENTED_PREREQUISITES`, controlled fixture only |
| Value | `PROYECTADO` |
| Reuse | `PROJECTED_REUSE / SAME_CONTEXT_REUSE` |
| Actual/repeated usage | YES / YES |
| Cross-context/demonstrated reuse | NO / NO |
| ASSET_VALIDATION_PROVENANCE | Sufficient for declared scope |
| GLOBAL_RESEARCH_PROVENANCE | PARTIAL |
| Software dependency licensing | PARTIAL |
| Project source licensing | `UNKNOWN / NO_ROOT_LICENSE_FOUND` |
| Historical market-data licensing | `UNKNOWN / RESTRICTED` |
| Synthetic fixture licensing | `NOT_APPLICABLE` |

`VALIDATED` certifies only that the applicable validation gates were met for the restricted framework claim. It does not certify every backtest, concrete strategy correctness, profitability, alpha, statistical robustness, universal absence of overfitting/look-ahead bias, live readiness, financial suitability/advice, distribution rights, Product readiness, Public sharing or CANONICAL authority.

External sharing, Public classification, distribution, Product reuse and CANONICAL evaluation remain blocked or restricted until their applicable licensing, exposure, maintenance and human-approval gates are satisfied.

## Review triggers and next gate

Review ASSET-1 at the earliest of:

1. material change to the operational boundary or observable framework behavior;
2. failed reproduction of the controlled fixture;
3. dependency/environment incompatibility or material dependency change;
4. first cross-context consumer or reuse claim;
5. licensing resolution or a change in source/data rights;
6. separately authorized CANONICAL evaluation;
7. evidence-freshness review by `2026-12-01` if none occurs earlier.

These are review triggers, not automatic transitions. The next governance gate is a separately authorized CANONICAL evaluation only if restrictions and Tier 2 promotion requirements are later satisfied; no such evaluation is authorized here.

## Decision effect

ASSET-1 final lifecycle is `VALIDATED / NOT_CANONICAL`. P004 contribution increases by one, from 1/3 to 2/3. The trigger remains `NOT_SATISFIED`; Package 004 remains `DORMANT / CONDITIONAL / NOT_AUTHORIZED`.

Next safe action: `ASSET_2_PHASE_C_CONTROLLED_EVIDENCE_PREPARATION`. It is not executed or authorized by this record.

## Post-transition integrity audit

| Control | Result |
|---|---|
| ASSET-1 final lifecycle | PASS — `VALIDATED` |
| UNDER_REVIEW historical trace | PASS — sequence 1 present |
| ASSET-1 CANONICAL | NO |
| ASSET-2/3/4/5 lifecycle changed by this decision | NO |
| Crypto modified | NO |
| Package 003 normative content modified | NO |
| Value inflated | NO — remains `PROYECTADO` |
| Reuse inflated | NO — demonstrated/cross-context remain NO |
| Licensing inflated | NO — PARTIAL/UNKNOWN/RESTRICTED preserved |
| P004 authorized | NO |
| Architecture conflict | NONE — standard-path guards and ordered history preserved |

Integrity result: PASS. `ASSET_1_POST_TRANSITION_INTEGRITY_FAILURE` not triggered.
