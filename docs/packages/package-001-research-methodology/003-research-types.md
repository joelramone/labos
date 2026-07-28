# 003 — Taxonomía de Tipos de Investigación

> **Etiqueta epistémica:** [Decisión]
>
> **Requirements:** R27.1, R27.2, R27.3, R27.4, R27.5

---

## Propósito

Este documento define la taxonomía completa de 12 tipos de investigación que LabOS reconoce. Cada tipo representa un enfoque metodológico distinto con propósito, preguntas típicas, dominios aplicables, tipos de evidencia, métodos de validación y criterios de uso específicos. [Decisión]

La taxonomía permite al Fundador seleccionar el tipo (o combinación de tipos) más apropiado para cada investigación, asegurando que el enfoque metodológico se alinee con la pregunta de investigación y el dominio. [Decisión]

---

## Resumen de tipos

| # | Tipo | Propósito central |
|---|------|-------------------|
| 1 | Exploratory | Comprender dominio, descubrir variables, identificar preguntas |
| 2 | Descriptive | Documentar qué ocurre, caracterizar sistemas/usuarios/datos |
| 3 | Comparative | Comparar herramientas, enfoques, productos, alternativas |
| 4 | Experimental | Probar hipótesis, medir resultados, controlar variables |
| 5 | Diagnostic | Investigar incidentes, fallas, causas raíz |
| 6 | Market | Identificar problemas, usuarios, competencia, willingness to pay |
| 7 | Product | Validar necesidades, propuesta de valor, comportamiento del usuario |
| 8 | Technical | Evaluar arquitecturas, protocolos, librerías, tecnologías |
| 9 | Quantitative | Analizar datasets, métricas, modelos |
| 10 | Qualitative | Analizar entrevistas, observaciones, documentos, experiencia |
| 11 | Educational | Estudiar métodos de aprendizaje, currículos, prácticas educativas |
| 12 | Creative | Analizar estilos, referencias, composición, narrativa, producción |

---

## Tipos de investigación


### 1. Exploratory

**Purpose:** Comprender un dominio nuevo o poco documentado, descubrir variables relevantes e identificar preguntas que merecen investigación formal. Se usa cuando no existe conocimiento previo suficiente para formular hipótesis precisas.

**Typical questions:**

- ¿Qué variables influyen en [fenómeno] dentro de [dominio]?
- ¿Qué patrones emergen al observar [sistema/proceso/comunidad]?
- ¿Qué preguntas específicas deberían investigarse a profundidad sobre [tema]?
- ¿Qué actores, herramientas o factores participan en [contexto]?

**Applicable domains:**

- SoftwareFactoryAgentsAI — explorar capacidades de nuevos modelos de IA o frameworks de agentes
- Crypto Scalping Core — explorar nuevos mercados, exchanges o instrumentos financieros
- English Learning Lab — explorar métodos de adquisición de idiomas no convencionales

**Evidence types:**

- Observación directa
- Documentación preliminar
- Notas de campo y patrones emergentes

**Validation methods:**

- Triangulación de múltiples fuentes independientes
- Revisión por pares del mapa conceptual producido

**Expected outputs:**

- Mapa conceptual del dominio
- Lista de variables identificadas
- Preguntas de investigación formuladas para investigación posterior
- Research_Brief(s) derivados

**When to use:**

- Cuando se ingresa a un dominio nuevo donde no hay conocimiento previo documentado dentro de LabOS
- Cuando los resultados previos son contradictorios y se necesita reformular el entendimiento del problema
- Cuando se necesita generar hipótesis antes de poder diseñar experimentos

**When NOT to use:**

- Cuando ya existe una hipótesis clara y verificable — usar **Experimental** en su lugar
- Cuando el objetivo es comparar alternativas concretas ya conocidas — usar **Comparative**
- Cuando se requiere una respuesta numérica o estadística sobre datos existentes — usar **Quantitative**

---


### 2. Descriptive

**Purpose:** Documentar de forma sistemática qué ocurre en un sistema, proceso o contexto sin intentar explicar por qué. Produce una caracterización precisa del estado actual como base para decisiones o investigaciones posteriores.

**Typical questions:**

