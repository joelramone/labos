# Research Journal Template

## Propósito

Template para mantener el registro cronológico de actividades, hallazgos, decisiones y progreso durante una investigación. El Research_Journal captura la progresión temporal del trabajo investigativo, garantizando trazabilidad y reproducibilidad.

Este template es obligatorio para investigaciones que superan las **4 horas de esfuerzo acumulado** (effort categories Medium y Large). Para investigaciones Small (<4h), su uso es opcional pero recomendado.

---

## Campos requeridos por entrada

Cada entrada del journal requiere **8 campos obligatorios**:

| # | Campo | Tipo | Descripción | Formato |
|---|-------|------|-------------|---------|
| 1 | **date** | string | Fecha de la sesión de trabajo | ISO 8601 (YYYY-MM-DD) |
| 2 | **stage** | string | Etapa actual del Research_Lifecycle | Una de las 16 etapas válidas (ver tabla abajo) |
| 3 | **activity** | string | Descripción de la actividad realizada | 1-3 oraciones específicas |
| 4 | **findings** | string | Resumen de resultados u observaciones | Hallazgos concretos o "Sin hallazgos nuevos — sesión de [tipo]" |
| 5 | **decisions** | string | Decisiones tomadas durante la sesión | Decisión concreta o "Ninguna" |
| 6 | **next_steps** | string[] | Acciones concretas siguientes | Mínimo 1, máximo 5. Formato: verbo + objeto |
| 7 | **time_invested** | integer | Tiempo invertido en la sesión | En minutos (mínimo 15, máximo 480) |
| 8 | **tools_used** | string[] | Herramientas utilizadas | Nombres específicos (mínimo 1) |

### Valores válidos para "stage"

| # | Valor | Descripción |
|---|-------|-------------|
| 1 | `Intake` | Captura del trigger y clasificación inicial |
| 2 | `Problem Framing` | Articulación del problema core |
| 3 | `Research Question` | Formulación de preguntas de investigación |
| 4 | `Scope` | Definición de alcance y timebox |
| 5 | `Assumptions` | Surfacing de premisas ocultas |
| 6 | `Source Collection` | Recopilación y registro de fuentes |
| 7 | `Evidence Evaluation` | Clasificación y evaluación de evidencia |
| 8 | `Analysis` | Síntesis e identificación de patrones |
| 9 | `Experimentation` | Validación de hipótesis mediante experimentos |
| 10 | `Findings` | Consolidación de hallazgos |
| 11 | `Conclusion` | Formulación de conclusiones trazables |
| 12 | `Review` | Validación de calidad y completitud |
| 13 | `Asset Extraction` | Extracción de activos reutilizables |
| 14 | `Product Hypothesis` | Evaluación de oportunidad comercial |
| 15 | `Publication or Archive` | Decisión de destino final |
| 16 | `Feedback and Iteration` | Captura de feedback y cierre |

---

## Campos opcionales

| Campo | Descripción | Cuándo usar |
|-------|-------------|-------------|
| **blockers** | Impedimentos identificados durante la sesión | Cuando hay dependencias externas o accesos pendientes |
| **loop_back** | Documentación de retorno a etapa previa | Cuando se ejecuta un loop-back en el lifecycle |
| **references** | Fuentes consultadas durante la sesión | Para trazabilidad rápida (el Source_Register es el registro formal) |
| **mood/energy** | Nivel de energía o dificultad percibida | Para retrospectivas personales de productividad |

---

## Regla de 4 horas — Creación obligatoria

> **REGLA:** Cuando una investigación supera las 4 horas de esfuerzo acumulado, el Research_Journal es **obligatorio**.

| Effort category | ¿Journal obligatorio? | Acción requerida |
|-----------------|----------------------|------------------|
| Small (<4h) | No (opcional) | Usar voluntariamente si la investigación es compleja |
| Medium (4-16h) | **Sí** | Crear al cruzar el umbral de 4h |
| Large (>16h) | **Sí** | Crear desde el inicio del trabajo |

**Si se alcanza el umbral de 4h sin journal existente:** crear retroactivamente en la misma sesión de trabajo, marcando entradas reconstruidas con `[RECONSTRUCCIÓN RETROACTIVA]`.

---

## Instrucciones de uso

### Paso 1: Crear el journal al inicio de la investigación

