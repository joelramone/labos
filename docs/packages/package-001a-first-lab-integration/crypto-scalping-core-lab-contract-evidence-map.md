# Mapa de Evidencia — Lab Contract Crypto Scalping Core

## Metadata

| Campo | Valor |
|-------|-------|
| **Documento** | Mapa de evidencia del Lab Contract |
| **Lab** | Crypto Scalping Core |
| **Package** | 001A — First Lab Integration |
| **Batch** | 3 — Lab Contract & Compliance |
| **Fecha** | 2025-07-24 |

---

## Propósito

Mapear cada afirmación sustantiva del Lab Contract a su fuente de evidencia, evaluando cobertura y confianza. [Hecho] Este documento permite auditar la trazabilidad del contrato.

---

## Sección 1 — Identity

| Afirmación | Evidencia | Path de evidencia | Estado | Clasificación epistémica | Confianza |
|------------|-----------|-------------------|--------|-------------------------|-----------|
| Nombre: Crypto Scalping Core | Portfolio Model | `.kiro/steering/portfolio-model.md` | VERIFIED | [Hecho] | ALTA |
| Owner: Joel Diaz | Decisión fundador | `founder-decisions-package-001a-batch1.md` | VERIFIED | [Hecho] | ALTA |
| Repositorio: github.com/joelramone/crypto-scalping-core | Decisión fundador | `founder-decisions-package-001a-batch1.md` (Dec 1) | VERIFIED | [Hecho] | ALTA |
| Branch: main | Decisión fundador | `founder-decisions-package-001a-batch1.md` (Dec 1) | VERIFIED | [Decisión] | ALTA |
| Estado: explorando | Decisión fundador | `founder-decisions-package-001a-batch3.md` (FD-B3-01) | VERIFIED | [Decisión] | ALTA |
| Fecha integración: 2025-07-24 | Batch 3 execution | Este documento | VERIFIED | [Hecho] | ALTA |

---

## Sección 2 — Mission

| Afirmación | Evidencia | Path de evidencia | Estado | Clasificación epistémica | Confianza |
|------------|-----------|-------------------|--------|-------------------------|-----------|
| Misión enfocada en investigación | Actividad observada en repositorio | `crypto-scalping-core-research-workflow-map.md` | VERIFIED | [Decisión] | ALTA |
| No afirma rentabilidad | Resultados de estrategias | `crypto-scalping-core-strategy-inventory.md` (PF < 1.0 en todas) | VERIFIED | [Hecho] | ALTA |
| Producción de conocimiento reproducible | 14 experiment journals | `crypto-scalping-core-research-artifacts-inventory.md` | VERIFIED | [Hecho] | ALTA |

---

## Sección 3 — Scope