- ¿Cuál es el estado actual de [sistema/proceso/mercado]?
- ¿Qué características tienen [usuarios/datos/componentes] en [contexto]?
- ¿Con qué frecuencia ocurre [evento] y bajo qué condiciones?
- ¿Cómo se distribuyen [recursos/actividades/resultados] en [dominio]?

**Applicable domains:**

- SentinelOps — documentar la topología actual de infraestructura o patrones de incidentes
- Human Performance Lab — caracterizar hábitos actuales, métricas basales de rendimiento
- CommunityManagerBotCrew — describir la composición y comportamiento de una audiencia

**Evidence types:**

- Mediciones y métricas
- Observación sistemática
- Datos de registro o logs

**Validation methods:**

- Verificación contra datos primarios
- Reproducibilidad de la observación en diferentes momentos

**Expected outputs:**

- Documento de estado actual (as-is)
- Perfiles o caracterizaciones
- Métricas basales documentadas
- Mapas de distribución o frecuencia

**When to use:**

- Cuando se necesita establecer una línea base antes de intervenir o cambiar algo
- Cuando se requiere un inventario o auditoría del estado actual
- Cuando múltiples stakeholders necesitan un entendimiento compartido de la realidad

**When NOT to use:**

- Cuando el objetivo es encontrar la causa de un problema — usar **Diagnostic**
- Cuando se busca entender un dominio nuevo sin estructura previa — usar **Exploratory**
- Cuando se necesita elegir entre opciones — usar **Comparative**

---


### 3. Comparative

**Purpose:** Evaluar y contrastar dos o más alternativas (herramientas, enfoques, productos, tecnologías) usando criterios explícitos para informar una decisión de selección.

**Typical questions:**

- ¿Cuál de las alternativas [A, B, C] satisface mejor los criterios [X, Y, Z]?
- ¿Qué ventajas y desventajas tiene [opción A] frente a [opción B] en [contexto]?
- ¿Qué trade-offs existen entre [enfoque 1] y [enfoque 2] para [caso de uso]?
- ¿Cuál es el costo-beneficio relativo de cada alternativa?

**Applicable domains:**

- SoftwareFactoryAgentsAI — comparar frameworks de agentes, modelos de lenguaje o arquitecturas
- Atlas Wealth Labs — comparar estrategias de inversión, plataformas o instrumentos financieros
- Music Lab — comparar DAWs, plugins o métodos de distribución musical

**Evidence types:**

- Benchmarks y pruebas de rendimiento
- Matrices de evaluación con criterios ponderados
- Documentación oficial de cada alternativa

**Validation methods:**

- Prueba directa de las alternativas bajo condiciones equivalentes
- Revisión de evaluaciones independientes publicadas

**Expected outputs:**

- Matriz comparativa con scoring
- Decision record con selección justificada
- Lista de trade-offs documentados
- Recomendación con condiciones de aplicabilidad

**When to use:**

- Cuando existen al menos 2 alternativas identificadas y se necesita elegir
- Cuando una decisión técnica o de producto requiere justificación basada en evidencia
- Cuando se evalúa reemplazar una herramienta o enfoque actual

**When NOT to use:**

- Cuando no se conocen las alternativas aún — usar **Exploratory** primero
- Cuando se necesita probar si una solución funciona antes de compararla — usar **Experimental**
- Cuando el problema es entender por qué algo falló — usar **Diagnostic**

---


### 4. Experimental

**Purpose:** Validar o refutar una hipótesis mediante la manipulación controlada de variables independientes y la medición de sus efectos sobre variables dependientes, con criterios de éxito y fracaso predefinidos.

**Typical questions:**

- ¿Produce [intervención X] un cambio medible en [variable Y]?
- ¿Se confirma la hipótesis de que [A causa B] bajo condiciones controladas?
- ¿Cuál es el efecto de [cambio] sobre [métrica] cuando se controlan [variables]?
- ¿Es reproducible el resultado de [experimento previo] bajo condiciones [variadas]?

**Applicable domains:**

- Crypto Scalping Core — probar estrategias de trading con backtesting y forward testing controlado
- SoftwareFactoryAgentsAI — experimentar con prompts, temperaturas, o arquitecturas de agentes
- Human Performance Lab — medir efecto de intervenciones (suplementos, rutinas, protocolos)

