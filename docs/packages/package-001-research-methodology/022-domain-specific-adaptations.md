# 022 — Domain-Specific Adaptations

[Decisión]

## Propósito

Este documento define el **framework de adaptación por dominio** de la metodología de investigación LabOS. Establece qué elementos son fijos (no negociables, universales) y cuáles son variables (adaptables según el dominio), documenta adaptaciones para los dominios activos del portafolio, y provee un template para incorporar nuevos dominios.

La metodología base es universal. Las adaptaciones permiten que cada lab opere con los métodos de evidencia, validación y herramientas apropiados a su contexto sin violar los principios fundacionales.

---

## 1. Elementos fijos vs elementos variables

### 1.1 Elementos fijos (no adaptables)

Los siguientes elementos son **obligatorios en toda investigación**, independientemente del dominio. Provienen de los principios fundacionales (001-research-principles), el evidence framework (006-evidence-framework) y el lifecycle (002-research-lifecycle). [Decisión]

| # | Elemento fijo | Origen | Justificación |
|---|---------------|--------|---------------|
| F1 | Research_Brief obligatorio | Principio 1, Lifecycle Etapa 1 | Sin pregunta documentada no hay investigación dirigida |
| F2 | Timebox o completion criteria obligatorio | Principio 5, R18 | Previene investigaciones indefinidas |
| F3 | Clasificación epistémica obligatoria | Principio 6 | Distingue hechos de hipótesis en todo dominio |
| F4 | Source registration obligatoria | Principio 8, R7 | Toda fuente debe evaluarse antes de citarse |
| F5 | Conclusión obligatoria | Principio 11, R12 | Toda investigación produce al menos una conclusión trazable |
| F6 | Asset extraction obligatoria | Principio 7, R15 | Toda investigación produce al menos un activo reutilizable |
| F7 | Human review para conclusiones | Principio 12, R14 | Previene conclusiones sin validación humana |
| F8 | AI outputs no son Primary_Evidence | Principio 9, R22 | Contenido IA requiere verificación antes de ser evidencia |
| F9 | Escala de confianza 1-5 | Evidence Framework Sección 2 | Toda evidencia se evalúa en la misma escala |
| F10 | 12 categorías de evidencia mutuamente exclusivas | Evidence Framework Sección 1 | Taxonomía universal de clasificación |
| F11 | Documentación de limitaciones | Principio 12, R13 | Honestidad sobre incertidumbre en todo dominio |
| F12 | Trazabilidad fuente → conclusión | Principio 3 | Cadena verificable en toda investigación |
| F13 | Registro de resultados negativos | Evidence Framework Sección 5.3 | Paridad entre resultados positivos y negativos |
| F14 | Quality gates del lifecycle | R29 | Puntos de control universales |

### 1.2 Elementos variables (adaptables por dominio)

Los siguientes elementos pueden personalizarse según las características del dominio sin violar los elementos fijos. [Decisión]

| # | Elemento variable | Qué se adapta | Restricción |
|---|-------------------|---------------|-------------|
| V1 | Tipos de evidencia priorizados | Qué categorías son más frecuentes/relevantes en el dominio | No puede eliminar categorías; solo prioriza |
| V2 | Métodos de validación disponibles | Cómo se validan hipótesis (experimento, observación, análisis, etc.) | Debe existir al menos 1 método documentado |
| V3 | Herramientas específicas del dominio | Herramientas adicionales al stack base | No reemplaza fuente de verdad (GitHub) |
| V4 | Nivel de formalidad del experiment design | Protocolo completo vs diseño simplificado | Debe documentar variables y criterio de éxito |
| V5 | Tipos de activos más probables | Qué tipo de asset se extrae típicamente | No puede omitir la extracción |
| V6 | Métricas de éxito específicas | Cómo se mide el éxito investigativo en el dominio | No reemplaza métricas generales (R24) |
| V7 | Constraints regulatorios o éticos | Restricciones adicionales por regulación o sensibilidad | Solo puede agregar restricciones, no relajarlas |
| V8 | Research types más frecuentes | Qué tipos de investigación predominan | Referencia a taxonomía de 003-research-types |
| V9 | Alternativas a experimentación controlada | Métodos cuando no se puede aislar variables | Obligatorio si el dominio no permite experimentos controlados |
| V10 | Ciclo de obsolescencia de evidencia | Cuánto tiempo la evidencia mantiene validez | No puede declarar evidencia permanente sin justificación |

