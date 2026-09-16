# ASSET-1 — Controlled Software Evidence

## Control record

| Field | Value |
|---|---|
| Authorization | `ASSET_REMEDIATION_PHASE_C_CONTROLLED_EVIDENCE_PREPARATION` / `FOUNDER_DECISION` |
| Date | 2026-09-02 |
| Candidate | `ASSET-1` — Framework de backtesting para estrategias de trading |
| Crypto repository | `https://github.com/joelramone/crypto-scalping-core.git` |
| Crypto branch / commit | `main` / `751970757a9c3b876ec16f3afd57c13f65a7457f` |
| Execution scope | Controlled software fixture only; no research or trading |
| Lifecycle | `UNCHANGED` |

## Fixture design

The fixture is a three-row synthetic OHLCV CSV created in LabOS. It contains chronological ISO-8601 timestamps and numeric open, high, low, close and volume values. It uses no Binance or other market data. A validation-only `ControlledStrategy` enters once at row zero, emits no explicit exit signal, and exposes fixed 1% take profit, 0.5% stop loss and two-candle maximum holding period.

| Artifact | Identity |
|---|---|
| Fixture | `tests/asset-validation/asset-1-controlled-fixture.csv` |
| Fixture SHA-256 | `6477028df7b39764100e6e22e3f32ac96feb9c36f0645ff5bafc4b3ccd161bb8` |
| Runner | `tests/asset-validation/asset-1-controlled-evidence-runner.py` |
| Runner SHA-256 | `ebe5ecfeb9d32bfa877466133435be927b29e245a5fb516335b415989d6e1ba5` |
| Bars | 3 |
| Data source | `SYNTHETIC_LOCAL`, generated solely for validation |

The runner and fixture are LabOS evidence artifacts. They are not Crypto tests, research experiments, datasets or production source.

## Expected outcome — defined before execution

`EXPECTED_BY_SPECIFICATION` was calculated manually from the fixture and declared before execution:

| Measure | Expected | Derivation |
|---|---:|---|
| Entry signals / entries / positions | 1 / 1 / 1 | Stub emits `True` only at row zero |
| Entry | Row 0 at 100.0 | Close of entry row |
| Exit | Row 1 at 101.0, `take_profit` | 100 × 1.01; row 1 high is 101.2 and low 100.0 does not reach stop 99.5 |
| Gross PnL | 1.0 | Notional 100 gives quantity 1; 101 − 100 |
| Fees | 0.0804 | 100 × 0.0004 + 101 × 0.0004 |
| Net PnL / final fixture equity | 0.9196 / 0.9196 | Gross PnL − fees; one closed position |
| Wins / losses / win rate | 1 / 0 / 1.0 | Positive net PnL |
| Expectancy / average win / average loss | 0.9196 / 0.9196 / 0.0 | One winning trade |
| Max drawdown | 0.0 | Single positive closed-trade equity increment |
| Profit factor | Positive infinity | Positive profit with no gross loss; observed but not used as a mandatory finite assertion |

No expected value was changed after observing the implementation.

## Execution safety and command

Classification before execution: `SAFE_CONTROLLED_TEST`.

The fixture is synthetic and local; runtime is bounded; no network, credentials, API, exchange, live/paper trading, optimizer, research pipeline, real dataset or permanent research output is involved. `PYTHONDONTWRITEBYTECODE=1` prevents Python cache writes and `PYTHONPATH` references Crypto read-only.

Executed twice successfully:

```text
set PYTHONDONTWRITEBYTECODE=1& set PYTHONPATH=C:\Users\jd0519\Documents\Personal\crypto-scalping-core& python tests\asset-validation\asset-1-controlled-evidence-runner.py tests\asset-validation\asset-1-controlled-fixture.csv
```

Two earlier launcher attempts targeting `.crypto-venv\Scripts\python.exe` returned exit 1 before Python execution because the repository environment has a Unix-style layout and no Windows `Scripts` path. They generated no framework observation and are not counted as test repetitions.

## Environment and dependencies

| Component | Observed | Declaration status | License metadata observed locally |
|---|---|---|---|
| Python | 3.13.7 | Repository README says 3.9+; exact version `VERSION_OBSERVED`, not pinned | NOT_APPLICABLE |
| pandas | 2.3.3 | `DECLARED_AND_USED`; `VERSION_UNPINNED` | BSD 3-Clause metadata observed via installed distribution |
| pydantic | 2.12.5 | `DECLARED_AND_USED`; range `>=2,<3`, exact version unpinned | MIT expression observed via installed distribution |

The successful run used user-level installed packages, not the repository's Unix-layout virtual environment. Transitive dependency versions were not captured. Dependency evidence is therefore `PARTIAL`, not a locked-environment claim.

## Observed outcome and comparison

Both captured runs exited 0. `OBSERVED_FROM_IMPLEMENTATION` matched every mandatory expected assertion: one trade, entry 100, take-profit exit 101, gross PnL 1, fees 0.0804, net PnL/final equity 0.9196, one win, no losses, win rate 1, expectancy and average win 0.9196, average loss and max drawdown 0.

