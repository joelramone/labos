# Decision Log Template

## Propósito

Template para registrar decisiones significativas tomadas durante una investigación, preservando el rationale, las alternativas evaluadas, la evidencia que soporta la elección, y el grado de reversibilidad. El Decision_Log garantiza que cualquier persona (incluido el mismo Fundador en el futuro) pueda entender por qué se eligió un camino y no otro.

Este template se utiliza en investigaciones de effort category **Large** (>16h) de forma obligatoria, y en investigaciones **Medium** (4–16h) de forma recomendada cuando la investigación involucra >3 fuentes, ≥1 hipótesis, o múltiples herramientas.

---

## Campos requeridos por entrada

Cada entrada del Decision Log requiere **8 campos obligatorios**:

| # | Campo | Tipo | Descripción | Formato |
|---|-------|------|-------------|---------|
| 1 | **decision** | string | Descripción de la decisión tomada | 1–3 oraciones declarativas |
| 2 | **context** | string | Situación que provocó la necesidad de decidir | 1–5 oraciones describiendo el estado actual y el problema que la decisión resuelve |
| 3 | **alternatives** | string[] | Opciones evaluadas antes de decidir | **Mínimo 2 alternativas**, cada una con nombre y descripción de 1–2 oraciones |
| 4 | **rationale** | string | Justificación de por qué se eligió la opción seleccionada | 1–5 oraciones explicando los criterios de decisión y por qué las alternativas fueron descartadas |
| 5 | **evidence** | string[] | Evidencia que soporta la decisión | Mínimo 1 referencia válida (ver tipos de referencia abajo) |
| 6 | **consequences** | string | Resultados anticipados de la decisión | 1–5 oraciones describiendo impactos esperados (positivos y negativos) |
| 7 | **reversibility** | enum | Evaluación del grado de reversibilidad | Uno de 3 niveles: `Fácilmente reversible`, `Reversible con esfuerzo`, `Irreversible` |
| 8 | **date** | string | Fecha en que se tomó la decisión | ISO 8601 (YYYY-MM-DD) |

### Niveles de reversibilidad

| Nivel | Etiqueta | Descripción | Costo de revertir |
|-------|----------|-------------|-------------------|
| 1 | **Fácilmente reversible** | La decisión puede deshacerse sin pérdida significativa de tiempo, recursos o información. Revertir no invalida trabajo posterior. | Bajo — minutos a pocas horas |
| 2 | **Reversible con esfuerzo** | La decisión puede revertirse, pero implica re-trabajo significativo, pérdida parcial de esfuerzo invertido, o necesidad de revisar artefactos dependientes. | Medio — horas a días de re-trabajo |
| 3 | **Irreversible** | La decisión no puede revertirse una vez ejecutada, o revertirla implica un costo inaceptable (perder toda la investigación, exceder timebox, o requerir recursos no disponibles). | Alto a imposible |

### Tipos de referencia válidos para "evidence"

| Tipo | Formato | Ejemplo |
|------|---------|---------|
| Link a documento | Ruta relativa o URL | `./006-evidence-framework.md#categoría-3` |
| Entrada de journal | Número de entrada del Research Journal | `Journal entry #5 (2024-03-15)` |
| Observación citada | Texto entrecomillado con fecha y contexto | `"El dataset no contiene registros post-2022" (observado 2024-03-14)` |
| Fuente externa | Nombre de fuente con fecha de consulta | `API docs de OpenAI, consultada 2024-03-10` |
| Source Register entry | ID de fuente en el Source_Register | `SRC-INV001-07 (quality score: 8/10)` |
| Evidence record | ID del registro de evidencia | `EVD-INV001-03 (confidence: 4)` |

---

## Campos opcionales

| Campo | Descripción | Cuándo usar |
|-------|-------------|-------------|
| **trigger** | Tipo de trigger que motivó la decisión | Para clasificar la naturaleza del cambio |
| **affected_artifacts** | Artefactos impactados por la decisión | Cuando la decisión modifica o invalida artefactos existentes |
| **linked_decisions** | Referencias a decisiones previas relacionadas | Cuando la decisión revisa, extiende o invalida otra anterior |
| **stakeholders_notified** | Personas o roles informados de la decisión | En investigaciones con múltiples participantes |

---

## Triggers de registro

No toda micro-decisión requiere una entrada en el Decision Log. Registrar una decisión es **obligatorio** cuando se activa alguno de los siguientes 6 triggers:

| # | Trigger | Descripción |
|---|---------|-------------|
| 1 | **Cambio de scope** | La decisión modifica el alcance: añade/elimina elementos, cambia inclusiones/exclusiones, o modifica profundidad de análisis |
| 2 | **Cambio de dirección** | La decisión altera el enfoque: cambia hipótesis principal, reformula research question, pivotea approach o modifica outcome esperado |
| 3 | **Cambio de metodología** | La decisión modifica métodos, herramientas, protocolos o procedimientos utilizados |
| 4 | **Cambio de timebox o deadline** | La decisión modifica los límites temporales: extensión, adelanto o reducción |
| 5 | **Resolución de conflicto de evidencia** | La decisión resuelve (o documenta como irresuelta) una contradicción entre fuentes |
| 6 | **Abandono o pausa** | La decisión abandona, pausa o archiva prematuramente una investigación, hipótesis, o línea de análisis |

> **Regla:** Si una decisión no corresponde a ninguno de estos 6 triggers, no requiere registro formal en el Decision Log. Puede documentarse como nota en el Research_Journal.

---

## Instrucciones de uso

### Paso 1: Crear el Decision Log al planificar la investigación

Copiar este template y completar el encabezado con los datos de la investigación (nombre, ID, fecha de inicio). Para investigaciones Large (>16h), crear desde el inicio. Para investigaciones Medium (4–16h), crear cuando se tome la primera decisión significativa (que corresponda a un trigger).

### Paso 2: Identificar si la decisión requiere registro

Antes de crear una entrada, verificar que la decisión corresponde a al menos uno de los 6 triggers definidos. Si no corresponde a ningún trigger, documentar como nota en el Research_Journal en lugar del Decision_Log.

### Paso 3: Completar todos los campos obligatorios de la entrada

Para cada decisión registrada, completar los 8 campos obligatorios. Prestar especial atención a:

- **Alternatives:** Documentar al menos 2 opciones evaluadas (incluyendo la elegida). Describir brevemente cada una para que un lector entienda qué se descartó.
- **Evidence:** Incluir al menos 1 referencia verificable. No se acepta "intuición" ni "experiencia general" como referencia.
- **Reversibility:** Asignar el nivel usando los criterios de evaluación (esfuerzo perdido, artefactos dependientes, ventana temporal).

### Paso 4: Mantener orden cronológico y revisar al concluir

Las entradas van en orden cronológico ascendente. No reordenar ni insertar retroactivamente. Al llegar a la etapa de Conclusion, revisar el Decision Log para verificar consistencia entre las decisiones registradas y los hallazgos finales.

---

## [DOMAIN-SPECIFIC] Secciones por dominio

Agregar campos adicionales según el dominio de investigación:

| Dominio | Campos adicionales sugeridos |
|---------|------------------------------|
| Technical | `technical_constraints` (limitaciones técnicas que influyen la decisión), `compatibility_impact` |
| Market | `market_signals` (señales de mercado que informan la decisión), `competitive_implications` |
| Financial | `cost_impact` (impacto económico estimado), `regulatory_constraints` |
| Creative | `creative_direction` (dirección estética o conceptual elegida), `audience_impact` |

---

## Template de entrada

```markdown
## Decision #[número secuencial]

- **Decision:** [Descripción de la decisión tomada en 1-3 oraciones]
- **Date:** YYYY-MM-DD
- **Context:** [Situación que provocó la necesidad de decidir, 1-5 oraciones]
- **Alternatives considered:**
  1. **[Nombre opción A]:** [Descripción de 1-2 oraciones]
  2. **[Nombre opción B]:** [Descripción de 1-2 oraciones]
  3. **[Nombre opción C]:** [Descripción de 1-2 oraciones] _(opcional)_
- **Rationale:** [Justificación de por qué se eligió la opción seleccionada, 1-5 oraciones]
- **Evidence:**
  - [Referencia válida 1]
  - [Referencia válida 2] _(opcional)_
- **Consequences:** [Impactos esperados positivos y negativos, 1-5 oraciones]
- **Reversibility:** [Fácilmente reversible | Reversible con esfuerzo | Irreversible]
```

---

## Template del documento completo

