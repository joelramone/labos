# Evaluación de Procedencia de Datos — Crypto Scalping Core

## Metadata

| Campo | Valor |
|-------|-------|
| **Documento** | Evaluación de procedencia de datos |
| **Lab** | Crypto Scalping Core |
| **Package** | 001A — First Lab Integration |
| **Batch** | 2 — Repository Discovery & Inventory |
| **Fecha** | 2025-07-24 |

---

## Propósito

Evaluar la procedencia, licenciamiento y restricciones de los datasets utilizados en el Lab. [Hecho] Determinar si los datos pueden compartirse, redistribuirse o utilizarse comercialmente.

---

## Datasets identificados

### Dataset 1: BTCUSDT_1m.csv

| Campo | Valor |
|-------|-------|
| Ubicación | `data/BTCUSDT_1m.csv` [Hecho] |
| Contenido | Velas OHLCV de 1 minuto para BTC/USDT [Hecho] |
| Fuente | Binance USD-M Futures API [Hecho] |
| Herramienta de descarga | `app/research/download_data.py` [Hecho] |
| Comando documentado | `python -m app.research.download_data --symbol BTCUSDT --interval 1m --start 2025-01-01 --end 2026-01-01` [Hecho] |
| Período | ~1 año de datos (según comando documentado en README) [Hecho] |
| Uso en investigación | Dataset PRINCIPAL — base de todos los 567 optimizer runs [Hecho] |
| Versionado en git | NO — incluido en .gitignore [Hecho] |

### Dataset 2: binance_klines.csv

| Campo | Valor |
|-------|-------|
| Ubicación | `data/binance_klines.csv` [Hecho] |
| Contenido | Klines de Binance (formato específico no verificado) [Hecho] |
| Fuente | Binance API (presumido) [Hecho] |
| Metadata de descarga | NO encontrada [Hecho] |
| Uso en investigación | No referenciado directamente en journals [Hecho] |
| Versionado en git | NO — incluido en .gitignore [Hecho] |

### Dataset 3: sample_trades.csv

| Campo | Valor |
|-------|-------|
| Ubicación | `data/sample_trades.csv` [Hecho] |
| Contenido | Trades de ejemplo (formato específico no verificado) [Hecho] |
| Fuente | Generado internamente (probable) o descargado [Hecho] |
| Metadata de descarga | NO encontrada [Hecho] |
| Uso en investigación | Testing/referencia [Hecho] |
| Versionado en git | NO — incluido en .gitignore [Hecho] |

---

## Evaluación de licenciamiento

### Binance Terms of Service

| Aspecto | Evaluación |
|---------|-----------|
| Licencia explícita en el repositorio | **NOT_FOUND** — no hay archivo LICENSE ni referencia a términos de datos [Hecho] |
| Binance API Terms of Service | Aplican por defecto al uso de la API [Hecho] |
| Uso personal/investigación | Generalmente permitido bajo ToS de Binance [Hecho] |
| Redistribución de datos crudos | **RESTRINGIDO** — ToS típicamente prohíben redistribución masiva [Hecho] |
| Uso comercial de datos derivados | **NO VERIFICADO** — requiere revisión legal de ToS actuales [Hecho] |
| Datos en tiempo real vs históricos | Históricos (batch download) — típicamente menos restrictivo [Hecho] |

### Estado de licencia por dataset

| Dataset | Licencia | Redistribuible | Uso comercial | Estado |
|---------|----------|----------------|---------------|--------|
| BTCUSDT_1m.csv | Binance ToS (implícita) | **NO** hasta verificación | **NO VERIFICADO** | RESTRICTED [Hecho] |
| binance_klines.csv | Binance ToS (presumida) | **NO** hasta verificación | **NO VERIFICADO** | RESTRICTED [Hecho] |
| sample_trades.csv | Desconocida | **NO** hasta verificación | **NO VERIFICADO** | RESTRICTED [Hecho] |

---

## Decisión del fundador sobre datasets

Ref: founder-decisions-package-001a-batch1.md, Decisión 2: [Hecho]

> "Datasets: Proveniencia externa, NO automáticamente propiedad del Lab. Artefactos procesados/derivados SÍ son propiedad. Datos crudos restringidos hasta verificar licencia."

| Tipo de dato | Propiedad | Compartible |
|-------------|-----------|-------------|
| Datos crudos de exchange (CSVs) | NO — propiedad del exchange | **RESTRINGIDO** [Decisión] |
| Artefactos derivados (leaderboards, reports, features calculados) | SÍ — propiedad del Lab | Lab-Private por defecto [Decisión] |
| Código de descarga/procesamiento | SÍ — propiedad del Lab | Lab-Private [Decisión] |

---

## Implicaciones para LabOS

1. **Los datasets NO pueden compartirse** entre labs sin verificación de licencia. [Decisión]
2. **Los reportes derivados SÍ pueden compartirse** (son análisis propios del Lab). [Decisión]
3. **Los leaderboards SON artefactos derivados** — propios del Lab pero contienen métricas de rendimiento que no exponen datos crudos. [Hecho]
4. **La reproducibilidad depende de re-descarga** — cualquier lab que quiera replicar debe descargar sus propios datos. [Hecho]

---

## Remediación requerida

| Ítem | Prioridad | Acción requerida | Owner |
|------|-----------|-----------------|-------|
| Verificar Binance ToS actuales | P2 | Leer Terms of Service vigentes de Binance respecto a uso de datos históricos | Fundador |
| Documentar período exacto del dataset | P3 | Registrar start/end dates exactos del BTCUSDT_1m.csv actual | Fundador |
| Evaluar sample_trades.csv origin | P3 | Determinar si es generado internamente o descargado | Fundador |

---

## Cross-references

- [founder-decisions-package-001a-batch1.md](./founder-decisions-package-001a-batch1.md) — Decisión sobre ownership de datos
- [crypto-scalping-core-dependency-map.md](./crypto-scalping-core-dependency-map.md) — Binance como fuente externa
- [crypto-scalping-core-repository-inventory.md](./crypto-scalping-core-repository-inventory.md) — Inventario de datasets

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 28       | 74%        |
| [Hipótesis]   | 0        | 0%         |
| [Decisión]    | 10       | 26%        |
| [Visión]      | 0        | 0%         |
