# Principios de Investigación

## Propósito

Este documento define los principios fundacionales que gobiernan toda actividad de investigación dentro de LabOS. [Decisión] Los principios son universales: aplican a todas las investigaciones independientemente del dominio, tipo de evidencia o herramientas utilizadas.

---

## Definición de investigación

**Investigación** = toda actividad de research o exploración que consume más de 4 horas de esfuerzo acumulado O que produce un output documentado destinado a reutilización. [Decisión]

Esta definición determina el umbral a partir del cual los principios son obligatorios. Actividades exploratorias menores a 4 horas que no producen output reutilizable no requieren compliance formal, pero se benefician de seguir los principios como guía.

---

## Principios

### Principio 1: Pregunta antes de esfuerzo

**Statement:** Toda investigación debe comenzar con al menos una pregunta explícita y delimitada antes de invertir esfuerzo investigativo. Sin pregunta documentada, no hay investigación — hay exploración sin dirección.

**Rationale:** La ausencia de una pregunta clara es la causa más frecuente de investigaciones que consumen tiempo sin producir resultados accionables. Una pregunta explícita permite medir progreso, definir cuándo la investigación está completa, y comunicar el propósito a terceros.

**Indicador de cumplimiento:** El Research_Brief contiene al menos una Research_Question documentada con subject, scope y método de verificación antes de que el esfuerzo acumulado supere las 2 horas.

**Ejemplo de violación:** Un fundador dedica 12 horas leyendo documentación sobre frameworks de agentes IA sin haber formulado qué pregunta específica intenta responder. Al final tiene notas dispersas pero no puede determinar si la investigación está completa o qué aprendió de forma estructurada.

---

### Principio 2: Evidencia sobre opinión

**Statement:** Las conclusiones de una investigación deben fundamentarse en evidencia documentada y trazable, no en impresiones, intuiciones o preferencias personales.

**Rationale:** Las opiniones no verificables no producen conocimiento reutilizable. La evidencia trazable permite a terceros evaluar la solidez de una conclusión, identificar limitaciones, y actualizar el conocimiento cuando aparece nueva información. LabOS opera con rigor epistémico porque su valor depende de la calidad del conocimiento que produce.

**Indicador de cumplimiento:** Toda conclusión formulada referencia al menos un registro de evidencia específico del Evidence_Framework con categoría y nivel de confianza asignados.

**Ejemplo de violación:** Un investigador concluye que "NotebookLM es mejor que ChatGPT para análisis de fuentes" sin documentar qué criterios usó para comparar, qué fuentes analizó con cada herramienta, ni qué resultados específicos observó.

---

### Principio 3: Trazabilidad de fuente a conclusión

**Statement:** Debe existir una cadena verificable desde cada conclusión hasta las fuentes y evidencia que la soportan. Ningún hallazgo puede existir como afirmación aislada sin origen documentado.

**Rationale:** La trazabilidad permite auditar la calidad de una investigación, identificar conclusiones que dependen de fuentes débiles, y actualizar resultados cuando una fuente es invalidada o superada. Sin trazabilidad, el conocimiento se degrada silenciosamente con el tiempo.

**Indicador de cumplimiento:** La conclusión contiene referencias explícitas a entradas del Source_Register, y cada fuente referenciada tiene evaluación de calidad completada con score numérico.

**Ejemplo de violación:** Un documento de conclusiones sobre estrategias de scalping en crypto afirma "el timeframe de 5 minutos ofrece mejor ratio riesgo-beneficio" sin indicar qué backtest, paper o dataset soporta la afirmación, haciendo imposible verificar o replicar el hallazgo.

---

### Principio 4: Scope explícito y defendible

**Statement:** Toda investigación debe declarar qué incluye, qué excluye y a qué profundidad opera antes de iniciar la fase de recolección. El scope limita el esfuerzo y define la frontera del trabajo.

**Rationale:** Las investigaciones sin scope definido tienden a expandirse indefinidamente (scope creep), consumir recursos desproporcionados respecto al valor esperado, y producir resultados superficiales en muchos frentes en lugar de profundos en pocos. El scope es un compromiso entre completitud y viabilidad.

**Indicador de cumplimiento:** El documento de scope existe con inclusiones, exclusiones y depth level documentados antes de que la etapa Source Collection comience.

