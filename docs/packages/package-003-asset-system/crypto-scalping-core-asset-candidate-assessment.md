# Assessment de Asset Candidates — Crypto Scalping Core

## Scope y safety boundary

[Hecho] Esta evaluación aplica Package 003 en modo read-only a `LABOS-REF-LAB-0001`. No modifica Crypto Scalping Core, no promueve candidates, no ejecuta trading y no valida automáticamente estrategias.

[Decisión] Ningún resultado implica profitability, live-trading readiness ni derechos de redistribución. Los datasets Binance/raw permanecen restringidos mientras licensing sea unresolved. Expectancy negativa de trading no invalida por sí sola un Asset técnico reusable; cada candidate se evalúa contra su claim real.

## Fuentes consultadas

- [Candidatos identificados por Package 001A](../package-001a-first-lab-integration/crypto-scalping-core-asset-candidates.md)
- [Readiness de Assets](../package-001a-first-lab-integration/crypto-scalping-core-asset-readiness.md)
- [Provenance de datos](../package-001a-first-lab-integration/crypto-scalping-core-data-provenance-assessment.md)
- [Source-of-truth map](../package-001a-first-lab-integration/crypto-scalping-core-source-of-truth-map.md)
- [Boundary analysis](../package-001a-first-lab-integration/crypto-scalping-core-boundary-analysis.md)

## Resumen

| Candidate | Tipo propuesto | Outcome | Razón dominante |
|---|---|---|---|
| ASSET-1 | Herramienta | NEEDS_REMEDIATION | Acoplamiento, owner acceptance y evidencia cross-context faltantes |
| ASSET-2 | Herramienta | NEEDS_REMEDIATION | Uso interno demostrado, pero interfaz/acoplamiento y ownership incompletos |
| ASSET-3 | Template | NEEDS_REMEDIATION | Patrón repetido, pero no existe template extraído ni source canónico único |
| ASSET-4 | Herramienta | NEEDS_REMEDIATION | Pipeline funcional, altamente integrado y sin validación fuera del origen |
| ASSET-5 | Herramienta | NEEDS_REMEDIATION | Metodología potencial, código integrado y riesgo financiero/licensing pendiente |

## ASSET-1 — Framework de backtesting

| Campo | Assessment |
|---|---|
| Candidate ID / name | ASSET-1 / Framework de backtesting para estrategias de trading |
| Proposed canonical type | Herramienta; opera como motor, aunque hoy esté acoplado |
| Originating Lab | LABOS-REF-LAB-0001 — Crypto Scalping Core |
| Provenance | Package 001A inventory → `app/research/backtester.py` + `simulation.py`; evidencia/read-only |
| Source of truth | Paths del repositorio identificados; source único del candidate extraído todavía NO establecido |
| Ownership | Lab boundary conocido; Asset_Owner humano y aceptación de mantenimiento no registrados |
| Lifecycle | CANDIDATE; no promovido |
| Qualification dimensions | Reuse NO_SATISFECHA; quality NO_SATISFECHA; provenance SATISFECHA; ownership NO_SATISFECHA; source of truth NO_SATISFECHA |
| Reuse evidence | Uso funcional dentro del proyecto; no demuestra uso fuera del contexto |
| Projected / demonstrated reuse | Projected: trading Labs/Atlas, escenario todavía hipotético. Demonstrated cross-context: NONE |
| Quality gate | Nivel 1 base + financial/licensing override ELEVATED; no elegible para Fast Path actual |
| Risk / sensitivity | HIGH financial; MEDIUM operational; Lab-Private mientras contenga estrategias/parámetros/resultados |
| sharing_scope / consumption_state | Lab-Private / NO_ACTIVE_EXTERNAL_CONSUMERS |
| Licensing restrictions | Código propio por confirmar; inputs Binance/raw no redistribuibles sin licencia verificada |
| Value status | PROYECTADO; utilidad técnica posible independiente de profitability |
| Missing evidence | Interfaz genérica, tests independientes, owner acceptance, canonical extracted source, license/dependency inventory |
| Promotion blockers | 4/5 dimensions no satisfechas; coupling; elevated gates |
| Next review trigger | Extracción y prueba contra segunda estrategia/contexto + owner/licensing record |
| Outcome | NEEDS_REMEDIATION |

