# ASSET-2 — Lifecycle Transition Decision

## Authoritative decision record

| Field | Value |
|---|---|
| Decision ID | `FD-ASSET-2-VALIDATED-001` |
| Classification | `FOUNDER_DECISION` |
| Decisor | Fundador |
| Effective timestamp | `2026-09-02T13:27:20-03:00` |
| Asset ID | `ASSET-2` |
| Name | Optimizador de parámetros por grid search con leaderboard |
| Type | `Herramienta` |
| Owner | Joel Diaz / Lab Founder |
| Originating Lab | Crypto Scalping Core / `LABOS-REF-LAB-0001` |
| Initial lifecycle | `CANDIDATE` |
| Intermediate lifecycle | `UNDER_REVIEW` |
| Final lifecycle | `VALIDATED` |
| Founder authorization | `APPROVE_ASSET_2_VALIDATED_TRANSITION` |
| Approval justification | Controlled optimizer evidence, independent review and confirmed source freshness satisfy all restricted internal VALIDATED gates. |
| CANONICAL | `NO / NOT_AUTHORIZED` |
| Package 004 | `DORMANT / CONDITIONAL / NOT_AUTHORIZED` |

The approval justification is 10–280 characters and identifies the evidence-based reason. This is the authoritative lifecycle act. The proposed governance record remains historical `PROPOSED_ONLY` evidence.

## Source freshness

| Evidence point | Commit / result |
|---|---|
| Phase B | `751970757a9c3b876ec16f3afd57c13f65a7457f` |
| Phase C controlled execution | `a86464448c2789b3d7278eaaaffb85666c518602` |
| Validation decision review | `dc4da184340377e8506b053bdedfb8fdb9153a29` |
| Transition-time HEAD | `dc4da184340377e8506b053bdedfb8fdb9153a29` |
| Branch | `main` |
| Classification | `SOURCE_FRESHNESS_CONFIRMED` |

No commit delta exists between validation review and transition time for the two IN_SCOPE files or the directly relevant ASSET-1 model/metrics dependencies inspected. The earlier `a864644… → dc4da184…` change remains documented: it added `ShortRegimeTransitionStrategy` registration, a default grid and CLI regime-loading selection, without changing the controlled Cartesian expansion, execution mechanics, metric propagation, ranking or leaderboard serialization. The new strategy adapter remains outside the controlled correctness claim.

The dirty Crypto research files observed before this action remained pre-existing and were not modified. No optimizer, test, strategy or research execution occurred.

## Pre-transition gate verification

| Gate | Required | Verified result |
|---|---|---|
| Candidate classification | PASS | PASS — coherent `Herramienta` Candidate |
| Tier 1 | 8/8 PASS | 8/8 PASS |
| Qualification | 5/5 SATISFIED | 5/5 SATISFIED |
| VALIDATED criteria | 12/12 PASS | 12 PASS; 0 partial/fail/insufficient |
| Quality | PASS_WITH_RESTRICTIONS | PASS_WITH_RESTRICTIONS |
| Financial/trading risk | PASS_WITH_RESTRICTIONS | PASS_WITH_RESTRICTIONS |
| Controlled determinism | DETERMINISTIC_MATCH | DETERMINISTIC_MATCH |
| Replay | REPLAY_MATCH | REPLAY_MATCH |
| Reproducibility | Documented evidence | `REPRODUCIBLE_WITH_DOCUMENTED_PREREQUISITES` |
| Source freshness | Permits transition | `SOURCE_FRESHNESS_CONFIRMED` |
| Blocking remediation | 0 | 0 |
| Founder decision | PRESENT | PRESENT — this decision |
| Duplicate VALIDATED/CANONICAL authority | NONE | NONE in authoritative lifecycle records |

All mandatory gates remain satisfied. The standard-path transition is authorized; Fast Path is not used.

## Lifecycle history

Both events belong to one Founder decision but retain separate ordered records. Package 003 requires the intermediate state and establishes no minimum residence time.

| Sequence | Effective timestamp | Transition | Guard/evidence | Reason |
|---:|---|---|---|---|
| 0 | Prior governed state; Phase A/B/C/review records | Entry/presence in `CANDIDATE` | Candidate assessment and remediation history | Registered for possible reuse; original Candidate timestamp is not invented |
| 1 | `2026-09-02T13:27:20-03:00` | `CANDIDATE → UNDER_REVIEW` | Tier 1 8/8; qualification 5/5; Founder review initiation; recommendation and matrix; freshness confirmed | Enter formal standard-path review after all five dimensions were satisfied |
| 2 | `2026-09-02T13:27:20-03:00` | `UNDER_REVIEW → VALIDATED` | Five base fields; concrete Forma B scenario; no duplicate; 12/12 criteria; quality/risk with restrictions | Accept `RECOMMEND_VALIDATED` for the restricted optimizer scope |

This history must not be compressed to a direct Candidate-to-Validated Fast Path.

## Evidence basis

