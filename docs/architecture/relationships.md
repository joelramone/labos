# Relaciones entre Entidades — LabOS

## Propósito

Este documento explicita todas las relaciones formales entre las entidades canónicas del ecosistema LabOS. [Hecho] Cada relación incluye: entidades involucradas, tipo de relación, cardinalidad, condiciones y referencia a la fuente que la define.

---

## Relaciones del Lab

### Lab → Asset (produce)

| Campo | Valor |
|-------|-------|
| **Tipo** | produce |
| **Cardinalidad** | 1 Lab produce 0..N Assets |
| **Condición** | Via Asset_First_Model: toda investigación >4h produce ≥1 activo. [Hecho] |
| **Mecanismo** | Research → conclusión → artefacto reutilizable documentado. |
| **Fuente** | Package 000 — 007-company-model.md |
| **Epistémico** | [Hecho] |

### Lab → Knowledge (produce)

| Campo | Valor |
|-------|-------|
| **Tipo** | produce |
| **Cardinalidad** | 1 Lab produce 0..N Knowledge entities |
| **Condición** | Pendiente definición formal de "Knowledge" como entidad. [Hipótesis] |
| **Estado** | ⚠️ Relación implícita — se formalizará con Package 002. |
| **Fuente** | Architectural-center.md (pipeline) |
| **Epistémico** | [Hipótesis] |

### Lab → Lab_State (tiene)

| Campo | Valor |
|-------|-------|
| **Tipo** | tiene (estado actual) |
| **Cardinalidad** | 1 Lab tiene exactamente 1 Lab_State en cualquier momento |
| **Valores posibles** | idea → explorando → validando → operando + pausado |
| **Transiciones** | idea→explorando (cuando inicia actividad), explorando→validando (cuando existe hipótesis de monetización activa), validando→operando (cuando existe revenue real), cualquier estado→pausado (decisión del fundador). [Hecho] |
| **Fuente** | Package 000 — 012-portfolio-model.md |
| **Epistémico** | [Hecho] |

### Lab → Lab_Contract (opera bajo)

| Campo | Valor |
|-------|-------|
| **Tipo** | opera bajo |
| **Cardinalidad** | 1 Lab tiene 0..1 Lab_Contract (0 si no está formalmente integrado) |
| **Condición** | Solo labs que completan el Integration_Lifecycle tienen contrato activo. [Decisión] |
| **Nivel actual** | SOLO — contrato completo (15 secciones) como referencia, sin revisión formal obligatoria. [Decisión] |
| **Fuente** | Package 001A — Requirement 2 |
| **Epistémico** | [Decisión] |

### Lab → Revenue_Thesis (tiene)

| Campo | Valor |
|-------|-------|
| **Tipo** | tiene |
| **Cardinalidad** | 1 Lab tiene 0..N Revenue_Thesis |
| **Condición** | Requerida antes de inversión >1 semana (INV-03). [Decisión] |
| **Fuente** | Package 000 — 009-revenue-thesis.md |
| **Epistémico** | [Hecho] |

---

## Relaciones del Research

### Research → Asset (produce)

| Campo | Valor |
|-------|-------|
| **Tipo** | produce |
| **Cardinalidad** | 1 Research produce 1..N Assets (o 1 nota de cierre) |
| **Condición** | Via Asset_First_Model. Aplica a investigaciones >4h acumuladas. [Hecho] |
| **Excepcción** | Si no se produce activo, se requiere nota de cierre (máximo 5 oraciones). [Hecho] |
| **Fuente** | Package 000 — 007-company-model.md, Package 001 — Principio 7 |
| **Epistémico** | [Hecho] |

### Research → Knowledge (produce)

| Campo | Valor |
|-------|-------|
| **Tipo** | produce |
| **Cardinalidad** | 1 Research produce 0..N Knowledge entities |
| **Condición** | Pendiente formalización. Toda investigación genera conocimiento implícitamente; la formalización como entidad catalogable es responsabilidad de Package 002. [Hipótesis] |
| **Fuente** | Architectural-center.md (pipeline) |
| **Epistémico** | [Hipótesis] |

---

## Relaciones del Asset

### Asset → Tipo (tiene)

| Campo | Valor |
|-------|-------|
| **Tipo** | tiene (clasificación) |
| **Cardinalidad** | 1 Asset tiene exactamente 1 Tipo |
| **Valores posibles** | documento, template, dataset, herramienta, componente, framework, playbook |
| **Fuente** | Package 000 — 007-company-model.md, ADR-0002 |
| **Epistémico** | [Hecho] |

### Asset → Estado (tiene)

| Campo | Valor |
|-------|-------|
| **Tipo** | tiene (ciclo de vida) |
| **Cardinalidad** | 1 Asset tiene exactamente 1 Estado en cualquier momento |
| **Valores posibles** | borrador → validado → productizado |
| **Transiciones** | borrador→validado (revisión completada + 5 campos mínimos cumplidos), validado→productizado (evidencia de uso real documentada). No existe borrador→productizado directo. [Hecho] |
| **Fuente** | Package 000 — 007-company-model.md |
| **Epistémico** | [Hecho] |