---

## 2. Adaptaciones por dominio

### 2.1 Technical Research

**Dominio:** Investigación técnica en infraestructura, desarrollo de software, DevOps, AIOps, arquitectura de sistemas.  
**Labs relacionados:** SoftwareFactoryAgentsAI, SentinelOps

| Aspecto | Adaptación |
|---------|-----------|
| **Evidence types priorizados** | Measurement, Experiment Result, Official Documentation, Primary Evidence (benchmarks reproducibles) |
| **Validation methods** | Proof of concept, benchmark controlado, A/B test, load test, configuración reproducible, code review |
| **Tools** | Deepnote (notebooks de análisis), GitHub (código, configuraciones, IaC), Kiro (specs), herramientas de profiling y monitoring |
| **Constraints** | Versiones cambian rápidamente; evidencia puede expirar con nueva release; documentar versiones exactas siempre |
| **Typical assets** | Technical Asset (código, configuraciones, arquitecturas), Knowledge Asset (comparativas, decisiones arquitectónicas) |
| **Special rules** | Toda configuración debe ser reproducible con versiones exactas documentadas. Los benchmarks deben especificar hardware, OS, y condiciones de ejecución. Evidencia de más de 12 meses requiere re-validación si la tecnología tiene releases frecuentes. |
| **Research types frecuentes** | Experimental, Technical, Comparative, Diagnostic |
| **Alternativas a experimentación** | N/A — la experimentación controlada es generalmente posible en este dominio |
| **Ciclo de obsolescencia** | 6-18 meses para tecnologías con releases frecuentes; 2-3 años para estándares estables |

**Ejemplo de aplicación:**

> **Escenario:** Investigar si una arquitectura event-driven reduce la latencia de procesamiento en SentinelOps comparada con la arquitectura request-response actual.  
> **Pasos metodológicos:** (1) Research Brief con pregunta sobre latencia, (2) Scope: comparar 2 arquitecturas en un servicio específico, timebox 16h, (3) PoC de ambas arquitecturas en entorno staging, (4) Benchmark controlado con carga sintética, (5) Conclusión con mediciones p50/p95/p99.  
> **Output esperado:** Technical Asset (PoC documentado) + Knowledge Asset (comparativa arquitectónica con datos).

---

### 2.2 Quantitative Research

**Dominio:** Trading algorítmico, análisis cuantitativo, modelado estadístico, ciencia de datos.  
**Labs relacionados:** Crypto Scalping Core, Atlas Wealth Labs

| Aspecto | Adaptación |
|---------|-----------|
| **Evidence types priorizados** | Measurement, Experiment Result, Market Data, Scientific Literature (papers de finanzas cuantitativas) |
| **Validation methods** | Backtesting con datos históricos, análisis estadístico (significance tests), out-of-sample testing, paper trading, walk-forward analysis |
| **Tools** | Deepnote (análisis cuantitativo, notebooks), GitHub (estrategias, datasets, modelos), herramientas de backtesting específicas |
| **Constraints** | Datos históricos no garantizan resultados futuros; riesgo de overfitting; survivorship bias en datos; market regime changes invalidan modelos |
| **Typical assets** | Data Asset (datasets curados, benchmarks), Technical Asset (modelos, estrategias), Knowledge Asset (análisis de mercado) |
| **Special rules** | Declarar limitaciones del backtesting explícitamente. No confundir correlación con causación. Documentar periodos de datos con fechas exactas. Reportar drawdown máximo junto a retorno. Separar análisis in-sample de out-of-sample. |
| **Research types frecuentes** | Quantitative, Experimental, Comparative, Exploratory |
| **Alternativas a experimentación** | Paper trading (simulación sin capital real), análisis de escenarios históricos, Monte Carlo simulation |
| **Ciclo de obsolescencia** | 3-12 meses para estrategias de trading; datos de mercado históricos no expiran pero su relevancia predictiva sí |

