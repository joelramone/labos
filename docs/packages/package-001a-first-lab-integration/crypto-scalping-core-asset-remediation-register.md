# Crypto Scalping Core — Asset Remediation Register

## Control del registro

| Campo | Valor |
|---|---|
| Register ID | `CSC-ASSET-REMEDIATION-001` |
| Fecha efectiva | 2026-08-24 |
| Reference Lab | `LABOS-REF-LAB-0001` |
| Governance authority | Package 003 — CLOSED; reglas sin modificar |
| Operational owner | Joel Diaz / Lab Founder |
| Owning Lab | Crypto Scalping Core |
| Authorization | `FD-ASSET-REM-A-001` — Phase A only |
| Lifecycle transitions | 0; `NONE_AUTHORIZED` |
| Package 004 | `NOT_AUTHORIZED` |

Este registro es la source of truth operacional para el estado de las remediaciones. No sustituye el [assessment histórico de Package 003](../package-003-asset-system/crypto-scalping-core-asset-candidate-assessment.md), el source artifact de cada Candidate ni el repositorio Crypto.

## Evidence vocabulary

| Clase | Uso |
|---|---|
| `DIRECTLY_VERIFIED` | Leído en el repositorio Crypto accesible durante Phase A, sin ejecutar ni modificar |
| `DOCUMENTED_PRIOR_EVIDENCE` | Evidencia registrada por Package 001A/003; no equivale a inspección actual |
| `FOUNDER_DECISION` | Decisión explícita `FD-ASSET-REM-A-001` |
| `INFERRED` | Conclusión declarada que requiere confirmación antes de ser gate evidence |
| `EVIDENCE_REQUIRED` | Evidencia ausente o no autorizada en Phase A |

## Input reconciliation

[Hecho] Los 20 Remediation IDs del [trigger evidence review](../../architecture/package-004-activation-trigger-evidence-review.md) existen una sola vez: 8 SMALL, 8 MEDIUM y 4 LARGE.

`ASSET_REMEDIATION_INPUT_CONFLICT` resuelto por autoridad normativa:

- Crypto es ahora `CRYPTO_REPOSITORY_ACCESSIBLE`; branch directamente verificado: `main`.
- Existen 19 journals y 11 leaderboards, frente a 14/8 en el inventario histórico. El histórico no se reescribe; la diferencia se registra como freshness.
- `AR-AS3-03` no bloquea por sí solo `VALIDATED`: Package 003 acepta Forma B `PROJECTED_REUSE` con dominio y escenario concretos. El dry-run queda como evidencia adicional Phase C, no como dimensión obligatoria.

## Master remediation register

