# Implementation Plan: Package 001 — Research Methodology

## Overview

Plan de implementación para producir los 26 documentos metodológicos y 9 templates del Package 001. Cada tarea produce un archivo markdown verificable en `docs/packages/package-001-research-methodology/` o `docs/templates/research/`. Las tareas están ordenadas para respetar dependencias conceptuales y permitir paralelismo donde sea posible.

## Tasks

- [x] 1. Actualizar README del package
  - [x] 1.1 Actualizar README del package
    - **Archivo:** `docs/packages/package-001-research-methodology/README.md`
    - Crear índice completo de los 26 documentos con nombre de archivo y descripción de una línea
    - Incluir glosario autoritativo con todos los términos del package
    - Declarar estado del package como "en progreso"
    - Incluir etiqueta epistémica: [Hecho]
    - _Requirements: R34.1, R34.3_
    - **Resultado esperado:** README con índice de 26 documentos, glosario completo, estado declarado
    - **Validación:** Cada documento listado tiene nombre de archivo correcto (NNN-kebab-case.md), glosario cubre todos los términos del glossary de requirements
    - **Dependencias:** Ninguna
    - **Paralelo:** No (establece la estructura base)

- [x] 2. Documentar research principles
  - [x] 2.1 Documentar research principles
    - **Archivo:** `docs/packages/package-001-research-methodology/001-research-principles.md`
    - Definir entre 10 y 15 principios fundacionales de investigación
    - Cada principio con: statement (≤2 oraciones), rationale (≤3 oraciones), compliance indicator observable, violation example concreto
    - Incluir mecanismo de excepción documentada
    - Incluir etiqueta epistémica: [Decisión]
    - _Requirements: R1.1, R1.2, R1.3, R1.4, R1.5_
    - **Resultado esperado:** Documento con 10-15 principios completos, cada uno verificable por tercero
    - **Validación:** Contar principios (10-15), verificar 4 campos por principio, confirmar que compliance indicators son observables
    - **Dependencias:** Tarea 1 (README establece glosario)
    - **Paralelo:** Sí (con tareas 3-8 una vez completada tarea 1)

- [x] 3. Documentar research lifecycle
  - [x] 3.1 Documentar research lifecycle
    - **Archivo:** `docs/packages/package-001-research-methodology/002-research-lifecycle.md`
    - Documentar las 16 etapas secuenciales del lifecycle con inputs/outputs/gates
    - Para cada etapa: propósito, inputs, actividades, outputs, responsable, herramientas, quality gate, estado resultante
    - Incluir modelo de estados con transiciones permitidas y criterios
    - Documentar artefactos mínimos por effort category
    - Incluir etiqueta epistémica: [Decisión]
    - _Requirements: R2.1, R2.2, R26.1, R26.2, R26.3, R26.4, R26.5, R26.6, R26.7_
    - **Resultado esperado:** Documento con 16 etapas completas, modelo de estados, transiciones, criterios
    - **Validación:** 16 etapas documentadas con todos los campos, transiciones cubren todos los estados, no hay estados huérfanos
    - **Dependencias:** Tarea 1 (glosario define términos clave)
    - **Paralelo:** Sí (con tareas 2, 4-8)

- [x] 4. Definir research types
  - [x] 4.1 Definir research types
    - **Archivo:** `docs/packages/package-001-research-methodology/003-research-types.md`
    - Documentar taxonomía de 12 tipos de investigación
    - Cada tipo con: purpose, typical questions (≥3), applicable domains (≥2), evidence types (≥2), validation methods (≥1), expected outputs, when to use (≥2), when NOT to use (≥2)
    - Incluir guía de selección y combinación de tipos
    - Incluir etiqueta epistémica: [Decisión]
    - _Requirements: R27.1, R27.2, R27.3, R27.4, R27.5_
    - **Resultado esperado:** Taxonomía completa con 12 tipos, guía de selección, reglas de combinación
    - **Validación:** 12 tipos con todos los campos, cada tipo referencia al menos un tipo contrastante, guía de combinación presente
    - **Dependencias:** Tarea 1 (glosario)
    - **Paralelo:** Sí (con tareas 2, 3, 5-8)

- [x] 5. Definir research question framework
  - [-] 5.1 Definir research question framework
    - **Archivo:** `docs/packages/package-001-research-methodology/004-research-question-framework.md`
    - Definir componentes obligatorios: subject, scope boundary, constraints, expected answer type, verification method
    - Documentar quality criteria: specificity, answerability, relevance, time-boundedness
    - Proceso de reformulación (máx 3 intentos) y escalación
    - Reglas de descomposición en sub-preguntas (máx 3 niveles)
    - Incluir etiqueta epistémica: [Decisión]
    - _Requirements: R4.1, R4.2, R4.3, R4.4, R4.5_
    - **Resultado esperado:** Framework completo con componentes, quality criteria, proceso de reformulación, descomposición
    - **Validación:** 5 componentes documentados, 4 quality criteria con definición, proceso de escalación claro, ejemplo de descomposición
    - **Dependencias:** Tarea 3 (lifecycle define contexto de etapa Research Question)
    - **Paralelo:** Sí (con tareas 2, 4, 6-8)