```markdown
# Decision Log — [Nombre de la Investigación]

> **Investigation ID:** [ID o referencia]
> **Fecha de inicio:** YYYY-MM-DD
> **Effort category:** [Medium | Large]
> **Dominio:** [Dominio de la investigación]

---

## Decision #1

- **Decision:** [Descripción de la decisión]
- **Date:** YYYY-MM-DD
- **Context:** [Situación que motivó la decisión]
- **Alternatives considered:**
  1. **[Opción A]:** [Descripción]
  2. **[Opción B]:** [Descripción]
- **Rationale:** [Justificación]
- **Evidence:**
  - [Referencia]
- **Consequences:** [Impactos esperados]
- **Reversibility:** [Nivel]

---

## Decision #2

- **Decision:** [Descripción de la decisión]
- **Date:** YYYY-MM-DD
- **Context:** [Situación que motivó la decisión]
- **Alternatives considered:**
  1. **[Opción A]:** [Descripción]
  2. **[Opción B]:** [Descripción]
- **Rationale:** [Justificación]
- **Evidence:**
  - [Referencia]
- **Consequences:** [Impactos esperados]
- **Reversibility:** [Nivel]

---

## Resumen

| Métrica | Valor |
|---------|-------|
| Total de decisiones | [N] |
| Fácilmente reversibles | [n] |
| Reversibles con esfuerzo | [n] |
| Irreversibles | [n] |
| Triggers activados | [lista de triggers únicos] |
| Rango de fechas | [primera fecha] — [última fecha] |
```

---

## Ejemplo completo

El siguiente ejemplo muestra un Decision Log con 3 entradas realistas de una investigación sobre selección de framework de evidencia para LabOS.

```markdown
# Decision Log — Evidence Evaluation Frameworks Comparison

> **Investigation ID:** INV-2025-003
> **Fecha de inicio:** 2025-01-15
> **Effort category:** Medium (estimado: 12h)
> **Dominio:** Technical

---

## Decision #1

- **Decision:** Adoptar el framework de Smith (2022) como base estructural para el Evidence_Framework de LabOS, complementándolo con categorías de evidencia digital de Lee (2023).
- **Date:** 2025-01-16
- **Context:** Se evaluaron 5 fuentes sobre frameworks de evaluación de evidencia. Se necesita seleccionar una base estructural para construir el Evidence_Framework propio de LabOS. El framework debe cubrir al menos 10 categorías de evidencia y ser aplicable a dominios técnicos, de mercado y creativos.
- **Alternatives considered:**
  1. **Smith (2022) como base:** Framework orientado a investigación técnica con 8 categorías. Score en Source_Register: 8.2/10. Estructura modular extensible.
  2. **Lee (2023) como base:** Framework de evidencia para decisiones de producto con 12 categorías. Score: 7.5/10. Más amplio pero menos riguroso en categorización.
  3. **GRADE (medicina) adaptado:** Framework estándar médico con alta madurez. Score: 9/10. Extremadamente riguroso pero diseñado para ensayos clínicos, requeriría adaptación extensiva.
- **Rationale:** Smith (2022) ofrece la mejor combinación de rigor y aplicabilidad al contexto LabOS. Su estructura modular permite extensión sin modificar la base. GRADE fue descartado porque su adaptación requeriría más de 8 horas adicionales sin garantía de que el resultado sea mejor que Smith. Lee (2023) se usa como complemento por sus categorías de evidencia digital que Smith no cubre.
- **Evidence:**
  - SRC-INV003-02 (Smith 2022, quality score: 8.2/10)
  - SRC-INV003-04 (Lee 2023, quality score: 7.5/10)
  - Journal entry #2 (2025-01-16): comparación detallada de taxonomías
- **Consequences:** La base Smith permite construir un framework de 10+ categorías dentro del timebox. El trade-off es que las categorías de "market signals" y "user behavior data" no están cubiertas por ninguna fuente y requerirán definición propia. Esto añade ~2h de trabajo adicional.
- **Reversibility:** Reversible con esfuerzo

---

## Decision #2

- **Decision:** Descartar la investigación del framework GRADE como línea de análisis y redirigir el esfuerzo a la definición de las 2 categorías faltantes (market signals y user behavior data).
- **Date:** 2025-01-17
- **Context:** La investigación ha consumido 6h de 12h estimadas. El análisis de Smith + Lee cubre 10 de 12 categorías necesarias. Profundizar en GRADE requeriría 8h adicionales (superando el timebox) y solo aportaría rigor adicional en categorías que ya están cubiertas por Smith. Las 2 categorías faltantes son más urgentes que mejorar las existentes.
- **Alternatives considered:**
  1. **Investigar GRADE en detalle:** Dedicar 4h adicionales a analizar GRADE y extraer lo aplicable. Beneficio potencial: mayor rigor en clasificación de confidence levels. Riesgo: superar timebox.
  2. **Cerrar línea GRADE y definir categorías faltantes:** Usar las ~6h restantes para definir "market signals" y "user behavior data" como categorías propias, basándose en analogía con las categorías existentes de Smith.
- **Rationale:** El análisis costo/beneficio es claro: GRADE aporta mejora marginal en un área ya cubierta (confidence levels), mientras que las 2 categorías faltantes representan un gap real que afecta la completitud del framework. Priorizar completitud sobre perfeccionamiento incremental.
- **Evidence:**
  - Journal entry #3 (2025-01-17): gap analysis mostrando 10/12 categorías cubiertas
  - "El timebox estimado es 12h y se han consumido 6h sin abordar los gaps principales" (observado 2025-01-17)
- **Consequences:** Se renuncia a la profundidad adicional de GRADE en el tratamiento de confidence levels. El framework tendrá confidence levels basados en Smith (escala 1-5 con descriptores), que es funcional aunque menos matizado que GRADE. Las 2 categorías nuevas serán definiciones propias sin respaldo académico directo, lo cual se documentará como limitación.
- **Reversibility:** Fácilmente reversible

---

## Decision #3

- **Decision:** Extender el timebox de la investigación de 12h a 16h para permitir la validación cruzada del framework propuesto contra 3 dominios del portafolio LabOS (Technical, Market, Creative).
- **Date:** 2025-01-20
- **Context:** El borrador del Evidence_Framework está completo con 12 categorías. Sin embargo, no se ha verificado que todas las categorías sean aplicables y suficientes para los dominios diversos de LabOS. Sin esta validación, el framework podría tener gaps no detectados que emergerían al usarlo en investigaciones reales de otros labs.
- **Alternatives considered:**
  1. **Cerrar con 12h y validar después:** Entregar el framework como está y validar durante su primer uso real. Riesgo: posibles gaps que requieran revisión mayor.
  2. **Extender timebox a 16h para validación cruzada:** Añadir 4h dedicadas a mapear las 12 categorías contra 3 dominios específicos del portafolio. Beneficio: mayor confianza en la completitud del framework.
- **Rationale:** El principio de LabOS de "evidence-driven" requiere que un framework que será usado por todos los labs tenga al menos una validación mínima de aplicabilidad multi-dominio. 4h adicionales (extensión del 33%) es un costo proporcionado al beneficio de detectar gaps antes de la adopción generalizada.
- **Evidence:**
  - 001-research-principles.md#principio-evidence-driven: toda decisión metodológica debe tener respaldo
  - "Las categorías market signals y user behavior data son definiciones propias sin respaldo académico" (Decision #1 consequences)
- **Consequences:** El timebox se extiende de 12h a 16h (total: +4h). La effort category se mantiene como Medium (4-16h). Si la validación cruzada identifica gaps adicionales, se documentarán como limitaciones del framework (no se extenderá el timebox nuevamente). Esto consume margen de la effort category Medium pero no la excede.
- **Reversibility:** Irreversible

---

## Resumen

| Métrica | Valor |
|---------|-------|
| Total de decisiones | 3 |
| Fácilmente reversibles | 1 |
| Reversibles con esfuerzo | 1 |
| Irreversibles | 1 |
| Triggers activados | Cambio de metodología, Cambio de dirección, Cambio de timebox |
| Rango de fechas | 2025-01-16 — 2025-01-20 |
```

