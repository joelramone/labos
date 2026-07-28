# Design Document

## Overview

Este documento define el diseño completo de Package 001 — Research Methodology. El diseño traduce los 36 requirements aprobados en una arquitectura documental, modelos conceptuales, workflows y matrices de trazabilidad que guiarán la producción de los 26 documentos del package y los 9 templates.

El diseño no produce software, APIs, bases de datos ni infraestructura técnica. Produce la estructura lógica y conceptual que permitirá escribir cada documento del package con coherencia interna y alineación con Package 000 — Foundation.

---

## 1. Arquitectura documental

### 1.1 Estructura del package

```
docs/packages/package-001-research-methodology/
├── README.md                          — Índice, glosario autoritativo, estado del package
├── 001-research-principles.md         — Principios que gobiernan toda investigación
├── 002-research-lifecycle.md          — Lifecycle completo con etapas y transiciones
├── 003-research-types.md              — Taxonomía de 12 tipos de investigación
├── 004-research-question-framework.md — Framework para formular preguntas
├── 005-hypothesis-framework.md        — Tipos y estructura de hipótesis
├── 006-evidence-framework.md          — Categorías, niveles de confianza, modelo
├── 007-source-evaluation.md           — Criterios de evaluación de fuentes
├── 008-research-workflow.md           — Workflow general del proceso investigativo
├── 009-tooling-workflow.md            — Roles, handoffs y flujos entre herramientas
├── 010-deepnote-guidelines.md         — Guía específica para uso de Deepnote
├── 011-notebooklm-guidelines.md       — Guía específica para uso de NotebookLM
├── 012-chatgpt-guidelines.md          — Guía específica para uso de ChatGPT Projects
├── 013-obsidian-guidelines.md         — Guía específica para uso de Obsidian
├── 014-experiment-design.md           — Framework de diseño de experimentos
├── 015-research-journal.md            — Estructura y reglas del journal
├── 016-decision-log.md                — Estructura y reglas del decision log
├── 017-conclusion-framework.md        — Framework para formular conclusiones
├── 018-research-to-asset.md           — Proceso de extracción de activos
├── 019-research-to-product-hypothesis.md — Derivación de hipótesis de producto
├── 020-quality-gates.md               — Quality gates con checklists
├── 021-research-ethics-and-safety.md  — Ética, privacidad, PI, IA responsable
├── 022-domain-specific-adaptations.md — Adaptaciones por dominio
├── 023-research-metrics.md            — Métricas e indicadores de salud
├── 024-anti-patterns.md               — Anti-patrones con correcciones
├── 025-package-summary.md             — Consolidación y declaración de consistencia
└── 026-package-review.md              — Checklist de aprobación y trazabilidad
```


### 1.2 Estructura de templates

```
docs/templates/research/
├── research-brief-template.md         — Intake y definición inicial
├── research-plan-template.md          — Plan con scope, timebox, recursos
├── source-register-template.md        — Registro de fuentes con evaluación
├── experiment-template.md             — Diseño de experimento
├── research-journal-template.md       — Entradas cronológicas
├── decision-log-template.md           — Registro de decisiones
├── conclusion-template.md             — Formulación de conclusión
├── research-asset-handoff-template.md — Transferencia a repositorio de activos
└── research-review-template.md        — Revisión final de investigación
```

### 1.3 Propósito de cada documento

| # | Documento | Propósito | Requirements cubiertos |
|---|-----------|-----------|----------------------|
| 0 | README.md | Índice central, glosario autoritativo, declaración de estado | R34 |
| 1 | 001-research-principles.md | Definir los ≥10 principios fundacionales de investigación | R1 |
| 2 | 002-research-lifecycle.md | Diseñar las 16 etapas con inputs/outputs/gates | R2, R26 |
| 3 | 003-research-types.md | Taxonomía de 12 tipos con guía de selección | R27 |
| 4 | 004-research-question-framework.md | Estructura y calidad de preguntas de investigación | R4 |
| 5 | 005-hypothesis-framework.md | 6 tipos de hipótesis con modelo completo | R9 |
| 6 | 006-evidence-framework.md | 12 categorías, escala de confianza, modelo | R8 |
| 7 | 007-source-evaluation.md | 10 criterios de evaluación, umbral mínimo | R7 |
| 8 | 008-research-workflow.md | Flujo general de trabajo investigativo | R3, R5, R6, R11 |
| 9 | 009-tooling-workflow.md | Roles de herramientas, handoffs, fuentes de verdad | R28 |
| 10 | 010-deepnote-guidelines.md | Uso de Deepnote: análisis de datos, notebooks | R28 |
| 11 | 011-notebooklm-guidelines.md | Uso de NotebookLM: consulta documental | R28, R22 |
| 12 | 012-chatgpt-guidelines.md | Uso de ChatGPT: contexto, debate, borradores | R28, R22 |
| 13 | 013-obsidian-guidelines.md | Uso de Obsidian: conocimiento permanente | R28 |
| 14 | 014-experiment-design.md | Protocolo de experimentos, alternativas | R10 |
| 15 | 015-research-journal.md | Estructura del journal, cuándo mantenerlo | R32 |
| 16 | 016-decision-log.md | Estructura del decision log, triggers | R32 |
| 17 | 017-conclusion-framework.md | Formulación de conclusiones trazables | R12 |
| 18 | 018-research-to-asset.md | Proceso de extracción, tipos, handoff | R15 |
| 19 | 019-research-to-product-hypothesis.md | Derivación comercial prudente | R16, R17, R31 |
| 20 | 020-quality-gates.md | 7 quality gates con checklists | R29 |
| 21 | 021-research-ethics-and-safety.md | Ética, privacidad, PI, IA responsable | R20, R21, R22 |
| 22 | 022-domain-specific-adaptations.md | Adaptaciones para 8+ dominios | R23 |
| 23 | 023-research-metrics.md | Métricas, review cadence, warning signals | R24 |
| 24 | 024-anti-patterns.md | Anti-patrones con correcciones | R30 |
| 25 | 025-package-summary.md | Consolidación de decisiones, consistencia | R34, R35 |
| 26 | 026-package-review.md | Checklist de aprobación, trazabilidad | R25, R35 |


---

## 2. Research Lifecycle

### 2.1 Lifecycle completo

El lifecycle define 16 etapas secuenciales con posibilidad de loop-back documentado.

