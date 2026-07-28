# Framework de Integración de Labs

## Propósito

Este documento define qué significa integrar un Lab al ecosistema LabOS, los principios que rigen la integración, y el proceso general desde la identificación hasta la operación. [Decisión]

---

## ¿Qué significa integrar un Lab?

Integrar un Lab es formalizar la relación entre un proyecto independiente y LabOS como sistema transversal. [Decisión] La integración no implica subordinación — implica un acuerdo de cooperación documentado (Lab Contract) donde ambas partes obtienen beneficio.

### El Lab obtiene

- Acceso a infraestructura compartida (templates, steering, metodología de investigación, quality gates). [Hecho]
- Visibilidad en el portafolio con estado y priorización definidos. [Hecho]
- Mecanismos de compartición de conocimiento y activos con otros Labs. [Hecho]

### LabOS obtiene

- Evidencia de uso real de su infraestructura (valida su propia hipótesis de producto). [Hecho]
- Activos compartibles que enriquecen el ecosistema. [Hipótesis]
- Señales de qué infraestructura priorizar según necesidades reales. [Hecho]

---

## Principios de Integración

### 1. No-destructivo [Decisión]

La integración NO modifica el proyecto que se integra. [Decisión] LabOS se adapta al Lab, no al revés. El Lab conserva su nombre, estructura, procesos internos e identidad.

**Implica:**
- No se renombra el proyecto para ajustarse a convenciones de LabOS.
- No se migra documentación existente a formato LabOS obligatoriamente.
- No se impone tooling ni workflows que el Lab no use.

### 2. Preservación de identidad [Decisión]

Cada Lab mantiene su misión, alcance y autonomía operativa. [Decisión] El Lab Contract documenta la relación sin absorber al Lab en LabOS.

**Implica:**
- El Lab puede operar sin LabOS si se desacopla (Decoupling Protocol).
- Las decisiones de dominio pertenecen al Lab, no a LabOS.
- El Lab define sus propios procesos internos dentro de su Lab_Boundary.

### 3. Reutilizable [Decisión]

El proceso de integración es genérico. [Decisión] Lo que se diseña para un Lab debe servir para cualquier Lab del portafolio sin modificación sustancial.

**Implica:**
- El Lab Contract es un template, no un documento ad-hoc por Lab.
- El lifecycle es estándar — los pasos son los mismos independientemente del dominio.
- Las reglas de boundary aplican uniformemente.

### 4. Incremental [Decisión]

Un Lab no necesita estar "completo" para integrarse. [Decisión] El Lab Contract acepta secciones pendientes y el lifecycle permite avanzar con información parcial.

**Implica:**
- Un Lab en estado `idea` puede iniciar integración con información mínima.
- Las secciones se completan a medida que el Lab evoluciona.
- No existe un "mínimo de madurez" para la integración — existe un mínimo de información documentable.

### 5. Proporcional a la etapa [Decisión]

Coherente con INV-05 (proporcionalidad de proceso a etapa): la complejidad de la integración es proporcional al estado del Lab y al número de operadores. [Decisión]

**Nivel SOLO (actual):** [Hecho]
- Decisiones de integración en 1 párrafo.
- Sin revisión formal obligatoria.
- Sin escalación — 1 decision-maker (fundador).

---

## Proceso General de Integración

```text
┌──────────────┐    ┌────────────┐    ┌──────────────────┐
│Identification│───▶│ Assessment │───▶│Contract Creation │
└──────────────┘    └────────────┘    └──────────────────┘
                                              │
                                              ▼
┌──────────┐    ┌───────────┐    ┌────────────────┐
│  Review  │◀───│ Operation │◀───│  Onboarding    │
└──────────┘    └───────────┘    └────────────────┘
```

Las 6 etapas se detallan en [lab-integration-lifecycle.md](./lab-integration-lifecycle.md). [Hecho]

---

## Prerrequisitos Mínimos para Integración

Un proyecto califica como candidato a Lab si cumple la definición canónica de Package 000: "Vertical de negocio independiente dentro del portafolio LabOS, con hipótesis de producto propia y estado de madurez definido." [Hecho]

Para la integración formal (creación de Lab Contract), se requiere adicionalmente verificar 4 características (extensión de Package 001A, per ADR-0001 §5): [Decisión]

1. **Independencia de dominio** — opera en un dominio no reclamado por otro Lab activo.
2. **Preservación de identidad** — mantiene nombre, misión e identidad propia.
3. **Autonomía operacional** — capaz de operar sin LabOS si se desacopla.
4. **Voluntad de integración** — acepta el Lab Contract estándar.

---

## Relación con la Terminología Canónica

Este framework extiende la definición de "Lab" de Package 000 sin redefinirla, conforme a [ADR-0001](../../decisions/0001-terminology-hierarchy.md). [Hecho] Los tipos de activos referenciados siguen la taxonomía canónica de 7 tipos definida en [ADR-0002](../../decisions/0002-asset-taxonomy-consolidation.md). [Hecho]

---

## Relación con el Baseline Arquitectónico

- **INV-01 (Clasificación epistémica):** Todos los documentos de integración clasifican afirmaciones. [Hecho]
- **INV-04 (Fuente de verdad única):** El Lab Contract es la fuente de verdad para la relación Lab-LabOS. [Decisión]
- **INV-05 (Proporcionalidad):** Nivel SOLO activo — governance mínima. [Hecho]
- **INV-09 (Máx 3 labs activos):** La integración formal no cambia el Lab_State — un Lab integrado en `idea` sigue siendo `idea`. [Decisión]

---

## Cross-references

- [lab-contract-template.md](./lab-contract-template.md) — Template de 15 secciones
- [lab-integration-lifecycle.md](./lab-integration-lifecycle.md) — 6 etapas detalladas
- [lab-boundaries.md](./lab-boundaries.md) — Clasificación de límites
- [ADR-0001](../../decisions/0001-terminology-hierarchy.md) — Jerarquía terminológica
- [ADR-0002](../../decisions/0002-asset-taxonomy-consolidation.md) — Taxonomía de activos
- [Architecture Baseline v1.0](../../architecture/architecture-baseline-v1.md) — Invariantes
- [Package 000 — 012-portfolio-model.md](../package-000-foundation/012-portfolio-model.md) — Estados de Lab

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 11       | 33%        |
| [Hipótesis]   | 1        | 3%         |
| [Decisión]    | 21       | 64%        |
| [Visión]      | 0        | 0%         |