| Remediation ID | Candidate | Description / source finding | Evidence required | Owner | Effort | Dependency | External evidence | Crypto modification | Research | Founder decision | Blocks VALIDATED | Execution phase | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AR-AS1-01 | ASSET-1 | Formalizar Tier 1, source, owner y duplicate audit; P003 halló source/owner incompletos | Tier 1 8/8, owner acceptance, source unit, registry search | Joel Diaz | SMALL | Candidate boundary | NO | NO | NO | YES — satisfied | YES, por source/Tier 1 restante | PHASE_A_LABOS_ONLY → B | `PARTIAL_PHASE_A`: owner, provenance, scenario y duplicate audit completos; content_state/source unit pendientes |
| AR-AS1-02 | ASSET-1 | Delimitar motor reusable frente a strategies/data | Static boundary + contract evidence | Joel Diaz | MEDIUM | AS1-01 | NO | NO para inspección; posible cambio futuro sí | NO | NO | YES | PHASE_B_REPOSITORY_VERIFICATION | `DEFERRED_NOT_AUTHORIZED` |
| AR-AS1-03 | ASSET-1 | Correctness/reproducibility de métricas | Fixture permitido, expected metrics, owner checklist | Joel Diaz | MEDIUM | AS1-02 | NO | Posible | YES — validation evidence | NO | YES | PHASE_C_NEW_EVIDENCE | `DEFERRED_NOT_AUTHORIZED` |
| AR-AS1-04 | ASSET-1 | Licensing/dependencies/misuse | Licencias actuales y dependency manifest verificable | Joel Diaz | MEDIUM | AS1-02 | YES | NO | NO | NO | YES | PHASE_A_LABOS_ONLY → C | `PARTIAL_PHASE_A`: restrictions preservadas; licencia externa/dependencies pendientes |
| AR-AS2-01 | ASSET-2 | Formalizar Tier 1, source, owner y duplicate audit | Tier 1, source unit, owner, duplicate search | Joel Diaz | SMALL | Candidate boundary | NO | NO | NO | YES — satisfied | YES | PHASE_A_LABOS_ONLY → B | `PARTIAL_PHASE_A` |
| AR-AS2-02 | ASSET-2 | Verificar contract desacoplado | Static interface/input/output boundary | Joel Diaz | MEDIUM | AS2-01 | NO | NO para inspección | NO | NO | YES | PHASE_B_REPOSITORY_VERIFICATION | `DEFERRED_NOT_AUTHORIZED` |
| AR-AS2-03 | ASSET-2 | Reproducir grid/ranking/leaderboard | Authorized fixture, deterministic expected output | Joel Diaz | MEDIUM | AS2-02 | NO | Posible | YES — validation evidence | NO | YES | PHASE_C_NEW_EVIDENCE | `DEFERRED_NOT_AUTHORIZED` |
| AR-AS2-04 | ASSET-2 | Overfitting/licensing/dependencies | Intended-use limits, current terms, pinned/recorded dependencies | Joel Diaz | MEDIUM | AS2-02 | YES | NO | NO | NO | YES | PHASE_A_LABOS_ONLY → C | `PARTIAL_PHASE_A` |
| AR-AS3-01 | ASSET-3 | No existía template/source único | Template limpio, no sensible, con source verificable | Joel Diaz | SMALL | 19 journals | NO | NO | NO | NO | YES | PHASE_A_LABOS_ONLY | `COMPLETE_PHASE_A` |
| AR-AS3-02 | ASSET-3 | Tier 1/owner/duplicate audit | Record 8/8, owner acceptance, search | Joel Diaz | SMALL | AS3-01 | NO | NO | NO | YES — satisfied | YES | PHASE_A_LABOS_ONLY | `COMPLETE_PHASE_A` |
| AR-AS3-03 | ASSET-3 | Dry-run en segundo contexto propuesto | Uso externo o dry-run documentado | Joel Diaz | SMALL | AS3-01 | NO | NO | YES | NO | NO para review usando Forma B; sí para demonstrated reuse | PHASE_C_NEW_EVIDENCE | `DEFERRED_OPTIONAL_NOT_AUTHORIZED` |
| AR-AS3-04 | ASSET-3 | Sensitivity boundary y Forma B review trigger | Sanitization check, destino/escenario, trigger 90 días | Joel Diaz | SMALL | AS3-01 | NO | NO | NO | NO | YES | PHASE_A_LABOS_ONLY | `COMPLETE_PHASE_A` |
| AR-AS4-01 | ASSET-4 | Formalizar Tier 1, source, owner y duplicate audit | Tier 1, owner, source boundary, search | Joel Diaz | SMALL | Candidate boundary | NO | NO | NO | YES — satisfied | YES | PHASE_A_LABOS_ONLY → B | `PARTIAL_PHASE_A` |
| AR-AS4-02 | ASSET-4 | Schema/path coupling | Static module/contract analysis | Joel Diaz | LARGE | AS4-01 | NO | NO para inspección | NO | NO | YES | PHASE_B_REPOSITORY_VERIFICATION | `DEFERRED_NOT_AUTHORIZED` |
| AR-AS4-03 | ASSET-4 | Correctness de synthesis/claims | Controlled expected report, correlation/non-causality review | Joel Diaz | LARGE | AS4-02 | NO | Posible | YES | NO | YES | PHASE_C_NEW_EVIDENCE | `DEFERRED_NOT_AUTHORIZED` |
| AR-AS4-04 | ASSET-4 | Input/output provenance y licensing | Lineage + current license/restriction evidence | Joel Diaz | MEDIUM | AS4-02 | YES | NO | NO | NO | YES | PHASE_A_LABOS_ONLY → C | `PARTIAL_PHASE_A` |
| AR-AS5-01 | ASSET-5 | Formalizar Tier 1, source, owner y duplicate audit | Tier 1, owner, source boundary, search | Joel Diaz | SMALL | Candidate boundary | NO | NO | NO | YES — satisfied | YES | PHASE_A_LABOS_ONLY → B | `PARTIAL_PHASE_A` |
| AR-AS5-02 | ASSET-5 | Separar claim técnico/data adapter | Static methodology and boundary analysis | Joel Diaz | LARGE | AS5-01 | NO | NO para inspección | NO | NO | YES | PHASE_B_REPOSITORY_VERIFICATION | `DEFERRED_NOT_AUTHORIZED` |
| AR-AS5-03 | ASSET-5 | Leakage/overfitting/staleness/correctness | Controlled calculations and independent evidence | Joel Diaz | LARGE | AS5-02 | NO | Posible | YES | NO | YES | PHASE_C_NEW_EVIDENCE | `DEFERRED_NOT_AUTHORIZED` |
| AR-AS5-04 | ASSET-5 | Licensing de inputs/derivados | Current data terms + derivative restrictions | Joel Diaz | MEDIUM | AS5-02 | YES | NO | NO | NO | YES | PHASE_A_LABOS_ONLY → C | `PARTIAL_PHASE_A` |