#### Etapa 1: Intake

| Campo | Valor |
|-------|-------|
| **Propósito** | Capturar el trigger de investigación y realizar clasificación inicial |
| **Inputs** | Pregunta, problema, idea, incidente, observación, oportunidad, documento, dataset |
| **Actividades** | Identificar trigger, clasificar tipo de entrada, estimar esfuerzo, crear Research_Brief inicial |
| **Outputs** | Research_Brief (borrador) con trigger, contexto, clasificación de dominio, effort category |
| **Responsable** | Fundador |
| **Herramientas** | ChatGPT Projects (contextualización), GitHub (registro), Obsidian (captura rápida) |
| **Quality Gate** | Research_Brief existe con todos los campos obligatorios completos |
| **Estado resultante** | Proposed |

#### Etapa 2: Problem Framing

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

#### Etapa 3: Research Question

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

#### Etapa 4: Scope

| Campo | Valor |
|-------|-------|
| **Propósito** | Delimitar alcance, timebox y criterios de finalización |
| **Inputs** | Research questions aprobadas |
| **Actividades** | Definir inclusiones/exclusiones, timebox, deadline, completion criteria, max sources |
| **Outputs** | Scope document con boundaries, timebox, deadline, exit criteria |
| **Responsable** | Fundador |
| **Herramientas** | GitHub (registro formal), ChatGPT (estimación de esfuerzo) |
| **Quality Gate** | Timebox definido, completion criteria explícitos, exclusiones documentadas |
| **Estado resultante** | Planned |

#### Etapa 5: Assumptions

| Campo | Valor |
|-------|-------|
| **Propósito** | Surfacear premisas ocultas antes de invertir esfuerzo investigativo |
| **Inputs** | Scope definido, research questions |
| **Actividades** | Listar assumptions, clasificar por tipo, evaluar confianza, documentar impacto si incorrectas |
| **Outputs** | Assumptions register con: statement, type, confidence, impact-if-wrong, validation approach |
| **Responsable** | Fundador |
| **Herramientas** | ChatGPT (challenge de assumptions), Obsidian (registro) |
| **Quality Gate** | ≥3 assumptions documentadas, cada una con confidence level y validation plan |
| **Estado resultante** | Planned |


#### Etapa 6: Source Collection

| Campo | Valor |
|-------|-------|
| **Propósito** | Recopilar y registrar fuentes relevantes con evaluación de calidad |
| **Inputs** | Research questions, scope, assumptions |
| **Actividades** | Buscar fuentes, evaluar calidad contra 10 criterios, registrar en Source_Register, clasificar por tipo |
| **Outputs** | Source_Register poblado con fuentes evaluadas, gaps de fuentes documentados |
| **Responsable** | Fundador |
| **Herramientas** | NotebookLM (consulta documental), ChatGPT (búsqueda contextual), Deepnote (datasets), GitHub (registro) |
| **Quality Gate** | ≥1 fuente con calidad suficiente para cada research question, gaps documentados |
| **Estado resultante** | In Progress |

#### Etapa 7: Evidence Evaluation

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

#### Etapa 8: Analysis

| Campo | Valor |
|-------|-------|
| **Propósito** | Sintetizar evidencia, identificar patrones y formular hipótesis |
| **Inputs** | Evidence register evaluado |
| **Actividades** | Analizar patrones, comparar evidencia, formular hipótesis, identificar gaps, triangular fuentes |
| **Outputs** | Análisis documentado con: patrones identificados, hipótesis formuladas, gaps, preguntas emergentes |
| **Responsable** | Fundador |
| **Herramientas** | Deepnote (análisis cuantitativo), NotebookLM (síntesis), ChatGPT (debate), Obsidian (mapeo conceptual) |
| **Quality Gate** | Análisis responde (parcial o totalmente) a las research questions, hipótesis formuladas correctamente |
| **Estado resultante** | In Progress |

#### Etapa 9: Experimentation

| Campo | Valor |
|-------|-------|
| **Propósito** | Validar hipótesis mediante experimentos controlados o métodos alternativos |
| **Inputs** | Hipótesis formuladas, protocol de experimento |
| **Actividades** | Ejecutar experimento según protocol, registrar resultados, documentar desviaciones, evaluar outcomes |
| **Outputs** | Experiment records con: resultados, desviaciones, decisiones, evidencia generada |
| **Responsable** | Fundador |
| **Herramientas** | Deepnote (notebooks), GitHub (código, datos), herramientas específicas del dominio |
| **Quality Gate** | Resultados documentados (positivos, negativos o inconclusos), hypothesis updated con verdict |
| **Estado resultante** | In Progress |
| **Nota** | Etapa opcional si el dominio no permite experimentación controlada; en ese caso, usar métodos alternativos documentados en Domain_Adaptation |

#### Etapa 10: Findings

| Campo | Valor |
|-------|-------|
| **Propósito** | Consolidar todos los resultados en hallazgos interpretables |
| **Inputs** | Evidence register, experiment records, analysis output |
| **Actividades** | Sintetizar hallazgos, clasificar por tipo y confianza, documentar relación con research questions |
| **Outputs** | Findings document con: hallazgos clasificados, confidence levels, relation to questions |
| **Responsable** | Fundador |
| **Herramientas** | Obsidian (síntesis), ChatGPT (revisión), GitHub (documentación formal) |
| **Quality Gate** | Cada research question tiene al menos un finding asociado (aunque sea "insuficiente evidencia") |
| **Estado resultante** | In Progress |


#### Etapa 11: Conclusion

| Campo | Valor |
|-------|-------|
| **Propósito** | Formular conclusiones trazables que respondan las research questions |
| **Inputs** | Findings consolidados |
| **Actividades** | Redactar conclusión, trazar a evidencia, clasificar confidence, documentar limitaciones, formular recomendaciones |
| **Outputs** | Conclusion document con: question answered, evidence summary, confidence, limitations, implications, actions, open questions |
| **Responsable** | Fundador |
| **Herramientas** | ChatGPT (refinamiento), Obsidian (conexión a conocimiento), GitHub (documento formal) |
| **Quality Gate** | Conclusión trazable a ≥1 evidencia, limitaciones documentadas, uncertainty section presente |
| **Estado resultante** | Under Review |

#### Etapa 12: Review

