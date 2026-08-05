# Inventario de Estrategias — Crypto Scalping Core

## Metadata

| Campo | Valor |
|-------|-------|
| **Documento** | Inventario de estrategias |
| **Lab** | Crypto Scalping Core |
| **Package** | 001A — First Lab Integration |
| **Batch** | 2 — Repository Discovery & Inventory |
| **Fecha** | 2025-07-24 |

---

## Propósito

Documentar todas las estrategias de trading encontradas en el repositorio, su estado de investigación y resultados evidenciados. [Hecho]

**NOTA CRÍTICA:** Ninguna estrategia ha demostrado rentabilidad (PF > 1.0) en las configuraciones probadas. [Hecho] TODAS muestran expectancy negativa.

---

## Estrategia 1: Donchian Breakout (Principal)

| Campo | Valor |
|-------|-------|
| Archivo | `app/strategies/breakout_trend.py` [Hecho] |
| Configuración | `app/config/breakout_config.py` [Hecho] |
| Tipo | Breakout / Trend-following [Hecho] |
| Timeframes probados | 5m (principal), 15m [Hecho] |
| Experimentos formales | EXP-000002 a EXP-000014 (~13 experimentos) [Hecho] |
| Total configs evaluadas | ~550+ (mayoría de las 567 totales) [Hecho] |
| Mejor PF obtenido | 0.7755 (5m, donchian_breakout_5m_smoke_v1.csv) [Hecho] |
| Mejor expectancy | -0.0483 (15m, EXP-000014) [Hecho] |
| Dataset | `data/BTCUSDT_1m.csv` resampled a 5m/15m [Hecho] |
| Estado | **RESEARCH** — expectancy negativa, NO CANDIDATA [Hecho] |

### Parámetros clave

| Parámetro | Importancia (correlación con PF) | Mejor valor observado |
|-----------|----------------------------------|----------------------|
| stop_loss_pct | 0.7865 (máxima) | 0.005-0.008 [Hecho] |
| take_profit_pct | 0.7468 | 0.006-0.012 [Hecho] |
| lookback | 0.6145 (corr. expectancy) | 10 [Hecho] |
| volume_ratio | 0.5043 | 1.0 [Hecho] |
| max_holding_candles | 0.2966 | 36 [Hecho] |

### Hallazgos del quality analysis (15m)

- quality_score >= 6 muestra PF > 1.0 en análisis de quartiles (1.08-1.19) [Hecho]
- close_location_value > 0.923 muestra PF = 1.556 en el quartil superior [Hecho]
- Estos hallazgos son de SUBSETS del dataset, no del conjunto completo [Hecho]
- El PF global de la estrategia sigue siendo < 1.0 [Hecho]

---

## Estrategia 2: RSI Mean Reversion

| Campo | Valor |
|-------|-------|
| Archivo | `app/strategies/rsi_mean_reversion.py` [Hecho] |
| Configuración | `app/config/rsi_config.py` [Hecho] |
| Tipo | Mean reversion basada en RSI [Hecho] |
| Timeframes probados | 1m [Hecho] |
| Experimentos formales | EXP-000001 [Hecho] |
| Total configs evaluadas | 48 [Hecho] |
| Mejor PF obtenido | 0.5136 [Hecho] |
| Mejor expectancy | -0.0718 [Hecho] |
| Max drawdown | 169.21 (significativo) [Hecho] |
| Total trades | 2354 (alta frecuencia) [Hecho] |
| Estado | **RESEARCH** — expectancy negativa, DESCARTADA en configuraciones probadas [Hecho] |

### Parámetros probados

| Parámetro | Rango |
|-----------|-------|
| rsi_threshold | 25, 30, 35 [Hecho] |
| distance_from_ema20 | -0.0015, -0.002 [Hecho] |
| volume_ratio | 0.8, 1.0 [Hecho] |
| take_profit_pct | 0.0025, 0.003 [Hecho] |
| stop_loss_pct | 0.002 [Hecho] |
| max_holding_candles | 15, 20 [Hecho] |

---

## Estrategia 3: High Volatility Engine

| Campo | Valor |
|-------|-------|
| Archivo | `app/strategies/high_vol_engine.py` [Hecho] |
| Tipo | Motor especializado para alta volatilidad [Hecho] |
| Experimentos formales | NINGUNO identificado en research/journal/ [Hecho] |
| Documentación de diseño | `audit/high_vol_edge_extraction_plan.md` [Hecho] |
| Estado | **RESEARCH** — sin evidencia de ejecución de backtest formal [Hecho] |

---

## Estrategia 4: Multi-Strategy Engine (Orquestador)

| Campo | Valor |
|-------|-------|
| Archivo | `app/strategies/multi_strategy_engine.py` [Hecho] |
| Tipo | Orquestador que combina múltiples estrategias [Hecho] |
| Experimentos formales | NINGUNO como sistema combinado [Hecho] |
| Estado | **RESEARCH** — framework de orquestación sin validación como sistema [Hecho] |

---

## Resumen de estados

| Estrategia | Estado | Mejor PF | Candidata a producción |
|-----------|--------|----------|------------------------|
| Donchian Breakout | RESEARCH | 0.7755 | **NO** — PF < 1.0 [Hecho] |
| RSI Mean Reversion | RESEARCH | 0.5136 | **NO** — PF < 1.0, descartada [Hecho] |
| High Vol Engine | RESEARCH | N/A | **NO** — sin evidencia de testing [Hecho] |
| Multi-Strategy Engine | RESEARCH | N/A | **NO** — sin validación [Hecho] |

---

## Criterio de promoción a CANDIDATA

Para que una estrategia pase de RESEARCH a CANDIDATA, debe cumplir: [Decisión]

1. PF > 1.0 sostenido en in-sample (requisito mínimo absoluto)
2. Walk-forward validation positiva (out-of-sample)
3. Monte Carlo robustness > percentil 5 positivo
4. Drawdown máximo aceptable (definido por risk parameters)

**Estado actual:** NINGUNA estrategia cumple siquiera el criterio 1. [Hecho]

---

## Implicaciones para LabOS

- El Lab está en fase de **investigación pura** — no hay edge demostrado. [Hecho]
- La infraestructura de testing es funcional y produce datos. [Hecho]
- El pipeline identifica correctamente que no hay estrategia viable — esto es un resultado VÁLIDO de investigación. [Hecho]
- NO se debe comunicar ninguna estrategia como "funcional" o "lista para trading". [Hecho]

---

## Cross-references

- [crypto-scalping-core-research-workflow-map.md](./crypto-scalping-core-research-workflow-map.md) — Pipeline de evaluación
- [crypto-scalping-core-research-artifacts-inventory.md](./crypto-scalping-core-research-artifacts-inventory.md) — Resultados de experimentos
- [crypto-scalping-core-knowledge-object-candidates.md](./crypto-scalping-core-knowledge-object-candidates.md) — Conocimiento derivado
- [crypto-scalping-core-monetization-hypothesis.md](./crypto-scalping-core-monetization-hypothesis.md) — Hipótesis de monetización

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 40       | 95%        |
| [Hipótesis]   | 0        | 0%         |
| [Decisión]    | 2        | 5%         |
| [Visión]      | 0        | 0%         |