**Ejemplo de aplicación:**

> **Escenario:** Investigar si una estrategia de mean-reversion en pares de crypto genera alpha consistente en timeframes de 5 minutos.  
> **Pasos metodológicos:** (1) Research Brief con hipótesis de trading, (2) Scope: BTC/ETH par, datos de 6 meses, timebox 12h, (3) Backtesting con train/test split 70/30, (4) Análisis estadístico de resultados (Sharpe, drawdown, win rate), (5) Conclusión con limitaciones de backtesting documentadas.  
> **Output esperado:** Data Asset (resultados de backtest) + Knowledge Asset (análisis de viabilidad) + Technical Asset (código de estrategia si viable).

---

### 2.3 Incident Research

**Dominio:** Diagnóstico de incidentes, postmortems, análisis de causa raíz, resolución de problemas operativos.  
**Labs relacionados:** SentinelOps, SoftwareFactoryAgentsAI

| Aspecto | Adaptación |
|---------|-----------|
| **Evidence types priorizados** | Direct Observation, Measurement (logs, métricas), Primary Evidence (timeline de eventos), Inference (correlación temporal) |
| **Validation methods** | Root cause analysis (5 Whys, Fishbone), reproducción en entorno controlado, correlación de timeline, análisis de logs |
| **Tools** | GitHub (postmortems, runbooks), Deepnote (análisis de logs), ChatGPT (generación de hipótesis de causa raíz), herramientas de observabilidad |
| **Constraints** | Tiempo-sensible (puede requerir acción antes de análisis completo); evidencia efímera (logs rotan); presión por resolución rápida |
| **Typical assets** | Knowledge Asset (postmortem documentado), Technical Asset (fix, runbook, playbook de respuesta) |
| **Special rules** | Se permiten conclusiones parciales si el incidente requiere resolución urgente; completar análisis post-resolución es obligatorio. El timebox inicial puede ser tan corto como 2 horas para la fase de mitigación. Documentar la timeline antes de formular hipótesis. Separar mitigación (acción inmediata) de resolución (causa raíz). |
| **Research types frecuentes** | Diagnostic, Technical, Exploratory |
| **Alternativas a experimentación** | Reproducción parcial en staging, análisis de correlación temporal, comparación con incidentes anteriores similares |
| **Ciclo de obsolescencia** | Postmortems no expiran como referencia; fixes técnicos expiran con cambios de arquitectura |

**Ejemplo de aplicación:**

> **Escenario:** Un servicio de SentinelOps experimenta latencia 10x durante 30 minutos sin causa aparente en dashboards estándar.  
> **Pasos metodológicos:** (1) Research Brief urgente (lightweight, <4h), (2) Recolección de evidencia: logs, métricas, timeline de deploys, (3) Correlación temporal entre eventos, (4) Hipótesis de causa raíz + reproducción en staging, (5) Conclusión con root cause identificado y fix.  
> **Output esperado:** Knowledge Asset (postmortem) + Technical Asset (runbook de respuesta para incidentes similares).

---

### 2.4 Market Research

**Dominio:** Investigación de mercado, análisis competitivo, validación de demanda, marketing digital, SaaS, agentes de IA.  
**Labs relacionados:** CommunityManagerBotCrew, Mindzers, SoftwareFactoryAgentsAI

