# ADR-0002: Consolidación de Taxonomía de Activos

## Metadata

| Campo | Valor |
|-------|-------|
| **ADR ID** | ADR-0002 |
| **Título** | Consolidación de Taxonomía de Activos |
| **Estado** | Accepted |
| **Fecha** | 2025-07-22 |
| **Prioridad** | P0 |
| **Autor** | Fundador |
| **Depende de** | ADR-0001 |

---

## Contexto

Package 000 (007-company-model.md) define una taxonomía de 7 tipos de activos: documento, template, dataset, herramienta, componente, framework, playbook. [Hecho] Esta taxonomía clasifica TODOS los activos producibles dentro del Asset_First_Model.

Package 001A (Requirement 7 — Asset Sharing Protocol) define 5 tipos para activos compartibles: templates, frameworks, tools, datasets, documentation. [Hecho] Estos nombres están en inglés, sin mapping explícito a la taxonomía canónica de Package 000.

Las dos listas no son idénticas ni se referencian mutuamente. [Hecho] La revisión arquitectónica identificó este problema como hallazgo T-02 (severidad Alta) en la architecture-decision-matrix.md.

---

## Declaración del Problema

Dos listas incompatibles de tipos de activos existen sin relación explícita entre ellas. [Hecho] Esto genera:

1. Confusión sobre si las 5 categorías de Package 001A son los mismos conceptos que los 7 tipos de Package 000 o categorías nuevas. [Hecho]
2. Inconsistencia idiomática: Package 000 usa nombres en español (canónicos), Package 001A usa nombres en inglés sin equivalencia declarada. [Hecho]
3. Ambigüedad sobre dónde encajan `componente` y `playbook` en el esquema de compartición. [Hecho]

---

## Decisión

Se establece la siguiente consolidación taxonómica: [Decisión]

### 1. Taxonomía canónica

La taxonomía de 7 tipos definida en Package 000 (007-company-model.md) es la FUENTE DE VERDAD ÚNICA para clasificación de activos. [Decisión]

| # | Tipo canónico | Descripción |
|---|---------------|-------------|
| 1 | **Documento** | Registro estructurado de conocimiento, análisis o decisiones. [Hecho] |
| 2 | **Template** | Plantilla reutilizable con estructura predefinida. [Hecho] |
| 3 | **Dataset** | Conjunto de datos organizados y documentados. [Hecho] |
| 4 | **Herramienta** | Software, script o utilidad ejecutable. [Hecho] |
| 5 | **Componente** | Módulo técnico aislado y reutilizable. [Hecho] |
| 6 | **Framework** | Estructura conceptual o técnica para organizar múltiples componentes. [Hecho] |
| 7 | **Playbook** | Guía operativa paso a paso para ejecución repetible. [Hecho] |

### 2. Subconjunto compartible

Los 5 tipos de Package 001A son un SUBCONJUNTO de la taxonomía canónica, no una taxonomía paralela. [Decisión] El mapping explícito es:

| Package 001A (inglés) | Tipo canónico (español) | Compartible por defecto |
|-----------------------|------------------------|------------------------|
| templates | Template | ✅ Sí |
| frameworks | Framework | ✅ Sí |
| tools | Herramienta | ✅ Sí |
| datasets | Dataset | ✅ Sí |
| documentation | Documento | ✅ Sí |

### 3. Tipos no compartibles por defecto

Los 2 tipos NO incluidos en el subconjunto compartible de Package 001A: [Decisión]

| Tipo canónico | Compartible por defecto | Razón |
|---------------|------------------------|-------|
| **Componente** | ❌ No — Lab-Private por defecto | Demasiado específico del contexto técnico del lab de origen. Requiere adaptación significativa para ser útil en otro lab. [Decisión] |
| **Playbook** | ❌ No — Lab-Private por defecto | Demasiado específico del proceso operativo del lab de origen. Los pasos son dependientes del dominio. [Decisión] |

### 4. Excepción de compartición

Un componente o playbook PUEDE ser compartido si el Lab de origen lo publica explícitamente mediante el Asset_Sharing_Protocol. [Decisión] La no-compartición es el DEFAULT, no una prohibición absoluta.

### 5. Nomenclatura

