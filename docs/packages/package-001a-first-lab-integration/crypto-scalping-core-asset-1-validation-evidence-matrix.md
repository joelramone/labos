# ASSET-1 — Validation Evidence Matrix

## Review control

| Field | Value |
|---|---|
| Review | `ASSET_1_VALIDATION_DECISION_REVIEW` |
| Date | 2026-09-02 |
| Candidate | `ASSET-1` |
| Current lifecycle | `CANDIDATE` |
| Review effect | Recommendation only; no transition |
| Package 003 | `CLOSED` |

## Identity and Tier 1 metadata

ASSET-1 is a valid Asset Candidate. Its primary consumption form is a `Framework`: it organizes loader, strategy interface, simulation and results components under a coherent backtesting contract. It is neither the entire repository nor a concrete trading strategy.

| Tier 1 field | Value | Source | Evidence class | Result |
|---|---|---|---|---|
| `nombre` | Framework de backtesting para estrategias de trading | Candidate assessment; remediation register | GOVERNED_RECORD | PASS |
| `tipo` | `Framework` | Candidate assessment; Package 003 taxonomy | GOVERNED_RECORD + NORMATIVE | PASS |
| `descripción` | Reusable technical framework that ingests OHLCV, accepts a strategy contract, simulates trades and returns structured metrics | Phase B boundary and Phase C evidence | DIRECTLY_VERIFIED | PASS |
| `hipótesis_de_uso` | A future Lab evaluating quantitative hypotheses can use the generic execution/metrics contract with its own permitted data and strategy | Phase A Forma B; readiness/integration records | DOCUMENTED_PRIOR_EVIDENCE | PASS |
| `content_state` | `borrador` | Phase C evidence and remediation register | GOVERNED_RECORD | PASS |
| `originating_Lab` | Crypto Scalping Core / `LABOS-REF-LAB-0001` | Package 001A records and register | GOVERNED_RECORD | PASS |
| `source_of_truth` | Governed Candidate evidence package in LabOS; operational implementation referenced at Crypto `main@7519707…` | Phase C evidence and register | DIRECTLY_VERIFIED + GOVERNED_RECORD | PASS |
| `provenance` | Crypto commit/boundary → fixture/runner hashes → command → two executions → evidence/review | Phase C controlled evidence | DIRECTLY_VERIFIED | PASS |

The eight fields are present and valid. `content_state=borrador` does not derive from or change lifecycle. Tier 2 is not imposed for this validation recommendation; future CANONICAL preparation remains separate.

## Source boundary

| Classification | Components |
|---|---|
| IN_SCOPE | `app/research/backtester.py`, `app/research/simulation.py`, `app/research/strategies/base.py` |
| DEPENDENCY | result structures, data utilities, features, config, regimes and concrete strategies |
| EXTERNAL_DEPENDENCY | caller-provided OHLCV input and Python packages |
| OUT_OF_SCOPE | repository as a whole, datasets, optimizer, research outputs, paper/live trading and concrete-strategy correctness |

Verdict: coherent and unchanged from Phase B. The controlled evidence exercises loader plus simulator/strategy contract without expanding the Asset to dependent research workflows.

## Five qualification dimensions

| Dimension | Requirement | Evidence | Strength | Risk | Verdict |
|---|---|---|---|---|---|
| Reuse evidence | Forma A or valid Forma B with destination and scenario | Forma B targets a future quantitative-research Lab using the generic execution/metrics contract; repeated Crypto use is supporting evidence only | MEDIUM | No cross-context use; 90-day trigger if later CANONICAL | SATISFIED |
| Minimum documentable quality | Five base fields plus owner validation | Tier 1 complete; Phase B contract; Phase C expected/observed deterministic validation; owner accepted in Phase A authorization record | HIGH for declared controlled scope | Coverage is not comprehensive | SATISFIED |
| Traceable provenance | KO, research_id or verifiable source plus Lab/origin | Crypto origin/commit, implementation boundary, fixture/runner hashes, command, outputs and reviews | HIGH for validation scope | Wider research/licensing provenance remains partial | SATISFIED |
| Assigned ownership | Human Asset_Owner accepts maintenance/lifecycle | Joel Diaz / Lab Founder recorded and accepted in Phase A/register | HIGH | SOLO role concentration remains conceptually separated | SATISFIED |
| Source of truth | One canonical, verifiable location | Unique governed Candidate evidence package in LabOS with one referenced operational Crypto source/commit | MEDIUM-HIGH | Must not confuse evidence SOT with operational repository | SATISFIED |