| Aspecto | Adaptación |
|---------|-----------|
| **Evidence types priorizados** | Market Data, Testimony, Direct Observation (comportamiento de usuarios), Measurement (métricas de funnel) |
| **Validation methods** | Landing page test, entrevistas (≥3 independientes), pre-venta, análisis de funnel, análisis competitivo documentado, survey con tamaño mínimo declarado |
| **Tools** | ChatGPT (análisis competitivo, generación de hipótesis), Obsidian (market maps, relaciones), GitHub (documentación formal), herramientas de analytics |
| **Constraints** | Datos de mercado cambian rápidamente; testimonios pueden tener sesgo de confirmación; interés declarado ≠ willingness-to-pay; muestras pequeñas no generalizan |
| **Typical assets** | Knowledge Asset (análisis competitivo, market map), Commercial Asset (propuesta de valor validada, blueprint de servicio) |
| **Special rules** | No confundir interés declarado con willingness-to-pay; validar con transacción real cuando sea posible. Documentar el tamaño de muestra en toda investigación cualitativa. Separar datos de mercado (observados) de proyecciones (inferidos). Señales de demanda deben ser externas al Fundador (alineado con R16.3). |
| **Research types frecuentes** | Market, Exploratory, Descriptive, Product |
| **Alternativas a experimentación** | Análisis competitivo (qué ya existe), entrevistas de problema (no de solución), análisis de búsquedas (search volume), señales de comunidades |
| **Ciclo de obsolescencia** | 3-6 meses para datos de mercado dinámicos; 12-18 meses para análisis competitivos en mercados estables |

**Ejemplo de aplicación:**

> **Escenario:** Investigar si existe demanda para un servicio de community management automatizado con IA en el segmento de startups B2B.  
> **Pasos metodológicos:** (1) Research Brief con hipótesis de mercado, (2) Scope: segmento B2B startups <50 empleados, timebox 8h, (3) Análisis competitivo de 5 competidores, (4) 3 entrevistas con fundadores target, (5) Landing page test con CTA de "join waitlist", (6) Conclusión con nivel de demanda evidenciado.  
> **Output esperado:** Knowledge Asset (análisis competitivo) + Commercial Asset (propuesta de valor si señales positivas).

---

### 2.5 Educational Research

**Dominio:** Aprendizaje de idiomas, formación profesional, diseño instruccional, longevidad cognitiva, desarrollo de habilidades.  
**Labs relacionados:** English Learning Lab, Mindzers

| Aspecto | Adaptación |
|---------|-----------|
| **Evidence types priorizados** | Scientific Literature, Professional Experience, Measurement (pre/post test), Direct Observation (comportamiento de aprendizaje) |
| **Validation methods** | Medición pre/post intervención, tracking longitudinal, comparación con grupo base, self-report con caveats documentados, peer comparison |
| **Tools** | Obsidian (knowledge base pedagógica), NotebookLM (literature review), GitHub (curricula, materiales), Deepnote (análisis de datos de aprendizaje) |
| **Constraints** | Resultados personales no generalizan; efecto placebo y Hawthorne en auto-medición; sesgo de autoinforme; transferencia de aprendizaje difícil de medir |
| **Typical assets** | Educational Asset (tutoriales, guías, materiales de curso), Knowledge Asset (frameworks pedagógicos, comparativas de métodos) |
| **Special rules** | Distinguir evidencia científica (peer-reviewed) de experiencia personal (n=1). Documentar explícitamente limitaciones de n=1. No generalizar resultados personales sin evidencia externa. Declarar el contexto del aprendiz (nivel previo, motivación, tiempo disponible). La efectividad se mide contra un objetivo de aprendizaje declarado, no contra sensación subjetiva. |
| **Research types frecuentes** | Educational, Experimental, Descriptive, Qualitative |
| **Alternativas a experimentación** | Revisión de literatura científica, comparación de métodos documentados, análisis de caso propio con limitaciones explícitas, análisis de cohortes públicas |
| **Ciclo de obsolescencia** | 2-5 años para principios pedagógicos; 6-18 meses para herramientas y plataformas específicas |

**Ejemplo de aplicación:**

