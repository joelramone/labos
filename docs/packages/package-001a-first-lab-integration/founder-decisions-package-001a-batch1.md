# Decisiones del Fundador — Package 001A Batch 1

## Propósito

Este documento registra las decisiones tomadas por el fundador (Joel Diaz) para resolver los 4 bloqueantes P0 identificados durante la evaluación de readiness de Crypto Scalping Core. [Hecho] Todas las decisiones fueron provistas el 2025-07-23.

---

## Decisión 1 — Ubicación del Proyecto

| Campo | Valor |
|-------|-------|
| Pregunta original | ¿Dónde vive (o vivirá) el proyecto? ¿Repositorio Git? ¿Carpeta local? ¿Otro sistema? |
| Evidencia resuelta | E-01 |
| Dimensión desbloqueada | D6 (Fuente de Verdad) |
| Fecha | 2025-07-23 |
| Estatus | **RESOLVED** |

### Respuesta del Fundador

| Campo | Valor | Clasificación |
|-------|-------|---------------|
| Ruta local | `C:\Users\jd0519\Documents\Personal\crypto-scalping-core` | [Hecho] |
| Repositorio remoto | `https://github.com/joelramone/crypto-scalping-core` | [Hecho] |
| Branch principal | `main` | [Hecho] |
| Fuente de verdad | Remoto (GitHub main branch) | [Decisión] |
| Clon local | Copia de trabajo operativa | [Hecho] |
| Permiso LabOS — lectura/inspección | SÍ | [Decisión] |
| Permiso LabOS — modificar código | NO | [Decisión] |
| Copias secundarias | Pueden existir pero NO son fuentes de verdad independientes | [Decisión] |

### Documentos Afectados

- [crypto-scalping-core-lab-profile.md](./crypto-scalping-core-lab-profile.md) — Actualizar repositorio y fuente de verdad
- [crypto-scalping-core-readiness-assessment.md](./crypto-scalping-core-readiness-assessment.md) — D6 → VALIDATED
- [evidence-required-register.md](./evidence-required-register.md) — E-01 → RESOLVED

---

## Decisión 2 — Ownership y Boundaries

| Campo | Valor |
|-------|-------|
| Pregunta original | ¿Confirmas que todo conocimiento producido por el Lab es Lab-Private hasta publicación explícita? ¿Hay alguna excepción? |
| Evidencia resuelta | E-02 |
| Dimensión desbloqueada | D15 (Propiedad del Conocimiento) |
| Fecha | 2025-07-23 |
| Estatus | **RESOLVED** |

### Respuesta del Fundador

| Clasificación | Contenido | Etiqueta |
|---------------|-----------|----------|
| Owner | Joel Diaz (Fundador) | [Hecho] |
| Lab-Private | Código de investigación, estrategias, parámetros, lógica de entrada/salida, configuraciones de riesgo, resultados no validados, experimentos en progreso, credenciales, API keys, cuentas, balances, datos financieros personales | [Decisión] |
| Lab-Published (por autorización) | Reportes de investigación, metodología, hallazgos generales | [Decisión] |
| LabOS-Shared (tras promoción) | Solo KOs y Assets promovidos explícitamente | [Decisión] |
| Externo | Exchanges, proveedores de datos de mercado (no se poseen) | [Hecho] |
| Datasets | Proveniencia externa, NO automáticamente propiedad del Lab. Artefactos procesados/derivados SÍ son propiedad. Datos crudos restringidos hasta verificar licencia. | [Decisión] |
| Exclusión corporativa | BYMA, NRTC, SentinelOps, información del empleador = ABSOLUTAMENTE excluidos | [Decisión] |

### Documentos Afectados

- [crypto-scalping-core-boundary-analysis.md](./crypto-scalping-core-boundary-analysis.md) — Confirmar boundaries propuestos
- [crypto-scalping-core-readiness-assessment.md](./crypto-scalping-core-readiness-assessment.md) — D15 → VALIDATED
- [evidence-required-register.md](./evidence-required-register.md) — E-02 → RESOLVED

---

## Decisión 3 — Riesgos

| Campo | Valor |
|-------|-------|
| Pregunta original | ¿Cuál es el riesgo principal del Lab? Mínimo 1 con probabilidad, impacto y mitigación. |
| Evidencia resuelta | E-03 |
| Dimensión desbloqueada | D16 (Riesgos Identificados) |
| Fecha | 2025-07-23 |
| Estatus | **RESOLVED** |

### Respuesta del Fundador — 5 Riesgos Identificados