**Evidence types:**

- Resultados experimentales con datos medibles
- Observaciones controladas pre/post intervención
- Datos de control vs grupo experimental

**Validation methods:**

- Reproducibilidad del experimento
- Análisis estadístico de significancia (cuando aplica)
- Peer review del diseño experimental

**Expected outputs:**

- Experiment record con protocolo y resultados
- Hipótesis validada o refutada con evidencia
- Datos crudos del experimento
- Análisis de desviaciones del protocolo

**When to use:**

- Cuando existe una hipótesis falsificable con variables identificadas
- Cuando es posible aislar o controlar variables (incluso parcialmente)
- Cuando se necesita evidencia de causalidad, no solo correlación

**When NOT to use:**

- Cuando no hay hipótesis clara aún — usar **Exploratory** para formularla
- Cuando las variables no pueden manipularse ni controlarse — considerar **Qualitative** o métodos alternativos de validación
- Cuando se busca documentar el estado actual sin intervención — usar **Descriptive**

---


### 5. Diagnostic

**Purpose:** Investigar incidentes, fallas o anomalías para identificar la causa raíz, separando síntomas observables de causas subyacentes, y proponer acciones correctivas.

**Typical questions:**

- ¿Por qué ocurrió [incidente/falla/anomalía]?
- ¿Cuál es la causa raíz de [síntoma observado]?
- ¿Qué secuencia de eventos condujo a [resultado no deseado]?
- ¿Qué factores contribuyentes pueden eliminarse para prevenir recurrencia?

**Applicable domains:**

- SentinelOps — diagnosticar incidentes de infraestructura, caídas de servicio, alertas falsas
- Crypto Scalping Core — investigar pérdidas inesperadas, fallos de ejecución o anomalías de mercado
- SoftwareFactoryAgentsAI — diagnosticar comportamiento inesperado de agentes o pipelines

**Evidence types:**

- Logs, trazas y registros de eventos
- Timelines de incidentes reconstruidas
- Mediciones antes y después del incidente

**Validation methods:**

- Reproducción controlada del fallo (cuando es seguro)
- Confirmación de que la corrección propuesta elimina el síntoma
- Análisis de 5-whys o árboles de fallo

**Expected outputs:**

- Root cause analysis documentado
- Timeline del incidente
- Acciones correctivas con prioridad
- Lecciones aprendidas
- Recomendaciones preventivas

**When to use:**

- Cuando ocurrió un incidente, falla o degradación que necesita explicación
- Cuando un sistema se comporta de manera inesperada y se necesita identificar la causa
- Cuando se requiere un post-mortem formal

**When NOT to use:**

- Cuando no hay un problema específico sino curiosidad general — usar **Exploratory**
- Cuando se busca documentar el comportamiento normal del sistema — usar **Descriptive**
- Cuando el objetivo es comparar soluciones al problema ya diagnosticado — usar **Comparative**

---


### 6. Market

**Purpose:** Identificar problemas reales de un segmento de usuarios, evaluar competencia existente, dimensionar oportunidades y detectar señales de willingness to pay antes de invertir en desarrollo.

**Typical questions:**

- ¿Qué problemas tiene [segmento] que no están resueltos adecuadamente?
- ¿Quiénes son los competidores en [espacio] y qué gaps dejan?
- ¿Existe evidencia de disposición a pagar por [solución/formato] en [segmento]?
- ¿Cuál es el tamaño aproximado del segmento y su accesibilidad?

**Applicable domains:**

- Mindzers — investigar mercados para productos digitales de conocimiento
- Atlas Wealth Labs — evaluar demanda de herramientas financieras para segmentos específicos
- CommunityManagerBotCrew — identificar mercados para servicios de automatización de contenido

**Evidence types:**

- Market data (tamaño, tendencias, competidores)
- Testimonios y señales de demanda directas
- Datos de comportamiento de usuarios potenciales

**Validation methods:**

- Entrevistas con usuarios potenciales del segmento
- Análisis de competidores con criterios explícitos
- Validación de disposición a pagar (encuestas, pre-ventas, landing pages)

**Expected outputs:**

