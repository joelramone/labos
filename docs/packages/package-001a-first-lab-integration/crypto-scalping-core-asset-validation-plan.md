# Crypto Scalping Core — Asset Validation Plan

## Naturaleza y límites

| Campo | Valor |
|---|---|
| Plan ID | `CSC-ASSET-VALIDATION-PLAN-001` |
| Reference Lab | `LABOS-REF-LAB-0001` |
| Fecha | 2026-08-24 |
| Estado | `PLANNING_ONLY / NOT_AUTHORIZED_FOR_EXECUTION` |
| Candidates | ASSET-1 a ASSET-5, sin renombrar |
| Lifecycle changes | `NOT_AUTHORIZED` |
| Crypto modifications | `NOT_AUTHORIZED` |

## Phase A disposition — 2026-08-24

`ASSET_REMEDIATION_PHASE_A` was executed under `FD-ASSET-REM-A-001` within LabOS-only boundaries.

| Control | Current value |
|---|---|
| Crypto access | `CRYPTO_REPOSITORY_ACCESSIBLE`, read-only |
| Current branch | `main`, directly verified |
| Remediations | 20 original; 3 complete Phase A, 8 partial Phase A, 9 deferred untouched |
| ASSET-3 | `READY_FOR_VALIDATION_DECISION_REVIEW`; no decision performed |
| ASSET-1/2/4/5 | `READY_FOR_REPOSITORY_VERIFICATION` |
| Assets in VALIDATED | 0 |
| P004 trigger | `NOT_SATISFIED` |

Current operational sources:

- [Master remediation register](./crypto-scalping-core-asset-remediation-register.md)
- [Phase A results](./crypto-scalping-core-asset-remediation-phase-a-results.md)
- [Validation test plan](./crypto-scalping-core-asset-validation-test-plan.md)
- [Independent Phase A review](./asset-remediation-phase-a-review.md)

The original plan below is preserved as pre-execution planning evidence. Where counts or classifications differ, the master register is current: direct inspection found 19 journals and 11 leaderboards, and the ASSET-3 dry-run is useful but not mandatory for a validation review using valid Forma B projected reuse.

## ASSET-3 lifecycle disposition — 2026-08-24

| Control | Current value |
|---|---|
| Founder decision | `FD-ASSET-3-VALIDATED-001` |
| Transition | `CANDIDATE → VALIDATED` — applied |
| CANONICAL | NO |
| Reuse / value | `PROJECTED_REUSE` / `PROYECTADO` — unchanged |
| Current VALIDATED count | 1 |
| P004 trigger | 1/3 — `NOT_SATISFIED` |
| Next authorized work | NONE |

Authoritative decision: [ASSET-3 lifecycle transition](./crypto-scalping-core-asset-3-lifecycle-transition-decision.md). The earlier Phase A disposition remains historical evidence of the pre-transition state.

## ASSET-1 lifecycle disposition — 2026-09-02

| Control | Current value |
|---|---|
| Founder decision | `FD-ASSET-1-VALIDATED-001` |
| Standard transition history | `CANDIDATE → UNDER_REVIEW → VALIDATED` — applied |
| Current lifecycle | `VALIDATED` |
| CANONICAL | NO |
| Quality / risk | `PASS_WITH_RESTRICTIONS` / `PASS_WITH_RESTRICTIONS` |
| Reproducibility | `REPRODUCIBLE_WITH_DOCUMENTED_PREREQUISITES`, controlled fixture only |
| Reuse / value | `PROJECTED_REUSE / SAME_CONTEXT_REUSE` / `PROYECTADO` |
| Current VALIDATED count | 2 — ASSET-3 and ASSET-1 |
| P004 trigger | 2/3 — `NOT_SATISFIED` |
| Next safe action | `ASSET_2_PHASE_C_CONTROLLED_EVIDENCE_PREPARATION`, not executed |

Authoritative decision: [ASSET-1 lifecycle transition](./crypto-scalping-core-asset-1-lifecycle-transition-decision.md). Earlier plan and review states remain historical evidence. No CANONICAL, Product, Public sharing or Package 004 action is authorized.

## ASSET-2 lifecycle disposition — 2026-09-02