- [x] 6. Definir hypothesis framework
  - [-] 6.1 Definir hypothesis framework
    - **Archivo:** `docs/packages/package-001-research-methodology/005-hypothesis-framework.md`
    - Documentar 6 tipos de hipótesis: research, technical, product, business, revenue, learning
    - Modelo completo con todos los campos: assertion, prior evidence, variables, validation method, success/failure criteria, time limit, risks, subsequent decision
    - Reglas de timeout y extensiones (máx 2 per hypothesis)
    - Sistema de identificadores: HYP-[type]-[seq]
    - Incluir etiqueta epistémica: [Decisión]
    - _Requirements: R9.1, R9.2, R9.3, R9.4, R9.5_
    - **Resultado esperado:** Framework con 6 tipos, modelo completo, reglas de gestión temporal, sistema de IDs
    - **Validación:** 6 tipos definidos, modelo tiene todos los campos de R9.2, reglas de timeout claras, formato de ID verificable
    - **Dependencias:** Tarea 3 (lifecycle define etapa Analysis donde se formulan hipótesis)
    - **Paralelo:** Sí (con tareas 2, 4, 5, 7, 8)

- [x] 7. Definir evidence framework
  - [x] 7.1 Definir evidence framework
    - **Archivo:** `docs/packages/package-001-research-methodology/006-evidence-framework.md`
    - Documentar 12 categorías mutuamente exclusivas de evidencia
    - Escala de confianza 1-5 con definiciones precisas por nivel
    - Modelo completo de Evidence Record con todos los campos
    - Reglas de conflicto, verificación, y ceiling de confidence por tipo
    - Proceso de registro de resultados (positivos, negativos, inconclusos)
    - Incluir etiqueta epistémica: [Decisión]
    - _Requirements: R8.1, R8.2, R8.3, R8.4, R8.5, R11.1, R11.2, R11.3, R11.4_
    - **Resultado esperado:** Framework con 12 categorías, escala 1-5, modelo de registro, reglas de conflicto
    - **Validación:** 12 categorías listadas y mutuamente exclusivas, escala con definiciones por nivel, modelo con todos los campos del design
    - **Dependencias:** Tarea 1 (glosario define Evidence_Framework)
    - **Paralelo:** Sí (con tareas 2-6, 8)

- [x] 8. Definir evaluación de fuentes
  - [x] 8.1 Definir evaluación de fuentes
    - **Archivo:** `docs/packages/package-001-research-methodology/007-source-evaluation.md`
    - Documentar 10 dimensiones de evaluación: authority, currency, independence, methodology, reproducibility, bias, conflict of interest, precision, applicability, traceability
    - Sistema de scoring 0-10 (0/1 por dimensión)
    - Umbral mínimo de calidad (score 6) con reglas para fuentes por debajo
    - Protocolo de registro inmediato (misma sesión que consulta)
    - Incluir etiqueta epistémica: [Decisión]
    - _Requirements: R7.1, R7.2, R7.3, R7.4, R7.5_
    - **Resultado esperado:** 10 criterios con definición, scoring, umbral, protocolo de registro
    - **Validación:** 10 dimensiones documentadas, reglas de peso para score <6, protocolo de timing verificable
    - **Dependencias:** Tarea 7 (evidence framework define las categorías que las fuentes alimentan)
    - **Paralelo:** Sí (con tareas 2-6, puede hacerse en paralelo con 7 si se coordina)

- [x] 9. Documentar workflow operativo
  - [x] 9.1 Documentar workflow operativo
    - **Archivo:** `docs/packages/package-001-research-methodology/008-research-workflow.md`
    - Documentar flujo general del proceso investigativo
    - Integrar problem framing (R3), scope (R5), assumptions (R6), results (R11)
    - Incluir reglas de timebox, completion criteria, y decisiones al 80%
    - Documentar mecanismo de loop-back entre etapas
    - Incluir etiqueta epistémica: [Decisión]
    - _Requirements: R3.1, R3.2, R3.3, R3.4, R5.1, R5.2, R5.3, R5.4, R6.1, R6.2, R6.3, R6.4, R11.1, R18.1, R18.2, R18.3, R18.4, R18.5_
    - **Resultado esperado:** Workflow completo integrando problem framing, scope, assumptions, timebox, loop-back
    - **Validación:** Cada etapa referencia inputs/outputs, timebox tiene reglas claras, loop-back documentado con justificación
    - **Dependencias:** Tareas 3, 5 (lifecycle y question framework establecen las etapas)
    - **Paralelo:** No (integra múltiples frameworks previos)

- [x] 10. Documentar tooling workflow
  - [x] 10.1 Documentar tooling workflow
    - **Archivo:** `docs/packages/package-001-research-methodology/009-tooling-workflow.md`
    - Documentar roles exclusivos de cada herramienta (ChatGPT, NotebookLM, Deepnote, Obsidian, GitHub, Kiro)
    - Definir qué origina cada herramienta, qué exporta, qué versiona
    - Clasificar temporal vs semi-permanente vs fuente de verdad
    - Handoff protocol entre herramientas
    - Reglas de qué NO copiar entre herramientas
    - Incluir etiqueta epistémica: [Decisión]
    - _Requirements: R28.1, R28.2, R28.3, R28.4, R28.5_
    - **Resultado esperado:** Roles definidos sin overlap, flujo de información, handoff protocol, restricciones
    - **Validación:** 6 herramientas con rol exclusivo, no hay input-output pair duplicado, handoff tiene 4 campos mínimos
    - **Dependencias:** Tarea 3 (lifecycle define en qué etapas se usa cada herramienta)
    - **Paralelo:** Sí (con tareas 2, 4-8)

