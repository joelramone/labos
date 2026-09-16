# Crypto Scalping Core — Asset Remediation Phase C Results

Scope: `ASSET-1 ONLY`. Authorization: `ASSET_REMEDIATION_PHASE_C_CONTROLLED_EVIDENCE_PREPARATION` / `FOUNDER_DECISION`. Date: 2026-09-02.

## Outcome

| Field | Result |
|---|---|
| Execution safety | `SAFE_CONTROLLED_TEST` |
| Fixture | Three synthetic OHLCV bars; SHA-256 `6477028df7b39764100e6e22e3f32ac96feb9c36f0645ff5bafc4b3ccd161bb8` |
| Successful repetitions | 2, exit 0 |
| Expected vs observed | `MATCH` |
| Repeatability | `DETERMINISTIC_MATCH` |
| Behavioral mismatch | NONE for positive fixture |
| Reproducibility | `REPRODUCIBLE_WITH_DOCUMENTED_PREREQUISITES` for controlled fixture only |
| Research / optimizer / trading / network | 0 / 0 / 0 / 0 |
| Crypto writes | 0 |
| Lifecycle transitions | 0 |
| Readiness | `READY_FOR_VALIDATION_DECISION_REVIEW` |

Expected and observed: one entry at 100, take-profit exit at 101, notional 100, gross PnL 1, fees 0.0804, net PnL/final fixture equity 0.9196, one win, no losses, expectancy 0.9196 and max drawdown 0. Both runs matched.

## Remediation execution

| Remediation | BEFORE | ACTION | EVIDENCE | AFTER | STATUS |
|---|---|---|---|---|---|
| AR-AS1-01 | `content_state` and governed Candidate source open | Recorded `borrador` independently of lifecycle and selected one LabOS evidence package as governed Candidate source | Controlled evidence document + register; Crypto operational boundary remains referenced | Tier 1 metadata gap closed for review preparation; lifecycle unchanged | COMPLETE |
| AR-AS1-03 | Correctness and reproducibility evidence absent | Defined expected results independently; ran bounded synthetic fixture twice; checked one missing-column case plus empty/order behavior | Fixture/runner hashes, exit-0 output, exact environment/command | Controlled behavior and repeatability evidenced; full historical research not covered | COMPLETE |
| AR-AS1-04 | Exact runtime versions and licenses incomplete | Captured Python/pandas/pydantic versions and installed license metadata | Python 3.13.7; pandas 2.3.3/BSD-3; pydantic 2.12.5/MIT metadata | Direct-run dependencies improved; root/transitive/data rights remain open | PARTIAL |

## Quality and remaining gaps

Testing evidence, controlled determinism, controlled reproducibility and execution traceability are `PASS`. Input contract and failure behavior remain `PARTIAL` due chronology/OHLC semantics and untested full-CLI edge behavior. Overall provenance remains `PARTIAL` beyond the now-complete controlled chain. Licensing remains `PARTIAL/UNKNOWN` and must be explicitly handled by the decision reviewer.

Value remains `PROYECTADO`; reuse remains `SAME_CONTEXT / PROJECTED_REUSE`. No financial conclusion is produced.

ASSET-2 Phase C: `NOT_AUTHORIZED / NOT_EXECUTED`.

P004 remains 1/3 `VALIDATED`, `NOT_SATISFIED`; Package 004 remains `NOT_AUTHORIZED`.

## ASSET-2 controlled evidence — 2026-09-02

Scope: ASSET-2 only under `ASSET_2_PHASE_C_CONTROLLED_EVIDENCE_PREPARATION`. Crypto moved from the Phase B commit to `a86464448c2789b3d7278eaaaffb85666c518602`; optimizer source files are unchanged, while the ASSET-1 dependency added direction support. Impact was assessed before execution.

| Control | Result |
|---|---|
| Safety | `SAFE_CONTROLLED_TEST` |
| Grid | 4 expected / 4 observed; `GRID_ENUMERATION_MATCH` |
| Metrics/ranking | Expected propagation and order; `RANKING_MATCH` |
| Tie | `DETERMINISTIC_UNDOCUMENTED_TIE_BEHAVIOR` |
| CSV | 77 columns, 4 rows, SHA-256 `ad6e5254…` |
| Replay | `REPLAY_MATCH` |
| Determinism | `DETERMINISTIC_MATCH` across two exit-0 runs |
| Negative cases | Empty grid explicit ValidationError; execution failure explicitly propagated |
| Research/trading/network/Crypto writes | 0 / 0 / 0 / 0 |
| Reproducibility | `REPRODUCIBLE_WITH_DOCUMENTED_PREREQUISITES`, controlled fixture only |
| Readiness | `READY_FOR_VALIDATION_DECISION_REVIEW` |

| Remediation | BEFORE | ACTION | EVIDENCE | AFTER | STATUS |
|---|---|---|---|---|---|
| AR-AS2-01 | Governed source/content state open | Selected unique LabOS evidence package; recorded `content_state=borrador`; anchored operational source to current commit | Evidence document + register | Candidate metadata ready for independent review | COMPLETE |
| AR-AS2-03 | Grid/ranking/leaderboard replay absent | Predeclared 2×2 grid and metrics; executed actual enumeration/ranking/serialization twice with controlled execution stub | Config/runner/output hashes and identical exit-0 results | Controlled E2E responsibility evidenced | COMPLETE |
| AR-AS2-04 | Dependencies/licensing partial | Captured Python, pandas, pydantic and PyYAML versions/license metadata | Installed metadata; requirements comparison | Evidence improved; PyYAML declaration, locks, transitives and project/data rights open | PARTIAL |

ASSET-2 lifecycle remains `CANDIDATE`. Value/reuse remain projected/same-context. Historical leaderboards remain usage evidence only. ASSET-1 and ASSET-3 remain `VALIDATED / NOT_CANONICAL`; P004 remains 2/3 and `NOT_SATISFIED`.
