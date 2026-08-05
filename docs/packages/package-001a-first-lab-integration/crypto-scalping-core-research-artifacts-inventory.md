# Inventario de Artefactos de Investigación — Crypto Scalping Core

## Metadata

| Campo | Valor |
|-------|-------|
| **Documento** | Inventario de artefactos de investigación |
| **Lab** | Crypto Scalping Core |
| **Package** | 001A — First Lab Integration |
| **Batch** | 2 — Repository Discovery & Inventory |
| **Fecha** | 2025-07-24 |

---

## Propósito

Inventario detallado de todos los artefactos de investigación producidos por el Lab, con clasificación de procedencia, freshness y confianza. [Hecho]

---

## Experiment Journals (14 entradas)

| ID | Estrategia | Timeframe | Configs evaluadas | Mejor PF | Mejor Expectancy | Procedencia | Freshness |
|----|-----------|-----------|-------------------|----------|-------------------|-------------|-----------|
| EXP-000001 | mean_reversion | 1m | 48 | 0.5136 | -0.0718 | COMPLETE | CURRENT [Hecho] |
| EXP-000002 | donchian_breakout | 5m | ~50+ | ~0.77 | negativa | COMPLETE | CURRENT [Hecho] |
| EXP-000003 | donchian_breakout | 5m | variable | <1.0 | negativa | COMPLETE | CURRENT [Hecho] |
| EXP-000004 | donchian_breakout | 5m | variable | <1.0 | negativa | COMPLETE | CURRENT [Hecho] |
| EXP-000005 | donchian_breakout | 5m | variable | <1.0 | negativa | COMPLETE | CURRENT [Hecho] |
| EXP-000006 | donchian_breakout | 5m | variable | <1.0 | negativa | COMPLETE | CURRENT [Hecho] |
| EXP-000007 | donchian_breakout | 5m | variable | <1.0 | negativa | COMPLETE | CURRENT [Hecho] |
| EXP-000008 | donchian_breakout | variable | variable | <1.0 | negativa | COMPLETE | CURRENT [Hecho] |
| EXP-000009 | donchian_breakout | variable | variable | <1.0 | negativa | COMPLETE | CURRENT [Hecho] |
| EXP-000010 | donchian_breakout | variable | variable | <1.0 | negativa | COMPLETE | CURRENT [Hecho] |
| EXP-000011 | donchian_breakout | variable | variable | <1.0 | negativa | COMPLETE | CURRENT [Hecho] |
| EXP-000012 | donchian_breakout | variable | variable | <1.0 | negativa | COMPLETE | CURRENT [Hecho] |
| EXP-000013 | donchian_breakout | variable | variable | <1.0 | negativa | COMPLETE | CURRENT [Hecho] |
| EXP-000014 | donchian_breakout | 15m | 2 | 0.8719 | -0.0483 | COMPLETE | CURRENT [Hecho] |

**Observación:** TODOS los experimentos muestran expectancy negativa (PF < 1.0). [Hecho]

---

## Leaderboards (8 CSVs)

| Archivo | Estrategia | Timeframe | Procedencia | Freshness |
|---------|-----------|-----------|-------------|-----------|
| donchian_breakout_5m_smoke_v1.csv | donchian_breakout | 5m | COMPLETE — generado por optimizer | CURRENT [Hecho] |
| donchian_breakout_5m_v2.csv | donchian_breakout | 5m | COMPLETE | CURRENT [Hecho] |
| donchian_breakout_5m_v3.csv | donchian_breakout | 5m | COMPLETE | CURRENT [Hecho] |
| donchian_breakout_5m_v4.csv | donchian_breakout | 5m | COMPLETE | CURRENT [Hecho] |
| donchian_breakout_15m_v1.csv | donchian_breakout | 15m | COMPLETE | CURRENT [Hecho] |
| donchian_breakout_15m_quality_regression.csv | donchian_breakout | 15m | COMPLETE | CURRENT [Hecho] |
| mean_reversion_1m_v1.csv | mean_reversion | 1m | COMPLETE | CURRENT [Hecho] |
| mean_reversion_1m_v2.csv | mean_reversion | 1m | COMPLETE | CURRENT [Hecho] |

---

## Reportes (2)

