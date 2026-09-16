# ASSET-2 — Validation Decision Review

## Decision record

| Field | Result |
|---|---|
| Authorization | `ASSET_2_VALIDATION_DECISION_REVIEW` / `FOUNDER_DECISION` |
| Date | 2026-09-02 |
| Candidate | `ASSET-2` — Optimizador de parámetros por grid search con leaderboard |
| Current lifecycle | `CANDIDATE` |
| Recommendation | `RECOMMEND_VALIDATED` |
| Transition performed | `NO` |
| Quality | `PASS_WITH_RESTRICTIONS` |
| Financial/trading risk | `PASS_WITH_RESTRICTIONS` |
| P004 after review | 2/3, `NOT_SATISFIED`, `NOT_AUTHORIZED` |

## Independent finding

Readiness and the Phase C approval were not treated as validation. The evidence was independently evaluated against Package 003 identity, Tier 1, all five qualification dimensions, VALIDATED entry criteria, effective exposure, risk override, governance and source-of-truth rules.

ASSET-2 is a valid `Herramienta` Candidate with a coherent two-module boundary and sufficient controlled evidence for its narrow responsibility: parameter-space enumeration → compatible execution → metric propagation → ranking → leaderboard representation. Expectations preceded observations; actual ASSET-2 functions were exercised; four expected combinations produced four ranked rows; two executions and replay yielded the identical CSV hash.

The recommendation does not validate a strategy, parameter optimality, profitability, alpha, robustness, absence of overfitting/look-ahead, OOS validity, historical research, live readiness or financial suitability.

## Source-version determination

Phase B inspected `751970757a9c3b876ec16f3afd57c13f65a7457f`; Phase C inspected `a86464448c2789b3d7278eaaaffb85666c518602`. Direct Phase C comparison established that the two IN_SCOPE files did not change across that interval. During this review, Crypto advanced externally to `dc4da184340377e8506b053bdedfb8fdb9153a29`. Read-only diff identified an eight-line addition/one-line replacement in `grid_search.py`: a new `ShortRegimeTransitionStrategy` import/registry/default-grid entry and CLI regime-loading selection. It did not alter the functions responsible for tested grid expansion, execution count, metric propagation, ranking or leaderboard serialization; `leaderboard.py` is unchanged. The new strategy integration is not covered by the controlled claim. The source changes therefore do not defeat the narrow recommendation, but remain an explicit freshness restriction to recheck at transition time.

## Qualification and validation

- Tier 1: 8/8 PASS.
- Qualification: 5/5 `SATISFIED`.
- VALIDATED criteria: 12/12 PASS; 0 PARTIAL, FAIL or EVIDENCE_REQUIRED.
- Grid enumeration: `GRID_ENUMERATION_MATCH`.
- Metric propagation: PASS.
- Ranking: `RANKING_MATCH`.
- Tie: `DETERMINISTIC_UNDOCUMENTED_TIE_BEHAVIOR`, PARTIAL/non-blocking.
- Leaderboard: PASS — four combinations/four rows, 77 columns and stable CSV identity.
- Determinism/replay: `DETERMINISTIC_MATCH` / `REPLAY_MATCH` across two exit-0 executions.
- Reproducibility: `REPRODUCIBLE_WITH_DOCUMENTED_PREREQUISITES`, controlled optimizer fixture only.
- Controlled traceability/provenance: PASS; historical/global provenance remains PARTIAL.
- Reuse: `PROJECTED_REUSE` with actual repeated same-context usage; not demonstrated/cross-context.
- Value: `PROYECTADO`.

## Restrictions and non-blocking gaps

Blocking remediation: NONE.

Non-blocking gaps/restrictions:

1. Tie precedence is deterministic but depends on enumeration order and is not a declared semantic contract.
2. Missing-metric handling, recovery, atomic persistence and overwrite protection remain partial.
3. PyYAML 6.0.3 is used in the controlled path but is not declared; pandas and the exact environment are unpinned; transitive inventory/lock is incomplete.
4. `NO_ROOT_LICENSE_FOUND`; project-source sharing/distribution rights remain unknown.
5. Historical market-data rights and historical leaderboard traceability remain `UNKNOWN/RESTRICTED` or PARTIAL.
6. Controlled test evidence is not comprehensive production coverage.
7. Crypto advanced to `dc4da184…` during review; the new short-strategy adapter is not covered by Phase C, although the tested optimizer core paths are unchanged.

Package 003 does not define complete dependency locking, comprehensive QA or external distribution rights as separate mandatory gates for effective Level 1 internal VALIDATED. These items remain explicit prerequisites/restrictions. They block or constrain external sharing, Public, distribution, Product reuse and future CANONICAL evaluation where the corresponding higher-exposure gates apply.

## Risk and correctness boundary

Risk verdict: `PASS_WITH_RESTRICTIONS`.

The fixture is synthetic, bounded and disconnected from brokerage/network activity. Correct enumeration and ranking only establish software behavior under the declared fixture. Correct ranking does not establish financial usefulness; deterministic replay does not establish research stability. Any real strategy optimization, financial deployment or broader sharing requires separate authorization and renewed elevated review.

## Lifecycle mechanics

ASSET-2 is not treated as Fast Path eligible because it has external/software dependencies and an elevated financial-use risk override. `RECOMMEND_VALIDATED` is a recommendation under the standard path. A later Founder action must preserve:

```text
CANDIDATE → UNDER_REVIEW → VALIDATED
```

This review performs no transition. CANONICAL and Package 004 remain unauthorized.

## Decision

`RECOMMEND_VALIDATED`

All exact mandatory controls required for the restricted internal VALIDATED claim are satisfied. Founder lifecycle authority remains required, and evidence freshness/duplicate status must be checked immediately before any transition.

Next safe action: `ASSET_2_LIFECYCLE_TRANSITION_DECISION`.

## Independent self-audit

| Control | Result |
|---|---|
| Five dimensions evaluated | PASS — 5/5 |
| Exact VALIDATED controls evaluated | PASS — evidence matrix |
| Source-version change addressed | PASS |
| Expected-before-observed preserved | PASS |
| Optimizer correctness generalized to finance/research | NO |
| Historical usage treated as correctness | NO |
| Same-context use treated as demonstrated reuse | NO |
| Value inflated | NO |
| Licensing categories separated | PASS |
| Dependency gaps silently fixed | NO |
| Lifecycle changed | NO |
| Crypto modified | NO |
| Package 003 modified | NO |
| Package 004 authorized/count changed | NO |

Integrity result: PASS; `ASSET_2_VALIDATION_REVIEW_INTEGRITY_FAILURE` not triggered.