Qualification count: 5 `SATISFIED`; 0 partial; 0 not satisfied; 0 insufficient.

## Controlled correctness evidence

`EXPECTED_BY_SPECIFICATION` was documented before execution: one entry at 100, take-profit exit at 101, gross PnL 1, fees 0.0804, net PnL/final fixture equity 0.9196, one win and max drawdown 0. `OBSERVED_FROM_IMPLEMENTATION` matched without revising expectations. Two captured exit-0 executions were identical: `DETERMINISTIC_MATCH`.

This is sufficient minimum behavioral evidence for the declared loader/simulator/strategy-interface scope. It is not comprehensive software certification and does not establish behavior for every strategy, dataset, resampling path, feature pipeline or CLI edge case.

## Reproducibility, contracts and tests

Controlled fixture: `REPRODUCIBLE_WITH_DOCUMENTED_PREREQUISITES`. Package 003 recommends repeatability but does not require a fully locked environment for VALIDATED; locked dependency stability becomes stricter with exposure and CANONICAL preparation. The classification is compatible with internal VALIDATED review under explicit prerequisites and restrictions.

| Control | Status | Blocking | Restriction |
|---|---|---:|---|
| Input contract | PARTIAL | NO | Chronological ordering is caller-owned; semantic OHLC validation incomplete |
| Output contract | PASS | NO | Applies to typed trades/results/metrics in declared scope |
| Failure behavior | PARTIAL | NO | Missing column explicit; empty simulator graceful; reverse order implicit; full CLI incomplete |
| Deterministic behavior | PASS | NO | Limited to fixture, commit and observed environment |
| Reproducibility | PASS | NO | Controlled fixture only, with documented prerequisites |
| Validation testing | PASS | NO | Two controlled runs plus bounded negative cases |
| Comprehensive production coverage | PARTIAL | NO | Not claimed or required as complete correctness certification |

## Dependencies and licensing

| Concern | Finding | Classification | Blocks VALIDATED? | Blocks/restricts |
|---|---|---|---:|---|
| Python | 3.13.7 observed; repository states 3.9+ | VERSION_OBSERVED / VERSION_UNPINNED | NO | Reproduction requires compatible runtime |
| pandas | 2.3.3 used; requirement unpinned; BSD-3 metadata observed | DEPENDENCY LICENSE PARTIAL | NO | Version stability and full dependency manifest |
| pydantic | 2.12.5 used; declared `>=2,<3`; MIT metadata observed | DEPENDENCY LICENSE PARTIAL | NO | Exact-version replay not guaranteed |
| Transitive dependencies | Inventory/locks incomplete | NON_BLOCKING_GAP at current internal exposure | NO | Cross-Lab/Public/CANONICAL preparation |
| Crypto project source | No root LICENSE; reuse rights unknown | PROJECT_SOURCE_LICENSE_STATUS `UNKNOWN` | NO under internal validation rule | External sharing, distribution, Public, Product reuse and CANONICAL decision until resolved |
| Synthetic fixture | Original LabOS validation data | DATA_LICENSE_STATUS `NOT_APPLICABLE` for external market data | NO | None for fixture |
| Historical market data | Rights unresolved and outside fixture | DATA_LICENSE_STATUS `UNKNOWN/RESTRICTED` | NO for software fixture scope | Historical research reuse/distribution |

Package 003 does not state that external distribution rights must be resolved before internal `VALIDATED`; it requires licensing/sensitivity gates when exposure, licensed data or sharing makes them applicable. The uncertainty therefore remains an elevated restriction, not an invented validation blocker. ASSET-1 is not Fast Path eligible because it has external dependencies and a financial risk override.

## Financial/trading risk override

Verdict: `PASS_WITH_RESTRICTIONS`.

