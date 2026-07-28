# Glosario Canónico — LabOS

## Propósito

Este documento consolida TODOS los términos de dominio de LabOS con su definición canónica, fuente de origen y extensiones aplicables. [Hecho] Es el punto de navegación único para terminología del ecosistema.

Las definiciones base provienen del glosario de Package 000 README.md. [Hecho] Las extensiones provienen de packages posteriores y están marcadas explícitamente como tales, respetando la jerarquía establecida en [ADR-0001](../decisions/0001-terminology-hierarchy.md). [Decisión]

---

## Reglas de Uso

1. El glosario de Package 000 README.md es la fuente de verdad terminológica global. [Decisión]
2. Este documento es un ÍNDICE DE NAVEGACIÓN, no un reemplazo de la fuente. [Decisión]
3. Los packages pueden EXTENDER definiciones (agregar características) pero no REDEFINIRLAS (cambiar significado base). [Decisión]
4. Toda extensión referencia explícitamente la definición base. [Decisión]
5. Modificar una definición base requiere un ADR que actualice Package 000. [Decisión]

Referencia: [ADR-0001 — Jerarquía de Definición Terminológica](../decisions/0001-terminology-hierarchy.md)

---

## Términos Canónicos

### Términos base (Package 000)

| # | Término | Definición canónica | Fuente | Extensiones | Epistémico |
|---|---------|--------------------|--------|-------------|------------|
| 1 | **Package** | Unidad discreta de trabajo con entregables concretos y criterios de aceptación. Cada package tiene un conjunto definido de documentos y un estado de progreso. | Package 000 README | — | [Hecho] |
| 2 | **LabOS** | Sistema operativo documental y metodológico para empresas de conocimiento asistidas por IA. Transforma investigación en activos reutilizables y líneas de negocio. | Package 000 README | Package 001A extiende: "sistema transversal que provee infraestructura operativa, steering, blueprints y automatizaciones compartidas al portafolio de Labs." | [Hecho] |
| 3 | **Lab** | Vertical de negocio independiente dentro del portafolio LabOS, con hipótesis de producto propia y estado de madurez definido. | Package 000 README | Package 001A extiende para INTEGRACIÓN FORMAL: requiere 4 características adicionales (independencia de dominio, preservación de identidad, autonomía operacional, voluntad de integración). Ver ADR-0001 §5. | [Hecho] |
| 4 | **Activo** | Artefacto reutilizable producido por investigación o trabajo: documento, template, dataset, herramienta, componente, framework o playbook. | Package 000 README | ADR-0002 establece: 7 tipos canónicos, 5 compartibles por defecto, 2 Lab-Private por defecto. | [Hecho] |
| 5 | **Hipótesis** | Suposición explícita que requiere validación con evidencia antes de tratarse como hecho. Se etiqueta `[Hipótesis]` en documentos. | Package 000 README | — | [Hecho] |
| 6 | **Hecho** | Información verificada o verificable contra una fuente observable. Se etiqueta `[Hecho]` en documentos. | Package 000 README | — | [Hecho] |
| 7 | **Visión** | Aspiración a largo plazo, no comprometida ni garantizada. Se etiqueta `[Visión]` en documentos. | Package 000 README | — | [Hecho] |
| 8 | **Asset_First_Model** | Enfoque donde toda investigación (>4h acumuladas) produce al menos un activo reutilizable documentado antes de considerar productización. | Package 000 README | Package 001 refuerza: Principio 7 del research methodology. | [Hecho] |
| 9 | **Revenue_Thesis** | Modelo documentado que describe cómo y por qué se espera generar ingresos, clasificado como hipótesis hasta que exista transacción real. | Package 000 README | — | [Hecho] |
| 10 | **Portfolio_Model** | Estructura organizativa donde múltiples labs operan bajo infraestructura compartida de LabOS con reglas de priorización definidas. | Package 000 README | — | [Hecho] |
| 11 | **Clasificación_Epistémica** | Sistema de etiquetado que diferencia hechos, hipótesis, visiones y decisiones en cada documento del package. | Package 000 README | Package 002A formaliza como INV-01 (invariante arquitectónica). | [Hecho] |
| 12 | **Package_Foundation** | Package 000: conjunto de 16 documentos que constituyen la definición fundacional de LabOS. | Package 000 README | — | [Hecho] |
| 13 | **Fundador** | Persona que opera LabOS en esta etapa inicial; único stakeholder con capacidad de decisión y ejecución. | Package 000 README | — | [Hecho] |

### Términos extendidos (Package 001A — marcados como extensiones)

