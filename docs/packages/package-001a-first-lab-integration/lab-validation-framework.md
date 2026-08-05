# Framework de Validación de Labs — Genérico

## Propósito

Este documento define un framework reutilizable para evaluar la preparación de cualquier Lab para integración formal al ecosistema LabOS. [Decisión] Es independiente del dominio — aplica igual a Labs técnicos, creativos, de investigación, de servicios o de producto.

---

## Filosofía del Framework

La validación NO es una barrera de entrada. [Decisión] Es un mecanismo de visibilidad que identifica:

1. Qué se sabe sobre el Lab (evidencia existente).
2. Qué no se sabe aún (evidencia requerida).
3. Qué decisiones necesita tomar el fundador para avanzar.

Un Lab en estado `idea` puede tener la mayoría de dimensiones como EVIDENCE_REQUIRED — esto es correcto y esperado. [Decisión] El framework no penaliza Labs tempranos; los hace visibles.

---

## Estatutos de Validación

| Estatus | Significado | Acción requerida |
|---------|-------------|-----------------|
| **VALIDATED** | Evidencia verificable confirma que la dimensión está cubierta. [Decisión] | Ninguna — documentar referencia a la evidencia. |
| **PARTIALLY_VALIDATED** | Existe evidencia parcial; algunos aspectos confirmados, otros pendientes. [Decisión] | Documentar qué está confirmado y qué falta. |
| **NOT_VALIDATED** | Se evaluó la dimensión y no se encontró evidencia que la soporte. [Decisión] | Identificar si es un blocker o un gap a remediar. |
| **NOT_APPLICABLE** | La dimensión no aplica al Lab en su estado o dominio actual. [Decisión] | Documentar justificación de no-aplicabilidad. |
| **EVIDENCE_REQUIRED** | No se puede evaluar porque la información necesaria no está disponible. [Decisión] | Registrar qué evidencia se necesita y quién puede proveerla. |

**Distinción clave:** NOT_VALIDATED ≠ EVIDENCE_REQUIRED. [Decisión]
- NOT_VALIDATED: se buscó evidencia y no existe (el Lab no cumple).
- EVIDENCE_REQUIRED: no se puede determinar porque la información no está accesible.

---

## 17 Dimensiones de Validación

### Grupo A: Identidad y Propósito (Dimensiones 1-4)

#### Dimensión 1: Existencia y Nombre

| Campo | Detalle |
|-------|---------|
| **Pregunta** | ¿El Lab existe como concepto nombrado con identidad distinguible? |
| **Evidencia requerida** | Nombre documentado en portfolio model o fuente equivalente. |
| **Indicadores de cumplimiento** | Nombre único, no duplica otro Lab, reconocible por el fundador. |
| **Proporcionalidad** | Aplica en todos los estados — incluyendo `idea`. |

#### Dimensión 2: Owner Nombrado

| Campo | Detalle |
|-------|---------|
| **Pregunta** | ¿Existe una persona identificada como responsable del Lab? |
| **Evidencia requerida** | Nombre del owner documentado (en nivel SOLO, siempre es el Fundador). |
| **Indicadores de cumplimiento** | Owner explícito, con capacidad de decisión sobre el Lab. |
| **Proporcionalidad** | Aplica en todos los estados. |

#### Dimensión 3: Misión Declarada

| Campo | Detalle |
|-------|---------|
| **Pregunta** | ¿El Lab tiene una declaración de propósito que explica por qué existe? |
| **Evidencia requerida** | Misión documentada en 1-3 oraciones. Puede ser [Hipótesis] en estado `idea`. |
| **Indicadores de cumplimiento** | Específica al dominio, no genérica, distinguible de otros Labs. |
| **Proporcionalidad** | Obligatoria desde `idea`. |

#### Dimensión 4: Dominio Definido

| Campo | Detalle |
|-------|---------|
| **Pregunta** | ¿El Lab opera en un dominio claramente identificable y diferenciado? |
| **Evidencia requerida** | Dominio nombrado que no solapa con otros Labs activos. |
| **Indicadores de cumplimiento** | Dominio reconocible, no ambiguo, independiente. |
| **Proporcionalidad** | Obligatoria desde `idea`. |

---

### Grupo B: Límites y Estructura (Dimensiones 5-8)

#### Dimensión 5: Boundary Documentado

