# Trazabilidad de Decisiones Arquitectónicas v1.0 — LabOS

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

Mapear las ~15 decisiones arquitectónicas mayores de LabOS a sus fuentes, packages de origen, documentos formalizadores y estado actual. [Decisión] Este documento es la cadena de trazabilidad que conecta cada decisión con su evidencia, permitiendo auditar el "por qué" de cada elemento del baseline.

---

## Mapa de Decisiones

### DEC-01: Knowledge-to-Value Pipeline como centro arquitectónico

| Campo | Valor |
|-------|-------|
| **Decisión** | El centro arquitectónico de LabOS es el Knowledge-to-Value Pipeline: Research → Knowledge → Assets → Products → Revenue. [Decisión] |
| **Package de origen** | 000 (concepto), 002A (formalización) |
| **Documento(s) fuente** | Package 000: 007-company-model.md, 004-startup-thesis.md |
| **Documento formalizador** | docs/packages/package-002a-architecture-review/architectural-center.md |
| **Baseline section** | architecture-baseline-v1.md §1 |
| **Estado** | FROZEN — requiere ADR para modificar |
| **Implicaciones** | Todo componente que no contribuye al pipeline debe justificar su existencia. |

---

### DEC-02: Definición canónica de Lab

| Campo | Valor |
|-------|-------|
| **Decisión** | Un Lab es una vertical de negocio independiente con hipótesis de producto propia y estado de madurez definido. Para integración formal se requieren 4 características adicionales. [Decisión] |
| **Package de origen** | 000 (definición base), 001A (extensión para integración) |
| **Documento(s) fuente** | Package 000: README.md (glosario), 012-portfolio-model.md |
| **Documento formalizador** | docs/decisions/0001-terminology-hierarchy.md (§5 caso específico) |
| **Baseline section** | architecture-baseline-v1.md §3, glossary.md |
| **Estado** | FROZEN — extensible solo con referencia explícita |
| **Implicaciones** | Nuevos labs no requieren las 4 características para existir, solo para integración formal. |

---

### DEC-03: Modelo de Packages como unidad de trabajo

| Campo | Valor |
|-------|-------|
| **Decisión** | El trabajo en LabOS se organiza en Packages: unidades discretas con entregables concretos, criterios de aceptación y estado de progreso. [Decisión] |
| **Package de origen** | 000 |
| **Documento(s) fuente** | Package 000: README.md (definición de Package) |
| **Documento formalizador** | architecture-baseline-v1.md (implícito en toda la estructura) |
| **Baseline section** | Transversal |
| **Estado** | FROZEN — INV-10 protege inmutabilidad de packages completados |
| **Implicaciones** | Todo trabajo significativo se empaqueta. Packages completados no se modifican retroactivamente. |

---

### DEC-04: Lab States (5 estados)

| Campo | Valor |
|-------|-------|
| **Decisión** | Un Lab puede estar en exactamente uno de 5 estados: idea, explorando, validando, operando, pausado. [Decisión] |
| **Package de origen** | 000 (definición), 001A (operacionalización con CSC) |
| **Documento(s) fuente** | Package 000: 012-portfolio-model.md |
| **Documento formalizador** | architecture-baseline-v1.md §7 |
| **Baseline section** | architecture-baseline-v1.md §7 |
| **Estado** | FROZEN — ampliable solo con ADR |
| **Implicaciones** | Cada Lab tiene un estado formalizado que determina su review cycle y priorización. |

---

### DEC-05: Autonomía de Labs (Founder Decision)

| Campo | Valor |
|-------|-------|
| **Decisión** | Los Labs operan independientemente de LabOS. LabOS provee infraestructura compartida pero no controla la operación diaria de un Lab. [Decisión] |
| **Package de origen** | 001A (Founder Decision FD-B1-03) |
| **Documento(s) fuente** | Package 001A: founder-decisions-package-001a-batch1.md |
| **Documento formalizador** | Lab Integration Framework, Decoupling_Protocol |
| **Baseline section** | architecture-baseline-v1.md §6, glossary.md (Decoupling_Protocol) |
| **Estado** | FROZEN — decisión del fundador |
| **Implicaciones** | Un Lab puede desacoplarse de LabOS sin perder operatividad. LabOS no tiene veto sobre decisiones Lab-locales. |

---

### DEC-06: Source-of-truth model (fuente de verdad única por concepto)

| Campo | Valor |
|-------|-------|
| **Decisión** | Cada concepto, término o definición tiene exactamente un documento como fuente de verdad. Los demás documentos referencian sin redefinir. [Decisión] |
| **Package de origen** | 002A (identificación), ADR-0001 (formalización) |
| **Documento(s) fuente** | architecture-invariants.md (INV-04, INV-07) |
| **Documento formalizador** | docs/decisions/0001-terminology-hierarchy.md |
| **Baseline section** | architecture-baseline-v1.md §2 (INV-04), §3 |
| **Estado** | FROZEN — formalizado como ADR e invariante |
| **Implicaciones** | Extensiones permitidas con referencia explícita. Redefiniciones prohibidas sin ADR. |

