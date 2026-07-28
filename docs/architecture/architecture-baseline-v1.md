# Architecture Baseline v1.0 — LabOS

## Metadata

| Campo | Valor |
|-------|-------|
| **Versión** | 1.0 |
| **Fecha** | 2025-07-22 |
| **Estado** | APPROVED |
| **Autor** | Fundador |
| **Origen** | Package 002A — Architecture Review |

---

## Propósito

Este documento congela el baseline arquitectónico v1.0 de LabOS. [Decisión] Todo package futuro debe operar dentro de los límites definidos aquí. Cualquier cambio a este baseline requiere un nuevo ADR y una nueva versión del documento.

---

## Sección 1: Centro Arquitectónico — Knowledge-to-Value Pipeline

El centro arquitectónico de LabOS es el **Knowledge-to-Value Pipeline**: el flujo de transformación de conocimiento en valor económico. [Decisión]

```text
Research → Knowledge → Assets → Products → Revenue
```

**Implicaciones:** [Decisión]

1. Investigación no es el fin — es la entrada del pipeline.
2. Documentación es el medio de transporte, no el destino.
3. Revenue es la salida, no el motor. El pipeline tiene secuencia por diseño.
4. El Asset_First_Model es el acelerador del pipeline.
5. Todo componente que no contribuye al pipeline debe justificar su existencia.

**Centro secundario:** Documentation-first como método operativo transversal. [Decisión]

Referencia completa: [architectural-center.md](../packages/package-002a-architecture-review/architectural-center.md)

---

## Sección 2: Invariantes Arquitectónicas

10 invariantes activas (7 confirmadas + 3 confirmadas con modificación): [Hecho]

| ID | Invariante | Estado | Resumen |
|----|-----------|--------|---------|
| INV-01 | Clasificación epistémica universal | CONFIRM | Toda afirmación sustantiva se clasifica como [Hecho], [Hipótesis], [Visión] o [Decisión]. Sin excepciones. |
| INV-02 | Toda investigación >4h produce un activo | CONFIRM | O produce activo reutilizable, o produce nota de cierre. Sin excepciones. |
| INV-03 | Validación de demanda antes de inversión | CONFIRM | No invertir >1 semana sin hipótesis de monetización documentada. Excepción: LabOS infraestructura interna. |
| INV-04 | Fuente de verdad única por concepto | MODIFY | Cada concepto tiene 1 documento fuente. Extensiones permitidas con referencia explícita. Formalizadas vía ADR-0001. |
| INV-05 | Proporcionalidad de proceso a etapa | CONFIRM | Complejidad de governance proporcional a operadores e ingresos. |
| INV-06 | Documentation-first es el modo de operación | CONFIRM | Ningún entregable se considera completo sin documentación. Excepción: spikes <4h declarados explícitamente. |
| INV-07 | Glosario Package 000 es fuente de verdad global | MODIFY | 13 términos canónicos. Evolución solo vía ADR. Formalizada vía ADR-0001. |
| INV-08 | Revenue tiene prioridad sobre infraestructura | CONFIRM | Revenue > infraestructura que no genera ingreso en 90 días. Excepción: cuando infraestructura ES el producto. |
| INV-09 | No más de 3 labs activos simultáneos | MODIFY | Reducido de 5 a 3 como umbral práctico. Expandible con evidencia de ≥30h/semana sostenidas. |
| INV-10 | Packages no se modifican retroactivamente | CONFIRM | Cambios requieren ADR. Excepción: correcciones de formato/typos. |

Referencia completa: [architecture-invariants.md](../packages/package-002a-architecture-review/architecture-invariants.md)

---

## Sección 3: Terminología Canónica

La fuente de verdad terminológica es el glosario de Package 000 README.md (13 términos base). [Decisión]

**Reglas:** [Decisión]
- Packages posteriores EXTIENDEN pero no REDEFINEN.
- Toda extensión referencia la definición base.
- Modificar definiciones base requiere ADR.

**Términos pendientes de definición formal:** Knowledge (Package 002), Product (Package 004), Capability (condicional).

Referencias:
- [ADR-0001 — Jerarquía de Definición Terminológica](../decisions/0001-terminology-hierarchy.md)
- [glossary.md — Glosario canónico consolidado](./glossary.md)

---

## Sección 4: Taxonomía de Activos

7 tipos canónicos con reglas de compartición: [Decisión]

| # | Tipo | Compartible por defecto | Notas |
|---|------|------------------------|-------|
| 1 | Documento | ✅ Sí | Registro de conocimiento, análisis o decisiones |
| 2 | Template | ✅ Sí | Plantilla reutilizable con estructura predefinida |
| 3 | Dataset | ✅ Sí | Conjunto de datos organizados y documentados |
| 4 | Herramienta | ✅ Sí | Software, script o utilidad ejecutable |
| 5 | Componente | ❌ No | Lab-Private por defecto; publicable explícitamente |
| 6 | Framework | ✅ Sí | Estructura conceptual o técnica |
| 7 | Playbook | ❌ No | Lab-Private por defecto; publicable explícitamente |

**Estados de activo:** borrador → validado → productizado [Hecho]

**Criterio mínimo:** 5 campos obligatorios (nombre, tipo, descripción, hipótesis de uso, estado). [Hecho]

Referencia: [ADR-0002 — Consolidación de Taxonomía de Activos](../decisions/0002-asset-taxonomy-consolidation.md)

---

## Sección 5: Propiedad de Entidades

