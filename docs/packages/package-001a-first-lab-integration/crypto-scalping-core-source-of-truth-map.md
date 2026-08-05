# Mapa de Fuentes de Verdad — Crypto Scalping Core

## Metadata

| Campo | Valor |
|-------|-------|
| **Documento** | Mapa de fuentes de verdad |
| **Lab** | Crypto Scalping Core |
| **Package** | 001A — First Lab Integration |
| **Batch** | 2 — Repository Discovery & Inventory |
| **Fecha** | 2025-07-24 |

---

## Propósito

Establecer qué constituye la fuente de verdad para cada tipo de información del Lab, conforme a INV-04 (fuente de verdad única por concepto). [Hecho]

---

## Fuente de verdad principal

| Campo | Valor |
|-------|-------|
| Fuente de verdad global | GitHub `main` branch [Decisión] |
| Repositorio | `https://github.com/joelramone/crypto-scalping-core` [Hecho] |
| Clon local | `C:\Users\jd0519\Documents\Personal\crypto-scalping-core` [Hecho] |
| Relación | Clon local = copia de trabajo; main = fuente canónica [Decisión] |

Ref: founder-decisions-package-001a-batch1.md, Decisión 1. [Hecho]

---

## Fuentes de verdad por categoría

| Categoría | Fuente de verdad | Ubicación | Notas |
|-----------|-----------------|-----------|-------|
| Código de estrategia | GitHub main | `app/strategies/` | Implementaciones canónicas [Hecho] |
| Configuración de estrategia | GitHub main | `app/config/` | Parámetros por defecto [Hecho] |
| Código de agentes | GitHub main | `app/agents/` | Lógica multi-agente [Hecho] |
| Código de investigación | GitHub main | `app/research/` | Pipeline ejecutable [Hecho] |
| Código de optimización | GitHub main | `app/optimization/` | Grid search, walk-forward [Hecho] |
| Journals de experimentos | GitHub main | `research/journal/` | Registro formal de experiments [Hecho] |
| Leaderboards | GitHub main | `research/leaderboards/` | Rankings de optimizer [Hecho] |
| Reportes de investigación | GitHub main | `research/reports/` | Discovery, quality analysis [Hecho] |
| Candidate signals | GitHub main | `research/candidate_signals/` | Señales en evaluación [Hecho] |
| Memory index | GitHub main | `research/memory/` | Índice de memoria [Hecho] |
| Grid search configs | GitHub main | `research/optimization/grid_search/` | YAMLs de configuración [Hecho] |
| Datasets locales | **LOCAL ONLY** | `data/` | NO versionados en git (.gitignored) [Hecho] |
| Variables de entorno | **LOCAL ONLY** | `.env` | Secretos — nunca en git [Hecho] |
| Dependencias | GitHub main | `requirements.txt` | Sin lock file [Hecho] |
| Documentación principal | GitHub main | `README.md` | Overview del proyecto [Hecho] |
| Auditorías de diseño | GitHub main | `audit/` | Documentos de arquitectura [Hecho] |

---

## Elementos sin fuente de verdad clara

| Elemento | Problema | Impacto | Recomendación |
|----------|----------|---------|---------------|
| Datasets locales | No versionados, no reproducibles sin re-descarga | MEDIO — si se pierde el archivo local, hay que re-descargar | Documentar comando exacto de descarga para reproducibilidad [Hecho] |
| Versiones de dependencias | No hay `requirements.lock` ni pinning completo | BAJO — pipeline puede romperse con actualizaciones | Considerar pip freeze o poetry.lock [Hipótesis] |
| Estado del live bot | No hay log de activación ni evidencia de uso | BAJO — no hay impacto operacional actual | Confirmar que nunca fue activado [Hecho] |

---

## Reglas de modificación

| Regla | Estado | Referencia |
|-------|--------|------------|
| LabOS puede LEER/INSPECCIONAR el repositorio | Autorizado [Decisión] | Decisión 1, Batch 1 |
| LabOS NO puede MODIFICAR código | Prohibido [Decisión] | Decisión 1, Batch 1 |
| Copias secundarias no son fuentes de verdad | Confirmado [Decisión] | Decisión 1, Batch 1 |
| Cambios al repo solo por el owner (Joel Diaz) | Implícito [Decisión] | Único contribuidor |

---

## Integridad de la fuente de verdad

| Aspecto | Estado |
|---------|--------|
| Git history intacto | SÍ — repositorio funcional en GitHub [Hecho] |
| Branch protection | NO verificado [Hecho] |
| Backup automático | SÍ — GitHub es el backup implícito [Hecho] |
| Signed commits | NO verificado [Hecho] |
| CI/CD | NO — sin pipelines automatizados [Hecho] |

---

## Cross-references

- [founder-decisions-package-001a-batch1.md](./founder-decisions-package-001a-batch1.md) — Decisión de fuente de verdad
- [crypto-scalping-core-repository-structure.md](./crypto-scalping-core-repository-structure.md) — Estructura del repositorio
- [Architecture Baseline v1.0](../../architecture/architecture-baseline-v1.md) — INV-04 (fuente de verdad única)

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 24       | 69%        |
| [Hipótesis]   | 1        | 3%         |
| [Decisión]    | 10       | 28%        |
| [Visión]      | 0        | 0%         |