> **Escenario:** Investigar si la técnica de spaced repetition con contexto narrativo mejora la retención de vocabulario en inglés comparada con flashcards estándar.  
> **Pasos metodológicos:** (1) Research Brief con hipótesis de aprendizaje, (2) Scope: vocabulario B2, 30 días de tracking, timebox 8h de diseño + 30 días de ejecución, (3) Literature review sobre spaced repetition, (4) Experimento personal (n=1): 50 palabras método A vs 50 palabras método B, (5) Medición pre/post con test estandarizado, (6) Conclusión con limitaciones de n=1.  
> **Output esperado:** Educational Asset (protocolo de estudio documentado) + Knowledge Asset (comparativa de métodos con datos personales y referencia a literatura).

---

### 2.6 Creative Research

**Dominio:** Fotografía, producción musical, creación de contenido, diseño visual, narrativa.  
**Labs relacionados:** Photography Lab, Music Lab

| Aspecto | Adaptación |
|---------|-----------|
| **Evidence types priorizados** | Professional Experience, Direct Observation, Testimony (feedback de audiencia), Measurement (métricas de audiencia/engagement) |
| **Validation methods** | Comparación de portfolio (antes/después), métricas de audiencia, peer review de profesionales, auto-evaluación contra criterios explícitos, A/B test de contenido |
| **Tools** | Obsidian (creative knowledge, referencias), GitHub (procesos, templates, pipelines), herramientas específicas del dominio (Lightroom, DAW, etc.) |
| **Constraints** | Calidad tiene componente subjetivo inevitable; métricas de audiencia no equivalen a calidad artística; tendencias son efímeras; el gusto personal sesga la evaluación |
| **Typical assets** | Educational Asset (tutoriales de técnica), Knowledge Asset (comparativas de herramientas/técnicas), Commercial Asset (contenido monetizable, presets, templates) |
| **Special rules** | Aceptar evaluación subjetiva documentada como válida cuando se explicitan los criterios de juicio. No requerir experimentación estadística para juicios estéticos. Separar métricas de audiencia (engagement, reach) de métricas de calidad (técnica, composición). Documentar los criterios estéticos contra los cuales se evalúa. |
| **Research types frecuentes** | Creative, Exploratory, Comparative, Qualitative |
| **Alternativas a experimentación** | Comparación de portfolio, análisis de referentes profesionales, feedback estructurado de peers, análisis de engagement con audiencia |
| **Ciclo de obsolescencia** | Principios estéticos: 5-10+ años. Herramientas y técnicas: 1-3 años. Tendencias de contenido: 3-12 meses. |

**Ejemplo de aplicación:**

> **Escenario:** Investigar si un workflow de edición fotográfica basado en presets parametrizados reduce el tiempo de post-procesado sin degradar la calidad percibida.  
> **Pasos metodológicos:** (1) Research Brief con pregunta sobre eficiencia de workflow, (2) Scope: retratos en luz natural, 20 fotos de prueba, timebox 8h, (3) Definir criterios de calidad explícitos (exposición, color, skin tones, sharpness), (4) Comparar workflow manual vs presets en las mismas 20 fotos, (5) Medir tiempo + evaluar calidad contra criterios, (6) Conclusión con trade-offs documentados.  
> **Output esperado:** Technical Asset (presets configurados) + Knowledge Asset (comparativa de workflows) + Educational Asset (guía de uso del workflow).

---

### 2.7 Health and Performance Research

**Dominio:** Rendimiento humano, optimización personal, biohacking, longevidad, hábitos, entrenamiento físico.  
**Labs relacionados:** Human Performance Lab

