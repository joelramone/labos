# Registro de Evidencia Requerida — Crypto Scalping Core

## Propósito

Este documento lista toda la evidencia que el fundador necesita proveer para que la evaluación de Crypto Scalping Core avance más allá del nivel de framework. [Hecho] Cada ítem indica qué se necesita, por qué, quién puede proveerlo, y qué dimensión del framework desbloquea.

---

## Instrucciones para el Fundador

Para avanzar la integración, el fundador debe revisar esta lista y proveer la información que pueda. [Decisión] No se requiere completar TODO — incluso respuestas parciales o "no existe" son valiosas para la evaluación.

**Formato sugerido de respuesta:** Para cada ítem, indicar uno de:
- **EXISTE**: [ubicación/descripción]
- **NO EXISTE**: el Lab no tiene esto aún
- **EXISTE PARCIALMENTE**: [qué hay y qué falta]
- **NO APLICA**: [justificación]

---

## Evidencia P0 — Bloqueante para Lab Contract — ✅ TODOS RESUELTOS

| # | Evidencia Requerida | Resolución | Fecha | Estatus |
|---|--------------------|-----------:|-------|---------|
| E-01 | Ubicación del proyecto | GitHub: `https://github.com/joelramone/crypto-scalping-core` (main). Local: `C:\Users\jd0519\Documents\Personal\crypto-scalping-core`. | 2025-07-23 | ✅ RESOLVED |
| E-02 | Confirmación de ownership | Lab-Private por defecto. Lab-Published solo por autorización. LabOS-Shared solo tras promoción. Exclusión corporativa absoluta. | 2025-07-23 | ✅ RESOLVED |
| E-03 | Identificación de riesgos | 5 riesgos: (A) Validez de investigación, (B) Riesgo financiero, (C) Dependencia de datos, (D) Overfitting, (E) Sostenibilidad operacional. | 2025-07-23 | ✅ RESOLVED |
| E-04 | Autonomía operacional | CSC opera independientemente de LabOS. Sin dependencias. Integraciones futuras opcionales. | 2025-07-23 | ✅ RESOLVED |

Ver detalle completo en [founder-decisions-package-001a-batch1.md](./founder-decisions-package-001a-batch1.md).

---

## Evidencia P1 — Necesaria para Transición a `explorando`

| # | Evidencia Requerida | Pregunta para el Fundador | Dimensión | Impacto si no se provee | Estatus |
|---|--------------------|-----------------------------|-----------|------------------------|---------|
| E-05 | Hipótesis de monetización completa | ¿Quién pagaría por outputs del Lab (segmento)? ¿Cómo se entregaría (formato)? ¿Qué mecanismo de ingreso (modelo)? | D11 | Lab no puede transicionar a `explorando` per portfolio model. | PENDIENTE |
| E-06 | Estado real del proyecto | ¿El proyecto es puramente una idea o ya tiene algún trabajo previo (aunque sea informal)? Describir honestamente. | General | No se puede calibrar la evaluación al estado real. | PARCIALMENTE RESUELTO — se sabe que existe repo, pendiente inspección |
| E-07 | Asignación de tiempo | ¿Cuántas horas semanales se asignarían al Lab si se activa? ¿De dónde salen (per capacidad disponible del portfolio model)? | General | No se puede evaluar viabilidad operativa. | PENDIENTE |

---

## Evidencia P1-NEW — Generada por Resolución de P0

| # | Evidencia Requerida | Cómo Resolver | Dimensión | Estatus |
|---|--------------------|--------------:|-----------|---------|
| E-21 | Inspección de estructura real del repositorio | LabOS inspecciona `https://github.com/joelramone/crypto-scalping-core` (permiso concedido) | D5, D7 | PENDIENTE |

---

## Evidencia P2 — Informativa para Evaluación Completa

