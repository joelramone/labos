# ASSET-2 — Proposed Governance Decision

## Status

`PROPOSED_ONLY`

This record is prepared evidence, not a lifecycle decision. It has no state effect without a separately authorized Founder action.

| Field | Proposed record |
|---|---|
| Asset | `ASSET-2` — Optimizador de parámetros por grid search con leaderboard |
| Type | `Herramienta` |
| Owner | Joel Diaz / Lab Founder |
| Originating Lab | Crypto Scalping Core / `LABOS-REF-LAB-0001` |
| Current lifecycle | `CANDIDATE` |
| Proposed path | `CANDIDATE → UNDER_REVIEW → VALIDATED` |
| Technical recommendation | `RECOMMEND_VALIDATED` |
| Qualification | 5/5 `SATISFIED` |
| VALIDATED criteria | 12 PASS; 0 PARTIAL; 0 FAIL; 0 EVIDENCE_REQUIRED |
| Quality | `PASS_WITH_RESTRICTIONS` |
| Risk | `PASS_WITH_RESTRICTIONS` |
| Reproducibility | `REPRODUCIBLE_WITH_DOCUMENTED_PREREQUISITES`, controlled optimizer fixture only |
| Value | `PROYECTADO` |
| Reuse | `ACTUAL_USAGE / REPEATED_USAGE / SAME_CONTEXT_REUSE / PROJECTED_REUSE`; no cross-context or demonstrated reuse |
| Validation provenance | PASS for declared controlled scope |
| Global research provenance | PARTIAL |
| Founder decision required | YES |
| CANONICAL | `NOT_PROPOSED / NOT_AUTHORIZED` |

## Evidence basis

- Phase B repository boundary and static contract at `751970757a9c3b876ec16f3afd57c13f65a7457f`.
- Phase C controlled source at `a86464448c2789b3d7278eaaaffb85666c518602`; review-time source `dc4da184340377e8506b053bdedfb8fdb9153a29` adds a short-strategy registration/default grid but leaves the controlled optimizer-core and leaderboard functions unchanged.
- Predetermined 2×2 grid, four expected/four observed combinations, exact metric propagation and expected ranking.
- Deterministic enumeration-order tie behavior.
- Four-row, 77-column leaderboard and identical CSV SHA-256 `ad6e52542ccc97ea4d795ff7277fd19d35e40717548fd7cdcbe0624db5e7e4ea` in two executions.
- `DETERMINISTIC_MATCH`, `REPLAY_MATCH` and controlled traceability PASS.
- Independent Phase C and validation-decision reviews.

## Dependencies and licensing restrictions

- Python 3.13.7, pandas 2.3.3, pydantic 2.12.5 and PyYAML 6.0.3 were observed.
- PyYAML is `USED_NOT_DECLARED / OPTIONAL`; exact environment/transitive lock is incomplete.
- Software dependency licensing is PARTIAL from installed metadata.
- Project source licensing is `UNKNOWN / NO_ROOT_LICENSE_FOUND`.
- Historical market-data licensing is `UNKNOWN / RESTRICTED`.
- Synthetic fixture is `SELF_CREATED / NOT_APPLICABLE` to market-data licensing.
- The review-time `ShortRegimeTransitionStrategy` adapter is not included in the controlled correctness claim and must be considered in the transition freshness check.
- No external sharing, Public classification, distribution, Product reuse or CANONICAL authority follows from the proposed VALIDATED status.

## Preserved restrictions

Validation would cover only the declared optimizer software scope. It would not certify parameter optimality, strategy profitability, alpha, robustness, absence of overfitting/look-ahead, OOS/walk-forward validity, historical research correctness, live readiness, suitability or financial advice. Tie semantics, failure recovery/atomic output, dependency declaration/locking, licensing and global provenance remain review triggers.

## Required next action

`ASSET_2_LIFECYCLE_TRANSITION_DECISION`

That action must recheck evidence freshness, duplicate status, mandatory gates and the Founder decision, then record the standard lifecycle path without bypassing `UNDER_REVIEW`. This proposal does not execute it and does not authorize CANONICAL or Package 004.