| Campo | Detalle |
|-------|---------|
| **Pregunta** | ¿Están documentados los límites de lo que pertenece al Lab vs. lo que no? |
| **Evidencia requerida** | Listado explícito de inclusiones y exclusiones. Clasificación Lab-Private / LabOS-Shared / Lab-Published. |
| **Indicadores de cumplimiento** | Al menos 3 ítems "dentro" y 3 ítems "fuera" documentados. |
| **Proporcionalidad** | Recomendado desde `idea`, obligatorio desde `explorando`. |

#### Dimensión 6: Fuente de Verdad

| Campo | Detalle |
|-------|---------|
| **Pregunta** | ¿Existe un lugar identificable donde vive la documentación autoritativa del Lab? |
| **Evidencia requerida** | Ruta, repositorio, carpeta o sistema nombrado como fuente de verdad. |
| **Indicadores de cumplimiento** | Accesible, actualizado, referenciable. |
| **Proporcionalidad** | Obligatorio desde `explorando`. En `idea`, puede ser EVIDENCE_REQUIRED. |

#### Dimensión 7: Interfaces Documentadas

| Campo | Detalle |
|-------|---------|
| **Pregunta** | ¿Se sabe qué entra al Lab (inputs) y qué sale (outputs)? |
| **Evidencia requerida** | Lista de inputs con origen y outputs con destino/consumidor. |
| **Indicadores de cumplimiento** | Al menos 1 input y 1 output identificados. Clasificación de boundary por ítem. |
| **Proporcionalidad** | Recomendado desde `idea` (puede ser hipotético), obligatorio desde `explorando`. |

#### Dimensión 8: Independencia de Dominio

| Campo | Detalle |
|-------|---------|
| **Pregunta** | ¿El dominio del Lab es independiente y no duplica otro Lab activo? |
| **Evidencia requerida** | Verificación contra portfolio model — ningún otro Lab activo reclama el mismo dominio. |
| **Indicadores de cumplimiento** | Dominio único en el portafolio. Sin solapamiento funcional con Labs en `explorando` o superior. |
| **Proporcionalidad** | Aplica siempre. |

---

### Grupo C: Actividad Operativa (Dimensiones 9-12)

#### Dimensión 9: Trabajo Recurrente Documentado

| Campo | Detalle |
|-------|---------|
| **Pregunta** | ¿Existe evidencia de actividad repetida en el Lab (no solo un evento aislado)? |
| **Evidencia requerida** | Commits, documentos con fechas, entradas de journal, horas registradas. |
| **Indicadores de cumplimiento** | ≥2 eventos de actividad documentados en diferentes fechas. |
| **Proporcionalidad** | NOT_APPLICABLE para `idea`. Obligatorio desde `explorando`. |

#### Dimensión 10: Outputs Producidos

| Campo | Detalle |
|-------|---------|
| **Pregunta** | ¿El Lab ha producido algo tangible (código, documentos, datos, artefactos)? |
| **Evidencia requerida** | Listado de outputs con tipo, fecha y estado. |
| **Indicadores de cumplimiento** | ≥1 output verificable con los 5 campos mínimos de activo (si aplica). |
| **Proporcionalidad** | NOT_APPLICABLE para `idea`. Obligatorio desde `explorando`. |

#### Dimensión 11: Hipótesis de Monetización

| Campo | Detalle |
|-------|---------|
| **Pregunta** | ¿El Lab tiene documentada una hipótesis de cómo generaría ingresos? |
| **Evidencia requerida** | Documento con 3 campos mínimos: segmento, formato, modelo de ingreso (per 012-portfolio-model.md). |
| **Indicadores de cumplimiento** | Hipótesis con los 3 campos, marcada como [Hipótesis]. |
| **Proporcionalidad** | Recomendado desde `idea`, obligatorio para transicionar a `explorando`. |

#### Dimensión 12: Investigación o Experimentación

| Campo | Detalle |
|-------|---------|
| **Pregunta** | ¿El Lab ha ejecutado alguna investigación o experimento documentado? |
| **Evidencia requerida** | Research ID, notebook, documento de hallazgos o nota de experimento. |
| **Indicadores de cumplimiento** | ≥1 investigación con tipo (Small/Medium/Large) y resultado documentado. |
| **Proporcionalidad** | NOT_APPLICABLE para `idea`. Esperado desde `explorando`. |

---

### Grupo D: Conocimiento y Activos (Dimensiones 13-15)

#### Dimensión 13: Knowledge Objects Producidos

| Campo | Detalle |
|-------|---------|
| **Pregunta** | ¿El Lab ha producido conocimiento sintetizado en formato de Knowledge Object? |
| **Evidencia requerida** | ≥1 KO con los 10 campos obligatorios del contrato de KO (Package 002). |
| **Indicadores de cumplimiento** | KO válido con knowledge_id, title, summary, type, domain, confidence, status, source_reference, created_date, validity_window. |
| **Proporcionalidad** | NOT_APPLICABLE para `idea`. Esperado desde `explorando`. |