| Aspecto | Adaptación |
|---------|-----------|
| **Evidence types priorizados** | Scientific Literature, Measurement (biomarkers, métricas de rendimiento), Experiment Result (auto-experimentación), Direct Observation |
| **Validation methods** | Tracking longitudinal de métricas personales, revisión de literatura científica, consulta con profesionales de salud, protocolo de auto-experimentación con baseline |
| **Tools** | Deepnote (análisis de datos de tracking), Obsidian (protocolos, knowledge base), NotebookLM (literature review de papers), wearables y herramientas de medición |
| **Constraints** | n=1 experiments (no generalizan); variación individual alta; publication bias en literatura; efectos placebo y nocebo; regulaciones de salud; no se da consejo médico |
| **Typical assets** | Knowledge Asset (protocolos documentados, revisiones de literatura), Data Asset (métricas personales anonimizadas), Educational Asset (guías basadas en evidencia) |
| **Special rules** | **Requiere human review obligatoria** para cualquier conclusión que se aplique a decisiones de salud. Documentar explícitamente que n=1 no generaliza. No formular recomendaciones de salud a terceros. Declarar que los resultados personales son anecdóticos sin evidencia adicional. Distinguir entre lo que la ciencia dice y lo que la experiencia personal sugiere. Consultar profesional antes de protocolos con riesgo. |
| **Research types frecuentes** | Experimental (auto-experimentación), Descriptive, Quantitative, Educational |
| **Alternativas a experimentación** | Revisión sistemática de literatura, tracking observacional sin intervención, consulta con profesionales, análisis de cohortes publicadas |
| **Ciclo de obsolescencia** | Principios fisiológicos: 5-10+ años. Suplementos y protocolos específicos: 1-3 años (nueva evidencia). Herramientas de tracking: 1-2 años. |

**Ejemplo de aplicación:**

> **Escenario:** Investigar si un protocolo de exposición a frío (cold exposure) de 2 minutos diarios mejora métricas de HRV (Heart Rate Variability) en un periodo de 30 días.  
> **Pasos metodológicos:** (1) Research Brief con hipótesis de rendimiento, (2) Literature review sobre cold exposure y HRV (buscar meta-análisis), (3) Baseline: 7 días de medición HRV sin intervención, (4) Protocolo: 30 días de cold exposure + medición diaria, (5) Análisis estadístico pre/post con limitaciones de n=1, (6) Conclusión distinguiendo "mi experiencia" de "lo que la ciencia dice".  
> **Output esperado:** Knowledge Asset (revisión de literatura + resultados personales) + Data Asset (datos de HRV anonimizados) + Educational Asset (protocolo documentado con caveats).

---

### 2.8 Finance Research

**Dominio:** Inversiones, wealth management, economía personal, análisis financiero, planificación patrimonial.  
**Labs relacionados:** Atlas Wealth Labs

| Aspecto | Adaptación |
|---------|-----------|
| **Evidence types priorizados** | Market Data, Official Documentation (regulaciones, reportes de reguladores), Scientific Literature (papers de finanzas), Measurement (rendimientos históricos), Secondary Evidence (reportes de instituciones) |
| **Validation methods** | Análisis histórico documentado, scenario modeling (stress tests), paper portfolio (sin capital real), consulta con profesional financiero, comparación con benchmarks establecidos |
| **Tools** | Deepnote (modelos financieros, análisis cuantitativo), GitHub (estrategias, modelos, documentación), NotebookLM (research papers, documentos regulatorios) |
| **Constraints** | Regulaciones financieras aplican; past performance ≠ future results (declarar siempre); conflict of interest debe declararse; no se provee asesoramiento financiero; riesgo de sesgo de supervivencia en datos |
| **Typical assets** | Knowledge Asset (análisis financiero, comparativas de instrumentos), Data Asset (modelos, datasets), Technical Asset (herramientas de cálculo, simuladores) |
| **Special rules** | **Declarar explícitamente que el contenido no constituye asesoramiento financiero.** Documentar assumptions de todo modelo con sus limitaciones. Separar análisis (descriptivo) de recomendación personal (prescriptivo). Declarar horizonte temporal de validez. No presentar rendimientos pasados como predicción. Cumplir con regulaciones locales de contenido financiero si se publica. |
| **Research types frecuentes** | Quantitative, Descriptive, Comparative, Market |
| **Alternativas a experimentación** | Análisis histórico con múltiples escenarios, paper portfolios, Monte Carlo simulation, comparación con benchmarks (S&P 500, índices relevantes) |
| **Ciclo de obsolescencia** | Principios financieros: 5-10+ años. Datos de mercado: actuales al momento de consulta. Regulaciones: verificar anualmente. Estrategias tácticas: 6-18 meses. |

**Ejemplo de aplicación:**

