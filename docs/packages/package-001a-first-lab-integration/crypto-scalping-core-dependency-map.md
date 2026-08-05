# Mapa de Dependencias — Crypto Scalping Core

## Metadata

| Campo | Valor |
|-------|-------|
| **Documento** | Mapa de dependencias |
| **Lab** | Crypto Scalping Core |
| **Package** | 001A — First Lab Integration |
| **Batch** | 2 — Repository Discovery & Inventory |
| **Fecha** | 2025-07-24 |

---

## Propósito

Documentar todas las dependencias del repositorio: internas (entre módulos), externas (librerías), de infraestructura (servicios) y con LabOS. [Hecho]

---

## Dependencias con LabOS

| Dependencia | Estado |
|-------------|--------|
| Runtime dependency en LabOS | **NINGUNA** [Hecho] |
| Shared infrastructure | **NINGUNA** [Hecho] |
| Shared databases | **NINGUNA** [Hecho] |
| Shared APIs | **NINGUNA** [Hecho] |
| Import de módulos LabOS | **NINGUNO** [Hecho] |

**Conclusión:** Crypto Scalping Core es operacionalmente independiente de LabOS. [Hecho] La integración con LabOS es exclusivamente de gobernanza (documentación, clasificación, reporting). [Decisión] Ref: founder-decisions-package-001a-batch1.md, Decisión 4.

---

## Dependencias externas (Python packages)

| Package | Versión | Propósito | Criticidad |
|---------|---------|-----------|------------|
| `pandas` | sin pin | Manipulación de datos, DataFrames | CRÍTICA — core del pipeline [Hecho] |
| `python-binance` | sin pin | API client de Binance | ALTA — única fuente de datos [Hecho] |
| `Flask` | sin pin | Dashboard web | BAJA — solo visualización [Hecho] |
| `plotly` | sin pin | Gráficos interactivos | BAJA — solo visualización [Hecho] |
| `python-dotenv` | sin pin | Variables de entorno | MEDIA — configuración [Hecho] |
| `requests` | sin pin | HTTP requests | MEDIA — comunicación con APIs [Hecho] |
| `pydantic>=2,<3` | 2.x | Validación de datos/config | MEDIA — estructura de configuración [Hecho] |
| `tabulate>=0.9.0` | 0.9+ | Formateo de tablas | BAJA — presentación [Hecho] |

**Observación:** No se usan versiones pinned (excepto pydantic y tabulate con rangos). [Hecho] Esto genera riesgo de reproducibilidad.

---

## Dependencias de infraestructura/servicios

| Servicio | Propósito | Tipo | Reemplazable |
|----------|-----------|------|-------------|
| **Binance API** | Descarga de datos OHLCV (USD-M Futures) | Exchange REST API | Parcialmente — otras exchanges proveen datos similares [Hecho] |
| **GitHub** | Hosting de código fuente | Git hosting | Sí — cualquier git provider [Hecho] |

**No se identifican:** bases de datos, colas de mensajes, servicios cloud, APIs propietarias más allá de Binance. [Hecho]

---

## Dependencias internas (entre módulos)

### Flujo de dependencia principal

```text
app/data/binance_downloader.py
    └──→ python-binance (API)
    └──→ data/*.csv (output)

app/data/features.py / app/research/features.py
    └──→ pandas
    └──→ data/*.csv (input)

app/strategies/*
    └──→ features (input calculado)
    └──→ config (parámetros)

app/research/backtester.py
    └──→ strategies (evaluadas)
    └──→ features (calculadas)
    └──→ data/*.csv (source)

app/optimization/grid_search.py
    └──→ backtester (ejecutor)
    └──→ YAML configs (parámetros)
    └──→ research/leaderboards/ (output)

app/research/discovery/
    └──→ research/leaderboards/ (input)
    └──→ research/reports/ (output)

app/research/signal_quality/
    └──→ backtester results (input)
    └──→ research/reports/ (output)

app/agents/*
    └──→ strategies (señales)
    └──→ trading/executor (ejecución)
    └──→ config (límites)

app/trading/executor.py
    └──→ paper_wallet.py (modo paper)
    └──→ python-binance (modo live — no confirmado activo)
```

### Matriz de acoplamiento

| Módulo | Depende de | Dependido por |
|--------|-----------|---------------|
| `data/` | python-binance, pandas | features, strategies, backtester |
| `strategies/` | features, config | agents, backtester |
| `agents/` | strategies, trading | main, live_bot |
| `trading/` | python-binance (live), config | agents |
| `optimization/` | backtester, strategies | (standalone — genera outputs) |
| `research/` | optimization, backtester | (standalone — genera reportes) |

---

## Riesgos de dependencia identificados

| Riesgo | Probabilidad | Impacto | Mitigación existente |
|--------|-------------|---------|---------------------|
| Binance API changes/deprecation | MEDIA | ALTO — única fuente de datos | Ninguna — sin abstracción de exchange [Hecho] |
| Version conflicts (no pinning) | MEDIA | MEDIO — puede romper pipeline | Solo pydantic tiene restricción de versión [Hecho] |
| python-binance library abandonment | BAJA | ALTO — sin alternativa configurada | Ninguna [Hecho] |
| Pandas breaking changes | BAJA | ALTO — core del pipeline | Ninguna [Hecho] |

---

## Dependencias con otros Labs

| Lab | Dependencia | Estado |
|-----|-------------|--------|
| Atlas Wealth Labs | NINGUNA | Independientes [Hecho] |
| Otros labs LabOS | NINGUNA | Independientes [Hecho] |

**Potencial futuro:** Compartir methodology/tooling con Atlas Wealth Labs (ambos son labs de finanzas cuantitativas). [Hipótesis] No implementado ni planificado actualmente.

---

## Cross-references

- [crypto-scalping-core-repository-structure.md](./crypto-scalping-core-repository-structure.md) — Estructura del código
- [crypto-scalping-core-labos-integration-map.md](./crypto-scalping-core-labos-integration-map.md) — Integración con LabOS
- [founder-decisions-package-001a-batch1.md](./founder-decisions-package-001a-batch1.md) — Decisión de autonomía

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 24       | 83%        |
| [Hipótesis]   | 2        | 7%         |
| [Decisión]    | 3        | 10%        |
| [Visión]      | 0        | 0%         |