- [x] 11. Documentar uso de Deepnote
  - [x] 11.1 Documentar uso de Deepnote
    - **Archivo:** `docs/packages/package-001-research-methodology/010-deepnote-guidelines.md`
    - Definir rol: análisis de datos, notebooks reproducibles, experimentación, visualizaciones
    - Documentar qué se origina, qué se exporta a GitHub, cuándo usar
    - Reglas de versionado de notebooks
    - Integración con lifecycle stages (Source Collection, Evidence Evaluation, Analysis, Experimentation)
    - Incluir etiqueta epistémica: [Decisión]
    - _Requirements: R28.1, R28.2_
    - **Resultado esperado:** Guía específica de Deepnote con rol, flujos, reglas de export
    - **Validación:** Rol no duplica otros tools, reglas de export claras, stages de uso identificados
    - **Dependencias:** Tarea 10 (tooling workflow define el marco general)
    - **Paralelo:** Sí (con tareas 12, 13, 14)

- [x] 12. Documentar uso de NotebookLM
  - [x] 12.1 Documentar uso de NotebookLM
    - **Archivo:** `docs/packages/package-001-research-methodology/011-notebooklm-guidelines.md`
    - Definir rol: consulta documental, comparación de fuentes, resúmenes con referencias
    - Reglas de clasificación de output como temporal (no fuente de verdad)
    - Reglas de AI responsable: no tratar resúmenes como Primary_Evidence
    - Integración con lifecycle stages (Source Collection, Evidence Evaluation)
    - Incluir etiqueta epistémica: [Decisión]
    - _Requirements: R28.1, R28.2, R22.1, R22.2, R22.3_
    - **Resultado esperado:** Guía de NotebookLM con rol, restricciones de IA, reglas de verificación
    - **Validación:** Restricción explícita de AI output como evidencia, reglas de export presentes
    - **Dependencias:** Tarea 10 (tooling workflow)
    - **Paralelo:** Sí (con tareas 11, 13, 14)

- [x] 13. Documentar uso de ChatGPT Projects
  - [x] 13.1 Documentar uso de ChatGPT Projects
    - **Archivo:** `docs/packages/package-001-research-methodology/012-chatgpt-guidelines.md`
    - Definir rol: contexto, debate, borradores, revisión, planes, challenge de ideas
    - Reglas de clasificación como temporal (output efímero)
    - Reglas de AI responsable: clasificar como AI_Generated_Content, verificación obligatoria
    - Qué exportar a GitHub (decisiones, conclusiones refinadas)
    - Incluir etiqueta epistémica: [Decisión]
    - _Requirements: R28.1, R28.2, R22.1, R22.2, R22.3, R22.4, R22.5, R22.6_
    - **Resultado esperado:** Guía de ChatGPT con rol, restricciones, reglas de verificación y export
    - **Validación:** AI_Generated_Content explícitamente definido, reglas de verificación contra fuentes, export protocol
    - **Dependencias:** Tarea 10 (tooling workflow)
    - **Paralelo:** Sí (con tareas 11, 12, 14)

- [x] 14. Documentar uso de Obsidian
  - [x] 14.1 Documentar uso de Obsidian
    - **Archivo:** `docs/packages/package-001-research-methodology/013-obsidian-guidelines.md`
    - Definir rol: conocimiento permanente, notas atómicas, relaciones conceptuales, índice personal
    - Reglas de cuándo contenido madura a documento formal en GitHub
    - Integración con lifecycle stages (todas las etapas como knowledge base)
    - Relación con Source_Register y Evidence records
    - Incluir etiqueta epistémica: [Decisión]
    - _Requirements: R28.1, R28.2_
    - **Resultado esperado:** Guía de Obsidian con rol, reglas de maduración, integración con lifecycle
    - **Validación:** Rol diferenciado de GitHub, criterios de maduración claros, no hay overlap con otros tools
    - **Dependencias:** Tarea 10 (tooling workflow)
    - **Paralelo:** Sí (con tareas 11, 12, 13)

- [x] 15. Definir experiment design
  - [x] 15.1 Definir experiment design
    - **Archivo:** `docs/packages/package-001-research-methodology/014-experiment-design.md`
    - Documentar campos obligatorios: hypothesis, variables (independent/dependent/controlled), method, success/failure criteria, time limit, resources, data format, risks
    - Clasificación: research experiment vs commercial validation experiment
    - Métodos alternativos para dominios sin experimentación controlada
    - Documentación de resultados terminales (success, failure, timeout, abandoned)
    - Incluir etiqueta epistémica: [Decisión]
    - _Requirements: R10.1, R10.2, R10.3, R10.4, R10.5, R19.2_
    - **Resultado esperado:** Framework de experiment design con campos, clasificación, alternativas, terminación
    - **Validación:** Campos alineados con R10.1, alternativas documentadas para ≥1 dominio, reglas de abandono claras
    - **Dependencias:** Tareas 6, 7 (hypothesis y evidence frameworks)
    - **Paralelo:** No (depende de hypothesis framework)