| Reporte | Contenido | Procedencia | Freshness | Confianza |
|---------|-----------|-------------|-----------|-----------|
| `discovery_report.md` | Resumen ejecutivo de 567 experimentos, parameter importance, pattern discovery, recommendations | COMPLETE — generado automáticamente por pipeline | CURRENT [Hecho] | MEDIO — basado en dataset único sin out-of-sample [Hecho] |
| `donchian_breakout_15m_quality_analysis_v1.md` | Feature analysis, winner/loser comparison, quality score performance, feature quartiles | COMPLETE — generado por signal_quality pipeline | CURRENT [Hecho] | MEDIO — análisis estadístico sin validación cruzada [Hecho] |

---

## Señales candidatas (1)

| Archivo | Contenido | Procedencia | Freshness | Confianza |
|---------|-----------|-------------|-----------|-----------|
| `donchian_breakout_15m_candidates_v1.csv` | Señales filtradas por quality criteria para potencial validación | COMPLETE | CURRENT [Hecho] | BAJO — señales con expectancy negativa aún [Hecho] |

---

## Datasets (3 en `data/`)

| Archivo | Fuente | Procedencia | Freshness | Licencia |
|---------|--------|-------------|-----------|----------|
| `BTCUSDT_1m.csv` | Binance USD-M Futures API | COMPLETE — descargado via download_data.py | CURRENT [Hecho] | NOT_FOUND — Binance ToS aplica [Hecho] |
| `binance_klines.csv` | Binance API | PARTIAL — sin metadata de descarga | UNKNOWN [Hecho] | NOT_FOUND [Hecho] |
| `sample_trades.csv` | Generado internamente (probable) | PARTIAL | UNKNOWN [Hecho] | N/A [Hecho] |

---

## Memory Index (1)

| Archivo | Contenido | Procedencia | Freshness |
|---------|-----------|-------------|-----------|
| `research/memory/index.csv` | Índice centralizado de investigación | COMPLETE | CURRENT [Hecho] |

---

## Clasificación de confianza general

| Artefacto | Confianza | Justificación |
|-----------|-----------|---------------|
| Journals | MEDIO | Registros completos pero basados en un solo dataset (BTCUSDT_1m.csv) sin validación out-of-sample [Hecho] |
| Leaderboards | MEDIO | Resultados reproducibles del optimizer, pero sujetos a overfitting potencial sin walk-forward [Hecho] |
| Discovery report | MEDIO | Síntesis automática correcta de los datos disponibles, pero universo limitado (1 par, 1 período) [Hecho] |
| Quality analysis | MEDIO | Metodología estadística sólida pero sin confirmación en datos independientes [Hecho] |
| Candidate signals | BAJO | Señales con expectancy negativa — no validadas para uso real [Hecho] |
| Datasets | MEDIO-BAJO | Datos de exchange confiables pero sin verificación de licencia formal [Hecho] |

---

## Artefactos ausentes (directorios vacíos)

| Directorio | Artefacto esperado | Razón de ausencia |
|------------|-------------------|-------------------|
| `research/walk_forward/` | Resultados de validación walk-forward | Código existe pero no ha sido ejecutado [Hecho] |
| `research/monte_carlo/` | Simulaciones de robustez | Código existe pero no ha sido ejecutado [Hecho] |
| `research/backtests/` | Outputs individuales de backtest | Posiblemente no se guardan individualmente [Hecho] |
| `research/ml/` | Modelos de machine learning | No implementado [Hecho] |
| `research/notebooks/` | Análisis exploratorio | No utilizado [Hecho] |
| `research/feature_store/` | Features versionados | No implementado [Hecho] |

---

## Cross-references

- [crypto-scalping-core-research-workflow-map.md](./crypto-scalping-core-research-workflow-map.md) — Flujo que produce estos artefactos
- [crypto-scalping-core-repository-inventory.md](./crypto-scalping-core-repository-inventory.md) — Inventario completo
- [crypto-scalping-core-knowledge-object-candidates.md](./crypto-scalping-core-knowledge-object-candidates.md) — Conocimiento derivado

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 44       | 100%       |
| [Hipótesis]   | 0        | 0%         |
| [Decisión]    | 0        | 0%         |
| [Visión]      | 0        | 0%         |