## Candidate governance and Tier 1 mapping

| Candidate | Governance source | Artifact source | Tier 1 status | Missing Tier 1 / boundary |
|---|---|---|---|---|
| ASSET-1 | Este registro + P003 assessment histórico | `remote GitHub main/app/research/backtester.py` y `simulation.py` | 6/8 verificables | `content_state`; una unidad `source_of_truth` única |
| ASSET-2 | Este registro + P003 assessment histórico | `remote GitHub main/app/optimization/grid_search.py` | 6/8 verificables | `content_state`; source del Candidate desacoplado/gobernado |
| ASSET-3 | Este registro | [Candidate content](./crypto-scalping-core-experiment-journal-template-candidate.md) | 8/8 | NONE para Candidate intake; no implica validation |
| ASSET-4 | Este registro + P003 assessment histórico | `remote GitHub main/app/research/discovery/` | 6/8 verificables | `content_state`; boundary/source unit |
| ASSET-5 | Este registro + P003 assessment histórico | `remote GitHub main/app/research/signal_quality/` | 6/8 verificables | `content_state`; boundary/source unit |

Los seis campos verificables de ASSET-1/2/4/5 son nombre, tipo, descripción, hipótesis_de_uso, originating_Lab y provenance. No se deriva `content_state` desde “funcional/operativo”, y una ruta de implementación no se declara automáticamente source canónico del Candidate.

## Source-of-truth map

| Candidate | Candidate governance SOT | Underlying artifact operational SOT | Evidence source | Branch | Status |
|---|---|---|---|---|---|
| ASSET-1 | Este register; identity baseline en P003 assessment | GitHub main: backtester + simulation paths | Journals, leaderboards, reports, Package 001A inventories | `main` `DIRECTLY_VERIFIED` | Candidate content SOT `EVIDENCE_REQUIRED` |
| ASSET-2 | Este register; identity baseline en P003 assessment | GitHub main: `grid_search.py` | 19 journals, 11 leaderboards, KO-5 mapping | `main` `DIRECTLY_VERIFIED` | Candidate content SOT `EVIDENCE_REQUIRED` |
| ASSET-3 | Este register | [Candidate template](./crypto-scalping-core-experiment-journal-template-candidate.md) | GitHub main: 19 journal instances | `main` `DIRECTLY_VERIFIED` | Identified; Candidate only |
| ASSET-4 | Este register; identity baseline en P003 assessment | GitHub main: `app/research/discovery/` | discovery report + leaderboards | `main` `DIRECTLY_VERIFIED` | Candidate content SOT `EVIDENCE_REQUIRED` |
| ASSET-5 | Este register; identity baseline en P003 assessment | GitHub main: `app/research/signal_quality/` | quality reports/candidate signals | `main` `DIRECTLY_VERIFIED` | Candidate content SOT `EVIDENCE_REQUIRED` |

Remote GitHub `main` es source of truth operacional de Crypto sólo porque Package 001A lo estableció y `.git/HEAD` fue verificado. LabOS es autoridad de sus records de governance/integration. Ninguno sustituye al otro.

## Provenance reconstruction

