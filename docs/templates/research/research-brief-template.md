# Research Brief Template

> **Propósito:** Capturar el trigger inicial de una investigación, establecer contexto, clasificar dominio y esfuerzo, y definir el tipo de investigación antes de invertir trabajo significativo. Este template es el punto de entrada obligatorio para toda investigación que supere 30 minutos de trabajo.
>
> **Campos requeridos:** 8 (full intake) | 4 (lightweight intake para esfuerzo Small <4h)
>
> **Requirements:** R2.2, R2.3, R27.3

---

## Instrucciones de uso

1. **Crear el Research Brief** al identificar una necesidad de investigación (pregunta, problema, oportunidad, incidente, observación, dataset o documento). Copiar este template y completar los campos obligatorios antes de invertir más de 30 minutos en investigación.

2. **Determinar el effort category** estimado (Small <4h, Medium 4–16h, Large >16h). Si el esfuerzo es Small (<4h), solo los campos marcados como `[LIGHTWEIGHT]` son obligatorios; los demás campos son opcionales pero recomendados.

3. **Seleccionar el research type** (o combinación de hasta 3 tipos) consultando la taxonomía en `003-research-types.md`. Incluir una justificación de 1–2 oraciones por cada tipo seleccionado.

4. **Validar completitud** verificando que todos los campos obligatorios según el effort category están completos. Si falta algún campo obligatorio, el Research Brief no se considera válido para iniciar investigación.

5. **Registrar en GitHub** con commit al repositorio una vez completo y válido. El Research Brief inicia el Research_Lifecycle en estado "Proposed".

---

## Campos requeridos

### Trigger `[LIGHTWEIGHT]`

> Qué evento, pregunta, observación o necesidad disparó esta investigación. Mínimo 1 oración.

**Trigger:**

<!-- Ejemplo: "Observé que el tiempo de respuesta del agente de clasificación supera los 3 segundos en producción, cuando debería ser <1s." -->

---

### Initial Context

> Información de fondo suficiente para entender el espacio del problema. Mínimo 2 oraciones.

**Context:**

<!-- Ejemplo: "El agente de clasificación fue desplegado hace 2 semanas usando GPT-4o. Los logs muestran latencia elevada en el 40% de las requests, pero no hay degradación en accuracy." -->

---

### Requester `[LIGHTWEIGHT]`

> Identidad de quien solicita o inicia la investigación.

**Requester:**

<!-- Ejemplo: "Fundador — Juan Delgado" -->

---

### Expected Value `[LIGHTWEIGHT]`

> Declaración única describiendo el resultado anticipado o beneficio de esta investigación.

**Expected value:**

<!-- Ejemplo: "Identificar la causa raíz de la latencia y determinar si es posible reducirla a <1s sin comprometer accuracy." -->

---

### Preliminary Domain Classification

> Dominio al que pertenece esta investigación, mapeado a un lab activo del portafolio o marcado como "unassigned".

**Domain:**

<!-- Opciones: SoftwareFactoryAgentsAI | CommunityManagerBotCrew | Mindzers | SentinelOps | Crypto Scalping Core | Atlas Wealth Labs | Human Performance Lab | Photography Lab | Music Lab | English Learning Lab | LabOS | unassigned -->

---

### Estimated Effort Category

> Categoría de esfuerzo estimado que determina el nivel de documentación requerido.

**Effort category:**

<!-- Opciones: Small (<4h) | Medium (4–16h) | Large (>16h) -->

---

### Origin Type `[LIGHTWEIGHT]`

> Tipo de entrada que originó la investigación. Exactamente uno de los valores permitidos.

**Origin type:**

<!-- Opciones: question | problem | opportunity | incident | dataset | document | observation -->

---

### Research Type

> Tipo(s) de investigación seleccionado(s) de la taxonomía (máximo 3). Incluir justificación por cada tipo.

**Research type(s):**

<!-- Opciones: Exploratory | Descriptive | Comparative | Experimental | Diagnostic | Market | Product | Technical | Quantitative | Qualitative | Educational | Creative -->

**Justification:**

<!-- Ejemplo: "Se selecciona Diagnostic porque existe un incidente observable (latencia elevada) y se necesita identificar la causa raíz antes de poder aplicar corrección." -->

---

## Campos opcionales

### Research Question (preliminary)

> Pregunta de investigación preliminar. Se refinará en la etapa de Research Question del lifecycle.

**Preliminary question:**

---

### Known Constraints

> Restricciones conocidas que podrían limitar la investigación (tiempo, acceso, recursos, regulación).

**Constraints:**

---

### Related Investigations

> Referencias a investigaciones previas o activas relacionadas con este tema.

**Related:**

---

### Priority

> Nivel de urgencia o importancia relativa.

**Priority:**

<!-- Opciones: High (bloquea trabajo activo) | Medium (impacta trabajo planificado) | Low (mejora futura) -->

---

### Stakeholders

> Personas, labs o sistemas afectados por esta investigación.

**Stakeholders:**

---

## [DOMAIN-SPECIFIC] Secciones por dominio

> Las siguientes secciones son opcionales y se activan según el dominio de la investigación. Incluir solo la sección aplicable.