| Control | Current value |
|---|---|
| Founder decision | `FD-ASSET-2-VALIDATED-001` |
| Standard transition history | `CANDIDATE → UNDER_REVIEW → VALIDATED` — applied |
| Current lifecycle | `VALIDATED` |
| CANONICAL | NO |
| Source freshness | `SOURCE_FRESHNESS_CONFIRMED` at Crypto `main@dc4da184…` |
| Quality / risk | `PASS_WITH_RESTRICTIONS` / `PASS_WITH_RESTRICTIONS` |
| Determinism / replay | `DETERMINISTIC_MATCH` / `REPLAY_MATCH` |
| Reproducibility | `REPRODUCIBLE_WITH_DOCUMENTED_PREREQUISITES`, controlled fixture only |
| Reuse / value | `PROJECTED_REUSE / SAME_CONTEXT_REUSE` / `PROYECTADO` |
| Current VALIDATED count | 3 — ASSET-1, ASSET-2 and ASSET-3 |
| P004 trigger | 3/3 — `SATISFIED` |
| Package 004 | `DORMANT / CONDITIONAL / NOT_AUTHORIZED` |
| Next safe action | `PACKAGE_004_ACTIVATION_READINESS_REVIEW`, not executed |

Authoritative decision: [ASSET-2 lifecycle transition](./crypto-scalping-core-asset-2-lifecycle-transition-decision.md). Earlier plan, remediation and review states remain historical evidence. Trigger satisfaction is not Package 004 activation or authorization.

Este documento es un plan operacional nuevo del Reference Lab; no reabre ni modifica el significado histórico de Package 001A o Package 003. Aplica [Package 003 Asset System](../package-003-asset-system/README.md) y el [evidence review del trigger P004](../../architecture/package-004-activation-trigger-evidence-review.md). No busca producir tres resultados positivos: prioriza calidad de evidencia, luego potencial de reuse/value y finalmente esfuerzo.

## Orden recomendado

| Priority | Candidate | Razón |
|---:|---|---|
| 1 | ASSET-3 — Template de journal de experimentación cuantitativa | Evidencia interna fuerte, bajo riesgo estructural, gap acotado y validación posible sin modificar Crypto |
| 2 | ASSET-2 — Optimizador de parámetros por grid search con leaderboard | 14+ runs/leaderboards aportan evidencia; requiere desacoplamiento y correctness verificable |
| 3 | ASSET-1 — Framework de backtesting para estrategias de trading | Alto potencial técnico; boundary y métricas independientes aún faltan |
| 4 | ASSET-4 — Pipeline de generación de discovery report automatizado | Output real, pero acoplamiento y validación de inferencias elevan esfuerzo |
| 5 | ASSET-5 — Pipeline de análisis de calidad de señales de trading | Metodología potencial, mayor riesgo de overfitting/misuse y licensing pendiente |

## Plan por Candidate

### ASSET-3 — Template de journal de experimentación cuantitativa

| Elemento | Plan |
|---|---|
| Current status | `CANDIDATE / NEEDS_REMEDIATION`; quality y provenance satisfechas; 3/5 dimensions fallan |
| Evidence | 14 `research/journal/EXP-*.md` consistentes; originating Lab y patrón identificados |
| Gap | No template limpio, source único, owner acceptance ni Forma B concreta |
| Remediation | AR-AS3-01..04: extracción no sensible, Tier 1/owner/source/duplicate audit, dry-run segundo contexto, restrictions + trigger 90 días |
| Validation test | Field/schema comparison de 14 instancias; completar el template en contexto no trading; owner checklist; source/reference check |
| Expected output | Candidate record 8/8, template propuesto, evaluation 5/5 o gaps explícitos, evidence bundle |
| Decision gate | `ASSET_VALIDATION_DECISION_REVIEW`; humano decide si permanece CANDIDATE, pasa a UNDER_REVIEW/VALIDATED o requiere remediation |

### ASSET-2 — Optimizador de parámetros por grid search con leaderboard

| Elemento | Plan |
|---|---|
| Current status | `CANDIDATE / NEEDS_REMEDIATION`; provenance 1/5 satisfecha |
| Evidence | `grid_search.py`, 14+ ejecuciones, ocho leaderboards, journals y KO-5 |
| Gap | Reuse projected incompleto; no owner/source; contract y correctness dependen del backtester; licensing/dependencies pendientes |
| Remediation | AR-AS2-01..04 |
| Validation test | Con autorización futura, ejecutar contract desacoplado sobre fixture permitido; verificar combinaciones, ranking determinista, schema de output y error handling; revisar overfitting claims |
| Expected output | Candidate/evaluation records, dependency/restriction manifest, reproducibility evidence |
| Decision gate | Review humano de 5 dimensions + effective risk gate; no promotion |