- [x] 16. Definir research journal
  - [x] 16.1 Definir research journal
    - **Archivo:** `docs/packages/package-001-research-methodology/015-research-journal.md`
    - Definir estructura de entrada: date, stage, activity, findings, decisions, next steps, time invested, tools used
    - Regla de creación obligatoria al superar 4h de esfuerzo
    - Orden cronológico, entradas identificables por posición secuencial
    - Regla de reconstrucción retroactiva si se alcanza umbral sin journal
    - Incluir etiqueta epistémica: [Decisión]
    - _Requirements: R32.1, R32.2, R32.5, R19.1_
    - **Resultado esperado:** Estructura del journal con campos obligatorios, reglas de uso, umbral de 4h
    - **Validación:** 8 campos documentados, regla de 4h presente, proceso retroactivo descrito
    - **Dependencias:** Tarea 3 (lifecycle define stages para el campo "stage")
    - **Paralelo:** Sí (con tarea 17)

- [x] 17. Definir decision log
  - [x] 17.1 Definir decision log
    - **Archivo:** `docs/packages/package-001-research-methodology/016-decision-log.md`
    - Definir estructura: decision description, context, alternatives (≥2), selection rationale, evidence, consequences, reversibility, date
    - Triggers para registrar una decisión (cambio de scope, dirección, metodología)
    - Referencia obligatoria a evidence o evento triggering
    - Incluir etiqueta epistémica: [Decisión]
    - _Requirements: R32.3, R32.4_
    - **Resultado esperado:** Estructura del decision log con campos, triggers, reglas de referencia
    - **Validación:** 8 campos documentados, triggers claros, reversibility tiene 3 niveles
    - **Dependencias:** Tarea 3 (lifecycle define contexto de decisiones)
    - **Paralelo:** Sí (con tarea 16)

- [x] 18. Definir conclusion framework
  - [x] 18.1 Definir conclusion framework
    - **Archivo:** `docs/packages/package-001-research-methodology/017-conclusion-framework.md`
    - Campos obligatorios: research question answered, evidence summary, confidence level (high/medium/low), limitations, implications, recommended actions, open questions
    - Trazabilidad obligatoria a evidencia registrada
    - Distinción: strong evidence, limited evidence, inference
    - Sección de uncertainty: known unknowns, methodological limitations, evidence gaps, scope limitations
    - Clasificación de uncertainty: reducible, irreducible, temporal
    - Reglas para contradicciones con findings previos
    - Incluir etiqueta epistémica: [Decisión]
    - _Requirements: R12.1, R12.2, R12.3, R12.4, R12.5, R13.1, R13.2, R13.3, R13.4_
    - **Resultado esperado:** Framework con campos, trazabilidad, tipos de conclusión, uncertainty completo
    - **Validación:** Campos alineados con R12.1, tres tipos de conclusión diferenciados, uncertainty tiene clasificación
    - **Dependencias:** Tareas 7, 8 (evidence y source evaluation definen qué soporta conclusiones)
    - **Paralelo:** No (depende de evidence framework)

- [x] 19. Definir research-to-asset
  - [x] 19.1 Definir research-to-asset
    - **Archivo:** `docs/packages/package-001-research-methodology/018-research-to-asset.md`
    - Documentar proceso de handoff: identificación, clasificación, documentación, transferencia, quality gate
    - 5 tipos de activo con criteria mínimos: Knowledge, Technical, Educational, Commercial, Data
    - Campos del Asset Handoff: name, type, description, usage hypothesis, target audience, source investigation, state
    - Quality gate de asset: autocontenido, uso identificado, metadata completa, no info sensible
    - Regla para investigaciones sin asset extraíble (justificación obligatoria)
    - Incluir etiqueta epistémica: [Decisión]
    - _Requirements: R15.1, R15.2, R15.3, R15.4, R15.5, R15.6_
    - **Resultado esperado:** Proceso completo de extracción con tipos, campos, quality gate, excepciones
    - **Validación:** 5 tipos con criteria, handoff tiene todos los campos, quality gate verificable, excepción documentada
    - **Dependencias:** Tarea 18 (conclusion framework define cuándo se completa la investigación)
    - **Paralelo:** No (secuencial tras conclusion)

- [x] 20. Definir research-to-product hypothesis
  - [x] 20.1 Definir research-to-product hypothesis
    - **Archivo:** `docs/packages/package-001-research-methodology/019-research-to-product-hypothesis.md`
    - Documentar proceso de derivación: evaluación de señales, Product_Hypothesis, Revenue_Hypothesis, decisión
    - Campos de Product_Hypothesis: 7 campos obligatorios (problem, segment, asset, format, evidence, validation, experiment)
    - Campos de Revenue_Hypothesis: revenue mechanism, price, segment, channel, volume, demand evidence, experiment
    - Criterios para NO formular hypothesis (5 condiciones)
    - Reglas de prudent monetization: no avanzar sin demand signal externo
    - Alineación con Package 000 reglas de negocio
    - Incluir etiqueta epistémica: [Decisión]
    - _Requirements: R16.1, R16.2, R16.3, R16.4, R17.1, R17.2, R17.3, R17.4, R31.1, R31.2, R31.3, R31.4, R31.5_
    - **Resultado esperado:** Proceso completo con Product y Revenue hypothesis, criterios de no-monetización, prudent rules
    - **Validación:** 7 campos de Product_Hypothesis, Revenue fields completos, 5 criterios de no-formulación, regla de demand signal
    - **Dependencias:** Tarea 19 (research-to-asset define el paso previo)
    - **Paralelo:** No (secuencial tras asset extraction)

