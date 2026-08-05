# Candidatos a Knowledge Object — Crypto Scalping Core

## Metadata

| Campo | Valor |
|-------|-------|
| **Documento** | Candidatos a Knowledge Object |
| **Lab** | Crypto Scalping Core |
| **Package** | 001A — First Lab Integration |
| **Batch** | 2 — Repository Discovery & Inventory |
| **Fecha** | 2025-07-24 |

---

## Propósito

Identificar conocimiento sintetizado en el repositorio que podría formalizarse como Knowledge Objects (KOs) según el contrato definido en Package 002. [Hecho] Todos los candidatos son PRIVADOS al Lab hasta publicación explícita.

---

## Candidato KO-1: Mejor timeframe para donchian_breakout

| Campo | Valor |
|-------|-------|
| Título propuesto | "El timeframe 5m produce el mejor PF promedio para donchian_breakout en BTCUSDT" |
| Tipo | `finding` |
| Summary | De 567 configuraciones evaluadas en timeframes 5m y 15m, el timeframe 5m produce consistentemente el mejor Profit Factor promedio (best individual PF = 0.7755 vs 0.8719 en 15m pero con promedio inferior). [Hecho] |
| Fuente | `research/reports/discovery_report.md` — "Best timeframe by average PF: 5m" [Hecho] |
| Confianza | MEDIO — basado en un único par (BTCUSDT) y un período de datos sin validación out-of-sample [Hecho] |
| Sensibilidad | Lab-Private [Decisión] |
| Validity window | 90 días — condiciones de mercado crypto cambian rápidamente [Hecho] |
| Limitaciones | Un solo par, un solo período, sin confirmación en otros mercados [Hecho] |

---

## Candidato KO-2: stop_loss_pct tiene máxima correlación con PF

| Campo | Valor |
|-------|-------|
| Título propuesto | "stop_loss_pct es el parámetro con mayor correlación con Profit Factor (r=0.7865)" |
| Tipo | `finding` |
| Summary | En el analysis de parameter importance sobre 567 configuraciones de donchian_breakout, stop_loss_pct muestra la correlación lineal más fuerte con Profit Factor (0.7865), seguido por take_profit_pct (0.7468). Esto sugiere que el control de riesgo es más determinante que las señales de entrada. [Hecho] |
| Fuente | `research/reports/discovery_report.md` — tabla "Parameter Importance" [Hecho] |
| Confianza | MEDIO — correlación lineal puede no capturar relaciones no-lineales, basado en dataset único [Hecho] |
| Sensibilidad | Lab-Private [Decisión] |
| Validity window | 180 días — hallazgo metodológico más estable que hallazgos de mercado [Hecho] |

---

## Candidato KO-3: quality_score filtering mejora expectancy en subsets

| Campo | Valor |
|-------|-------|
| Título propuesto | "Filtrar trades por quality_score >= 6 mejora PF de 1.01 a 1.08-1.19 en quartile analysis" |
| Tipo | `finding` |
| Summary | El análisis de quartiles del quality_score en 564 trades de donchian_breakout 15m muestra que quality_score > 5 produce PF positivo (1.085 para score 6, 1.192 para score 7), mientras que score <= 5 tiene PF cercano a 1.0. Sin embargo, el PF GLOBAL sigue siendo < 1.0. [Hecho] |
| Fuente | `research/reports/donchian_breakout_15m_quality_analysis_v1.md` — tabla "Quality Score Performance" [Hecho] |
| Confianza | MEDIO — hallazgo estadístico en-sample sin confirmación out-of-sample. Posible data mining bias. [Hecho] |
| Sensibilidad | Lab-Private [Decisión] |
| Validity window | 90 días [Hecho] |
| Limitaciones | Subset analysis puede generar ilusión de edge por multiple comparisons [Hecho] |

---

## Candidato KO-4: mean_reversion a 1m no es rentable con parámetros probados