#### Dimensión 14: Activos Reutilizables Producidos

| Campo | Detalle |
|-------|---------|
| **Pregunta** | ¿El Lab ha producido activos que cumplen los 5 campos mínimos (per Asset_First_Model)? |
| **Evidencia requerida** | ≥1 activo con nombre, tipo (de 7 canónicos), descripción, hipótesis de uso, estado. |
| **Indicadores de cumplimiento** | Activo catalogado con tipo canónico, estado definido (borrador/validado/productizado). |
| **Proporcionalidad** | NOT_APPLICABLE para `idea`. Obligatorio desde `explorando` (per INV-02). |

#### Dimensión 15: Propiedad del Conocimiento

| Campo | Detalle |
|-------|---------|
| **Pregunta** | ¿Está claro quién posee el conocimiento y activos producidos por el Lab? |
| **Evidencia requerida** | Declaración de ownership. Clasificación de sensitivity per knowledge-boundaries. |
| **Indicadores de cumplimiento** | Ownership declarado; no hay ambigüedad sobre qué es Lab-Private vs compartido. |
| **Proporcionalidad** | Recomendado desde `idea`, obligatorio desde `explorando`. |

---

### Grupo E: Riesgos y Sostenibilidad (Dimensiones 16-17)

#### Dimensión 16: Riesgos Identificados

| Campo | Detalle |
|-------|---------|
| **Pregunta** | ¿Se han identificado riesgos para la operación del Lab? |
| **Evidencia requerida** | ≥1 riesgo documentado con probabilidad, impacto y mitigación. |
| **Indicadores de cumplimiento** | Riesgo específico al dominio (no genérico), con mitigación accionable. |
| **Proporcionalidad** | Recomendado desde `idea`, obligatorio para Lab Contract. |

#### Dimensión 17: Ruta de Salida (Decoupling)

| Campo | Detalle |
|-------|---------|
| **Pregunta** | ¿Puede el Lab operar independientemente si se desacopla de LabOS? |
| **Evidencia requerida** | Confirmación de que el Lab no depende exclusivamente de LabOS para existir. |
| **Indicadores de cumplimiento** | Autonomía operacional verificable o declarada. Decoupling_Protocol referenciable. |
| **Proporcionalidad** | Evaluable desde `idea` (conceptual). Obligatorio para Lab Contract. |

---

## Criterios de Veredicto Global

| Veredicto | Condición |
|-----------|-----------|
| **READY** | Todas las dimensiones obligatorias para el estado actual están VALIDATED o PARTIALLY_VALIDATED. [Decisión] |
| **CONDITIONALLY_READY** | ≤2 dimensiones obligatorias en NOT_VALIDATED con plan de remediación. [Decisión] |
| **NOT_READY** | ≥3 dimensiones obligatorias en NOT_VALIDATED sin plan de remediación. [Decisión] |
| **EVIDENCE_REQUIRED** | ≥3 dimensiones en EVIDENCE_REQUIRED — no se puede evaluar sin más información. [Decisión] |

---

## Uso del Framework

1. Instanciar una evaluación por Lab candidato. [Decisión]
2. Evaluar cada dimensión con el estatus correspondiente. [Decisión]
3. Documentar evidencia encontrada o razón de ausencia. [Decisión]
4. Generar veredicto global basado en criterios. [Decisión]
5. Producir registro de evidencia requerida si el veredicto es EVIDENCE_REQUIRED. [Decisión]

---

## Cross-references

- [lab-integration-framework.md](./lab-integration-framework.md) — Principios de integración
- [lab-contract-template.md](./lab-contract-template.md) — Secciones del contrato que se validan
- [lab-validation-criteria.md](./lab-validation-criteria.md) — Criterios obligatorios y recomendados
- [Architecture Baseline v1.0](../../architecture/architecture-baseline-v1.md) — INV-05 (proporcionalidad)
- [Package 000 — 012-portfolio-model.md](../package-000-foundation/012-portfolio-model.md) — Lab States

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 0        | 0%         |
| [Hipótesis]   | 0        | 0%         |
| [Decisión]    | 28       | 100%       |
| [Visión]      | 0        | 0%         |

> **Nota**: El 100% de decisiones es esperado — este es un framework normativo que define cómo se evalúan Labs. No describe un estado actual sino que establece reglas.