- Análisis de competidores con gaps identificados
- Perfil de segmento con problemas priorizados
- Evidencia de demanda (o ausencia documentada)
- Product_Hypothesis o Revenue_Hypothesis (si la evidencia lo soporta)

**When to use:**

- Cuando se considera crear un producto o servicio nuevo y se necesita validar demanda
- Cuando se busca entender el landscape competitivo antes de invertir recursos
- Cuando se evalúa entrar a un mercado nuevo con un activo existente

**When NOT to use:**

- Cuando ya se tiene un producto y se necesita entender su uso — usar **Product**
- Cuando se investiga una tecnología sin intención comercial inmediata — usar **Technical**
- Cuando se busca entender un fenómeno sin contexto comercial — usar **Exploratory**

---


### 7. Product

**Purpose:** Validar necesidades de usuario, propuesta de valor, y comportamiento real frente a un producto o prototipo existente. Se centra en el producto como artefacto y su interacción con usuarios.

**Typical questions:**

- ¿Resuelve [producto/prototipo] el problema que [segmento] declara tener?
- ¿Cómo se comportan los usuarios al interactuar con [feature/producto]?
- ¿Qué fricción experimentan los usuarios en [flujo/proceso]?
- ¿Qué propuesta de valor resuena más con [segmento]?

**Applicable domains:**

- Mindzers — validar propuesta de valor de herramientas digitales de conocimiento
- SoftwareFactoryAgentsAI — validar si un agente resuelve el problema declarado del usuario
- English Learning Lab — validar efectividad de formatos o herramientas de aprendizaje con usuarios

**Evidence types:**

- Datos de uso y comportamiento (analytics, sesiones)
- Feedback directo de usuarios (entrevistas, surveys)
- Métricas de retención, activación o conversión

**Validation methods:**

- Test de usabilidad con usuarios reales
- A/B testing (cuando hay volumen suficiente)
- Análisis de cohortes y comportamiento longitudinal

**Expected outputs:**

- Findings de usabilidad con evidencia
- Métricas de producto interpretadas
- Decisiones de priorización informadas
- Iteraciones de propuesta de valor documentadas

**When to use:**

- Cuando existe un producto, prototipo o MVP y se necesita validar su efectividad
- Cuando se observa comportamiento inesperado de usuarios en un producto existente
- Cuando se prioriza entre features basándose en datos de uso

**When NOT to use:**

- Cuando no existe producto aún y se investiga el mercado — usar **Market**
- Cuando se busca evaluar la tecnología subyacente, no la experiencia del usuario — usar **Technical**
- Cuando se investigan hábitos generales sin relación a un producto específico — usar **Qualitative**

---


### 8. Technical

**Purpose:** Evaluar arquitecturas, protocolos, librerías, tecnologías o enfoques técnicos para determinar su viabilidad, limitaciones, rendimiento y adecuación a un caso de uso concreto.

**Typical questions:**

- ¿Es viable [tecnología/arquitectura] para [caso de uso] bajo [restricciones]?
- ¿Cuáles son las limitaciones técnicas de [librería/protocolo/servicio]?
- ¿Qué rendimiento ofrece [enfoque técnico] bajo [condiciones de carga/volumen]?
- ¿Cómo se integra [componente A] con [componente B] en [contexto]?

**Applicable domains:**

- SoftwareFactoryAgentsAI — evaluar frameworks de orquestación, modelos de lenguaje, APIs de IA
- SentinelOps — evaluar herramientas de observabilidad, protocolos de monitoreo, arquitecturas de alerting
- Crypto Scalping Core — evaluar exchanges APIs, latencias, librerías de trading algorítmico

**Evidence types:**

- Benchmarks y pruebas de rendimiento
- Documentación técnica oficial
- Proof of concept funcionales
- Resultados de integración

**Validation methods:**

- Implementación de proof of concept
- Load testing y stress testing
- Revisión de documentación oficial y changelogs

**Expected outputs:**

- Evaluación técnica con criterios explícitos
- Proof of concept documentado (si aplica)
- Limitaciones y riesgos técnicos identificados
- Recomendación técnica con condiciones

**When to use:**