**Ejemplo de violación:** Una investigación sobre "fotografía de producto para e-commerce" nunca define si cubre iluminación, composición, post-procesado, equipamiento o todo a la vez. Después de 20 horas, tiene notas superficiales sobre cada tema pero ninguna conclusión accionable en profundidad.

---

### Principio 5: Timebox como contrato

**Statement:** Toda investigación debe tener un límite temporal explícito asignado antes de iniciar trabajo activo. El timebox es un contrato con uno mismo: al expirar, se produce una conclusión con la evidencia disponible o se documenta una extensión justificada.

**Rationale:** Sin timebox, las investigaciones se convierten en sumideros de tiempo que nunca concluyen. El timebox fuerza la priorización de fuentes, la formulación de conclusiones parciales cuando la evidencia es insuficiente, y la toma de decisiones con información imperfecta — una habilidad operativa crítica.

**Indicador de cumplimiento:** El Research Plan contiene un timebox expresado en horas con fecha límite calculada, y existe un registro de conclusión o extensión documentada antes o en la fecha límite.

**Ejemplo de violación:** Un fundador investiga "mejores prácticas de community management con IA" con timebox de 8 horas. Lleva 16 horas invertidas sin haber documentado una conclusión parcial ni solicitado una extensión formal — el timebox fue ignorado silenciosamente.

---

### Principio 6: Clasificación epistémica obligatoria

**Statement:** Toda afirmación producida durante una investigación debe clasificarse explícitamente como hecho, hipótesis, interpretación o decisión. No se permite contenido sin clasificación epistémica.

**Rationale:** Mezclar hechos con hipótesis sin distinción produce documentos que parecen rigurosos pero contienen suposiciones no validadas tratadas como verdades. La clasificación fuerza al investigador a ser honesto sobre el nivel de certeza de cada afirmación y permite a lectores futuros evaluar qué requiere validación adicional.

**Indicador de cumplimiento:** Cada sección del documento de conclusiones utiliza etiquetas [Hecho], [Hipótesis], [Decisión] o [Interpretación] en las afirmaciones clave, y ninguna afirmación sustantiva queda sin clasificar.

**Ejemplo de violación:** Un análisis de mercado sobre herramientas de productividad personal afirma "el mercado crecerá 25% anual" junto a "existen 3 competidores directos" sin distinguir que lo primero es una hipótesis basada en un reporte y lo segundo es un hecho verificable.

---

### Principio 7: Toda investigación produce un activo

**Statement:** Al completar una investigación, debe extraerse al menos un activo reutilizable documentado. Si la investigación no produce un activo, debe documentarse explícitamente por qué no fue posible.

**Rationale:** La investigación que no produce outputs reutilizables es consumo de tiempo, no generación de valor. Un activo — sea un template, un dataset, un playbook, una comparativa o una guía — permite que el conocimiento generado beneficie investigaciones futuras, otros labs del portafolio, o se convierta en producto. La investigación sin activo es un callejón sin salida.

**Indicador de cumplimiento:** El Asset Handoff existe con campos completos (nombre, tipo, descripción, hipótesis de uso, audiencia objetivo), o existe una declaración documentada de "investigación sin activo extraíble" con justificación.

**Ejemplo de violación:** Un fundador invierte 10 horas investigando opciones de hosting para un servicio web, toma una decisión, pero nunca documenta la comparativa como activo reutilizable. Seis meses después, necesita elegir hosting para otro proyecto y repite la investigación desde cero.

---

### Principio 8: Fuentes evaluadas, no asumidas

**Statement:** Toda fuente utilizada en una investigación debe pasar por una evaluación de calidad documentada antes de que su contenido se trate como evidencia. No se asume calidad por reputación, popularidad o familiaridad.

**Rationale:** La calidad de una conclusión no puede exceder la calidad de las fuentes que la soportan. Fuentes no evaluadas introducen sesgos invisibles, información desactualizada o datos incorrectos que contaminan toda la cadena de razonamiento. La evaluación explícita hace visible la calidad de los cimientos de cada investigación.

**Indicador de cumplimiento:** Cada fuente referenciada tiene una entrada en el Source_Register con score de calidad calculado contra las 10 dimensiones de evaluación definidas en 007-source-evaluation.

**Ejemplo de violación:** Un investigador cita "según un artículo de Medium" como soporte para una decisión técnica sobre arquitectura de microservicios, sin evaluar la autoridad del autor, la fecha de publicación, la metodología del artículo ni la existencia de conflictos de interés.

---