Expected vs observed classification: `MATCH`. No `BEHAVIORAL_MISMATCH` occurred for the positive fixture.

Repeatability classification: `DETERMINISTIC_MATCH`. The two captured outputs were identical, including fixture hash, trade and metrics. This establishes deterministic behavior only for this controlled fixture and environment.

## Input/output contract and negative cases

Input verified: six required columns `timestamp, open, high, low, close, volume`; numeric OHLCV values are converted to floats. The loader preserves timestamp text at 1m ingestion and does not validate or reorder chronology.

Output verified: typed `BacktestResult` containing a list of typed `BacktestTrade` and typed `BacktestMetrics`; no file output was created by the simulator.

| Case | Observation | Classification |
|---|---|---|
| Missing `volume` | `ValueError: Missing required CSV columns: volume` | `EXPLICIT` |
| Empty simulator input | Zero trades and zero-valued finite metrics | `GRACEFUL_AT_SIMULATOR_BOUNDARY` |
| Reverse chronological input | Loader does not reorder; simulator operates positionally and still creates one fixture-dependent trade | `IMPLICIT`; chronological order is a documented prerequisite |

The full CLI empty-data path was not executed because it would expand beyond the minimal simulator/loader evidence. Its failure behavior remains `PARTIAL`.

## Provenance improvement

Before Phase C, provenance was `PARTIAL`: implementation/workflow references existed but controlled fixture identity, hash, command, environment and output were absent.

After Phase C, the controlled evidence chain is:

```text
ASSET-1 Candidate
→ Crypto origin main@751970757a9c3b876ec16f3afd57c13f65a7457f
→ operational boundary app/research/backtester.py + simulation.py + strategies/base.py
→ LabOS runner ebe5ecfe…
→ synthetic fixture 6477028d…
→ two exit-0 matching executions
→ this evidence document
→ independent Phase C review dated 2026-09-02
```

Candidate governance source of truth is this LabOS evidence package and its remediation-register entry; operational implementation remains the referenced Crypto repository/commit. `content_state` is recorded as `borrador`, independently of lifecycle, because technical evidence exists but licensing and broader validation remain incomplete.

Provenance for the controlled fixture is `PASS`; overall Asset provenance remains `PARTIAL` because project reuse rights, dependency lock and historical dataset/experiment lineage are outside or unresolved.

## Reproducibility and quality update

Controlled-fixture classification: `REPRODUCIBLE_WITH_DOCUMENTED_PREREQUISITES`. Prerequisites are Python 3.9+, compatible pandas/pydantic, Crypto commit above, LabOS fixture/runner hashes, chronological OHLCV, and the recorded command. This does not classify historical research as reproducible.

| Control affected by Phase C | Phase B | Phase C | Basis / residual limitation |
|---|---|---|---|
| Input contract | PARTIAL | PARTIAL | Required schema verified; chronology and semantic OHLC integrity remain assumptions |
| Failure behavior | PARTIAL | PARTIAL | Missing column explicit and empty simulator graceful; complete CLI/error surface not tested |
| Testing evidence | PARTIAL | PASS | Controlled loader/simulator/trade/metrics assertions passed twice for defined scope |
| Deterministic behavior | EVIDENCE_REQUIRED | PASS | Two identical controlled executions |
| Reproducibility | EVIDENCE_REQUIRED | PASS | For controlled fixture with documented prerequisites only |
| Traceability | PARTIAL | PASS | Commit, runner, fixture, hashes, command, environment and output linked |
| Provenance | PARTIAL | PARTIAL | Controlled chain complete; licensing and wider lineage remain open |

Unrelated quality controls, value `PROYECTADO`, `SAME_CONTEXT_REUSE` and `PROJECTED_REUSE` are unchanged.

## Licensing boundary, limitations and readiness

Synthetic data makes market-data licensing `NOT_APPLICABLE` to this correctness fixture. It does not resolve Binance rights for historical research. Locally installed pandas/pydantic license metadata is direct but partial evidence. Crypto still has `NO_ROOT_LICENSE_FOUND`; source reuse/redistribution rights and a complete third-party/transitive license manifest remain `UNKNOWN/PARTIAL`.

The controlled evidence supports software behavior only. It does not establish strategy correctness, profitability, alpha, robustness, absence of overfitting/look-ahead across experiments, live readiness or financial suitability.

Readiness: `READY_FOR_VALIDATION_DECISION_REVIEW`. The mandatory technical evidence targeted by Phase C is sufficient for independent review, and Tier 1 now has an explicit `borrador` content state and unique governed Candidate evidence source. Licensing remains an elevated restriction that must be evaluated by the independent decision reviewer and blocks external sharing/canonicalization while unresolved; it is not silently treated as satisfied. Readiness is neither recommendation nor lifecycle transition.