- Cuando se necesita decidir sobre adopción de una tecnología con implicaciones de largo plazo
- Cuando se evalúa la viabilidad técnica antes de iniciar implementación
- Cuando se investigan limitaciones de una tecnología ya en uso

**When NOT to use:**

- Cuando se comparan múltiples alternativas tecnológicas con criterios equivalentes — usar **Comparative**
- Cuando se diagnostica un fallo en tecnología ya implementada — usar **Diagnostic**
- Cuando el foco es la experiencia del usuario, no la tecnología subyacente — usar **Product**

---


### 9. Quantitative

**Purpose:** Analizar datasets, métricas y modelos numéricos para identificar patrones, tendencias, correlaciones o anomalías que respondan preguntas de investigación con evidencia cuantificable.

**Typical questions:**

- ¿Qué tendencia muestra [métrica] en el periodo [X a Y]?
- ¿Existe correlación entre [variable A] y [variable B] en [dataset]?
- ¿Qué modelo predictivo explica mejor [fenómeno] dado [datos disponibles]?
- ¿Cuál es la distribución de [variable] en [población/sistema]?

**Applicable domains:**

- Crypto Scalping Core — análisis de series temporales, backtesting de estrategias, modelos de riesgo
- Atlas Wealth Labs — análisis de portafolio, métricas financieras, modelado de escenarios
- Human Performance Lab — análisis de métricas biométricas, tracking de variables de rendimiento

**Evidence types:**

- Datos numéricos estructurados (datasets, CSVs, APIs)
- Resultados de análisis estadístico
- Visualizaciones con datos interpretados
- Modelos con métricas de ajuste

**Validation methods:**

- Validación cruzada de modelos
- Reproducibilidad del análisis con mismos datos
- Verificación contra datos independientes (out-of-sample)

**Expected outputs:**

- Análisis estadístico documentado
- Visualizaciones con interpretación
- Modelos con métricas de rendimiento
- Conclusiones cuantificadas con intervalos de confianza

**When to use:**

- Cuando existen datos numéricos suficientes para responder la pregunta
- Cuando se necesitan respuestas objetivas basadas en mediciones
- Cuando se buscan patrones o correlaciones en grandes volúmenes de datos

**When NOT to use:**

- Cuando no existen datos numéricos y se trabaja con experiencias o percepciones — usar **Qualitative**
- Cuando el objetivo es entender el "por qué" detrás de los números — complementar con **Qualitative** o **Diagnostic**
- Cuando se busca explorar un dominio sin datos previos — usar **Exploratory**

---


### 10. Qualitative

**Purpose:** Analizar experiencias, percepciones, documentos, observaciones y contextos no cuantificables para comprender significados, motivaciones y dinámicas que los datos numéricos no capturan.

**Typical questions:**

- ¿Cómo perciben [usuarios/participantes] la experiencia de [proceso/producto]?
- ¿Qué motivaciones subyacen al comportamiento observado en [contexto]?
- ¿Qué patrones temáticos emergen de [entrevistas/documentos/observaciones]?
- ¿Cómo interpretan [actores] el significado de [fenómeno] en su contexto?

**Applicable domains:**

- Human Performance Lab — entender experiencia subjetiva de protocolos de rendimiento, percepciones de bienestar
- English Learning Lab — analizar experiencia de aprendizaje, motivaciones, barreras percibidas
- CommunityManagerBotCrew — comprender percepción de comunidades sobre contenido y engagement

**Evidence types:**

- Transcripciones de entrevistas
- Notas de observación
- Análisis temático de documentos
- Experiencia profesional documentada

**Validation methods:**

- Triangulación de múltiples fuentes cualitativas
- Validación con participantes (member checking)
- Análisis por múltiples revisores independientes

**Expected outputs:**

- Análisis temático con categorías emergentes
- Narrativas estructuradas con evidencia citada
- Framework conceptual derivado de los datos
- Insights accionables con contexto

**When to use:**

- Cuando se busca comprender el "por qué" y el "cómo" detrás de comportamientos
- Cuando los datos numéricos son insuficientes para responder la pregunta de investigación
- Cuando se investigan experiencias, percepciones o dinámicas sociales

**When NOT to use:**

