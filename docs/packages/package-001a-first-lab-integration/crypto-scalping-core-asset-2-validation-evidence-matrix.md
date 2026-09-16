# ASSET-2 — Validation Evidence Matrix

## Review control

| Field | Value |
|---|---|
| Review | `ASSET_2_VALIDATION_DECISION_REVIEW` |
| Date | 2026-09-02 |
| Candidate | `ASSET-2` — Optimizador de parámetros por grid search con leaderboard |
| Current lifecycle | `CANDIDATE` |
| Review effect | Recommendation only; no transition |
| Package 003 | `CLOSED` |

## Identity and Tier 1 metadata

ASSET-2 remains a valid Asset Candidate. Its primary canonical type is `Herramienta`: it accepts an experiment/grid configuration, enumerates parameter combinations, invokes a controlled execution dependency, collects metrics, ranks results and represents a leaderboard. It is not the repository, the legacy optimizer, a strategy, a dataset or an historical output.

| Tier 1 field | Value | Source | Evidence class | Result |
|---|---|---|---|---|
| `nombre` | Optimizador de parámetros por grid search con leaderboard | Candidate assessment; remediation register | GOVERNED_RECORD | PASS |
| `tipo` | `Herramienta` | Candidate assessment; Package 003 taxonomy | GOVERNED_RECORD + NORMATIVE | PASS |
| `descripción` | Reusable grid-search tool that enumerates a parameter space, executes a compatible controlled evaluation, propagates metrics, ranks results and builds a leaderboard | Phase B boundary; Phase C evidence | DIRECTLY_VERIFIED | PASS |
| `hipótesis_de_uso` | A future quantitative-research Lab can use the tool to compare a declared parameter space through a standardized ranked leaderboard | Phase A Forma B; validation plan | DOCUMENTED_PRIOR_EVIDENCE | PASS |
| `content_state` | `borrador` | Phase C evidence; remediation register | GOVERNED_RECORD | PASS |
| `originating_Lab` | Crypto Scalping Core / `LABOS-REF-LAB-0001` | Package 001A records; register | GOVERNED_RECORD | PASS |
| `source_of_truth` | Governed Candidate evidence package in LabOS; controlled implementation at `main@a864644…` and review-time operational source `main@dc4da18…` | Phase C evidence; review-time diff; register | DIRECTLY_VERIFIED + GOVERNED_RECORD | PASS |
| `provenance` | Crypto commit/boundary → config/runner hashes → four controlled executions → metrics/ranking → CSV hash → reviews | Phase C controlled evidence | DIRECTLY_VERIFIED | PASS |

Tier 1 result: 8/8 PASS. `content_state=borrador` remains independent of lifecycle. Tier 2 is not imposed for this VALIDATED recommendation; it belongs to later CANONICAL preparation.

Owner: Joel Diaz / Lab Founder. Operational source: Crypto Scalping Core. Governance source: this LabOS evidence package and remediation register.

## Source boundary and version integrity

| Classification | Components |
|---|---|
| IN_SCOPE | `app/research/optimizer/grid_search.py`, `app/research/optimizer/leaderboard.py` |
| DEPENDENCY | ASSET-1, diagnostics, Research Memory and experiment/config YAML |
| OUT_OF_SCOPE | legacy `app/optimization/grid_search.py`, real strategies, datasets, historical journals and historical leaderboards |

Phase B used `751970757a9c3b876ec16f3afd57c13f65a7457f`; Phase C used `a86464448c2789b3d7278eaaaffb85666c518602`. Phase C found no IN_SCOPE change between those commits. During this decision review, Crypto advanced externally to `dc4da184340377e8506b053bdedfb8fdb9153a29`. Read-only diff found an IN_SCOPE change in `grid_search.py`: registration/default grid for `ShortRegimeTransitionStrategy` and inclusion of that name in the CLI regime-loading condition. `leaderboard.py` and the tested enumeration, execution-loop, metric propagation, ranking and serialization functions did not change. The new concrete-strategy adapter was not exercised and is outside the controlled correctness claim. `SOURCE_VERSION_CHANGED` is therefore addressed as a non-blocking freshness restriction, not ignored. Evidence freshness and this diff must be rechecked before any lifecycle decision.

## Five qualification dimensions