| # | Término | Definición (extensión) | Fuente | Relación con base | Epistémico |
|---|---------|----------------------|--------|-------------------|------------|
| 14 | **Lab_Contract** | Documento formal que establece la relación entre un Lab y LabOS, definiendo misión, alcance, entradas, salidas, recursos compartidos, privados, dependencias, quality gates y ciclo de revisión. 15 secciones. | Package 001A | Extiende: mecanismo formal de integración para Labs (base: "Lab" en Package 000). | [Decisión] |
| 15 | **Integration_Lifecycle** | Secuencia de etapas para incorporar un proyecto al ecosistema LabOS: Identification → Assessment → Contract Creation → Onboarding → Operation → Review. | Package 001A | Nuevo concepto — proceso de integración. | [Decisión] |
| 16 | **Lab_Boundary** | Delimitación explícita de lo que pertenece al Lab (privado) vs lo que pertenece a LabOS (compartido). 4 clasificaciones: Lab-Private, LabOS-Shared, Lab-Published, Cross-Lab. | Package 001A | Nuevo concepto — operacionaliza propiedad. | [Decisión] |
| 17 | **Knowledge_Sharing_Protocol** | Reglas que definen cómo un Lab comparte conocimiento con LabOS y otros Labs sin duplicar documentación. | Package 001A | Nuevo concepto — extensión del principio documentation-first. | [Decisión] |
| 18 | **Asset_Sharing_Protocol** | Reglas que definen cómo un Lab comparte activos reutilizables. Incluye 5 tipos compartibles por defecto (ver ADR-0002). | Package 001A | Extiende: "Activo" de Package 000 con reglas de compartición. | [Decisión] |
| 19 | **Governance_Model** | Estructura de responsabilidades, escalación y toma de decisiones entre Lab y LabOS. Nivel activo: SOLO (1 operador). | Package 001A | Nuevo concepto — formaliza gobernanza. | [Decisión] |
| 20 | **Decoupling_Protocol** | Procedimiento documentado para separar un Lab del ecosistema LabOS preservando operatividad independiente. | Package 001A | Nuevo concepto — reversibilidad de integración. | [Decisión] |
| 21 | **Lab_State** | Estado operativo de un Lab: idea, explorando, validando, operando, pausado. | Package 000 (012) / 001A | Definido en Package 000 portfolio-model.md, referenciado por 001A. | [Hecho] |
| 22 | **Review_Cycle** | Periodicidad y criterios con los que se evalúa la salud y cumplimiento de un Lab. Intervalo: 30-180 días. | Package 001A | Nuevo concepto — cadencia de evaluación. | [Decisión] |

### Términos pendientes de definición formal

| # | Término | Estado | Package responsable | Epistémico |
|---|---------|--------|--------------------| ------------|
| 23 | **Knowledge** (entidad) | Pendiente definición formal | Package 002 | [Hipótesis] |
| 24 | **Product** (entidad) | Pendiente definición formal | Package 004 | [Hipótesis] |
| 25 | **Capability** | Pendiente — abstracción futura | Condicional (≥3 labs activos) | [Visión] |

---

## Taxonomía de Activos (referencia rápida)

Referencia: [ADR-0002 — Consolidación de Taxonomía de Activos](../decisions/0002-asset-taxonomy-consolidation.md)

| # | Tipo canónico | Compartible por defecto | Equivalente inglés |
|---|---------------|------------------------|--------------------|
| 1 | Documento | ✅ Sí | documentation |
| 2 | Template | ✅ Sí | templates |
| 3 | Dataset | ✅ Sí | datasets |
| 4 | Herramienta | ✅ Sí | tools |
| 5 | Componente | ❌ No (Lab-Private) | component |
| 6 | Framework | ✅ Sí | frameworks |
| 7 | Playbook | ❌ No (Lab-Private) | playbook |

---

## Cross-references

- [Package 000 README.md — Glosario base](../packages/package-000-foundation/README.md)
- [ADR-0001 — Jerarquía de Definición Terminológica](../decisions/0001-terminology-hierarchy.md)
- [ADR-0002 — Consolidación de Taxonomía de Activos](../decisions/0002-asset-taxonomy-consolidation.md)
- [canonical-domain-map.md — Mapa de entidades](./canonical-domain-map.md)
- [architecture-invariants.md — INV-04, INV-07](../packages/package-002a-architecture-review/architecture-invariants.md)

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 16       | 46%        |
| [Hipótesis]   | 2        | 6%         |
| [Decisión]    | 16       | 46%        |
| [Visión]      | 1        | 3%         |
