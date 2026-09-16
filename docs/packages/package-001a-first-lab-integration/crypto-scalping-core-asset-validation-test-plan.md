# Crypto Scalping Core — Asset Validation Test Plan

## Scope

Este documento especifica evidencia para futuros reviews; no ejecuta tests, investigación, lifecycle transitions ni promotion. Las clasificaciones `READY_*` son workflow states locales, no estados de Package 003.

## Phase B — repository verification, no execution authorized

| Candidate | Exact files/directories | Read-only checks | Expected evidence |
|---|---|---|---|
| ASSET-1 | `app/research/backtester.py`, `simulation.py`, `strategies/`, `config.py`, `data_utils.py`, `features.py`, `results.py`; tests relacionados | Mapear public contract, strategy/data coupling, inputs/outputs/errors, existing test coverage and fixture references | Static boundary report; candidate unit decision; dependency graph; existing-test inventory |
| ASSET-2 | `app/optimization/grid_search.py`, `app/main.py`, relevant strategies/configs, `research/leaderboards/` | Mapear grid source, parameter lineage, ranking/output schema, environment variables, deterministic ordering and existing tests | Interface/schema report; parameter-to-leaderboard trace; candidate source boundary |
| ASSET-3 | Candidate template + 19 `research/journal/EXP-*.md` | Reconfirm 11 common sections, placeholder completeness, absence of copied sensitive values and relative provenance links | Template schema/checklist report; no execution required |
| ASSET-4 | `app/research/discovery/*.py`, `research/reports/discovery_report.md`, `research/leaderboards/` | Mapear loaders, schemas, aggregation, correlations, report generation, path assumptions and claim language | Module/dataflow map; candidate boundary; list of calculations requiring Phase C |
| ASSET-5 | `app/research/signal_quality/*.py`, quality reports, candidate signals | Mapear feature/scoring formulas, adapters, inputs/outputs, leakage surfaces, assumptions and claims | Method/dataflow map; candidate boundary; list of calculations requiring Phase C |

### CMD-compatible command examples — planning only

These examples are not executed by this plan:

```bat
cmd /c type app\research\backtester.py
cmd /c type app\optimization\grid_search.py
cmd /c dir /s /b app\research\discovery\*.py
cmd /c dir /s /b app\research\signal_quality\*.py
cmd /c dir /b research\journal\EXP-*.md
cmd /c findstr /s /n /i "def class import" app\research\*.py app\optimization\*.py
```

All commands must run from the Crypto repository under a separately authorized read-only Phase B. Commands that execute code, tests or write caches are excluded.

## Exact future validation evidence packages

### ASSET-3

| Criterion | Required evidence | Gate |
|---|---|---|
| Candidate intake | Tier 1 8/8 and unique name/source | Schema/field-count check |
| Reuse | Forma B destination + concrete scenario; demonstrated reuse optional | Qualification review |
| Quality | 19-instance structure comparison; five base fields; dated reviewer/owner validation | Document/schema review |
| Provenance | Journal list → extracted template → Candidate/evaluation references | Cross-reference validation |
| Risk/restrictions | No private result copied; Dataset placeholder demands restriction | Risk gate Level 1 |
| Duplicate | Search VALIDATED/CANONICAL registry | Duplicate audit |
| Decision | Human record citing all evidence | `ASSET_VALIDATION_DECISION_REVIEW` — not executed |

### ASSET-1

| Criterion | Required evidence | Phase |
|---|---|---|
| Boundary/source | One governed unit and explicit public contract | B |
| Reproducibility | Authorized fixed fixture; inputs/config/version; repeat result | C |
| Correctness | Independently calculated PF, expectancy, drawdown and trade accounting | C |
| Dependencies | Versioned environment and stable dependency inventory | B/C |
| Reuse | Existing Forma B; actual external use optional for VALIDATED | A/C |
| Risk | Financial-use limits, no profitability/live claim, data/code licenses | C |

### ASSET-2

| Criterion | Required evidence | Phase |
|---|---|---|
| Boundary/source | Strategy-neutral or explicitly bounded optimization contract | B |
| Reproducibility | Authorized fixed parameter grid and fixture | C |
| Correctness | Combination count, parameter traceability, ranking and leaderboard schema | C |
| Dependencies | Backtester/strategy/config/version map | B/C |
| Reuse | Existing Forma B; internal runs support quality only | A/C |
| Risk | Overfitting warning, input/output restrictions and licenses | C |

### ASSET-4

Required package: static module/schema map (B); allowed fixture with known aggregations/rankings/correlations (C); report claim review that distinguishes correlation from causality (C); per-output provenance and licensing (C); owner/source/Tier 1 completion. A failing generic-boundary test may justify `NOT_AN_ASSET` rather than further extraction.

### ASSET-5

Required package: static formula/data-adapter map (B); controlled calculations for features, buckets and scores (C); leakage/overfitting/staleness review (C); independent/non-restricted evidence where applicable (C); licensing and strict non-profitability/non-live boundary. A methodology claim must be evaluated separately from strategy performance.

## Phase C — new/external evidence, not authorized

| Evidence class | Candidates | Required action |
|---|---|---|
| Licensing/Terms | ASSET-1,2,4,5 | Verify current Binance data terms, repository code rights and third-party package licenses; preserve dated source references |
| Reproducibility | ASSET-1,2 | Run authorized fixed fixtures; record environment, inputs, outputs and expected values |
| Research validity | ASSET-4,5 | Controlled evidence for synthesis/method correctness, non-causality, leakage, overfitting and staleness |
| Demonstrated reuse/dry-run | ASSET-3; optional for others | Use outside origin with date/context/result; never backfill or infer |
| Dependency integrity | ASSET-1,2,4,5 | Verify versions, compatibility and failure behavior in an authorized environment |

## Phase D — validation decision, not authorized

For each Candidate, the human reviewer must receive Tier 1, five-dimension evaluation, source/provenance, duplicate audit, effective exposure/risk gate and unresolved restrictions. Outcomes may retain CANDIDATE/UNDER_REVIEW or recommend remediation. No template, script or AI may change lifecycle automatically.