| Dimension | Requirement | Evidence | Strength | Risk | Verdict |
|---|---|---|---|---|---|
| Reuse evidence | Valid Forma A or Forma B with destination and scenario | Forma B identifies a future quantitative-research Lab using a declared parameter space and standardized leaderboard; 12 leaderboards/20 journals support usage only | MEDIUM | No cross-context use; 90-day trigger if later CANONICAL | SATISFIED |
| Minimum documentable quality | Five base fields plus owner validation | Tier 1 complete; Phase B contract; Phase C expected-before-observed 2×2 validation and negative cases | HIGH for controlled scope | Not comprehensive QA | SATISFIED |
| Traceable provenance | KO, research_id or verifiable source plus Lab/origin | Crypto origin/commits, narrow source boundary, fixture/config hashes, command, output hash and reviews | HIGH for validation scope | Historical/license provenance remains partial | SATISFIED |
| Assigned ownership | Human Asset_Owner accepts maintenance/lifecycle | Joel Diaz / Lab Founder recorded in register and Phase A authorization | HIGH | SOLO roles remain conceptually distinct | SATISFIED |
| Source of truth | One canonical, verifiable location | Unique governed Candidate evidence package in LabOS referencing one operational Crypto source/commit | MEDIUM-HIGH | Governance SOT must not be confused with operational source | SATISFIED |

Qualification: 5 SATISFIED; 0 partially satisfied; 0 not satisfied; 0 insufficient.

## Controlled software evidence

Expected combinations, metrics and ranks were recorded before execution. The actual ASSET-2 enumeration, orchestration, ranking and leaderboard builders were exercised with a compatible deterministic execution stub and ASSET-1 result models. Four expected combinations produced four results and four rows. Metric propagation matched. Ranking matched descending `(profit_factor, expectancy)`.

The exact tie was stable by enumeration order: `DETERMINISTIC_UNDOCUMENTED_TIE_BEHAVIOR`. This remains PARTIAL and a non-blocking restriction because Package 003 does not require a more sophisticated semantic tie breaker for internal VALIDATED, while no declared ASSET-2 contract was contradicted.

Two exit-0 executions produced the same CSV SHA-256 `ad6e52542ccc97ea4d795ff7277fd19d35e40717548fd7cdcbe0624db5e7e4ea`: `DETERMINISTIC_MATCH` and `REPLAY_MATCH`. This proves only controlled software repeatability, not financial or historical research stability.

## Quality controls

| Control | Status | Blocking | Restriction / scope |
|---|---|---:|---|
| Source boundary | PASS_WITH_RESTRICTION | NO | Narrow boundary; legacy excluded; review-time strategy registration delta is outside the tested core claim |
| Parameter input contract | PASS | NO | Tested actual `GridSearchConfig` 2×2 schema |
| Grid enumeration | PASS | NO | Four expected/four observed; tested ordering only |
| Execution integration | PASS | NO | Compatible deterministic stub; no real strategy claim |
| Metric propagation | PASS | NO | Financial meaning of metrics not certified |
| Ranking | PASS | NO | Descending PF then expectancy |
| Tie behavior | PARTIAL | NO | Stable enumeration order is undocumented semantically |
| Leaderboard contract | PASS | NO | 4 rows, 77 columns, fields/order/CSV verified |
| Failure behavior | PARTIAL | NO | Empty grid and raised execution explicit; missing metrics, recovery and atomicity incomplete |
| Determinism | PASS | NO | Same source, config, parameter order and environment only |
| Replay | PASS | NO | Controlled artifact only |
| Controlled traceability | PASS | NO | Full hash-linked chain |
| Historical traceability | PARTIAL | NO | Historical outputs remain unhashed usage evidence |
| Validation testing | PASS | NO | Controlled positive/repeat/negative evidence; not comprehensive coverage |
| Dependencies | PARTIAL | NO | PyYAML undeclared; exact locks/transitives incomplete |
| Provenance | PASS for validation scope / PARTIAL globally | NO | Historical data and licensing remain outside claim |

## Dependencies and licensing

| Concern | Finding | Classification | Blocks internal VALIDATED? | Restricts |
|---|---|---|---:|---|
| Python | 3.13.7 observed; exact runtime unpinned | VERSION_OBSERVED / VERSION_UNPINNED | NO | Replay requires documented compatible environment |
| pandas | 2.3.3, declared and used; BSD-3 metadata observed | VERSION_UNPINNED | NO | Exact-version stability |
| pydantic | 2.12.5, declared; requirement `>=2,<3`; MIT observed | VERSION_OBSERVED | NO | Exact-version replay |
| PyYAML | 6.0.3 used in controlled path but not declared; MIT observed | USED_NOT_DECLARED / OPTIONAL | NO | Dependency correction before broader consumption; documented prerequisite |
| pytest | Not used in controlled path | NOT_USED_IN_CONTROLLED_PATH | NO | None for this evidence |
| Lock/transitives | Incomplete | NON_BLOCKING_GAP at current internal exposure | NO | Cross-Lab/Public/CANONICAL preparation |
| Crypto project source | `NO_ROOT_LICENSE_FOUND`; source rights unknown | PROJECT_SOURCE_LICENSE_STATUS `UNKNOWN` | NO under Package 003 internal-validation rule | External sharing, Public, distribution, Product reuse and CANONICAL |
| Synthetic fixture | Self-created | DATA_LICENSE_STATUS `NOT_APPLICABLE` | NO | None |
| Historical market data | Rights unresolved and outside fixture | DATA_LICENSE_STATUS `UNKNOWN/RESTRICTED` | NO for software fixture | Historical reuse/distribution |