- Cuando existen datos numéricos suficientes y se buscan respuestas cuantificables — usar **Quantitative**
- Cuando el objetivo es medir el efecto de una intervención controlada — usar **Experimental**
- Cuando se necesita un inventario objetivo del estado actual — usar **Descriptive**

---


### 11. Educational

**Purpose:** Estudiar métodos de aprendizaje, diseño curricular, prácticas pedagógicas y efectividad de formatos educativos para mejorar la transmisión y retención de conocimiento.

**Typical questions:**

- ¿Qué método de enseñanza produce mejor retención de [contenido] en [contexto]?
- ¿Cómo debería estructurarse un currículo para [objetivo de aprendizaje]?
- ¿Qué formatos educativos son más efectivos para [perfil de estudiante/audiencia]?
- ¿Qué prácticas pedagógicas mejoran [competencia específica] en [dominio]?

**Applicable domains:**

- English Learning Lab — investigar métodos de adquisición de idiomas, formatos de práctica, currículos
- Mindzers — investigar cómo empaquetar conocimiento en productos educativos efectivos
- Human Performance Lab — estudiar cómo enseñar prácticas de rendimiento y hábitos de forma efectiva

**Evidence types:**

- Resultados de assessment pre/post
- Observaciones de sesiones de aprendizaje
- Literatura pedagógica y didáctica
- Feedback de estudiantes/participantes

**Validation methods:**

- Comparación pre/post intervención educativa
- Análisis longitudinal de retención
- Benchmarking contra estándares pedagógicos reconocidos

**Expected outputs:**

- Evaluación de efectividad de métodos
- Diseño curricular documentado
- Recomendaciones pedagógicas con evidencia
- Templates o frameworks educativos reutilizables

**When to use:**

- Cuando se diseña un producto o experiencia educativa y se necesita fundamentar decisiones pedagógicas
- Cuando se evalúa la efectividad de un método de enseñanza existente
- Cuando se investiga cómo transferir conocimiento especializado a una audiencia específica

**When NOT to use:**

- Cuando se investiga un tema para aprender sobre él (no sobre cómo enseñarlo) — usar **Exploratory** o el tipo apropiado al dominio
- Cuando se busca validar un producto educativo como negocio — usar **Product** o **Market**
- Cuando el foco es la experiencia subjetiva del aprendiz sin evaluar efectividad — usar **Qualitative**

---


### 12. Creative

**Purpose:** Analizar estilos, referencias visuales o sonoras, composición, narrativa y procesos de producción creativa para informar decisiones estéticas y de producción con fundamento.

**Typical questions:**

- ¿Qué elementos de composición/estilo caracterizan [referencia/género/tendencia]?
- ¿Cómo logran [creadores/obras de referencia] el efecto de [cualidad estética]?
- ¿Qué narrativa o estructura funciona mejor para comunicar [mensaje] a [audiencia]?
- ¿Qué procesos de producción optimizan [calidad/consistencia] en [medio]?

**Applicable domains:**

- Photography Lab — analizar composición, iluminación, estilos de edición, referencias visuales
- Music Lab — analizar estructura musical, producción, mezcla, géneros, referencias sonoras
- CommunityManagerBotCrew — analizar formatos de contenido, narrativas y estilos de comunicación efectivos

**Evidence types:**

- Análisis de obras de referencia
- Documentación de procesos creativos
- Feedback de audiencia sobre piezas producidas
- Comparación de estilos con criterios explícitos

**Validation methods:**

- Peer review por profesionales del dominio creativo
- Análisis comparativo contra referencias establecidas
- Feedback estructurado de la audiencia objetivo

**Expected outputs:**

- Análisis de referencias con criterios explícitos
- Guías de estilo documentadas
- Frameworks de producción creativa
- Decisiones estéticas fundamentadas con evidencia

**When to use:**

- Cuando se necesita fundamentar decisiones estéticas o de producción creativa con análisis
- Cuando se busca desarrollar un estilo consistente basado en referencias
- Cuando se investiga qué elementos creativos resuenan con una audiencia específica

**When NOT to use:**

- Cuando se evalúa la viabilidad comercial del producto creativo — usar **Market** o **Product**
- Cuando se analizan datos de engagement sin foco en la dimensión estética — usar **Quantitative**
- Cuando se busca entender la experiencia subjetiva de la audiencia en profundidad — usar **Qualitative**