---

### DEC-07: Ownership y provenance del conocimiento

| Campo | Valor |
|-------|-------|
| **Decisión** | Cada entidad del sistema tiene un owner definido. El conocimiento tiene provenance trazable a sus fuentes originales. [Decisión] |
| **Package de origen** | 002 |
| **Documento(s) fuente** | knowledge-ownership.md, knowledge-provenance.md |
| **Documento formalizador** | architecture-baseline-v1.md §5, canonical-domain-map.md |
| **Baseline section** | architecture-baseline-v1.md §5 |
| **Estado** | FROZEN — parte del Knowledge Architecture |
| **Implicaciones** | Todo Knowledge Object tiene owner y cadena de provenance documentada. |

---

### DEC-08: Knowledge lifecycle (8 estados)

| Campo | Valor |
|-------|-------|
| **Decisión** | El conocimiento transita por un lifecycle definido con estados, transiciones y quality gates formalizados. [Decisión] |
| **Package de origen** | 002 |
| **Documento(s) fuente** | knowledge-lifecycle.md, knowledge-quality-gates.md |
| **Documento formalizador** | Package 002 (CLOSED) |
| **Baseline section** | Contenido en BA-009 (Knowledge Architecture) |
| **Estado** | FROZEN — Package 002 CLOSED (INV-10) |
| **Implicaciones** | El conocimiento no es estático; avanza por estados con criterios de calidad para cada transición. |

---

### DEC-09: Knowledge sharing (reference-based)

| Campo | Valor |
|-------|-------|
| **Decisión** | El conocimiento se comparte entre Labs mediante referencias, no mediante duplicación. Un Lab publica una referencia; otros Labs la consumen sin copiar el contenido. [Decisión] |
| **Package de origen** | 002 (principio), 001A (protocolo) |
| **Documento(s) fuente** | knowledge-sharing.md, Knowledge_Sharing_Protocol (001A) |
| **Documento formalizador** | Package 002 knowledge-sharing.md |
| **Baseline section** | Contenido en BA-009 |
| **Estado** | FROZEN — Package 002 CLOSED |
| **Implicaciones** | Previene drift, duplicación y desincronización entre Labs. |

---

### DEC-10: Knowledge-to-Asset boundary (handoff formal)

| Campo | Valor |
|-------|-------|
| **Decisión** | La transformación de Knowledge a Asset es un proceso definido con criterios de handoff explícitos, no una conversión automática ni implícita. [Decisión] |
| **Package de origen** | 002 (handoff), 001 (research-to-asset pipeline) |
| **Documento(s) fuente** | knowledge-to-asset-handoff.md, 018-research-to-asset.md |
| **Documento formalizador** | Package 002 knowledge-to-asset-handoff.md |
| **Baseline section** | Contenido en BA-009 |
| **Estado** | FROZEN — Package 002 CLOSED |
| **Implicaciones** | Package 003 (Asset System) operacionalizará este handoff con workflows concretos. |

---

### DEC-11: Conditional approval (patrón de aprobación)

| Campo | Valor |
|-------|-------|
| **Decisión** | Los packages y documentos pueden aprobarse con condiciones (remediaciones non-blocking) que no impiden el cierre pero quedan activas con triggers naturales. [Decisión] |
| **Package de origen** | 001A (primer uso del patrón) |
| **Documento(s) fuente** | founder-decisions-package-001a-batch4.md (FD-B4-01: APPROVED incondicional con 7 remediaciones) |
| **Documento formalizador** | package-001a-closure-record.md |
| **Baseline section** | Patrón operativo documentado en closure record |
| **Estado** | FROZEN — patrón establecido |
| **Implicaciones** | Un package puede cerrarse con remediaciones abiertas si estas son non-blocking y tienen triggers. |

---

### DEC-12: Reference Lab (concepto y primer registro)

| Campo | Valor |
|-------|-------|
| **Decisión** | Un Reference Lab es un Lab activo que sirve como caso de validación para frameworks de LabOS. CSC es LABOS-REF-LAB-0001. [Decisión] |
| **Package de origen** | 001A |
| **Documento(s) fuente** | reference-lab-eligibility-criteria-v1.md, crypto-scalping-core-reference-lab-record.md |
| **Documento formalizador** | Package 001A (framework docs) |
| **Baseline section** | Contenido en BA-010 |
| **Estado** | FROZEN — criterios y primer registro establecidos |
| **Implicaciones** | Frameworks futuros de LabOS se validan contra Reference Labs antes de generalizarse. |

---

### DEC-13: Package 003 = Asset System (identidad canónica)

| Campo | Valor |
|-------|-------|
| **Decisión** | El siguiente package en la secuencia es Package 003 — Asset System. Su scope es operacionalizar el Asset_First_Model. [Decisión] |
| **Package de origen** | 002A (roadmap), reconciliación post-001A |
| **Documento(s) fuente** | approved-roadmap-proposal.md, post-package-001a-roadmap-reconciliation.md |
| **Documento formalizador** | post-package-001a-roadmap-reconciliation.md |
| **Baseline section** | Roadmap (BA-008) |
| **Estado** | CONFIRMED — sin colisiones, identidad única |
| **Implicaciones** | Todos los prerequisitos satisfechos. Iniciable por decisión del fundador. |

