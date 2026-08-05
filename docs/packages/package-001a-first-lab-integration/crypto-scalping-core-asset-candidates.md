# Candidatos a Asset — Crypto Scalping Core

## Metadata

| Campo | Valor |
|-------|-------|
| **Documento** | Candidatos a Asset |
| **Lab** | Crypto Scalping Core |
| **Package** | 001A — First Lab Integration |
| **Batch** | 2 — Repository Discovery & Inventory |
| **Fecha** | 2025-07-24 |

---

## Propósito

Identificar componentes del repositorio que podrían promoverse a Assets formales del Lab, siguiendo la taxonomía canónica de 7 tipos (ref: ADR-0002). [Hecho] Todos los candidatos están actualmente acoplados al proyecto y requieren trabajo de extracción.

---

## Candidato ASSET-1: Framework de backtesting

| Campo | Valor |
|-------|-------|
| Nombre propuesto | "Framework de backtesting para estrategias de trading" |
| Tipo canónico | Herramienta [Decisión] |
| Ubicación actual | `app/research/backtester.py` + `app/research/simulation.py` [Hecho] |
| Descripción | Motor de backtesting que evalúa estrategias contra datos históricos OHLCV. Calcula PF, expectancy, drawdown, win/loss por configuración. [Hecho] |
| Hipótesis de uso | Cualquier lab de trading cuantitativo necesita un backtester — potencial como herramienta educativa o componente reutilizable. [Hipótesis] |
| Estado actual | Funcional dentro del proyecto, acoplado a las estrategias específicas [Hecho] |
| Esfuerzo de extracción | MEDIO — requiere desacoplar de las estrategias específicas y generalizar interfaz [Hipótesis] |
| Reutilización cross-lab | Atlas Wealth Labs (potencial), otros labs de trading [Hipótesis] |

---

## Candidato ASSET-2: Optimizador Grid Search

| Campo | Valor |
|-------|-------|
| Nombre propuesto | "Optimizador de parámetros por grid search con leaderboard" |
| Tipo canónico | Herramienta [Decisión] |
| Ubicación actual | `app/optimization/grid_search.py` [Hecho] |
| Descripción | Ejecuta búsqueda exhaustiva de parámetros, evalúa cada combinación vía backtester, genera leaderboard CSV con rankings. Soporta configuración YAML. [Hecho] |
| Hipótesis de uso | Optimización de parámetros es un problema genérico en research cuantitativo — potencial como herramienta independiente. [Hipótesis] |
| Estado actual | Funcional, ejecutado 14+ veces con resultados documentados [Hecho] |
| Esfuerzo de extracción | MEDIO — interfaz de estrategia necesita abstracción [Hipótesis] |
| Reutilización cross-lab | Alta — cualquier lab con optimización de parámetros [Hipótesis] |

---

## Candidato ASSET-3: Template de experiment journal

| Campo | Valor |
|-------|-------|
| Nombre propuesto | "Template de journal de experimentación cuantitativa" |
| Tipo canónico | Template [Decisión] |
| Ubicación actual | Formato implícito en `research/journal/EXP-*.md` (14 instancias) [Hecho] |
| Descripción | Estructura estándar para registrar experimentos: ID, objective, hypothesis, dataset, strategy, timeframe, parameter grid, results, best configuration, lessons learned, recommendations. [Hecho] |
| Hipótesis de uso | Cualquier lab de investigación necesita un formato reproducible de registro de experimentos. Compatible con Package 001 principles. [Hipótesis] |
| Estado actual | Formato implícito generado automáticamente por el optimizer [Hecho] |
| Esfuerzo de extracción | BAJO — ya es un formato documentable como template [Hecho] |
| Reutilización cross-lab | MUY ALTA — aplicable a cualquier investigación estructurada [Hecho] |

---

## Candidato ASSET-4: Pipeline de discovery report

