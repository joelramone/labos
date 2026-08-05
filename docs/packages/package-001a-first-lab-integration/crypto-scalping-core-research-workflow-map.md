# Mapa de Flujo de Investigación — Crypto Scalping Core

## Metadata

| Campo | Valor |
|-------|-------|
| **Documento** | Mapa de flujo de investigación |
| **Lab** | Crypto Scalping Core |
| **Package** | 001A — First Lab Integration |
| **Batch** | 2 — Repository Discovery & Inventory |
| **Fecha** | 2025-07-24 |

---

## Propósito

Documentar el flujo de trabajo de investigación REAL evidenciado por los artefactos del repositorio. [Hecho] No se documentan flujos aspiracionales — solo lo que se puede verificar.

---

## Flujo de trabajo evidenciado

```text
┌─────────────────────────────────────────────────────────────────────────┐
│                    PIPELINE DE INVESTIGACIÓN ACTIVO                      │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  [1] Descarga de datos ──→ [2] Generación de features ──→              │
│         (Binance API)              (app/research/features.py)           │
│                                                                         │
│  ──→ [3] Definición de estrategia ──→ [4] Grid search ──→              │
│         (app/strategies/)                (app/optimization/)            │
│                                                                         │
│  ──→ [5] Registro en leaderboard ──→ [6] Discovery report ──→          │
│         (research/leaderboards/)        (research/reports/)             │
│                                                                         │
│  ──→ [7] Quality analysis ──→ [8] Exportar señales candidatas          │
│         (app/research/signal_quality/)   (research/candidate_signals/)  │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘


┌─────────────────────────────────────────────────────────────────────────┐
│                   PIPELINE PARCIALMENTE IMPLEMENTADO                     │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  [9] Walk-forward validation                                            │
│       Código: app/optimization/walk_forward.py ── EXISTE                │
│       Outputs: research/walk_forward/ ── VACÍO (.gitkeep)               │
│       Estado: PARCIALMENTE IMPLEMENTADO                                 │
│                                                                         │
│  [10] Monte Carlo simulation                                            │
│       Código: app/montecarlo.py ── EXISTE                               │
│       Outputs: research/monte_carlo/ ── VACÍO (.gitkeep)                │
│       Estado: PARCIALMENTE IMPLEMENTADO                                 │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│                        PIPELINE NO IMPLEMENTADO                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  [11] Machine Learning                                                  │
│       Directorio: research/ml/ ── VACÍO (.gitkeep)                      │
│       Estado: PLANIFICADO, SIN CÓDIGO NI OUTPUTS                        │
│                                                                         │
│  [12] Feature Store versionado                                          │
│       Directorio: research/feature_store/ ── VACÍO (.gitkeep)           │
│       Estado: PLANIFICADO, SIN IMPLEMENTACIÓN                           │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Detalle por etapa

### Etapa 1: Descarga de datos [ACTIVO]

| Campo | Valor |
|-------|-------|
| Herramienta | `app/research/download_data.py` [Hecho] |
| Fuente | Binance USD-M Futures API [Hecho] |
| Output | `data/BTCUSDT_1m.csv` (confirmado existente) [Hecho] |
| Comando | `python -m app.research.download_data --symbol BTCUSDT --interval 1m` [Hecho] |
| Estado | **OPERATIVO** — evidencia de ejecución exitosa [Hecho] |

### Etapa 2: Generación de features [ACTIVO]

| Campo | Valor |
|-------|-------|
| Herramienta | `app/research/features.py`, `app/data/features.py` [Hecho] |
| Input | CSV de velas OHLCV [Hecho] |
| Features generados | RSI, EMA, ATR, volume_ratio, quality_score, body_to_range, close_location, range_expansion, atr_expansion, ema_slope, ema_alignment, breakout_distance [Hecho] |
| Estado | **OPERATIVO** — features referenciados en quality analysis [Hecho] |

### Etapa 3: Definición de estrategia [ACTIVO]

| Campo | Valor |
|-------|-------|
| Herramienta | `app/strategies/` (4 implementaciones) [Hecho] |
| Estrategia principal actual | donchian_breakout (breakout_trend.py) [Hecho] |
| Estrategia anterior | mean_reversion (rsi_mean_reversion.py) [Hecho] |
| Parámetros configurables | lookback, volume_ratio, TP, SL, max_holding, quality filters [Hecho] |
| Estado | **OPERATIVO** [Hecho] |

### Etapa 4: Grid search optimization [ACTIVO]

| Campo | Valor |
|-------|-------|
| Herramienta | `app/optimization/grid_search.py` [Hecho] |
| Configuración | YAMLs en `research/optimization/grid_search/` [Hecho] |
| Métricas evaluadas | Profit Factor, Expectancy, Max Drawdown, Total Trades [Hecho] |
| Total ejecuciones documentadas | 567 configuraciones evaluadas [Hecho] |
| Estado | **OPERATIVO** — 14 experimentos formales completados [Hecho] |

### Etapa 5: Registro en leaderboard [ACTIVO]

| Campo | Valor |
|-------|-------|
| Output | 8 CSVs en `research/leaderboards/` [Hecho] |
| Formato | Rankings por Profit Factor descendente [Hecho] |
| Estado | **OPERATIVO** [Hecho] |

### Etapa 6: Discovery report [ACTIVO]

| Campo | Valor |
|-------|-------|
| Herramienta | `app/research/discovery/` [Hecho] |
| Output | `research/reports/discovery_report.md` [Hecho] |
| Contenido | Executive summary, best experiments, parameter importance, pattern discovery, recommendations [Hecho] |
| Estado | **OPERATIVO** — al menos 1 ejecución completa confirmada [Hecho] |

### Etapa 7: Quality analysis [ACTIVO]

| Campo | Valor |
|-------|-------|
| Herramienta | `app/research/signal_quality/` [Hecho] |
| Output | `research/reports/donchian_breakout_15m_quality_analysis_v1.md` [Hecho] |
| Contenido | Winner vs Loser feature comparison, feature quartiles, quality score performance [Hecho] |
| Estado | **OPERATIVO** — al menos 1 ejecución completa confirmada [Hecho] |

### Etapa 8: Exportar señales candidatas [ACTIVO]

| Campo | Valor |
|-------|-------|
| Output | `research/candidate_signals/donchian_breakout_15m_candidates_v1.csv` [Hecho] |
| Estado | **OPERATIVO** — 1 CSV generado [Hecho] |

### Etapa 9: Walk-forward validation [PARCIAL]

| Campo | Valor |
|-------|-------|
| Código | `app/optimization/walk_forward.py` — EXISTE [Hecho] |
| Output esperado | `research/walk_forward/` — VACÍO [Hecho] |
| Estado | **PARCIALMENTE IMPLEMENTADO** — código existe pero sin evidencia de ejecución exitosa [Hecho] |

### Etapa 10: Monte Carlo simulation [PARCIAL]

| Campo | Valor |
|-------|-------|
| Código | `app/montecarlo.py` — EXISTE [Hecho] |
| Output esperado | `research/monte_carlo/` — VACÍO [Hecho] |
| Estado | **PARCIALMENTE IMPLEMENTADO** — código existe pero sin outputs generados [Hecho] |

---

## Registro de experimentos (Experiment Journal)

El pipeline incluye un sistema de registro formal con 14 entradas: [Hecho]

| Componente | Detalle |
|------------|---------|
| Ubicación | `research/journal/EXP-NNNNNN.md` [Hecho] |
| Formato estándar | ID, Fecha, Objective, Hypothesis, Dataset, Strategy, Timeframe, Parameter Grid, Results, Best Configuration, Lessons Learned, Recommendations [Hecho] |
| Automatización | Los journals se generan automáticamente al finalizar cada optimizer run [Hecho] |

---

## Hallazgos sobre el flujo

1. **Pipeline funcional de 8 etapas confirmado** con evidencia de ejecución real. [Hecho]
2. **Etapas 9-10 tienen código pero no outputs** — parcialmente implementadas. [Hecho]
3. **No hay feedback loop automático** — las recomendaciones del journal son manuales. [Hecho]
4. **El flujo es lineal, no cíclico** — no hay evidencia de re-optimización automatizada basada en resultados previos. [Hecho]
5. **Ningún experimento ha cruzado el umbral de profitabilidad** (PF > 1.0) — el pipeline genera datos pero no ha producido una estrategia viable. [Hecho]

---

## Cross-references

- [crypto-scalping-core-repository-structure.md](./crypto-scalping-core-repository-structure.md) — Estructura del repositorio
- [crypto-scalping-core-research-artifacts-inventory.md](./crypto-scalping-core-research-artifacts-inventory.md) — Artefactos producidos
- [crypto-scalping-core-strategy-inventory.md](./crypto-scalping-core-strategy-inventory.md) — Estrategias evaluadas
- [crypto-scalping-core-knowledge-object-candidates.md](./crypto-scalping-core-knowledge-object-candidates.md) — Conocimiento derivado

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 45       | 100%       |
| [Hipótesis]   | 0        | 0%         |
| [Decisión]    | 0        | 0%         |
| [Visión]      | 0        | 0%         |

> **Nota:** Documento puramente descriptivo basado en evidencia directa del repositorio.
