# Crypto Scalping Core — Asset Remediation Phase B Results

DUAL_REPOSITORY_ACCESS_READY. LabOS readable/writable; Crypto readable/read-only. Crypto main at 751970757a9c3b876ec16f3afd57c13f65a7457f, dirty preexisting. Commands: inventory, rg/type, Git metadata. Tests/experiments/trading/Crypto writes: 0. Package 003 CLOSED; Package 004 NOT_AUTHORIZED.

Current inventory: 12 leaderboards and 20 journals versus Phase A 11/19. Nine leaderboards and 15 journals tracked; three leaderboards/five journals untracked; memory index modified. Usage evidence only.

| Candidate | Before | Phase B action/evidence | After/status |
|---|---|---|---|
| ASSET-1 | MODERATE; READY_FOR_REPOSITORY_VERIFICATION | Direct framework/contracts/deps/tests/workflow inspection; minimal boundary | Static boundary complete; correctness/source/licenses open; READY_FOR_PHASE_C_EVIDENCE |
| ASSET-2 | MODERATE; legacy/current ambiguity | Current optimizer separated; parameters→memory traced; tests/12 outputs inspected | Static boundary complete; E2E/identity/source/licenses open; READY_FOR_PHASE_C_EVIDENCE |
| ASSET-4 | FAR/lower priority | Limited seven discovery modules + discovery output inventory | PARTIAL; REMEDIATION_REMAINS |
| ASSET-5 | FAR/lower priority | Limited signal_quality features/scoring/integration/output inventory | PARTIAL; REMEDIATION_REMAINS |

COMPLETE: AS1/AS2 boundary and static contract. PARTIAL: governance/dependencies/licenses and AS4/5 inventory. DEFERRED_PHASE_C: AS1 deterministic fixture; AS2 deterministic E2E/identity; licenses/dependency correction. BLOCKED for Phase B: 0.

For AS1/2, reuse remains PROJECTED_REUSE and value PROYECTADO; repeated use is SAME_CONTEXT, not CROSS_CONTEXT/DEMONSTRATED. Both are EXECUTION_EVIDENCE_REQUIRED. Software correctness is separate from strategy/profitability.

Phase C: AS1 expected trades/metrics/failures and environment; AS2 grid/rank/CSV/memory ties/failures and identity; both governed source/content_state and licenses. No new market experiment is required for software correctness.

VALIDATED before/after: ASSET-3 only. P004: 1/3, NOT_SATISFIED. Readiness is not recommendation or transition.

## Quality evidence matrix

| Candidate | Quality control | Status | Direct evidence / limitation |
|---|---|---|---|
| ASSET-1 | Clear scope | PASS | Minimal framework boundary identified; whole repository explicitly excluded |
| ASSET-1 | Inputs | PARTIAL | OHLCV schema and timeframe known; ordering, duplicates and OHLC integrity incompletely enforced |
| ASSET-1 | Outputs | PASS | `BacktestResult`, `BacktestTrade`, `BacktestMetrics` and CLI presentation are distinguishable |
| ASSET-1 | Dependencies | PARTIAL | Internal stack plus pandas/pydantic mapped; versions and full license evidence open |
| ASSET-1 | Failure behavior | PARTIAL | Missing columns/interval/timestamp failures visible; empty/warmup and semantic validation incomplete |
| ASSET-1 | Traceability | PARTIAL | Static data→features→strategy→simulation→metrics path exists; run identity/hashes absent |
| ASSET-1 | Existing usage | PASS | Multiple research workflows and outputs establish actual repeated same-context usage |
| ASSET-1 | Reproducibility | EVIDENCE_REQUIRED | Command and prerequisites exist, but no controlled replay or locked environment evidence |
| ASSET-1 | Source of truth | PARTIAL | Operational source paths identified; governed Candidate source/content_state remain open |
| ASSET-1 | Restrictions | PASS | Financial, licensing and correctness boundaries explicitly preserved |
| ASSET-1 | Testing evidence | PARTIAL | Indirect strategy/research tests exist; no direct engine/metrics/loader contract suite found |
| ASSET-2 | Clear scope | PASS | Current research optimizer and leaderboard isolated from legacy optimizer |
| ASSET-2 | Inputs | PASS | YAML/CLI config and parameter grid contract statically identified |
| ASSET-2 | Outputs | PASS | Ranked typed rows, CSV leaderboard and memory/journal outputs identified |
| ASSET-2 | Dependencies | PARTIAL | ASSET-1/internal stack mapped; optional PyYAML and pytest used but undeclared; versions open |
| ASSET-2 | Failure behavior | PARTIAL | Unsupported strategy and selected memory failure behavior visible; atomic persistence/recovery absent |
| ASSET-2 | Traceability | PARTIAL | Parameters→execution→metrics→row→artifacts traced; commit/config/data hashes omitted |
| ASSET-2 | Existing usage | PASS | 12 leaderboards and linked journals establish actual repeated same-context usage only |
| ASSET-2 | Reproducibility | EVIDENCE_REQUIRED | Static deterministic path exists; controlled E2E replay and environment capture absent |
| ASSET-2 | Source of truth | PARTIAL | Operational implementation selected; governed Candidate source/content_state remain open |
| ASSET-2 | Restrictions | PASS | Research stability separated from software determinism and profitability claims |
| ASSET-2 | Testing evidence | PARTIAL | Config/memory/import tests exist; current full grid/rank/CSV/replay path lacks direct E2E coverage |

