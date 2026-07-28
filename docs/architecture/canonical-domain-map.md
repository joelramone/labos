# Mapa Canónico de Dominio — LabOS

## Propósito

Este documento cataloga todas las entidades canónicas del ecosistema LabOS, su propiedad, ciclo de vida, relaciones y estado de definición formal. [Hecho] Es la referencia autoritativa para entender cómo se conectan los conceptos del sistema.

---

## Catálogo de Entidades

### Entidades Formalmente Definidas

#### 1. Lab

| Campo | Valor |
|-------|-------|
| **Owner** | Fundador (decisión de creación); Lab owner (operación) |
| **Fuente** | Package 000 README (glosario) + 012-portfolio-model.md |
| **Estados del ciclo de vida** | idea → explorando → validando → operando + pausado |
| **Relaciones** | produce → Asset, produce → Knowledge (pendiente), tiene → Lab_State, opera bajo → Lab_Contract |
| **Extensiones** | Package 001A agrega 4 características para integración formal |
| **Epistémico** | [Hecho] |

#### 2. Asset (Activo)

| Campo | Valor |
|-------|-------|
| **Owner** | Lab de origen (creación); LabOS o Lab (según clasificación de boundary) |
| **Fuente** | Package 000 — 007-company-model.md |
| **Tipos** | documento, template, dataset, herramienta, componente, framework, playbook (7 canónicos) |
| **Estados del ciclo de vida** | borrador → validado → productizado |
| **Relaciones** | tiene → Tipo (1 de 7), tiene → Estado, pertenece a → Lab, puede ser compartido vía → Asset_Sharing_Protocol |
| **Shareability** | 5 tipos compartibles por defecto, 2 Lab-Private por defecto (ADR-0002) |
| **Epistémico** | [Hecho] |

#### 3. Research (Investigación)

| Campo | Valor |
|-------|-------|
| **Owner** | Lab que ejecuta la investigación |
| **Fuente** | Package 001 — Research Methodology (26 documentos) |
| **Categorías** | Small (<4h), Medium (4-16h), Large (>16h) |
| **Estados del ciclo de vida** | iniciada → en progreso → concluida (+ nota de cierre si sin activo) |
| **Relaciones** | produce → Asset (vía Asset_First_Model), produce → Knowledge (pendiente), ejecutada por → Lab |
| **Invariante** | INV-02: toda investigación >4h produce al menos 1 activo o nota de cierre |
| **Epistémico** | [Hecho] |

#### 4. Package

| Campo | Valor |
|-------|-------|
| **Owner** | LabOS (infraestructura transversal) |
| **Fuente** | Package 000 README (glosario) |
| **Tipos** | Fundacional, Implementación, Meta, Dormido |
| **Estados del ciclo de vida** | pendiente → en progreso → completo (+ revisión formal) |
| **Relaciones** | contiene → documentos, depende de → otros packages, produce → decisiones |
| **Invariante** | INV-10: packages completados no se modifican retroactivamente sin ADR |
| **Epistémico** | [Hecho] |

#### 5. Revenue_Thesis

| Campo | Valor |
|-------|-------|
| **Owner** | Lab que propone la tesis |
| **Fuente** | Package 000 README (glosario) + 009-revenue-thesis.md |
| **Estados del ciclo de vida** | hipótesis → en validación → validada (con transacción real) / invalidada |
| **Relaciones** | pertenece a → Lab, requiere → Asset (validado), genera → Revenue |
| **Invariante** | INV-03: no invertir >1 semana sin hipótesis de monetización |
| **Epistémico** | [Hecho] |

#### 6. Lab_Contract

| Campo | Valor |
|-------|-------|
| **Owner** | LabOS (template); Lab (instancia) |
| **Fuente** | Package 001A — Requirement 2 |
| **Secciones** | 15 secciones definidas |
| **Estados del ciclo de vida** | borrador → activo → en revisión → actualizado |
| **Relaciones** | vincula → Lab con LabOS, define → Lab_Boundary, establece → Review_Cycle |
| **Nivel activo** | SOLO — completo como template, sin revisión formal obligatoria hasta trigger de gobernanza |
| **Epistémico** | [Decisión] |

#### 7. Lab_State

| Campo | Valor |
|-------|-------|
| **Owner** | LabOS (definición); Fundador (asignación) |
| **Fuente** | Package 000 — 012-portfolio-model.md |
| **Valores** | idea, explorando, validando, operando, pausado |
| **Relaciones** | asignado a → Lab, determina → Review_Cycle cadencia |
| **Nota** | Único sistema de clasificación activo. Maturity_Model dormido hasta trigger. |
| **Epistémico** | [Hecho] |

---

### Entidades Pendientes de Definición Formal

#### 8. Knowledge (Conocimiento)

| Campo | Valor |
|-------|-------|
| **Owner** | Pendiente — probablemente Lab de origen |
| **Fuente** | Pendiente — Package 002 (Knowledge Architecture) |
| **Estados del ciclo de vida** | Por definir |
| **Relaciones esperadas** | producido por → Research, producido por → Lab, transforma en → Asset |
| **Estado de definición** | ⚠️ PENDIENTE — existe como concepto implícito en el pipeline pero no tiene definición formal |
| **Epistémico** | [Hipótesis] |

#### 9. Product (Producto)