---

## Reglas operativas

1. **Cronología estricta:** Las entradas se registran en orden cronológico ascendente. No se reordenan ni insertan retroactivamente.
2. **No editar entradas pasadas:** Si una decisión previa se revisa o invalida, crear una nueva entrada que referencia la anterior — no modificar la original.
3. **Una decisión por entrada:** Cada entrada documenta exactamente una decisión. Si un evento produce múltiples decisiones, crear entradas separadas con la misma fecha.
4. **Trigger obligatorio:** Toda entrada debe corresponder a al menos uno de los 6 triggers. Si no corresponde a ninguno, documentar en el Research_Journal.
5. **Evidencia verificable:** El campo evidence no acepta auto-referencias circulares ni apelaciones a autoridad no documentada. Toda referencia debe ser localizable por un tercero.
6. **Alternatives mínimo 2:** Siempre documentar al menos 2 opciones evaluadas (incluyendo la elegida). Esto demuestra que hubo deliberación, no solo reacción.

---

## Referencias

- [016-decision-log.md](../../packages/package-001-research-methodology/016-decision-log.md) — Definición completa de estructura, triggers y reglas operativas
- [015-research-journal.md](../../packages/package-001-research-methodology/015-research-journal.md) — Artefacto complementario para registro cronológico
- [006-evidence-framework.md](../../packages/package-001-research-methodology/006-evidence-framework.md) — Categorías y niveles de confianza para el campo evidence
- [007-source-evaluation.md](../../packages/package-001-research-methodology/007-source-evaluation.md) — IDs de fuentes válidos como referencia
