# Registro de Documentos Arquitectónicos v1.0 — LabOS

## Metadata

| Campo | Valor |
|-------|-------|
| **Versión** | 1.0 |
| **Fecha** | 2025-07-30 |
| **Estado** | READY_FOR_FOUNDER_APPROVAL |
| **Autor** | Principal Architect (LabOS) |
| **Baseline** | LABOS-ARCH-BASELINE-001 |

---

## Propósito

Registro completo y categorizado de todos los documentos significativos del ecosistema LabOS que constituyen, soportan o complementan el Architecture Baseline v1.0. [Decisión] Este registro es la fuente de verdad para determinar qué documentos son parte del baseline, cuáles lo gobiernan y cuáles lo soportan.

---

## Categorías

| Categoría | Significado | Mutable sin ADR |
|-----------|-------------|-----------------|
| **CANONICAL** | Define entidades, relaciones o estructuras del sistema. Parte del baseline. | No |
| **GOVERNING** | Establece reglas, restricciones o procesos que gobiernan la operación. | No |
| **SUPPORTING** | Aporta contexto, análisis o justificación sin ser normativo. | Sí (con trazabilidad) |
| **OPERATIONAL** | Documentos de ejecución, instancias, o evidencia operativa. | Sí |
| **HISTORICAL** | Registros de proceso completado. Inmutables por INV-10. | No (INV-10) |
| **PROPOSED** | En estado pendiente de aprobación o ejecución. | Sí |

---

## Registro Completo

### Documentos de Arquitectura (docs/architecture/)

| # | ID | Documento | Ruta | Categoría | Package | Status | Baseline | Mutable |
|---|-----|-----------|------|-----------|---------|--------|----------|---------|
| 1 | REG-001 | Architecture Baseline v1.0 | docs/architecture/architecture-baseline-v1.md | CANONICAL | 002A | APPROVED | ✅ Sí | No — requiere ADR |
| 2 | REG-002 | Glosario Canónico | docs/architecture/glossary.md | CANONICAL | 002A | APPROVED | ✅ Sí | No — requiere ADR |
| 3 | REG-003 | Mapa de Dominio Canónico | docs/architecture/canonical-domain-map.md | CANONICAL | 002A | APPROVED | ✅ Sí | No — requiere ADR |
| 4 | REG-004 | Relaciones entre Entidades | docs/architecture/relationships.md | CANONICAL | 002A | APPROVED | ✅ Sí | No — requiere ADR |
| 5 | REG-005 | Package Identity Resolution | docs/architecture/package-identity-resolution.md | SUPPORTING | 002A | APPROVED | ✅ Sí | Sí (con trazabilidad) |
| 6 | REG-006 | Roadmap Reconciliation Post-001A | docs/architecture/post-package-001a-roadmap-reconciliation.md | SUPPORTING | 001A | ROADMAP_RECONCILED | ✅ Sí | Sí (con trazabilidad) |
| 7 | REG-007 | Roadmap Review Post-001A | docs/architecture/post-package-001a-roadmap-review.md | SUPPORTING | 001A | ROADMAP_RECONCILED | ✅ Sí | Sí (con trazabilidad) |
| 8 | REG-008 | Architecture README | docs/architecture/README.md | SUPPORTING | — | ACTIVE | No | Sí |

### Decisiones Arquitectónicas (docs/decisions/)

| # | ID | Documento | Ruta | Categoría | Package | Status | Baseline | Mutable |
|---|-----|-----------|------|-----------|---------|--------|----------|---------|
| 9 | REG-009 | ADR-0001 — Jerarquía Terminológica | docs/decisions/0001-terminology-hierarchy.md | GOVERNING | 002A | ACCEPTED | ✅ Sí | No — solo supersesión |
| 10 | REG-010 | ADR-0002 — Taxonomía de Activos | docs/decisions/0002-asset-taxonomy-consolidation.md | GOVERNING | 002A | ACCEPTED | ✅ Sí | No — solo supersesión |
| 11 | REG-011 | Decisions README | docs/decisions/README.md | SUPPORTING | — | ACTIVE | No | Sí |

### Package 000 — Foundation (docs/packages/package-000-foundation/)

