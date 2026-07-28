# 002 — Research Lifecycle

> **Etiqueta epistémica:** [Decisión]
>
> **Requirements cubiertos:** R2.1, R2.2, R26.1, R26.2, R26.3, R26.4, R26.5, R26.6, R26.7

## Propósito

Este documento define las **16 etapas secuenciales** del Research_Lifecycle de LabOS, incluyendo para cada etapa sus inputs, actividades, outputs, quality gates, responsable y herramientas. Define además el **modelo de estados** con transiciones permitidas, criterios de avance, reglas de loop-back y duraciones máximas recomendadas.

El Research_Lifecycle transforma una entrada inicial (pregunta, problema, idea, incidente, observación, oportunidad, documento, dataset) en una salida de valor: conclusión validada, activo reutilizable y, opcionalmente, hipótesis de producto.

---

## Tabla de contenidos

1. [Lifecycle completo — 16 etapas](#lifecycle-completo--16-etapas)
2. [Modelo de estados](#modelo-de-estados)
3. [Transiciones permitidas](#transiciones-permitidas)
4. [Criterios de transición](#criterios-de-transición)
5. [Reglas de loop-back](#reglas-de-loop-back)
6. [Duración máxima por etapa y escalación](#duración-máxima-por-etapa-y-escalación)
7. [Artefactos mínimos por effort category](#artefactos-mínimos-por-effort-category)
8. [Diagrama de flujo](#diagrama-de-flujo)

---

## Lifecycle completo — 16 etapas

El lifecycle define 16 etapas secuenciales con posibilidad de loop-back documentado.

### Etapa 1: Intake

| Campo | Valor |
|-------|-------|
| **Propósito** | Capturar el trigger de investigación y realizar clasificación inicial |
| **Inputs** | Pregunta, problema, idea, incidente, observación, oportunidad, documento, dataset |
| **Actividades** | Identificar trigger, clasificar tipo de entrada, estimar esfuerzo, crear Research_Brief inicial |
| **Outputs** | Research_Brief (borrador) con trigger, contexto, clasificación de dominio, effort category |
| **Responsable** | Fundador |
| **Herramientas** | ChatGPT Projects (contextualización), GitHub (registro), Obsidian (captura rápida) |
| **Quality Gate** | Research_Brief existe con todos los campos obligatorios completos según effort category |
| **Estado resultante** | Proposed |

---

### Etapa 2: Problem Framing

| Campo | Valor |
|-------|-------|
| **Propósito** | Articular el problema core separando síntomas de causas raíz |
| **Inputs** | Research_Brief (borrador) |
| **Actividades** | Documentar problema, identificar síntomas vs causa raíz, definir contexto afectado, stakeholders |
| **Outputs** | Problem statement con: síntomas, causa probable, contexto, stakeholders, constraints |
| **Responsable** | Fundador |
| **Herramientas** | ChatGPT Projects (debate estructurado), Obsidian (conexiones conceptuales) |
| **Quality Gate** | Problem statement es suficientemente específico para generar ≥1 research question |
| **Estado resultante** | Framed |

---

### Etapa 3: Research Question

| Campo | Valor |
|-------|-------|
| **Propósito** | Formular preguntas de investigación verificables y time-bounded |
| **Inputs** | Problem statement documentado |
| **Actividades** | Formular pregunta principal, descomponer en sub-preguntas si es compleja, evaluar calidad |
| **Outputs** | Research question(s) con: subject, scope, constraints, answer type, verification method |
| **Responsable** | Fundador |
| **Herramientas** | ChatGPT Projects (refinamiento), Obsidian (mapeo de relaciones) |
| **Quality Gate** | Todas las preguntas pasan criterios de calidad: specificity, answerability, relevance, time-boundedness |
| **Estado resultante** | Framed |


---

### Etapa 4: Scope

| Campo | Valor |
|-------|-------|
| **Propósito** | Delimitar alcance, timebox y criterios de finalización |
| **Inputs** | Research questions aprobadas |
| **Actividades** | Definir inclusiones/exclusiones, timebox, deadline, completion criteria, max sources |
| **Outputs** | Scope document con boundaries, timebox, deadline, exit criteria |
| **Responsable** | Fundador |
| **Herramientas** | GitHub (registro formal), ChatGPT Projects (estimación de esfuerzo) |
| **Quality Gate** | Timebox definido, completion criteria explícitos, exclusiones documentadas |
| **Estado resultante** | Planned |

---

### Etapa 5: Assumptions

| Campo | Valor |
|-------|-------|
| **Propósito** | Surfacear premisas ocultas antes de invertir esfuerzo investigativo |
| **Inputs** | Scope definido, research questions |
| **Actividades** | Listar assumptions, clasificar por tipo, evaluar confianza, documentar impacto si incorrectas |
| **Outputs** | Assumptions register con: statement, type, confidence, impact-if-wrong, validation approach |
| **Responsable** | Fundador |
| **Herramientas** | ChatGPT Projects (challenge de assumptions), Obsidian (registro) |
| **Quality Gate** | ≥1 assumption documentada con confidence level y validation plan (≥3 recomendado para investigaciones Large), o justificación explícita de ausencia |
| **Estado resultante** | Planned |

---

### Etapa 6: Source Collection

| Campo | Valor |
|-------|-------|
| **Propósito** | Recopilar y registrar fuentes relevantes con evaluación de calidad |
| **Inputs** | Research questions, scope, assumptions |
| **Actividades** | Buscar fuentes, evaluar calidad contra 10 criterios, registrar en Source_Register, clasificar por tipo |
| **Outputs** | Source_Register poblado con fuentes evaluadas, gaps de fuentes documentados |
| **Responsable** | Fundador |
| **Herramientas** | NotebookLM (consulta documental), ChatGPT Projects (búsqueda contextual), Deepnote (datasets), GitHub (registro) |
| **Quality Gate** | ≥1 fuente con calidad suficiente (score ≥6) para cada research question, gaps documentados |
| **Estado resultante** | In Progress |


---

### Etapa 7: Evidence Evaluation

| Campo | Valor |
|-------|-------|
| **Propósito** | Clasificar y evaluar evidencia extraída de las fuentes |
| **Inputs** | Source_Register poblado |
| **Actividades** | Extraer claims de fuentes, clasificar evidencia por categoría, asignar confidence level, documentar limitaciones, identificar conflictos |
| **Outputs** | Evidence register con: claims, categories, confidence levels, limitations, conflicts |
| **Responsable** | Fundador |
| **Herramientas** | NotebookLM (comparación de fuentes), Deepnote (análisis cuantitativo), Obsidian (mapeo) |
| **Quality Gate** | Toda evidencia clasificada, conflictos documentados, ningún AI output sin verificación tratado como Primary_Evidence |
| **Estado resultante** | In Progress |

---

### Etapa 8: Analysis

| Campo | Valor |
|-------|-------|
| **Propósito** | Sintetizar evidencia, identificar patrones y formular hipótesis |
| **Inputs** | Evidence register evaluado |
| **Actividades** | Analizar patrones, comparar evidencia, formular hipótesis, identificar gaps, triangular fuentes |
| **Outputs** | Análisis documentado con: patrones identificados, hipótesis formuladas, gaps, preguntas emergentes |
| **Responsable** | Fundador |
| **Herramientas** | Deepnote (análisis cuantitativo), NotebookLM (síntesis), ChatGPT Projects (debate), Obsidian (mapeo conceptual) |
| **Quality Gate** | Análisis responde (parcial o totalmente) a las research questions, hipótesis formuladas correctamente |
| **Estado resultante** | In Progress |

---

### Etapa 9: Experimentation

| Campo | Valor |
|-------|-------|
| **Propósito** | Validar hipótesis mediante experimentos controlados o métodos alternativos |
| **Inputs** | Hipótesis formuladas, protocol de experimento |
| **Actividades** | Ejecutar experimento según protocol, registrar resultados, documentar desviaciones, evaluar outcomes |
| **Outputs** | Experiment records con: resultados, desviaciones, decisiones, evidencia generada |
| **Responsable** | Fundador |
| **Herramientas** | Deepnote (notebooks), GitHub (código, datos), herramientas específicas del dominio |
| **Quality Gate** | Resultados documentados (positivos, negativos o inconclusos), hypothesis actualizada con verdict |
| **Estado resultante** | In Progress |
| **Nota** | Etapa opcional si el dominio no permite experimentación controlada; en ese caso, usar métodos alternativos documentados en [022-domain-specific-adaptations.md](./022-domain-specific-adaptations.md) |


---

### Etapa 10: Findings

| Campo | Valor |
|-------|-------|
| **Propósito** | Consolidar todos los resultados en hallazgos interpretables |
| **Inputs** | Evidence register, experiment records, analysis output |
| **Actividades** | Sintetizar hallazgos, clasificar por tipo y confianza, documentar relación con research questions |
| **Outputs** | Findings document con: hallazgos clasificados, confidence levels, relación con questions |
| **Responsable** | Fundador |
| **Herramientas** | Obsidian (síntesis), ChatGPT Projects (revisión), GitHub (documentación formal) |
| **Quality Gate** | Cada research question tiene al menos un finding asociado (aunque sea "insuficiente evidencia") |
| **Estado resultante** | In Progress |

---

### Etapa 11: Conclusion

| Campo | Valor |
|-------|-------|
| **Propósito** | Formular conclusiones trazables que respondan las research questions |
| **Inputs** | Findings consolidados |
| **Actividades** | Redactar conclusión, trazar a evidencia, clasificar confidence, documentar limitaciones, formular recomendaciones |
| **Outputs** | Conclusion document con: question answered, evidence summary, confidence, limitations, implications, actions, open questions |
| **Responsable** | Fundador |
| **Herramientas** | ChatGPT Projects (refinamiento), Obsidian (conexión a conocimiento), GitHub (documento formal) |
| **Quality Gate** | Conclusión trazable a ≥1 evidencia, limitaciones documentadas, uncertainty section presente |
| **Estado resultante** | Under Review |

---

### Etapa 12: Review

| Campo | Valor |
|-------|-------|
| **Propósito** | Validar calidad, completitud y compliance de la investigación |
| **Inputs** | Conclusion, Research_Journal, Source_Register, todos los artefactos |
| **Actividades** | Evaluar contra checklist de revisión, verificar trazabilidad, validar compliance ético, confirmar human review |
| **Outputs** | Review result: approved, approved-with-limitations, o requires-rework |
| **Responsable** | Fundador (human review obligatorio) |
| **Herramientas** | GitHub (review formal), checklist de [020-quality-gates.md](./020-quality-gates.md) |
| **Quality Gate** | Checklist completado, deficiencias documentadas y remediadas si aplica |
| **Estado resultante** | Completed (si aprobado), In Progress (si requiere rework) |


---

### Etapa 13: Asset Extraction

| Campo | Valor |
|-------|-------|
| **Propósito** | Extraer activos reutilizables de la investigación completada |
| **Inputs** | Investigación aprobada en Review |
| **Actividades** | Identificar activos extraíbles, clasificar por tipo, documentar metadata, ejecutar handoff a repository |
| **Outputs** | ≥1 Research_Asset con: name, type, description, usage hypothesis, target audience, source reference, state |
| **Responsable** | Fundador |
| **Herramientas** | GitHub (assets repository), Obsidian (conexiones), Kiro (spec si el activo requiere implementación) |
| **Quality Gate** | Asset cumple quality criteria mínimos, metadata completa, trazabilidad a investigación fuente |
| **Estado resultante** | Converted to Asset |

---

### Etapa 14: Product Hypothesis

| Campo | Valor |
|-------|-------|
| **Propósito** | Evaluar si existe una oportunidad comercial derivada de la investigación |
| **Inputs** | Assets extraídos, conclusions, evidence of demand |
| **Actividades** | Evaluar oportunidad, formular Product_Hypothesis o Revenue_Hypothesis si evidencia lo soporta, documentar ausencia de señal comercial si no |
| **Outputs** | Product_Hypothesis (si aplica) o declaración documentada de ausencia de oportunidad comercial |
| **Responsable** | Fundador |
| **Herramientas** | ChatGPT Projects (análisis de mercado), GitHub (documentación), Obsidian (conexiones) |
| **Quality Gate** | Si se formula hypothesis: todos los campos requeridos completos, evidencia referenciada. Si no se formula: justificación documentada |
| **Estado resultante** | Converted to Asset (sin hypothesis) o Published (si hypothesis pasa gate comercial) |
| **Nota** | Etapa que permite concluir sin producto comercial. No fuerza monetización. Ver [019-research-to-product-hypothesis.md](./019-research-to-product-hypothesis.md) |

---

### Etapa 15: Publication or Archive

| Campo | Valor |
|-------|-------|
| **Propósito** | Decidir destino final: publicación externa, archivo interno, o ambos |
| **Inputs** | Investigación completa con assets y hypothesis (si aplica) |
| **Actividades** | Evaluar idoneidad para publicación, preparar para archivo, verificar privacy/IP compliance |
| **Outputs** | Decisión de publicación/archivo documentada, assets en repositorio final |
| **Responsable** | Fundador |
| **Herramientas** | GitHub (versionado final), Obsidian (índice de conocimiento) |
| **Quality Gate** | Privacy/IP checklist aprobado, formato adecuado para destino |
| **Estado resultante** | Published o Archived |


---

### Etapa 16: Feedback and Iteration

| Campo | Valor |
|-------|-------|
| **Propósito** | Capturar feedback, identificar mejoras y alimentar futuras investigaciones |
| **Inputs** | Investigación publicada/archivada, feedback externo o interno |
| **Actividades** | Registrar feedback, identificar mejoras al proceso, documentar preguntas derivadas, actualizar métricas |
| **Outputs** | Feedback record, potential new Research_Briefs, process improvement notes |
| **Responsable** | Fundador |
| **Herramientas** | Obsidian (conexiones), GitHub (issues), ChatGPT Projects (reflexión) |
| **Quality Gate** | Feedback registrado, métricas actualizadas |
| **Estado resultante** | Archived (estado final estable) |

---

## Modelo de estados

### Estados de una investigación

| Estado | Descripción | Etapa(s) del lifecycle |
|--------|-------------|----------------------|
| **Proposed** | Intake completado, Research_Brief creado | Intake |
| **Framed** | Problema articulado, research questions formuladas | Problem Framing, Research Question |
| **Planned** | Scope definido, timebox asignado, assumptions documentadas | Scope, Assumptions |
| **In Progress** | Trabajo investigativo activo | Source Collection → Findings |
| **Blocked** | Investigación detenida por dependencia externa, falta de acceso, o decisión pendiente | Cualquier etapa |
| **Under Review** | Conclusión formulada, pendiente revisión humana | Conclusion, Review |
| **Completed** | Review aprobado, conclusión aceptada | Review (aprobado) |
| **Converted to Asset** | ≥1 activo extraído y registrado en repository | Asset Extraction |
| **Published** | Investigación o activos compartidos externamente | Publication |
| **Archived** | Investigación almacenada como referencia, ciclo cerrado | Archive, Feedback |
| **Rejected** | Investigación abandonada antes de conclusión con justificación documentada | Cualquier etapa |


---

## Transiciones permitidas

```text
Proposed → Framed              (problem framing completado)
Framed → Planned               (scope y assumptions definidos)
Planned → In Progress          (quality gate de inicio aprobado)
In Progress → In Progress      (avance entre etapas 6-10)
In Progress → Blocked          (dependencia o decisión pendiente)
Blocked → In Progress          (blocker resuelto)
In Progress → Under Review     (conclusión formulada)
Under Review → Completed       (review aprobado)
Under Review → In Progress     (review requiere rework)
Completed → Converted to Asset (asset extraído)
Converted to Asset → Published (publication gate aprobado)
Converted to Asset → Archived  (sin publicación, archivo directo)
Published → Archived           (ciclo completo)
[Cualquier estado] → Rejected  (abandono con justificación)
[Cualquier estado] → Blocked   (blocker externo detectado)
```

### Transiciones NO permitidas

- No se puede avanzar de Proposed directamente a In Progress (debe pasar por Framed → Planned).
- No se puede retroceder de Completed a In Progress (requiere nueva investigación).
- No se puede pasar de Rejected a ningún otro estado (terminal).
- No se puede pasar de Archived a estados activos (terminal, requiere nueva investigación referenciando la anterior).

---

## Criterios de transición

| Transición | Criterio |
|------------|----------|
| Proposed → Framed | Research_Brief completo + problem statement documentado + ≥1 research question formulada |
| Framed → Planned | Scope definido con timebox + assumptions documentadas (≥1 o justificación explícita de ausencia) |
| Planned → In Progress | Quality gate de inicio aprobado: Research_Brief, questions, scope, timebox, assumptions verificados |
| In Progress → Under Review | Conclusión formulada con trazabilidad a evidencia + uncertainty documented |
| Under Review → Completed | Human review aprobado, checklist satisfecho (≥6/8 items pass) |
| Under Review → In Progress | Review identifica deficiencias remediables, máx 3 ciclos de remediación |
| Completed → Converted to Asset | ≥1 asset extraído con metadata completa (name, type, description, usage hypothesis, state) |
| Converted to Asset → Published | Privacy/IP checklist aprobado + formato de publicación listo |
| [Cualquier] → Rejected | Justificación documentada + partial findings preservados si existen |
| [Cualquier] → Blocked | Blocker identificado + fecha estimada de resolución + impacto documentado |
| Blocked → In Progress | Blocker resuelto + documentación de resolución |


---

## Reglas de loop-back

El lifecycle soporta progresión no-lineal cuando las condiciones lo requieren. Todo loop-back debe documentarse formalmente.

### Requisitos para ejecutar un loop-back

Cada retorno a una etapa previa requiere documentar:

1. **Condición triggering** — qué evento o hallazgo invalida el output de la etapa actual
2. **Etapa destino** — a qué etapa se retorna
3. **Razón de insuficiencia** — por qué el output actual es insuficiente (1-3 oraciones)
4. **Outcome esperado** — qué se espera obtener al repetir la etapa destino

### Loop-backs comunes permitidos

| Desde | Hacia | Condición típica |
|-------|-------|-----------------|
| Evidence Evaluation | Source Collection | Fuentes insuficientes o gaps críticos detectados |
| Analysis | Evidence Evaluation | Conflictos no resueltos requieren re-evaluación |
| Analysis | Source Collection | Nuevas preguntas requieren fuentes adicionales |
| Experimentation | Analysis | Resultados inconclusos requieren nueva síntesis |
| Findings | Analysis | Hallazgos no responden las research questions |
| Conclusion | Findings | Evidencia insuficiente para soportar conclusión |
| Review | In Progress (cualquier etapa 6-10) | Deficiencias identificadas durante review |
| Research Question | Problem Framing | Pregunta no formulable con el framing actual |
| Scope | Research Question | Questions no caben en timebox razonable |

### Límite de loop-back

Si una investigación ejecuta loop-back **a la misma etapa más de 3 veces**, el Fundador debe registrar un Decision_Log entry con una de las siguientes resoluciones:

- **Continuar** — con justificación explícita de por qué esta iteración será diferente
- **Pivotar** — reformular la research question o el approach
- **Cerrar** — cerrar la investigación con closure rationale y clasificar como Rejected

### Registro de loop-back

Cada loop-back se registra en el Research_Journal con los siguientes campos:

- Fecha
- Etapa origen
- Etapa destino
- Condición triggering
- Razón de insuficiencia
- Outcome esperado
- Número de iteración (1ª, 2ª, 3ª vez a esta etapa)


---

## Duración máxima por etapa y escalación

Cada etapa tiene una duración máxima recomendada. Cuando se excede, se activa el protocolo de escalación.

### Duraciones máximas recomendadas

| # | Etapa | Duración máxima | Notas |
|---|-------|----------------|-------|
| 1 | Intake | 2 horas | Clasificación rápida, no investigar |
| 2 | Problem Framing | 4 horas | Si no se articula en 4h, el problema es demasiado amplio |
| 3 | Research Question | 4 horas | Incluye hasta 3 intentos de reformulación |
| 4 | Scope | 2 horas | Decisión de boundaries, no investigación |
| 5 | Assumptions | 2 horas | Surfacing, no validación |
| 6 | Source Collection | 8 horas | Proporcional al scope definido |
| 7 | Evidence Evaluation | 8 horas | Clasificación y evaluación |
| 8 | Analysis | 16 horas | Etapa más intensiva de síntesis |
| 9 | Experimentation | 40 horas (máx 90 días calendario) | Depende del tipo de experimento |
| 10 | Findings | 4 horas | Consolidación de resultados |
| 11 | Conclusion | 4 horas | Síntesis final |
| 12 | Review | 4 horas (máx 14 días calendario) | Incluye tiempo de espera por reviewer |
| 13 | Asset Extraction | 4 horas | Handoff documentado |
| 14 | Product Hypothesis | 4 horas | Evaluación de oportunidad |
| 15 | Publication or Archive | 2 horas | Decisión y preparación |
| 16 | Feedback and Iteration | 2 horas | Registro y cierre |

### Protocolo de escalación

Cuando una etapa excede su duración máxima recomendada, el Fundador ejecuta el siguiente protocolo:

1. **Revisar progreso** — documentar qué se ha avanzado y qué falta
2. **Documentar blocker** — identificar por qué no se ha completado la etapa
3. **Decidir** — elegir una de las tres opciones:

| Opción | Acción requerida |
|--------|-----------------|
| **Extender** | Registrar nueva deadline con justificación. La extensión no puede exceder el doble de la duración original |
| **Saltar etapa** | Documentar rationale de por qué la etapa puede omitirse sin comprometer la investigación. Solo aplicable a etapas opcionales (Experimentation, Product Hypothesis) |
| **Cerrar investigación** | Clasificar como Rejected con closure rationale, preservar partial findings |

La decisión de escalación se registra en el Decision_Log.


---

## Artefactos mínimos por effort category

La cantidad de artefactos requeridos varía según la categoría de esfuerzo estimada en el Intake.

| Effort Category | Artefactos obligatorios | Artefactos opcionales |
|-----------------|------------------------|----------------------|
| **Small** (<4h) | Research_Brief (lightweight), Conclusion | Journal, Source_Register |
| **Medium** (4-16h) | Research_Brief, Source_Register, Conclusion, Research_Journal, Asset Handoff | Experiment Record, Decision_Log |
| **Large** (>16h) | Todos los artefactos: Research_Brief, Research Plan, Source_Register, Evidence register, Experiment Record, Research_Journal, Decision_Log, Conclusion, Asset Handoff, Research Review | — |

### Reglas de artefactos

- **Small (<4h):** El Research_Brief puede ser lightweight (solo trigger, requester, expected value, origin type). La conclusión puede ser breve (1-2 párrafos) pero debe ser trazable a al menos 1 fuente.
- **Medium (4-16h):** Requiere Source_Register con evaluación de calidad. El Research_Journal es obligatorio por superar el umbral de 4h. El Asset Handoff documenta al menos 1 activo extraído.
- **Large (>16h):** Todos los artefactos son obligatorios. La investigación debe pasar por todas las etapas del lifecycle sin omisiones (excepto Experimentation si el dominio no lo permite, con justificación documentada).

### Regla de re-clasificación

Si durante la investigación el esfuerzo real supera la categoría estimada:
- De Small a Medium: crear Source_Register y Research_Journal retroactivamente (reconstrucción permitida)
- De Medium a Large: crear artefactos faltantes antes de avanzar a Conclusion

La re-clasificación se registra en el Decision_Log con justificación.

---

## Diagrama de flujo

```text
[Trigger]
    │
    ▼
┌─────────────┐
│  1. Intake  │──────────────────────────────► Proposed
└─────┬───────┘
      │
      ▼
┌──────────────────┐
│ 2. Problem       │
│    Framing       │─────────────────────────► Framed
└─────┬────────────┘
      │
      ▼
┌──────────────────┐
│ 3. Research      │
│    Question      │─────────────────────────► Framed
└─────┬────────────┘
      │
      ▼
┌─────────────┐
│  4. Scope   │──────────────────────────────► Planned
└─────┬───────┘
      │
      ▼
┌──────────────────┐
│ 5. Assumptions   │─────────────────────────► Planned
└─────┬────────────┘
      │
      ▼
┌──────────────────┐      ◄── loop-back ──┐
│ 6. Source        │                       │
│    Collection    │───┐                   │
└──────────────────┘   │                   │
      │                │                   │
      ▼                │                   │
┌──────────────────┐   │                   │
│ 7. Evidence      │   │   In Progress     │
│    Evaluation    │   │                   │
└──────────────────┘   │                   │
      │                │                   │
      ▼                │                   │
┌──────────────────┐   │                   │
│ 8. Analysis      │◄──┘                   │
└──────────────────┘                       │
      │                                    │
      ▼                                    │
┌──────────────────┐                       │
│ 9. Experiment-   │ (opcional)            │
│    ation         │                       │
└──────────────────┘                       │
      │                                    │
      ▼                                    │
┌──────────────────┐                       │
│ 10. Findings     │───────────────────────┘
└─────┬────────────┘
      │
      ▼
┌──────────────────┐
│ 11. Conclusion   │─────────────────────────► Under Review
└─────┬────────────┘
      │
      ▼
┌──────────────────┐     rework
│ 12. Review       │──────────────────────────► In Progress
└─────┬────────────┘                              (loop-back)
      │ approved
      ▼
┌──────────────────┐
│ 13. Asset        │─────────────────────────► Converted to Asset
│    Extraction    │
└─────┬────────────┘
      │
      ▼
┌──────────────────┐
│ 14. Product      │ (evaluación, no fuerza monetización)
│    Hypothesis    │
└─────┬────────────┘
      │
      ▼
┌──────────────────┐
│ 15. Publication  │─────────────────────────► Published / Archived
│    or Archive    │
└─────┬────────────┘
      │
      ▼
┌──────────────────┐
│ 16. Feedback     │─────────────────────────► Archived (final)
│    and Iteration │
└──────────────────┘
```

---

## Referencias internas

- [001-research-principles.md](./001-research-principles.md) — Principios que aplican a todas las etapas
- [008-research-workflow.md](./008-research-workflow.md) — Workflow operativo detallado con timebox y loop-back
- [020-quality-gates.md](./020-quality-gates.md) — Quality gates detallados con checklists
- [022-domain-specific-adaptations.md](./022-domain-specific-adaptations.md) — Adaptaciones por dominio que modifican etapas opcionales
- [023-research-metrics.md](./023-research-metrics.md) — Métricas que se alimentan del lifecycle

---

## Tabla epistémica

| Clasificación | Cantidad | Descripción |
|---------------|----------|-------------|
| [Decisión] | 1 | Este documento completo es una decisión de diseño del lifecycle |