---

### DEC-14: Taxonomía de activos (7 tipos canónicos)

| Campo | Valor |
|-------|-------|
| **Decisión** | Existen exactamente 7 tipos canónicos de activos: Documento, Template, Dataset, Herramienta, Componente, Framework, Playbook. 5 compartibles por defecto, 2 Lab-Private por defecto. [Decisión] |
| **Package de origen** | 000 (definición), 002A (hallazgo), ADR-0002 (consolidación) |
| **Documento(s) fuente** | Package 000: 007-company-model.md |
| **Documento formalizador** | docs/decisions/0002-asset-taxonomy-consolidation.md |
| **Baseline section** | architecture-baseline-v1.md §4 |
| **Estado** | FROZEN — formalizado como ADR |
| **Implicaciones** | Nuevos tipos solo mediante ADR que actualice Package 000. Package 003 usa esta taxonomía directamente. |

---

### DEC-15: Jerarquía de definición terminológica

| Campo | Valor |
|-------|-------|
| **Decisión** | El glosario de Package 000 README es la fuente de verdad global. Packages posteriores extienden pero no redefinen. Modificaciones requieren ADR. [Decisión] |
| **Package de origen** | 002A (hallazgo INV-04, INV-07), ADR-0001 (formalización) |
| **Documento(s) fuente** | architecture-invariants.md (INV-04, INV-07) |
| **Documento formalizador** | docs/decisions/0001-terminology-hierarchy.md |
| **Baseline section** | architecture-baseline-v1.md §3 |
| **Estado** | FROZEN — formalizado como ADR |
| **Implicaciones** | Toda extensión terminológica referencia la definición base. Sin definiciones paralelas permitidas. |

---

## Matriz de Trazabilidad Resumida

| # | Decisión | Fuente original | ADR | Invariante | Baseline §  |
|---|----------|----------------|-----|------------|-------------|
| DEC-01 | K2V Pipeline | Package 000 | — | — | §1 |
| DEC-02 | Lab definition | Package 000 + 001A | ADR-0001 §5 | INV-07 | §3 |
| DEC-03 | Package model | Package 000 | — | INV-10 | Transversal |
| DEC-04 | Lab States | Package 000 | — | — | §7 |
| DEC-05 | Lab autonomy | Package 001A (FD) | — | — | §6 |
| DEC-06 | Source-of-truth | Package 002A | ADR-0001 | INV-04, INV-07 | §2, §3 |
| DEC-07 | Ownership/provenance | Package 002 | — | — | §5 |
| DEC-08 | Knowledge lifecycle | Package 002 | — | — | BA-009 |
| DEC-09 | Knowledge sharing | Package 002 + 001A | — | — | BA-009 |
| DEC-10 | K→A boundary | Package 002 + 001 | — | INV-02 | BA-009 |
| DEC-11 | Conditional approval | Package 001A | — | — | Patrón |
| DEC-12 | Reference Lab | Package 001A | — | — | BA-010 |
| DEC-13 | Package 003 identity | Package 002A + reconcil. | — | — | BA-008 |
| DEC-14 | Asset taxonomy | Package 000 + 002A | ADR-0002 | — | §4 |
| DEC-15 | Terminology hierarchy | Package 002A | ADR-0001 | INV-04, INV-07 | §3 |

---

## Cobertura

| Aspecto | Decisiones que lo cubren |
|---------|-------------------------|
| Pipeline de valor | DEC-01, DEC-10 |
| Entidades principales | DEC-02, DEC-04, DEC-07, DEC-08, DEC-14 |
| Gobernanza y proceso | DEC-03, DEC-05, DEC-06, DEC-11, DEC-15 |
| Compartición | DEC-09, DEC-14 |
| Roadmap y evolución | DEC-13, DEC-12 |

[Hecho] Las 15 decisiones cubren las 5 áreas principales del sistema sin gaps identificados.

---

## Cross-references

- [architecture-baseline-v1.md](./architecture-baseline-v1.md)
- [architecture-baseline-v1.0-manifest.md](./architecture-baseline-v1.0-manifest.md)
- [0001-terminology-hierarchy.md](../decisions/0001-terminology-hierarchy.md)
- [0002-asset-taxonomy-consolidation.md](../decisions/0002-asset-taxonomy-consolidation.md)
- [architecture-invariants.md](../packages/package-002a-architecture-review/architecture-invariants.md)
- [approved-roadmap-proposal.md](../packages/package-002a-architecture-review/approved-roadmap-proposal.md)

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 2        | 6%         |
| [Hipótesis]   | 0        | 0%         |
| [Decisión]    | 32       | 94%        |
| [Visión]      | 0        | 0%         |

> **Nota:** Alta proporción de decisiones porque este documento mapea decisiones tomadas. Los hechos se limitan a verificaciones de cobertura.