### Asset → Compartición (puede ser compartido)

| Campo | Valor |
|-------|-------|
| **Tipo** | puede ser compartido |
| **Condición** | 5 de 7 tipos son compartibles por defecto: documento, template, dataset, herramienta, framework. [Decisión] |
| **Excepción** | Componente y playbook son Lab-Private por defecto; pueden compartirse si el Lab los publica explícitamente. [Decisión] |
| **Mecanismo** | Asset_Sharing_Protocol (Package 001A — Requirement 7) |
| **Fuente** | ADR-0002 |
| **Epistémico** | [Decisión] |

### Asset → Lab (pertenece a)

| Campo | Valor |
|-------|-------|
| **Tipo** | pertenece a |
| **Cardinalidad** | 1 Asset pertenece a exactamente 1 Lab (origen) |
| **Nota** | Un asset compartido sigue perteneciendo al Lab de origen; otros Labs solo lo referencian, no lo copian. [Decisión] |
| **Fuente** | Package 001A — Lab_Boundary, Knowledge_Sharing_Protocol |
| **Epistémico** | [Decisión] |

---

## Relaciones del Package

### Package → Documentos (contiene)

| Campo | Valor |
|-------|-------|
| **Tipo** | contiene |
| **Cardinalidad** | 1 Package contiene 1..N documentos |
| **Condición** | Cada documento tiene un propósito único. Un documento = un propósito. [Hecho] |
| **Fuente** | Documentation Standards (steering) |
| **Epistémico** | [Hecho] |

### Package → Package (depende de)

| Campo | Valor |
|-------|-------|
| **Tipo** | depende de |
| **Cardinalidad** | 1 Package depende de 0..N otros Packages |
| **Dependencias conocidas** | 001A depende de 000; 002 depende de 000; 003 depende de 000, 001A, 002; 004-009 dormidos con triggers de activación. [Hecho] |
| **Invariante** | INV-10: packages completados no se modifican sin ADR. [Decisión] |
| **Fuente** | Package 002A — approved-roadmap-proposal.md |
| **Epistémico** | [Hecho] |

---

## Pipeline de Valor (flujo completo)

```text
Research → Knowledge → Assets → Products → Revenue
   │           │          │          │          │
   │           │          │          │          └── Transacción real documentada
   │           │          │          └── Asset productizado con usuarios
   │           │          └── Artefacto reutilizable (7 tipos)
   │           └── Entidad de conocimiento (pending Package 002)
   └── Actividad exploratoria ≥4h
```

### Etapas del Pipeline

| Etapa | Entrada | Salida | Package responsable | Estado |
|-------|---------|--------|--------------------| --------|
| Research | Pregunta/hipótesis | Conclusiones + evidencia | Package 001 | ✅ Operativo |
| Knowledge | Conclusiones de research | Conocimiento catalogado | Package 002 | ⚠️ Pendiente |
| Assets | Conocimiento/research | Artefactos reutilizables (7 tipos) | Package 000 + 003 | ✅ Definido / ⚠️ Operacionalización pendiente |
| Products | Assets validados | Producto vendible | Package 004 | 💤 Dormido |
| Revenue | Producto en mercado | Ingreso recurrente | Package 005 | 💤 Dormido |

### Nota sobre etapa actual

En la etapa actual (pre-revenue, pre-product), el pipeline opera en modo directo: Research → Assets. [Hecho] Las etapas Knowledge y Products se formalizarán cuando sus packages respectivos se ejecuten. El pipeline no se bloquea por la ausencia de etapas intermedias formalizadas. [Decisión]

---

## Reglas de Integridad

1. Todo Asset DEBE tener exactamente 1 Lab propietario. [Decisión]
2. Todo Asset DEBE tener exactamente 1 Tipo de los 7 canónicos. [Decisión]
3. Todo Asset DEBE tener exactamente 1 Estado de los 3 posibles. [Decisión]
4. Todo Lab DEBE tener exactamente 1 Lab_State. [Decisión]
5. Toda Research >4h DEBE producir ≥1 Asset O 1 nota de cierre (INV-02). [Hecho]
6. Todo Lab con inversión >1 semana DEBE tener Revenue_Thesis documentada (INV-03). [Decisión]
7. Ningún concepto tiene más de 1 fuente de verdad (INV-04). [Decisión]

---

## Cross-references

- [canonical-domain-map.md — Catálogo de entidades](./canonical-domain-map.md)
- [glossary.md — Definiciones canónicas](./glossary.md)
- [ADR-0001 — Jerarquía terminológica](../decisions/0001-terminology-hierarchy.md)
- [ADR-0002 — Taxonomía de activos](../decisions/0002-asset-taxonomy-consolidation.md)
- [architectural-center.md — Pipeline de valor](../packages/package-002a-architecture-review/architectural-center.md)
- [Package 000 — 007-company-model.md](../packages/package-000-foundation/007-company-model.md)
- [Package 000 — 012-portfolio-model.md](../packages/package-000-foundation/012-portfolio-model.md)

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 16       | 43%        |
| [Hipótesis]   | 3        | 8%         |
| [Decisión]    | 18       | 49%        |
| [Visión]      | 0        | 0%         |