## ASSET-2 — Optimizador Grid Search

| Campo | Assessment |
|---|---|
| Candidate ID / name | ASSET-2 / Optimizador de parámetros por grid search con leaderboard |
| Proposed canonical type | Herramienta |
| Originating Lab | LABOS-REF-LAB-0001 |
| Provenance / source | Package 001A + `app/optimization/grid_search.py`; source único extraído no establecido |
| Ownership / lifecycle | Owner acceptance faltante / CANDIDATE |
| Qualification dimensions | Reuse NO_SATISFECHA; quality NO_SATISFECHA; provenance SATISFECHA; ownership NO_SATISFECHA; source NO_SATISFECHA |
| Reuse evidence | 14+ ejecuciones internas: evidencia de repetición/calidad, no demonstrated cross-context reuse |
| Projected / demonstrated reuse | Projected específico: optimización en otros Labs cuantitativos. Demonstrated: NONE |
| Quality gate | Nivel 1 + financial/operational override ELEVATED |
| Risk / sensitivity | HIGH financial; parámetros/leaderboards Lab-Private |
| sharing_scope / consumption_state | Lab-Private / NO_ACTIVE_EXTERNAL_CONSUMERS |
| Licensing restrictions | Resultados e inputs de market data restringidos; dependencia/licencia debe inventariarse |
| Value status | PROYECTADO; repetición interna respalda calidad pero no adopción |
| Missing evidence / blockers | Abstracción de strategy interface, tests independientes, owner, source canónico, restrictions; 4/5 dimensions fallan |
| Next review trigger | Ejecución desacoplada con dataset permitido y escenario externo documentado |
| Outcome | NEEDS_REMEDIATION |

## ASSET-3 — Template de experiment journal

| Campo | Assessment |
|---|---|
| Candidate ID / name | ASSET-3 / Template de journal de experimentación cuantitativa |
| Proposed canonical type | Template |
| Originating Lab | LABOS-REF-LAB-0001 |
| Provenance / source | Formato implícito en 14 `research/journal/EXP-*.md`; no existe archivo template canónico único |
| Ownership / lifecycle | Owner acceptance faltante / CANDIDATE |
| Qualification dimensions | Reuse NO_SATISFECHA; quality SATISFECHA por 14 instancias consistentes; provenance SATISFECHA; ownership NO_SATISFECHA; source NO_SATISFECHA |
| Reuse evidence | Repetición interna demostrada; no uso fuera del contexto originador |
| Projected / demonstrated reuse | Projected: cualquier Lab de research estructurado. Demonstrated cross-context: NONE |
| Quality gate | Nivel 1 base; Fast Path bloqueado por dimensiones incompletas |
| Risk / sensitivity | LOW estructural; contenido de instancias puede ser HIGH/Lab-Private y no integra el template |
| sharing_scope / consumption_state | LabOS-Shared propuesto / NO_ACTIVE_EXTERNAL_CONSUMERS |
| Licensing restrictions | Estructura interna sin restricción conocida; confirmar que no copie contenido/licencia externa |
| Value status | PROYECTADO; fuerte evidencia de utilidad interna |
| Missing evidence / blockers | Extraer template limpio, canonical source, owner acceptance y escenario cross-Lab concreto; 3/5 dimensions fallan |
| Next review trigger | Template extraído + dry-run en un segundo contexto sin datos sensibles |
| Outcome | NEEDS_REMEDIATION |

## ASSET-4 — Pipeline de discovery report