The evidence explicitly limits validation to deterministic software behavior. It makes no claim of profitability, alpha, statistical robustness, universal absence of overfitting/look-ahead bias, market suitability, production/live readiness or financial advice. Synthetic data, no network/trading and human decision authority adequately isolate the validation claim. Future sharing, CANONICAL promotion or operational use requires renewed elevated review.

## Provenance, usage and value

`ASSET_VALIDATION_PROVENANCE`: PASS. The implementation and controlled evidence chain is identifiable and reproducible. `GLOBAL_RESEARCH_PROVENANCE`: PARTIAL due historical data rights, dirty research outputs and unlocked environment; it is outside the validation claim.

| Classification | Result |
|---|---|
| ACTUAL_USAGE | YES |
| REPEATED_USAGE | YES |
| SAME_CONTEXT_REUSE | YES — Crypto only |
| CROSS_CONTEXT_REUSE | NO |
| PROJECTED_REUSE | YES — valid Forma B |
| DEMONSTRATED_REUSE | NO |

Value remains `PROYECTADO`. Evidence supports expected usefulness through standardized execution, structured metrics, repeated same-context use and controlled deterministic behavior, but no consumer/time/risk/value measurement supports `DEMOSTRADO`. Package 003 value classification informs priority and does not automatically change lifecycle; commercial value is not required.

## ASSET_1_VALIDATED_CRITERIA_MATRIX

| ID | Mandatory criterion | Evidence | Normative source | Status | Blocking | Restriction |
|---|---|---|---|---|---:|---|
| VC-01 | Valid Asset Candidate and canonical type | Identity plus coherent Framework consumption form | Definition; taxonomy | PASS | NO | Boundary must remain narrow |
| VC-02 | Tier 1 exactly 8/8 | Metadata table above | Registry contract | PASS | NO | `content_state` remains independent |
| VC-03 | Five qualification dimensions satisfied | 5/5 table above | Qualification framework | PASS | NO | Forma B, not demonstrated reuse |
| VC-04 | Five base fields verified | Name/type/description/use hypothesis/content state | Lifecycle VALIDATED entry | PASS | NO | None |
| VC-05 | Concrete reuse scenario | Future quantitative-research Lab applying generic execution/metrics contract | Lifecycle; qualification | PASS | NO | 90-day trigger if later CANONICAL |
| VC-06 | No VALIDATED/CANONICAL duplicate | Phase A registry duplicate audit; no conflicting record identified | Lifecycle; registry contract | PASS | NO | Recheck at transition time |
| VC-07 | Verifiable provenance and one source of truth | Controlled chain plus governed Candidate source | Source-of-truth rules | PASS | NO | Global research provenance remains partial |
| VC-08 | Human owner assigned | Joel Diaz / Lab Founder | Ownership | PASS | NO | Roles remain conceptually separate |
| VC-09 | Applicable base exposure evaluated | No active external consumer/product attachment/Public evidence; effective Level 1 | Quality gates | PASS | NO | Default LabOS-Shared is authorization, not consumption |
| VC-10 | Financial/licensing risk override evaluated | Explicit correctness boundary; separated licensing categories | Risk model; quality gates | PASS | NO | ELEVATED restrictions preserved |
| VC-11 | Applicable minimum quality gate satisfied | Controlled match/repeatability plus explicit partial contracts | Quality gates | PASS | NO | Not comprehensive correctness certification |
| VC-12 | Valid human lifecycle decision remains required | Review recommends only; no state mutation | Governance; lifecycle | PASS | NO | Standard-path transitions must be explicit |

Totals: 12 controls; PASS 12; PARTIAL 0; FAIL 0; EVIDENCE_REQUIRED 0. Partial technical qualities are explicit non-blocking restrictions within VC-11, not hidden compensation for a failed mandatory criterion.

## Quality gate verdict

`PASS_WITH_RESTRICTIONS`

Source boundary, output contract, controlled determinism, scoped reproducibility, traceability and validation tests pass. Input validation, full failure surface, dependency locking and global provenance remain partial. Those limits constrain the claim and future exposure; they do not defeat minimum internal validation under the exact Package 003 rules.
