# ASSET-1 — Repository Verification

Control: 2026-08-25; Crypto main 751970757a9c3b876ec16f3afd57c13f65a7457f, dirty state preexisting. STATIC + READ_ONLY; tests, experiments and Crypto writes: 0. Lifecycle UNCHANGED.

## Boundary

ASSET-1 is not the repository. IN_SCOPE: app/research/simulation.py (engine/results/metrics), strategies/base.py (plugin contract), backtester.py (CLI/orchestration/load). DEPENDENCY: results.py, data_utils.py, features.py, config.py, regimes/ and concrete strategies. EXTERNAL_DEPENDENCY: local OHLCV CSV. OUT_OF_SCOPE: data, optimizer, outputs/reports, app/main.py, app/optimization/, paper/live trading, strategy correctness and profitability.

Entry: python -m app.research.backtester --data <csv> --strategy <key> --timeframe <1m|5m|15m>. Inputs require timestamp/open/high/low/close/volume. Output is typed BacktestResult/Trade/Metrics; CLI output is not an authoritative run. Missing columns/unsupported interval fail explicitly. Empty/warmup, ordering, duplicates, OHLC integrity, signal semantics and fee/notional validation are partial.

## Evidence

Python 3.9+, pandas and pydantic are DECLARED_AND_USED. Internal research stack and local CSV are used. Broker/network is NOT_APPLICABLE. Locked versions UNKNOWN. Software licensing PARTIAL; NO_ROOT_LICENSE_FOUND means repository license UNKNOWN. Market-data licensing RESTRICTED/UNKNOWN.

No direct tests were found for loader/resampling/simulation/metrics/drawdown/base contract. Strategy/regime/attribution/diagnostic tests give indirect evidence; the tested validator is not invoked by this CLI. Tests were inspected, not run.

ACTUAL_USAGE, REPEATED_USAGE and SAME_CONTEXT_REUSE exist across optimizer, walk-forward, OOS, regimes and reports. CROSS_CONTEXT_REUSE absent; PROJECTED_REUSE, not DEMONSTRATED_REUSE. Value PROYECTADO/unmeasured.

Path: snapshot → CSV → load/resample/features → strategy → simulator → metrics. Same ordered inputs/code/config/versions should be deterministic (no RNG), but no replay/locked environment: EXECUTION_EVIDENCE_REQUIRED. Provenance source → implementation → workflow/outputs → Package 001A/KO-5 → Candidate → Package 003 → Phase A → Phase B is PARTIAL because governed source/content_state, hashes and rights remain open.

| Quality control | Status |
|---|---|
| Clear scope, outputs, usage, restrictions | PASS |
| Inputs, dependencies, failures, traceability, source of truth, testing | PARTIAL |
| Reproducibility | EVIDENCE_REQUIRED |

Remediation: boundary/static contract COMPLETE; licenses/source PARTIAL; controlled correctness DEFERRED_PHASE_C. Readiness READY_FOR_PHASE_C_EVIDENCE. Phase C requires deterministic expected trades/metrics/failures, environment record, governed source/content_state and licenses—not new research.

Framework validation never implies strategy correctness, profit, alpha, universal absence of look-ahead/overfitting, live readiness or suitability.

## Re-verification — 2026-09-02

The repository was re-inspected at the same commit `751970757a9c3b876ec16f3afd57c13f65a7457f` on branch `main`. `git diff 7519707..HEAD` returned no source, test, configuration or dependency-declaration changes. The dirty tree remains confined to preexisting research memory, regime/report files and untracked journals/leaderboards/reports; none is promoted to correctness evidence. Therefore the 2026-08-25 boundary, dependency, test, usage and reproducibility findings remain current.

Execution classification: repository inventory, Git metadata and static file inspection were `SAFE_READ_ONLY`. Unit tests and backtest execution were not necessary to refresh the static finding and were not run. A behavioral correctness claim still requires `DEFERRED_EXECUTION_REQUIRED` under a separately authorized controlled fixture.
