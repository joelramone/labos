# Propuesta de Roadmap Revisado

## Propósito

Este documento propone un roadmap revisado de packages para LabOS basado en los hallazgos de la revisión arquitectónica. [Decisión] El roadmap preserva packages necesarios, identifica simplificaciones, y distingue packages fundacionales de packages de implementación.

---

## Roadmap Actual (antes de revisión)

| # | Package | Estado | Tipo |
|---|---------|--------|------|
| 000 | Foundation | Completo (pendiente revisión formal) | Fundacional |
| 001 | Research Methodology | Completo | Fundacional |
| 001A | First Lab Integration | Requirements definidos, no ejecutado | Fundacional |
| 002 | Knowledge Architecture | Pendiente | Fundacional |
| 002A | Architecture Review | Este package | Meta |
| 003 | Asset System | Pendiente | Implementación |
| 004 | Product Factory | Pendiente | Implementación |
| 005 | Revenue Engine | Pendiente | Implementación |
| 006 | AI Workspace | Pendiente | Implementación |
| 007 | Automation | Pendiente | Implementación |
| 008 | Operating Model | Pendiente | Implementación |
| 009 | Scaling | Pendiente | Implementación |

---

## Análisis del Roadmap Actual

### Observaciones [Hecho]

1. **10 packages** definidos (excluyendo 002A que es meta-package).
2. **2 completados** (000, 001), **1 con requirements** (001A), **7 pendientes** sin documentación.
3. Los packages 003→009 siguen una lógica secuencial implícita pero no se ha documentado cuáles son prerequisitos de cuáles.
4. Package 001A tiene 16 requirements con 80+ acceptance criteria — un nivel de especificación desproporcionado para su stage.
5. Package 002 (Knowledge Architecture) tiene solo un README placeholder de 4 líneas.

### Problemas Identificados [Decisión]

1. **Packages 003-009 son prematuros.** No se justifica planificar "Revenue Engine" o "Scaling" cuando no hay revenue ni necesidad de escalar. Planificar tan lejos viola el principio documentation-first: se está diseñando sin contexto suficiente.

2. **Package 001A es desproporcionado.** 16 requirements con gobernanza de equipo para un contexto de fundador solo. Necesita simplificación antes de ejecución.

3. **Falta el Value Pipeline.** No existe un package o documento que formalice el pipeline de valor que esta revisión identifica como centro arquitectónico.

4. **Overlap entre 008 (Operating Model) y 001A (Lab Integration).** Ambos cubren gobernanza, roles y procesos operativos. Potencial duplicación.

---

## Roadmap Propuesto

### Clasificación de packages

| Tipo | Definición | Cuándo ejecutar |
|------|-----------|-----------------|
| **Fundacional** | Define conceptos, principios y estructuras que todo lo demás referencia | Ejecutar antes de packages de implementación |
| **Implementación** | Define procesos, herramientas y workflows operativos | Ejecutar cuando existe demanda real del pipeline |
| **Meta** | Revisa y corrige la arquitectura misma | Ejecutar periódicamente o ante hallazgo crítico |
| **Dormido** | Documentado pero no activo hasta trigger | Solo placeholder, no invertir tiempo |

### Roadmap Revisado

| # | Package | Estado propuesto | Tipo | Cambios | Justificación |
|---|---------|-----------------|------|---------|---------------|
| 000 | Foundation | ✅ Completo — ejecutar revisión formal | Fundacional | Sin cambios al package. Ejecutar la revisión pendiente del fundador. | Base estable y coherente. [Hecho] |
| 001 | Research Methodology | ✅ Completo — operar en modo lightweight | Fundacional | ADR-0004 modifica la operación (no el package). Default Small. | El package es riguroso y completo. La operación se simplifica sin modificar el package. [Decisión] |
| 001A | Lab Integration | ⚠️ Ejecutar con Lab Contract completo, gobernanza operativa simplificada | Fundacional | ADR-0003 simplifica la operación diaria (decisiones en 1 párrafo) pero el Lab Contract mantiene 15 secciones como template para visibilidad total. Ejecutar en paralelo con Package 002. | El fundador confirma preferencia por completitud de estructura, aceptando el overhead de documentación. [Decisión] |
| 002 | Knowledge Architecture | 🔜 Siguiente a ejecutar (redefinido) | Fundacional | Scope reducido: definir "Knowledge entity", conectar con pipeline de valor, establecer estructura de captura. NO diseñar retrieval system ni tooling. | Es necesario para completar el pipeline de valor pero debe ser ligero y conceptual, no un sistema de software. [Decisión] |
| 002A | Architecture Review | ✅ Este package | Meta | — | — |
| 003 | Asset System | 📋 Listo para planificar | Implementación | Scope: operacionalizar el Asset_First_Model de Package 000. Definir workflows de creación, validación y publicación de activos. | El Asset_First_Model ya está definido conceptualmente. Este package lo hace operativo. Prerequisito: 002 completado. [Decisión] |
| 004 | Product Factory | 💤 Dormido | Implementación | No planificar hasta que exista ≥3 activos en estado `validado`. | Sin activos validados, no hay materia prima para "product factory". Prematuro. [Decisión] |
| 005 | Revenue Engine | 💤 Dormido | Implementación | No planificar hasta primera transacción real documentada. | Las rutas de monetización ya están en Package 000 (008). Un package separado solo se justifica cuando hay revenue real que sistematizar. [Decisión] |
| 006 | AI Workspace | 💤 Dormido | Implementación | No planificar hasta que un agente IA esté operando una tarea real de LabOS. | AI-native es un principio, no un package premature. Se activa cuando hay un caso de uso concreto. [Decisión] |
| 007 | Automation | 💤 Dormido | Implementación | No planificar hasta que un proceso manual se haya ejecutado ≥5 veces con evidencia de repetibilidad. | "Automatización prematura sin proceso manual validado" es un anti-patrón declarado en engineering-principles. [Hecho] |
| 008 | Operating Model | 🔀 Merge con 001A | Implementación | Fusionar con Package 001A cuando se active gobernanza formal. Evitar overlap. | Los temas de gobierno, roles y operación están cubiertos entre Package 000 (principios) y 001A (integración). Un package separado genera duplicación. [Decisión] |
| 009 | Scaling | 💤 Dormido | Implementación | No planificar hasta que existan ≥3 labs en estado `operando` con revenue. | Escalar sin product-market fit en ningún lab es optimización prematura. [Decisión] |