| # | Evidencia Requerida | Pregunta para el Fundador | Dimensión | Impacto si no se provee |
|---|--------------------|-----------------------------|-----------|------------------------|
| E-08 | Código existente | ¿Existe código escrito (scripts, bots, herramientas) relacionado con trading cuantitativo? ¿Dónde? ¿En qué lenguaje? | D10, D14 | No se puede evaluar madurez técnica. |
| E-09 | Investigación previa | ¿Se ha hecho investigación informal sobre mercados, exchanges, o estrategias? ¿Dónde están los resultados? | D12 | No se puede evaluar base de conocimiento existente. |
| E-10 | Datasets existentes | ¿Existen datos de mercado recolectados o comprados? ¿Formato? ¿Volumen? | D14 | No se puede evaluar potencial de activos tipo Dataset. |
| E-11 | Estrategias documentadas | ¿Existe alguna estrategia de trading documentada (aunque sea informal)? ¿Backtested? | D10 | No se puede evaluar outputs previos. |
| E-12 | Resultados de performance | ¿Se han ejecutado backtests o paper trading? ¿Existen resultados? | D10 | No se puede evaluar criterio de avance del portfolio model. |
| E-13 | Dependencias técnicas | ¿Qué lenguajes, librerías, APIs o servicios externos se usan o se planea usar? | D10 | No se puede evaluar complejidad técnica. |
| E-14 | Exchanges target | ¿Qué exchanges se consideran o se han usado? ¿Hay cuentas activas? | D10 | No se puede evaluar dependencias externas. |
| E-15 | Historial de actividad | ¿Cuánto tiempo se ha invertido informalmente en este Lab? ¿Cuándo comenzó la idea? | D9 | No se puede estimar madurez real vs. documentada. |

---

## Evidencia P3 — Se Genera con Operación Futura

Estos ítems NO requieren acción inmediata del fundador. Se generarán naturalmente cuando el Lab inicie operación formal: [Hecho]

| # | Evidencia | Se genera cuando... |
|---|-----------|---------------------|
| E-16 | Knowledge Objects formales | El Lab ejecute ≥1 investigación y sintetice hallazgos per Package 002. |
| E-17 | Activos con 5 campos mínimos | El Lab produzca ≥1 artefacto que cumpla criterio de activo per Package 000. |
| E-18 | Notas de cierre | Una investigación >4h concluya sin producir activo formal (per INV-02). |
| E-19 | Review cycle outputs | El Lab complete ≥1 ciclo de revisión per Lab Contract. |
| E-20 | Métricas operativas | El Lab tenga ≥1 período de actividad medible. |

---

## Resumen por Prioridad

| Prioridad | Ítems | Estado | Urgencia |
|-----------|-------|--------|----------|
| P0 | E-01 a E-04 | ✅ **TODOS RESUELTOS** (2025-07-23) | Completado |
| P1 | E-05, E-06, E-07, E-21 | Pendientes (no bloqueantes para Lab Contract) | Antes de transicionar a `explorando` |
| P2 | E-08 a E-15 | Pendientes — varios resoluble vía inspección de repo | Cuando sea conveniente |
| P3 | E-16 a E-20 | No requiere acción — se auto-genera | Con operación del Lab |

**Total de ítems P0 resueltos: 4/4.** [Hecho]
**Total de ítems pendientes no-bloqueantes: 12 (P1-P2).** [Hecho]
**Total de ítems auto-generables: 5 (P3).** [Hecho]
**Resultado: Lab Contract puede crearse.** [Decisión]

---

## Formato de Entrega Sugerido

El fundador puede responder a este registro de la forma más conveniente: [Decisión]

1. **Inline** — Responder directamente en un mensaje/documento con las respuestas por E-##.
2. **Documento** — Crear un documento de respuestas en la carpeta del Lab.
3. **Conversación** — Responder verbalmente durante una sesión de trabajo y documentar después.

No hay requisito de formato formal. La información es más valiosa que la presentación. [Decisión]

---

## Cross-references

- [founder-decisions-package-001a-batch1.md](./founder-decisions-package-001a-batch1.md) — Decisiones que resuelven P0
- [integration-gap-analysis.md](./integration-gap-analysis.md) — Gaps que generan estos requerimientos
- [crypto-scalping-core-readiness-assessment.md](./crypto-scalping-core-readiness-assessment.md) — Evaluación que los identifica
- [lab-validation-framework.md](./lab-validation-framework.md) — Dimensiones referenciadas
- [lab-validation-criteria.md](./lab-validation-criteria.md) — Criterios obligatorios
- [Package 000 — 012-portfolio-model.md](../package-000-foundation/012-portfolio-model.md) — Criterio de transición a `explorando`

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 5        | 33%        |
| [Hipótesis]   | 0        | 0%         |
| [Decisión]    | 5        | 33%        |
| [Visión]      | 0        | 0%         |

> **Nota**: Este documento es predominantemente un registro estructurado (preguntas y clasificaciones). Los hechos son estados observables; las decisiones son sobre priorización y formato.