- [x] 21. Definir quality gates
  - [x] 21.1 Definir quality gates
    - **Archivo:** `docs/packages/package-001-research-methodology/020-quality-gates.md`
    - Documentar 7 quality gates: initiate, experiment, findings, conclusions, assets, publish, commercial
    - Cada gate con: name, position, required inputs (≥1), evaluation criteria (≥3 items), pass/fail, fail actions, responsible
    - Reglas de remediation (≤30 días, ≤3 intentos por gate)
    - Alternative evidence path para dominios sin experimentación controlada
    - Human review requirements integrados (R14)
    - Incluir etiqueta epistémica: [Decisión]
    - _Requirements: R29.1, R29.2, R29.3, R29.4, R29.5, R14.1, R14.2, R14.3, R14.4, R14.5_
    - **Resultado esperado:** 7 gates completos con checklists, reglas de fallo, human review integrado
    - **Validación:** 7 gates con ≥3 criteria cada uno, fail actions definidas, human review obligatorio en conclusions
    - **Dependencias:** Tareas 3, 9, 18 (lifecycle, workflow y conclusion definen los puntos de gate)
    - **Paralelo:** No (integra múltiples frameworks)

- [x] 22. Definir ética, seguridad y privacidad
  - [x] 22.1 Definir ética, seguridad y privacidad
    - **Archivo:** `docs/packages/package-001-research-methodology/021-research-ethics-and-safety.md`
    - Privacy: data type, collection, storage, access, retention (≤365 días), deletion
    - IP: source licensing, attribution, commercial use verification
    - Responsible AI: clasificación AI_Generated_Content, verificación obligatoria, labeling
    - Reglas para dominios regulados (finance, health, legal)
    - Prohibiciones explícitas: credenciales, datos sin anonimizar, AI sin verificar
    - Incluir etiqueta epistémica: [Decisión]
    - _Requirements: R20.1, R20.2, R20.3, R20.4, R20.5, R21.1, R21.2, R21.3, R21.4, R21.5, R22.1, R22.2, R22.3, R22.4, R22.5, R22.6_
    - **Resultado esperado:** Documento integrado de ética, privacy, IP y AI responsable
    - **Validación:** Privacy tiene 6 campos, IP tiene 5 reglas, AI tiene clasificación + verificación, dominios regulados cubiertos
    - **Dependencias:** Tareas 7, 8 (evidence y source evaluation definen qué requiere verificación)
    - **Paralelo:** Sí (con tareas 15-20 si dependencias de 7/8 están completas)

- [x] 23. Definir adaptaciones por dominio
  - [x] 23.1 Definir adaptaciones por dominio
    - **Archivo:** `docs/packages/package-001-research-methodology/022-domain-specific-adaptations.md`
    - Definir elementos fijos (no adaptables) vs elementos variables (adaptables)
    - Documentar adaptaciones para ≥8 dominios: Technical, Quantitative, Incident, Market, Educational, Creative, Health/Performance, Finance
    - Cada dominio con: evidence types, validation methods, tools, constraints, typical assets, special rules
    - Template para nuevos dominios
    - Verificación de no-contradicción con elementos fijos
    - Incluir etiqueta epistémica: [Decisión]
    - _Requirements: R23.1, R23.2, R23.3, R23.4, R23.5, R23.6_
    - **Resultado esperado:** Framework de adaptación con fijos/variables, 8+ dominios completos, template para nuevos
    - **Validación:** Elementos fijos listados, ≥8 dominios con tabla completa, template incluido, no contradice fijos
    - **Dependencias:** Tareas 2, 7, 15 (principios, evidence y experiments definen los elementos fijos)
    - **Paralelo:** No (requiere frameworks previos completos)

- [x] 24. Definir métricas
  - [x] 24.1 Definir métricas
    - **Archivo:** `docs/packages/package-001-research-methodology/023-research-metrics.md`
    - Definir métricas con measurement method y periodo mensual: investigations initiated/completed, avg days por effort category, assets per investigation, hypotheses generated, quality gate pass rate, domains investigated, completed-to-abandoned ratio
    - Review cadence: al menos mensual
    - Warning signals: 5 condiciones con acciones correctivas
    - Incluir etiqueta epistémica: [Decisión]
    - _Requirements: R24.1, R24.2, R24.3, R24.4_
    - **Resultado esperado:** Métricas completas con métodos, cadence, warning signals y acciones
    - **Validación:** 8 métricas con measurement method, cadence mensual, 5 warning signals con ≥1 acción correctiva cada uno
    - **Dependencias:** Tareas 3, 21 (lifecycle y quality gates definen qué se mide)
    - **Paralelo:** Sí (con tareas 22, 23 si dependencias están completas)

