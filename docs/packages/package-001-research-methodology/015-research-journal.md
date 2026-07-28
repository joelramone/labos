# 015 — Research Journal

> **Etiqueta epistémica:** [Decisión]
>
> **Requirements cubiertos:** R32.1, R32.2, R32.5, R19.1

## Propósito

Este documento define la estructura, campos obligatorios, reglas de uso y procesos del Research_Journal dentro de LabOS. El Research_Journal es un artefacto transversal que registra cronológicamente las actividades, hallazgos, decisiones y cambios realizados durante una investigación, garantizando trazabilidad y reproducibilidad.

El Research_Journal permite que cualquier persona (incluido el mismo investigador en el futuro) pueda reconstruir la progresión de una investigación: qué se hizo, qué se encontró, qué se decidió y qué sigue.

---

## Tabla de contenidos

1. [Estructura de una entrada](#estructura-de-una-entrada)
2. [Campos obligatorios](#campos-obligatorios)
3. [Regla de creación obligatoria — Umbral de 4 horas](#regla-de-creación-obligatoria--umbral-de-4-horas)
4. [Orden y organización](#orden-y-organización)
5. [Proceso de reconstrucción retroactiva](#proceso-de-reconstrucción-retroactiva)
6. [Cuándo registrar entradas](#cuándo-registrar-entradas)
7. [Contribución a la reproducibilidad](#contribución-a-la-reproducibilidad)
8. [Relación con el lifecycle](#relación-con-el-lifecycle)
9. [Anti-patrones del journal](#anti-patrones-del-journal)

---

## Estructura de una entrada

Cada entrada del Research_Journal documenta una sesión de trabajo completada sobre una investigación. La entrada captura el estado del avance en un punto específico del tiempo.

### Modelo de entrada

```
Journal Entry #{posición secuencial}
├── date              : string (formato ISO 8601: YYYY-MM-DD)
├── stage             : string (etapa actual del lifecycle)
├── activity          : string (actividad realizada, 1-3 oraciones)
├── findings          : string (resumen de resultados u observaciones)
├── decisions         : string (decisiones tomadas, si las hay; "Ninguna" si no aplica)
├── next_steps        : string[] (al menos 1 acción concreta siguiente)
├── time_invested     : integer (tiempo invertido en minutos)
└── tools_used        : string[] (lista de nombres de herramientas utilizadas)
```

---

## Campos obligatorios

El Research_Journal requiere **8 campos obligatorios** por entrada. Todos deben completarse al cierre de cada sesión de trabajo.

| # | Campo | Tipo | Descripción | Reglas |
|---|-------|------|-------------|--------|
| 1 | **date** | string | Fecha de la sesión de trabajo | Formato ISO 8601 (YYYY-MM-DD). Obligatorio. No puede ser fecha futura. |
| 2 | **stage** | string | Etapa actual del lifecycle en la que se trabajó | Debe corresponder a una de las 16 etapas definidas en [002-research-lifecycle.md](./002-research-lifecycle.md). Ver tabla de valores válidos abajo. |
| 3 | **activity** | string | Descripción de la actividad realizada | Mínimo 1 oración, máximo 3 oraciones. Debe ser suficientemente específica para que un tercero entienda qué se hizo. |
| 4 | **findings** | string | Resumen de resultados, observaciones o hallazgos de la sesión | Si la sesión no produjo hallazgos nuevos, documentar: "Sin hallazgos nuevos — sesión de [tipo de actividad]". |
| 5 | **decisions** | string | Decisiones tomadas durante la sesión | Si no se tomaron decisiones, registrar "Ninguna". Si se tomó una decisión significativa (scope, dirección, metodología), debe existir también un entry correspondiente en el Decision_Log. |
| 6 | **next_steps** | string[] | Acciones concretas siguientes | Mínimo 1 acción concreta. Cada acción debe ser ejecutable (verbo + objeto). Máximo 5 acciones. |
| 7 | **time_invested** | integer | Tiempo invertido en la sesión | Expresado en minutos. Mínimo 15 minutos (sesiones menores no requieren journal entry). Máximo 480 minutos (8 horas); si una sesión excede 8h, dividir en múltiples entries. |
| 8 | **tools_used** | string[] | Herramientas utilizadas durante la sesión | Lista de nombres de herramientas (ChatGPT Projects, NotebookLM, Deepnote, Obsidian, GitHub, Kiro, u otras). Mínimo 1 herramienta. |

### Valores válidos para el campo "stage"

El campo `stage` debe contener exactamente uno de los siguientes valores, correspondientes a las 16 etapas del Research_Lifecycle:

| # | Valor del campo | Etapa del lifecycle |
|---|-----------------|---------------------|
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

## Regla de creación obligatoria — Umbral de 4 horas

### Regla principal

**CUANDO una investigación supera las 4 horas de esfuerzo acumulado**, el Research_Journal es **obligatorio**.

Esta regla se alinea con:
- La clasificación de esfuerzo del Research_Lifecycle: investigaciones **Medium** (4-16h) y **Large** (>16h) requieren journal.
- Package 000 Foundation, Regla 3: toda investigación mayor a 4h produce un activo documentado.

### Aplicación del umbral

| Effort category | ¿Journal obligatorio? | Notas |
|-----------------|----------------------|-------|
| Small (<4h) | No (opcional) | El Fundador puede mantenerlo voluntariamente para investigaciones complejas aunque breves |
| Medium (4-16h) | **Sí** | Obligatorio al cruzar el umbral de 4h |
| Large (>16h) | **Sí** | Obligatorio desde el inicio del trabajo |

### Mecanismo de detección del umbral

El Fundador es responsable de monitorear el esfuerzo acumulado. El umbral se considera alcanzado cuando:

1. La suma de `time_invested` de todas las sesiones registradas (o estimadas) supera 240 minutos (4 horas), **O**
2. La investigación fue clasificada como Medium o Large en el Intake.

Si la investigación fue clasificada como Small y el esfuerzo real supera 4h, se activa la **reclasificación a Medium** (documentada en el Decision_Log) y la creación obligatoria del journal.

---

## Orden y organización

### Orden cronológico

Las entradas del Research_Journal se mantienen en **orden cronológico ascendente** por fecha (la entrada más antigua primero, la más reciente al final).

### Identificación de entradas

Cada entrada es **identificable por su posición secuencial** dentro del journal:

- La primera entrada es `#1`
- La segunda entrada es `#2`
- Y así sucesivamente

La posición secuencial sirve como identificador único dentro del journal de una investigación específica. Este identificador se utiliza para:

- Referencias cruzadas desde el Decision_Log
- Trazabilidad desde conclusiones hacia actividades específicas
- Loop-back documentation en el lifecycle

### Formato de referencia

Para referenciar una entrada del journal desde otro artefacto:

```
Journal Entry #N (YYYY-MM-DD)
```

Ejemplo: `Journal Entry #3 (2025-01-15)` — tercera entrada del journal, correspondiente al 15 de enero de 2025.

---

## Proceso de reconstrucción retroactiva

### Cuándo aplica

La reconstrucción retroactiva se activa cuando:

1. Una investigación alcanza el umbral de 4 horas de esfuerzo acumulado, **Y**
2. No existe un Research_Journal previo para esa investigación.

### Requisito temporal

La reconstrucción **debe completarse dentro de la misma sesión de trabajo** en la que se identifica que se alcanzó el umbral. No puede posponerse a sesiones futuras.

### Proceso de reconstrucción

1. **Identificar sesiones previas** — Revisar registros disponibles (commits, mensajes en herramientas, notas, calendarios) para determinar las sesiones de trabajo realizadas antes del umbral.

2. **Reconstruir entradas** — Para cada sesión identificada, crear una entrada con los 8 campos obligatorios usando la mejor información disponible. Si un campo no puede determinarse con certeza:
   - `findings`: registrar "Reconstrucción retroactiva — hallazgos no registrados en tiempo real"
   - `decisions`: registrar "Reconstrucción retroactiva — decisiones no registradas en tiempo real"
   - `time_invested`: estimar en incrementos de 30 minutos, marcando como "(estimado)"
   - `tools_used`: listar las herramientas que se recuerdan haber usado

3. **Marcar entradas reconstruidas** — Toda entrada reconstruida retroactivamente debe incluir una nota visible:

   ```
   [RECONSTRUCCIÓN RETROACTIVA — Entrada creada el YYYY-MM-DD basada en registros disponibles]
   ```

4. **Registrar la decisión** — Documentar en el Decision_Log:
   - Que se creó el journal retroactivamente
   - El motivo (umbral de 4h alcanzado sin journal existente)
   - Las fuentes utilizadas para la reconstrucción

5. **Continuar con entradas en tiempo real** — A partir de la sesión actual, todas las entradas futuras se registran en tiempo real al cierre de cada sesión.

### Limitaciones de la reconstrucción

- Las entradas retroactivas tienen menor fidelidad que las registradas en tiempo real.
- No se espera perfección en la reconstrucción; se espera mejor esfuerzo razonable.
- Si no hay registros suficientes para reconstruir una sesión, crear una entrada mínima con los campos conocidos y marcar los demás como "No determinable — reconstrucción retroactiva".

---

## Cuándo registrar entradas

### Trigger de registro

Una entrada se registra **al cierre de cada sesión de trabajo** sobre la investigación. Una sesión de trabajo se define como un bloque continuo o semi-continuo de esfuerzo dedicado a la investigación.

### Reglas de registro

| Situación | Acción |
|-----------|--------|
| Sesión de trabajo ≥ 15 minutos | Registrar entrada obligatoriamente |
| Sesión de trabajo < 15 minutos | No requiere entrada (actividad trivial) |
| Sesión que abarca múltiples etapas | Registrar una entrada por etapa trabajada |
| Día con múltiples sesiones separadas | Registrar una entrada por sesión (pueden compartir la misma fecha) |
| Sesión sin hallazgos nuevos | Registrar entrada — documentar la actividad realizada y que no hubo hallazgos |
| Loop-back ejecutado | Registrar entrada documentando: etapa origen, etapa destino, condición triggering, razón |

---

## Contribución a la reproducibilidad

El Research_Journal contribuye directamente al cumplimiento de R19.1 (reproducibilidad) al documentar:

| Elemento de reproducibilidad | Campo(s) del journal que lo capturan |
|-----------------------------|--------------------------------------|
| Metodología usada | `activity`, `stage` |
| Pasos de análisis realizados | `activity`, `findings` |
| Herramientas y versiones | `tools_used` |
| Secuencia temporal de trabajo | `date`, orden cronológico |
| Decisiones y cambios de dirección | `decisions`, `next_steps` |
| Esfuerzo invertido | `time_invested` |

### Reglas de reproducibilidad aplicadas al journal

1. Las entradas deben ser **suficientemente detalladas** para que un tercero pueda entender la progresión del trabajo sin acceso al investigador original.
2. El campo `activity` debe describir **qué se hizo**, no solo que "se trabajó en la investigación".
3. El campo `tools_used` debe incluir herramientas específicas, no genéricos (e.g., "ChatGPT Projects" en vez de "IA").
4. Si una fuente fue consultada durante la sesión, debe registrarse también en el Source_Register (el journal no reemplaza el registro formal de fuentes).

---

## Relación con el lifecycle

### Artefacto transversal

El Research_Journal es un artefacto **transversal** que abarca desde la etapa **Planned** (cuando se crea) hasta la última etapa activa de la investigación. A diferencia de otros artefactos que se crean en una etapa específica, el journal se actualiza continuamente.

| Aspecto | Valor |
|---------|-------|
| **Creación** | Etapa Planned (inicio del trabajo activo) o al superar umbral de 4h |
| **Actualización** | Todas las etapas activas (Source Collection → Feedback and Iteration) |
| **Cierre** | Última sesión de trabajo de la investigación |
| **Artefacto complementario** | Decision_Log (para decisiones significativas referenciadas desde el journal) |

### Interacción con quality gates

El Research_Journal se verifica en el quality gate de la etapa **Review** (Etapa 12):

- ✓ Journal existe y tiene entradas (para investigaciones >4h)
- ✓ Entradas están en orden cronológico
- ✓ Campos obligatorios están completos
- ✓ Etapas referenciadas son válidas
- ✓ Tiempo total registrado es coherente con el esfuerzo estimado

---

## Anti-patrones del journal

| Anti-patrón | Síntoma | Corrección |
|-------------|---------|------------|
| Journal vacío con esfuerzo >4h | Investigación Medium/Large sin entradas | Ejecutar reconstrucción retroactiva inmediatamente |
| Entradas genéricas | `activity: "Trabajé en la investigación"` | Especificar qué se hizo: fuentes consultadas, análisis realizado, etc. |
| Acumulación de sesiones | Múltiples sesiones registradas en un solo bloque retroactivo al final | Registrar al cierre de cada sesión, no acumular |
| Journal como reemplazo de Source_Register | Fuentes documentadas solo en journal, no en registro formal | El journal complementa; las fuentes van al Source_Register |
| Next steps sin acción concreta | `next_steps: "Continuar investigando"` | Cada next step debe ser un verbo + objeto específico ejecutable |
| Omisión de decisiones | Decisiones tomadas en sesión no registradas ni en journal ni en Decision_Log | Registrar en `decisions` y, si es significativa, crear entry en Decision_Log |

---

## Ejemplo de entrada

```markdown
## Entry #4

- **Date:** 2025-01-18
- **Stage:** Source Collection
- **Activity:** Consulté 5 artículos académicos sobre frameworks de evaluación de evidencia. Comparé taxonomías de 3 autores diferentes. Evalué calidad de cada fuente contra los 10 criterios del Source_Register.
- **Findings:** 3 de 5 fuentes superan el umbral de calidad (score ≥6). Las taxonomías de Smith (2022) y Lee (2023) son compatibles con nuestro modelo. La taxonomía de García (2021) es demasiado específica para el dominio médico.
- **Decisions:** Adoptar la estructura base de Smith (2022) como punto de partida para el evidence framework, complementada con las categorías de Lee (2023) para evidencia digital.
- **Next steps:**
  1. Registrar las 5 fuentes en el Source_Register con evaluación completa
  2. Documentar conflictos entre Smith y Lee en el campo de "inference"
  3. Buscar 2 fuentes adicionales sobre evidencia de tipo "market data"
- **Time invested:** 120 minutos
- **Tools used:** NotebookLM, ChatGPT Projects, GitHub
```

---

## Referencias internas

- [002-research-lifecycle.md](./002-research-lifecycle.md) — Define las 16 etapas que alimentan el campo `stage`
- [016-decision-log.md](./016-decision-log.md) — Artefacto complementario para decisiones significativas
- [020-quality-gates.md](./020-quality-gates.md) — Quality gate donde se verifica el journal
- [008-research-workflow.md](./008-research-workflow.md) — Workflow operativo que incluye el journal

---

## Tabla epistémica

| Clasificación | Cantidad | Descripción |
|---------------|----------|-------------|
| [Decisión] | 1 | Este documento completo define la estructura y reglas del Research_Journal |
