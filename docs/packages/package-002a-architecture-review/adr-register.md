# Registro de ADRs Candidatos

## Propósito

Este documento registra los Architecture Decision Records (ADR) propuestos como resultado de la revisión arquitectónica. [Hecho] Cada ADR candidato incluye contexto, decisión requerida, dependencias y el package donde debe implementarse. Los ADRs se priorizan según el backlog de remediación.

---

## Convención de ADRs

- Ubicación: `docs/decisions/NNNN-titulo.md`
- Formato: Context → Decision → Consequences → Status
- Numeración: secuencial desde 0001
- Estado: proposed → accepted → deprecated | superseded

---

## ADRs Candidatos

### ADR-0001: Jerarquía de definición terminológica

| Campo | Valor |
|-------|-------|
| **ID** | ADR-0001 |
| **Título** | Jerarquía de definición: Package 000 como fuente de verdad, packages posteriores como extensiones |
| **Estado** | Proposed |
| **Contexto** | Package 001A introduce definiciones (Lab, tipos de activos) que divergen de las establecidas en Package 000 sin referenciarlas. [Hecho] No existe una regla que establezca qué glosario prevalece cuando hay conflicto. [Hecho] El resultado es ambigüedad sobre qué definición usar en packages futuros. |
| **Decisión requerida** | Establecer que el glosario de Package 000 README.md es la fuente de verdad terminológica global. Packages posteriores pueden EXTENDER (agregar características al término) pero no REDEFINIR (cambiar significado). Toda extensión debe referenciar la definición base explícitamente. |
| **Dependencias** | Ninguna — es fundacional |
| **Target package** | Package 000 (se agrega la regla al README o como decisión independiente) |
| **Remediación asociada** | REM-01, REM-02 |

---

### ADR-0002: Consolidación de taxonomía de activos

| Campo | Valor |
|-------|-------|
| **ID** | ADR-0002 |
| **Título** | Taxonomía única de 7 tipos de activos con subconjunto compartible |
| **Estado** | Proposed |
| **Contexto** | Package 000 define 7 tipos de activos (documento, template, dataset, herramienta, componente, framework, playbook). [Hecho] Package 001A define 5 tipos para activos compartibles (templates, frameworks, tools, datasets, documentation) usando nombres en inglés sin mapping a la taxonomía canónica. [Hecho] Esto crea confusión sobre si son los mismos tipos o tipos diferentes. |
| **Decisión requerida** | Confirmar taxonomía de 7 tipos de Package 000 como canónica. Crear mapping explícito: templates→template, frameworks→framework, tools→herramienta, datasets→dataset, documentation→documento. Declarar que componente y playbook no son compartibles por defecto (son demasiado específicos de un lab). |
| **Dependencias** | ADR-0001 (establece la regla general de precedencia) |
| **Target package** | Package 000 (confirmación) + Package 001A (referencia cuando se ejecute) |
| **Remediación asociada** | REM-02 |

---

### ADR-0003: Gobernanza proporcional al número de operadores