| Candidate | Chain | Status |
|---|---|---|
| ASSET-1 | Crypto Lab → Binance/raw/configs → backtester/simulation → journals/leaderboards → KO-5 cuando aplica → ASSET-1 → P003 evaluation | `PARTIAL`: código/rutas directos; data licensing y candidate boundary pendientes |
| ASSET-2 | Crypto Lab → data/configs/backtester → grid_search → leaderboards/journals → KO-5 → ASSET-2 → P003 evaluation | `PARTIAL`: cadena técnica visible; licensing/dependency evidence incompleta |
| ASSET-3 | Crypto Lab → 19 journals → estructura común → Candidate template → ASSET-3 → Phase A evaluation | `COMPLETE` para origen interno; no KO requerido; reuse sigue projected |
| ASSET-4 | Crypto Lab → data/leaderboards → discovery modules → discovery report → KO-1/2/5 cuando aplican → ASSET-4 → P003 evaluation | `PARTIAL`: lineage identificado, licensing/validation genérica pendientes |
| ASSET-5 | Crypto Lab → Binance-derived trades/features → signal_quality modules → reports/signals → KO-3/5 cuando aplican → ASSET-5 → P003 evaluation | `PARTIAL`: data rights y validation independiente pendientes |

## Licensing status

| Concern | Candidates | Status | Evidence / next phase |
|---|---|---|---|
| Binance raw/historical data | ASSET-1,2,4,5 | `RESTRICTED` | Package 001A; no redistribución hasta verificación |
| Binance ToS/current rights | ASSET-1,2,4,5 | `UNKNOWN` | PHASE_C_NEW_EVIDENCE; no assumption |
| Crypto repository code license | ASSET-1,2,4,5 | `UNKNOWN` | No `LICENSE` file directamente verificado; Phase C decision/evidence |
| Python third-party software | ASSET-1,2,4,5 | `UNKNOWN` | `requirements.txt` mayormente unpinned; package license/version verification Phase C |
| Journal template structure | ASSET-3 | `NOT_APPLICABLE` para external content | Sanitized structure only; no external content copied |

## Phase totals

| Result | Count |
|---|---:|
| Original actions | 20 |
| `COMPLETE_PHASE_A` | 3 |
| `PARTIAL_PHASE_A` | 8 |
| Deferred untouched | 9 |
| Remaining actions with any open component | 17 |
| Phase B primary actions | 4 |
| Phase C primary actions | 5 + unresolved portions of 4 licensing actions |
| Phase D validation decisions | 5 possible gates; none authorized |

## ASSET-3 validation review status

| Campo | Estado |
|---|---|
| Review | `ASSET-3-VAL-REV-001` — COMPLETE |
| Recommendation | `RECOMMEND_VALIDATED` |
| Evidence freshness | 20 journals directly verified on 2026-08-24; Phase A's 19-count preserved historically |
| Proposed governance record | [PROPOSED_ONLY](./crypto-scalping-core-asset-3-proposed-governance-decision.md) |
| Lifecycle | `CANDIDATE` — unchanged |
| Phase D | `ASSET_3_LIFECYCLE_TRANSITION_DECISION` — `NOT_AUTHORIZED` |
| P004 trigger contribution | 0 |

## ASSET-3 lifecycle decision status

| Campo | Estado |
|---|---|
| Decision | `FD-ASSET-3-VALIDATED-001` — APPROVED |
| Authoritative record | [Lifecycle transition decision](./crypto-scalping-core-asset-3-lifecycle-transition-decision.md) |
| Previous lifecycle | `CANDIDATE` |
| Current lifecycle | `VALIDATED` |
| CANONICAL | NO |
| Reuse | `PROJECTED_REUSE` — unchanged |
| Value | `PROYECTADO` — unchanged |
| Blocking remediation | 0 |
| P004 trigger contribution | 1 |
| Other Asset transitions | 0 |


## Phase B repository verification — 2026-08-25

Authorization: ASSET_REMEDIATION_PHASE_B_REPOSITORY_VERIFICATION / FOUNDER_DECISION. DUAL_REPOSITORY_ACCESS_READY. Crypto main at 751970757a9c3b876ec16f3afd57c13f65a7457f; dirty state preexisting. Mode STATIC + READ_ONLY; tests/experiments/Crypto writes/lifecycle transitions: 0. Results: [Phase B results](./crypto-scalping-core-asset-remediation-phase-b-results.md). Review: [Phase B review](./asset-remediation-phase-b-review.md).

