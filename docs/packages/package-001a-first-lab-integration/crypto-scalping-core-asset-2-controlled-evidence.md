# ASSET-2 — Controlled Optimizer Evidence

## Control record

| Field | Value |
|---|---|
| Authorization | `ASSET_2_PHASE_C_CONTROLLED_EVIDENCE_PREPARATION` / `FOUNDER_DECISION` |
| Date | 2026-09-02 |
| Candidate | `ASSET-2` — Optimizador de parámetros por grid search con leaderboard |
| Crypto branch / commit | `main` / `a86464448c2789b3d7278eaaaffb85666c518602` |
| Prior evidence commit | `751970757a9c3b876ec16f3afd57c13f65a7457f` |
| Source version status | `SOURCE_VERSION_CHANGED` |
| Lifecycle | `CANDIDATE / UNCHANGED` |

## Source-version and boundary assessment

The current commit differs from Phase B. Direct diff inspection found no change in `app/research/optimizer/grid_search.py` or `leaderboard.py`; changes relevant to the dependency boundary were limited to ASSET-1 `simulation.py` and `strategies/base.py`, adding long/short direction support with a default long direction. The controlled ASSET-2 stub does not depend on direction behavior. Phase B optimizer contract remains current for this test, but all Phase C identity is anchored to `a864644…`.

Boundary remains:

- IN_SCOPE: `app/research/optimizer/grid_search.py`, `app/research/optimizer/leaderboard.py`.
- DEPENDENCY: ASSET-1 models/metric calculation, diagnostics, Research Memory, YAML/configuration.
- OUT_OF_SCOPE: historical leaderboards/journals, real strategies/research and legacy `app/optimization/grid_search.py`.

## Controlled fixture and expected results

The validation fixture uses the actual `GridSearchConfig` parameter schema and the real optimizer/leaderboard functions. A LabOS-only `ControlledGridStrategy` accepts the actual parameter names. Strategy execution is replaced only at the ASSET-1 call boundary by a deterministic function returning two internally consistent synthetic trades whose metrics are calculated by the real ASSET-1 metric function. No real strategy or research data is executed.

| Artifact | SHA-256 |
|---|---|
| Config `tests/asset-validation/asset-2-controlled-config.yaml` | `b3091755bec8af73dd89f4d1a0f784180badf17a4512fcafb676b3d7c00b78e0` |
| Executable fixture/runner `tests/asset-validation/asset-2-controlled-evidence-runner.py` | `543507aafc302f6116f5cce6b5d9eb5ca855d94c511009bb58bc5d46b8386082` |
| Controlled leaderboard CSV | `ad6e52542ccc97ea4d795ff7277fd19d35e40717548fd7cdcbe0624db5e7e4ea` |

Expected combinations and metrics were declared before execution:

| Enumeration | Parameters | Expected PF | Expected expectancy | Expected rank |
|---:|---|---:|---:|---:|
| 1 | TP 0.01 / SL 0.005 | 1.5 | 0.2 | 4 |
| 2 | TP 0.01 / SL 0.01 | 2.0 | 0.1 | 3 |
| 3 | TP 0.02 / SL 0.005 | 2.0 | 0.3 | 1 |
| 4 | TP 0.02 / SL 0.01 | 2.0 | 0.3 | 2 |

Ranking specification observed statically before execution: descending tuple `(profit_factor, expectancy)`. Python stable sort preserves enumeration order for the rank-1/rank-2 exact tie.

## Safety, command and environment

Classification before execution: `SAFE_CONTROLLED_TEST`. Synthetic/in-memory inputs only; no network, credentials, Binance, trading, paper trading, optimizer CLI, research pipeline, real datasets, journals or historical leaderboards. CSV output is a LabOS validation artifact.

Command executed twice:

```text
set PYTHONDONTWRITEBYTECODE=1& set PYTHONPATH=C:\Users\jd0519\Documents\Personal\crypto-scalping-core& python tests\asset-validation\asset-2-controlled-evidence-runner.py tests\asset-validation\asset-2-controlled-config.yaml
```

| Dependency | Observed | Declaration / license evidence |
|---|---|---|
| Python | 3.13.7 | VERSION_OBSERVED; exact version unpinned |
| pandas | 2.3.3 | DECLARED_AND_USED; VERSION_UNPINNED; BSD-3 metadata observed |
| pydantic | 2.12.5 | DECLARED_AND_USED; declared `>=2,<3`; MIT metadata observed |
| PyYAML | 6.0.3 | OPTIONAL / USED_NOT_DECLARED; MIT metadata observed |

Transitive versions and full licenses remain incomplete. No dependency file was changed.

## Observed results

Both runs exited 0 and produced:

- 4 expected combinations and 4 evaluated configurations;
- 4 ranked results and 4 serialized rows;
- exact expected metric propagation and rank order;
- 77 CSV columns equal to `LEADERBOARD_COLUMNS`;
- identical CSV SHA-256 `ad6e5254…`.

Verdicts:

- Grid enumeration: `GRID_ENUMERATION_MATCH`.
- Metrics propagation: PASS.
- Ranking: `RANKING_MATCH`.
- Tie: `DETERMINISTIC_UNDOCUMENTED_TIE_BEHAVIOR`.
- Replay: `REPLAY_MATCH`.
- Software determinism: `DETERMINISTIC_MATCH`.

The tiny floating representations `0.20000000000000007` and `1.5000000000000002` were accepted under the predeclared numeric tolerance; expected ranking and CSV replay were not changed to accommodate output.

Research-result stability is NOT_APPLICABLE to this controlled software fixture and remains unassessed.

## Leaderboard and failure contracts

The controlled CSV preserves rank order, strategy/timeframe, metrics, diagnostics and parameter fields. Every input combination maps to one result and one row because `min_trades=0` and no controlled run is filtered. The output path is outside Crypto research directories.

| Negative case | Observation | Classification |
|---|---|---|
| Empty `parameters` in `GridSearchConfig` | Pydantic `ValidationError` | EXPLICIT / GRACEFUL |
| Controlled execution raises | `RuntimeError: controlled execution failure` propagates; no summary/CSV written for that invocation | EXPLICIT_PROPAGATED |
| Missing metric | Not executed; required `BacktestMetrics` fields are model-required | PARTIAL / model validation only |

Failure behavior is `PARTIAL`: invalid config and failed execution are explicit, but recovery, partial-run persistence and atomic file writing remain outside this fixture.

## Traceability and output identity

Controlled chain:

```text
Crypto main@a864644…
→ ASSET-2 source boundary
→ config b3091755…
→ executable fixture 543507aa…
→ 4 explicit parameter combinations
→ synthetic executions + actual metric models
→ actual ranking/row construction
→ controlled CSV ad6e5254…
→ two identical executions
→ this evidence document and independent review
```

Controlled traceability: `PASS`. Historical leaderboard traceability remains `PARTIAL`; Phase C does not retroactively add hashes, commits or config identity to prior artifacts. Persistence remains non-atomic and an existing target can be overwritten.

Output identity/replay: `REPLAY_MATCH`. The commit, config, runner, parameter order, environment and output hash uniquely identify the controlled evidence package.

## Reproducibility and quality update

Classification: `REPRODUCIBLE_WITH_DOCUMENTED_PREREQUISITES`, for the controlled optimizer fixture only. Prerequisites are the recorded commit, config/runner hashes, Python with compatible dependencies, insertion-preserving parameter order and the exact command.

| Control | Phase B | Phase C | Residual limitation |
|---|---|---|---|
| Grid enumeration | EVIDENCE_REQUIRED | PASS | Parameter dictionary order is significant |
| Execution count | EVIDENCE_REQUIRED | PASS | Controlled no-filter case only |
| Metrics propagation | PARTIAL | PASS | Metric correctness belongs to ASSET-1; controlled values only |
| Ranking | EVIDENCE_REQUIRED | PASS | Descending PF then expectancy |
| Tie behavior | PARTIAL | PASS_WITH_RESTRICTION | Stable enumeration order is not declared as a semantic contract |
| Leaderboard serialization | PARTIAL | PASS | Controlled 77-column/4-row CSV |
| Traceability | PARTIAL | PASS | Controlled package only; historical outputs unchanged |
| Replay/determinism | EVIDENCE_REQUIRED | PASS | Same source/config/order/environment only |
| Failure behavior | PARTIAL | PARTIAL | Atomicity/recovery/missing metric path incomplete |
| Dependencies | PARTIAL | PARTIAL | PyYAML used-not-declared; versions/transitives unpinned |
| Provenance | PARTIAL | PARTIAL | Controlled chain complete; global research/licensing incomplete |

## Limitations, licensing and readiness

Validation does not establish profitable parameters, strategy profitability, alpha, robustness, parameter optimality, absence of overfitting, OOS/walk-forward validity, live readiness or financial suitability.

Software dependency licensing remains PARTIAL; Crypto project source is `UNKNOWN / NO_ROOT_LICENSE_FOUND`; historical market-data licensing is `UNKNOWN / RESTRICTED`; synthetic controlled data is `NOT_APPLICABLE` to external market-data licensing. No license conclusion is upgraded.

Value remains `PROYECTADO`. Usage remains `ACTUAL_USAGE / REPEATED_USAGE / SAME_CONTEXT_REUSE`; reuse remains `PROJECTED_REUSE`; cross-context/demonstrated reuse remains NO.

Candidate governance source of truth is this LabOS evidence package and register entry; operational implementation remains Crypto `main@a864644…`. `content_state=borrador`, independent of lifecycle.

Readiness: `READY_FOR_VALIDATION_DECISION_REVIEW`. The targeted technical evidence is sufficient for independent review. Tie semantics, failure/persistence behavior, dependency declaration/licensing and global provenance remain explicit restrictions for that reviewer. Readiness is not recommendation or lifecycle transition.