| Campo | Assessment |
|---|---|
| Candidate ID / name | ASSET-4 / Pipeline de generación de discovery report automatizado |
| Proposed canonical type | Herramienta |
| Originating Lab | LABOS-REF-LAB-0001 |
| Provenance / source | Package 001A + `app/research/discovery/`; extracted canonical source no establecido |
| Ownership / lifecycle | Owner acceptance faltante / CANDIDATE |
| Qualification dimensions | Reuse NO_SATISFECHA; quality NO_SATISFECHA; provenance SATISFECHA; ownership NO_SATISFECHA; source NO_SATISFECHA |
| Reuse evidence | Genera report interno; ninguna aplicación externa registrada |
| Projected / demonstrated reuse | Projected: Labs con múltiples experiment runs. Demonstrated: NONE |
| Quality gate | Nivel 1 + financial/licensing/operational override ELEVATED |
| Risk / sensitivity | HIGH por inferencias financieras; reports/resultados Lab-Private |
| sharing_scope / consumption_state | Lab-Private / NO_ACTIVE_EXTERNAL_CONSUMERS |
| Licensing restrictions | Outputs derivados no habilitan redistribución de raw inputs; licencia pendiente |
| Value status | PROYECTADO |
| Missing evidence / blockers | Separación de schema/paths, validación genérica, owner, source, licensing; 4/5 dimensions fallan |
| Next review trigger | Pipeline desacoplado probado con evidencia no restringida y claims limitados |
| Outcome | NEEDS_REMEDIATION |

## ASSET-5 — Pipeline de quality analysis

| Campo | Assessment |
|---|---|
| Candidate ID / name | ASSET-5 / Pipeline de análisis de calidad de señales de trading |
| Proposed canonical type | Herramienta |
| Originating Lab | LABOS-REF-LAB-0001 |
| Provenance / source | Package 001A + `app/research/signal_quality/`; extracted canonical source no establecido |
| Ownership / lifecycle | Owner acceptance faltante / CANDIDATE |
| Qualification dimensions | Reuse NO_SATISFECHA; quality NO_SATISFECHA; provenance SATISFECHA; ownership NO_SATISFECHA; source NO_SATISFECHA |
| Reuse evidence | Report interno existente; no reusable use fuera del Lab |
| Projected / demonstrated reuse | Projected: análisis de señales en Labs cuantitativos. Demonstrated: NONE |
| Quality gate | Nivel 1 + financial/licensing override ELEVATED |
| Risk / sensitivity | HIGH financial; signal features/P&L Lab-Private |
| sharing_scope / consumption_state | Lab-Private / NO_ACTIVE_EXTERNAL_CONSUMERS |
| Licensing restrictions | Binance/raw datasets restringidos; derivados requieren revisión antes de sharing/publicación |
| Value status | PROYECTADO; una expectativa negativa no anula utilidad metodológica o técnica |
| Missing evidence / blockers | Separar claim técnico de estrategia, tests, owner, source, licensing y validación cross-context; 4/5 dimensions fallan |
| Next review trigger | Validación metodológica desacoplada con dataset autorizado y limitaciones explícitas |
| Outcome | NEEDS_REMEDIATION |

## Safety and outcome matrix

| Control | Resultado |
|---|---|
| Candidates evaluados | 5/5 |
| Outcome permitido por candidate | 5/5 |
| PROMOTED/CANONICAL como outcome | 0 |
| Candidates promovidos | 0 |
| Profitability claim | 0 |
| Live-trading readiness claim/authorization | 0 |
| Automatic strategy validation | 0 |
| Binance/raw licensing assumed | 0 |
| Crypto files modified | 0 |

## Cross-category coverage

[Hecho] Los candidates representan **2/7** tipos: Herramienta (4) y Template (1).

`VALIDATION_COVERAGE_LIMITATION`: Dataset, Framework, Playbook, Documento y Componente no reciben validación práctica en este set. No se inventan candidates para completar taxonomía.

## Practical usability and AI-readiness observations

[Hecho] Con README y los documentos canónicos W1–W3, un Founder SOLO puede identificar, calificar, decidir, compartir, revisar y deprecar conceptualmente, pero los templates operativos aún no existen porque pertenecen a W5. Friction actual: transcribir Tier 1/Tier 2 y resultados entre documentos es `MODERATE`.

- `FUTURE`: los templates W5 deberían permitir intake low-risk `LIGHTWEIGHT` con exactamente ocho campos Tier 1.
- `FUTURE`: validación automática de field counts, stale reviews y conflicts puede reducir errores.
- `DEFERRED_IMPLEMENTATION`: un agente futuro podría detectar metadata faltante, preparar evaluation, citar provenance y proponer promotion/deprecation.
- [Decisión] AI no puede promote, own, archive ni cambiar authority.