| Campo | Valor |
|-------|-------|
| **Propósito** | Validar calidad, completitud y compliance de la investigación |
| **Inputs** | Conclusion, Research_Journal, Source_Register, all artifacts |
| **Actividades** | Evaluar contra checklist de revisión, verificar trazabilidad, validar compliance ético, confirmar human review |
| **Outputs** | Review result: approved, approved-with-limitations, or requires-rework |
| **Responsable** | Fundador (human review obligatorio) |
| **Herramientas** | GitHub (review formal), checklist de 026-package-review |
| **Quality Gate** | Checklist completado, deficiencias documentadas y remediadas si aplica |
| **Estado resultante** | Completed (si aprobado), In Progress (si requiere rework) |

#### Etapa 13: Asset Extraction

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

#### Etapa 14: Product Hypothesis

| Campo | Valor |
|-------|-------|
| **Propósito** | Evaluar si existe una oportunidad comercial derivada de la investigación |
| **Inputs** | Assets extraídos, conclusions, evidence of demand |
| **Actividades** | Evaluar oportunidad, formular Product_Hypothesis o Revenue_Hypothesis si evidencia lo soporta, documentar ausencia de señal comercial si no |
| **Outputs** | Product_Hypothesis (si aplica) o declaración documentada de ausencia de oportunidad comercial |
| **Responsable** | Fundador |
| **Herramientas** | ChatGPT (análisis de mercado), GitHub (documentación), Obsidian (conexiones) |
| **Quality Gate** | Si se formula hypothesis: todos los campos requeridos completos, evidencia referenciada. Si no se formula: justificación documentada |
| **Estado resultante** | Converted to Asset (sin hypothesis) o Published (si hypothesis pasa gate comercial) |
| **Nota** | Etapa que permite concluir sin producto comercial. No fuerza monetización |

#### Etapa 15: Publication or Archive

| Campo | Valor |
|-------|-------|
| **Propósito** | Decidir destino final: publicación externa, archivo interno, o ambos |
| **Inputs** | Investigación completa con assets y hypothesis (si aplica) |
| **Actividades** | Evaluar idoneidad para publicación, preparar para archivo, verificar privacy/IP compliance |
| **Outputs** | Decision de publicación/archivo documentada, assets en repositorio final |
| **Responsable** | Fundador |
| **Herramientas** | GitHub (versionado final), Obsidian (índice de conocimiento) |
| **Quality Gate** | Privacy/IP checklist aprobado, formato adecuado para destino |
| **Estado resultante** | Published o Archived |

#### Etapa 16: Feedback and Iteration

| Campo | Valor |
|-------|-------|
| **Propósito** | Capturar feedback, identificar mejoras y alimentar futuras investigaciones |
| **Inputs** | Investigación publicada/archivada, feedback externo o interno |
| **Actividades** | Registrar feedback, identificar mejoras al proceso, documentar preguntas derivadas, actualizar métricas |
| **Outputs** | Feedback record, potential new Research_Briefs, process improvement notes |
| **Responsable** | Fundador |
| **Herramientas** | Obsidian (conexiones), GitHub (issues), ChatGPT (reflexión) |
| **Quality Gate** | Feedback registrado, métricas actualizadas |
| **Estado resultante** | Archived (estado final estable) |


---

## 3. Modelo de estados

### 3.1 Estados de una investigación

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
| **Archived** | Investigación almacenada como referencia, ciclo cerrado | Archive |
| **Rejected** | Investigación abandonada antes de conclusión con justificación documentada | Cualquier etapa |

### 3.2 Transiciones permitidas

```
Proposed → Framed          (problem framing completado)
Framed → Planned           (scope y assumptions definidos)
Planned → In Progress      (quality gate de inicio aprobado)
In Progress → In Progress  (avance entre etapas 6-10)
In Progress → Blocked      (dependencia o decisión pendiente)
Blocked → In Progress      (blocker resuelto)
In Progress → Under Review (conclusion formulada)
Under Review → Completed   (review aprobado)
Under Review → In Progress (review requiere rework)
Completed → Converted to Asset (asset extraído)
Converted to Asset → Published (publication gate aprobado)
Converted to Asset → Archived  (sin publicación, archivo directo)
Published → Archived       (ciclo completo)
[Cualquier estado] → Rejected (abandono con justificación)
```

### 3.3 Criterios de transición

| Transición | Criterio |
|------------|----------|
| Proposed → Framed | Research_Brief completo + problem statement documentado + ≥1 research question formulada |
| Framed → Planned | Scope definido con timebox + assumptions documentadas |
| Planned → In Progress | Quality gate de inicio aprobado (Research_Brief, questions, scope, timebox, assumptions) |
| In Progress → Under Review | Conclusión formulada con trazabilidad a evidencia + uncertainty documented |
| Under Review → Completed | Human review aprobado, checklist satisfecho |
| Completed → Converted to Asset | ≥1 asset extraído con metadata completa |
| → Rejected | Justificación documentada + partial findings preserved si existen |


---

## 4. Modelo de artefactos

### 4.1 Artefactos y su relación con el lifecycle

| Artefacto | Creado en etapa | Actualizado en etapas | Propósito |
|-----------|-----------------|----------------------|-----------|
| **Research Brief** | Intake | Problem Framing, Research Question | Documento fundacional de la investigación |
| **Research Plan** | Scope, Assumptions | — | Plan ejecutable con timebox y resources |
| **Source Register** | Source Collection | Evidence Evaluation, Analysis | Registro de todas las fuentes con evaluación |
| **Experiment Record** | Experimentation | — | Protocolo y resultados de cada experimento |
| **Research Journal** | Planned (inicio) | Todas las etapas activas | Registro cronológico continuo |
| **Decision Log** | Planned (inicio) | Todas las etapas donde se toman decisiones | Registro de decisiones con rationale |
| **Conclusion** | Conclusion | Review (si rework) | Síntesis final de la investigación |
| **Asset Handoff** | Asset Extraction | — | Formalización de transferencia a assets repo |
| **Research Review** | Review | — | Evaluación formal de calidad y completitud |

### 4.2 Dependencias entre artefactos

