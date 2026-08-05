# Inventario del Repositorio — Crypto Scalping Core

## Metadata

| Campo | Valor |
|-------|-------|
| **Documento** | Inventario del repositorio |
| **Lab** | Crypto Scalping Core |
| **Package** | 001A — First Lab Integration |
| **Batch** | 2 — Repository Discovery & Inventory |
| **Fecha** | 2025-07-24 |

---

## Propósito

Inventario estructurado de todos los componentes significativos del repositorio, clasificados por tipo, propósito y potencial de reutilización. [Hecho]

---

## Inventario de estrategias

| ID | Nombre | Tipo | Ruta | Propósito | Lifecycle | Sensibilidad | Reutilización |
|----|--------|------|------|-----------|-----------|--------------|---------------|
| STR-01 | breakout_trend | Herramienta | `app/strategies/breakout_trend.py` | Estrategia Donchian breakout (principal) | RESEARCH | Lab-Private | Media — acoplada al backtester |
| STR-02 | rsi_mean_reversion | Herramienta | `app/strategies/rsi_mean_reversion.py` | Estrategia mean reversion basada en RSI | RESEARCH | Lab-Private | Media — acoplada al backtester |
| STR-03 | high_vol_engine | Herramienta | `app/strategies/high_vol_engine.py` | Motor de alta volatilidad | RESEARCH | Lab-Private | Baja — sin evidencia de uso en experimentos |
| STR-04 | multi_strategy_engine | Herramienta | `app/strategies/multi_strategy_engine.py` | Orquestador multi-estrategia | RESEARCH | Lab-Private | Media — framework potencialmente reutilizable |

---

## Inventario de agentes

| ID | Nombre | Tipo | Ruta | Propósito | Lifecycle | Sensibilidad | Reutilización |
|----|--------|------|------|-----------|-----------|--------------|---------------|
| AGT-01 | strategy_agent | Componente | `app/agents/strategy_agent.py` | Genera señales de trading | RESEARCH | Lab-Private | Baja — específico al dominio |
| AGT-02 | risk_agent | Componente | `app/agents/risk_agent.py` | Valida límites de riesgo | RESEARCH | Lab-Private | Media — patrón reutilizable |
| AGT-03 | supervisor_agent | Componente | `app/agents/supervisor_agent.py` | Control de apagado automático | RESEARCH | Lab-Private | Media — patrón reutilizable |
| AGT-04 | regime_agent | Componente | `app/agents/regime_agent.py` | Detección de régimen de mercado | RESEARCH | Lab-Private | Baja — específico |
| AGT-05 | mean_reversion_agent | Componente | `app/agents/mean_reversion_agent.py` | Agente de mean reversion | RESEARCH | Lab-Private | Baja — específico |
| AGT-06 | volatility_regime_detector | Componente | `app/agents/volatility_regime_detector.py` | Detector de régimen de volatilidad | RESEARCH | Lab-Private | Baja — específico |

---

## Inventario de infraestructura de investigación

| ID | Nombre | Tipo | Ruta | Propósito | Lifecycle | Sensibilidad | Reutilización |
|----|--------|------|------|-----------|-----------|--------------|---------------|
| INF-01 | backtester | Herramienta | `app/research/backtester.py` | Motor de backtesting | OPERATIVO | Lab-Private | Alta — reutilizable con adaptaciones |
| INF-02 | grid_search | Herramienta | `app/optimization/grid_search.py` | Optimizador por grid search | OPERATIVO | Lab-Private | Alta — patrón genérico |
| INF-03 | walk_forward | Herramienta | `app/optimization/walk_forward.py` | Validación walk-forward | PARCIAL | Lab-Private | Alta — código existe, sin outputs |
| INF-04 | download_data | Herramienta | `app/research/download_data.py` | Descarga datos de Binance | OPERATIVO | Lab-Private | Media — acoplado a Binance |
| INF-05 | features | Herramienta | `app/research/features.py` | Generación de features técnicos | OPERATIVO | Lab-Private | Media — features estándar |
| INF-06 | simulation | Herramienta | `app/research/simulation.py` | Motor de simulación | OPERATIVO | Lab-Private | Media |
| INF-07 | discovery | Herramienta | `app/research/discovery/` | Pipeline de descubrimiento automatizado | OPERATIVO | Lab-Private | Alta — genera reportes automáticos |
| INF-08 | signal_quality | Herramienta | `app/research/signal_quality/` | Evaluación de calidad de señales | OPERATIVO | Lab-Private | Alta — metodología reutilizable |
| INF-09 | montecarlo | Herramienta | `app/montecarlo.py` | Simulación Monte Carlo | PARCIAL | Lab-Private | Media — código existe, sin outputs |

---

## Inventario de artefactos de investigación