| Remediation | Before | Phase B evidence/action | After/status | Next |
|---|---|---|---|---|
| AR-AS1-01 | Source/content_state pending | Minimal operational source boundary identified | PARTIAL; governed Candidate source still open | Phase C governance |
| AR-AS1-02 | Static contract pending | Inputs/outputs/deps/failures/boundary inspected | COMPLETE | Evidence review after Phase C |
| AR-AS1-03 | Correctness/reproducibility pending | Static path reconstructed; no experiment/test run | DEFERRED_PHASE_C | Controlled deterministic fixture |
| AR-AS1-04 | Licensing/deps partial | pandas/Pydantic mapped; no root license; data rights open | PARTIAL | External licenses/version evidence |
| AR-AS2-01 | Source ambiguity | app/research/optimizer selected; legacy app/optimization excluded | PARTIAL; governed source open | Phase C governance |
| AR-AS2-02 | Contract pending | Config→grid→metrics→CSV→memory traced | COMPLETE; coupled to AS1/Memory | Accept explicit dependencies |
| AR-AS2-03 | Determinism pending | Static ordering/trace assessed; E2E tests absent | DEFERRED_PHASE_C | Controlled fixture |
| AR-AS2-04 | Licensing/deps partial | PyYAML optional used-not-declared; licenses open | PARTIAL | License/dependency correction |
| AR-AS4-01/02 | Lower-priority boundary | Limited discovery module/output inventory | PARTIAL | Future authorized work |
| AR-AS5-01/02 | Lower-priority boundary | Limited signal_quality module/output inventory | PARTIAL | Future authorized work |

| Candidate | Reuse/value | Reproducibility | Readiness |
|---|---|---|---|
| ASSET-1 | PROJECTED_REUSE; SAME_CONTEXT repeated usage; value PROYECTADO | EXECUTION_EVIDENCE_REQUIRED | READY_FOR_PHASE_C_EVIDENCE |
| ASSET-2 | PROJECTED_REUSE; SAME_CONTEXT repeated usage; value PROYECTADO | EXECUTION_EVIDENCE_REQUIRED | READY_FOR_PHASE_C_EVIDENCE |
| ASSET-4/5 | PROJECTED_REUSE / PROYECTADO | Not deeply assessed | REMEDIATION_REMAINS |

Freshness: current working tree has 12 leaderboard CSVs and 20 journals; nine/15 tracked, three/five untracked, memory index modified. Phase A 11/19 remains historical. Existence is usage evidence only, not correctness/reproducibility/value/reuse outside Crypto.

P004 remains 1/3 VALIDATED (ASSET-3 only), NOT_SATISFIED. Package 004 NOT_AUTHORIZED. ASSET-1/2 lifecycle UNCHANGED.

### Phase B freshness re-verification — 2026-09-02

The Phase B package was re-audited against Crypto `main` at the same commit `751970757a9c3b876ec16f3afd57c13f65a7457f`. No source/test/config/dependency-declaration changes exist since the 2026-08-25 evidence baseline. Current dirty research artifacts remain preexisting and were not modified. Phase B statuses, remaining gaps and next phases are unchanged; this entry supplements and does not replace the historical Phase A or original Phase B entries.

## ASSET-1 Phase C controlled evidence — 2026-09-02

Authorization: `ASSET_REMEDIATION_PHASE_C_CONTROLLED_EVIDENCE_PREPARATION` / `FOUNDER_DECISION`. Scope ASSET-1 only. Evidence: [controlled evidence](./crypto-scalping-core-asset-1-controlled-evidence.md); [Phase C results](./crypto-scalping-core-asset-remediation-phase-c-results.md); [independent review](./asset-1-phase-c-controlled-evidence-review.md).

| Remediation | Before | Phase C action/evidence | After/status | Remaining / next |
|---|---|---|---|---|
| AR-AS1-01 | Governed source and `content_state` open | Unique LabOS Candidate evidence package selected; `content_state=borrador`; operational Crypto commit/boundary referenced | `COMPLETE` for review preparation | Reviewer must preserve separation from Crypto operational SOT |
| AR-AS1-03 | Controlled correctness/reproducibility absent | Three-bar synthetic fixture, manual expected result, two exit-0 identical runs, negative observations | `COMPLETE`; `DETERMINISTIC_MATCH`; controlled fixture reproducible with prerequisites | Does not cover historical research or complete CLI edge surface |
| AR-AS1-04 | Runtime versions/licenses incomplete | Python 3.13.7, pandas 2.3.3/BSD-3 metadata and pydantic 2.12.5/MIT metadata observed | `PARTIAL` | No root license; transitive/source reuse and market-data rights unresolved |

