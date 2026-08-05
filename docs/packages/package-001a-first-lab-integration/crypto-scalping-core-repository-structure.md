# Estructura del Repositorio — Crypto Scalping Core

## Metadata

| Campo | Valor |
|-------|-------|
| **Documento** | Estructura del repositorio |
| **Lab** | Crypto Scalping Core |
| **Package** | 001A — First Lab Integration |
| **Batch** | 2 — Repository Discovery & Inventory |
| **Fecha** | 2025-07-24 |
| **Fuente de verdad** | GitHub `main` branch ([Decisión] — ref: founder-decisions-package-001a-batch1.md) |

---

## Propósito

Este documento presenta la vista arquitectónica del repositorio `crypto-scalping-core`, organizado por capas funcionales. [Hecho] Permite a LabOS comprender la estructura sin necesidad de inspeccionar archivo por archivo.

---

## Vista general

El repositorio tiene una **estructura dual** que separa código ejecutable de artefactos durables de investigación: [Hecho]

```text
crypto-scalping-core/
├── app/              ← Código ejecutable principal
├── src/              ← Código adicional (módulo de análisis)
├── research/         ← Artefactos durables de investigación
├── data/             ← Datasets locales
├── audit/            ← Documentos de auditoría arquitectónica
├── diagrams/         ← Diagramas PlantUML
├── docker/           ← Dockerfile
├── scripts/          ← Scripts utilitarios
├── .agents/          ← Placeholder para agentes IA futuros (vacío)
├── .env.example      ← Template de variables de entorno (sin secretos)
├── requirements.txt  ← Dependencias Python
├── README.md         ← Documentación principal
└── output*.txt       ← ~50 archivos de salida generados
```

---

## Capa 1: Código de aplicación (`app/`)

Contiene el código ejecutable del sistema de trading algorítmico. [Hecho]

| Subdirectorio | Propósito | Módulos clave |
|---------------|-----------|---------------|
| `app/agents/` | Sistema multi-agente de trading | 6 agentes: strategy, risk, supervisor, regime, mean_reversion, volatility_regime_detector |
| `app/strategies/` | Implementaciones de estrategia | breakout_trend, rsi_mean_reversion, high_vol_engine, multi_strategy_engine |
| `app/data/` | Ingesta de datos | binance_downloader, features, market_stream, real_data_loader |
| `app/research/` | Código ejecutable de investigación | backtester, grid_search (via optimization/), features, simulation, discovery, signal_quality |
| `app/optimization/` | Optimización de parámetros | grid_search, walk_forward |
| `app/trading/` | Capa de ejecución | executor, paper_wallet, execution_metrics |
| `app/config/` | Configuraciones de estrategia | breakout_config, rsi_config |
| `app/utils/` | Utilidades compartidas | logger, metrics, datetime_utils, signal_rejections, strategy_performance_tracker |

**Punto de entrada principal:** `app/main.py` (paper trading), `app/live_bot.py` (bot live — sin evidencia de activación). [Hecho]

---

## Capa 2: Infraestructura de investigación (`app/research/`)

Código Python ejecutable que implementa el pipeline de investigación: [Hecho]

```text
app/research/
├── analysis/          ← Módulos de análisis
├── discovery/         ← Discovery automatizado
├── memory/            ← Sistema de memoria de investigación
├── optimizer/         ← Motor de optimización
├── signal_quality/    ← Evaluación de calidad de señales
├── strategies/        ← Definiciones de estrategia para backtest
├── backtester.py      ← Motor de backtesting
├── config.py          ← Configuración de investigación
├── data_utils.py      ← Utilidades de datos
├── download_data.py   ← Descarga de datos de Binance
├── features.py        ← Generación de features
├── results.py         ← Procesamiento de resultados
└── simulation.py      ← Motor de simulación
```

**Distinción clave:** `app/research/` = código ejecutable; `research/` = artefactos producidos. [Hecho]

---

## Capa 3: Artefactos durables de investigación (`research/`)

Almacena los outputs y registros producidos por el pipeline de investigación: [Hecho]