---


## Guía de selección de tipo

### Criterios de selección

Para seleccionar el tipo de investigación apropiado, el Fundador debe considerar:

1. **Pregunta de investigación**: ¿Qué se intenta responder? La naturaleza de la pregunta indica el tipo.
2. **Estado del conocimiento**: ¿Se conoce el dominio o es nuevo?
3. **Datos disponibles**: ¿Existen datos cuantitativos o solo cualitativos?
4. **Objetivo final**: ¿Se busca entender, comparar, validar, diagnosticar o producir?
5. **Dominio**: ¿Qué tipos de evidencia son accesibles en este dominio?

### Árbol de decisión simplificado

```
¿Hay un incidente o falla que investigar?
  → Sí: Diagnostic
  → No: continuar

¿Se conoce el dominio y las variables relevantes?
  → No: Exploratory
  → Sí: continuar

¿El objetivo es documentar el estado actual sin intervenir?
  → Sí: Descriptive
  → No: continuar

¿Se tienen alternativas concretas para evaluar?
  → Sí: Comparative
  → No: continuar

¿Se tiene una hipótesis falsificable con variables controlables?
  → Sí: Experimental
  → No: continuar

¿El foco es comercial (mercado, demanda, competencia)?
  → Sí: Market
  → No: continuar

¿Se investiga un producto existente y su interacción con usuarios?
  → Sí: Product
  → No: continuar

¿Se evalúa viabilidad, rendimiento o limitaciones de una tecnología?
  → Sí: Technical
  → No: continuar

¿Se trabaja con datos numéricos estructurados?
  → Sí: Quantitative
  → No: continuar

¿Se analizan experiencias, percepciones o documentos cualitativos?
  → Sí: Qualitative
  → No: continuar

¿El foco es cómo enseñar o transmitir conocimiento?
  → Sí: Educational
  → No: continuar

¿Se analizan estilos, composición, narrativa o producción creativa?
  → Sí: Creative
```


### Justificación de selección

Al declarar el tipo de investigación en el Research_Brief, el Fundador debe incluir una justificación de 1-2 oraciones por cada tipo seleccionado que explique por qué ese tipo se ajusta a la pregunta de investigación. [Decisión]

**Formato de justificación:**

> "Se selecciona [tipo] porque [razón vinculada a la pregunta de investigación y al objetivo]."

**Ejemplos de justificaciones válidas:**

- "Se selecciona Exploratory porque no existe documentación previa sobre el ecosistema de herramientas de orquestación de agentes y se necesita mapear el landscape antes de evaluar opciones."
- "Se selecciona Quantitative porque la pregunta requiere analizar 6 meses de datos de rendimiento para identificar patrones estadísticamente significativos."
- "Se selecciona Market porque la investigación busca validar si existe demanda real para una herramienta de análisis financiero en el segmento de traders independientes."

---

## Guía de combinación de tipos

### Reglas de combinación

1. **Máximo 3 tipos por investigación.** Combinar más de 3 tipos indica que la investigación debe descomponerse en sub-investigaciones. [Decisión]
2. **Cada tipo combinado debe abordar un aspecto diferente** de la pregunta de investigación. No se combinan tipos que cubren el mismo aspecto.
3. **Al combinar tipos, se debe documentar** qué fase o aspecto de la investigación cubre cada tipo.
4. **La combinación no exime del cumplimiento** de los requisitos mínimos de cada tipo individual.

### Combinaciones frecuentes y válidas

| Combinación | Caso de uso típico |
|-------------|-------------------|
| Exploratory → Comparative | Primero mapear el espacio, luego comparar las opciones descubiertas |
| Market + Quantitative | Investigar un mercado combinando análisis cualitativo de demanda con datos numéricos de tamaño |
| Technical + Experimental | Evaluar una tecnología y luego validar su rendimiento mediante experimento controlado |
| Qualitative + Quantitative | Entender motivaciones (por qué) y medir frecuencias (cuánto) sobre un mismo fenómeno |
| Diagnostic + Technical | Diagnosticar la causa raíz y luego evaluar la solución técnica propuesta |
| Educational + Creative | Investigar cómo enseñar un tema y qué formatos creativos son más efectivos |
| Product + Quantitative | Validar un producto combinando datos de uso con métricas de comportamiento |