ASSET-1 readiness is `READY_FOR_VALIDATION_DECISION_REVIEW`; lifecycle `UNCHANGED`; value `PROYECTADO`; reuse `SAME_CONTEXT / PROJECTED_REUSE`; no validation recommendation. ASSET-2 Phase C remains `NOT_AUTHORIZED`. P004 remains 1/3 `VALIDATED`, `NOT_SATISFIED`, Package 004 `NOT_AUTHORIZED`.

## ASSET-1 validation decision review — 2026-09-02

Authorization: `ASSET_1_VALIDATION_DECISION_REVIEW` / `FOUNDER_DECISION`. Evidence: [decision review](./crypto-scalping-core-asset-1-validation-decision-review.md), [validation matrix](./crypto-scalping-core-asset-1-validation-evidence-matrix.md), and [proposed governance decision](./crypto-scalping-core-asset-1-proposed-governance-decision.md).

Disposition: `RECOMMEND_VALIDATED`; quality and financial/trading risk `PASS_WITH_RESTRICTIONS`; Tier 1 8/8; qualification 5/5; VALIDATED controls 12/12 PASS. Recommendation is limited to the declared software-framework scope. Value remains `PROYECTADO`; reuse remains `PROJECTED_REUSE / SAME_CONTEXT_REUSE`; licensing and global research provenance remain restricted/partial.

Lifecycle remains `CANDIDATE`. Transitions performed: 0. ASSET-1 is not Fast Path eligible; any later authorization must use the standard path `CANDIDATE → UNDER_REVIEW → VALIDATED`. P004 remains 1/3 `VALIDATED`, `NOT_SATISFIED`; Package 004 remains `NOT_AUTHORIZED`.

## ASSET-1 lifecycle decision — 2026-09-02

Founder decision `FD-ASSET-1-VALIDATED-001` approved `APPROVE_ASSET_1_VALIDATED_TRANSITION`. Authoritative record: [ASSET-1 lifecycle transition decision](./crypto-scalping-core-asset-1-lifecycle-transition-decision.md).

Historical sequence recorded without Fast Path compression:

1. `CANDIDATE → UNDER_REVIEW` — qualification 5/5 and Founder review initiation.
2. `UNDER_REVIEW → VALIDATED` — five base fields, concrete scenario, no duplicate and applicable quality/risk gates verified.

Final state: `ASSET-1 VALIDATED / NOT_CANONICAL`. Quality/risk remain `PASS_WITH_RESTRICTIONS`; value `PROYECTADO`; reuse `PROJECTED_REUSE / SAME_CONTEXT_REUSE`; global research provenance PARTIAL; licensing conclusions unchanged. ASSET-2/4/5 lifecycles unchanged.

P004 before/after: 1/3 → 2/3 `VALIDATED`, contributors ASSET-3 and ASSET-1. Trigger `AT_LEAST_3_ASSETS_IN_VALIDATED` remains `NOT_SATISFIED`; Package 004 remains `NOT_AUTHORIZED`.

## ASSET-2 Phase C controlled evidence — 2026-09-02

Authorization: `ASSET_2_PHASE_C_CONTROLLED_EVIDENCE_PREPARATION` / `FOUNDER_DECISION`. Current Crypto source is `main@a86464448c2789b3d7278eaaaffb85666c518602` (`SOURCE_VERSION_CHANGED` from Phase B); ASSET-2 source files are unchanged and the ASSET-1 dependency delta was assessed. Evidence: [controlled evidence](./crypto-scalping-core-asset-2-controlled-evidence.md), [Phase C results](./crypto-scalping-core-asset-remediation-phase-c-results.md), [independent review](./asset-2-phase-c-controlled-evidence-review.md).

| Remediation | Before | Phase C evidence/action | After/status | Remaining / next |
|---|---|---|---|---|
| AR-AS2-01 | Candidate source/content_state open | Unique LabOS Candidate evidence package selected; `content_state=borrador`; operational source anchored to current commit | COMPLETE for review preparation | Preserve governance/operational source separation |
| AR-AS2-03 | Controlled E2E/replay absent | 2×2 actual-schema grid; predetermined metrics/ranks; two identical enumeration→ranking→CSV runs | COMPLETE; grid/ranking/replay/determinism MATCH | Historical outputs remain unhashed usage evidence |
| AR-AS2-04 | Dependencies/licensing partial | Python 3.13.7, pandas 2.3.3, pydantic 2.12.5, PyYAML 6.0.3 and local license metadata captured | PARTIAL | PyYAML undeclared; locks/transitives/root/data rights unresolved |