```
Research Brief
    └── Research Plan
         ├── Source Register
         │    └── Evidence (evaluada)
         │         └── Analysis
         │              ├── Hypothesis → Experiment Record
         │              └── Findings
         │                   └── Conclusion
         │                        ├── Asset Handoff
         │                        └── Product Hypothesis
         ├── Research Journal (transversal)
         └── Decision Log (transversal)

Research Review ← depende de todos los artefactos anteriores
```

### 4.3 Artefacto mínimo por effort category

| Effort Category | Artefactos obligatorios | Artefactos opcionales |
|-----------------|------------------------|----------------------|
| Small (<4h) | Research Brief (lightweight), Conclusion | Journal, Source Register |
| Medium (4-16h) | Research Brief, Source Register, Conclusion, Journal, Asset Handoff | Experiment Record, Decision Log |
| Large (>16h) | Todos los artefactos | — |


---

## 5. Tooling Workflow

### 5.1 Roles de herramientas

| Herramienta | Rol principal | Clasificación |
|-------------|--------------|---------------|
| **ChatGPT Projects** | Contexto, debate, borradores, revisión, planes, challenge de ideas | Herramienta de análisis |
| **NotebookLM** | Consulta documental, comparación de fuentes, resúmenes con referencias | Herramienta de análisis |
| **Deepnote** | Análisis de datos, notebooks reproducibles, experimentación, visualizaciones | Herramienta de análisis + Repositorio (notebooks) |
| **Obsidian** | Conocimiento permanente, notas atómicas, relaciones conceptuales, índice personal | Repositorio de conocimiento |
| **GitHub** | Documentación versionada, código, datasets, templates, decisiones, trazabilidad | Fuente de verdad formal |
| **Kiro** | Spec-driven development, requirements, design, tasks, implementación | Herramienta de desarrollo |

### 5.2 Qué se origina en cada herramienta

| Herramienta | Origina |
|-------------|---------|
| ChatGPT Projects | Borradores, análisis exploratorio, planes iniciales, debates estructurados, críticas |
| NotebookLM | Resúmenes documentales, comparaciones de fuentes, respuestas con citas |
| Deepnote | Análisis cuantitativos, visualizaciones, resultados de experimentos de datos |
| Obsidian | Notas atómicas, mapas conceptuales, conexiones entre investigaciones |
| GitHub | Documentos formales, versiones finales, código, datasets, templates, decision records |
| Kiro | Specs, requirements, designs, tasks para features que requieren implementación |

### 5.3 Qué se exporta y versiona

| Herramienta | Se exporta a | Se versiona en |
|-------------|-------------|----------------|
| ChatGPT Projects | GitHub (decisiones, conclusiones refinadas) | No se versiona (temporal) |
| NotebookLM | GitHub (citas verificadas), Obsidian (insights) | No se versiona (temporal) |
| Deepnote | GitHub (notebooks finales, resultados) | GitHub (notebooks como código) |
| Obsidian | GitHub (cuando madura a documento formal) | Obsidian (versionado interno via git) |
| GitHub | — (es el destino final) | GitHub (git nativo) |
| Kiro | GitHub (specs formales) | GitHub (dentro de .kiro/) |

### 5.4 Qué es temporal vs fuente de verdad

| Clasificación | Herramientas | Regla |
|---------------|-------------|-------|
| **Temporal** | ChatGPT Projects, NotebookLM | Outputs son efímeros. Todo lo relevante debe exportarse a GitHub u Obsidian antes de que se pierda contexto |
| **Semi-permanente** | Deepnote, Obsidian | Contenido persiste pero no es fuente de verdad formal hasta que se exporta a GitHub |
| **Fuente de verdad** | GitHub | Documentación formal, decisiones, versiones finales, templates, código |

### 5.5 Qué no debe copiarse entre herramientas

- **Credenciales o tokens**: nunca copiar entre herramientas ni registrar en documentos
- **Datos personales sin anonimización**: no mover a herramientas sin control de acceso
- **AI output sin verificación**: no copiar respuestas de ChatGPT/NotebookLM a GitHub como evidencia verificada
- **Notebooks con datos sensibles**: no exportar a repositorios públicos sin sanitización
- **Contexto de conversación completo**: solo exportar decisiones y conclusiones, no el chat completo

### 5.6 Flujo de información entre herramientas

```
[Trigger: pregunta, problema, idea]
       │
       ▼
ChatGPT Projects ──── debate, exploración, borrador ────┐
       │                                                 │
       ▼                                                 │
NotebookLM ──── consulta de fuentes, comparación ───────┤
       │                                                 │
       ▼                                                 │
Deepnote ──── análisis de datos, experimentación ──────┤
       │                                                 │
       ▼                                                 ▼
Obsidian ◄──── insights validados, notas atómicas ──── [síntesis]
       │
       ▼
GitHub ◄──── documento formal, versión final, activo ── [fuente de verdad]
       │
       ▼
Kiro ◄──── spec para implementación (si aplica) ────── [desarrollo]
```


---

## 6. Evidence Model

### 6.1 Modelo conceptual de evidencia

Modelo documental (no es una base de datos, es una estructura para documentos y templates):

```
Evidence Record
├── evidence_id        : string (formato: EVD-{investigation_id}-{seq})
├── source_id          : string (referencia al Source_Register)
├── evidence_type      : enum (primary, secondary, observation, measurement,
│                              experiment, professional_experience, official_docs,
│                              scientific_literature, market_data, testimony,
│                              inference, opinion)
├── claim              : string (afirmación que esta evidencia soporta)
├── observed_result    : string (qué se observó o midió concretamente)
├── confidence         : integer (1-5)
│   ├── 1: Speculation — sin evidencia directa, inferencia lejana
│   ├── 2: Low — evidencia indirecta, fuente limitada, sin verificación
│   ├── 3: Medium — fuente razonable, evidencia parcial, una confirmación
│   ├── 4: High — múltiples fuentes independientes, evidencia directa
│   └── 5: Very High — reproducible, verificado, múltiples confirmaciones
├── limitations        : string[] (limitaciones conocidas de esta evidencia)
├── collected_at       : date (cuándo se recopiló)
├── verified_by        : string (quién verificó: "human", "unverified", "AI-assisted")
├── verification_note  : string (cómo se verificó, contra qué fuente)
├── status             : enum (pending_verification, verified, contested, superseded, retracted)
└── relevance          : string (relación con la research question)
```

### 6.2 Reglas del evidence model