| # | ID | Documento | Ruta | Categoría | Status | Baseline | Mutable |
|---|-----|-----------|------|-----------|--------|----------|---------|
| 12 | REG-012 | Company Vision | docs/packages/package-000-foundation/001-company-vision.md | CANONICAL | CLOSED | ✅ Sí | No (INV-10) |
| 13 | REG-013 | Mission | docs/packages/package-000-foundation/002-mission.md | CANONICAL | CLOSED | ✅ Sí | No (INV-10) |
| 14 | REG-014 | Problem Statement | docs/packages/package-000-foundation/003-problem-statement.md | CANONICAL | CLOSED | ✅ Sí | No (INV-10) |
| 15 | REG-015 | Startup Thesis | docs/packages/package-000-foundation/004-startup-thesis.md | CANONICAL | CLOSED | ✅ Sí | No (INV-10) |
| 16 | REG-016 | Manifesto | docs/packages/package-000-foundation/005-manifesto.md | CANONICAL | CLOSED | ✅ Sí | No (INV-10) |
| 17 | REG-017 | Operating Principles | docs/packages/package-000-foundation/006-operating-principles.md | GOVERNING | CLOSED | ✅ Sí | No (INV-10) |
| 18 | REG-018 | Company Model | docs/packages/package-000-foundation/007-company-model.md | CANONICAL | CLOSED | ✅ Sí | No (INV-10) |
| 19 | REG-019 | Business Model | docs/packages/package-000-foundation/008-business-model.md | CANONICAL | CLOSED | ✅ Sí | No (INV-10) |
| 20 | REG-020 | Revenue Thesis | docs/packages/package-000-foundation/009-revenue-thesis.md | CANONICAL | CLOSED | ✅ Sí | No (INV-10) |
| 21 | REG-021 | Portfolio Model | docs/packages/package-000-foundation/012-portfolio-model.md | CANONICAL | CLOSED | ✅ Sí | No (INV-10) |
| 22 | REG-022 | Foundation README (Glosario base) | docs/packages/package-000-foundation/README.md | CANONICAL | CLOSED | ✅ Sí | No (INV-10) |

### Package 002A — Architecture Review (docs/packages/package-002a-architecture-review/)

| # | ID | Documento | Ruta | Categoría | Status | Baseline | Mutable |
|---|-----|-----------|------|-----------|--------|----------|---------|
| 23 | REG-023 | Invariantes Arquitectónicas | docs/packages/package-002a-architecture-review/architecture-invariants.md | CANONICAL | APPROVED | ✅ Sí | No — requiere ADR |
| 24 | REG-024 | Roadmap Aprobado | docs/packages/package-002a-architecture-review/approved-roadmap-proposal.md | GOVERNING | APPROVED | ✅ Sí | No — requiere ADR |
| 25 | REG-025 | Centro Arquitectónico | docs/packages/package-002a-architecture-review/architectural-center.md | CANONICAL | APPROVED | ✅ Sí | No — requiere ADR |
| 26 | REG-026 | Matriz de Decisiones | docs/packages/package-002a-architecture-review/architecture-decision-matrix.md | SUPPORTING | CLOSED | ✅ Sí | No (INV-10) |
| 27 | REG-027 | Remediation Backlog | docs/packages/package-002a-architecture-review/remediation-backlog.md | OPERATIONAL | ACTIVE | No | Sí (gestión operacional) |
| 28 | REG-028 | ADR Register | docs/packages/package-002a-architecture-review/adr-register.md | SUPPORTING | CLOSED | ✅ Sí | No (INV-10) |

### Package 002 — Knowledge Architecture (docs/packages/package-002-knowledge-architecture/)

| # | ID | Documento | Ruta | Categoría | Status | Baseline | Mutable |
|---|-----|-----------|------|-----------|--------|----------|---------|
| 29 | REG-029 | Knowledge Architecture (22 docs + README) | docs/packages/package-002-knowledge-architecture/ | CANONICAL | CLOSED | ✅ Sí | No (INV-10) |

### Package 001A — First Lab Integration (docs/packages/package-001a-first-lab-integration/)

| # | ID | Documento | Ruta | Categoría | Status | Baseline | Mutable |
|---|-----|-----------|------|-----------|--------|----------|---------|
| 30 | REG-030 | Lab Integration Framework | docs/packages/package-001a-first-lab-integration/lab-integration-framework.md | CANONICAL | CLOSED | ✅ Sí | No (INV-10) |
| 31 | REG-031 | Lab Integration Patterns v1 | docs/packages/package-001a-first-lab-integration/lab-integration-patterns-v1.md | CANONICAL | CLOSED | ✅ Sí | No (INV-10) |
| 32 | REG-032 | Lab Integration Checklist v1 | docs/packages/package-001a-first-lab-integration/lab-integration-checklist-v1.md | CANONICAL | CLOSED | ✅ Sí | No (INV-10) |
| 33 | REG-033 | Lab Contract Template | docs/packages/package-001a-first-lab-integration/lab-contract-template.md | CANONICAL | CLOSED | ✅ Sí | No (INV-10) |
| 34 | REG-034 | Reference Lab Eligibility Criteria v1 | docs/packages/package-001a-first-lab-integration/reference-lab-eligibility-criteria-v1.md | CANONICAL | CLOSED | ✅ Sí | No (INV-10) |
| 35 | REG-035 | CSC Lab Contract | docs/packages/package-001a-first-lab-integration/crypto-scalping-core-lab-contract.md | OPERATIONAL | APPROVED | No | Sí (operacional) |
| 36 | REG-036 | CSC Reference Lab Record | docs/packages/package-001a-first-lab-integration/crypto-scalping-core-reference-lab-record.md | OPERATIONAL | ACTIVE | No | Sí (operacional) |
| 37 | REG-037 | Package 001A Closure Record | docs/packages/package-001a-first-lab-integration/package-001a-closure-record.md | HISTORICAL | CLOSED | ✅ Sí | No (INV-10) |
| 38 | REG-038 | CSC Remediation Plan | docs/packages/package-001a-first-lab-integration/crypto-scalping-core-remediation-plan.md | OPERATIONAL | ACTIVE | No | Sí (operacional) |

