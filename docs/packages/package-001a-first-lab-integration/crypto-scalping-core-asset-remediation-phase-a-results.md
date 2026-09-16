# Crypto Scalping Core — Asset Remediation Phase A Results

## Execution record

| Campo | Resultado |
|---|---|
| Authorization | `FD-ASSET-REM-A-001` |
| Repository | `CRYPTO_REPOSITORY_ACCESSIBLE`, read-only |
| Crypto branch | `main` — `DIRECTLY_VERIFIED` via `.git/HEAD` |
| Crypto writes / commands / tests | 0 / 0 / 0 |
| Lifecycle transitions | 0 |
| Candidates promoted/canonicalized | 0 / 0 |
| Package 004 | `NOT_AUTHORIZED` |

## Evidence directly verified

- ASSET-1 paths exist: `app/research/backtester.py` and `simulation.py`; visible contracts show strategy, features, config and pandas/pydantic dependencies.
- ASSET-2 path exists: `app/optimization/grid_search.py`; visible imports confirm coupling to `app.main`, RSI strategy and logging.
- ASSET-4 has seven Python modules plus package cache under `app/research/discovery/`.
- ASSET-5 has `features.py` and `scoring.py` under `app/research/signal_quality/`.
- `research/journal/` contains 19 experiment records. Eleven headings are common to all 19.
- `research/leaderboards/` contains 11 CSV leaderboards; reports include discovery and quality-analysis outputs plus newer research records.
- `.git/HEAD` points to `refs/heads/main`.
- `requirements.txt` is mostly unpinned and contains third-party dependencies; root `LICENSE` is absent.

These checks establish current existence/structure only. They do not establish reproducibility, correctness, reuse, licensing or live-trading readiness.

## Before / actions / after

### ASSET-3 — Tier A

| Before Phase A | Phase A actions | After Phase A |
|---|---|---|
| Distance `NEAR`; 2/5 dimensions satisfied; no template/source, owner or concrete Forma B | AR-AS3-01, 02 and 04 COMPLETE; direct comparison of 19 journals; sanitized Candidate template; ownership; Tier 1 8/8; duplicate search; specific projected domain/scenario; LOW structural restriction | Five qualification dimensions have sufficient evidence for a human review; provenance `COMPLETE`; value `PROYECTADO`; reuse `PROJECTED_REUSE`; no demonstrated reuse; no lifecycle change |

- Resolved: Candidate identity, ownership, unique Candidate content source, provenance mapping, sensitivity boundary, Tier 1, duplicate check, projected reuse statement and 90-day trigger rule.
- Remaining: AR-AS3-03 dry-run/demonstrated reuse is optional Phase C evidence; a human Asset Validation Decision has not occurred.
- Distance after: `NEAR` — unchanged because readiness improved but lifecycle decision remains.
- Workflow readiness: `READY_FOR_VALIDATION_DECISION_REVIEW`.

### ASSET-1 — Tier B

| Before Phase A | Phase A actions | After Phase A |
|---|---|---|
| Distance `MODERATE`; provenance only satisfied; 4/5 dimensions failed | AR-AS1-01/04 PARTIAL; direct path/import verification; ownership; provenance/source layers; projected reuse scenario; duplicate audit; risk/licensing classification | Reuse projected, provenance and ownership now documented; quality and Candidate source remain unsatisfied; Tier 1 6/8; licensing/dependency evidence incomplete |

- Resolved: human owner, owning Lab, current branch/path existence, concrete projected scenario, governance/provenance map, current restrictions and no-duplicate evidence in LabOS records.
- Remaining: content_state, single Candidate source boundary, static contract review, reproducibility/correctness, dependencies and external licenses.
- Distance after: `MODERATE` — unchanged.
- Workflow readiness: `READY_FOR_REPOSITORY_VERIFICATION`.

### ASSET-2 — Tier B

| Before Phase A | Phase A actions | After Phase A |
|---|---|---|
| Distance `MODERATE`; provenance only; historical 14+ internal runs | AR-AS2-01/04 PARTIAL; direct file/import and current output inventory; ownership/provenance/scenario/duplicate/risk mapping | Current code/output existence verified; reuse remains projected; quality/source/Tier 1 incomplete; licensing/dependencies unresolved |