1. Toda evidencia con `verified_by: "unverified"` no puede soportar una conclusión con confidence > 2.
2. Evidencia tipo `opinion` o `inference` tiene un ceiling de confidence = 3 máximo.
3. Evidencia tipo `AI_generated` (producida por herramientas IA) debe registrarse con `verified_by: "AI-assisted"` y no puede servir como Primary_Evidence hasta verificación contra fuente original.
4. Si dos evidencias con el mismo `claim` tienen `status: contested`, la conclusión debe documentar el conflicto.


---

## 7. Hypothesis Model

### 7.1 Modelo conceptual de hipótesis

```
Hypothesis Record
├── hypothesis_id      : string (formato: HYP-{investigation_id}-{seq})
├── type               : enum (research, technical, product, business, revenue, learning)
├── statement          : string (afirmación clara y falsificable)
├── context            : string (por qué se formula esta hipótesis)
├── assumptions        : string[] (supuestos que deben ser ciertos para que la hipótesis tenga sentido)
├── prior_evidence     : string[] (evidence_ids que motivaron la hipótesis)
├── variables
│   ├── independent    : string[] (qué se manipula o varía)
│   ├── dependent      : string[] (qué se mide)
│   └── controlled     : string[] (qué se mantiene constante)
├── validation_method  : string (cómo se probará)
├── success_criteria   : string (qué resultado confirma la hipótesis)
├── failure_criteria   : string (qué resultado refuta la hipótesis)
├── timebox            : string (tiempo máximo para validar)
├── risks              : string[] (qué puede salir mal durante la validación)
├── result             : enum (pending, confirmed, refuted, inconclusive, revised, abandoned)
├── result_evidence    : string[] (evidence_ids que soportan el resultado)
├── result_confidence  : integer (1-5)
├── decision           : string (qué se decide basado en el resultado)
└── decision_date      : date
```

### 7.2 Reglas del hypothesis model

1. Una hipótesis con `type: revenue` o `type: product` no puede tener `result: confirmed` sin al menos una transacción real o señal de demanda verificable (alineado con Package 000 prohibiciones de negocio).
2. Una hipótesis que alcanza su `timebox` sin resultado debe transicionar a `result: revised` o `result: abandoned` con justificación.
3. Una hipótesis con `type: learning` puede confirmarse con evidencia subjetiva (experiencia personal) siempre que se documente como tal con confidence ≤ 3.
4. Toda hipótesis debe tener tanto `success_criteria` como `failure_criteria` definidos antes de iniciar validación.


---

## 8. Research-to-Asset Handoff

### 8.1 Punto formal de handoff

El handoff ocurre en la **Etapa 13: Asset Extraction** del lifecycle, después de que la investigación pasa el Review (Etapa 12).

### 8.2 Proceso de handoff

```
1. Identificación
   └── Revisar conclusions, findings y artifacts de la investigación
   └── Identificar qué outputs son reutilizables fuera del contexto de esta investigación

2. Clasificación
   └── Asignar tipo de activo: Knowledge, Technical, Educational, Commercial, Data
   └── Evaluar quality criteria mínimos

3. Documentación
   └── Completar Asset Handoff template con:
       ├── asset_name (≤80 caracteres)
       ├── asset_type
       ├── description (1-3 oraciones)
       ├── source_investigation (referencia)
       ├── usage_hypothesis (quién lo usaría y cómo)
       ├── target_audience
       ├── quality_assessment (cumple criteria mínimos: sí/no)
       ├── dependencies (qué necesita el consumidor para usar este activo)
       ├── state (draft | ready | published)
       └── monetization_potential (none | low | medium | high + justificación)

4. Transferencia
   └── Mover o referenciar el activo en assets/{type}/ según corresponda
   └── Actualizar índice de activos
   └── Crear link de trazabilidad bidireccional (investigación → activo, activo → investigación)

5. Quality Gate de Asset
   └── El activo cumple:
       ├── Es autocontenido (comprensible sin leer toda la investigación)
       ├── Tiene uso identificado (no es documentación por documentar)
       ├── Metadata completa
       └── No contiene información sensible sin sanitizar
```

### 8.3 Tipos de activos y sus criteria mínimos

| Tipo | Criteria mínimos | Ejemplo |
|------|-----------------|---------|
| Knowledge Asset | Insight documentado, fuentes citadas, limitaciones declaradas | Comparativa de frameworks, análisis de mercado |
| Technical Asset | Funcional, documentado, reproducible | Script, configuración, arquitectura documentada |
| Educational Asset | Estructura pedagógica, prerequisitos claros, ejercicios/ejemplos | Tutorial, guía paso a paso, curso |
| Commercial Asset | Propuesta de valor clara, target definido, formato entregable | Template vendible, servicio blueprint |
| Data Asset | Schema documentado, fuentes citadas, limitaciones de uso | Dataset curado, benchmark, colección de mediciones |


---

## 9. Research-to-Product Handoff

### 9.1 Principio fundamental

La derivación de hipótesis de producto es un proceso de evaluación, no de forzamiento. Una investigación puede concluir sin producto comercial si la evidencia no lo soporta.

### 9.2 Proceso de derivación

```
1. Evaluación de señales comerciales
   └── Revisar conclusions buscando:
       ├── Problema confirmado que afecta a un segmento identificable
       ├── Activo producido que otros podrían necesitar
       ├── Conocimiento que otros pagarían por obtener
       └── Gap de mercado evidenciado durante la investigación

2. Formulación de Product_Hypothesis (solo si señales existen)
   └── Completar:
       ├── problem_confirmed: qué problema fue validado por la investigación
       ├── beneficiary_segment: quién se beneficiaría (específico)
       ├── deliverable_asset: qué activo puede entregarse
       ├── useful_format: qué formato sería útil (servicio, producto, contenido, tool)
       ├── commercial_evidence: qué señales de demanda existen
       ├── pre_validation_required: qué debe validarse antes de vender
       ├── minimum_experiment: cuál sería el experimento comercial mínimo
       ├── source_investigation: referencia a la investigación fuente
       └── confidence_level: confianza en la oportunidad (1-5)

3. Formulación de Revenue_Hypothesis (solo si Product_Hypothesis es viable)
   └── Completar:
       ├── revenue_mechanism: cómo fluye el dinero (venta directa, suscripción, licencia)
       ├── price_hypothesis: precio estimado con justificación
       ├── target_segment: a quién se vendería
       ├── channel_hypothesis: por dónde se distribuiría
       ├── volume_basis: base para estimar volumen
       ├── demand_evidence: señales que soportan demanda
       ├── minimum_commercial_experiment: experimento mínimo para validar willingness-to-pay
       └── validation_timeline: cuánto tiempo para validar

4. Decisión
   └── Opciones:
       ├── Advance: Product_Hypothesis pasa a validación (Package 004 o lab correspondiente)
       ├── Archive: Documentar oportunidad para evaluación futura
       └── Discard: Evidencia insuficiente, documentar rationale
```

