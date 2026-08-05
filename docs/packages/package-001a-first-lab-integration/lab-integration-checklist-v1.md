# Lab Integration Checklist v1

## Metadata

| Campo | Valor |
|-------|-------|
| **Documento** | Checklist de integración de Labs |
| **Versión** | 1.0 |
| **Package** | 001A — First Lab Integration |
| **Batch** | 4 — Reference Lab Freeze & Package Closure |
| **Fecha** | 2025-07-30 |
| **Reference Lab** | LABOS-REF-LAB-0001 (Crypto Scalping Core) |

---

## Propósito

Definir el checklist completo para integrar un Lab al ecosistema LabOS. [Decisión] Organizado en 5 fases secuenciales con ítems verificables, responsables y outputs esperados.

---

## Fase 0 — Intake (Recepción)

**Objetivo:** Determinar si el Lab es candidato viable para integración. [Decisión]

| # | Ítem | Requerido | Evidencia | Responsable | Status | Blocker | Output |
|---|------|-----------|-----------|-------------|--------|---------|--------|
| 0.1 | Lab existe (repositorio, documentos, o artefactos identificables) | Obligatorio | URL de repo o inventario de artefactos | Principal Architect | ☐ | P0 | Confirmación de existencia |
| 0.2 | Owner identificado y disponible | Obligatorio | Nombre + rol + disponibilidad | Principal Architect | ☐ | P0 | Owner confirmado |
| 0.3 | Dominio definido (qué investiga/produce el Lab) | Obligatorio | Descripción en 1-2 oraciones | Owner | ☐ | P0 | Domain statement |
| 0.4 | No duplica un Lab existente activo | Obligatorio | Comparación con portafolio actual | Principal Architect | ☐ | P0 | Confirmación de no-duplicidad |
| 0.5 | Fundador aprueba iniciar integración | Obligatorio | Decisión documentada | Fundador | ☐ | P0 | Founder decision record |
| 0.6 | Hipótesis de monetización documentada (al menos como hipótesis) | Opcional | Documento o declaración | Owner | ☐ | — | Monetization hypothesis draft |

**Gate de salida:** Todos los ítems obligatorios completos → proceder a Fase 1. [Decisión]

---

## Fase 1 — Validation (Evaluación de Readiness)

**Objetivo:** Evaluar la madurez y readiness del Lab para integración formal. [Decisión]

| # | Ítem | Requerido | Evidencia | Responsable | Status | Blocker | Output |
|---|------|-----------|-----------|-------------|--------|---------|--------|
| 1.1 | Assessment de readiness multi-dimensional | Obligatorio | Documento de evaluación con criterios | Principal Architect | ☐ | P1 | `{lab}-readiness-assessment.md` |
| 1.2 | Identificar decisiones que requieren input del fundador | Obligatorio | Lista de decisiones P0 | Principal Architect | ☐ | P0 | Founder decisions document |
| 1.3 | Resolver decisiones P0 bloqueantes | Obligatorio | Decisiones documentadas con respuesta | Fundador | ☐ | P0 | Founder decisions resolved |
| 1.4 | Lab State candidato identificado con evidencia | Obligatorio | Mapping estado ↔ evidencia | Principal Architect | ☐ | P1 | State recommendation |
| 1.5 | Boundaries del Lab definidos (IN/OUT) | Obligatorio | Declaración de scope | Owner + Architect | ☐ | P1 | Boundary analysis |
| 1.6 | Autonomía del Lab confirmada | Obligatorio | Verificación de dependencias | Principal Architect | ☐ | P1 | Dependency assessment |
| 1.7 | Profile del Lab creado | Opcional | Documento descriptivo | Principal Architect | ☐ | — | `{lab}-lab-profile.md` |

**Gate de salida:** Readiness ≥ mínimo viable, decisiones P0 resueltas → proceder a Fase 2. [Decisión]

---

## Fase 2 — Repository Discovery (Inspección)

**Objetivo:** Inspeccionar el repositorio/artefactos del Lab y documentar su estado real. [Decisión]

| # | Ítem | Requerido | Evidencia | Responsable | Status | Blocker | Output |
|---|------|-----------|-----------|-------------|--------|---------|--------|
| 2.1 | Inventario de repositorio (estructura, archivos clave) | Obligatorio | Listado estructurado | Principal Architect | ☐ | P1 | `{lab}-repository-inventory.md` |
| 2.2 | Mapa de workflow de investigación/producción | Obligatorio | Pipeline documentado con etapas | Principal Architect | ☐ | P1 | `{lab}-research-workflow-map.md` |
| 2.3 | Inventario de artefactos de investigación | Obligatorio | Lista con tipos y conteos | Principal Architect | ☐ | P1 | `{lab}-research-artifacts-inventory.md` |
| 2.4 | Mapa de dependencias (internas y externas) | Obligatorio | Deps listadas con versiones | Principal Architect | ☐ | P2 | `{lab}-dependency-map.md` |
| 2.5 | Source of Truth map | Obligatorio | Declaración por concepto | Principal Architect | ☐ | P1 | `{lab}-source-of-truth-map.md` |
| 2.6 | Knowledge Object candidates identificados | Opcional | Lista con criterios de evaluación | Principal Architect | ☐ | — | `{lab}-knowledge-object-candidates.md` |
| 2.7 | Asset candidates identificados | Opcional | Lista con 4 condiciones evaluadas | Principal Architect | ☐ | — | `{lab}-asset-candidates.md` |
| 2.8 | Monetization hypotheses documentadas | Opcional | Hipótesis con campos mínimos | Principal Architect | ☐ | — | `{lab}-monetization-hypothesis.md` |
| 2.9 | Estrategias/productos inventariados | Condicional | Listado con métricas si aplica | Principal Architect | ☐ | — | `{lab}-strategy-inventory.md` |
| 2.10 | Gap analysis vs. frameworks LabOS | Obligatorio | Gaps identificados y clasificados | Principal Architect | ☐ | P2 | `integration-gap-analysis.md` |

