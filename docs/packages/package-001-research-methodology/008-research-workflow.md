# 008 — Research Workflow

> **Etiqueta epistémica:** [Decisión]
>
> **Requirements cubiertos:** R3.1, R3.2, R3.3, R3.4, R5.1, R5.2, R5.3, R5.4, R6.1, R6.2, R6.3, R6.4, R11.1, R18.1, R18.2, R18.3, R18.4, R18.5

## Propósito

Este documento define el **workflow operativo** del proceso investigativo de LabOS: cómo se ejecuta una investigación paso a paso, integrando problem framing, definición de scope, documentación de assumptions, registro de resultados, reglas de timebox, completion criteria y mecanismos de loop-back entre etapas.

El workflow complementa al [002-research-lifecycle.md](./002-research-lifecycle.md) (que define las 16 etapas formales) y al [004-research-question-framework.md](./004-research-question-framework.md) (que define la formulación de preguntas) proporcionando las reglas operativas de ejecución: cuándo actuar, qué decidir, cuándo retroceder y cuándo cerrar.

---

## Tabla de contenidos

1. [Visión general del flujo](#visión-general-del-flujo)
2. [Problem framing operativo](#problem-framing-operativo)
3. [Definición de scope](#definición-de-scope)
4. [Documentación de assumptions](#documentación-de-assumptions)
5. [Registro de resultados](#registro-de-resultados)
6. [Reglas de timebox](#reglas-de-timebox)
7. [Completion criteria](#completion-criteria)
8. [Decisiones al 80%](#decisiones-al-80)
9. [Mecanismo de loop-back](#mecanismo-de-loop-back)
10. [Flujo integrado — diagrama operativo](#flujo-integrado--diagrama-operativo)
11. [Referencias internas](#referencias-internas)

---

## Visión general del flujo

El workflow operativo conecta cuatro bloques funcionales principales, cada uno con inputs/outputs definidos:

```text
┌────────────────────────────────────────────────────────────────────────┐
│                        BLOQUE 1: DEFINICIÓN                            │
│                                                                        │
│  [Trigger] → Problem Framing → Research Question → Scope → Assumptions │
│                                                                        │
│  Output: Plan ejecutable con boundaries claros                         │
└────────────────────────┬───────────────────────────────────────────────┘
                         │
                         ▼
┌────────────────────────────────────────────────────────────────────────┐
│                        BLOQUE 2: EJECUCIÓN                             │
│                                                                        │
│  Source Collection → Evidence Evaluation → Analysis → Experimentation  │
│                                                                        │
│  Output: Evidencia evaluada, hipótesis validadas                       │
└────────────────────────┬───────────────────────────────────────────────┘
                         │
                         ▼
┌────────────────────────────────────────────────────────────────────────┐
│                        BLOQUE 3: SÍNTESIS                              │
│                                                                        │
│  Findings → Conclusion → Review                                        │
│                                                                        │
│  Output: Conclusión validada y aprobada                                │
└────────────────────────┬───────────────────────────────────────────────┘
                         │
                         ▼
┌────────────────────────────────────────────────────────────────────────┐
│                        BLOQUE 4: VALOR                                 │
│                                                                        │
│  Asset Extraction → Product Hypothesis → Publication/Archive           │
│                                                                        │
│  Output: Activo reutilizable, oportunidad comercial (si aplica)        │
└────────────────────────────────────────────────────────────────────────┘
```

**Regla transversal:** En cada transición entre bloques se evalúa el timebox consumido y se aplican las reglas de decisión al 80%.

---

## Problem framing operativo

### Propósito

Articular el problema con suficiente claridad para derivar preguntas de investigación. Separar explícitamente lo que se observa (síntoma) de lo que se infiere (causa raíz).

### Inputs requeridos

- Research_Brief completado (etapa Intake)
- Trigger documentado con contexto inicial

### Proceso paso a paso

| Paso | Acción | Output |
|------|--------|--------|
| 1 | Redactar **problem statement** (mínimo 2 oraciones describiendo el problema) | Statement documentado |
| 2 | Identificar **contexto afectado** (dominio y entorno operativo) | Dominio + entorno |
| 3 | Registrar **síntomas observables** (≥1 observación concreta y medible) | Lista de síntomas |
| 4 | Documentar **constraints conocidos** (factores que limitan soluciones posibles) | Lista de constraints |
| 5 | Identificar **stakeholders impactados** (≥1 rol o grupo nombrado) | Lista de stakeholders |
| 6 | Separar **síntoma** (qué se observa) de **root problem** (por qué ocurre) como campos etiquetados | Síntoma + root problem |
| 7 | Formular ≥1 **research question** que incluya variable, contexto y criterio medible | Question(s) inicial(es) |

### Reglas de validación

- **Bloqueo:** Si alguno de los campos obligatorios (problem statement, contexto, síntomas, constraints, stakeholders, síntoma, root problem) queda vacío, la investigación NO puede avanzar a la siguiente etapa.
- **Indicador de completitud:** El problem statement es suficientemente específico si genera al menos una research question verificable.
- **Timebox:** Máximo 4 horas. Si no se logra articular el problema en ese tiempo, el problema es demasiado amplio y requiere descomposición.

### Output del problem framing

```text
Problem Statement:
  [Descripción del problema — mínimo 2 oraciones]

Contexto afectado:
  Dominio: [dominio]
  Entorno: [descripción del entorno operativo]

Síntomas observables:
  1. [Observación concreta y medible]
  2. [...]

Constraints conocidos:
  - [Factor limitante 1]
  - [...]

Stakeholders impactados:
  - [Rol o grupo 1]
  - [...]

Síntoma (qué se observa):
  [Evento observable y medible]

Root Problem (por qué ocurre):
  [Explicación causal]

Research Questions derivadas:
  1. [Pregunta con variable + contexto + criterio medible]
```

---

## Definición de scope

### Propósito

Establecer boundaries explícitos que prevengan investigación indefinida. Cada investigación tiene un alcance finito, medible y revisable.

### Inputs requeridos

- Research questions aprobadas (pasan quality criteria)
- Problem framing completado

### Campos obligatorios del scope

| Campo | Descripción | Ejemplo |
|-------|-------------|---------|
| **Inclusiones** | Qué está dentro del alcance de esta investigación | "Comparar 3 frameworks de orquestación de agentes" |
| **Exclusiones** | Qué está explícitamente fuera (previene scope creep) | "No incluye implementación de PoC, solo evaluación documental" |
| **Profundidad de análisis** | Nivel de detalle: superficial, moderado o profundo | "Moderado — síntesis y comparación entre fuentes" |
| **Dominios involucrados** | Qué áreas de conocimiento participan | "AI Agents, DevOps" |
| **Máximo de fuentes** | Entero entre 3 y 50 | "15 fuentes máximo" |
| **Timebox** | Horas de esfuerzo (mínimo 1h, máximo 40h) | "16 horas" |
| **Deadline** | Fecha calendario (formato YYYY-MM-DD) | "2025-02-15" |

### Niveles de profundidad

| Nivel | Descripción | Esfuerzo típico |
|-------|-------------|-----------------|
| **Superficial** | Resumen de fuentes existentes, sin análisis original | 1-4h |
| **Moderado** | Síntesis y comparación entre fuentes, integración de hallazgos | 4-16h |
| **Profundo** | Análisis original con cross-validation de claims, experimentación | 16-40h |

### Regla de cambio de scope post-inicio

Si el scope necesita cambiar después de que el trabajo ha comenzado:

1. Documentar **qué elemento del scope** se modifica
2. Registrar **la razón** del cambio
3. Evaluar **impacto en timebox y deadline** — confirmar si siguen siendo válidos o requieren ajuste
4. Registrar el cambio en el Decision_Log

---

## Documentación de assumptions

### Propósito

Surfacear premisas ocultas que podrían invalidar la investigación si resultan incorrectas. Toda investigación parte de supuestos — el rigor requiere hacerlos explícitos.

### Cuándo documentar

- **Obligatorio:** Al inicio de toda investigación, antes de invertir esfuerzo en recopilación de fuentes.
- **Mínimo:** ≥1 assumption listada, o justificación explícita de por qué no existen assumptions.

### Estructura de cada assumption

| Campo | Descripción |
|-------|-------------|
| **Statement** | La premisa que se asume verdadera |
| **Tipo** | Domain (sobre el tema), Methodological (sobre el enfoque), Resource (sobre tiempo/capacidad), Contextual (sobre condiciones externas) |
| **Confidence level** | High / Medium / Low |
| **Basis** | Base para el nivel de confianza asignado |
| **Impact if wrong** | Qué pasa si esta assumption es incorrecta |
| **Validation approach** | Cómo se verificará durante la investigación |

### Clasificación de assumptions

| Tipo | Descripción | Ejemplo |
|------|-------------|---------|
| **Domain** | Sobre el tema investigado | "El mercado de AI agents crecerá >30% anual en los próximos 3 años" |
| **Methodological** | Sobre el enfoque de investigación | "Las fuentes públicas disponibles son suficientes para responder la pregunta" |
| **Resource** | Sobre tiempo, capacidad o materiales | "16 horas son suficientes para evaluar 10 fuentes con profundidad moderada" |
| **Contextual** | Sobre condiciones externas | "Las herramientas evaluadas seguirán disponibles durante el periodo de análisis" |

### Reglas de invalidación

Cuando una assumption se invalida durante la investigación (evidencia la contradice o la confianza cae por debajo del nivel original):

1. **Identificar findings dependientes** — qué hallazgos se basan en esta assumption
2. **Reassess cada finding afectado** — producir para cada uno:
   - **Revisión:** El finding se ajusta con nueva evidencia
   - **Retracción:** El finding se retira por no sostenerse
   - **Confirmación:** El finding sigue siendo válido a pesar de la invalidación (con justificación)
3. **Registrar en Decision_Log** — documentar la invalidación y sus consecuencias

### Regla de ausencia

Si una investigación se documenta sin al menos una assumption listada, se requiere **justificación explícita** de que no existen premisas ocultas. Esta justificación previene el patrón de no haber reflexionado sobre assumptions.

---

## Registro de resultados

### Propósito

Documentar de forma estructurada y consistente todo resultado de la investigación — positivo, negativo o inconcluso — para mantener trazabilidad y aprendizaje.

### Campos obligatorios por resultado

| Campo | Descripción |
|-------|-------------|
| **Actividad productora** | Qué actividad generó este resultado (análisis de fuente, experimento, observación, comparación) |
| **Fecha** | Cuándo se obtuvo |
| **Clasificación** | Positivo, Negativo, o Inconcluso |
| **Descripción** | 1-3 párrafos describiendo qué se encontró |
| **Categoría de evidencia** | Según taxonomía del [006-evidence-framework.md](./006-evidence-framework.md) |
| **Confidence level** | 1-5 según escala definida |
| **Datos/referencias de soporte** | Fuentes, datos o referencias que soportan el resultado |
| **Relación con research question** | Qué pregunta responde (total o parcialmente) |

### Resultados negativos e inconclusos

Los resultados negativos e inconclusos tienen **la misma obligación de documentación** que los positivos. Requieren adicionalmente:

- Qué se intentó
- Por qué no produjo un finding positivo
- Qué se aprendió (incluso de la ausencia de resultado)

### Verificación de resultados

| Status | Definición | Cuándo aplica |
|--------|-----------|---------------|
| **Preliminary** | No verificado contra fuentes independientes | Resultado recién obtenido |
| **Confirmed** | Verificado contra ≥2 fuentes independientes | Después de cross-validation |
| **Contested** | ≥2 fuentes proveen evidencia conflictiva | Cuando se detectan discrepancias |

### Cambio de status

Cuando un resultado cambia de status (preliminary → confirmed, o preliminary → contested):

1. Registrar el **nuevo status**
2. Documentar la **fecha de cambio**
3. Describir la **evidencia que triggereó** la transición
4. Referenciar las **fuentes corroborantes o conflictivas**

---

## Reglas de timebox

### Principio fundamental

Toda investigación tiene un tiempo máximo de esfuerzo. El timebox previene investigación indefinida y fuerza decisiones oportunas.

### Requisito de definición

Al iniciar una investigación se debe definir **al menos uno** de:

| Mecanismo | Formato | Rango |
|-----------|---------|-------|
| **Timebox** | Horas de esfuerzo | 1–80 horas |
| **Deadline** | Fecha calendario | YYYY-MM-DD |
| **Completion criteria** | Condiciones observables de finalización | Lista de condiciones |

### Regla de compliance

Si una investigación no tiene definido ninguno de estos tres mecanismos, se marca como **non-compliant** y se bloquea trabajo adicional hasta que se defina al menos uno.

### Decisión obligatoria al alcanzar el timebox

Cuando se consume el 100% del timebox asignado, el Fundador **debe** elegir una de tres opciones:

| Opción | Requisitos | Restricción |
|--------|-----------|-------------|
| **Concluir** | Progresar a Conclusion con findings actuales | Debe avanzar a Conclusion dentro de 48 horas |
| **Extender** | Justificación escrita + nuevo timebox | Nuevo timebox ≤ timebox original. Máximo 2 extensiones consecutivas por investigación |
| **Reducir scope** | Documentar qué se elimina del alcance + completion criteria actualizados | Scope reducido debe ser viable con tiempo restante |

### Formato de extensión

```text
Extensión #[1/2]:
  Timebox original: [X horas]
  Timebox adicional: [Y horas, donde Y ≤ X]
  Razón: [Justificación de por qué se necesita más tiempo]
  Nuevo completion criteria: [Qué se espera lograr con el tiempo adicional]
  Fecha de decisión: [YYYY-MM-DD]
```

### Regla de grace period

Cuando los completion criteria se cumplen, la investigación **debe** progresar a la etapa de Conclusion dentro de **48 horas**. Si transcurren 48 horas sin progresión, la investigación se marca como **overdue** y se notifica al Fundador.

---

## Completion criteria

### Propósito

Definir condiciones observables y verificables bajo las cuales una investigación se considera "terminada" — independientemente del timebox restante.

### Características de buenos completion criteria

- **Observables:** Un tercero puede verificar si se cumplieron
- **Binarios:** Se cumplieron o no — sin ambigüedad
- **Vinculados a la research question:** Responden (total o parcialmente) a la pregunta original
- **Independientes del esfuerzo:** Se definen por resultado, no por horas invertidas

### Ejemplos por nivel de profundidad

| Profundidad | Completion criteria ejemplo |
|-------------|---------------------------|
| Superficial | "Se identificaron y resumieron ≥5 fuentes que cubren el tema" |
| Moderado | "Se produjo una comparación documentada entre ≥3 opciones con pros/cons para cada una" |
| Profundo | "La hipótesis principal fue validada o refutada con evidencia de ≥2 fuentes independientes" |

### Relación con timebox

- Los completion criteria y el timebox son **complementarios**, no excluyentes.
- Si los criteria se cumplen antes del timebox → avanzar a Conclusion (no gastar tiempo extra).
- Si el timebox se agota antes de cumplir criteria → aplicar regla de decisión al 80%.

---

## Decisiones al 80%

### Regla del 80%

Cuando una investigación ha consumido el **80% o más de su timebox** sin alcanzar una conclusión:

1. **Detener trabajo activo** temporalmente
2. **Evaluar estado actual** — qué se tiene y qué falta
3. **Decidir** — el Fundador elige una de las siguientes opciones:

| Opción | Cuándo aplica | Acción requerida |
|--------|---------------|-----------------|
| **Extender timebox** | Hay progreso claro y la conclusión está próxima | Justificación escrita + nuevo timebox ≤ original. Máximo 2 extensiones |
| **Reducir scope** | El alcance original era demasiado amplio | Documentar qué elementos se eliminan + confirmar que lo restante es viable |
| **Concluir con findings parciales** | Hay evidencia suficiente para una conclusión parcial | Documentar qué queda sin resolver + avanzar a Conclusion |

### Trigger automático

El checkpoint del 80% se activa **automáticamente** cuando:

```text
Horas invertidas ≥ 0.8 × Timebox asignado
```

### Registro de la decisión al 80%

```text
Checkpoint 80%:
  Timebox asignado: [X horas]
  Horas invertidas: [Y horas]
  Estado actual: [Resumen de progreso en 2-3 oraciones]
  Qué falta: [Lo que no se ha logrado]
  Decisión: [Extender / Reducir scope / Concluir parcialmente]
  Justificación: [Por qué esta opción]
  Fecha: [YYYY-MM-DD]
```

---

## Mecanismo de loop-back

### Principio

El workflow no es estrictamente lineal. Cuando la evidencia lo requiere, es legítimo retroceder a una etapa previa. Sin embargo, todo retroceso debe ser **justificado, documentado y limitado** para prevenir loops infinitos.

### Cuándo se permite un loop-back

Un loop-back es legítimo cuando:

- La evidencia recopilada invalida el framing original
- Las fuentes son insuficientes para responder la research question
- Una assumption clave se demuestra incorrecta
- Los resultados de experimentación contradicen el análisis previo
- El review identifica gaps que requieren trabajo adicional

### Loop-backs por bloque

#### Bloque 1 (Definición) → Bloque 1

| Desde | Hacia | Condición |
|-------|-------|-----------|
| Research Question → Problem Framing | La pregunta no es formulable con el framing actual |
| Scope → Research Question | Las questions no caben en un timebox razonable |

#### Bloque 2 (Ejecución) → Bloque 2

| Desde | Hacia | Condición |
|-------|-------|-----------|
| Evidence Evaluation → Source Collection | Fuentes insuficientes o gaps críticos |
| Analysis → Evidence Evaluation | Conflictos no resueltos requieren re-evaluación |
| Analysis → Source Collection | Nuevas preguntas requieren fuentes adicionales |
| Experimentation → Analysis | Resultados inconclusos requieren nueva síntesis |

#### Bloque 3 (Síntesis) → Bloque 2

| Desde | Hacia | Condición |
|-------|-------|-----------|
| Findings → Analysis | Hallazgos no responden las research questions |
| Conclusion → Findings | Evidencia insuficiente para soportar conclusión |
| Review → cualquier etapa 6-10 | Deficiencias identificadas durante review |

### Requisitos para ejecutar un loop-back

Cada retorno a una etapa previa **debe documentar** los siguientes campos:

| Campo | Descripción |
|-------|-------------|
| **Fecha** | Cuándo se decide el retroceso |
| **Etapa origen** | Desde dónde se retrocede |
| **Etapa destino** | A dónde se retorna |
| **Condición triggering** | Qué evento o hallazgo invalida el output actual |
| **Razón de insuficiencia** | Por qué el output actual es insuficiente (1-3 oraciones) |
| **Outcome esperado** | Qué se espera obtener al repetir la etapa destino |
| **Número de iteración** | 1ª, 2ª, o 3ª vez que se retorna a esta etapa |

### Límite de iteraciones

Si una investigación ejecuta loop-back **a la misma etapa más de 3 veces**, se activa un protocolo de escalación:

| Opción | Descripción |
|--------|-------------|
| **Continuar** | Justificación explícita de por qué esta iteración será diferente |
| **Pivotar** | Reformular la research question o el approach |
| **Cerrar** | Cerrar investigación con closure rationale, clasificar como Rejected |

La decisión se registra en el Decision_Log.

### Impacto del loop-back en el timebox

- Cada loop-back **consume tiempo del timebox original** — no lo resetea.
- Si un loop-back lleva la investigación al checkpoint del 80%, se aplican las reglas de decisión al 80%.
- Si se otorga extensión, la extensión cubre tanto trabajo nuevo como el loop-back.

---

## Flujo integrado — diagrama operativo

```text
[Trigger identificado]
       │
       ▼
╔══════════════════════════════════════════════════════════════════╗
║  PROBLEM FRAMING                                                ║
║  • Problem statement (≥2 oraciones)                             ║
║  • Síntoma vs Root Problem                                      ║
║  • Contexto + Constraints + Stakeholders                        ║
║  • Output: ≥1 research question verificable                     ║
║  • Timebox: 4h máximo                                           ║
╚═══════════════╤══════════════════════════════════════════════════╝
                │
                ▼
╔══════════════════════════════════════════════════════════════════╗
║  SCOPE + ASSUMPTIONS                                            ║
║  • Inclusiones / Exclusiones / Profundidad                      ║
║  • Timebox (1-40h) + Deadline (YYYY-MM-DD)                      ║
║  • Completion criteria observables                              ║
║  • Assumptions (≥1 con type, confidence, impact, validation)    ║
║  • Output: Plan ejecutable con boundaries                       ║
╚═══════════════╤══════════════════════════════════════════════════╝
                │
                ▼
╔══════════════════════════════════════════════════════════════════╗
║  EJECUCIÓN (Source → Evidence → Analysis → Experiment)          ║
║                                                                  ║
║  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐  ║
║  │ Sources  │───▶│ Evidence │───▶│ Analysis │───▶│ Experiment│  ║
║  └──────────┘    └──────────┘    └──────────┘    └──────────┘  ║
║       ▲               │               │               │         ║
║       └───────────────┴───── loop-back ┴───────────────┘         ║
║                                                                  ║
║  • Checkpoint 80%: evaluar progreso y decidir                   ║
║  • Cada resultado registrado con 8 campos obligatorios          ║
║  • Assumptions monitoreadas — invalidación trigger reassessment ║
╚═══════════════╤══════════════════════════════════════════════════╝
                │
                ▼
╔══════════════════════════════════════════════════════════════════╗
║  SÍNTESIS                                                        ║
║  • Findings consolidados (cada question tiene ≥1 finding)       ║
║  • Conclusion trazable a evidencia                              ║
║  • Uncertainty section obligatoria                              ║
║  • Review humano → approved / rework                            ║
║                                                                  ║
║  Si rework: loop-back a etapa identificada (máx 3 ciclos)       ║
╚═══════════════╤══════════════════════════════════════════════════╝
                │
                ▼
╔══════════════════════════════════════════════════════════════════╗
║  VALOR                                                           ║
║  • Asset extraction (≥1 activo o justificación de ausencia)     ║
║  • Product Hypothesis (si hay señales — no forzar)              ║
║  • Publication / Archive                                         ║
║  • Feedback → posibles nuevos Research_Briefs                   ║
╚══════════════════════════════════════════════════════════════════╝
```

### Puntos de decisión en el flujo

| Punto | Condición | Opciones |
|-------|-----------|----------|
| Post-Problem Framing | ¿El statement genera ≥1 question? | Avanzar / Reformular framing |
| Post-Scope | ¿Timebox definido? ¿Criteria claros? | Avanzar / Ajustar scope |
| Checkpoint 80% | ≥80% timebox consumido sin conclusión | Extender / Reducir / Concluir parcial |
| Timebox 100% | Timebox agotado completamente | Concluir / Extender (máx 2) / Reducir |
| Loop-back ×3 | Misma etapa visitada 3 veces | Continuar / Pivotar / Cerrar |
| Assumption invalidada | Evidencia contradice assumption | Reassess findings / Ajustar scope |
| Review no aprobado | Checklist con deficiencias | Rework (máx 3 ciclos) / Completar con limitaciones / Abandonar |
| Completion criteria met | Criteria cumplidos antes de timebox | Avanzar a Conclusion (≤48h) |

---

## Referencias internas

- [002-research-lifecycle.md](./002-research-lifecycle.md) — Lifecycle completo con 16 etapas, estados y transiciones
- [004-research-question-framework.md](./004-research-question-framework.md) — Framework de formulación y calidad de preguntas
- [006-evidence-framework.md](./006-evidence-framework.md) — Categorías de evidencia y escala de confianza
- [015-research-journal.md](./015-research-journal.md) — Donde se registran loop-backs y decisiones
- [016-decision-log.md](./016-decision-log.md) — Donde se documentan decisiones de timebox y escalación
- [020-quality-gates.md](./020-quality-gates.md) — Quality gates que gobiernan transiciones

---

## Tabla epistémica

| Clasificación | Cantidad | Descripción |
|---------------|----------|-------------|
| [Decisión] | 1 | Este documento completo es una decisión de diseño del workflow operativo |