## Remediation execution detail

| Remediation | BEFORE | ACTION | EVIDENCE | AFTER | STATUS |
|---|---|---|---|---|---|
| AR-AS1-01 | Candidate source/content_state incomplete | Identified minimal operational source boundary | `backtester.py`, `simulation.py`, strategy base and support modules | Operational source clarified; governed Candidate record incomplete | PARTIAL |
| AR-AS1-02 | Framework contract/boundary unverified | Inspected entry points, inputs, outputs, dependencies and failures | Static source/import/CLI contracts | Static boundary and contract established | COMPLETE |
| AR-AS1-03 | Metrics correctness/replay absent | Reconstructed reproducibility path without execution | Existing code/tests/workflow only | Behavioral evidence still needed | DEFERRED_PHASE_C |
| AR-AS1-04 | Dependency/licensing evidence incomplete | Reconciled declarations with imports and restrictions | `requirements.txt`, imports, no root LICENSE | Dependency map partial; external/data licenses open | PARTIAL |
| AR-AS2-01 | Current/legacy source ambiguity | Selected coherent reusable research optimizer boundary | `app/research/optimizer/*`; legacy path excluded | Operational source clarified; governed Candidate record incomplete | PARTIAL |
| AR-AS2-02 | Contract/traceability unverified | Traced config through leaderboard and memory | Source plus existing artifacts/tests | Static contract complete; artifact identity remains partial | COMPLETE |
| AR-AS2-03 | Ranking/replay correctness absent | Assessed ordering and determinism statically | Sorting, row construction, CSV and memory paths | Controlled E2E evidence still needed | DEFERRED_PHASE_C |
| AR-AS2-04 | Overfitting/dependencies/licensing open | Separated software determinism from research stability; mapped dependencies | Imports, requirements and risk rules | Boundaries explicit; dependency correction/licenses open | PARTIAL |
| AR-AS4-01/02 | Lower-priority source boundary open | Performed limited module/output inventory | Discovery package and existing reports | Boundary evidence remains incomplete | PARTIAL |
| AR-AS5-01/02 | Lower-priority source boundary open | Performed limited module/output inventory | Signal-quality package and existing reports | Boundary evidence remains incomplete | PARTIAL |

## Phase C routing

| Candidate | Unresolved item | Phase C requirement |
|---|---|---|
| ASSET-1 | Metric/trade/failure behavior | Controlled execution evidence |
| ASSET-1 | Environment and replay identity | Controlled execution evidence; dependency correction if approved |
| ASSET-1 | Candidate source/content_state | LabOS governance documentation |
| ASSET-1 | Software and market-data rights | External license verification |
| ASSET-1 | Demonstrated reuse/value | Cross-context reuse; value measurement; neither required to preserve projected status |
| ASSET-2 | Grid/rank/ties/CSV/memory behavior | Controlled execution evidence |
| ASSET-2 | Artifact identity/hashes/atomicity | Code change and/or documentation decision |
| ASSET-2 | PyYAML/test declarations and versions | Dependency correction |
| ASSET-2 | Candidate source/content_state | LabOS governance documentation |
| ASSET-2 | Software and market-data rights | External license verification |
| ASSET-2 | Research robustness/profitability | New research evidence only if separately authorized; not an Asset software-correctness gate |

## Freshness confirmation — 2026-09-02

Re-verification found Crypto on `main` at the same evidence commit. Static findings and inventory counts remain unchanged. Commands were `SAFE_READ_ONLY`; tests, experiments, trading and Crypto writes remained zero. ASSET-1 and ASSET-2 remain `READY_FOR_PHASE_C_EVIDENCE`, not ready for validation-decision review.