Copiar este template y completar el encabezado con los datos de la investigación (nombre, ID, fecha de inicio). Para investigaciones Large, crear el journal inmediatamente. Para investigaciones Medium, crear cuando se alcance el umbral de 4h.

### Paso 2: Registrar una entrada al cierre de cada sesión de trabajo

Al finalizar cada sesión de trabajo (≥15 minutos), agregar una nueva entrada con los 8 campos obligatorios completados. Numerar secuencialmente (#1, #2, #3...). Ser específico en el campo `activity` — describir qué se hizo, no solo que se trabajó.

### Paso 3: Mantener orden cronológico y revisar acumulados

Las entradas van en orden cronológico ascendente (la más antigua primero). Periódicamente, revisar que el tiempo acumulado sea coherente con la effort category asignada. Si el esfuerzo real supera la categoría estimada, registrar la reclasificación en el Decision_Log.

### Paso 4: Usar el journal como input para artefactos posteriores

Al llegar a las etapas de Conclusion y Review, usar el journal como fuente de trazabilidad. Las entradas alimentan la sección de reproducibilidad de la conclusión y se verifican en el quality gate de Review.

---

## [DOMAIN-SPECIFIC] Secciones por dominio

Agregar campos adicionales según el dominio de investigación:

| Dominio | Campos adicionales sugeridos |
|---------|------------------------------|
| Technical | `environment` (OS, versiones), `code_refs` (commits, branches) |
| Quantitative | `datasets_used`, `metrics_observed`, `statistical_notes` |
| Market | `signals_detected`, `competitors_identified`, `demand_indicators` |
| Creative | `inspiration_sources`, `iterations_count`, `feedback_received` |

---

## Template de entrada

```markdown
## Entry #[número secuencial]

- **Date:** YYYY-MM-DD
- **Stage:** [etapa del lifecycle]
- **Activity:** [Descripción de 1-3 oraciones de lo que se realizó]
- **Findings:** [Resumen de hallazgos o "Sin hallazgos nuevos — sesión de [tipo]"]
- **Decisions:** [Decisión tomada o "Ninguna"]
- **Next steps:**
  1. [Acción concreta: verbo + objeto]
  2. [Acción concreta: verbo + objeto]
- **Time invested:** [número] minutos
- **Tools used:** [Herramienta1], [Herramienta2]
```

---

## Template del documento completo

```markdown
# Research Journal — [Nombre de la Investigación]

> **Investigation ID:** [ID o referencia]
> **Fecha de inicio:** YYYY-MM-DD
> **Effort category:** [Small | Medium | Large]
> **Dominio:** [Dominio de la investigación]

---

## Entry #1

- **Date:** YYYY-MM-DD
- **Stage:** [etapa]
- **Activity:** [descripción]
- **Findings:** [hallazgos]
- **Decisions:** [decisiones]
- **Next steps:**
  1. [acción]
- **Time invested:** [minutos] minutos
- **Tools used:** [herramientas]

---

## Entry #2

- **Date:** YYYY-MM-DD
- **Stage:** [etapa]
- **Activity:** [descripción]
- **Findings:** [hallazgos]
- **Decisions:** [decisiones]
- **Next steps:**
  1. [acción]
- **Time invested:** [minutos] minutos
- **Tools used:** [herramientas]

---

## Resumen de esfuerzo

| Métrica | Valor |
|---------|-------|
| Total de entradas | [N] |
| Tiempo total invertido | [suma] minutos |
| Etapas cubiertas | [lista] |
| Rango de fechas | [primera fecha] — [última fecha] |
```

---

## Ejemplo completo

El siguiente ejemplo muestra un Research_Journal con 3 entradas realistas de una investigación sobre frameworks de evaluación de evidencia.

```markdown
# Research Journal — Evidence Evaluation Frameworks Comparison

> **Investigation ID:** INV-2025-003
> **Fecha de inicio:** 2025-01-15
> **Effort category:** Medium (estimado: 12h)
> **Dominio:** Technical

---

## Entry #1

- **Date:** 2025-01-15
- **Stage:** Source Collection
- **Activity:** Busqué artículos académicos y documentación sobre frameworks de evaluación de evidencia. Identifiqué 7 fuentes potenciales a través de Google Scholar, ACM Digital Library y recomendaciones de ChatGPT Projects. Realicé filtrado inicial por relevancia y accesibilidad.
- **Findings:** 5 de 7 fuentes son accesibles y relevantes. Dos frameworks dominan la literatura: el modelo GRADE (medicina) y el Evidence Quality Framework de Smith (2022) para investigación técnica. El framework de García (2021) es demasiado específico para dominio clínico.
- **Decisions:** Descartar las 2 fuentes inaccesibles (paywall sin alternativa). Priorizar Smith (2022) como referencia principal por su orientación técnica.
- **Next steps:**
  1. Evaluar las 5 fuentes contra los 10 criterios del Source_Register
  2. Documentar las fuentes en el registro formal con scores de calidad
  3. Buscar 1-2 fuentes adicionales sobre evidencia de tipo "market data"
- **Time invested:** 90 minutos
- **Tools used:** ChatGPT Projects, Google Scholar, NotebookLM

---

## Entry #2

- **Date:** 2025-01-16
- **Stage:** Evidence Evaluation
- **Activity:** Evalué cada fuente contra los 10 criterios de calidad definidos en el Source_Register. Extraje claims principales de Smith (2022) y Lee (2023). Comparé las taxonomías de categorías de evidencia propuestas por cada autor. Documenté conflictos identificados entre frameworks.
- **Findings:** Smith (2022) obtiene score 8.2/10 y Lee (2023) score 7.5/10. Ambos son compatibles en estructura base pero difieren en el tratamiento de "evidencia inferida": Smith la clasifica como categoría separada, Lee la subsume bajo "evidencia indirecta". 3 claims de Smith son directamente aplicables a nuestro contexto sin adaptación.
- **Decisions:** Adoptar la estructura base de Smith (2022) como punto de partida para el evidence framework. Complementar con las categorías de evidencia digital de Lee (2023). Documentar el conflicto sobre "inferencia" en el Decision_Log para resolución posterior.
- **Next steps:**
  1. Crear entry en Decision_Log sobre la elección de Smith como base
  2. Mapear las categorías de Lee que complementan a Smith sin contradicción
  3. Redactar borrador de taxonomía combinada para revisión
- **Time invested:** 150 minutos
- **Tools used:** NotebookLM, ChatGPT Projects, GitHub, Obsidian

---

## Entry #3

- **Date:** 2025-01-17
- **Stage:** Analysis
- **Activity:** Sinteticé la taxonomía combinada Smith + Lee. Mapeé cada categoría de evidencia propuesta contra los dominios de investigación de LabOS (Technical, Market, Creative, etc.) para verificar cobertura. Identifiqué gaps donde ningún framework cubre adecuadamente la evidencia de tipo "market signals" y "user behavior data".
- **Findings:** La taxonomía combinada cubre 10 de 12 categorías necesarias para LabOS. Los gaps están en: (1) market signals como evidencia — ningún framework académico lo trata formalmente, y (2) user behavior data — los frameworks existentes asumen datos experimentales controlados, no observacionales. Se requiere definición propia para estas 2 categorías.
- **Decisions:** Ninguna — se requiere consulta adicional antes de definir categorías nuevas. Escalar la pregunta sobre "market signals como evidencia" al Fundador para decisión.
- **Next steps:**
  1. Documentar los 2 gaps como preguntas abiertas en el research brief
  2. Buscar 1 fuente adicional sobre market research evidence frameworks
  3. Preparar propuesta de definición para las 2 categorías faltantes
  4. Avanzar a la redacción del borrador del evidence framework con las 10 categorías confirmadas
- **Time invested:** 120 minutos
- **Tools used:** Obsidian, ChatGPT Projects, GitHub

---

## Resumen de esfuerzo

| Métrica | Valor |
|---------|-------|
| Total de entradas | 3 |
| Tiempo total invertido | 360 minutos (6h) |
| Etapas cubiertas | Source Collection, Evidence Evaluation, Analysis |
| Rango de fechas | 2025-01-15 — 2025-01-17 |
```

---

## Referencias

- [015-research-journal.md](../../packages/package-001-research-methodology/015-research-journal.md) — Definición completa de estructura y reglas
- [002-research-lifecycle.md](../../packages/package-001-research-methodology/002-research-lifecycle.md) — 16 etapas del lifecycle (valores válidos para "stage")
- [016-decision-log.md](../../packages/package-001-research-methodology/016-decision-log.md) — Artefacto complementario para decisiones significativas