### 9.3 Criterios para NO formular hypothesis de producto

- No existe un problema confirmado por la investigación
- El segmento beneficiario no es identificable
- No hay señales de demanda (ni directas ni inferidas)
- El activo producido es de uso exclusivamente interno
- El dominio tiene restricciones que impiden comercialización (ética, regulación, IP)

En estos casos, la investigación se archiva como Knowledge Asset sin presión de monetización.


---

## 10. Domain Adaptations

### 10.1 Framework de adaptación

Cada dominio adapta los elementos **variables** de la metodología. Los elementos **fijos** no son negociables.

**Elementos fijos (no adaptables):**
- Research_Brief obligatorio
- Completion criteria o timebox obligatorio
- Epistemic_Classification obligatoria
- Source registration obligatoria
- Conclusion obligatoria
- Asset extraction obligatoria
- Human review para conclusions
- AI outputs no son Primary_Evidence

**Elementos variables (adaptables por dominio):**
- Tipos de evidencia priorizados
- Métodos de validación disponibles
- Herramientas específicas del dominio
- Nivel de formalidad del experiment design
- Tipos de activos más probables
- Métricas de éxito específicas
- Constraints regulatorios o éticos

### 10.2 Adaptaciones por dominio

#### Technical Research (AWS, Kubernetes, DevOps, AIOps)

| Aspecto | Adaptación |
|---------|-----------|
| Evidence types | Measurement, experiment, official documentation, reproducible test |
| Validation methods | Proof of concept, benchmark, A/B test, load test, reproducible configuration |
| Tools emphasis | Deepnote (notebooks), GitHub (code/config), Kiro (specs) |
| Constraints | Versiones cambian rápidamente, evidencia puede expirar con nueva release |
| Typical assets | Technical Asset, Knowledge Asset (comparativas, architectures) |
| Special rules | Toda configuración debe ser reproducible; documentar versiones exactas |

#### Quantitative Research (Trading, Finance, Data Analysis)

| Aspecto | Adaptación |
|---------|-----------|
| Evidence types | Measurement, experiment, market data, statistical analysis |
| Validation methods | Backtesting, statistical significance, out-of-sample testing, paper trading |
| Tools emphasis | Deepnote (análisis), GitHub (estrategias, datasets) |
| Constraints | Datos históricos no garantizan resultados futuros; overfitting risk |
| Typical assets | Data Asset, Technical Asset, Knowledge Asset |
| Special rules | Declarar limitaciones de backtesting; no confundir correlación con causación; documentar periodos de datos |

#### Incident Research (Diagnostics, Postmortems)

| Aspecto | Adaptación |
|---------|-----------|
| Evidence types | Direct observation, measurement, logs, timeline reconstruction |
| Validation methods | Root cause analysis, reproduction in controlled environment, timeline correlation |
| Tools emphasis | GitHub (postmortem), Deepnote (log analysis), ChatGPT (hypothesis generation) |
| Constraints | Tiempo-sensible, puede requerir acción antes de análisis completo |
| Typical assets | Knowledge Asset (postmortem), Technical Asset (fix, runbook) |
| Special rules | Permitir conclusiones parciales si el incidente requiere resolución urgente; completar análisis post-resolución |

#### Market Research (Marketing, SaaS, AI Agents)

| Aspecto | Adaptación |
|---------|-----------|
| Evidence types | Market data, testimony, survey, competitive analysis, demand signals |
| Validation methods | Landing page test, interview (≥3), pre-sale, funnel analysis |
| Tools emphasis | ChatGPT (análisis competitivo), Obsidian (market maps), GitHub (documentation) |
| Constraints | Datos de mercado cambian rápidamente; testimonios pueden tener sesgo de confirmación |
| Typical assets | Knowledge Asset, Commercial Asset |
| Special rules | No confundir interés declarado con willingness-to-pay; validar con transacción real cuando sea posible |

#### Educational Research (English, Training, Longevity)

| Aspecto | Adaptación |
|---------|-----------|
| Evidence types | Scientific literature, professional experience, measurement (pre/post), observation |
| Validation methods | Pre/post measurement, longitudinal tracking, peer comparison, self-report with caveats |
| Tools emphasis | Obsidian (knowledge base), NotebookLM (literature review), GitHub (curricula) |
| Constraints | Resultados personales no generalizan; efecto placebo; sesgo de autoinforme |
| Typical assets | Educational Asset, Knowledge Asset |
| Special rules | Distinguir evidencia científica de experiencia personal; documentar n=1 limitations |

#### Creative Research (Photography, Music, Content Creation)

| Aspecto | Adaptación |
|---------|-----------|
| Evidence types | Professional experience, observation, comparative analysis, audience feedback |
| Validation methods | Portfolio comparison, audience metrics, peer review, self-assessment against criteria |
| Tools emphasis | Obsidian (creative knowledge), GitHub (processes, templates), domain-specific tools |
| Constraints | Calidad subjetiva; métricas de audiencia no equivalen a calidad; tendencias efímeras |
| Typical assets | Educational Asset, Knowledge Asset, Commercial Asset (content) |
| Special rules | Aceptar evaluación subjetiva documentada como válida; no requerir experimentación estadística para juicios estéticos |

#### Health and Performance Research (Longevity, Biohacking, Training)

| Aspecto | Adaptación |
|---------|-----------|
| Evidence types | Scientific literature, measurement (biomarkers, metrics), self-experiment, observation |
| Validation methods | Longitudinal self-tracking, literature review, consultation with professionals |
| Tools emphasis | Deepnote (tracking data), Obsidian (protocols), NotebookLM (literature) |
| Constraints | n=1 experiments; individual variation; publication bias in literature; regulatory limits |
| Typical assets | Knowledge Asset, Data Asset (personal metrics) |
| Special rules | Requiere human review para cualquier conclusión aplicada a salud; documentar que n=1 no generaliza; no dar consejo médico |