**Gate de salida:** Inventarios completos, estado real documentado → proceder a Fase 3. [Decisión]

---

## Fase 3 — Lab Contract (Contrato Formal)

**Objetivo:** Crear, validar y obtener aprobación del Lab Contract formal. [Decisión]

| # | Ítem | Requerido | Evidencia | Responsable | Status | Blocker | Output |
|---|------|-----------|-----------|-------------|--------|---------|--------|
| 3.1 | Lab State aprobado por fundador | Obligatorio | Decisión documentada | Fundador | ☐ | P0 | Founder decision (Lab State) |
| 3.2 | Lab Contract instanciado (15 secciones) | Obligatorio | Documento completo con evidencia | Principal Architect | ☐ | P0 | `{lab}-lab-contract.md` |
| 3.3 | Evidence map creado (trazabilidad) | Obligatorio | Mapping sección ↔ evidencia | Principal Architect | ☐ | P1 | `{lab}-lab-contract-evidence-map.md` |
| 3.4 | Compliance evaluation ejecutada | Obligatorio | Evaluación contra frameworks | Principal Architect | ☐ | P1 | `{lab}-lab-contract-compliance.md` |
| 3.5 | Remediaciones documentadas (si existen gaps) | Condicional | Plan con IDs, owners, targets | Principal Architect | ☐ | P2 | `{lab}-remediation-plan.md` |
| 3.6 | Auto-review del batch ejecutado | Obligatorio | Documento de review con veredicto | Principal Architect | ☐ | P2 | `package-XXX-batchN-review.md` |
| 3.7 | Lab Contract presentado al fundador | Obligatorio | Contrato en estado READY_FOR_APPROVAL | Principal Architect | ☐ | P0 | Contrato listo para decisión |
| 3.8 | Fundador aprueba Lab Contract | Obligatorio | Decisión: APPROVE/CONDITIONS/REJECT | Fundador | ☐ | P0 | Founder decision (approval) |

**Gate de salida:** Lab Contract APPROVED → proceder a Fase 4. [Decisión]

---

## Fase 4 — Closure (Cierre del Package)

**Objetivo:** Registrar el Lab como Reference Lab (si califica), extraer patrones y cerrar formalmente el package. [Decisión]

| # | Ítem | Requerido | Evidencia | Responsable | Status | Blocker | Output |
|---|------|-----------|-----------|-------------|--------|---------|--------|
| 4.1 | Evaluar elegibilidad como Reference Lab | Obligatorio | Criterios evaluados | Principal Architect | ☐ | P2 | Eligibility assessment |
| 4.2 | Registrar como Reference Lab (si elegible) | Condicional | Registro formal con ID | Principal Architect | ☐ | — | `{lab}-reference-lab-record.md` |
| 4.3 | Extraer patrones de integración | Obligatorio | Patrones domain-neutral documentados | Principal Architect | ☐ | P2 | `lab-integration-patterns-vN.md` |
| 4.4 | Crear checklist reutilizable | Obligatorio | Checklist con fases y ítems | Principal Architect | ☐ | P2 | `lab-integration-checklist-vN.md` |
| 4.5 | Definir criterios de elegibilidad | Obligatorio | Criterios formales documentados | Principal Architect | ☐ | P2 | `reference-lab-eligibility-criteria-vN.md` |
| 4.6 | Final audit del package | Obligatorio | Verificación de completitud | Principal Architect | ☐ | P2 | `package-XXX-final-audit.md` |
| 4.7 | Closure record | Obligatorio | Registro formal de cierre | Principal Architect | ☐ | P1 | `package-XXX-closure-record.md` |
| 4.8 | README actualizado | Obligatorio | Refleja estado CLOSED | Principal Architect | ☐ | P2 | README.md actualizado |
| 4.9 | Auto-review del batch de cierre | Obligatorio | Review con veredicto | Principal Architect | ☐ | P2 | `package-XXX-batchN-review.md` |

**Gate de salida:** Closure record completo, README actualizado → Package CLOSED. [Decisión]

---

## Notas de uso

### Campos de status

| Status | Significado |
|--------|-------------|
| ☐ | No iniciado |
| ⏳ | En progreso |
| ✅ | Completo |
| ⛔ | Bloqueado |
| ➖ | No aplica (justificar) |

### Niveles de blocker

| Nivel | Significado | Acción |
|-------|-------------|--------|
| P0 | Bloquea el gate de salida de la fase | Resolver antes de avanzar |
| P1 | Bloquea calidad del output pero no la fase | Resolver dentro de la fase |
| P2 | No bloquea — documentar como remediación | Resolver post-fase si tiene trigger |
| — | No es blocker | Completar si hay bandwidth |

---

## Cross-references

- [lab-integration-patterns-v1.md](./lab-integration-patterns-v1.md) — Patrones que informan este checklist
- [crypto-scalping-core-reference-lab-record.md](./crypto-scalping-core-reference-lab-record.md) — Reference Lab que validó este checklist
- [reference-lab-eligibility-criteria-v1.md](./reference-lab-eligibility-criteria-v1.md) — Criterios para Fase 4.1
- [lab-integration-framework.md](./lab-integration-framework.md) — Framework original (Batch 1)

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 0        | 0%         |
| [Hipótesis]   | 0        | 0%         |
| [Decisión]    | 35       | 100%       |
| [Visión]      | 0        | 0%         |

> **Nota:** 100% decisiones porque un checklist es enteramente prescriptivo — define qué hacer, en qué orden, con qué criterio. No documenta hechos ni hace predicciones.