---

## Secuencia de Ejecución Propuesta

```text
INMEDIATO (0-2 semanas):
├── Ejecutar ADRs P0 (0001, 0002)
├── Ejecutar ADRs P1 (0003, 0004, 0005)
└── Revisión formal de Package 000 por el fundador

CORTO PLAZO (2-6 semanas):
├── Package 002 — Knowledge Architecture (scope reducido)  ──┐
├── Package 001A — Lab Integration (Lab Contract completo,   │ EN PARALELO
│                   gobernanza operativa simplificada)       ──┘
├── Ejecutar ADRs P2 (0006, 0007, 0008)
└── Crear docs/architecture/value-pipeline.md

MEDIANO PLAZO (6-12 semanas):
└── Package 003 — Asset System (operacionalización)

CONDICIONAL (triggers específicos):
├── Package 004 — cuando ≥3 activos validados
├── Package 005 — cuando primera transacción real
├── Package 006 — cuando primer agente IA operativo
├── Package 007 — cuando proceso manual ejecutado ≥5 veces
├── Package 008 — merge con 001A cuando gobernanza formal
└── Package 009 — cuando ≥3 labs en estado operando
```

**Nota sobre Q4:** El Lab Contract se ejecuta con las 15 secciones completas para visibilidad total. La simplificación aplica a la operación diaria (decisiones documentadas en 1 párrafo, sin escalación formal), no al template del contrato. [Decisión]

---

## Packages Eliminados o Fusionados

| Package original | Decisión | Justificación |
|-----------------|----------|---------------|
| 008 - Operating Model | MERGE con 001A | Overlap significativo con gobernanza de Lab Integration. Un solo package cubre "cómo operan los labs dentro de LabOS". [Decisión] |

**Nota:** Ningún package se elimina completamente. Los marcados como "dormidos" conservan su placeholder y se activan cuando su trigger se cumple. [Decisión] Esto preserva la visión de largo plazo sin invertir en planificación prematura.

---

## Principio Rector del Roadmap

> **"No planificar más allá de lo que la evidencia actual justifica."** [Decisión]
>
> Cada package se activa cuando existe evidencia observable de que es necesario, no cuando se anticipa que será necesario. Los triggers de activación son condiciones medibles, no fechas en un calendario.

Este principio es coherente con:
- Manifiesto principio #3: "Hipótesis antes de inversión" [Hecho]
- Anti-patrón de engineering-principles: "Código/documentación 'por si acaso' sin hipótesis de uso" [Hecho]
- Invariante INV-05: Proporcionalidad de proceso a etapa [Decisión]

---

---

## Roadmap Gate Status

**Fecha de evaluación:** 2025-07-22 [Hecho]

### P0 ADRs — RESUELTOS ✅

| ADR | Título | Estado |
|-----|--------|--------|
| ADR-0001 | Jerarquía de Definición Terminológica | ✅ Accepted |
| ADR-0002 | Consolidación de Taxonomía de Activos | ✅ Accepted |

Ambos ADRs P0 están aprobados y documentados en `docs/decisions/`. [Hecho] Las inconsistencias terminológicas y taxonómicas que bloqueaban packages futuros están resueltas. [Hecho]

### Architecture Baseline — CONGELADO ✅

El baseline arquitectónico v1.0 está aprobado y congelado en [architecture-baseline-v1.md](../../architecture/architecture-baseline-v1.md). [Hecho] Incluye: centro arquitectónico, 10 invariantes, terminología canónica, taxonomía de activos, propiedad de entidades, modelo de gobernanza activo y sistema de clasificación.

### Gate de Progreso — APROBADO ✅

**El proyecto puede proceder a la siguiente fase del roadmap:** [Decisión]

1. **Package 002 (Knowledge Architecture)** — scope reducido: definir "Knowledge" como entidad, conectar con pipeline de valor, establecer estructura de captura. [Decisión]
2. **Package 001A (Lab Integration)** — ejecutar en paralelo con Package 002. Lab Contract completo, gobernanza operativa simplificada (nivel SOLO). [Decisión]

**Prerequisitos satisfechos:** [Hecho]
- ✅ Terminología unificada (ADR-0001)
- ✅ Taxonomía consolidada (ADR-0002)
- ✅ Centro arquitectónico declarado (Knowledge-to-Value Pipeline)
- ✅ Invariantes evaluadas y formalizadas (10/10)
- ✅ Baseline congelado (v1.0)

**ADRs P1 pendientes (no bloquean progreso):** ADR-0003 (gobernanza), ADR-0004 (research default), ADR-0005 (value pipeline). Se ejecutan en corto plazo (2-6 semanas). [Decisión]

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 14       | 30%        |
| [Hipótesis]   | 0        | 0%         |
| [Decisión]    | 28       | 70%        |
| [Visión]      | 0        | 0%         |