#### Finance Research (Investment, Wealth, Economics)

| Aspecto | Adaptación |
|---------|-----------|
| Evidence types | Market data, official documentation, statistical analysis, historical performance |
| Validation methods | Historical analysis, scenario modeling, paper portfolio, professional consultation |
| Tools emphasis | Deepnote (financial models), GitHub (strategies), NotebookLM (research papers) |
| Constraints | Regulaciones financieras; past performance ≠ future results; conflict of interest disclosure |
| Typical assets | Knowledge Asset, Data Asset, Technical Asset (models) |
| Special rules | Declarar que no es consejo financiero; documentar assumptions de modelo; separar análisis de recomendación personal |


---

## 11. Traceability

### 11.1 Matriz: Requirement → Documento → Template → Evidencia de cumplimiento

| Requirement | Documento(s) | Template | Evidencia de cumplimiento |
|-------------|-------------|----------|--------------------------|
| R1 Principios | 001-research-principles.md | — | ≥10 principios documentados con compliance indicators |
| R2 Intake | 002-research-lifecycle.md, 008-research-workflow.md | research-brief-template.md | Template con campos obligatorios, ejemplo completado |
| R3 Problem Framing | 002-research-lifecycle.md, 008-research-workflow.md | research-brief-template.md | Sección de problem statement en template |
| R4 Research Question | 004-research-question-framework.md | research-plan-template.md | Framework con quality criteria, ejemplo |
| R5 Scope | 002-research-lifecycle.md | research-plan-template.md | Sección de scope con timebox y exclusiones |
| R6 Assumptions | 002-research-lifecycle.md | research-plan-template.md | Assumptions register en template |
| R7 Source Collection | 007-source-evaluation.md | source-register-template.md | 10 criterios documentados, template con evaluación |
| R8 Evidence Evaluation | 006-evidence-framework.md | source-register-template.md | 12 categorías, escala 1-5 definida |
| R9 Hypothesis | 005-hypothesis-framework.md | experiment-template.md | 6 tipos, modelo con todos los campos |
| R10 Experiment Design | 014-experiment-design.md | experiment-template.md | Protocol structure, alternativas por dominio |
| R11 Results Registration | 006-evidence-framework.md, 015-research-journal.md | research-journal-template.md | Estructura para resultados positivos y negativos |
| R12 Conclusion | 017-conclusion-framework.md | conclusion-template.md | Campos obligatorios, trazabilidad a evidencia |
| R13 Uncertainty | 017-conclusion-framework.md | conclusion-template.md | Sección de uncertainty con clasificación |
| R14 Human Review | 020-quality-gates.md, 026-package-review.md | research-review-template.md | Review checklist, approval authority |
| R15 Asset Extraction | 018-research-to-asset.md | research-asset-handoff-template.md | Proceso, quality criteria, handoff template |
| R16 Product Hypothesis | 019-research-to-product-hypothesis.md | — | Proceso de derivación, campos obligatorios |
| R17 Revenue Hypothesis | 019-research-to-product-hypothesis.md | — | Revenue model, validation experiment |
| R18 Timeboxing | 002-research-lifecycle.md, 008-research-workflow.md | research-plan-template.md | Timebox obligatorio en plan |
| R19 Reproducibility | 014-experiment-design.md, 015-research-journal.md | experiment-template.md | Campos de environment, steps, config |
| R20 Privacy | 021-research-ethics-and-safety.md | research-brief-template.md | Sección de data handling, checklist |
| R21 IP | 021-research-ethics-and-safety.md | source-register-template.md | Campo de licensing en source register |
| R22 Responsible AI | 012-chatgpt-guidelines.md, 011-notebooklm-guidelines.md, 021-research-ethics-and-safety.md | — | Reglas explícitas, classification como AI_Generated |
| R23 Domain Adaptations | 022-domain-specific-adaptations.md | — | 8 dominios documentados con tabla de adaptaciones |
| R24 Metrics | 023-research-metrics.md | — | Métricas definidas, warning signals, cadence |
| R25 Critical Review | 026-package-review.md | research-review-template.md | Checklist, criteria de rework/archive/publish |
| R26 Lifecycle Stages | 002-research-lifecycle.md | — | 16 etapas con inputs/outputs/gates |
| R27 Research Types | 003-research-types.md | research-brief-template.md | 12 tipos con purpose y guidance |
| R28 Tooling | 009-tooling-workflow.md, 010-013 guidelines | — | Roles, handoffs, source of truth |
| R29 Quality Gates | 020-quality-gates.md | research-review-template.md | 7 gates con checklists |
| R30 Anti-patterns | 024-anti-patterns.md | — | Anti-patterns con symptoms y corrections |
| R31 Prudent Monetization | 019-research-to-product-hypothesis.md | — | Criteria para NO monetizar documentados |
| R32 Journal/Decision Log | 015-research-journal.md, 016-decision-log.md | research-journal-template.md, decision-log-template.md | Estructura y reglas de uso |
| R33 Templates | docs/templates/research/ | Todos (9) | 9 templates con examples |
| R34 Package Structure | README.md, 025-package-summary.md | — | 26 docs + 9 templates producidos |
| R35 Approval Criteria | 026-package-review.md | — | Checklist verificable |
| R36 Restrictions | 025-package-summary.md | — | Exclusiones documentadas |


### 11.2 Matriz: Research Stage → Input → Output → Quality Gate