| Entidad | Owner | Fuente |
|---------|-------|--------|
| Lab | Fundador (creación) / Lab owner (operación) | Package 000 |
| Asset | Lab de origen | Package 000 |
| Research | Lab ejecutor | Package 001 |
| Package | LabOS | Package 000 |
| Revenue_Thesis | Lab que propone | Package 000 |
| Lab_Contract | LabOS (template) / Lab (instancia) | Package 001A |
| Lab_State | LabOS (definición) / Fundador (asignación) | Package 000 |
| Knowledge | Pendiente | Package 002 |
| Product | Pendiente | Package 004 |

Referencia: [canonical-domain-map.md](./canonical-domain-map.md)

---

## Sección 6: Modelo de Gobernanza Activo

**Nivel actual: SOLO** (1 operador, pre-revenue) [Hecho]

| Aspecto | Implementación en nivel SOLO |
|---------|------------------------------|
| Decisiones | Documentadas en 1 párrafo por el fundador. Sin escalación formal. [Decisión] |
| Lab Contract | Completo (15 secciones) como template para visibilidad total. [Decisión] |
| Revisión formal | No obligatoria hasta trigger de gobernanza. [Decisión] |
| Escalación | No aplica — 1 decision-maker. [Hecho] |
| Review cycle | Proporcional a Lab_State del lab. [Decisión] |

**Triggers de escalación a Nivel EARLY:** [Decisión]
- Primer operador distinto al fundador, O
- Revenue recurrente >$1000/mes

**Triggers de escalación a Nivel TEAM:** [Decisión]
- >1 operador activo

---

## Sección 7: Sistema de Clasificación Activo

### Lab States (ACTIVO) [Hecho]

| Estado | Significado | Review asociado |
|--------|-------------|-----------------|
| idea | Identificado, sin actividad | 0 revisión |
| explorando | Actividad exploratoria en curso | 15 min/mes |
| validando | Hipótesis de monetización en prueba | 30 min/mes |
| operando | Revenue real generado | 1h/mes |
| pausado | Suspendido temporalmente | 0 revisión |

Fuente: Package 000 — 012-portfolio-model.md [Hecho]

### Maturity Model (DORMIDO) [Decisión]

El Maturity Model de Package 001A (L0-L4) está documentado como framework futuro. [Decisión]

**Trigger de activación:** ≥3 labs en estado `explorando` o superior simultáneamente Y ≥1 operador distinto al fundador. [Decisión]

---

## Sección 8: ADRs Aprobados

| ADR | Título | Estado | Fecha | Prioridad |
|-----|--------|--------|-------|-----------|
| ADR-0001 | Jerarquía de Definición Terminológica | Accepted | 2025-07-22 | P0 |
| ADR-0002 | Consolidación de Taxonomía de Activos | Accepted | 2025-07-22 | P0 |

ADRs pendientes de ejecución (P1, P2): ADR-0003 a ADR-0008 en [adr-register.md](../packages/package-002a-architecture-review/adr-register.md). [Hecho]

---

## Sección 9: Condiciones para Actualización del Baseline

Este baseline se actualiza (nueva versión) cuando: [Decisión]

1. Se aprueba un ADR que modifica una invariante arquitectónica (INV-01 a INV-10).
2. Se aprueba un ADR que modifica una definición canónica del glosario de Package 000.
3. Se cambia el centro arquitectónico.
4. Se agrega o elimina un tipo de activo de la taxonomía canónica.
5. Se modifica el pipeline de valor (agregar/remover etapas).

**NO requieren nueva versión:** [Decisión]
- ADRs que simplifican operación sin modificar invariantes (e.g., ADR-0003, ADR-0004).
- Nuevos packages que operan dentro del baseline existente.
- Extensiones terminológicas que no contradicen definiciones base.

**Proceso de actualización:** [Decisión]
1. Proponer ADR con justificación de cambio.
2. Aprobar ADR.
3. Actualizar este documento (nueva versión: 1.1, 2.0, etc.).
4. Notificar impacto en packages existentes.

---

## Sección 10: Referencias

### Documentos de arquitectura

- [architectural-center.md](../packages/package-002a-architecture-review/architectural-center.md) — Centro arquitectónico [Hecho]
- [architecture-invariants.md](../packages/package-002a-architecture-review/architecture-invariants.md) — Invariantes [Hecho]
- [glossary.md](./glossary.md) — Glosario canónico [Hecho]
- [canonical-domain-map.md](./canonical-domain-map.md) — Mapa de entidades [Hecho]
- [relationships.md](./relationships.md) — Relaciones entre entidades [Hecho]

### ADRs

- [ADR-0001](../decisions/0001-terminology-hierarchy.md) — Jerarquía terminológica [Hecho]
- [ADR-0002](../decisions/0002-asset-taxonomy-consolidation.md) — Taxonomía de activos [Hecho]

### Packages fuente

- [Package 000 — Foundation](../packages/package-000-foundation/README.md) [Hecho]
- [Package 001 — Research Methodology](../packages/package-001-research-methodology/) [Hecho]
- [Package 001A — First Lab Integration (requirements)](../../.kiro/specs/package-001a-first-lab-integration/requirements.md) [Hecho]
- [Package 002A — Architecture Review](../packages/package-002a-architecture-review/) [Hecho]

### Documentos de soporte

- [architecture-decision-matrix.md](../packages/package-002a-architecture-review/architecture-decision-matrix.md) [Hecho]
- [remediation-backlog.md](../packages/package-002a-architecture-review/remediation-backlog.md) [Hecho]
- [approved-roadmap-proposal.md](../packages/package-002a-architecture-review/approved-roadmap-proposal.md) [Hecho]
- [adr-register.md](../packages/package-002a-architecture-review/adr-register.md) [Hecho]

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 24       | 38%        |
| [Hipótesis]   | 0        | 0%         |
| [Decisión]    | 39       | 62%        |
| [Visión]      | 0        | 0%         |