PyYAML's undeclared state is not hidden or repaired. At effective Level 1 with no external consumer, Product attachment or Public scope, Package 003 makes dependency stability recommended rather than an independent mandatory VALIDATED gate. It remains a non-blocking gap and explicit reproduction restriction.

## Risk, provenance, usage and value

Financial/trading risk verdict: `PASS_WITH_RESTRICTIONS`. Optimizer correctness does not establish optimal parameters, profitability, alpha, robustness, absence of overfitting/look-ahead, OOS validity, live readiness, financial suitability or advice. Future operational, sharing, Product or CANONICAL use requires renewed elevated review.

`ASSET_VALIDATION_PROVENANCE`: PASS. `GLOBAL_RESEARCH_PROVENANCE`: PARTIAL. Retroactive hashes for historical leaderboards are not a Package 003 requirement for this declared controlled scope.

| Classification | Result |
|---|---|
| ACTUAL_USAGE | YES |
| REPEATED_USAGE | YES |
| SAME_CONTEXT_REUSE | YES — Crypto only |
| CROSS_CONTEXT_REUSE | NO |
| PROJECTED_REUSE | YES — valid Forma B |
| DEMONSTRATED_REUSE | NO |

Value remains `PROYECTADO`. Standard enumeration, comparison, ranking, repeatability and traceability support expected usefulness, but no cross-context consumer or measured time/quality/risk outcome supports `DEMOSTRADO`.

## ASSET_2_VALIDATED_CRITERIA_MATRIX

| ID | Mandatory criterion | Evidence | Normative source | Status | Blocking | Restriction |
|---|---|---|---|---|---:|---|
| VC-01 | Valid Candidate and canonical type | Coherent `Herramienta` identity and narrow consumption form | Definition; taxonomy | PASS | NO | Boundary cannot include legacy/artifacts |
| VC-02 | Tier 1 exactly 8/8 | Metadata table above | Registry contract | PASS | NO | `content_state` remains independent |
| VC-03 | Five qualification dimensions satisfied | 5/5 table above | Qualification framework | PASS | NO | Forma B, not demonstrated reuse |
| VC-04 | Five base fields verified | Name, type, description, use hypothesis, content state | Lifecycle VALIDATED entry | PASS | NO | None |
| VC-05 | Concrete reuse scenario | Future quantitative Lab using standardized grid/ranked comparison | Lifecycle; qualification | PASS | NO | 90-day trigger if later CANONICAL |
| VC-06 | No VALIDATED/CANONICAL duplicate | Register/Phase A duplicate audit; legacy optimizer excluded, not a governed duplicate | Lifecycle; registry contract | PASS | NO | Recheck at transition time |
| VC-07 | Verifiable provenance and one source of truth | Controlled hash chain plus governed Candidate SOT | Source-of-truth rules | PASS | NO | Global provenance remains partial |
| VC-08 | Human owner assigned | Joel Diaz / Lab Founder | Ownership | PASS | NO | SOLO roles remain conceptually separate |
| VC-09 | Applicable exposure evaluated | No active external consumer, Product attachment or Public evidence; effective Level 1 | Quality gates | PASS | NO | LabOS-Shared authorization is not consumption |
| VC-10 | Financial/licensing risk override evaluated | Correctness boundary and separated licenses/data rights | Risk model; quality gates | PASS | NO | Elevated restrictions preserved |
| VC-11 | Applicable minimum quality gate satisfied | Grid/metrics/rank/leaderboard/determinism/replay pass; partial controls explicit | Quality gates | PASS | NO | Not comprehensive QA; dependency/failure restrictions |
| VC-12 | Human lifecycle decision remains required | Recommendation only; no state change | Governance; lifecycle | PASS | NO | Standard path must be separately authorized |

Totals: 12 mandatory controls; PASS 12; PARTIAL 0; FAIL 0; EVIDENCE_REQUIRED 0. Technical PARTIAL controls are explicit limitations within the applicable quality gate; they are not omitted or used to compensate for a failed mandatory criterion.

## Final gate

Quality: `PASS_WITH_RESTRICTIONS`.

The narrow internal validation claim has sufficient boundary, contract, enumeration, integration, propagation, ranking, leaderboard, deterministic replay, traceability and test evidence. Tie semantics, failure recovery/atomic persistence, dependency declaration/locking, source licensing and historical provenance remain restrictions. They constrain use and future exposure but do not defeat the exact internal VALIDATED criteria.