### [DOMAIN-SPECIFIC] Technical Research

| Campo | Valor |
|-------|-------|
| Technology/Stack | |
| Version(s) | |
| Environment | |
| Reproducibility requirements | |

### [DOMAIN-SPECIFIC] Quantitative Research

| Campo | Valor |
|-------|-------|
| Dataset source | |
| Time period | |
| Variables of interest | |
| Statistical methods considered | |

### [DOMAIN-SPECIFIC] Market Research

| Campo | Valor |
|-------|-------|
| Target segment | |
| Geographic scope | |
| Competitive landscape known | |
| Demand signal source | |

### [DOMAIN-SPECIFIC] Health/Performance Research

| Campo | Valor |
|-------|-------|
| Metrics tracked | |
| Baseline available | |
| Safety considerations | |
| Professional consultation needed | |

### [DOMAIN-SPECIFIC] Creative Research

| Campo | Valor |
|-------|-------|
| Medium | |
| References/influences | |
| Aesthetic criteria | |
| Audience | |

### [DOMAIN-SPECIFIC] Finance Research

| Campo | Valor |
|-------|-------|
| Instruments/markets | |
| Regulatory considerations | |
| Historical data available | |
| Risk disclaimer | |

---

## Ejemplo completo

> A continuación un Research Brief completado con datos realistas para una investigación de esfuerzo Medium en el dominio Technical.

---

### Trigger `[LIGHTWEIGHT]`

**Trigger:** El agente de clasificación de tickets en SoftwareFactoryAgentsAI está respondiendo con latencia promedio de 3.2 segundos por request en producción, superando el SLA interno de 1 segundo establecido en el deployment brief.

---

### Initial Context

**Context:** El agente fue desplegado hace 14 días usando GPT-4o como modelo base con un prompt de 2,400 tokens. Los logs de producción muestran que el 43% de las requests superan 2.5s, concentradas en tickets con más de 500 palabras. No se ha observado degradación en la accuracy de clasificación (se mantiene en 91%). El problema fue detectado al revisar las métricas semanales de SentinelOps.

---

### Requester `[LIGHTWEIGHT]`

**Requester:** Fundador — Juan Delgado

---

### Expected Value `[LIGHTWEIGHT]`

**Expected value:** Identificar la causa raíz de la latencia elevada y determinar si es posible reducirla por debajo de 1 segundo sin degradar la accuracy por debajo del 85%.

---

### Preliminary Domain Classification

**Domain:** SoftwareFactoryAgentsAI

---

### Estimated Effort Category

**Effort category:** Medium (4–16h)

---

### Origin Type `[LIGHTWEIGHT]`

**Origin type:** incident

---

### Research Type

**Research type(s):** Diagnostic, Technical

**Justification:**
- "Se selecciona Diagnostic porque existe un incidente observable (latencia elevada fuera de SLA) con síntomas medibles, y se necesita identificar la causa raíz separando factores contribuyentes."
- "Se selecciona Technical porque la resolución requiere evaluar alternativas técnicas (modelos más rápidos, prompt optimization, caching) y medir su viabilidad bajo las restricciones del sistema."

---

### Research Question (preliminary)

**Preliminary question:** ¿Qué factor(es) causan que el 43% de las requests del agente de clasificación superen 2.5s de latencia, y qué intervención técnica puede reducir la latencia promedio a <1s manteniendo accuracy ≥85%?

---

### Known Constraints

**Constraints:**
- Presupuesto de API limitado a $50/mes para este agente.
- No se puede cambiar la arquitectura del sistema (debe permanecer como agente stateless).
- El fix debe ser compatible con el deployment pipeline actual en GitHub Actions.

---

### Related Investigations

**Related:** Ninguna investigación previa sobre este agente. Existe knowledge asset KA-007 "GPT-4o latency patterns" del lab SoftwareFactoryAgentsAI con benchmarks generales.

---

### Priority

**Priority:** High (bloquea trabajo activo) — El SLA incumplido afecta la confianza del sistema de tickets y genera acumulación manual.

---

### Stakeholders

**Stakeholders:** SoftwareFactoryAgentsAI (lab owner), SentinelOps (monitoring), Fundador (decisión de inversión).

---

### [DOMAIN-SPECIFIC] Technical Research

| Campo | Valor |
|-------|-------|
| Technology/Stack | OpenAI GPT-4o API, Python 3.11, FastAPI, GitHub Actions |
| Version(s) | GPT-4o (2024-05-13), openai-python 1.30.1 |
| Environment | Production (AWS Lambda), Staging (local Docker) |
| Reproducibility requirements | Debe poder reproducirse en staging con dataset de 50 tickets representativos |

---

## Variante Lightweight (Small <4h)

> Para investigaciones de esfuerzo Small (<4h), solo los campos marcados `[LIGHTWEIGHT]` son obligatorios. Ejemplo mínimo válido:

**Trigger:** ¿Existe un plugin de Obsidian que permita sincronizar notas con formato Dataview directamente a GitHub sin pasar por git manual?

**Requester:** Fundador — Juan Delgado

**Expected value:** Determinar si existe una solución existente para automatizar el sync Obsidian→GitHub, evitando commits manuales diarios.

**Origin type:** question

---