### Principio 9: AI como herramienta, no como fuente

**Statement:** El contenido generado por herramientas de IA (ChatGPT, NotebookLM, Copilot, etc.) se clasifica como AI_Generated_Content y requiere verificación contra fuentes primarias antes de tratarse como evidencia.

**Rationale:** Las herramientas de IA producen contenido plausible pero no necesariamente correcto. Tratar output de IA como evidencia primaria introduce un riesgo sistemático de construir conclusiones sobre información fabricada (hallucinations). LabOS usa IA extensivamente pero distingue entre usar IA para generar hipótesis y tratar output de IA como evidencia verificada.

**Indicador de cumplimiento:** Todo contenido derivado de herramientas de IA que se incorpora como evidencia tiene una etiqueta AI_Generated_Content y una referencia a la fuente primaria contra la cual fue verificado.

**Ejemplo de violación:** Un fundador pregunta a ChatGPT "¿cuáles son las mejores prácticas de backtesting para estrategias de trading?" y copia la respuesta directamente en su documento de conclusiones sin verificar si las "mejores prácticas" listadas son reales, están actualizadas, o son invenciones plausibles del modelo.

---

### Principio 10: Reproducibilidad del proceso

**Statement:** El proceso seguido en una investigación debe estar documentado con suficiente detalle para que un tercero pueda reproducir los pasos y llegar a conclusiones verificables con las mismas fuentes.

**Rationale:** Si un proceso investigativo no puede reproducirse, sus conclusiones no pueden auditarse ni actualizarse. La reproducibilidad no requiere que un tercero obtenga resultados idénticos, pero sí que pueda seguir los mismos pasos, consultar las mismas fuentes y evaluar si las conclusiones se sostienen. Esto es especialmente crítico cuando el fundador es la única persona operando.

**Indicador de cumplimiento:** El Research_Journal contiene entradas cronológicas que documentan qué se hizo, qué fuentes se consultó, qué herramientas se usó y qué decisiones se tomó en cada sesión de trabajo.

**Ejemplo de violación:** Un fundador concluye que "el framework CrewAI es superior a LangChain para orquestación multi-agente" pero su Research_Journal no documenta qué criterios usó para comparar, qué versiones probó, ni qué experimentos ejecutó — imposibilitando que alguien verifique la conclusión en el futuro.

---

### Principio 11: Separación de hallazgo y recomendación

**Statement:** Los hallazgos (qué se encontró) deben documentarse separadamente de las recomendaciones (qué se sugiere hacer). Un hallazgo es descriptivo; una recomendación es prescriptiva.

**Rationale:** Mezclar hallazgos con recomendaciones impide evaluar la evidencia independientemente de las decisiones derivadas. Un lector futuro puede aceptar los hallazgos pero llegar a recomendaciones diferentes según su contexto. La separación permite reutilizar hallazgos en contextos donde las recomendaciones originales no aplican.

**Indicador de cumplimiento:** El documento de conclusión tiene secciones separadas y claramente etiquetadas para "Hallazgos" (findings) y "Recomendaciones" (recommendations), sin que las recomendaciones se presenten dentro de la narrativa de hallazgos.

**Ejemplo de violación:** Un análisis de herramientas de edición fotográfica mezcla "Lightroom procesa archivos RAW en 2.3 segundos promedio" (hallazgo) con "por lo tanto deberías usar Lightroom" (recomendación) en el mismo párrafo, sin permitir que el lector evalúe el dato independientemente del consejo.

---

### Principio 12: Honestidad sobre limitaciones

**Statement:** Toda investigación debe documentar explícitamente sus limitaciones: qué no se investigó, qué evidencia faltó, qué sesgos pueden estar presentes y qué confianza merece cada conclusión.

**Rationale:** Una investigación que no declara limitaciones aparenta completitud que no posee. Las limitaciones documentadas protegen al tomador de decisiones de sobreestimar la solidez de una conclusión, permiten priorizar investigaciones futuras que llenen los gaps, y demuestran rigor intelectual. Investigación sin limitaciones documentadas es investigación sospechosa.

**Indicador de cumplimiento:** La sección de uncertainty del documento de conclusión existe y contiene al menos: limitaciones metodológicas, gaps de evidencia identificados, y nivel de confianza asignado (high/medium/low) con justificación.