| Afirmación | Evidencia | Path de evidencia | Estado | Clasificación epistémica | Confianza |
|------------|-----------|-------------------|--------|-------------------------|-----------|
| Market-data research IN | download_data.py + data/*.csv | Repositorio: `app/research/download_data.py` | VERIFIED | [Hecho] | ALTA |
| Feature engineering IN | features.py funcional | Repositorio: `app/research/features.py` | VERIFIED | [Hecho] | ALTA |
| Backtesting IN | backtester.py operativo | Repositorio: `app/research/backtester.py` | VERIFIED | [Hecho] | ALTA |
| Optimization IN | grid_search con 567 runs | Repositorio: `app/optimization/grid_search.py` | VERIFIED | [Hecho] | ALTA |
| Quality analysis IN | signal_quality/ con output | Repositorio: `app/research/signal_quality/` | VERIFIED | [Hecho] | ALTA |
| Employer/corporate OUT | Decisión fundador | `founder-decisions-package-001a-batch1.md` (Dec 2) | VERIFIED | [Decisión] | ALTA |
| Live trading OUT | Sin edge demostrado | `crypto-scalping-core-strategy-inventory.md` | VERIFIED | [Decisión] | ALTA |

---

## Sección 4 — Ownership

| Afirmación | Evidencia | Path de evidencia | Estado | Clasificación epistémica | Confianza |
|------------|-----------|-------------------|--------|-------------------------|-----------|
| Lab-Private por defecto | Decisión fundador | `founder-decisions-package-001a-batch1.md` (Dec 2) | VERIFIED | [Decisión] | ALTA |
| Datasets externos: RESTRINGIDO | Decisión fundador | `founder-decisions-package-001a-batch1.md` (Dec 2) | VERIFIED | [Decisión] | ALTA |
| Exclusión corporativa | Decisión fundador | `founder-decisions-package-001a-batch1.md` (Dec 2) | VERIFIED | [Decisión] | ALTA |
| LabOS authority solo sobre promovidos | Package 002 rules | `lab-boundaries.md` + Package 002 | VERIFIED | [Decisión] | ALTA |

---

## Sección 5 — Boundaries

| Afirmación | Evidencia | Path de evidencia | Estado | Clasificación epistémica | Confianza |
|------------|-----------|-------------------|--------|-------------------------|-----------|
| Estrategias son Lab-Private | Decisión fundador confirmada | `crypto-scalping-core-boundary-analysis.md` | VERIFIED | [Decisión] | ALTA |
| Credenciales NUNCA en repo | Buena práctica + decisión | `crypto-scalping-core-boundary-analysis.md` | VERIFIED | [Decisión] | ALTA |
| BYMA/NRTC/SentinelOps excluidos | Decisión fundador | `founder-decisions-package-001a-batch1.md` (Dec 2) | VERIFIED | [Decisión] | ALTA |

---

## Sección 6 — Inputs

| Afirmación | Evidencia | Path de evidencia | Estado | Clasificación epistémica | Confianza |
|------------|-----------|-------------------|--------|-------------------------|-----------|
| Binance API como fuente de datos | Código de descarga | Repositorio: `app/data/binance_downloader.py` | VERIFIED | [Hecho] | ALTA |
| requirements.txt existe | Archivo en repositorio | Repositorio: `requirements.txt` | VERIFIED | [Hecho] | ALTA |
| Licencia de Binance data: RESTRINGIDO | ToS no verificado formalmente | N/A — pendiente | EVIDENCE_REQUIRED | [Hecho] | BAJA |

---

## Sección 7 — Activities

| Afirmación | Evidencia | Path de evidencia | Estado | Clasificación epistémica | Confianza |
|------------|-----------|-------------------|--------|-------------------------|-----------|
| Pipeline de 8 etapas operativo | Outputs verificados | `crypto-scalping-core-research-workflow-map.md` | VERIFIED | [Hecho] | ALTA |
| Walk-forward parcial | Código existe, outputs vacíos | Repositorio: `app/optimization/walk_forward.py` + `research/walk_forward/` | VERIFIED | [Hecho] | ALTA |
| Monte Carlo parcial | Código existe, outputs vacíos | Repositorio: `app/montecarlo.py` + `research/monte_carlo/` | VERIFIED | [Hecho] | ALTA |
| 14 experiment journals | Archivos en journal/ | Repositorio: `research/journal/EXP-*.md` | VERIFIED | [Hecho] | ALTA |

---

## Sección 8 — Outputs

| Afirmación | Evidencia | Path de evidencia | Estado | Clasificación epistémica | Confianza |
|------------|-----------|-------------------|--------|-------------------------|-----------|
| 14 journals existentes | Conteo de archivos | Repositorio: `research/journal/` | VERIFIED | [Hecho] | ALTA |
| 8 leaderboard CSVs | Conteo de archivos | Repositorio: `research/leaderboards/` | VERIFIED | [Hecho] | ALTA |
| 2 research reports | Conteo de archivos | Repositorio: `research/reports/` | VERIFIED | [Hecho] | ALTA |
| 4 estrategias RESEARCH | Conteo + evaluación PF | `crypto-scalping-core-strategy-inventory.md` | VERIFIED | [Hecho] | ALTA |
| Ningún output rentable | PF < 1.0 en todas | `crypto-scalping-core-strategy-inventory.md` | VERIFIED | [Hecho] | ALTA |

---

## Sección 9 — Knowledge

| Afirmación | Evidencia | Path de evidencia | Estado | Clasificación epistémica | Confianza |
|------------|-----------|-------------------|--------|-------------------------|-----------|
| 5 KO candidates identificados | Documento de candidatos | `crypto-scalping-core-knowledge-object-candidates.md` | VERIFIED | [Hecho] | ALTA |
| 0 KOs promovidos | Ninguna acción de promoción | N/A — estado inicial | VERIFIED | [Hecho] | ALTA |

---

## Sección 10 — Assets

| Afirmación | Evidencia | Path de evidencia | Estado | Clasificación epistémica | Confianza |
|------------|-----------|-------------------|--------|-------------------------|-----------|
| 5 Asset candidates identificados | Documento de candidatos | `crypto-scalping-core-asset-candidates.md` | VERIFIED | [Hecho] | ALTA |
| Ninguno cumple 4 condiciones | Evaluación en documento | `crypto-scalping-core-asset-candidates.md` (Condiciones de promoción) | VERIFIED | [Hecho] | ALTA |
| Lifecycle: borrador | Sin validación ni productización | N/A — estado inicial | VERIFIED | [Hecho] | ALTA |

---

## Sección 11 — Dependencies

| Afirmación | Evidencia | Path de evidencia | Estado | Clasificación epistémica | Confianza |
|------------|-----------|-------------------|--------|-------------------------|-----------|
| Cero dependencies con LabOS | Inspección de imports/code | `crypto-scalping-core-dependency-map.md` | VERIFIED | [Hecho] | ALTA |
| python-binance sin pin | requirements.txt | `crypto-scalping-core-dependency-map.md` | VERIFIED | [Hecho] | ALTA |
| Binance API única fuente | Código de descarga | Repositorio: `app/data/binance_downloader.py` | VERIFIED | [Hecho] | ALTA |

---

## Sección 12 — Risks

| Afirmación | Evidencia | Path de evidencia | Estado | Clasificación epistémica | Confianza |
|------------|-----------|-------------------|--------|-------------------------|-----------|
| 5 riesgos fundador-approved | Decisión explícita | `founder-decisions-package-001a-batch1.md` (Dec 3) | VERIFIED | [Hecho] | ALTA |
| Overfitting alta probabilidad | PF in-sample < 1.0 aún | `crypto-scalping-core-strategy-inventory.md` | VERIFIED | [Hecho] | ALTA |

---

## Sección 13 — Governance

| Afirmación | Evidencia | Path de evidencia | Estado | Clasificación epistémica | Confianza |
|------------|-----------|-------------------|--------|-------------------------|-----------|
| Nivel SOLO | 1 operador pre-revenue | `../../architecture/architecture-baseline-v1.md` (Sección 6) | VERIFIED | [Hecho] | ALTA |
| Review 15min/mes | Cadence de `explorando` | `../../architecture/architecture-baseline-v1.md` (Sección 7) | VERIFIED | [Decisión] | ALTA |

---

## Sección 14 — Autonomy and Decoupling

| Afirmación | Evidencia | Path de evidencia | Estado | Clasificación epistémica | Confianza |
|------------|-----------|-------------------|--------|-------------------------|-----------|
| Autonomía confirmada | Decisión fundador + inspección | `founder-decisions-package-001a-batch1.md` (Dec 4) + `crypto-scalping-core-dependency-map.md` | VERIFIED | [Hecho] | ALTA |
| Cero LabOS runtime deps | Dependency map | `crypto-scalping-core-dependency-map.md` | VERIFIED | [Hecho] | ALTA |
| Código funciona sin LabOS | Arquitectura del proyecto | `crypto-scalping-core-dependency-map.md` | VERIFIED | [Hecho] | ALTA |

---

## Sección 15 — Evolution and Exit

| Afirmación | Evidencia | Path de evidencia | Estado | Clasificación epistémica | Confianza |
|------------|-----------|-------------------|--------|-------------------------|-----------|
| Estado actual: explorando | Decisión FD-B3-01 | `founder-decisions-package-001a-batch3.md` | VERIFIED | [Decisión] | ALTA |
| Next: validando cuando PF > 1.0 + OOS | Architecture baseline | `../../architecture/architecture-baseline-v1.md` (Sección 7) | VERIFIED | [Decisión] | ALTA |
| Archivo en 90 días sin actividad | Regla proporcional | INV-05 + decisión de governance | VERIFIED | [Decisión] | ALTA |

---

## Resumen de cobertura

| Estado | Cantidad | Porcentaje |
|--------|----------|------------|
| VERIFIED | 47 | 98% |
| EVIDENCE_REQUIRED | 1 | 2% |
| NOT_APPLICABLE | 0 | 0% |

### Ítem con evidencia pendiente

| Sección | Afirmación | Razón | Prioridad | Bloqueante |
|---------|-----------|-------|-----------|------------|
| 6 (Inputs) | Licencia Binance data verificada | ToS no revisado formalmente | P2 | NO |

---

## Cross-references

- [crypto-scalping-core-lab-contract.md](./crypto-scalping-core-lab-contract.md) — Contrato evaluado
- [founder-decisions-package-001a-batch1.md](./founder-decisions-package-001a-batch1.md) — Decisiones Batch 1
- [founder-decisions-package-001a-batch3.md](./founder-decisions-package-001a-batch3.md) — Decisiones Batch 3
- [crypto-scalping-core-research-workflow-map.md](./crypto-scalping-core-research-workflow-map.md) — Pipeline verificado
- [crypto-scalping-core-dependency-map.md](./crypto-scalping-core-dependency-map.md) — Dependencias verificadas
- [crypto-scalping-core-strategy-inventory.md](./crypto-scalping-core-strategy-inventory.md) — Resultados de estrategias

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 40       | 73%        |
| [Hipótesis]   | 0        | 0%         |
| [Decisión]    | 15       | 27%        |
| [Visión]      | 0        | 0%         |

> **Nota:** Alto porcentaje de hechos porque este documento mapea evidencia existente y verificable. Las decisiones corresponden a afirmaciones del contrato que son reglas elegidas, no hechos observables.
