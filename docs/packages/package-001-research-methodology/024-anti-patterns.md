# 024 — Anti-Patterns

> **Etiqueta epistémica:** [Decisión]
>
> **Requirements cubiertos:** R30.1, R30.2, R30.3, R30.4

## Propósito

Este documento identifica y documenta los **anti-patrones de investigación** más comunes dentro de LabOS — prácticas que parecen razonables pero que degradan la calidad, trazabilidad o valor de una investigación. Se organizan en dos categorías: **generales** (aplicables a toda investigación) y **específicos de AI** (relevantes cuando herramientas de inteligencia artificial participan en el proceso).

Cada anti-patrón se mapea a las etapas del [Research Lifecycle](./002-research-lifecycle.md) donde es más probable que ocurra. Al final del documento se provee un **checklist de detección por etapa** para uso en quality gates y revisiones.

---

## Tabla de contenidos

1. [Anti-patrones generales](#anti-patrones-generales)
2. [Anti-patrones específicos de AI](#anti-patrones-específicos-de-ai)
3. [Mapeo a lifecycle stages](#mapeo-a-lifecycle-stages)
4. [Checklist de detección por stage](#checklist-de-detección-por-stage)
5. [Referencias](#referencias)

---

## Anti-patrones generales

### AP-G01: Documentación como validación

| Campo | Valor |
|-------|-------|
| **Nombre** | Documentation as Validated Knowledge |
| **Descripción** | Tratar documentación extensa como sinónimo de conocimiento validado. El hecho de que algo esté documentado en detalle no implica que haya sido verificado contra evidencia independiente o que sus conclusiones sean correctas. La exhaustividad documental se confunde con rigor investigativo. |
| **Síntomas** | (1) Documentos extensos sin una sola referencia a fuentes primarias verificadas. (2) Ausencia de uncertainty section o sección de limitaciones a pesar de conclusiones definitivas. (3) Revisiones que evalúan formato y completitud pero no verifican claims contra evidencia. |
| **Consecuencias** | Conclusiones potencialmente falsas se integran al sistema de conocimiento como hechos, contaminando decisiones downstream y activos derivados. |
| **Corrección** | Exigir que toda conclusión trace a ≥1 entrada del Source_Register con calidad evaluada. Incluir uncertainty section obligatoria en todos los documentos con conclusiones. |
| **Stages** | Evidence Evaluation, Conclusion, Review |

---

### AP-G02: AI como evidencia primaria

| Campo | Valor |
|-------|-------|
| **Nombre** | AI Output as Primary Evidence |
| **Descripción** | Tratar respuestas generadas por herramientas de IA (ChatGPT, NotebookLM, etc.) como Primary_Evidence sin verificación independiente contra fuentes originales. Las respuestas de IA son AI_Generated_Content con un techo de confidence level 3 hasta que se verifican. |
| **Síntomas** | (1) Findings que citan "según ChatGPT" o "NotebookLM indica" como fuente de evidencia. (2) Confidence levels de 4 o 5 asignados a contenido sin verificación humana. (3) Ausencia de fuentes primarias en el Source_Register a pesar de múltiples claims factuales. |
| **Consecuencias** | Investigaciones construidas sobre una base no verificada; conclusiones que no resisten escrutinio externo; riesgo de hallucinations incorporadas como conocimiento validado. |
| **Corrección** | Aplicar Regla R22.2: verificar toda afirmación factual contra fuente primaria independiente. Clasificar todo output de IA como AI_Generated_Content y respetar el techo de confidence level. |
| **Stages** | Source Collection, Evidence Evaluation, Analysis |

---

### AP-G03: Validación sin criterios explícitos

| Campo | Valor |
|-------|-------|
| **Nombre** | Validation Without Explicit Criteria |
| **Descripción** | Declarar que una hipótesis, conclusión o activo "está validado" sin haber definido previamente los criterios de éxito y fracaso. La validación se reduce a una aprobación subjetiva sin un estándar observable contra el cual medir. |
| **Síntomas** | (1) Hipótesis marcadas como "validadas" sin success criterion documentado antes del experimento. (2) Quality gates aprobados sin checklist explícito de criterios a verificar. (3) Uso de lenguaje vago como "se validó satisfactoriamente" sin métricas. |
| **Consecuencias** | Imposibilidad de distinguir entre hipótesis realmente confirmadas y suposiciones no desafiadas; quality gates que no filtran deficiencias reales. |
| **Corrección** | Definir success criterion y failure criterion antes de iniciar validación (R10.1). Utilizar quality gates con checklists explícitos (020-quality-gates.md). No marcar "validado" sin evidencia que satisfaga los criterios predefinidos. |
| **Stages** | Experimentation, Conclusion, Review |

---

### AP-G04: Investigación indefinida

| Campo | Valor |
|-------|-------|
| **Nombre** | Indefinite Research Without Closure |
| **Descripción** | Conducir investigación sin timebox ni completion criteria definidos, permitiendo que la investigación se extienda indefinidamente sin producir conclusiones. La ausencia de presión temporal elimina el incentivo para sintetizar y concluir. |
| **Síntomas** | (1) Investigaciones sin deadline ni timebox documentado en el scope. (2) Investigaciones que superan el 200% del timebox original sin decisión de extensión, reducción o cierre registrada. (3) Acumulación continua de fuentes sin avance hacia análisis o conclusión. |
| **Consecuencias** | Recursos consumidos sin retorno; oportunidad temporal perdida; investigaciones que nunca producen activos reutilizables ni alimentan decisiones. |
| **Corrección** | Exigir timebox y completion criteria en Etapa 4 (Scope). Activar protocolo de escalación al 80% del timebox (R5.3). Registrar decisión formal si se excede el timebox. |
| **Stages** | Scope, Source Collection, Analysis |

---

### AP-G05: Monetización automática

| Campo | Valor |
|-------|-------|
| **Nombre** | Forced Monetization of Research |
| **Descripción** | Convertir automáticamente toda investigación completada en un producto comercial sin evaluar si la evidencia soporta una hipótesis de demanda. La presión por monetizar distorsiona la investigación y fuerza conclusiones prematuras sobre viabilidad comercial. |
| **Síntomas** | (1) Product Hypotheses formuladas sin evidencia de demanda en el Source_Register. (2) Todas las investigaciones producen un "producto" independientemente de la naturaleza de los hallazgos. (3) Revenue Hypotheses sin variable de validación ni método para medir demanda real. |
| **Consecuencias** | Inversión de tiempo en productos sin demanda verificada; dilución de esfuerzo entre demasiadas iniciativas comerciales no validadas; distorsión del proceso investigativo hacia conclusiones comercialmente convenientes. |
| **Corrección** | Aplicar Etapa 14 como evaluación, no como mandato. Documentar explícitamente cuando no existe señal comercial (R31). Requerir evidencia de demanda antes de formular Product_Hypothesis. |
| **Stages** | Asset Extraction, Product Hypothesis |

---

### AP-G06: Actividad como progreso

| Campo | Valor |
|-------|-------|
| **Nombre** | Activity Confused With Progress |
| **Descripción** | Medir progreso investigativo por horas invertidas, fuentes consultadas o documentos producidos en lugar de por preguntas respondidas, hipótesis validadas/refutadas o conclusiones formuladas. La actividad genera sensación de avance sin progreso real hacia los objetivos. |
| **Síntomas** | (1) Research Journal con muchas entradas de actividad pero sin findings ni decisiones registradas. (2) Source_Register con decenas de fuentes pero sin evidencia evaluada contra las research questions. (3) Etapas completadas "por calendario" sin que sus quality gates estén realmente satisfechos. |
| **Consecuencias** | Timebox consumido sin responder las research questions; falsa sensación de productividad que retrasa decisiones de cierre o pivote; activos que no resisten revisión de calidad. |
| **Corrección** | Medir progreso por research questions respondidas y quality gates satisfechos, no por volumen de trabajo. Revisar al 50% del timebox si los findings responden (parcial o totalmente) a las questions. |
| **Stages** | Source Collection, Evidence Evaluation, Analysis, Findings |

---

### AP-G07: Resultados negativos ignorados

| Campo | Valor |
|-------|-------|
| **Nombre** | Ignoring Negative Results |
| **Descripción** | Descartar o no documentar resultados negativos (hipótesis refutadas, approaches fallidos, fuentes insuficientes) como si no tuvieran valor. Los resultados negativos son evidencia legítima que previene repetición de errores y refina el entendimiento del problema. |
| **Síntomas** | (1) Experiment records solo documentan éxitos; fracasos sin registro formal. (2) Hipótesis que "desaparecen" del registro sin verdict documentado. (3) Investigaciones previas que exploraron el mismo problema se repiten porque los findings negativos no se preservaron. |
| **Consecuencias** | Repetición de experimentos fallidos; pérdida de aprendizaje organizacional; sesgo de supervivencia en la base de conocimiento que distorsiona futuras investigaciones. |
| **Corrección** | Aplicar R11.2: documentar resultados negativos con los mismos campos obligatorios que los positivos. Preservar todos los experiment records independientemente del outcome. Incluir lessons learned en closure. |
| **Stages** | Experimentation, Findings, Conclusion |

---

### AP-G08: Scope creep silencioso

| Campo | Valor |
|-------|-------|
| **Nombre** | Silent Scope Creep |
| **Descripción** | Expandir progresivamente el alcance de una investigación sin documentar formalmente el cambio ni evaluar su impacto en timebox y deadline. Nuevas preguntas, fuentes adicionales o "investigaciones laterales" se incorporan sin pasar por el control de cambio de scope. |
| **Síntomas** | (1) Research questions adicionales aparecen en findings sin haber pasado por quality evaluation. (2) Source_Register contiene fuentes no relacionadas con las questions originales documentadas. (3) Timebox excedido sin registro de decisión de extensión o reducción. |
| **Consecuencias** | Investigación sin fin predecible; timebox sin significado real; conclusiones difusas que no responden a las preguntas originales con foco. |
| **Corrección** | Aplicar R5.4: todo cambio de scope requiere documentación del elemento modificado, razón e impacto en timebox/deadline. Las nuevas preguntas pasan por quality evaluation antes de incorporarse. |
| **Stages** | Source Collection, Analysis, Findings |

---

## Anti-patrones específicos de AI

### AP-AI01: Aceptación de resúmenes sin verificación

| Campo | Valor |
|-------|-------|
| **Nombre** | Accepting AI Summaries Unverified |
| **Descripción** | Aceptar resúmenes generados por herramientas de IA (ChatGPT, NotebookLM, etc.) como representaciones fieles de las fuentes originales sin verificar que el resumen refleje con precisión el contenido de la fuente. Los resúmenes de IA pueden omitir matices, invertir conclusiones o inventar detalles. |
| **Síntomas** | (1) Findings basados en "lo que NotebookLM resumió" sin consulta directa de la fuente citada. (2) Citas indirectas que no se verifican contra el texto original. (3) Discrepancias entre lo que el resumen de IA dice y lo que la fuente realmente afirma, descubiertas solo en review. |
| **Consecuencias** | Hallazgos construidos sobre representaciones distorsionadas de la evidencia; conclusiones que no resisten escrutinio cuando se consulta la fuente original; pérdida de confianza en el sistema de evidencia. |
| **Corrección** | Verificar claims específicos del resumen contra la fuente primaria. Registrar verificación como campo obligatorio en el Evidence Record. Nunca asignar confidence > 3 a contenido basado solo en resumen de IA. |
| **Stages** | Source Collection, Evidence Evaluation |

---

### AP-AI02: Confianza de IA como calidad de evidencia

| Campo | Valor |
|-------|-------|
| **Nombre** | AI Confidence as Evidence Quality |
| **Descripción** | Utilizar el nivel de "certeza" o "confianza" expresado por una herramienta de IA como proxy del confidence level real de la evidencia. Cuando una IA dice "estoy seguro de que X" o presenta información con tono asertivo, esto no incrementa la calidad epistémica real de la afirmación. |
| **Síntomas** | (1) Confidence levels asignados en base a cuán "seguro" suena el output de IA, no en base a la calidad de fuentes subyacentes. (2) Frases como "ChatGPT confirma con alta confianza" usadas para justificar niveles 4-5. (3) Ausencia de evaluación de fuentes independiente cuando la IA "ya lo verificó". |
| **Consecuencias** | Inflación artificial de confidence levels; quality gates aprobados con evidencia que no soporta el nivel declarado; degradación del rigor del Evidence Framework. |
| **Corrección** | Confidence levels se asignan exclusivamente según la escala del Evidence Framework (R8.2), basada en tipo de fuente, independencia y verificabilidad. El tono de la IA es irrelevante para la clasificación. |
| **Stages** | Evidence Evaluation, Analysis, Conclusion |

---

### AP-AI03: Delegación de juicio a IA

| Campo | Valor |
|-------|-------|
| **Nombre** | Delegating Judgment to AI |
| **Descripción** | Delegar a herramientas de IA decisiones que requieren juicio humano: evaluación final de evidencia, clasificación de confidence de conclusiones, aprobación de quality gates, o determinación de si una hipótesis está validada. La IA puede informar estas decisiones pero no tomarlas. |
| **Síntomas** | (1) Quality gates "aprobados" por IA sin revisión humana posterior. (2) Decisiones de lifecycle (cerrar, pivotar, extender) basadas en recomendación de IA sin evaluación humana. (3) Conclusiones finales formuladas por IA y aceptadas sin edición ni challenge humano. |
| **Consecuencias** | Ausencia de accountability humana en decisiones críticas; quality gates sin rigor; R14 (human review) violado sistemáticamente. |
| **Corrección** | Usar IA como input para la decisión, nunca como decisor. Mantener human review obligatorio para conclusiones, quality gates y transiciones de estado. Documentar explícitamente quién (humano) tomó cada decisión. |
| **Stages** | Evidence Evaluation, Conclusion, Review |

---

### AP-AI04: Consenso entre IAs como confirmación

| Campo | Valor |
|-------|-------|
| **Nombre** | AI Consensus as Independent Confirmation |
| **Descripción** | Tratar el acuerdo entre múltiples herramientas de IA (ej. ChatGPT y NotebookLM dan la misma respuesta) como "confirmación independiente" que incrementa el confidence level. Las herramientas de IA pueden compartir datos de entrenamiento, sesgos y limitaciones — su acuerdo no constituye corroboración independiente. |
| **Síntomas** | (1) Justificaciones como "tanto ChatGPT como NotebookLM coinciden, así que es confidence 5". (2) Fuentes citadas que en realidad provienen todas de outputs de IA, sin fuente primaria humana. (3) Aumento de confidence level basado en cantidad de herramientas de IA consultadas en lugar de calidad de fuentes primarias. |
| **Consecuencias** | Falsa corroboración; confidence levels inflados sin base epistémica real; riesgo de que sesgos compartidos entre IAs se amplifiquen en lugar de detectarse. |
| **Corrección** | Solo fuentes primarias independientes (no generadas por IA) constituyen confirmación para incrementar confidence level. El acuerdo entre herramientas de IA no modifica el confidence de la evidencia. |
| **Stages** | Source Collection, Evidence Evaluation, Analysis |

---

### AP-AI05: Prompt como metodología

| Campo | Valor |
|-------|-------|
| **Nombre** | Prompt Engineering as Methodology |
| **Descripción** | Sustituir el diseño metodológico riguroso (scope, questions, criterios de evaluación) por la iteración de prompts hasta obtener una respuesta "que suena bien". La calidad del prompt no reemplaza la calidad del diseño investigativo; un prompt perfecto aplicado a una pregunta mal formulada produce respuestas elocuentes pero no rigurosas. |
| **Síntomas** | (1) Investigaciones que saltan directamente de trigger a "conversar con ChatGPT" sin pasar por Problem Framing ni Research Question. (2) Ausencia de research questions formales — el prompt se usa como sustituto. (3) Iteración infinita de prompts sin criterios predefinidos de cuándo una respuesta es suficiente. |
| **Consecuencias** | Investigaciones sin estructura reproducible; imposibilidad de evaluar la calidad de los hallazgos contra un estándar; dependencia de la herramienta en lugar de la metodología. |
| **Corrección** | Completar las etapas 1-5 del lifecycle antes de consultar herramientas de IA. Usar prompts como herramienta dentro de una metodología, no como sustituto de la metodología. Definir criteria de suficiencia antes de iniciar consultas. |
| **Stages** | Intake, Problem Framing, Research Question |

---

## Mapeo a lifecycle stages

La siguiente tabla mapea cada anti-patrón a las etapas del lifecycle donde es más probable que se manifieste.

| Anti-patrón | Intake | Problem Framing | Research Question | Scope | Assumptions | Source Collection | Evidence Evaluation | Analysis | Experimentation | Findings | Conclusion | Review | Asset Extraction | Product Hypothesis | Publication | Feedback |
|-------------|--------|-----------------|-------------------|-------|-------------|-------------------|--------------------|---------|-----------------|---------|-----------:|--------|-----------------|-------------------|-------------|----------|
| AP-G01 Documentation as Validation | | | | | | | ● | | | | ● | ● | | | | |
| AP-G02 AI as Primary Evidence | | | | | | ● | ● | ● | | | | | | | | |
| AP-G03 Validation Without Criteria | | | | | | | | | ● | | ● | ● | | | | |
| AP-G04 Indefinite Research | | | | ● | | ● | | ● | | | | | | | | |
| AP-G05 Forced Monetization | | | | | | | | | | | | | ● | ● | | |
| AP-G06 Activity as Progress | | | | | | ● | ● | ● | | ● | | | | | | |
| AP-G07 Ignoring Negative Results | | | | | | | | | ● | ● | ● | | | | | |
| AP-G08 Silent Scope Creep | | | | | | ● | | ● | | ● | | | | | | |
| AP-AI01 Summaries Unverified | | | | | | ● | ● | | | | | | | | | |
| AP-AI02 AI Confidence as Quality | | | | | | | ● | ● | | | ● | | | | | |
| AP-AI03 Delegating Judgment | | | | | | | ● | | | | ● | ● | | | | |
| AP-AI04 AI Consensus | | | | | | ● | ● | ● | | | | | | | | |
| AP-AI05 Prompt as Methodology | ● | ● | ● | | | | | | | | | | | | | |

---

## Checklist de detección por stage

Cada etapa del lifecycle incluye al menos una pregunta de detección para identificar anti-patrones activos. Estas preguntas pueden integrarse a los quality gates de [020-quality-gates.md](./020-quality-gates.md).

### Etapa 1: Intake

| # | Pregunta de detección | Anti-patrón detectado |
|---|----------------------|----------------------|
| 1 | ¿Se ha consultado una herramienta de IA antes de documentar formalmente el trigger y la clasificación del problema? | AP-AI05 Prompt as Methodology |

### Etapa 2: Problem Framing

| # | Pregunta de detección | Anti-patrón detectado |
|---|----------------------|----------------------|
| 1 | ¿El problem statement fue generado por IA sin reformulación ni challenge humano? | AP-AI05 Prompt as Methodology |

### Etapa 3: Research Question

| # | Pregunta de detección | Anti-patrón detectado |
|---|----------------------|----------------------|
| 1 | ¿Las research questions surgieron de un prompt iterativo sin pasar por los criterios de calidad (specificity, answerability, relevance, time-boundedness)? | AP-AI05 Prompt as Methodology |

### Etapa 4: Scope

| # | Pregunta de detección | Anti-patrón detectado |
|---|----------------------|----------------------|
| 1 | ¿El scope carece de timebox o deadline definidos? | AP-G04 Indefinite Research |

### Etapa 5: Assumptions

| # | Pregunta de detección | Anti-patrón detectado |
|---|----------------------|----------------------|
| 1 | ¿Las assumptions documentadas provienen exclusivamente de sugerencias de IA sin reflexión humana sobre el contexto específico? | AP-AI03 Delegating Judgment |

### Etapa 6: Source Collection

| # | Pregunta de detección | Anti-patrón detectado |
|---|----------------------|----------------------|
| 1 | ¿Alguna fuente registrada es exclusivamente un output de IA sin fuente primaria verificable detrás? | AP-G02 AI as Primary Evidence |
| 2 | ¿Se han agregado fuentes no relacionadas con las research questions documentadas? | AP-G08 Silent Scope Creep |
| 3 | ¿Se están aceptando resúmenes de IA como representación fiel de fuentes sin verificar contra el original? | AP-AI01 Summaries Unverified |

### Etapa 7: Evidence Evaluation

| # | Pregunta de detección | Anti-patrón detectado |
|---|----------------------|----------------------|
| 1 | ¿Se ha asignado confidence level > 3 a evidencia proveniente de IA sin verificación contra fuente primaria? | AP-AI02 AI Confidence as Quality |
| 2 | ¿El acuerdo entre múltiples herramientas de IA se ha contado como "confirmación independiente"? | AP-AI04 AI Consensus |
| 3 | ¿Existen findings extensamente documentados pero sin referencia a Source_Register? | AP-G01 Documentation as Validation |

### Etapa 8: Analysis

| # | Pregunta de detección | Anti-patrón detectado |
|---|----------------------|----------------------|
| 1 | ¿El análisis muestra más horas de actividad que preguntas respondidas? | AP-G06 Activity as Progress |
| 2 | ¿Se han incorporado nuevas preguntas de investigación sin control formal de scope? | AP-G08 Silent Scope Creep |

### Etapa 9: Experimentation

| # | Pregunta de detección | Anti-patrón detectado |
|---|----------------------|----------------------|
| 1 | ¿La hipótesis se ha declarado "validada" sin que existan success/failure criteria definidos previamente? | AP-G03 Validation Without Criteria |
| 2 | ¿Los resultados negativos se han omitido del registro de experimentos? | AP-G07 Ignoring Negative Results |

### Etapa 10: Findings

| # | Pregunta de detección | Anti-patrón detectado |
|---|----------------------|----------------------|
| 1 | ¿Los findings registran hallazgos sobre preguntas que no estaban en el scope original? | AP-G08 Silent Scope Creep |
| 2 | ¿Existen solo findings positivos cuando se exploraron múltiples hipótesis? | AP-G07 Ignoring Negative Results |

### Etapa 11: Conclusion

| # | Pregunta de detección | Anti-patrón detectado |
|---|----------------------|----------------------|
| 1 | ¿La conclusión carece de uncertainty section o limitaciones? | AP-G01 Documentation as Validation |
| 2 | ¿La conclusión fue generada por IA y aceptada sin edición humana? | AP-AI03 Delegating Judgment |
| 3 | ¿El confidence level de la conclusión supera el nivel máximo soportado por la evidencia registrada? | AP-AI02 AI Confidence as Quality |

### Etapa 12: Review

| # | Pregunta de detección | Anti-patrón detectado |
|---|----------------------|----------------------|
| 1 | ¿La revisión evaluó formato y completitud pero no verificó claims contra evidencia? | AP-G01 Documentation as Validation |
| 2 | ¿La revisión fue ejecutada por IA sin human review posterior? | AP-AI03 Delegating Judgment |
| 3 | ¿Se aprobó un quality gate sin checklist explícito de criterios? | AP-G03 Validation Without Criteria |

### Etapa 13: Asset Extraction

| # | Pregunta de detección | Anti-patrón detectado |
|---|----------------------|----------------------|
| 1 | ¿Se está creando un activo comercial desde una investigación sin evidencia de demanda? | AP-G05 Forced Monetization |

### Etapa 14: Product Hypothesis

| # | Pregunta de detección | Anti-patrón detectado |
|---|----------------------|----------------------|
| 1 | ¿Se ha formulado una Product_Hypothesis sin evidencia de demanda en el Source_Register? | AP-G05 Forced Monetization |

### Etapa 15: Publication or Archive

| # | Pregunta de detección | Anti-patrón detectado |
|---|----------------------|----------------------|
| 1 | ¿El documento a publicar contiene claims no verificados provenientes de herramientas de IA? | AP-G02 AI as Primary Evidence |

### Etapa 16: Feedback and Iteration

| # | Pregunta de detección | Anti-patrón detectado |
|---|----------------------|----------------------|
| 1 | ¿El feedback se procesó sin registrar lessons learned de los resultados negativos encontrados? | AP-G07 Ignoring Negative Results |

---

## Referencias

- [002-research-lifecycle.md](./002-research-lifecycle.md) — 16 etapas del lifecycle referenciadas en el mapeo
- [012-chatgpt-guidelines.md](./012-chatgpt-guidelines.md) — Anti-patrones específicos de ChatGPT (complementarios a este documento)
- [006-evidence-framework.md](./006-evidence-framework.md) — Confidence levels y categorías de evidencia
- [020-quality-gates.md](./020-quality-gates.md) — Quality gates donde se integran las preguntas de detección
- [001-research-principles.md](./001-research-principles.md) — Principios que los anti-patrones violan

---

## Tabla epistémica

| Clasificación | Cantidad | Descripción |
|---------------|----------|-------------|
| [Decisión] | 1 | Este documento completo es una decisión de diseño sobre qué prácticas constituyen anti-patrones |