Todas las referencias futuras a tipos de activos DEBEN usar los nombres canónicos en español de Package 000. [Decisión] Los equivalentes en inglés pueden aparecer entre paréntesis para contexto internacional, pero el nombre canónico gobierna.

Ejemplo correcto: "herramienta (tool)"
Ejemplo incorrecto: "tool" sin referencia al nombre canónico.

---

## Alternativas Consideradas

### (a) Adoptar la taxonomía de 5 tipos de Package 001A como canónica

**Rechazada.** [Decisión] La taxonomía de Package 001A es menos completa (5 vs 7 tipos), excluye componente y playbook sin justificación explícita, y usa nomenclatura en inglés que rompe la convención idiomática del proyecto.

### (b) Crear una taxonomía nueva unificada con nombres diferentes

**Rechazada.** [Decisión] La taxonomía de Package 000 ya está bien definida, con descripciones claras y criterios de activo establecidos. No hay evidencia de que los 7 tipos sean insuficientes o mal nombrados.

### (c) Mantener ambas taxonomías como "vistas diferentes"

**Rechazada.** [Decisión] Perpetúa la confusión. "Vista diferente" es eufemismo para "inconsistencia tolerada". Viola INV-04 (fuente de verdad única por concepto).

---

## Consecuencias

### Positivas

- Una sola taxonomía elimina ambigüedad sobre clasificación de activos. [Hecho]
- El mapping explícito resuelve la confusión idiomática español/inglés. [Hecho]
- Componente y playbook ganan reglas explícitas de compartición que antes no existían. [Hecho]

### Negativas

- Package 001A necesitará referenciar este mapping cuando se ejecute. [Hecho]
- Los nombres canónicos en español pueden generar fricción en documentación técnica con audiencia internacional. [Hipótesis]

### Neutras

- La taxonomía de 7 tipos se mantiene sin cambios respecto a Package 000. [Hecho]
- Los 5 tipos compartibles de Package 001A siguen siendo los mismos — solo se formaliza su relación con la taxonomía base. [Hecho]

---

## Trade-offs

**Exhaustividad vs Simplicidad.** La taxonomía de 7 tipos puede percibirse como pesada para activos pequeños (¿es un script de 20 líneas una "herramienta" o un "componente"?). Sin embargo, tener categorías claras previene miscategorización y facilita la búsqueda y reutilización. [Decisión]

El criterio de decisión entre herramienta y componente: si opera de forma autónoma es herramienta; si requiere un sistema mayor para funcionar es componente. [Decisión]

---

## Impacto de Migración

- **Package 001A (al ejecutarse):** El Asset_Sharing_Protocol debe referenciar este ADR y usar los nombres canónicos en español con el mapping aquí definido. El shared asset index usará los tipos canónicos. [Decisión]
- **Operación inmediata:** El glosario canónico (`docs/architecture/glossary.md`) incluirá esta taxonomía como referencia. [Decisión]
- **Catalogación de activos existentes:** Los activos actualmente en `assets/` deben clasificarse usando los 7 tipos canónicos. [Decisión]

---

## Implicaciones Futuras

- **Package 003 (Asset System):** Usará esta taxonomía canónica directamente como base para workflows de creación, validación y publicación. [Hipótesis]
- **Nuevos tipos de activos:** Solo pueden agregarse mediante ADR que actualice Package 000 (007-company-model.md). No se permiten tipos ad-hoc en packages individuales. [Decisión]
- **Automatización futura:** El shared asset index (cuando se implemente) usará los tipos canónicos como categorías de filtrado. [Visión]

---

## Referencias

- [Package 000 — 007-company-model.md (taxonomía de activos)](../packages/package-000-foundation/007-company-model.md) [Hecho]
- [Package 001A requirements.md — Requirement 7](../../.kiro/specs/package-001a-first-lab-integration/requirements.md) [Hecho]
- [architecture-decision-matrix.md — Hallazgo T-02](../packages/package-002a-architecture-review/architecture-decision-matrix.md) [Hecho]
- [remediation-backlog.md — REM-02](../packages/package-002a-architecture-review/remediation-backlog.md) [Hecho]
- [ADR-0001 — Jerarquía de Definición Terminológica](./0001-terminology-hierarchy.md) [Hecho]

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 20       | 40%        |
| [Hipótesis]   | 2        | 4%         |
| [Decisión]    | 27       | 54%        |
| [Visión]      | 1        | 2%         |