- [Validation decision review](./crypto-scalping-core-asset-2-validation-decision-review.md): `RECOMMEND_VALIDATED`.
- [Validation evidence matrix](./crypto-scalping-core-asset-2-validation-evidence-matrix.md): Tier 1 8/8, qualification 5/5 and 12/12 mandatory criteria.
- [Controlled evidence](./crypto-scalping-core-asset-2-controlled-evidence.md): four expected/four observed combinations, metrics/ranking match, two identical executions.
- [Phase C independent review](./asset-2-phase-c-controlled-evidence-review.md): `ASSET_2_PHASE_C_APPROVE_WITH_NON_BLOCKING_NOTES`.
- Phase B repository verification and independent review: approved with non-blocking notes.

## Preserved classifications

| Concern | State after transition |
|---|---|
| Quality | `PASS_WITH_RESTRICTIONS` |
| Risk | `PASS_WITH_RESTRICTIONS` |
| Tie behavior | `DETERMINISTIC_UNDOCUMENTED_TIE_BEHAVIOR`; quality PARTIAL; `NON_BLOCKING_GAP` |
| Failure behavior | PARTIAL — empty grid ValidationError and execution RuntimeError explicit; missing metrics/recovery/atomicity/overwrite incomplete |
| Determinism | `DETERMINISTIC_MATCH` |
| Replay | `REPLAY_MATCH` |
| Reproducibility | `REPRODUCIBLE_WITH_DOCUMENTED_PREREQUISITES`, controlled fixture only |
| Dependencies | Python observed/unpinned; pandas declared/used/unpinned; pydantic declared/observed; PyYAML `USED_NOT_DECLARED / OPTIONAL`; lock/transitives incomplete |
| Software dependency licensing | PARTIAL |
| Project source licensing | `UNKNOWN / NO_ROOT_LICENSE_FOUND` |
| Synthetic fixture | `SELF_CREATED / NOT_APPLICABLE` |
| Historical market-data licensing | `UNKNOWN / RESTRICTED` |
| Controlled traceability | PASS |
| Asset validation provenance | PASS / sufficient for declared scope |
| Historical/global provenance | PARTIAL / PARTIAL |
| Value | `PROYECTADO` |
| Actual/repeated/same-context usage | YES / YES / YES |
| Projected reuse | YES |
| Cross-context/demonstrated reuse | NO / NO |

The 12 historical leaderboards and 20 journals remain usage evidence, not correctness evidence. Their historical identity is not rewritten.

## Correctness and authorization restrictions

`VALIDATED` applies only to the declared optimizer software responsibility. Optimizer correctness is not parameter optimality; ranking correctness is not financial usefulness; deterministic replay is not statistical robustness; repeated use is not cross-context reuse; and a VALIDATED Asset is not a validated strategy.

This decision establishes no profitability, alpha, robust parameter selection, absence of overfitting/look-ahead, OOS validity, live readiness, suitability or financial advice. It grants no external sharing, Public, distribution, Product reuse, Product attachment, CANONICAL or Package 004 authorization. Licensing remains unresolved as recorded.

## Review triggers and next governance gate

Review at the earliest of:

1. material optimizer behavior or source-boundary change;
2. grid/ranking contract or leaderboard schema change;
3. failed controlled replay;
4. dependency/environment incompatibility;
5. tie-breaking semantic change;
6. first cross-context reuse or consumer;
7. licensing change or resolution;
8. separately authorized CANONICAL evaluation;
9. evidence-freshness review by `2026-12-01` if none occurs earlier.

These triggers do not create automatic transitions.

## P004 recomputation

Authoritative lifecycle records now establish:

| Asset | Lifecycle | Evidence |
|---|---|---|
| ASSET-1 | `VALIDATED` | `FD-ASSET-1-VALIDATED-001` |
| ASSET-2 | `VALIDATED` | `FD-ASSET-2-VALIDATED-001` — this record |
| ASSET-3 | `VALIDATED` | `FD-ASSET-3-VALIDATED-001` |

Count: 3/3. Trigger `AT_LEAST_3_ASSETS_IN_VALIDATED`: `SATISFIED`. This means only `PACKAGE_004_ACTIVATION_TRIGGER_SATISFIED`. Package 004 remains `DORMANT / CONDITIONAL / NOT_AUTHORIZED` and is not active.

Next safe action: `PACKAGE_004_ACTIVATION_READINESS_REVIEW`. It is not executed here.

## Post-transition integrity audit

| Control | Result |
|---|---|
| ASSET-2 final lifecycle | PASS — `VALIDATED` |
| UNDER_REVIEW historical trace | PASS — sequence 1 |
| ASSET-2 CANONICAL | NO |
| ASSET-1/3/4/5 changed by this decision | NO |
| Crypto modified | NO |
| Package 003 normative content modified | NO |
| Value/reuse/licensing/financial claims inflated | NO |
| P004 trigger recomputed | YES — three authoritative records |
| P004 authorized/activated | NO / NO |
| Architecture conflict | NONE — trigger satisfaction remains distinct from authorization |

Integrity result: PASS. `ASSET_2_POST_TRANSITION_INTEGRITY_FAILURE` not triggered.