| Campo | Valor |
|-------|-------|
| **ID** | ADR-0003 |
| **Título** | Modelo de gobernanza escalonado por número de operadores e ingresos |
| **Estado** | Proposed |
| **Contexto** | Package 001A diseña un modelo de gobernanza con escalación de 3 niveles, Lab Contract de 15 secciones, y review cycles formales. [Hecho] Esto es apropiado para una organización con múltiples stakeholders pero genera overhead desproporcionado para 1 fundador que toma todas las decisiones unilateralmente. [Decisión] El riesgo de burnout por overhead administrativo está documentado en el registro de riesgos (Riesgo #9). [Hecho] |
| **Decisión requerida** | Establecer 3 niveles de gobernanza con triggers de activación: Nivel SOLO (1 operador, pre-revenue): decisiones documentadas en 1 párrafo, Lab Contract COMPLETO (15 secciones) como referencia de estructura pero sin revisión formal obligatoria, sin escalación. Nivel EARLY (1 operador con revenue >$1000/mes O primer colaborador): revisiones mensuales ligeras, escalación de 2 niveles. Nivel TEAM (>1 operador activo): gobernanza completa de Package 001A activada. Nota: el fundador confirmó preferencia por Lab Contract completo (15 secciones) para visibilidad total; la simplificación aplica a la operación diaria, no al template. |
| **Dependencias** | Ninguna |
| **Target package** | docs/decisions/ (independiente, aplica transversalmente) |
| **Remediación asociada** | REM-03 |

---

### ADR-0004: Research Lifecycle con default lightweight

| Campo | Valor |
|-------|-------|
| **ID** | ADR-0004 |
| **Título** | Modo Small como operación por defecto del Research Lifecycle |
| **Estado** | Proposed |
| **Contexto** | El Research Lifecycle de Package 001 define 16 etapas como el proceso completo. [Hecho] Aunque existe categorización por esfuerzo (Small/Medium/Large), la presentación del documento implica que las 16 etapas son "el proceso" y las versiones reducidas son excepciones. [Hipótesis] En la práctica, la mayoría de investigaciones de un solopreneur son Small (<4h) o Medium (4-16h). Las investigaciones Large (>16h) son la excepción, no la norma. [Hipótesis] |
| **Decisión requerida** | Invertir la perspectiva: Small es el default. Se "gradúa" al superar umbrales. La compliance se adapta: Small = 3 preguntas de verificación; Medium = assessment parcial de 6 principios; Large = assessment completo de 12 principios. Las 16 etapas son referencia teórica para Large, no operación estándar. |
| **Dependencias** | Ninguna |
| **Target package** | docs/decisions/ (modificación operativa del Package 001) |
| **Remediación asociada** | REM-04 |

---

### ADR-0005: Knowledge-to-Value Pipeline como centro arquitectónico

| Campo | Valor |
|-------|-------|
| **ID** | ADR-0005 |
| **Título** | Declaración del centro arquitectónico: Knowledge-to-Value Pipeline |
| **Estado** | Proposed |
| **Contexto** | La revisión arquitectónica identifica una tensión entre la profundidad del sistema de investigación (Package 001, 26 docs) y la prioridad declarada de revenue (principios operativos, manifiesto). [Hecho] No existe un documento autoritativo que conecte el pipeline completo Research→Knowledge→Assets→Products→Revenue. [Hecho] Cada package optimiza su dominio sin referencia explícita a cómo contribuye al flujo de valor global. |
| **Decisión requerida** | Declarar que el centro arquitectónico de LabOS es el Knowledge-to-Value Pipeline. Todo componente del sistema se evalúa por su contribución al throughput de este pipeline. Crear documento `docs/architecture/value-pipeline.md` como formalización. |
| **Dependencias** | Ninguna — es fundacional |
| **Target package** | docs/architecture/ (nuevo documento) + Package 002A (este package, como resultado de la revisión) |
| **Remediación asociada** | REM-05 |

---

### ADR-0006: Sistema único de clasificación de labs

| Campo | Valor |
|-------|-------|
| **ID** | ADR-0006 |
| **Título** | Usar solo Lab States de Package 000, deferir Maturity Model |
| **Estado** | Proposed |
| **Contexto** | Coexisten dos sistemas de clasificación: 5 estados de lab (Package 000: idea→operando) que miden actividad comercial, y 5 niveles de madurez (Package 001A: L0-L4) que miden integración al ecosistema. [Hecho] Mantener ambos sistemas para 1 persona operando 2 labs genera confusión terminológica y overhead de evaluación sin beneficio proporcional. [Decisión] |
| **Decisión requerida** | Los 5 estados de Package 000 son el único sistema activo. El Maturity Model se documenta como "framework dormido" con trigger de activación: se activa cuando ≥3 labs están en estado `explorando` o superior simultáneamente Y existe al menos 1 operador distinto al fundador. |
| **Dependencias** | ADR-0003 (gobernanza proporcional define el trigger general) |
| **Target package** | docs/decisions/ |
| **Remediación asociada** | REM-06 |

---

### ADR-0007: Cadencia de revisión proporcional a estado de lab

| Campo | Valor |
|-------|-------|
| **ID** | ADR-0007 |
| **Título** | Review cycles proporcionales al estado del lab |
| **Estado** | Proposed |
| **Contexto** | Package 001A define revisiones mensuales + trimestrales + anuales para todos los labs integrados. [Hecho] Con 11 labs en el portfolio (2 activos, 9 en idea), aplicar revisión mensual a todos genera overhead innecesario. Labs en estado `idea` no tienen actividad que revisar. [Hecho] |
| **Decisión requerida** | Modelo proporcional: `idea`=0 revisión, `explorando`=15 min/mes, `validando`=30 min/mes, `operando`=1h/mes. Revisiones trimestrales/anuales se activan solo para labs en estado ≥`validando` con ≥3 labs en ese estado. |
| **Dependencias** | ADR-0003 (gobernanza proporcional) |
| **Target package** | docs/decisions/ |
| **Remediación asociada** | REM-07 |

---

### ADR-0008: Triggers de escalación de complejidad

| Campo | Valor |
|-------|-------|
| **ID** | ADR-0008 |
| **Título** | Documento de triggers que activan frameworks dormidos |
| **Estado** | Proposed |
| **Contexto** | Múltiples decisiones de esta revisión simplifican frameworks (gobernanza, maturity model, security, reviews) con la premisa de "activar después". [Hecho] Sin un registro explícito de cuándo se activa cada framework, existe el riesgo de: (a) nunca activarlos y perder la preparación, o (b) activarlos arbitrariamente sin criterio. [Hipótesis] |
| **Decisión requerida** | Crear documento `docs/architecture/complexity-triggers.md` como registro vivo de condiciones observables que activan complejidad dormida. Revisar este documento en cada revisión mensual de labs activos. |
| **Dependencias** | ADR-0003, ADR-0006, ADR-0007 (definen los frameworks dormidos) |
| **Target package** | docs/architecture/ (nuevo documento) |
| **Remediación asociada** | REM-09 |

---

## Orden de Ejecución Recomendado

```text
ADR-0001 (terminología)          ─── P0, sin dependencias
    │
    ▼
ADR-0002 (taxonomía activos)     ─── P0, depende de 0001
    
ADR-0003 (gobernanza)            ─── P1, sin dependencias
    │
    ├──▶ ADR-0006 (lab states)   ─── P2, depende de 0003
    │
    ├──▶ ADR-0007 (review cycles)─── P2, depende de 0003
    │
    └──▶ ADR-0008 (triggers)     ─── P2, depende de 0003+0006+0007

ADR-0004 (research default)      ─── P1, sin dependencias

ADR-0005 (value pipeline)        ─── P1, sin dependencias
```

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 18       | 56%        |
| [Hipótesis]   | 4        | 13%        |
| [Decisión]    | 10       | 31%        |
| [Visión]      | 0        | 0%         |