| ID | Riesgo | Probabilidad | Impacto | Owner |
|----|--------|-------------|---------|-------|
| A | Validez de investigación | MEDIA | ALTO | Joel Diaz |
| B | Riesgo financiero | MEDIA | CRÍTICO | Joel Diaz |
| C | Dependencia de datos | MEDIA | ALTO | Joel Diaz |
| D | Overfitting | ALTA | ALTO | Joel Diaz |
| E | Sostenibilidad operacional | ALTA | MEDIO | Joel Diaz |

**Nota:** Evaluación cualitativa únicamente (sin probabilidades numéricas). [Decisión]

### Documentos Afectados

- [crypto-scalping-core-readiness-assessment.md](./crypto-scalping-core-readiness-assessment.md) — D16 → VALIDATED
- [evidence-required-register.md](./evidence-required-register.md) — E-03 → RESOLVED

---

## Decisión 4 — Autonomía Operacional

| Campo | Valor |
|-------|-------|
| Pregunta original | ¿Puede el proyecto operar independientemente de LabOS? ¿Existía antes de LabOS o nació dentro? |
| Evidencia resuelta | E-04 |
| Dimensión desbloqueada | D17 (Ruta de Salida / Decoupling) |
| Fecha | 2025-07-23 |
| Estatus | **RESOLVED** |

### Respuesta del Fundador

| Afirmación | Clasificación |
|------------|---------------|
| CSC es operacionalmente independiente de LabOS | [Hecho] |
| No tiene dependencias actuales con LabOS | [Hecho] |
| Futuras integraciones con LabOS serán opcionales únicamente | [Decisión] |
| LabOS = capa de gobernanza, NO dependencia de runtime | [Decisión] |
| Principio de decoupling: cada Lab debe poder existir independientemente de LabOS | [Decisión] |

### Documentos Afectados

- [crypto-scalping-core-readiness-assessment.md](./crypto-scalping-core-readiness-assessment.md) — D17 → VALIDATED
- [crypto-scalping-core-boundary-analysis.md](./crypto-scalping-core-boundary-analysis.md) — Confirmar autonomía
- [evidence-required-register.md](./evidence-required-register.md) — E-04 → RESOLVED

---

## Resumen de Resolución

| # | Bloqueante P0 | Estatus anterior | Estatus nuevo | Decisión |
|---|--------------|-----------------|---------------|----------|
| 1 | Ubicación del proyecto (D6) | EVIDENCE_REQUIRED | **RESOLVED** | GitHub main branch = fuente de verdad |
| 2 | Ownership de conocimiento (D15) | EVIDENCE_REQUIRED | **RESOLVED** | Modelo de ownership confirmado |
| 3 | Riesgos no documentados (D16) | EVIDENCE_REQUIRED | **RESOLVED** | 5 riesgos con evaluación cualitativa |
| 4 | Autonomía operacional (D17) | EVIDENCE_REQUIRED | **RESOLVED** | Independencia confirmada, sin dependencias |

**Resultado:** Todos los bloqueantes P0 resueltos. Batch 2 autorizado a proceder. [Hecho]

---

## Impacto en Veredictos

| Veredicto | Antes | Después |
|-----------|-------|---------|
| Readiness Assessment | EVIDENCE_REQUIRED | **READY_WITH_REMEDIATION** |
| Batch 1 Review | FOUNDER_DECISIONS_REQUIRED | **BATCH_1_APPROVED_WITH_REMEDIATION** |
| Batch 2 Authorization | No autorizado | **AUTHORIZED** |

---

## Cross-references

- [crypto-scalping-core-readiness-assessment.md](./crypto-scalping-core-readiness-assessment.md) — Evaluación actualizada
- [crypto-scalping-core-boundary-analysis.md](./crypto-scalping-core-boundary-analysis.md) — Boundaries confirmados
- [crypto-scalping-core-lab-profile.md](./crypto-scalping-core-lab-profile.md) — Perfil actualizado
- [evidence-required-register.md](./evidence-required-register.md) — Registro con ítems resueltos
- [integration-gap-analysis.md](./integration-gap-analysis.md) — Gaps actualizados
- [package-001a-batch1-summary.md](./package-001a-batch1-summary.md) — Resumen actualizado
- [package-001a-batch1-review.md](./package-001a-batch1-review.md) — Review con nuevo veredicto

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 12       | 35%        |
| [Hipótesis]   | 0        | 0%         |
| [Decisión]    | 22       | 65%        |
| [Visión]      | 0        | 0%         |

> **Nota**: Alto porcentaje de decisiones porque este documento registra elecciones explícitas del fundador. Los hechos corresponden a estados verificables (existencia del repositorio, independencia operacional).