ASSET-2 readiness is `READY_FOR_VALIDATION_DECISION_REVIEW`; lifecycle remains `CANDIDATE`; value `PROYECTADO`; reuse `PROJECTED_REUSE / SAME_CONTEXT_REUSE`; no recommendation or transition. P004 remains 2/3 `VALIDATED`, `NOT_SATISFIED`; Package 004 remains `NOT_AUTHORIZED`.

## ASSET-2 validation decision review — 2026-09-02

Authorization: `ASSET_2_VALIDATION_DECISION_REVIEW` / `FOUNDER_DECISION`. Evidence: [decision review](./crypto-scalping-core-asset-2-validation-decision-review.md), [validation matrix](./crypto-scalping-core-asset-2-validation-evidence-matrix.md), and [proposed governance decision](./crypto-scalping-core-asset-2-proposed-governance-decision.md).

Disposition: `RECOMMEND_VALIDATED`; quality and financial/trading risk `PASS_WITH_RESTRICTIONS`; Tier 1 8/8; qualification 5/5; exact VALIDATED controls 12/12 PASS. `SOURCE_VERSION_CHANGED` was addressed twice: ASSET-2 IN_SCOPE modules were unchanged between Phase B `7519707…` and Phase C `a864644…`; during review, Crypto advanced externally to `dc4da18…` and `grid_search.py` gained only a short-strategy registry/default/CLI-loading integration. The controlled enumeration, metric, ranking and leaderboard functions remained unchanged; the new strategy adapter is outside the correctness claim. Evidence freshness remains a transition-time check.

The recommendation is limited to controlled optimizer software behavior. Tie semantics, failure recovery/atomicity, PyYAML `USED_NOT_DECLARED`, unlocked dependencies, project/data licensing and historical provenance remain non-blocking restrictions at current internal exposure. Value remains `PROYECTADO`; reuse remains `PROJECTED_REUSE / SAME_CONTEXT_REUSE`; no financial or research claim was inferred.

Lifecycle remains `CANDIDATE`; transitions performed: 0. A separately authorized Founder action must preserve `CANDIDATE → UNDER_REVIEW → VALIDATED`. P004 remains 2/3 `VALIDATED`, `NOT_SATISFIED`; Package 004 remains `NOT_AUTHORIZED`.

## ASSET-2 lifecycle decision — 2026-09-02

Founder decision `FD-ASSET-2-VALIDATED-001` approved `APPROVE_ASSET_2_VALIDATED_TRANSITION`. Authoritative record: [ASSET-2 lifecycle transition decision](./crypto-scalping-core-asset-2-lifecycle-transition-decision.md).

Source freshness: transition-time Crypto `main@dc4da184340377e8506b053bdedfb8fdb9153a29` equals the validation-review commit; no later IN_SCOPE or directly relevant dependency delta was found. Classification: `SOURCE_FRESHNESS_CONFIRMED`.

Historical standard-path sequence:

1. `CANDIDATE → UNDER_REVIEW` — Tier 1 8/8, qualification 5/5 and Founder review initiation.
2. `UNDER_REVIEW → VALIDATED` — five base fields, concrete Forma B scenario, no duplicate, criteria 12/12 and applicable quality/risk gates verified.

Final state: `ASSET-2 VALIDATED / NOT_CANONICAL`. Quality/risk remain `PASS_WITH_RESTRICTIONS`; tie and failure behavior remain PARTIAL; dependency/licensing restrictions remain open; value `PROYECTADO`; reuse `PROJECTED_REUSE / SAME_CONTEXT_REUSE`; global provenance PARTIAL. ASSET-1/3/4/5 lifecycles unchanged.

P004 recomputed from authoritative decisions: ASSET-1, ASSET-2 and ASSET-3 are `VALIDATED`; progress 3/3; trigger `AT_LEAST_3_ASSETS_IN_VALIDATED` is `SATISFIED`. Package 004 remains `DORMANT / CONDITIONAL / NOT_AUTHORIZED`.