**Ejemplo de violación:** Una investigación sobre "rentabilidad de cursos online en español" concluye que "los cursos técnicos de $49 generan mejor margen" sin documentar que solo analizó 3 plataformas, no consideró cursos fuera de tecnología, y que sus datos provienen exclusivamente de fuentes públicas sin acceso a métricas internas.

---

## Mecanismo de excepción documentada

### Cuándo aplica

Una investigación puede exceptuarse de uno o más principios cuando existe una justificación legítima. [Decisión] Las excepciones no invalidan los principios — los reconocen como norma y documentan por qué la desviación es aceptable en un caso específico.

### Campos obligatorios de la excepción

Toda excepción debe documentarse con los siguientes campos:

| Campo | Descripción |
| ----- | ----------- |
| **Principio exceptuado** | Identificador y nombre del principio (e.g., "Principio 5: Timebox como contrato") |
| **Justificación** | Razón concreta por la cual el principio no puede cumplirse en este caso. Mínimo 2 oraciones. |
| **Alcance** | Qué parte de la investigación queda fuera del principio. Debe ser lo más estrecho posible. |
| **Fecha de decisión** | Fecha en que se tomó la decisión de exceptuar. |
| **Revisión** | Fecha o condición bajo la cual la excepción será reevaluada. |
| **Decisor** | Quién aprobó la excepción (en etapa actual: Fundador). |

### Restricciones

- Una investigación no puede exceptuarse de más de 3 principios simultáneamente. Si requiere más excepciones, debe reevaluarse si la actividad califica como "investigación" bajo esta metodología. [Decisión]
- Los principios 2 (Evidencia sobre opinión) y 9 (AI como herramienta, no como fuente) no admiten excepción completa — solo admiten excepción parcial de alcance limitado. [Decisión]
- Toda excepción debe registrarse en el Research_Journal de la investigación correspondiente.

### Ejemplo de excepción válida

> **Principio exceptuado:** Principio 10: Reproducibilidad del proceso
> **Justificación:** La investigación involucró entrevistas confidenciales con 3 profesionales del sector financiero que solicitaron anonimato completo. Documentar los pasos con nivel de detalle que permita identificar a los entrevistados violaría el acuerdo de confidencialidad. Se documenta el proceso a nivel general sin datos identificables.
> **Alcance:** Solo las entradas del Research_Journal correspondientes a las sesiones de entrevista (3 de 12 entradas totales).
> **Fecha de decisión:** 2025-02-15
> **Revisión:** Reevaluar si los entrevistados autorizan uso de datos en 6 meses.
> **Decisor:** Fundador

---

## Compliance assessment

Toda investigación debe incluir, como parte de su cierre, una evaluación de compliance contra los 12 principios. [Decisión] Una investigación sin compliance assessment documentado se considera **incompleta** hasta que el assessment sea registrado.

### Formato del assessment

| Principio | Cumple | Evidencia / Excepción |
| --------- | ------ | --------------------- |
| 1. Pregunta antes de esfuerzo | Sí / No / Parcial | Referencia a Research_Brief o excepción documentada |
| 2. Evidencia sobre opinión | Sí / No / Parcial | Referencia a Evidence records o excepción |
| ... | ... | ... |
| 12. Honestidad sobre limitaciones | Sí / No / Parcial | Referencia a sección de uncertainty o excepción |

### Regla de completitud

- **Cumple:** La investigación se marca como completa.
- **Parcial con excepciones documentadas:** La investigación se marca como completa con nota de excepciones.
- **No cumple sin excepción:** La investigación se marca como **incompleta** y requiere remediación antes de avanzar a la etapa de Asset Extraction.

---

## Trazabilidad a requirements

| Principio / Sección | Requirement |
| -------------------- | ----------- |
| 12 principios definidos | R1.1 (entre 10-15 principios universales) |
| Statement + Rationale + Indicator + Violation | R1.2 (4 campos por principio) |
| Mecanismo de excepción documentada | R1.3 (excepción con principio, justificación, scope, fecha) |
| Definición de investigación (>4h o output reutilizable) | R1.4 (definición de "investigación") |
| Compliance assessment obligatorio | R1.5 (investigación sin assessment = incompleta) |

---

## Tabla epistémica

| Clasificación | Cantidad | Notas |
| ------------- | -------- | ----- |
| [Hecho] | 0 | — |
| [Hipótesis] | 0 | — |
| [Visión] | 0 | — |
| [Decisión] | 16 | 12 principios + definición de investigación + restricciones de excepción + compliance assessment + max excepciones |
