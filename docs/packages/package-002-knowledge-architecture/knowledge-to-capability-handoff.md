# Handoff Conocimiento → Capability

## Estado: FUTURO / DORMIDO [Decisión]

Este documento reconoce que un handoff Knowledge → Capability podría ser necesario en el futuro, pero NO lo activa ahora. No existe lifecycle, registro, esquema ni implementación de Capability hasta que se cumplan los triggers de activación.

---

## Por qué existe este documento

| Razón | Detalle |
|-------|---------|
| El architecture baseline menciona Capability como entidad pendiente. | [Architecture Baseline v1.0](../../architecture/architecture-baseline-v1.md) — Sección 5. [Hecho] |
| El roadmap aprobado incluye Capability Architecture como condicional. | Condicionado a ≥3 Labs activos con evidencia operativa de necesidad. [Hecho] |
| Múltiples KOs + múltiples Assets trabajando juntos PODRÍAN constituir una "Capability". | Patrón observado en modelos de madurez organizacional. [Hipótesis] |
| Documentar el concepto ahora previene tener que retrofit más adelante. | Se preserva la intención arquitectónica sin activar overhead prematuro. [Decisión] |

---

## Relación conceptual

```text
Knowledge → Asset → [múltiples Assets + workflow] → Capability (futuro)
```

Una Capability SERÍA: una habilidad repetible y medible de un Lab para producir un resultado específico, compuesta por múltiples Assets, Knowledge Objects y procedimientos operativos. [Hipótesis]

**Distinción clave con Asset:** [Decisión]

| Concepto | Definición | Ejemplo hipotético |
|----------|-----------|-------------------|
| **Asset** | Artefacto reutilizable individual (documento, herramienta, playbook, etc.). | "Guía de ventanas óptimas de trading BTC/USDT". |
| **Capability** (futura) | Combinación de Assets + KOs + workflow + persona que produce un resultado medible y repetible. | "Capacidad de evaluar y optimizar timing de entrada en cualquier par crypto en cualquier exchange". |

Un Asset es un COMPONENTE de una Capability. Una Capability es un SISTEMA de Assets. [Hipótesis]

---

## Señales candidatas de elegibilidad (NO aprobadas)

Estas señales PODRÍAN indicar que una Capability está emergiendo. Son observaciones pendientes de validación, NO criterios formales: [Hipótesis]

| Señal | Descripción |
|-------|-------------|
| Uso repetido del mismo grupo | El mismo conjunto de Assets y KOs se usa junto ≥3 veces en contextos similares. [Hipótesis] |
| Workflow estable | Existe un flujo documentado que combina estos elementos de forma predecible. [Hipótesis] |
| Resultado medible | El output del workflow es cuantificable y repetible. [Hipótesis] |
| Beneficio multi-Lab | Más de un Lab podría beneficiarse de la misma combinación. [Hipótesis] |
| Owner identificable | Una persona o Lab puede ser responsable de la Capability como unidad. [Hipótesis] |
| Criterios de calidad repetibles | Se puede definir "buena ejecución" vs "mala ejecución" del workflow. [Hipótesis] |

---

## Decisiones futuras requeridas (FOUNDER_DECISION_REQUIRED cuando se active)

Cuando los triggers se cumplan, el fundador deberá decidir mediante ADR: [Decisión]

| Decisión pendiente | Pregunta a resolver |
|-------------------|---------------------|
| Definición formal | ¿Qué constituye formalmente una Capability? ¿Qué la diferencia de un Asset complejo o un proceso? [Decisión] |
| Relación con Labs | ¿Las Capabilities pertenecen a Labs individuales o a LabOS? ¿Pueden ser cross-Lab? [Decisión] |
| Lifecycle propio | ¿Las Capabilities tienen su propio ciclo de vida? ¿Con qué estados? [Decisión] |
| Compartición y licenciamiento | ¿Pueden las Capabilities compartirse o licenciarse? ¿Cómo? [Decisión] |
| Versionado | ¿Cómo se versiona algo que es un sistema de componentes? [Decisión] |
| Package responsable | ¿Qué Package define formalmente Capability Architecture? [Decisión] |

---

## Trigger de activación [Decisión]

La Capability Architecture se activa SOLO cuando se cumple al menos uno de estos triggers:

| Trigger | Condición | Evidencia requerida |
|---------|-----------|---------------------|
| Escala de Labs | ≥3 Labs activos en estado `explorando` o superior. | Portfolio Model muestra ≥3 Labs activos simultáneos. [Decisión] |
| Evidencia operativa | ≥1 Lab ha documentado un workflow que usa ≥3 Assets juntos de forma repetida (≥3 usos). | Documentación explícita del workflow y sus resultados. [Decisión] |
| Decisión del fundador | El fundador decide explícitamente formalizar el concepto vía ADR. | ADR aprobado. [Decisión] |

**Hasta que se cumpla un trigger:** No hay Capability lifecycle, no hay registry, no hay schema, no hay implementación. [Decisión]

---

## Riesgos de activación prematura

| Riesgo | Descripción |
|--------|-------------|
| Over-engineering | Crear abstracciones sin evidencia operativa de necesidad. 1 persona con 2 Labs activos no necesita Capabilities formales. [Decisión] |
| Entidades sin sustancia | Registrar "Capabilities" que en realidad son un Asset con un nombre más ambicioso. [Decisión] |
| Overhead de gobernanza | Agregar lifecycle, versionado y ownership a una entidad que nadie consume activamente. [Decisión] |
| Confusión conceptual | Difuminar la línea entre Asset (que funciona bien) y Capability (que es abstracta). [Decisión] |

---

## Owner de la decisión futura

**Fundador, vía ADR, cuando los triggers se cumplan.** [Decisión]

El ADR deberá:
1. Documentar la evidencia que motivó la activación. [Decisión]
2. Definir formalmente Capability con criterios testables. [Decisión]
3. Establecer el lifecycle mínimo. [Decisión]
4. Asignar un Package responsable de la arquitectura. [Decisión]
5. Definir la relación con Assets y KOs existentes. [Decisión]

---

## Cross-references

- [knowledge-to-asset-handoff.md](./knowledge-to-asset-handoff.md) — El handoff previo en el pipeline (Knowledge → Asset)
- [knowledge-lifecycle.md](./knowledge-lifecycle.md) — Estados del KO que alimentarían Capabilities
- [knowledge-ownership.md](./knowledge-ownership.md) — Modelo de propiedad como base para Capability ownership
- [ADR-0002](../../decisions/0002-asset-taxonomy-consolidation.md) — 7 tipos de Asset que compondrían Capabilities
- [007-company-model.md](../package-000-foundation/007-company-model.md) — Asset_First_Model como precursor
- [Architecture Baseline v1.0](../../architecture/architecture-baseline-v1.md) — Pipeline, entidades pendientes (Sección 5)

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 2        | 5%         |
| [Hipótesis]   | 8        | 21%        |
| [Decisión]    | 28       | 74%        |
| [Visión]      | 0        | 0%         |