- [x] 25. Documentar anti-patterns
  - [x] 25.1 Documentar anti-patterns
    - **Archivo:** `docs/packages/package-001-research-methodology/024-anti-patterns.md`
    - Documentar ≥7 anti-patterns generales con: name (≤5 words), description, symptoms (≥2), consequences (≥1), correction (≥1)
    - Documentar ≥4 anti-patterns específicos de AI
    - Mapear cada anti-pattern a ≥1 lifecycle stage
    - Incluir ≥1 checklist question por stage para detección
    - Incluir etiqueta epistémica: [Decisión]
    - _Requirements: R30.1, R30.2, R30.3, R30.4_
    - **Resultado esperado:** 11+ anti-patterns (7 generales + 4 AI) con mapeo a stages y detección
    - **Validación:** ≥7 generales con 5 campos, ≥4 AI-specific, mapeo a stages presente, checklist questions por stage
    - **Dependencias:** Tareas 3, 13 (lifecycle y ChatGPT guidelines definen contexto de anti-patterns)
    - **Paralelo:** Sí (con tareas 22-24)

- [x] 26. Crear templates
  - [x] 26.1 Crear research-brief-template
    - **Archivo:** `docs/templates/research/research-brief-template.md`
    - Campos requeridos: trigger, context, requester, expected value, domain classification, effort category, origin type, research type
    - Campos opcionales para lightweight intake (<4h)
    - Usage instructions (≥3 steps), domain-specific sections con [DOMAIN-SPECIFIC] label
    - Ejemplo completo con datos realistas
    - _Requirements: R33.1, R33.2, R33.3, R33.4, R2.2, R2.3, R27.3_
    - **Resultado esperado:** Template con required/optional fields, instructions, example
    - **Validación:** Campos alineados con R2.2, lightweight variant presente, example completo
    - **Dependencias:** Tareas 3, 4, 9 (lifecycle, types, workflow)
    - **Paralelo:** Sí (con 26.2-26.9)

  - [x] 26.2 Crear research-plan-template
    - **Archivo:** `docs/templates/research/research-plan-template.md`
    - Campos: research questions, scope (inclusions/exclusions/depth), timebox, deadline, completion criteria, assumptions register, max sources
    - Usage instructions, domain-specific sections, ejemplo completo
    - _Requirements: R33.1, R33.2, R33.3, R33.4, R4.1, R5.1, R5.2, R6.1_
    - **Resultado esperado:** Template con scope, timebox, assumptions, questions
    - **Validación:** Scope tiene depth levels, timebox en horas, assumptions con 4 campos
    - **Dependencias:** Tareas 5, 9 (question framework y workflow)
    - **Paralelo:** Sí (con 26.1, 26.3-26.9)

  - [x] 26.3 Crear source-register-template
    - **Archivo:** `docs/templates/research/source-register-template.md`
    - Campos: source ID, type, access date, author, relevance, quality score, 10 dimensions scoring, IP/licensing
    - Usage instructions, ejemplo completo con evaluación
    - _Requirements: R33.1, R33.2, R33.3, R33.4, R7.1, R7.2, R21.1_
    - **Resultado esperado:** Template con registro de fuentes y evaluación de 10 dimensiones
    - **Validación:** 10 dimensiones presentes, scoring 0-10, campos de IP incluidos
    - **Dependencias:** Tarea 8 (source evaluation)
    - **Paralelo:** Sí (con 26.1-26.2, 26.4-26.9)

  - [x] 26.4 Crear experiment-template
    - **Archivo:** `docs/templates/research/experiment-template.md`
    - Campos: hypothesis, variables (ind/dep/controlled), method, success/failure criteria, time limit, resources, data format, risks, classification (research/commercial)
    - Environment y reproducibility fields (OS, tools, versions, config, steps)
    - Usage instructions, ejemplo completo
    - _Requirements: R33.1, R33.2, R33.3, R33.4, R10.1, R10.2, R19.2_
    - **Resultado esperado:** Template de experiment design con reproducibility
    - **Validación:** Campos alineados con R10.1, environment fields presentes, ejemplo completo
    - **Dependencias:** Tarea 15 (experiment design)
    - **Paralelo:** Sí (con 26.1-26.3, 26.5-26.9)

  - [x] 26.5 Crear research-journal-template
    - **Archivo:** `docs/templates/research/research-journal-template.md`
    - Campos por entrada: date, stage, activity, findings, decisions, next steps, time invested, tools used
    - Estructura cronológica, regla de 4h
    - Usage instructions, ejemplo con 2-3 entradas realistas
    - _Requirements: R33.1, R33.2, R33.3, R33.4, R32.1, R32.2_
    - **Resultado esperado:** Template de journal con estructura de entradas
    - **Validación:** 8 campos por entrada, ejemplo con múltiples entradas, regla de 4h referenciada
    - **Dependencias:** Tarea 16 (research journal)
    - **Paralelo:** Sí (con 26.1-26.4, 26.6-26.9)

  - [x] 26.6 Crear decision-log-template
    - **Archivo:** `docs/templates/research/decision-log-template.md`
    - Campos: decision, context, alternatives (≥2), rationale, evidence, consequences, reversibility, date
    - Usage instructions, ejemplo completo
    - _Requirements: R33.1, R33.2, R33.3, R33.4, R32.3, R32.4_
    - **Resultado esperado:** Template de decision log con campos completos
    - **Validación:** 8 campos, alternatives requiere ≥2, reversibility tiene 3 niveles, ejemplo completo
    - **Dependencias:** Tarea 17 (decision log)
    - **Paralelo:** Sí (con 26.1-26.5, 26.7-26.9)

  - [x] 26.7 Crear conclusion-template
    - **Archivo:** `docs/templates/research/conclusion-template.md`
    - Campos: question answered, evidence summary, confidence (high/medium/low), limitations, implications, actions, open questions
    - Sección de uncertainty con clasificación (reducible/irreducible/temporal)
    - Sección de epistemic classification
    - Usage instructions, ejemplo completo
    - _Requirements: R33.1, R33.2, R33.3, R33.4, R12.1, R13.1, R13.2_
    - **Resultado esperado:** Template de conclusión con uncertainty integrada
    - **Validación:** Campos de R12.1, uncertainty con 3 tipos, epistemic tags presentes
    - **Dependencias:** Tarea 18 (conclusion framework)
    - **Paralelo:** Sí (con 26.1-26.6, 26.8-26.9)

  - [x] 26.8 Crear research-asset-handoff-template
    - **Archivo:** `docs/templates/research/research-asset-handoff-template.md`
    - Campos: asset name, type, description, usage hypothesis, target audience, source investigation, state, monetization potential, dependencies
    - Quality gate checklist: autocontenido, uso identificado, metadata, no info sensible
    - Usage instructions, ejemplo completo
    - _Requirements: R33.1, R33.2, R33.3, R33.4, R15.2, R15.3_
    - **Resultado esperado:** Template de handoff con campos y quality gate
    - **Validación:** Campos alineados con R15.2, quality gate verificable, ejemplo completo
    - **Dependencias:** Tarea 19 (research-to-asset)
    - **Paralelo:** Sí (con 26.1-26.7, 26.9)

  - [x] 26.9 Crear research-review-template
    - **Archivo:** `docs/templates/research/research-review-template.md`
    - Checklist de 8 items (R25.1): question answered, ≥3 evidence items, sources verified, traceability, uncertainties, ≥1 asset, limitations, ethics compliance
    - Campos de remediation: section, corrective action, responsible, target date
    - Sign-off: reviewer, date, result (approved/revision-needed/rejected)
    - Usage instructions, ejemplo completo
    - _Requirements: R33.1, R33.2, R33.3, R33.4, R25.1, R25.2, R14.1_
    - **Resultado esperado:** Template de review con checklist, remediation, sign-off
    - **Validación:** 8 checklist items de R25.1, remediation fields presentes, sign-off con 3 opciones
    - **Dependencias:** Tarea 21 (quality gates define checklist)
    - **Paralelo:** Sí (con 26.1-26.8)