> **Escenario:** Investigar si una estrategia de DCA (Dollar Cost Averaging) en ETFs de renta variable global supera a lump-sum investing para horizontes de 10+ años en el contexto de un inversionista con ingreso mensual.  
> **Pasos metodológicos:** (1) Research Brief con pregunta de inversión, (2) Scope: ETFs globales diversificados, datos 2000-2024, timebox 12h, (3) Literature review de estudios DCA vs lump-sum, (4) Análisis cuantitativo con datos históricos (múltiples ventanas de 10 años), (5) Scenario modeling con diferentes condiciones de mercado, (6) Conclusión con declaración de "no es asesoramiento financiero" y limitaciones de datos históricos.  
> **Output esperado:** Knowledge Asset (análisis comparativo con datos) + Data Asset (modelo de simulación) + Educational Asset (guía de DCA con limitaciones).

---

## 3. Template para nuevos dominios

Cuando un nuevo lab se incorpora al portafolio LabOS o se identifica un dominio investigativo no cubierto, se documenta su adaptación utilizando la siguiente estructura. [Decisión]

```markdown
### N.N [Nombre del dominio] Research

**Dominio:** [Descripción del dominio en 1-2 oraciones]  
**Labs relacionados:** [Labs del portafolio que operan en este dominio]

| Aspecto | Adaptación |
|---------|-----------|
| **Evidence types priorizados** | [Mínimo 1 categoría del Evidence Framework] |
| **Validation methods** | [Mínimo 1 método de validación disponible] |
| **Tools** | [Herramientas del stack LabOS + herramientas específicas] |
| **Constraints** | [Restricciones propias del dominio] |
| **Typical assets** | [Tipos de assets más probables] |
| **Special rules** | [Reglas adicionales específicas del dominio] |
| **Research types frecuentes** | [Referencia a taxonomía de 003-research-types] |
| **Alternativas a experimentación** | [Obligatorio si el dominio no permite experimentación controlada] |
| **Ciclo de obsolescencia** | [Tiempo estimado de validez de la evidencia por tipo] |

**Ejemplo de aplicación:**

> **Escenario:** [Situación concreta de investigación en el dominio]  
> **Pasos metodológicos:** [Secuencia abreviada de pasos]  
> **Output esperado:** [Tipos de assets que se producirían]
```

### 3.1 Checklist de validación para nueva adaptación

Antes de considerar completa una nueva Domain_Adaptation, verificar: [Decisión]

- [ ] Todos los campos de la tabla tienen al menos un valor documentado
- [ ] Los evidence types referenciados existen en la taxonomía de 12 categorías (006-evidence-framework)
- [ ] Al menos 1 método de validación está documentado con suficiente detalle para ser ejecutable
- [ ] Si el dominio no permite experimentación controlada, la sección "Alternativas a experimentación" está completa
- [ ] Las special rules no contradicen ningún elemento fijo (verificar contra tabla 1.1)
- [ ] El ejemplo de aplicación es concreto y sigue el lifecycle documentado
- [ ] Los research types referenciados existen en la taxonomía de 003-research-types
- [ ] Los assets típicos referenciados coinciden con los 5 tipos definidos en R15

---

## 4. Verificación de no-contradicción

### 4.1 Regla de no-contradicción

Ninguna adaptación de dominio puede contradecir, relajar o eliminar un elemento fijo. [Decisión] Las adaptaciones solo pueden:

- **Agregar** restricciones (special rules más estrictas que las generales)
- **Priorizar** elementos variables (qué evidencia es más relevante)
- **Especificar** métodos (cómo se valida en este dominio concreto)
- **Contextualizar** herramientas (qué herramientas adicionales se usan)

Las adaptaciones **no pueden**:

- Eliminar la obligación de Research_Brief
- Relajar la escala de confianza o permitir confidence > ceiling por categoría
- Omitir la clasificación epistémica
- Tratar AI outputs como Primary_Evidence
- Saltear human review en conclusiones
- Declarar que un dominio no requiere asset extraction
- Eliminar la documentación de limitaciones