| Campo | Valor |
|-------|-------|
| Título propuesto | "Mean reversion RSI en 1m BTC/USDT produce PF máximo de 0.5136 con 48 configuraciones evaluadas" |
| Tipo | `finding` |
| Summary | Un sweep de 48 configuraciones de mean_reversion en timeframe 1m (6 parámetros, rango completo) produce un PF máximo de 0.5136 con expectancy -0.0718 y drawdown de 169.21. La estrategia es decisivamente no rentable en este timeframe y par. [Hecho] |
| Fuente | `research/journal/EXP-000001.md` [Hecho] |
| Confianza | ALTO — 48 configuraciones con resultado uniforme negativo proporcionan evidencia fuerte de no-viabilidad [Hecho] |
| Sensibilidad | Lab-Private [Decisión] |
| Validity window | 365 días — resultado negativo robusto [Hecho] |

---

## Candidato KO-5: Pipeline grid search → leaderboard → quality analysis

| Campo | Valor |
|-------|-------|
| Título propuesto | "Pipeline de investigación: grid search → leaderboard → discovery report → quality analysis" |
| Tipo | `methodology` |
| Summary | El Lab ha desarrollado un pipeline reproducible de 8 etapas que automatiza: descarga de datos, generación de features, optimización por grid search, ranking en leaderboard, generación de discovery report con parameter importance, y quality analysis por feature quartiles. El pipeline produce 14 tipos de artefactos documentados. [Hecho] |
| Fuente | Múltiples: `app/research/`, `app/optimization/`, `research/` (evidencia en 14 experiments + 8 leaderboards + 2 reports) [Hecho] |
| Confianza | ALTO — pipeline ejecutado 14+ veces con outputs verificables [Hecho] |
| Sensibilidad | Lab-Private (proceso), potencialmente Lab-Published (metodología genérica) [Decisión] |
| Validity window | 365 días — metodología estable [Hecho] |
| Potencial de reutilización | ALTO — aplicable a cualquier estrategia de trading cuantitativo [Hecho] |

---

## Resumen de candidatos

| KO | Tipo | Confianza | Reutilización cross-lab | Prioridad |
|----|------|-----------|------------------------|-----------|
| KO-1 | finding | MEDIO | Baja — específico al par/timeframe | P2 |
| KO-2 | finding | MEDIO | Media — hallazgo de diseño de estrategia | P2 |
| KO-3 | finding | MEDIO | Baja — requiere validación adicional | P3 |
| KO-4 | finding | ALTO | Baja — resultado negativo específico | P2 |
| KO-5 | methodology | ALTO | ALTA — pipeline genérico aplicable a otros labs | P1 |

---

## Notas sobre confianza

Todos los candidatos KO excepto KO-5 comparten las mismas limitaciones: [Hecho]

1. **Dataset único** — solo BTCUSDT_1m.csv como fuente
2. **Sin validación out-of-sample** — walk-forward no ejecutado
3. **Sin robustez verificada** — Monte Carlo no ejecutado
4. **Un solo par de trading** — no hay diversificación de mercados
5. **Un solo período temporal** — no se conoce la estabilidad temporal

Estas limitaciones reducen la confianza de ALTO a MEDIO para hallazgos de mercado. [Hecho]

---

## Cross-references

- [knowledge-object-contract.md](../package-002-knowledge-architecture/knowledge-object-contract.md) — Contrato KO (formato requerido)
- [crypto-scalping-core-research-artifacts-inventory.md](./crypto-scalping-core-research-artifacts-inventory.md) — Fuentes de estos candidatos
- [crypto-scalping-core-asset-candidates.md](./crypto-scalping-core-asset-candidates.md) — Potencial handoff KO → Asset

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 28       | 82%        |
| [Hipótesis]   | 0        | 0%         |
| [Decisión]    | 6        | 18%        |
| [Visión]      | 0        | 0%         |