### Package 001 — Research Methodology (docs/packages/package-001-research-methodology/)

| # | ID | Documento | Ruta | Categoría | Status | Baseline | Mutable |
|---|-----|-----------|------|-----------|--------|----------|---------|
| 39 | REG-039 | Research Methodology (20+ docs) | docs/packages/package-001-research-methodology/ | CANONICAL | CLOSED | ✅ Sí | No (INV-10) |

### Post-Baseline Package and Roadmap Records

| # | ID | Documento | Ruta | Categoría | Status | Baseline | Mutable |
|---|-----|-----------|------|-----------|--------|----------|---------|
| 40 | REG-040 | Package 003 — Asset System | docs/packages/package-003-asset-system/ | CANONICAL | CLOSED | No — post-baseline extension; formal baseline reconciliation pending | No (INV-10) |
| 41 | REG-041 | Post-Package 003 Roadmap Reconciliation | docs/architecture/post-package-003-roadmap-reconciliation.md | SUPPORTING | PLANNING | No | Sí — roadmap governance |
| 42 | REG-042 | Future Infrastructure Register | docs/architecture/future-infrastructure-register.md | SUPPORTING | FUTURE / DORMANT | No | Sí — trigger registry |
| 43 | REG-043 | Post-Package 003 Roadmap Review | docs/architecture/post-package-003-roadmap-review.md | SUPPORTING | REVIEWED | No | Sí — append-only review evidence |
| 44 | REG-044 | Package 004 — Product Factory | docs/packages/package-004-product-factory/ | CANONICAL | CLOSED — FD-P004-CLOSURE-001 | No — post-baseline extension | No (INV-10) |

---

## Resumen por Categoría

| Categoría | Cantidad | En Baseline | Mutable sin ADR |
|-----------|----------|-------------|-----------------|
| CANONICAL | 25 | 23 | No |
| GOVERNING | 5 | 5 | No |
| SUPPORTING | 10 | 5 | Sí (con trazabilidad) |
| OPERATIONAL | 4 | 0 | Sí |
| HISTORICAL | 1 | 1 | No (INV-10) |
| PROPOSED | 0 | 0 | — |
| **TOTAL** | **44** | **34** | — |

[Hecho] 34 documentos (o grupos documentales) permanecen en Architecture Baseline v1.0. Packages 003 and 004 are CLOSED post-baseline canonical extensions; the three post-P003 roadmap records are supporting and do not modify the frozen Baseline. Architecture Freeze remains PRESERVED.

---

## Política de Actualización del Registro

1. **Nuevos documentos CANONICAL o GOVERNING** solo se agregan al registro mediante aprobación del fundador tras entrega de un package. [Decisión]
2. **Documentos SUPPORTING** pueden agregarse con trazabilidad y sin aprobación formal. [Decisión]
3. **Documentos OPERATIONAL** se gestionan independientemente del baseline. [Decisión]
4. **Eliminación de documentos del baseline** requiere ADR con justificación. [Decisión]
5. **Cambio de categoría** (e.g., SUPPORTING → CANONICAL) requiere aprobación del fundador. [Decisión]

---

## Review Triggers

Este registro se revisa cuando: [Decisión]

- Se cierra un nuevo package (agregar documentos producidos).
- Se aprueba un nuevo ADR (agregar al registro).
- Se detecta un documento no registrado que debería estarlo.
- Se actualiza el Architecture Baseline (nueva versión).

---

## Cross-references

- [architecture-baseline-v1.0-manifest.md](./architecture-baseline-v1.0-manifest.md) — Manifiesto del baseline
- [architecture-baseline-v1.md](./architecture-baseline-v1.md) — Documento de baseline
- [architecture-change-control-v1.0.md](./architecture-change-control-v1.0.md) — Control de cambios

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 2        | 11%        |
| [Hipótesis]   | 0        | 0%         |
| [Decisión]    | 16       | 89%        |
| [Visión]      | 0        | 0%         |