| ID | Nombre | Tipo | Ruta | Propósito | Lifecycle | Sensibilidad | Reutilización |
|----|--------|------|------|-----------|-----------|--------------|---------------|
| ART-01 | Experiment Journal (×14) | Documento | `research/journal/EXP-000001.md` a `EXP-000014.md` | Registro formal de experimentos | COMPLETO | Lab-Private | Alta — template reutilizable |
| ART-02 | Leaderboards (×8) | Dataset | `research/leaderboards/*.csv` | Rankings de configuraciones optimizadas | COMPLETO | Lab-Private | Baja — específicos al dataset |
| ART-03 | Discovery Report | Documento | `research/reports/discovery_report.md` | Reporte de descubrimiento cross-experimentos | COMPLETO | Lab-Published | Alta — metodología reutilizable |
| ART-04 | Quality Analysis v1 | Documento | `research/reports/donchian_breakout_15m_quality_analysis_v1.md` | Análisis de calidad de señales | COMPLETO | Lab-Published | Alta — metodología reutilizable |
| ART-05 | Candidate Signals | Dataset | `research/candidate_signals/donchian_breakout_15m_candidates_v1.csv` | Señales candidatas para validación | COMPLETO | Lab-Private | Baja — específico |
| ART-06 | Memory Index | Dataset | `research/memory/index.csv` | Índice de memoria de investigación | OPERATIVO | Lab-Private | Media — patrón útil |

---

## Inventario de datasets

| ID | Nombre | Tipo | Ruta | Propósito | Lifecycle | Sensibilidad | Reutilización |
|----|--------|------|------|-----------|-----------|--------------|---------------|
| DAT-01 | BTCUSDT_1m | Dataset | `data/BTCUSDT_1m.csv` | Velas 1m BTC/USDT — dataset principal | OPERATIVO | RESTRICTED | Media — pendiente verificación de licencia |
| DAT-02 | binance_klines | Dataset | `data/binance_klines.csv` | Klines adicionales de Binance | OPERATIVO | RESTRICTED | Media — pendiente verificación de licencia |
| DAT-03 | sample_trades | Dataset | `data/sample_trades.csv` | Trades de ejemplo/testing | OPERATIVO | Lab-Private | Baja |

---

## Inventario de ejecución/trading

| ID | Nombre | Tipo | Ruta | Propósito | Lifecycle | Sensibilidad | Reutilización |
|----|--------|------|------|-----------|-----------|--------------|---------------|
| EXE-01 | executor | Componente | `app/trading/executor.py` | Motor de ejecución de órdenes | RESEARCH | Lab-Private | Media |
| EXE-02 | paper_wallet | Componente | `app/trading/paper_wallet.py` | Wallet de paper trading | RESEARCH | Lab-Private | Media — patrón útil |
| EXE-03 | live_bot | Componente | `app/live_bot.py` | Bot de trading live | INACTIVO | Lab-Private | Baja — sin evidencia de activación |
| EXE-04 | dashboard | Herramienta | `app/dashboard.py` | Dashboard Flask de monitoreo | RESEARCH | Lab-Private | Media |

---

## Inventario de documentación de auditoría

| ID | Nombre | Tipo | Ruta | Propósito | Lifecycle | Sensibilidad | Reutilización |
|----|--------|------|------|-----------|-----------|--------------|---------------|
| AUD-01 | high_vol_edge_extraction_plan | Documento | `audit/high_vol_edge_extraction_plan.md` | Plan de extracción de edge en alta volatilidad | COMPLETO | Lab-Private | Baja |
| AUD-02 | market_regime_adaptive_system_design | Documento | `audit/market_regime_adaptive_system_design.md` | Diseño de sistema adaptativo a régimen | COMPLETO | Lab-Private | Media |
| AUD-03 | market_regime_adaptive_v2 | Documento | `audit/market_regime_adaptive_v2.md` | Iteración v2 del diseño adaptativo | COMPLETO | Lab-Private | Baja |
| AUD-04 | phase2_structural_mathematical_validation | Documento | `audit/phase2_structural_mathematical_validation.md` | Validación estructural y matemática | COMPLETO | Lab-Private | Media |
| AUD-05 | professional_volatility_regime_detector | Documento | `audit/professional_volatility_regime_detector.md` | Detector profesional de régimen de volatilidad | COMPLETO | Lab-Private | Media |

---

## Resumen por tipo

| Tipo canónico | Cantidad | Ejemplos principales |
|---------------|----------|---------------------|
| Herramienta | 13 | backtester, grid_search, download_data, discovery |
| Componente | 9 | 6 agentes, executor, paper_wallet, live_bot |
| Documento | 9 | 14 journals (template), 2 reportes, 5 auditorías |
| Dataset | 6 | 3 CSVs locales, 8 leaderboards, 1 candidate signals |

---

## Cross-references

- [crypto-scalping-core-repository-structure.md](./crypto-scalping-core-repository-structure.md) — Vista arquitectónica
- [crypto-scalping-core-strategy-inventory.md](./crypto-scalping-core-strategy-inventory.md) — Detalle de estrategias
- [crypto-scalping-core-research-artifacts-inventory.md](./crypto-scalping-core-research-artifacts-inventory.md) — Detalle de artefactos
- [crypto-scalping-core-asset-candidates.md](./crypto-scalping-core-asset-candidates.md) — Candidatos a Asset

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 42       | 100%       |
| [Hipótesis]   | 0        | 0%         |
| [Decisión]    | 0        | 0%         |
| [Visión]      | 0        | 0%         |

> **Nota:** Este documento es puramente descriptivo — todos los ítems son hechos observados directamente del repositorio.