| Subdirectorio | Contenido | Estado |
|---------------|-----------|--------|
| `research/journal/` | 14 entradas de experimento (EXP-000001 a EXP-000014) | Poblado [Hecho] |
| `research/leaderboards/` | 8 CSVs con resultados de optimización | Poblado [Hecho] |
| `research/reports/` | 2 reportes: discovery_report.md, quality_analysis_v1.md | Poblado [Hecho] |
| `research/candidate_signals/` | 1 CSV: donchian_breakout_15m_candidates_v1.csv | Poblado [Hecho] |
| `research/memory/` | index.csv (memoria de investigación) | Poblado [Hecho] |
| `research/optimization/grid_search/` | Configuraciones de grid search | Poblado [Hecho] |
| `research/datasets/` | raw/ y processed/ (con .gitkeep) | Vacío [Hecho] |
| `research/backtests/` | .gitkeep | Vacío [Hecho] |
| `research/walk_forward/` | .gitkeep | Vacío [Hecho] |
| `research/monte_carlo/` | .gitkeep | Vacío [Hecho] |
| `research/ml/` | .gitkeep | Vacío [Hecho] |
| `research/notebooks/` | .gitkeep | Vacío [Hecho] |
| `research/feature_store/` | .gitkeep | Vacío [Hecho] |
| `research/features/` | .gitkeep | Vacío [Hecho] |
| `research/strategies/` | .gitkeep | Vacío [Hecho] |

---

## Capa 4: Datasets locales (`data/`)

| Archivo | Contenido | Tamaño estimado |
|---------|-----------|-----------------|
| `BTCUSDT_1m.csv` | Velas 1m BTC/USDT descargadas de Binance | Dataset principal de investigación [Hecho] |
| `binance_klines.csv` | Klines adicionales de Binance | Secundario [Hecho] |
| `sample_trades.csv` | Trades de ejemplo | Referencia/testing [Hecho] |

**Nota:** Carpeta `data/` está en `.gitignore` — los datasets son locales y no se versionan. [Hecho]

---

## Capa 5: Documentos de auditoría (`audit/`)

5 documentos de diseño y auditoría arquitectónica: [Hecho]

- `high_vol_edge_extraction_plan.md`
- `market_regime_adaptive_system_design.md`
- `market_regime_adaptive_v2.md`
- `phase2_structural_mathematical_validation.md`
- `professional_volatility_regime_detector.md`

---

## Capa 6: Salidas generadas (`output*.txt`)

~50 archivos numerados `output*.txt` en la raíz del repositorio. [Hecho] Son outputs de ejecución generados por el sistema — no código fuente ni documentación permanente.

---

## Áreas excluidas del análisis

| Directorio | Razón de exclusión |
|------------|-------------------|
| `.git/` | Control de versiones interno [Hecho] |
| `.crypto-venv/` | Entorno virtual Python [Hecho] |
| `venv/` | Entorno virtual Python alternativo [Hecho] |
| `__pycache__/` | Bytecode compilado Python [Hecho] |

---

## Diagrama de dependencia interna

```text
app/strategies/ ──→ app/data/features.py ──→ app/data/binance_downloader.py
       │                                              │
       ▼                                              ▼
app/agents/ ──→ app/trading/executor.py          Binance API
       │
       ▼
app/research/backtester.py ──→ research/ (outputs)
       │
       ▼
app/research/optimizer/ ──→ research/leaderboards/
       │
       ▼
app/research/discovery/ ──→ research/reports/
```

---

## Cross-references

- [crypto-scalping-core-repository-inventory.md](./crypto-scalping-core-repository-inventory.md) — Inventario detallado por ítem
- [crypto-scalping-core-research-workflow-map.md](./crypto-scalping-core-research-workflow-map.md) — Flujo de trabajo evidenciado
- [crypto-scalping-core-dependency-map.md](./crypto-scalping-core-dependency-map.md) — Dependencias internas y externas
- [founder-decisions-package-001a-batch1.md](./founder-decisions-package-001a-batch1.md) — Decisión de fuente de verdad

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 30       | 88%        |
| [Hipótesis]   | 0        | 0%         |
| [Decisión]    | 4        | 12%        |
| [Visión]      | 0        | 0%         |
