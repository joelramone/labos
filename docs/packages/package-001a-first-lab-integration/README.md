# Package 001A — First Lab Integration

## Propósito

Este package define el framework completo de integración de Labs al ecosistema LabOS. [Decisión] Establece el proceso estándar, contratos, ciclo de vida, límites y políticas que aplican a cualquier Lab presente o futuro del portafolio.

## Caso de Estudio

**Crypto Scalping Core** — Trading cuantitativo, estrategias algorítmicas y herramientas de trading. [Hecho] Estado actual: `idea`. [Hecho]

> **Nota:** SentinelOps fue el caso de estudio original en los requirements. Por decisión del fundador (separación corporativa/personal), el caso de estudio activo es Crypto Scalping Core. SentinelOps permanece solo como referencia histórica en documentos ya versionados. [Decisión]

## Documentos del Package

| # | Documento | Propósito |
|---|-----------|-----------|
| 1 | [lab-integration-framework.md](./lab-integration-framework.md) | Framework completo de integración — qué significa integrar un Lab |
| 2 | [lab-contract-template.md](./lab-contract-template.md) | Template del Lab Contract (15 secciones) con guía por sección |
| 3 | [lab-integration-lifecycle.md](./lab-integration-lifecycle.md) | 6 etapas del ciclo de vida de integración |
| 4 | [lab-boundaries.md](./lab-boundaries.md) | 4 clasificaciones de límites y reglas de propiedad |
| 5 | [lab-maturity-model.md](./lab-maturity-model.md) | Framework dormido de madurez (L0-L4) |
| 6 | [lab-integration-checklist.md](./lab-integration-checklist.md) | Checklist paso a paso por etapa del lifecycle |
| 7 | [crypto-scalping-core-lab-contract.md](./crypto-scalping-core-lab-contract.md) | Instanciación del Lab Contract para Crypto Scalping Core |
| 8 | [crypto-scalping-core-integration-assessment.md](./crypto-scalping-core-integration-assessment.md) | Evaluación de readiness del Lab |
| 9 | [crypto-scalping-core-capability-map.md](./crypto-scalping-core-capability-map.md) | Mapa de capacidades potenciales |
| 10 | [crypto-scalping-core-knowledge-map.md](./crypto-scalping-core-knowledge-map.md) | Dominios de conocimiento relevantes |
| 11 | [crypto-scalping-core-asset-inventory.md](./crypto-scalping-core-asset-inventory.md) | Inventario de activos (actual y proyectado) |
| 12 | [crypto-scalping-core-integration-backlog.md](./crypto-scalping-core-integration-backlog.md) | Backlog priorizado de acciones de integración |
| 13 | [package-001a-summary.md](./package-001a-summary.md) | Resumen del package: decisiones y entregables |
| 14 | [package-001a-review.md](./package-001a-review.md) | Auto-review: completitud y preguntas abiertas |

## Dependencias

- [Package 000 — Foundation](../package-000-foundation/README.md) — Definiciones base, glosario, portfolio model. [Hecho]
- [ADR-0001 — Jerarquía de Definición Terminológica](../../decisions/0001-terminology-hierarchy.md) — Reglas de terminología. [Hecho]
- [ADR-0002 — Consolidación de Taxonomía de Activos](../../decisions/0002-asset-taxonomy-consolidation.md) — Tipos y compartición de activos. [Hecho]
- [Architecture Baseline v1.0](../../architecture/architecture-baseline-v1.md) — Invariantes y centro arquitectónico. [Hecho]

## Restricciones

- Este package es exclusivamente documental. [Decisión] No produce código, APIs, ni infraestructura.
- No se recomienda ni se implementa trading en vivo. [Decisión]
- No se inventan datos sobre Crypto Scalping Core. [Decisión] Solo se usa evidencia confirmada del portfolio model.
- Gobernanza nivel SOLO: decisiones en 1 párrafo, sin escalación formal. [Decisión]

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 5        | 33%        |
| [Decisión]    | 10       | 67%        |
| [Hipótesis]   | 0        | 0%         |
| [Visión]      | 0        | 0%         |