### 4.2 Matriz de verificación

La siguiente tabla confirma que cada dominio respeta los elementos fijos:

| Elemento fijo | Technical | Quantitative | Incident | Market | Educational | Creative | Health | Finance |
|---------------|:---------:|:------------:|:--------:|:------:|:-----------:|:--------:|:------:|:-------:|
| F1 Research_Brief obligatorio | ✓ | ✓ | ✓* | ✓ | ✓ | ✓ | ✓ | ✓ |
| F2 Timebox obligatorio | ✓ | ✓ | ✓* | ✓ | ✓ | ✓ | ✓ | ✓ |
| F3 Clasificación epistémica | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| F4 Source registration | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| F5 Conclusión obligatoria | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| F6 Asset extraction | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| F7 Human review | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓+ | ✓ |
| F8 AI ≠ Primary_Evidence | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| F9 Escala confianza 1-5 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| F10 12 categorías evidencia | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| F11 Documentar limitaciones | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| F12 Trazabilidad | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| F13 Registro negativos | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| F14 Quality gates | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

**Leyenda:**
- ✓ = Cumple sin modificación
- ✓* = Cumple con adaptación: Incident Research permite Research_Brief lightweight y timebox corto (≥2h) para fase de mitigación, pero ambos siguen siendo obligatorios
- ✓+ = Cumple con restricción adicional: Health Research **refuerza** este elemento requiriendo human review para cualquier conclusión aplicada a salud

### 4.3 Protocolo de verificación

Al agregar o modificar una adaptación de dominio, ejecutar el siguiente protocolo: [Decisión]

1. Listar cada special rule de la adaptación
2. Para cada special rule, verificar que no contradice ningún elemento fijo (F1-F14)
3. Si una special rule parece entrar en conflicto, documentar:
   - El conflicto aparente
   - La resolución (la special rule se ajusta para respetar el elemento fijo)
   - Cómo el dominio cumple el elemento fijo a pesar de la adaptación
4. Si la resolución no es posible sin violar un elemento fijo, la adaptación no se aprueba

---

## 5. Relación con labs del portafolio

El framework de adaptación conecta directamente con los labs activos del portafolio LabOS. [Decisión]

| Lab | Dominio(s) de adaptación aplicables |
|-----|--------------------------------------|
| SoftwareFactoryAgentsAI | Technical Research, Incident Research |
| SentinelOps | Technical Research, Incident Research |
| Crypto Scalping Core | Quantitative Research |
| Atlas Wealth Labs | Finance Research, Quantitative Research |
| CommunityManagerBotCrew | Market Research |
| Mindzers | Market Research, Educational Research |
| English Learning Lab | Educational Research |
| Photography Lab | Creative Research |
| Music Lab | Creative Research |
| Human Performance Lab | Health and Performance Research |

Un lab puede operar bajo múltiples adaptaciones de dominio simultáneamente si sus investigaciones abarcan más de un dominio. En ese caso, se aplica la adaptación más restrictiva para los elementos compartidos y se documentan los elementos específicos de cada dominio por separado.

---

## Trazabilidad

| Sección del documento | Requirements cubiertos |
|-----------------------|-----------------------|
| Sección 1 (Elementos fijos vs variables) | R23.1 |
| Sección 2 (Adaptaciones por dominio - 8 dominios) | R23.2, R23.3 |
| Sección 3 (Template para nuevos dominios) | R23.5 |
| Sección 4 (Verificación de no-contradicción) | R23.6 |
| Sección 5 (Relación con labs) | R23.6 |
| Ejemplos de aplicación en cada dominio | R23.2 (scenario, steps, output) |
| Alternativas a experimentación por dominio | R23.4 |

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho] | 0 | 0% |
| [Decisión] | 12 | 100% |
| [Hipótesis] | 0 | 0% |
| [Visión] | 0 | 0% |

Las decisiones incluyen: framework de fijos/variables, 8 adaptaciones de dominio, template para nuevos dominios, regla de no-contradicción, protocolo de verificación, y mapeo a labs del portafolio.