| Campo | Valor |
|-------|-------|
| **Owner** | Pendiente — probablemente Lab que lo produce |
| **Fuente** | Pendiente — Package 004 (Product Factory) |
| **Estados del ciclo de vida** | Por definir (probable: concepto → prototipo → MVP → producto) |
| **Relaciones esperadas** | creado desde → Asset (productizado), genera → Revenue, validado por → Revenue_Thesis |
| **Estado de definición** | ⚠️ PENDIENTE — Package 004 dormido hasta ≥3 activos validados |
| **Epistémico** | [Hipótesis] |

#### 10. Capability (Capacidad)

| Campo | Valor |
|-------|-------|
| **Owner** | Pendiente |
| **Fuente** | Pendiente — condicional |
| **Relaciones esperadas** | poseída por → Lab, compuesta de → Assets, ofrecida al → ecosistema |
| **Estado de definición** | ⚠️ PENDIENTE — abstracción prematura para la etapa actual. Se activa cuando ≥3 labs estén activos con reutilización real entre ellos. |
| **Epistémico** | [Visión] |

---

## Tipos de Relación

| Tipo de relación | Significado | Ejemplo |
|-----------------|-------------|---------|
| **produce** | La entidad A genera la entidad B como output | Lab produce Asset |
| **consume** | La entidad A utiliza la entidad B como input | Lab consume Shared_Service |
| **contiene** | La entidad A incluye la entidad B como parte | Package contiene documentos |
| **extiende** | La entidad A agrega características a B sin modificar su base | Package 001A extiende definición de Lab |
| **depende de** | La entidad A requiere la entidad B para funcionar | Package depende de otro Package |
| **vincula** | La entidad A establece una relación formal con B | Lab_Contract vincula Lab con LabOS |
| **transforma en** | La entidad A se convierte en B mediante un proceso | Knowledge transforma en Asset |
| **asignado a** | La entidad A se asigna como propiedad/estado de B | Lab_State asignado a Lab |

---

## Diagrama de Relaciones

```text
┌─────────────────────────────────────────────────────────────────────┐
│                    KNOWLEDGE-TO-VALUE PIPELINE                        │
│                                                                      │
│                                                                      │
│  ┌──────────┐  produce   ┌───────────┐  transforma  ┌──────────┐  │
│  │ Research │───────────▶│ Knowledge │─────────────▶│  Asset   │  │
│  │          │            │ (pending) │              │ (7 tipos)│  │
│  └────┬─────┘            └───────────┘              └────┬─────┘  │
│       │                                                   │        │
│       │ produce (directo,                                 │        │
│       │ etapa actual)                                     │        │
│       └──────────────────────────────────────────────────▶│        │
│                                                           │        │
│                                          productiza       ▼        │
│                                                   ┌──────────┐     │
│                                                   │ Product  │     │
│                                                   │ (pending)│     │
│                                                   └────┬─────┘     │
│                                                        │           │
│                                            genera      ▼           │
│                                                   ┌──────────┐     │
│                                                   │ Revenue  │     │
│                                                   │          │     │
│                                                   └──────────┘     │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘

        ENTIDADES DE SOPORTE:

┌─────────┐  opera bajo  ┌──────────────┐
│   Lab   │─────────────▶│ Lab_Contract │
│         │              └──────────────┘
│         │  tiene        ┌──────────────┐
│         │─────────────▶│  Lab_State   │
│         │              └──────────────┘
│         │  ejecuta      ┌──────────────┐
│         │─────────────▶│  Research    │
│         │              └──────────────┘
│         │  produce      ┌──────────────┐
│         │─────────────▶│   Asset      │
└─────────┘              └──────────────┘

┌─────────┐  contiene     ┌──────────────┐
│ Package │─────────────▶│  Documentos  │
│         │              └──────────────┘
│         │  depende de   ┌──────────────┐
│         │─────────────▶│  Package(s)  │
└─────────┘              └──────────────┘

┌─────────────────┐  requiere   ┌──────────────┐
│ Revenue_Thesis  │────────────▶│ Asset (valid)│
│                 │             └──────────────┘
│                 │  pertenece a ┌──────────────┐
│                 │────────────▶│     Lab      │
└─────────────────┘             └──────────────┘
```

---

## Resumen de Estado de Definición

| Entidad | Formalmente definida | Package fuente | Operativa hoy |
|---------|---------------------|---------------|---------------|
| Lab | ✅ Sí | 000, 001A | ✅ Sí |
| Asset | ✅ Sí | 000 | ✅ Sí |
| Research | ✅ Sí | 001 | ✅ Sí |
| Package | ✅ Sí | 000 | ✅ Sí |
| Revenue_Thesis | ✅ Sí | 000 | ✅ Sí |
| Lab_Contract | ✅ Sí | 001A | ⚠️ Pendiente ejecución |
| Lab_State | ✅ Sí | 000 | ✅ Sí |
| Knowledge | ❌ No | 002 (pendiente) | ❌ No |
| Product | ❌ No | 004 (dormido) | ❌ No |
| Capability | ❌ No | Condicional | ❌ No |

---

## Cross-references

- [glossary.md — Glosario canónico](./glossary.md)
- [relationships.md — Relaciones detalladas](./relationships.md)
- [architecture-baseline-v1.md — Baseline congelado](./architecture-baseline-v1.md)
- [Package 000 — 007-company-model.md](../packages/package-000-foundation/007-company-model.md)
- [Package 000 — 012-portfolio-model.md](../packages/package-000-foundation/012-portfolio-model.md)

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 12       | 52%        |
| [Hipótesis]   | 3        | 13%        |
| [Decisión]    | 7        | 30%        |
| [Visión]      | 1        | 4%         |
