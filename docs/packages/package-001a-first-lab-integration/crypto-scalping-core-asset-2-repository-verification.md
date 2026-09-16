# ASSET-2 — Repository Verification

Evidence 2026-08-25: Crypto main at 751970757a9c3b876ec16f3afd57c13f65a7457f; dirty state preexisting. STATIC + READ_ONLY; tests/experiments/Crypto writes 0; lifecycle UNCHANGED.

## Boundary, contract and traceability

IN_SCOPE: app/research/optimizer/grid_search.py and leaderboard.py. DEPENDENCY: ASSET-1 stack, diagnostics, Research Memory and experiment YAML. OUT_OF_SCOPE: artifacts and legacy app/optimization/grid_search.py (synthetic RSI/app.main flow without leaderboard persistence).

Entry: python -m app.research.optimizer.grid_search --config <yaml>. Trace: YAML/CLI parameters → product → strategy → simulate_strategy → metrics/diagnostics → sort by profit_factor/expectancy → row/CSV → journal/memory index. Traceability is PARTIAL: leaderboard rows omit experiment/config/commit/data hashes, paths may overwrite, persistence is non-atomic, and ties preserve grid enumeration rather than a declared semantic rule.

Python/pandas/pydantic and internal stack are DECLARED_AND_USED. PyYAML is OPTIONAL/USED_NOT_DECLARED with limited fallback; pytest is test-only USED_NOT_DECLARED; locked environment UNKNOWN. Software licensing PARTIAL with NO_ROOT_LICENSE_FOUND; market data RESTRICTED/UNKNOWN; broker/network NOT_APPLICABLE.

Tests cover config propagation, memory/journal linkage, no memory on optimizer failure, migration/import/duplicates and historical-import ties. No direct current E2E test covers product/filter/ranking ties/CSV round-trip/atomicity/replay. Tests were not run.

There are 12 current leaderboards, not historical Phase A 11: 9 tracked, 3 untracked. There are 13 YAMLs and 20 journals; journals 16–20 are untracked and memory/index.csv modified. This is USAGE_EVIDENCE only.

ACTUAL_USAGE, REPEATED_USAGE and SAME_CONTEXT_REUSE are supported. CROSS_CONTEXT_REUSE absent; PROJECTED_REUSE and PROYECTADO value remain. Same inputs/code/versions/order should be software-deterministic, but research stability is separate. No controlled replay/hashes: EXECUTION_EVIDENCE_REQUIRED.

Provenance source → ASSET-1/data/strategy → optimizer → configs/metrics/artifacts → Package 001A/KO-5 → Candidate → Package 003 → Phase A → Phase B is PARTIAL.

| Control | Status |
|---|---|
| Scope, inputs, outputs, usage, restrictions | PASS |
| Dependencies, failures, traceability, source of truth, testing | PARTIAL |
| Reproducibility | EVIDENCE_REQUIRED |

Current boundary/static contract remediation COMPLETE; licenses/deps/source PARTIAL; E2E determinism DEFERRED_PHASE_C. Readiness READY_FOR_PHASE_C_EVIDENCE.

Phase C: controlled config→grid→rank→CSV→memory fixture including ties/failures; artifact identity; governed source/content_state; dependency correction/version capture; licenses. Optimizer validation never implies profitability, alpha, absence of overfitting/look-ahead, live readiness or suitability.

## Re-verification — 2026-09-02

The repository was re-inspected at the same commit `751970757a9c3b876ec16f3afd57c13f65a7457f` on branch `main`. No source, test, configuration or dependency-declaration delta exists from the 2026-08-25 evidence baseline. The current 12 leaderboards and 20 journals remain 9/15 tracked and 3/5 untracked respectively; the modified memory index and research outputs are `USAGE_EVIDENCE`, not correctness or reproducibility evidence.

Execution classification: inventory, Git metadata, imports, contracts and artifact headers were `SAFE_READ_ONLY`. No optimizer, test or experiment was run. End-to-end config → parameter product → execution → metrics → ranked row → CSV → journal/memory verification remains `DEFERRED_EXECUTION_REQUIRED` for Phase C.
