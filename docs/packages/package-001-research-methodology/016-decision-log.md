# 016 — Decision Log

> **Etiqueta epistémica:** [Decisión]
>
> **Requirements cubiertos:** R32.3, R32.4

## Propósito

Este documento define la **estructura del Decision Log**, los **triggers que obligan a registrar una decisión**, las **reglas de referencia a evidencia**, y las **políticas de reversibilidad**. El Decision Log es un artefacto transversal que se mantiene activo durante todas las etapas del lifecycle donde se toman decisiones, desde Planned hasta Publication/Archive.

El propósito del Decision Log es preservar el rationale de cada decisión significativa de una investigación para que cualquier persona (incluido el mismo Fundador en el futuro) pueda entender por qué se eligió un camino y no otro, con qué evidencia se contaba al momento, y qué consecuencias se anticipaban.

---

## Tabla de contenidos

1. [Estructura de una entrada](#estructura-de-una-entrada)
2. [Campos obligatorios](#campos-obligatorios)
3. [Triggers de registro](#triggers-de-registro)
4. [Reglas de referencia a evidencia](#reglas-de-referencia-a-evidencia)
5. [Niveles de reversibilidad](#niveles-de-reversibilidad)
6. [Cuándo mantener el Decision Log](#cuándo-mantener-el-decision-log)
7. [Relación con el lifecycle](#relación-con-el-lifecycle)
8. [Reglas operativas](#reglas-operativas)
9. [Referencias cruzadas](#referencias-cruzadas)

---

## Estructura de una entrada

Cada entrada del Decision Log registra una decisión significativa tomada durante una investigación. Las entradas se ordenan cronológicamente y se identifican por posición secuencial dentro del log.

### Campos obligatorios

El Decision Log define **8 campos obligatorios** para cada entrada:

| #  | Campo | Descripción | Formato |
|----|-------|-------------|---------|
| 1 | **Decision description** | Descripción de la decisión tomada | 1–3 oraciones declarativas |
| 2 | **Context** | Situación que provocó la necesidad de decidir | 1–5 oraciones describiendo el estado actual y el problema que la decisión resuelve |
| 3 | **Alternatives considered** | Opciones evaluadas antes de decidir | Mínimo 2 alternativas, cada una con nombre y descripción de 1–2 oraciones |
| 4 | **Selection rationale** | Justificación de por qué se eligió la opción seleccionada sobre las alternativas | 1–5 oraciones explicando los criterios de decisión y por qué las alternativas fueron descartadas |
| 5 | **Evidence** | Evidencia que soporta la decisión | Mínimo 1 referencia válida (ver sección de reglas de referencia) |
| 6 | **Consequences** | Resultados anticipados de la decisión | 1–5 oraciones describiendo impactos esperados (positivos y negativos) |
| 7 | **Reversibility** | Evaluación del grado de reversibilidad | Uno de 3 niveles definidos (ver sección de reversibilidad) |
| 8 | **Date** | Fecha en que se tomó la decisión | ISO 8601 (YYYY-MM-DD) |

---

## Triggers de registro

No toda micro-decisión requiere registro en el Decision Log. Los siguientes **triggers** definen cuándo es obligatorio registrar una decisión:

### Trigger 1: Cambio de scope

Una decisión que modifica el alcance de la investigación: añade o elimina elementos del scope, cambia las inclusiones/exclusiones, o modifica los límites de profundidad de análisis.

**Ejemplos:**

- Excluir un sub-tema originalmente incluido por falta de fuentes de calidad.
- Ampliar el scope para cubrir un dominio adicional que emergió como relevante.
- Reducir la cantidad máxima de fuentes a consultar.

### Trigger 2: Cambio de dirección

Una decisión que altera la dirección o enfoque de la investigación: cambia la hipótesis principal, reformula la research question, pivotea el approach de análisis, o modifica el outcome esperado.

**Ejemplos:**

- Abandonar una hipótesis refutada y formular una nueva.
- Cambiar de un enfoque cuantitativo a uno cualitativo por limitaciones de datos.
- Decidir que la investigación será exploratoria en lugar de confirmatoria.

### Trigger 3: Cambio de metodología

Una decisión que modifica los métodos, herramientas, protocolos o procedimientos utilizados en la investigación.

**Ejemplos:**

- Cambiar la herramienta primaria de análisis de Deepnote a NotebookLM.
- Adoptar un método alternativo de validación porque la experimentación controlada no es viable.
- Modificar el protocolo de evaluación de fuentes por insuficiencia del método original.

### Trigger 4: Cambio de timebox o deadline

Una decisión que modifica los límites temporales de la investigación: extensión del timebox, cambio de deadline, o reducción del tiempo asignado.

**Ejemplos:**

- Extender el timebox de 16h a 24h por complejidad mayor a la estimada.
- Adelantar el deadline por urgencia externa.
- Reducir timebox y cerrar con hallazgos parciales.

### Trigger 5: Resolución de conflicto de evidencia

Una decisión que resuelve (o documenta como no resuelta) una contradicción entre dos o más fuentes de evidencia.

**Ejemplos:**

- Decidir cuál de dos fuentes contradictorias tiene mayor peso y por qué.
- Declarar un conflicto como irresoluble con la evidencia disponible.
- Descartar una fuente por evaluación de calidad insuficiente frente a otra que la contradice.

### Trigger 6: Abandono o pausa

Una decisión de abandonar, pausar o archivar prematuramente una investigación, hipótesis, o línea de análisis.

**Ejemplos:**

- Abandonar una investigación que superó su timebox sin resultados.
- Pausar una línea de análisis por falta de acceso a fuentes necesarias.
- Descartar un experimento que no puede ejecutarse con los recursos disponibles.

---

## Reglas de referencia a evidencia

Toda entrada del Decision Log debe incluir al menos **1 referencia válida** en el campo Evidence. Las referencias vinculan la decisión a la evidencia o evento que la motivó.

### Tipos de referencia válidos

| Tipo | Formato | Ejemplo |
|------|---------|---------|
| **Link a documento** | Ruta relativa o URL al documento fuente | `./006-evidence-framework.md#categoría-3` |
| **Entrada de journal** | Número de entrada del Research Journal (posición secuencial) | `Journal entry #5 (2024-03-15)` |
| **Observación citada** | Texto entrecomillado con fecha y contexto | `"El dataset no contiene registros posteriores a 2022" (observado 2024-03-14)` |
| **Fuente externa nombrada** | Nombre de fuente con fecha de consulta | `API documentation de OpenAI, consultada 2024-03-10` |
| **Source Register entry** | ID de la fuente en el Source_Register de la investigación | `SRC-INV001-07 (quality score: 8/10)` |
| **Evidence record** | ID del registro de evidencia | `EVD-INV001-03 (confidence: 4)` |

### Reglas de validez

1. Toda referencia debe ser **verificable**: un tercero debe poder localizar la evidencia referenciada sin información adicional.
2. Las referencias tipo "observación citada" deben incluir **fecha** y **contexto suficiente** para reproducir la observación.
3. Si la decisión fue motivada por un **trigger event** (no por evidencia pre-existente), la referencia debe describir el evento con fecha.
4. No se acepta como referencia válida: "intuición", "experiencia general", "es obvio", o cualquier apelación a conocimiento no documentado.

---

## Niveles de reversibilidad

Cada decisión se clasifica en uno de **3 niveles de reversibilidad**:

### Nivel 1: Fácilmente reversible

| Aspecto | Descripción |
|---------|-------------|
| **Definición** | La decisión puede deshacerse sin pérdida significativa de tiempo, recursos o información. Revertir no invalida trabajo posterior. |
| **Costo de revertir** | Bajo — minutos a pocas horas de reconfiguración |
| **Impacto en artefactos** | Ningún artefacto producido queda invalidado al revertir |
| **Ejemplos** | Cambiar de herramienta para una etapa específica; modificar el orden de análisis de fuentes; ajustar un criterio de búsqueda |

### Nivel 2: Reversible con esfuerzo

| Aspecto | Descripción |
|---------|-------------|
| **Definición** | La decisión puede revertirse, pero implica re-trabajo significativo, pérdida parcial de esfuerzo invertido, o necesidad de recalcular/re-evaluar artefactos dependientes. |
| **Costo de revertir** | Medio — horas a días de re-trabajo |
| **Impacto en artefactos** | Uno o más artefactos producidos requieren revisión o actualización |
| **Ejemplos** | Cambiar la research question principal después de haber recopilado fuentes; redefinir el scope después de haber iniciado análisis; descartar un experimento a mitad de ejecución |

### Nivel 3: Irreversible

| Aspecto | Descripción |
|---------|-------------|
| **Definición** | La decisión no puede revertirse una vez ejecutada, o revertirla implica un costo inaceptable (perder toda la investigación, exceder el timebox, o requerir recursos no disponibles). |
| **Costo de revertir** | Alto a imposible — rehacer la investigación completa o perder ventana de oportunidad |
| **Impacto en artefactos** | Todos los artefactos posteriores dependen de esta decisión |
| **Ejemplos** | Publicar una conclusión externamente; abandonar una investigación y archivarla como inconclusa; invertir timebox completo en una dirección que excluye explorar alternativas |

### Criterios de asignación

Para asignar el nivel correcto, evaluar:

1. **¿Cuánto esfuerzo se pierde si se revierte?** (minutos → Nivel 1, horas/días → Nivel 2, todo → Nivel 3)
2. **¿Cuántos artefactos dependen de esta decisión?** (ninguno → Nivel 1, algunos → Nivel 2, todos → Nivel 3)
3. **¿Existe una ventana temporal después de la cual revertir es imposible?** (no → Nivel 1–2, sí → Nivel 3)

---

## Cuándo mantener el Decision Log

El Decision Log es **obligatorio** para investigaciones de effort category **Large** (>16h).

Para investigaciones **Medium** (4–16h), el Decision Log es **opcional** pero recomendado cuando la investigación involucra:

- Más de 3 fuentes evaluadas.
- Al menos 1 hipótesis formulada.
- Participación de más de 1 herramienta en el análisis.

Para investigaciones **Small** (<4h), el Decision Log **no es requerido** a menos que se tome una decisión de tipo Nivel 3 (irreversible).

---

## Relación con el lifecycle

El Decision Log es un **artefacto transversal** que se crea en la etapa **Planned** (junto con el Research Journal) y se mantiene activo a lo largo de todas las etapas donde se toman decisiones.

### Etapas con mayor densidad de decisiones

| Etapa del lifecycle | Decisiones típicas |
|--------------------|--------------------|
| **Scope** | Definición de inclusiones/exclusiones, timebox, profundidad |
| **Assumptions** | Clasificación de assumptions, validación approach |
| **Source Collection** | Selección/descarte de fuentes, resolución de gaps |
| **Evidence Evaluation** | Resolución de conflictos, asignación de confidence |
| **Analysis** | Elección de método de análisis, formulación de hipótesis |
| **Experimentation** | Selección de protocolo, decisiones ante resultados inesperados |
| **Conclusion** | Nivel de confianza asignado, alcance de la conclusión |
| **Asset Extraction** | Qué extraer como activo, formato de empaquetado |

### Etapas con menor densidad de decisiones

| Etapa del lifecycle | Nota |
|--------------------|------|
| **Intake** | Generalmente 0–1 decisiones (clasificación de effort category) |
| **Problem Framing** | Decisiones sobre articulación del problema (generalmente capturadas en el Research Brief) |
| **Review** | Decisiones de aprobación (capturadas en el Research Review) |
| **Feedback/Iteration** | Decisiones sobre futuras investigaciones (capturadas en nuevos Research Briefs) |

---

## Reglas operativas

1. **Cronología estricta:** Las entradas se registran en orden cronológico. No se reordenan ni se insertan retroactivamente entre entradas existentes.

2. **No editar entradas pasadas:** Si una decisión previa se revisa o invalida, se crea una nueva entrada que referencia la anterior — no se modifica la original.

3. **Una decisión por entrada:** Cada entrada documenta exactamente una decisión. Si un evento produce múltiples decisiones relacionadas, se crean entradas separadas con la misma fecha.

4. **Trigger obligatorio:** Toda entrada debe corresponder a al menos uno de los 6 triggers definidos. Si una decisión no corresponde a ningún trigger, no requiere registro formal en el Decision Log (puede documentarse en el Research Journal como nota).

5. **Evidencia verificable:** El campo Evidence no acepta auto-referencias circulares ni apelaciones a autoridad sin documentación. Toda referencia debe ser localizable por un tercero.

6. **Revisión en conclusión:** Al formular la conclusión de una investigación, el Decision Log debe revisarse para verificar que las decisiones registradas son consistentes con los hallazgos finales. Inconsistencias detectadas se documentan en la sección de uncertainty de la conclusión.

---

## Referencias cruzadas

- [002-research-lifecycle.md](./002-research-lifecycle.md) — Define las etapas donde el Decision Log es activo
- [015-research-journal.md](./015-research-journal.md) — Artefacto complementario para registro cronológico de actividades
- [006-evidence-framework.md](./006-evidence-framework.md) — Define categorías y niveles de confianza referenciados en el campo Evidence
- [007-source-evaluation.md](./007-source-evaluation.md) — Define los IDs de fuentes que pueden usarse como referencia
- [008-research-workflow.md](./008-research-workflow.md) — Define el flujo general donde se insertan decisiones
- [020-quality-gates.md](./020-quality-gates.md) — Quality gates que pueden generar decisiones de tipo trigger