- [x] 27. Validar enlaces y consistencia
  - [x] 27.1 Validar enlaces y consistencia
    - **Archivo:** Todos los documentos en `docs/packages/package-001-research-methodology/` y `docs/templates/research/`
    - Verificar que todos los cross-references entre documentos apuntan a archivos existentes
    - Verificar que términos del glosario se usan consistentemente
    - Verificar que no hay contradicción con Package 000 (principios, glosario, decisiones)
    - Verificar naming convention: NNN-kebab-case.md, secuencial sin gaps
    - _Requirements: R34.6, R34.7, R35.1k_
    - **Resultado esperado:** Listado de inconsistencias encontradas (si las hay) con ubicación y corrección sugerida
    - **Validación:** Todos los links internos resuelven, glosario consistente, no hay contradicciones con Package 000
    - **Dependencias:** Tareas 1-26 (todos los documentos deben existir)
    - **Paralelo:** No (requiere todos los documentos previos)

- [x] 28. Crear package summary
  - [x] 28.1 Crear package summary
    - **Archivo:** `docs/packages/package-001-research-methodology/025-package-summary.md`
    - Listar toda decisión metodológica del package con: documento de origen, rationale reference
    - Declaración de consistencia: no hay contradicciones internas entre los 26 documentos
    - Documentar exclusiones explícitas (R36): no software, no APIs, no databases, no SaaS
    - Relación con otros packages: dependencias y consumers (002-009)
    - Incluir etiqueta epistémica: [Hecho]
    - _Requirements: R34.4, R34.5, R36.1, R36.2, R36.3, R36.4_
    - **Resultado esperado:** Summary con decisiones, consistencia, exclusiones, relaciones inter-package
    - **Validación:** Decisiones trazables a documentos, exclusiones de R36.1 presentes, consumers listados
    - **Dependencias:** Tareas 1-26 (consolida decisiones de todos los documentos)
    - **Paralelo:** No (requiere todos los documentos previos)