### Combinaciones inválidas o redundantes

| Combinación | Razón de invalidez |
|-------------|-------------------|
| Exploratory + Descriptive | Ambos documentan sin intervenir; Exploratory ya incluye documentación inicial |
| Market + Product (sin producto existente) | Product requiere un producto real; sin producto, solo aplica Market |
| Experimental + Descriptive | Experimental interviene; Descriptive no. Son mutuamente excluyentes en propósito |


### Documentación de combinación en Research_Brief

Cuando se combinan 2-3 tipos en una investigación, el Research_Brief debe documentar:

1. **Tipos seleccionados** (máximo 3)
2. **Justificación por tipo** (1-2 oraciones cada una)
3. **Aspecto o fase que cubre cada tipo** — qué parte de la pregunta de investigación aborda
4. **Secuencia o paralelismo** — si los tipos se aplican en secuencia (primero uno, luego otro) o en paralelo (simultáneamente sobre diferentes aspectos)

**Ejemplo de combinación documentada:**

> **Tipos:** Exploratory + Technical + Comparative
>
> **Justificación:**
> - Exploratory: Se desconoce el landscape actual de frameworks de orquestación de agentes y se necesita mapear opciones.
> - Technical: Se requiere evaluar las limitaciones técnicas de los frameworks identificados.
> - Comparative: Se necesita seleccionar el framework más adecuado para el caso de uso específico.
>
> **Aspecto por tipo:**
> - Exploratory → Fase de descubrimiento (identificar qué frameworks existen)
> - Technical → Fase de evaluación profunda (limitaciones, rendimiento, integración)
> - Comparative → Fase de decisión (selección final con criterios ponderados)
>
> **Secuencia:** Secuencial (Exploratory → Technical → Comparative)

---

## Matriz de contraste entre tipos

Para facilitar la distinción entre tipos que pueden confundirse:

| Tipo A | Tipo B | Distinción clave |
|--------|--------|-----------------|
| Exploratory | Descriptive | Exploratory descubre variables nuevas; Descriptive documenta variables ya conocidas |
| Comparative | Technical | Comparative evalúa múltiples opciones; Technical profundiza en una sola tecnología |
| Market | Product | Market investiga antes de tener producto; Product investiga con producto existente |
| Quantitative | Experimental | Quantitative analiza datos existentes; Experimental genera datos nuevos mediante intervención |
| Qualitative | Descriptive | Qualitative busca significados y motivaciones; Descriptive documenta hechos observables |
| Diagnostic | Exploratory | Diagnostic parte de un problema concreto; Exploratory parte de curiosidad o desconocimiento |
| Educational | Qualitative | Educational evalúa efectividad de enseñanza; Qualitative comprende experiencias sin juzgar efectividad |
| Creative | Qualitative | Creative analiza con criterios estéticos y de producción; Qualitative busca comprensión profunda de experiencias |
| Market | Quantitative | Market busca señales de demanda comercial; Quantitative analiza datos sin sesgo comercial |
| Technical | Experimental | Technical evalúa viabilidad; Experimental prueba una hipótesis con protocolo controlado |
| Product | Educational | Product valida un producto específico; Educational investiga cómo transmitir conocimiento |
| Diagnostic | Technical | Diagnostic busca causa raíz de un fallo; Technical evalúa capacidades de una tecnología |

---

## Referencias cruzadas

- [002-research-lifecycle.md](./002-research-lifecycle.md) — El tipo de investigación influye en qué etapas del lifecycle son obligatorias u opcionales
- [004-research-question-framework.md](./004-research-question-framework.md) — Las preguntas típicas de cada tipo guían la formulación de research questions
- [006-evidence-framework.md](./006-evidence-framework.md) — Los evidence types de cada tipo se mapean a las categorías del Evidence_Framework
- [022-domain-specific-adaptations.md](./022-domain-specific-adaptations.md) — Las adaptaciones por dominio especifican qué tipos son más frecuentes en cada lab

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Decisión] | 100% | Toda la taxonomía y guías de selección son decisiones de diseño metodológico |