- Resolved: owner, Lab, branch/path, provenance references, concrete projected scenario, restrictions and duplicate audit. Current evidence is 19 journals and 11 leaderboards; this supersedes counts for freshness only, not historical records.
- Remaining: content_state, governed Candidate source/contract, deterministic optimization evidence, parameter traceability test, dependency/license verification.
- Distance after: `MODERATE` — unchanged.
- Workflow readiness: `READY_FOR_REPOSITORY_VERIFICATION`.

### ASSET-4 — Tier C

| Before Phase A | Phase A actions | After Phase A |
|---|---|---|
| Distance `FAR`; integrated pipeline, provenance only | AR-AS4-01/04 PARTIAL; module/report existence, owner, provenance/scenario/source layers, restrictions | Documentation clearer; no generic boundary or correctness evidence; licensing/claims remain elevated |

- Resolved: owner, origin/branch/module inventory, provenance chain, projected scenario, duplicate audit and explicit correlation/non-causality restriction.
- Remaining: Tier 1 content_state/source unit, static schema contract, controlled report test, lineage per output and external licensing.
- Distance after: `FAR` — unchanged.
- Workflow readiness: `READY_FOR_REPOSITORY_VERIFICATION`.

### ASSET-5 — Tier C

| Before Phase A | Phase A actions | After Phase A |
|---|---|---|
| Distance `FAR`; integrated methodology and elevated risk | AR-AS5-01/04 PARTIAL; direct module/report existence, owner, provenance/scenario/restrictions | Evidence map improved; method boundary, correctness, leakage/overfitting/staleness and data rights remain open |

- Resolved: owner, origin/branch/path, provenance chain, projected scenario, duplicate audit and prohibition on profitability/live-readiness inference.
- Remaining: Tier 1 content_state/source, static method/adapter boundary, controlled calculations, independent evidence and licensing.
- Distance after: `FAR` — unchanged.
- Workflow readiness: `READY_FOR_REPOSITORY_VERIFICATION`.

## Qualification and value after Phase A

| Candidate | Reuse | Quality | Provenance | Ownership | Source of truth | Value | Workflow readiness |
|---|---|---|---|---|---|---|---|
| ASSET-1 | `SATISFECHA` Forma B | `NO_SATISFECHA` | `SATISFECHA` | `SATISFECHA` | `NO_SATISFECHA` | `PROYECTADO` | `READY_FOR_REPOSITORY_VERIFICATION` |
| ASSET-2 | `SATISFECHA` Forma B | `NO_SATISFECHA` | `SATISFECHA` | `SATISFECHA` | `NO_SATISFECHA` | `PROYECTADO` | `READY_FOR_REPOSITORY_VERIFICATION` |
| ASSET-3 | `SATISFECHA` Forma B | `SATISFECHA` — prior + current structure evidence | `SATISFECHA` | `SATISFECHA` | `SATISFECHA` | `PROYECTADO` | `READY_FOR_VALIDATION_DECISION_REVIEW` |
| ASSET-4 | `SATISFECHA` Forma B | `NO_SATISFECHA` | `SATISFECHA` | `SATISFECHA` | `NO_SATISFECHA` | `PROYECTADO` | `READY_FOR_REPOSITORY_VERIFICATION` |
| ASSET-5 | `SATISFECHA` Forma B | `NO_SATISFECHA` | `SATISFECHA` | `SATISFECHA` | `NO_SATISFECHA` | `PROYECTADO` | `READY_FOR_REPOSITORY_VERIFICATION` |

Forma B was documented with a destination domain and concrete scenario; it is not demonstrated reuse. These qualification results prepare a future review and do not change lifecycle.

## ASSET-3 decision gate

`ASSET-3_READY_FOR_VALIDATION_DECISION_REVIEW`

Rationale: Candidate content/source now exists, Tier 1 is 8/8, all five dimensions have referenced evidence, exposure is Level 1 with LOW structural risk, and no VALIDATED/CANONICAL duplicate was found. A separate human review must still verify the package and explicitly decide. AR-AS3-03 may add demonstrated reuse later but is not a prerequisite under Forma B.

## Trigger check

| Control | Result |
|---|---|
| Assets in `VALIDATED` | 0 |
| Candidates ready for validation decision review | 1 — ASSET-3 |
| Candidates counted toward P004 trigger | 0 |
| P004 trigger | `NOT_SATISFIED` |

## Scope integrity

No lifecycle, promotion, canonicalization, Package 003 rule, P004 trigger, Product hypothesis or Product Factory work changed. `REMEDIATION_SCOPE_VIOLATION`: 0.