- [x] 29. Ejecutar revisión crítica
  - [x] 29.1 Ejecutar revisión crítica
    - **Archivo:** `docs/packages/package-001-research-methodology/026-package-review.md`
    - Approval checklist cubriendo completitud estructural de 26 documentos y 9 templates
    - Verificación de trazabilidad: cada documento traza a ≥1 objetivo del README
    - Evaluación de 11 condiciones de R35.1 (a-k) como pasa/no pasa
    - Sign-off section: reviewer name, date, approval result
    - Incluir etiqueta epistémica: [Hecho]
    - _Requirements: R25.1, R25.2, R25.3, R25.4, R34.5, R35.1, R35.2, R35.3, R35.4_
    - **Resultado esperado:** Documento de review con checklist, trazabilidad, 11 condiciones evaluadas, sign-off
    - **Validación:** 11 condiciones de R35.1 presentes con campo pasa/no pasa, sign-off section con 3 campos
    - **Dependencias:** Tareas 27, 28 (validación y summary deben estar completos)
    - **Paralelo:** No (es revisión final)

- [x] 30. Corregir inconsistencias
  - [x] 30.1 Corregir inconsistencias
    - **Archivo:** Documentos identificados en tareas 27 y 29 con inconsistencias
    - Aplicar correcciones a cross-references rotos
    - Resolver contradicciones terminológicas con glosario del README
    - Actualizar campos faltantes o incompletos detectados en revisión
    - _Requirements: R35.3, R35.4_
    - **Resultado esperado:** Todos los issues de tareas 27 y 29 resueltos, documentos actualizados
    - **Validación:** Re-ejecutar validación de tarea 27, verificar que issues previos están corregidos
    - **Dependencias:** Tareas 27, 29 (identifican las inconsistencias)
    - **Paralelo:** No (secuencial tras revisión)

- [x] 31. Actualizar índices generales
  - [x] 31.1 Actualizar índices generales
    - **Archivo:** `docs/templates/research/README.md` y `docs/packages/package-001-research-methodology/README.md`
    - Crear/actualizar `docs/templates/research/README.md` con índice de 9 templates: filename, purpose, count de required fields
    - Actualizar README del package con estado final de documentos
    - Verificar que todos los archivos listados existen
    - _Requirements: R33.5, R34.3_
    - **Resultado esperado:** Índice de templates creado, README del package actualizado con estado correcto
    - **Validación:** 9 templates listados en index con 3 campos cada uno, README refleja estado actual
    - **Dependencias:** Tareas 26, 30 (templates completos y correcciones aplicadas)
    - **Paralelo:** No (requiere correcciones previas)

- [x] 32. Asignar estado final al package
  - [x] 32.1 Asignar estado final al package
    - **Archivo:** `docs/packages/package-001-research-methodology/README.md`
    - Actualizar estado del package de "en progreso" a "completo" o "en revisión" según resultado de tarea 29
    - Registrar fecha de completitud
    - Confirmar que 26 documentos + 9 templates están producidos y listados
    - _Requirements: R34.3, R35.2_
    - **Resultado esperado:** README con estado final declarado, fecha, confirmación de entregables
    - **Validación:** Estado es uno de los permitidos (pendiente/en progreso/completo/en revisión), 35 archivos confirmados
    - **Dependencias:** Tareas 29, 30, 31 (revisión, correcciones e índices completos)
    - **Paralelo:** No (última tarea del package)

- [x] 33. Checkpoint final
  - Verificar que todos los documentos existen y son consistentes
  - Confirmar con el usuario si hay preguntas o ajustes pendientes
  - Ensure all validations pass, ask the user if questions arise.

## Notes

- Este package es exclusivamente documental: no produce software, APIs, bases de datos ni infraestructura técnica.
- Cada tarea produce archivos markdown verificables en `docs/packages/package-001-research-methodology/` o `docs/templates/research/`.
- Las tareas están ordenadas para respetar dependencias conceptuales entre frameworks.
- Los documentos 001-008 pueden producirse en paralelo (fundamentales e independientes entre sí).
- Los documentos 009-014 (tooling) tienen dependencia del lifecycle pero pueden paralelizarse entre sí.
- Los documentos 015-020 son secuenciales (cada framework se construye sobre el anterior).
- Los documentos 021-025 pueden paralelizarse parcialmente.
- Las tareas 27-32 son estrictamente secuenciales (revisión, corrección, cierre).
- Los 9 templates tienen dependencia de sus documentos framework respectivos pero pueden paralelizarse entre sí.
- No aplican property-based tests (no hay software que probar).
- La validación se realiza mediante verificación de estructura, completitud de campos, y consistencia terminológica.

## Task Dependency Graph

```json
{
  "waves": [
    { "id": 0, "tasks": ["1.1"] },
    { "id": 1, "tasks": ["2.1", "3.1", "4.1", "7.1"] },
    { "id": 2, "tasks": ["5.1", "6.1", "8.1", "10.1"] },
    { "id": 3, "tasks": ["9.1", "11.1", "12.1", "13.1", "14.1", "16.1", "17.1"] },
    { "id": 4, "tasks": ["15.1", "18.1", "22.1", "25.1"] },
    { "id": 5, "tasks": ["19.1", "21.1", "23.1", "24.1"] },
    { "id": 6, "tasks": ["20.1"] },
    { "id": 7, "tasks": ["26.1", "26.2", "26.3", "26.4", "26.5", "26.6", "26.7", "26.8", "26.9"] },
    { "id": 8, "tasks": ["27.1", "28.1"] },
    { "id": 9, "tasks": ["29.1"] },
    { "id": 10, "tasks": ["30.1"] },
    { "id": 11, "tasks": ["31.1"] },
    { "id": 12, "tasks": ["32.1"] }
  ]
}
```