| Campo | Valor |
|-------|-------|
| Nombre propuesto | "Pipeline de generación de discovery report automatizado" |
| Tipo canónico | Herramienta [Decisión] |
| Ubicación actual | `app/research/discovery/` [Hecho] |
| Descripción | Pipeline que analiza múltiples leaderboards y genera un reporte ejecutivo con: best experiments, parameter importance (correlación), pattern discovery, recommendations. [Hecho] |
| Hipótesis de uso | La síntesis cross-experimentos es valiosa para cualquier investigación con múltiples runs — potencial como herramienta de análisis. [Hipótesis] |
| Estado actual | Funcional, genera `research/reports/discovery_report.md` [Hecho] |
| Esfuerzo de extracción | ALTO — lógica de análisis es genérica pero integrada al proyecto [Hipótesis] |
| Reutilización cross-lab | Media — útil para labs con optimización iterativa [Hipótesis] |

---

## Candidato ASSET-5: Pipeline de quality analysis

| Campo | Valor |
|-------|-------|
| Nombre propuesto | "Pipeline de análisis de calidad de señales de trading" |
| Tipo canónico | Herramienta [Decisión] |
| Ubicación actual | `app/research/signal_quality/` [Hecho] |
| Descripción | Analiza trades individuales: winner vs loser feature comparison, feature quartile analysis, quality score bucketing, correlación con net P&L. Genera reporte markdown automáticamente. [Hecho] |
| Hipótesis de uso | El análisis de calidad de señales es una necesidad común en trading cuantitativo — metodología potencialmente valiosa como herramienta. [Hipótesis] |
| Estado actual | Funcional, genera quality analysis report [Hecho] |
| Esfuerzo de extracción | ALTO — metodología es exportable pero código está integrado [Hipótesis] |
| Reutilización cross-lab | Media — específico a trading pero metodología generalizable [Hipótesis] |

---

## Evaluación de prioridad

| Asset | Esfuerzo | Reutilización | Prioridad propuesta | Justificación |
|-------|----------|---------------|--------------------|----|
| ASSET-3 (Template journal) | BAJO | MUY ALTA | **P1** | Mínimo esfuerzo, máximo reuso, alineado con Package 001 [Decisión] |
| ASSET-2 (Grid search) | MEDIO | ALTA | **P2** | Herramienta probada, requiere extracción [Decisión] |
| ASSET-1 (Backtester) | MEDIO | ALTA | **P2** | Funcional pero acoplado [Decisión] |
| ASSET-4 (Discovery) | ALTO | MEDIA | **P3** | Útil pero esfuerzo alto [Decisión] |
| ASSET-5 (Quality analysis) | ALTO | MEDIA | **P3** | Metodología valiosa pero muy integrada [Decisión] |

---

## Condiciones de promoción

Antes de promover cualquier candidato a Asset formal, debe cumplirse: [Decisión]

1. **Desacoplamiento** — el componente debe funcionar independientemente del proyecto
2. **Documentación** — README, usage examples, API clara
3. **5 campos mínimos** — nombre, tipo, descripción, hipótesis de uso, estado (ref: ADR-0002)
4. **Hipótesis de monetización** — documentada como [Hipótesis] (ref: Asset_First_Model)

**Estado actual:** NINGÚN candidato cumple las 4 condiciones todavía. [Hecho] Todos requieren trabajo de extracción.

---

## Nota sobre acoplamiento

Todos los candidatos están actualmente **tightly coupled** al repositorio `crypto-scalping-core`: [Hecho]

- Importan módulos internos del proyecto
- Usan la estructura de datos específica del backtester
- Dependen del formato de configuración YAML del proyecto
- No tienen interfaces públicas definidas

El esfuerzo de extracción es real pero no bloquea su documentación como candidatos. [Hecho]

---

## Cross-references

- [ADR-0002 — Consolidación de Taxonomía de Activos](../../decisions/0002-asset-taxonomy-consolidation.md) — 7 tipos canónicos
- [knowledge-to-asset-handoff.md](../package-002-knowledge-architecture/knowledge-to-asset-handoff.md) — Proceso de handoff
- [crypto-scalping-core-knowledge-object-candidates.md](./crypto-scalping-core-knowledge-object-candidates.md) — KOs que informan estos Assets
- [crypto-scalping-core-monetization-hypothesis.md](./crypto-scalping-core-monetization-hypothesis.md) — Hipótesis de monetización

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 22       | 52%        |
| [Hipótesis]   | 12       | 29%        |
| [Decisión]    | 8        | 19%        |
| [Visión]      | 0        | 0%         |

> **Nota:** Alto porcentaje de hipótesis porque las evaluaciones de reutilización y esfuerzo son estimaciones sin validación.