| Stage | Input | Output | Quality Gate |
|-------|-------|--------|-------------|
| Intake | Trigger (pregunta, problema, idea, etc.) | Research_Brief (borrador) | Brief con campos obligatorios completos |
| Problem Framing | Research_Brief | Problem statement (síntomas + causa) | Statement genera ≥1 research question |
| Research Question | Problem statement | Question(s) con components | Pasa quality criteria (4 dimensiones) |
| Scope | Research questions | Scope doc con timebox + exclusions | Timebox definido, criteria explícitos |
| Assumptions | Scope, questions | Assumptions register | ≥3 assumptions con confidence + impact |
| Source Collection | Questions, scope | Source_Register poblado | ≥1 source con calidad suficiente por question |
| Evidence Evaluation | Source_Register | Evidence records clasificados | Toda evidencia clasificada, conflicts documented |
| Analysis | Evidence records | Análisis con patrones e hypotheses | Responde (parcial) a research questions |
| Experimentation | Hypotheses, protocol | Experiment records con results | Resultados documentados, hypothesis updated |
| Findings | Evidence, experiments, analysis | Findings consolidados | Cada question tiene ≥1 finding |
| Conclusion | Findings | Conclusion trazable | Trazable a ≥1 evidencia, limitations documented |
| Review | All artifacts | Review result (approved/rework) | Checklist completado |
| Asset Extraction | Approved conclusion | ≥1 Research_Asset | Asset cumple quality criteria, metadata completa |
| Product Hypothesis | Assets, conclusions | Product/Revenue hypothesis o "no signal" | Campos completos si hypothesis, justificación si ausente |
| Publication/Archive | Complete investigation | Decision + final storage | Privacy/IP checklist aprobado |
| Feedback/Iteration | Published/archived investigation | Feedback record, new briefs | Feedback registrado, métricas updated |

### 11.3 Matriz: Tool → Responsabilidad → Fuente de verdad → Riesgo principal

| Tool | Responsabilidad | Fuente de verdad | Riesgo principal |
|------|----------------|------------------|-----------------|
| ChatGPT Projects | Debate, borradores, revisión, planes, challenge | No (temporal) | Aceptar output como evidencia sin verificar |
| NotebookLM | Consulta documental, comparación, resúmenes con citas | No (temporal) | Confundir resumen IA con fuente primaria |
| Deepnote | Análisis de datos, notebooks reproducibles, visualización | Semi (notebooks versionados) | Notebooks no exportados se pierden |
| Obsidian | Conocimiento permanente, notas atómicas, relaciones | Semi (conocimiento personal) | Knowledge rot si no se actualiza |
| GitHub | Documentación versionada, decisions, templates, código | Sí (fuente de verdad formal) | Documentación desactualizada vs realidad |
| Kiro | Specs, requirements, design, tasks, implementation | Sí (specs formales) | Specs que no se implementan |


---

## 12. Revisión

### 12.1 Review checklist

Checklist para la revisión de cada investigación completada:

```
□ Research_Brief existe con todos los campos obligatorios
□ Problem statement es específico y distingue síntomas de causas
□ Research question(s) pasan quality criteria
□ Scope definido con timebox y exclusiones
□ Assumptions documentadas con confidence y impact
□ Source_Register contiene ≥1 fuente evaluada por research question
□ Evidence clasificada con confidence levels
□ Ningún AI output tratado como Primary_Evidence sin verificación
□ Conclusion trazable a evidencia registrada
□ Uncertainty section presente con gaps documentados
□ Limitations explícitas
□ ≥1 Research_Asset extraído con metadata completa
□ Asset cumple quality criteria mínimos
□ Product/Revenue hypothesis documentada (o ausencia justificada)
□ Privacy/IP compliance verificado
□ Research_Journal mantenido (si effort >4h)
□ Decision_Log actualizado para decisiones de scope/direction
□ Epistemic_Classification consistente (hechos vs hipótesis vs opiniones)
□ Timebox respetado (o extensión justificada)
□ No contradice Package 000 principles
```

### 12.2 Approval authority

| Decisión | Autoridad | Criterio |
|----------|-----------|----------|
| Aprobar conclusión de investigación | Fundador | Checklist satisfecho, human review completado |
| Aprobar extracción de asset | Fundador | Asset cumple quality criteria, metadata completa |
| Aprobar Product/Revenue hypothesis | Fundador | Evidencia suficiente, hypothesis completamente formulada |
| Aprobar publicación externa | Fundador | Privacy/IP checklist aprobado, quality satisfactoria |
| Rechazar investigación | Fundador | Justificación documentada, partial findings preserved |
| Aprobar Package 001 completo | Fundador | Todos los criteria del R35 satisfechos |

### 12.3 Criterios de rework

Una investigación requiere rework cuando:
- La conclusión no es trazable a evidencia documentada
- El checklist de review tiene ≥3 ítems no satisfechos
- Se identifica AI output tratado como Primary_Evidence
- Existen claims sin clasificación epistémica
- El timebox fue excedido sin justificación documentada
- Privacy o IP concerns no están resueltos

**Proceso de rework:**
1. Documentar deficiencias específicas con referencias a secciones
2. Asignar correcciones requeridas
3. Re-ejecutar etapas necesarias (no reiniciar toda la investigación)
4. Re-evaluar contra checklist

### 12.4 Criterios de archive

Una investigación se archiva cuando:
- Review aprobado y assets extraídos
- Investigación abandonada con justificación (→ Rejected + archive)
- Investigación completada sin oportunidad comercial (→ Knowledge Asset + archive)
- Investigación superada por investigación posterior (→ superseded + archive)

**Estado en archive:**
- Accesible para referencia futura
- No se actualiza activamente
- Puede generar nuevas Research_Briefs si se identifica relevancia

### 12.5 Criterios de publication

Una investigación (o sus assets) se publica externamente cuando:
- Review completamente aprobado
- Privacy checklist satisfecho (no datos sensibles, no client info)
- IP checklist satisfecho (no third-party content sin licencia)
- Formato adecuado para la audiencia target
- Fundador aprueba publicación explícitamente

**Formatos de publicación posibles:**
- Blog post / artículo
- Open-source tool o template
- Curso o material educativo
- Dataset público
- Playbook compartido

---

## Correctness Properties

Este design no produce software, por lo tanto no aplican property-based tests. La verificación de correctness se realiza mediante:

1. **Trazabilidad completa**: Cada requirement (R1-R36) tiene al menos un documento y/o template asignado en la matriz 11.1.
2. **Consistencia interna**: El modelo de estados (sección 3) es compatible con el lifecycle (sección 2) — cada etapa produce un estado válido.
3. **No contradicción con Package 000**: Los principios de negocio, operativos y de documentación de Package 000 son respetados (referencias explícitas en hypothesis model y revenue hypothesis).
4. **Completitud de artefactos**: El modelo de artefactos (sección 4) cubre todas las etapas del lifecycle con al menos un artefacto aplicable.
5. **Coverage de herramientas**: Todas las 6 herramientas tienen roles definidos y no hay etapa sin herramienta asignada.
