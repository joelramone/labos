# Decisiones del Fundador — Package 001A Batch 3

## Metadata

| Campo | Valor |
|-------|-------|
| **Documento** | Decisiones del fundador — Batch 3 |
| **Package** | 001A — First Lab Integration |
| **Batch** | 3 — Lab Contract & Compliance |
| **Fecha** | 2025-07-24 |

---

## Propósito

Registrar las decisiones del fundador (Joel Diaz) requeridas para Batch 3 de Package 001A. [Hecho] Batch 3 requiere una decisión sobre Lab State para poder instanciar el Lab Contract con el estado correcto.

---

## FD-B3-01 — Lab State de Crypto Scalping Core

| Campo | Valor |
|-------|-------|
| **Decision ID** | FD-B3-01 |
| **Pregunta** | ¿Debería el Lab State de Crypto Scalping Core cambiar de `idea` a `explorando`? |
| **Fecha** | 2025-07-24 |
| **Estatus** | **RESOLVED** |
| **Clasificación** | FOUNDER_DECISION |

### Opciones presentadas

| Opción | Descripción | Evidencia requerida |
|--------|-------------|---------------------|
| `idea` | Sin actividad significativa, hipótesis sin explorar | Mínima — solo existencia del Lab |
| `explorando` | Actividad exploratoria activa, investigación en curso | Experimentación activa, artefactos producidos, pipeline funcional |
| `validando` | Hipótesis de monetización en prueba activa | PF > 1.0, out-of-sample validation, señal de demanda de mercado |
| `operando` | Revenue real generado | Transacciones reales, ingresos documentados |

### Recomendación del Principal Architect

**EXPLORANDO** — basada en evidencia del repositorio (Batch 2): [Decisión]

| Evidencia | Detalle |
|-----------|---------|
| Experimentos formales | 14 journals (EXP-000001 a EXP-000014) [Hecho] |
| Configuraciones evaluadas | 567 optimizer runs documentados [Hecho] |
| Pipeline operativo | 8 etapas funcionales con outputs verificables [Hecho] |
| Estrategias implementadas | 4 (breakout, mean_reversion, high_vol, multi) [Hecho] |
| Artefactos de investigación | 27+ (journals, leaderboards, reports, CSVs, configs) [Hecho] |
| Knowledge Object candidates | 5 identificados [Hecho] |
| Asset candidates | 5 identificados [Hecho] |
| Código funcional | Pipeline end-to-end ejecutado múltiples veces [Hecho] |

**Razón por la que NO califica como `validando`:** Ninguna estrategia ha alcanzado PF > 1.0. [Hecho] No hay hipótesis de monetización validada con señal de demanda. [Hecho]

### Respuesta del Fundador

**Aprobado: EXPLORANDO** [Decisión]

### Decisión final

| Campo | Valor |
|-------|-------|
| **Lab State asignado** | `explorando` [Decisión] |
| **Fecha efectiva** | 2025-07-24 |
| **Rationale** | 14 experimentos formales, 567 configuraciones evaluadas, pipeline de 8 etapas operativo, 4 estrategias implementadas, investigación activa con artefactos verificables |
| **Evidencia base** | Inspección de repositorio (Batch 2): research/journal/, research/leaderboards/, research/reports/, app/strategies/, app/optimization/ |
| **Review cadence** | 15 min/mes (per portfolio-model estado `explorando`) |

### Documentos afectados

| Documento | Cambio requerido |
|-----------|-----------------|
| Portfolio Model (steering) | Lab State: `idea` → `explorando` |
| crypto-scalping-core-lab-contract.md | Sección 1 (Identity): estado = explorando |
| Lab Contract Sección 15 (Evolution) | Current state = explorando, review triggers definidos |

### Trigger de siguiente transición

**`explorando` → `validando`:** cuando una estrategia alcance PF > 1.0 con validación out-of-sample (walk-forward) y el fundador apruebe iniciar validación de hipótesis de monetización. [Decisión]

---

## Resumen de Decisiones Batch 3

| # | Decision ID | Pregunta | Decisión | Clasificación |
|---|-------------|----------|----------|---------------|
| 1 | FD-B3-01 | Lab State → explorando | **APROBADO** | FOUNDER_DECISION |

---

## Cross-references

- [founder-decisions-package-001a-batch1.md](./founder-decisions-package-001a-batch1.md) — Decisiones Batch 1
- [crypto-scalping-core-readiness-assessment.md](./crypto-scalping-core-readiness-assessment.md) — Evaluación de readiness
- [crypto-scalping-core-research-workflow-map.md](./crypto-scalping-core-research-workflow-map.md) — Pipeline evidenciado
- [crypto-scalping-core-research-artifacts-inventory.md](./crypto-scalping-core-research-artifacts-inventory.md) — Artefactos producidos
- [../../architecture/architecture-baseline-v1.md](../../architecture/architecture-baseline-v1.md) — Sección 7: Lab States

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 10       | 40%        |
| [Hipótesis]   | 0        | 0%         |
| [Decisión]    | 15       | 60%        |
| [Visión]      | 0        | 0%         |

> **Nota:** Alto porcentaje de decisiones porque este documento registra una elección explícita del fundador con sus consecuencias. Los hechos corresponden a evidencia verificable del repositorio.