### ASSET-1 — Framework de backtesting para estrategias de trading

| Elemento | Plan |
|---|---|
| Current status | `CANDIDATE / NEEDS_REMEDIATION`; provenance 1/5 satisfecha |
| Evidence | `backtester.py`, `simulation.py`, internal runs, leaderboards/journals |
| Gap | Boundary multi-file, strategy coupling, owner/source, expected-metric tests y licensing |
| Remediation | AR-AS1-01..04 |
| Validation test | Con autorización futura, fixture autorizado con estrategia/datos sintéticos o permitidos; comprobar PF/expectancy/drawdown contra resultados calculados independientemente, sin evaluar profitability |
| Expected output | Defined tool contract, candidate/evaluation records, test evidence, restrictions/dependencies |
| Decision gate | Review humano de qualification y elevated risk gate |

### ASSET-4 — Pipeline de generación de discovery report automatizado

| Elemento | Plan |
|---|---|
| Current status | `CANDIDATE / NEEDS_REMEDIATION`; provenance 1/5 satisfecha |
| Evidence | `app/research/discovery/`, report sobre 567 runs, confidence MEDIO, KO-1/2/5 references |
| Gap | Schemas/paths integrados, un dataset, sin validación genérica; correlation/claims y licensing pendientes |
| Remediation | AR-AS4-01..04 |
| Validation test | Input fixture permitido con resultados conocidos; verificar agregaciones, ranking, correlaciones y lenguaje no causal; lineage de cada output |
| Expected output | Generic contract o evidencia de que no es justificable; evaluation, restrictions y correctness report |
| Decision gate | `READY_FOR_REVIEW`, `NEEDS_REMEDIATION`, `EVIDENCE_REQUIRED` o `NOT_AN_ASSET`; lifecycle sólo por decisión separada |

### ASSET-5 — Pipeline de análisis de calidad de señales de trading

| Elemento | Plan |
|---|---|
| Current status | `CANDIDATE / NEEDS_REMEDIATION`; provenance 1/5 satisfecha |
| Evidence | `app/research/signal_quality/`, quality report, candidate signals, KO-3/5; confidence MEDIO |
| Gap | Claim/metodología acoplados, no cross-validation, leakage/overfitting/staleness, owner/source y licensing |
| Remediation | AR-AS5-01..04 |
| Validation test | Evidencia controlada con expected feature/quartile calculations; tests de leakage y límites de inferencia; no live data/trading |
| Expected output | Method contract, validation evidence, restrictions, candidate/evaluation records o rechazo justificado |
| Decision gate | Review humano bajo elevated financial/licensing/research-validity gate |

## Execution waves propuestas — no autorizadas

| Wave | Scope | Gate |
|---|---|---|
| VP0 | LabOS-only: Candidate records, ownership questions, duplicate/source/provenance audits | Evidencia suficiente para decidir si cualquier trabajo sobre Crypto está justificado |
| VP1 | ASSET-3 extraction y dry-run fuera de Crypto | Independent evaluation; posible `ASSET_VALIDATION_DECISION_REVIEW` |
| VP2 | Con autorización explícita futura: ASSET-2/1 boundaries y reproducibility tests | Separate validation decision por Candidate |
| VP3 | Sólo si evidencia/beneficio lo justifican: ASSET-4/5 research validation | Continue, remediate o `NOT_AN_ASSET`; no target count |

Cada Wave requiere autorización propia si afecta Crypto. Un resultado negativo se preserva como evidencia válida y no debe reabrirse para satisfacer el trigger de Product Factory.

## Safety y decision gates

- Raw Binance datasets permanecen `RESTRICTED` hasta resolver licensing por autoridad competente.
- Ningún output afirma profitability, live-trading readiness o automatic strategy validation.
- `DEMONSTRATED_REUSE` requiere uso fuera del contexto de origen; runs repetidos no bastan.
- La transición a `VALIDATED` y cualquier promoción posterior requieren actos humanos separados.
- Este plan no modifica el registry, no canonicaliza Assets y no autoriza Package 004.
