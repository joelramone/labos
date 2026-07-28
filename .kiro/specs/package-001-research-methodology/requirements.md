# Requirements Document

## Introduction

Package 001 — Research Methodology define la metodología estándar mediante la cual LabOS transforma entradas diversas (preguntas, ideas, problemas, experiencia, documentos, datasets, incidentes, observaciones, oportunidades de mercado) en salidas de valor (evidencia organizada, conclusiones trazables, conocimiento validado, decisiones, activos reutilizables, hipótesis de producto, oportunidades de monetización).

Este package es exclusivamente documental: no produce software, integraciones técnicas ni plataformas SaaS. Produce documentos metodológicos, frameworks, templates y guías que cualquier lab del portafolio LabOS puede aplicar independientemente del dominio.

La metodología debe ser aplicable a dominios heterogéneos sin asumir que todos utilizan el mismo tipo de evidencia, los mismos métodos de validación ni los mismos ciclos de experimentación.

### Distinciones conceptuales fundamentales

Este package distingue explícitamente entre:

- **Fuente de evidencia**: Origen verificable de información (documento, medición, observación, experimento).
- **Herramienta de análisis**: Instrumento utilizado para procesar, comparar o sintetizar información (Deepnote, NotebookLM, ChatGPT).
- **Repositorio de conocimiento**: Almacén permanente de conocimiento validado (Obsidian, GitHub).
- **Conclusión**: Síntesis fundamentada derivada de evidencia evaluada.
- **Activo**: Artefacto reutilizable extraído de una investigación completada.
- **Producto**: Entregable comercial dirigido a un segmento con propuesta de valor.
- **Oportunidad comercial**: Hipótesis de monetización derivada de hallazgos, que requiere validación independiente.


## Glossary

- **Research_Methodology**: Conjunto de principios, procesos, frameworks y templates que gobiernan cómo se conduce investigación dentro de LabOS.
- **Research_Lifecycle**: Secuencia ordenada de etapas que transforma una pregunta o problema inicial en una conclusión validada y un activo reutilizable.
- **Research_Question**: Pregunta explícita, delimitada y verificable que inicia y guía una investigación.
- **Research_Brief**: Documento inicial que define pregunta, propósito, alcance, timebox y criterios de finalización de una investigación.
- **Evidence_Framework**: Sistema de categorización, evaluación y registro de evidencia con niveles de confianza y limitaciones.
- **Source_Register**: Registro estructurado de todas las fuentes consultadas con evaluación de calidad por criterio.
- **Hypothesis**: Afirmación explícita y falsificable que requiere validación mediante evidencia o experimentación.
- **Quality_Gate**: Punto de control con criterios explícitos que debe superarse para avanzar a la siguiente etapa.
- **Research_Asset**: Artefacto reutilizable producido como resultado de una investigación completada.
- **Product_Hypothesis**: Hipótesis que propone una oportunidad comercial con segmento, formato y evidencia de demanda.
- **Revenue_Hypothesis**: Hipótesis específica sobre mecanismo de ingreso, precio, canal y volumen esperado.
- **Research_Journal**: Registro cronológico de actividades, hallazgos, decisiones y cambios durante una investigación.
- **Decision_Log**: Registro de decisiones con contexto, alternativas evaluadas, justificación y reversibilidad.
- **Experiment**: Actividad controlada diseñada para validar o refutar una hipótesis con criterios predefinidos.
- **Domain_Adaptation**: Ajuste de la metodología general para acomodar particularidades de un dominio específico.
- **Epistemic_Classification**: Sistema de etiquetado que diferencia hechos, hipótesis, interpretaciones y opiniones.
- **Anti_Pattern**: Práctica identificada como contraproducente que debe evitarse.
- **Timebox**: Límite temporal explícito asignado a una investigación o etapa para prevenir trabajo indefinido.
- **Primary_Evidence**: Evidencia obtenida directamente de la fuente original verificable (medición, observación directa, documento oficial).
- **AI_Generated_Content**: Contenido producido por herramientas de IA que requiere verificación contra fuentes primarias antes de tratarse como evidencia.
- **Fundador**: Persona que opera LabOS; único stakeholder con capacidad de decisión y ejecución en la etapa actual.
- **LabOS**: Sistema operativo documental y metodológico para empresas de conocimiento asistidas por IA.
- **Package**: Unidad discreta de trabajo con entregables concretos y criterios de aceptación.


## Requirements

### Requirement 1: Principios de investigación

**User Story:** As a Fundador, I want documented research principles that govern all investigation activity, so that every research effort within LabOS maintains rigor, traceability, and produces actionable outputs.

#### Acceptance Criteria

1. WHEN the Research_Methodology is established, THEN the Research_Methodology SHALL define between 10 and 15 principles that apply to all investigations regardless of domain.
2. WHEN a principle is defined, THEN the Research_Methodology SHALL specify for that principle: a statement of no more than 2 sentences, a rationale of no more than 3 sentences, an observable compliance indicator verifiable by a third party without subjective judgment, and a violation example describing a concrete scenario where the principle is breached.
3. WHEN any investigation is conducted within LabOS, THEN the investigation SHALL comply with all defined principles or document an explicit exception that includes: the principle being excepted, the justification for the exception, the scope of the exception, and the date of the exception decision.
4. WHEN an investigation is initiated, THEN the Research_Methodology SHALL define "investigation" as any research or exploration activity that consumes more than 4 hours of accumulated effort or produces a documented output intended for reuse.
5. IF an investigation concludes without a documented compliance assessment against all defined principles, THEN the investigation SHALL be considered incomplete until the assessment is recorded.

### Requirement 2: Research intake

**User Story:** As a Fundador, I want a structured intake process for research, so that investigations begin with a clear trigger, context, and initial classification before any work is invested.

#### Acceptance Criteria

1. WHEN a research need is identified (from a question, idea, problem, incident, observation, opportunity, or external input), THEN the Research_Methodology SHALL require creation of a Research_Brief before any investigative work exceeding 30 minutes is performed.
2. WHEN a Research_Brief is created, THEN the Research_Brief SHALL contain: trigger (what prompted the investigation, minimum 1 sentence), initial context (background information sufficient to understand the problem space, minimum 2 sentences), requester identity, expected value (a single statement describing the anticipated outcome or benefit), preliminary domain classification (mapped to an existing lab or marked as "unassigned"), and estimated effort category (small <4h, medium 4–16h, large >16h).
3. WHEN a Research_Brief is classified as small effort (<4h), THEN the Research_Methodology SHALL permit a lightweight intake where only trigger, requester, expected value, and origin type are mandatory, and initial context and preliminary domain classification are optional.
4. WHEN a Research_Brief is created, THEN the Research_Brief SHALL declare exactly one origin type from: question, problem, opportunity, incident, dataset, document, or observation.
5. IF a Research_Brief is submitted without all mandatory fields populated for its effort category, THEN the Research_Methodology SHALL reject the submission and indicate which mandatory fields are missing.

### Requirement 3: Problem framing

**User Story:** As a Fundador, I want a structured problem framing stage, so that the core problem is articulated clearly before research questions are formulated.

#### Acceptance Criteria

1. WHEN an investigation advances from Intake to Problem Framing, THEN the Research_Methodology SHALL require documentation of: problem statement (minimum 2 sentences describing the problem), affected context (domain and operational environment), observable symptoms (at least 1 concrete, measurable observation), known constraints (factors that limit possible solutions), and stakeholders impacted (at least 1 named role or group).
2. WHEN a problem is framed, THEN the Research_Methodology SHALL require the Fundador to document the symptom (what is observed, described as a measurable or observable event) and the root problem (a causal explanation of why the symptom occurs) as two separate, labeled fields.
3. WHEN the problem framing is complete, THEN the output SHALL contain at least one research question that includes a defined variable, a target population or context, and a measurable outcome criterion.
4. IF any of the required problem framing fields (problem statement, affected context, observable symptoms, known constraints, stakeholders impacted, symptom, or root problem) is left empty, THEN the Research_Methodology SHALL prevent the investigation from advancing to the next stage and SHALL indicate which fields are missing.

### Requirement 4: Research question formulation

**User Story:** As a Fundador, I want a structured framework for formulating research questions, so that investigations begin with clear, answerable, time-bounded questions that prevent scope drift.

#### Acceptance Criteria

1. WHEN a research question is formulated, THEN the Research_Methodology SHALL require the following components: subject, scope boundary, constraints, expected answer type, and verification method.
2. WHEN a research question is formulated, THEN the Research_Methodology SHALL evaluate it against quality criteria: specificity (scope boundary defines what is included and excluded), answerability (can be resolved with resources identified in the question's constraints), relevance (traces back to the originating problem statement), and time-boundedness (can be answered within a timebox not exceeding 5 working days per question).
3. IF a research question fails one or more quality criteria during evaluation, THEN the Research_Methodology SHALL identify the failing criteria, provide the reason for failure, and require reformulation within a maximum of 3 attempts before escalation.
4. WHEN a question involves more than one independent variable or requires answers from two or more distinct knowledge domains, THEN the Research_Methodology SHALL decompose it into sub-questions with explicit dependency relationships, priority order, and a maximum decomposition depth of 3 levels.
5. IF a research question fails to pass quality criteria after 3 reformulation attempts, THEN the Research_Methodology SHALL flag the question for scope review and require the Fundador to either redefine the originating problem statement or discard the question with a documented rationale.

### Requirement 5: Scope definition

**User Story:** As a Fundador, I want explicit scope definition for every investigation, so that boundaries are clear and prevent unbounded research.

#### Acceptance Criteria

1. WHEN an investigation scope is defined, THEN the Research_Methodology SHALL require documentation of: what is included, what is explicitly excluded, depth of analysis level (one of: superficial — summary of existing sources only; moderate — synthesis and comparison across sources; deep — original analysis with cross-validation of claims), domains involved, and maximum number of sources to consult (specified as an integer between 3 and 50).
2. WHEN scope is defined, THEN the Research_Methodology SHALL require a timebox expressed in hours (minimum 1 hour, maximum 40 hours) and a deadline expressed as a calendar date (format YYYY-MM-DD).
3. IF an investigation has consumed 80% or more of its timebox without reaching a conclusion, THEN the Research_Methodology SHALL require the Fundador to select one of three options: extend the timebox with a written justification stating the new timebox and reason, reduce scope by documenting which elements are removed, or conclude with partial findings documenting what remains unresolved.
4. IF the scope of an investigation needs to change after work has begun, THEN the Research_Methodology SHALL require documentation of: the original scope element being modified, the reason for the change, and the impact on timebox and deadline (confirming whether they remain valid or require adjustment).

### Requirement 6: Assumptions documentation

**User Story:** As a Fundador, I want explicit documentation of assumptions at the start of every investigation, so that hidden premises are surfaced and can be validated or challenged.

#### Acceptance Criteria

1. WHEN an investigation begins, THEN the Research_Methodology SHALL require listing assumptions that could affect the investigation's conclusions, documenting for each: statement, confidence level (high/medium/low), basis for the confidence level assigned, impact if wrong, and proposed validation approach.
2. WHEN an assumption is invalidated during the investigation (evidence contradicts the assumption or its confidence level is reduced to a level below the originally assigned level), THEN the Research_Methodology SHALL require reassessment of all findings that depended on that assumption, producing for each affected finding either a revision, a retraction, or a documented confirmation that the finding remains valid despite the invalidated assumption.
3. WHEN assumptions are documented, THEN the Research_Methodology SHALL classify each as one of: domain assumption (about the subject matter being investigated), methodological assumption (about the research approach or tools used), resource assumption (about time, capacity, or materials available), or contextual assumption (about external conditions or environment).
4. IF an investigation is documented without at least one assumption listed, THEN the Research_Methodology SHALL require explicit justification that no assumptions exist, preventing undocumented hidden premises.

### Requirement 7: Source collection and registration

**User Story:** As a Fundador, I want a structured source collection and registration process, so that all information sources are catalogued, evaluated, and traceable throughout the investigation.

#### Acceptance Criteria

1. WHEN a source is consulted during an investigation, THEN the Source_Register SHALL record: source identifier (unique within the investigation), type (document, API, dataset, person, tool output, observation), access date, author or origin, relevance statement (1-3 sentences linking the source to the research question), and initial quality score (integer 1-5 where 1=lowest, 5=highest).
2. WHEN a source is registered, THEN the Source_Register SHALL evaluate it against 10 dimensions (authority, currency, independence, methodology, reproducibility, bias, conflict of interest, precision, applicability, and traceability), assigning each dimension a score of 0 (not met) or 1 (met), producing an aggregate quality score of 0-10.
3. IF a source scores below 6 out of 10 on the aggregate quality evaluation, THEN the Research_Methodology SHALL permit its use only with an explicit limitation note (stating which dimensions failed) and a confidence weight no greater than 50% of the weight assigned to sources scoring 6 or above.
4. IF no sources score 6 or above out of 10 for a research question, THEN the Research_Methodology SHALL require documenting this gap as a limitation of the investigation, including: the research question affected, the number of sources evaluated, the highest aggregate score achieved, and the dimensions most commonly failed.
5. WHEN a source is registered, THEN the Source_Register SHALL record the evaluation within the same session as the source consultation, before the source is cited in any finding or conclusion.

### Requirement 8: Evidence evaluation

**User Story:** As a Fundador, I want a structured evidence evaluation framework, so that findings are categorized by type and confidence level regardless of domain.

#### Acceptance Criteria

1. WHEN the Evidence_Framework is documented, THEN the Evidence_Framework SHALL define the following mutually exclusive categories for classifying evidence: primary evidence, secondary evidence, direct observation, measurement, experiment result, professional experience, official documentation, scientific literature, market data, testimony, inference, and opinion.
2. WHEN a finding is recorded, THEN the Evidence_Framework SHALL require the following fields: source reference (author or origin and locator), date obtained, evidence category (one from the defined taxonomy), confidence level (1-5 scale where 1 = unverified opinion with no supporting data, 2 = plausible inference without direct evidence, 3 = indirect evidence from analogous context, 4 = direct evidence from a single reliable source, 5 = direct evidence corroborated by multiple independent sources), limitations (at least one statement of scope or applicability constraint), relevance to research question (explicit link to the question the finding addresses), and verifiability assessment (one of: independently reproducible, verifiable against cited source, not independently verifiable).
3. WHEN evidence from different categories or sources conflicts, THEN the Evidence_Framework SHALL require documentation of the conflict including: the conflicting claims stated verbatim or paraphrased, analysis of at least one possible cause of the discrepancy, and a resolution rationale that explicitly addresses each piece of conflicting evidence without discarding any without a stated reason.
4. IF a finding cannot be classified into exactly one evidence category from the defined taxonomy, THEN the Evidence_Framework SHALL require the recorder to assign the single most representative category and document the ambiguity in the limitations field.
5. WHEN the Evidence_Framework is applied to a specific domain, THEN the Evidence_Framework SHALL document which evidence categories are expected to be available or unavailable in that domain, and SHALL NOT reject findings solely because their evidence category is uncommon for the domain.

### Requirement 9: Hypothesis formulation

**User Story:** As a Fundador, I want a structured hypothesis framework, so that assumptions are made explicit, typed, testable, and traceable with clear criteria for acceptance or rejection.

#### Acceptance Criteria

1. WHEN the Research_Methodology defines hypothesis types, THEN the following types SHALL be included: research hypothesis, technical hypothesis, product hypothesis, business hypothesis, revenue hypothesis, and learning hypothesis.
2. WHEN a hypothesis is formulated, THEN the Research_Methodology SHALL require: assertion (a single declarative sentence of no more than 280 characters stating what is believed to be true), prior evidence (at least 1 documented reference or observation supporting the hypothesis), variables (what changes and what is measured), validation method, success criterion (observable condition that would confirm the hypothesis), failure criterion (observable condition that would refute the hypothesis), time limit (between 1 and 90 calendar days), risks, and subsequent decision (what happens if confirmed vs refuted).
3. IF a hypothesis exceeds its defined time limit without validation, THEN the Research_Methodology SHALL require a documented decision containing one of: extend (with at least 1 new evidence reference justifying extension, maximum 2 extensions allowed per hypothesis), revise the hypothesis with updated assertion and criteria, or abandon with a rationale referencing the evidence gap or invalidating condition.
4. WHEN a hypothesis is validated or refuted, THEN the Research_Methodology SHALL require recording the result with at least 1 evidence reference, a confidence level on a scale of 1 to 5 (where 1 is minimal confidence and 5 is high confidence), and a link to the subsequent decision taken.
5. WHEN a hypothesis is created, THEN the Research_Methodology SHALL assign a unique identifier following the pattern HYP-[type-abbreviation]-[sequential-number] to enable traceability across documents and decisions.

### Requirement 10: Experiment design

**User Story:** As a Fundador, I want a structured experiment design framework, so that experiments have clear protocols, variables, controls, and acceptance criteria before execution begins.

#### Acceptance Criteria

1. WHEN an experiment is designed, THEN the Research_Methodology SHALL require: hypothesis under test, independent variables, dependent variables, controlled variables, method description, success criterion (numeric threshold or binary observable outcome), failure criterion (numeric threshold or binary observable outcome), time limit (maximum 90 days), required resources, expected data format, and risks.
2. WHEN an experiment is designed, THEN the Research_Methodology SHALL require classifying it as either a research experiment (validates knowledge by testing a causal or explanatory hypothesis) or a commercial validation experiment (validates demand or willingness to pay by measuring market behavior).
3. IF the independent variables in a domain cannot be isolated or manipulated by the researcher, THEN the Research_Methodology SHALL require selecting at least one alternative validation approach: observational study, comparative analysis, expert review, or triangulation of multiple evidence types, and documenting the justification for why controlled experimentation is not feasible.
4. WHEN an experiment reaches any terminal state (success criterion met, failure criterion met, time limit reached, or abandoned by explicit decision), THEN the Research_Methodology SHALL require documented results including: outcome classification (success, failure, timeout, or abandoned), negative results, unexpected findings, and deviations from protocol.
5. IF an experiment is abandoned before reaching its success or failure criterion, THEN the Research_Methodology SHALL require documenting: reason for abandonment, partial results obtained, lessons learned (maximum 5 sentences), and whether the hypothesis remains open or is reclassified.

### Requirement 11: Results registration

**User Story:** As a Fundador, I want structured registration of all research results, so that findings are documented consistently regardless of whether they are positive, negative, or inconclusive.

#### Acceptance Criteria

1. WHEN a result is obtained from any research activity (source analysis, experiment, observation, comparison), THEN the Research_Methodology SHALL require recording: activity that produced the result, date, result classification (positive, negative, or inconclusive), result description (1-3 paragraphs summarizing what was found), evidence category, confidence level (1-5 scale as defined in Evidence_Framework), supporting data or references, and relationship to the research question.
2. WHEN a negative or inconclusive result is obtained (hypothesis refuted, approach failed, source insufficient, evidence insufficient to conclude), THEN the Research_Methodology SHALL require documenting it using the same mandatory fields as positive results, including what was attempted, why it did not produce a positive finding, and what was learned.
3. WHEN results are registered, THEN the Research_Methodology SHALL require indicating the verification status as one of: preliminary (not yet verified against independent sources), confirmed (verified against at least 2 independent sources), or contested (at least 2 sources provide conflicting evidence on the same finding).
4. WHEN a result's verification status changes (from preliminary to confirmed, or from preliminary to contested), THEN the Research_Methodology SHALL require documenting: the new status, date of change, evidence that triggered the transition, and references to the corroborating or conflicting sources.

### Requirement 12: Conclusion formulation

**User Story:** As a Fundador, I want a structured conclusion framework, so that research findings are synthesized into clear, traceable, and actionable conclusions that distinguish confidence levels.

#### Acceptance Criteria

1. WHEN a conclusion is formulated, THEN the Research_Methodology SHALL require: research question answered, evidence summary with references (citing at least one entry from the Source_Register or Evidence_Framework), confidence level (high: supported by evidence at confidence levels 4-5, medium: supported by evidence at confidence levels 3, low: supported by evidence at confidence levels 1-2, with written justification), limitations, implications for the original problem, at least one recommended action with expected outcome, and open questions remaining.
2. WHEN a conclusion is formulated, THEN the Research_Methodology SHALL require that every conclusion traces back to at least one piece of recorded evidence in the Source_Register or Evidence_Framework.
3. WHEN a conclusion is formulated, THEN the Research_Methodology SHALL require distinguishing between: conclusions supported by strong evidence (2 or more independent sources at confidence level 4-5), conclusions supported by limited evidence (single source or evidence at confidence level 1-3), and conclusions based on inference (logical derivation from indirect evidence without direct source confirmation).
4. IF a conclusion contradicts a previously accepted finding within LabOS, THEN the Research_Methodology SHALL require explicit documentation of the contradiction, analysis of why it occurred, identification of which finding has stronger evidentiary support, and a resolution decision (accept new conclusion, retain previous finding, or flag as unresolved pending further evidence).
5. IF the available evidence is insufficient to support any conclusion for a research question, THEN the Research_Methodology SHALL require documenting an inconclusive outcome with: evidence gaps identified, minimum evidence that would be needed to reach a conclusion, and recommended next steps to obtain that evidence.

### Requirement 13: Uncertainty documentation

**User Story:** As a Fundador, I want explicit documentation of uncertainty and limitations, so that consumers of research outputs understand the boundaries of what was validated and what remains unknown.

#### Acceptance Criteria

1. WHEN an investigation produces conclusions, THEN the Research_Methodology SHALL require a dedicated uncertainty section documenting: known unknowns (identified gaps), methodological limitations, evidence gaps, scope limitations, and areas requiring further investigation, where each item includes a description, the affected conclusion(s), and an impact assessment (high: may invalidate conclusion, medium: reduces confidence, low: minor caveat).
2. WHEN uncertainty is documented, THEN the Research_Methodology SHALL require classifying each uncertainty as: reducible (can be addressed with more research), irreducible (inherent to the domain or context), or temporal (will resolve with time or future events).
3. WHEN findings are communicated, THEN the Research_Methodology SHALL prohibit presenting uncertain conclusions as definitive, requiring that each conclusion with medium or low confidence level includes a visible qualification statement identifying the type of uncertainty and its potential impact on the conclusion's validity.
4. IF an investigation's uncertainty section lists zero items across all categories, THEN the Research_Methodology SHALL require an explicit justification explaining why no uncertainties were identified, subject to verification during human review.

### Requirement 14: Human review

**User Story:** As a Fundador, I want defined human review requirements, so that critical decisions and conclusions are validated by human judgment before being treated as accepted knowledge.

#### Acceptance Criteria

1. WHEN an investigation reaches the Conclusion stage, THEN the Research_Methodology SHALL require human review consisting of the reviewer reading the conclusion, verifying that claims are supported by cited evidence, and recording a review result (approved, revision-needed, or rejected) with date and reviewer identity before the conclusion is accepted as validated knowledge.
2. WHEN an investigation produces findings that will inform decisions in regulated domains (finance, health, legal), THEN the Research_Methodology SHALL require explicit human review with documented approval containing: reviewer identity, date, list of findings reviewed, approval decision, and any conditions or caveats noted.
3. WHEN more than 50% of an investigation's analysis steps are performed by AI-assisted tools, THEN the Research_Methodology SHALL require human verification of each finding that directly supports the conclusion, by checking it against at least one original source cited in the investigation.
4. WHEN human review identifies one or more findings that are unsupported, contradicted by sources, or insufficiently evidenced, THEN the Research_Methodology SHALL require documented remediation actions specifying: the deficiency identified, the corrective action to be taken, the responsible party, and a target resolution date not exceeding 30 calendar days, before the conclusion is accepted.
5. IF a conclusion remains in review status without a recorded review result for more than 14 calendar days, THEN the Research_Methodology SHALL flag the investigation as review-overdue and notify the Fundador.

### Requirement 15: Research asset extraction

**User Story:** As a Fundador, I want a defined process for converting research outputs into reusable assets, so that every completed investigation produces tangible, catalogued artifacts for the LabOS portfolio.

#### Acceptance Criteria

1. WHEN the Research_Methodology defines asset types, THEN the following types SHALL be included: Knowledge Asset (documented insight, framework, comparison), Technical Asset (code, configuration, architecture, tool), Educational Asset (tutorial, guide, course material), Commercial Asset (template, tool, service blueprint for sale), and Data Asset (dataset, benchmark, measurement collection).
2. WHEN an investigation is completed and passes its conclusion Quality_Gate, THEN the Research_Methodology SHALL require extraction of at least one Research_Asset with: name (≤80 characters), type (one of the defined asset types), description (1-3 sentences), usage hypothesis (who would use this and how), target audience, source investigation reference (investigation identifier and conclusion date), and initial state set to "draft".
3. WHEN a Research_Asset is extracted, THEN the Research_Methodology SHALL define the handoff procedure requiring: the asset is placed in the corresponding assets repository category folder, the asset includes a metadata header referencing the source investigation identifier, and the extraction is recorded in the investigation's conclusion document with the asset name and repository location.
4. WHEN a single investigation produces multiple assets, THEN the Research_Methodology SHALL permit cataloguing each independently with its own metadata and usage hypothesis.
5. WHEN a Research_Asset in "draft" state is evaluated for completion, THEN the Research_Methodology SHALL require all of the following quality criteria to be met before transitioning to "complete" state: the description accurately reflects current content, the usage hypothesis identifies at least one specific target audience segment, the asset content is self-contained (usable without requiring access to the source investigation), and the asset has been reviewed by the Fundador.
6. IF an investigation passes its conclusion Quality_Gate but the Fundador determines that no meaningful asset can be extracted, THEN the Research_Methodology SHALL require documenting a justification (1-3 sentences) explaining why no asset was produced, recorded in the investigation's conclusion document.

### Requirement 16: Product hypothesis derivation

**User Story:** As a Fundador, I want a structured process for deriving product hypotheses from research, so that commercial opportunities are identified systematically without premature commitment.

#### Acceptance Criteria

1. WHEN a Product_Hypothesis is derived from an investigation, THEN the Research_Methodology SHALL require answering all of the following fields: (a) what problem was identified by the research and what evidence supports it (minimum 1 documented observation, data point, or user statement), (b) who could benefit (target segment described as a role or profile), (c) what asset can be delivered, (d) what format applies (one of: service, product, content, tool), (e) what commercial evidence exists (at least 1 demand signal: search volume, direct request, competitor existence, or stated willingness to pay), (f) what must be validated before selling (specific assumption and proposed validation method), and (g) what would be the minimum commercial experiment (action, metric, and success threshold within a timeframe of 30 days or less).
2. WHEN a Product_Hypothesis is formulated, THEN the Research_Methodology SHALL require it references the source investigation by identifier, at least 1 piece of supporting evidence (data point, quote, observation, or external source), and a confidence level classified as one of: speculative (no direct evidence, inferred from adjacent data), emerging (1-2 weak signals such as informal mentions or indirect indicators), or supported (3 or more signals, or 1 strong signal such as a paying customer request or documented search demand).
3. WHEN a Product_Hypothesis is formulated, THEN the Research_Methodology SHALL define that the hypothesis may advance to commercial validation only when: (a) all 7 fields from criterion 1 are completed, (b) the confidence level is "emerging" or "supported", and (c) at least 1 demand signal is external to the Fundador (not self-assessed need), aligned with Package 000 Regla 4: validar demanda antes de desarrollar producto.
4. IF a Product_Hypothesis cannot be completed because one or more of the 7 required fields from criterion 1 lack available evidence, THEN the Research_Methodology SHALL mark the hypothesis as "incomplete", identify the missing fields, and require a follow-up investigation action for each missing field before the hypothesis can advance.

### Requirement 17: Revenue hypothesis derivation

**User Story:** As a Fundador, I want a structured process for formulating revenue hypotheses from research findings, so that monetization potential is assessed rigorously without forcing commercial conclusions prematurely.

#### Acceptance Criteria

1. WHEN a Revenue_Hypothesis is formulated, THEN the Research_Methodology SHALL require all of the following fields to be completed: revenue mechanism (how money flows), price hypothesis (expressed as a numeric range with currency and justification source), target segment (described by size, profile, and observable need), channel hypothesis, volume estimate basis (expressed as a numeric range with underlying assumptions stated), evidence supporting demand (at least 1 data point from observation, interview, or market reference), and minimum experiment to validate willingness to pay (with a pass/fail metric and time-bound deadline of no more than 90 days).
2. WHEN an investigation produces fewer than 2 independent data points supporting demand for the identified segment, THEN the Research_Methodology SHALL permit concluding without a Revenue_Hypothesis, documenting: the research question investigated, evidence gathered, reason the evidence is insufficient to support a revenue mechanism, and suggested follow-up conditions that would warrant revisiting.
3. WHEN a Revenue_Hypothesis is formulated, THEN the Research_Methodology SHALL prohibit treating it as validated revenue until a real transaction has occurred, where a real transaction is defined as a documented payment with date, amount in USD, client segment, revenue source, and acquisition channel (aligned with Package 000 revenue thesis promotion criteria).
4. IF a Revenue_Hypothesis is formulated but 1 or more required fields cannot be completed due to lack of evidence, THEN the Research_Methodology SHALL classify it as an incomplete hypothesis, marking the missing fields explicitly and requiring that each missing field include a stated action to obtain the missing evidence within 30 days.

### Requirement 18: Completion criteria and timeboxing

**User Story:** As a Fundador, I want explicit completion criteria and timeboxing for every investigation, so that research does not become indefinite and resources are protected.

#### Acceptance Criteria

1. WHEN an investigation is initiated, THEN the Research_Methodology SHALL require defining at least one of: a timebox (maximum hours of effort, between 1 and 80 hours), a deadline (latest acceptable date), or explicit completion criteria (conditions under which the investigation is considered done).
2. WHEN a timebox is reached, THEN the Research_Methodology SHALL enforce a mandatory decision point where the Fundador must choose one of: conclude the investigation, extend with a documented reason and a new timebox no greater than the original timebox duration (maximum 2 consecutive extensions per investigation), or reduce the scope with updated completion criteria.
3. IF an investigation has no defined completion criteria, timebox, or deadline, THEN the Research_Methodology SHALL flag it as non-compliant and block further work until a timebox, deadline, or completion criteria are added.
4. WHEN completion criteria are met, THEN the Research_Methodology SHALL require progressing to the Conclusion stage within 48 hours.
5. IF the 48-hour grace period elapses without progression to the Conclusion stage, THEN the Research_Methodology SHALL flag the investigation as overdue and notify the Fundador that action is required.

### Requirement 19: Reproducibility

**User Story:** As a Fundador, I want reproducibility requirements for research, so that investigations can be repeated, verified, or extended by the same or different researcher in the future.

#### Acceptance Criteria

1. WHEN an investigation is documented, THEN the Research_Methodology SHALL require recording at minimum: the research question, methodology used, sources consulted (with access dates and archive references), analysis steps performed, and conclusions reached, such that another researcher can follow the same steps and verify the core findings.
2. WHEN an experiment is documented, THEN the Research_Methodology SHALL require recording: environment (operating system, hardware if relevant), tools used with version identifiers, configuration applied, input data or references to input data location, steps performed in execution order, and output obtained.
3. IF reproducibility is impractical (one-time observations, expired sources, ephemeral data), THEN the Research_Methodology SHALL require documenting: the reason reproduction is not possible, the date the limitation was identified, and what evidence is preserved as record (screenshots, exports, logs, or copies).
4. WHEN sources are referenced in an investigation or experiment, THEN the Research_Methodology SHALL require that each source is either archived locally, captured via snapshot, or accompanied by an access date, so that source unavailability does not silently break reproducibility.

### Requirement 20: Privacy and data handling

**User Story:** As a Fundador, I want privacy and data handling guidelines, so that research within LabOS respects personal data boundaries, client confidentiality, and regulatory requirements.

#### Acceptance Criteria

1. IF research involves personal data, THEN the Research_Methodology SHALL require documentation of: data type, collection method, storage location, access controls, retention period (maximum 365 days unless regulatory obligation requires longer), and deletion procedure — completed before any data collection begins.
2. IF research involves client information or data classified as confidential (data subject to NDA, contractual restriction, or containing third-party PII), THEN the Research_Methodology SHALL prohibit storing that data in public repositories or unencrypted locations.
3. WHEN research produces outputs that reference identifiable individuals, THEN the Research_Methodology SHALL require anonymization (removal or replacement of all attributes that permit direct or indirect identification) or explicit consent documentation before the output is stored or shared.
4. IF research involves regulated domains (finance, health, or any domain subject to jurisdiction-specific regulation documented in the scope-and-boundaries regulatory tables), THEN the Research_Methodology SHALL require documenting applicable regulatory constraints and compliance measures before data processing begins.
5. IF a research activity is found to lack the required privacy documentation specified in criteria 1 through 4, THEN the Research_Methodology SHALL require suspension of data processing for that activity until documentation is completed and reviewed by the Fundador.

### Requirement 21: Intellectual property

**User Story:** As a Fundador, I want intellectual property guidelines, so that research respects copyright, licensing, and attribution requirements throughout the investigation process.

#### Acceptance Criteria

1. WHEN a source is used in research, THEN the Research_Methodology SHALL require documenting at minimum: the source name, author or rights holder, license type, permitted uses, and any attribution requirements specified by the license.
2. WHEN research produces assets intended for commercial use, THEN the Research_Methodology SHALL require verifying that all incorporated sources have a documented license permitting commercial usage before the asset is marked as ready for commercial distribution.
3. WHEN research incorporates third-party content, THEN the Research_Methodology SHALL require attribution that includes: original author or rights holder, source title or identifier, license type, and year of publication where available, in all outputs where the content appears.
4. IF a source lacks an explicitly stated license, has conflicting license information, or the Fundador cannot determine whether commercial use is permitted, THEN the Research_Methodology SHALL require documenting the specific uncertainty, marking the affected content as "IP-unresolved", and restricting commercial use of outputs containing that content until a determination is made.
5. WHEN a source's licensing terms prohibit the intended use of the research output, THEN the Research_Methodology SHALL require either removing the source from the output or replacing it with a compatibly licensed alternative before publication.

### Requirement 22: Responsible use of AI

**User Story:** As a Fundador, I want explicit rules for responsible AI use in research, so that AI-generated content is properly classified, verified, and never treated as primary evidence without human validation.

#### Acceptance Criteria

1. WHEN AI tools (ChatGPT, NotebookLM, or any AI system) generate substantive content during research (including summaries, factual claims, explanations, or analysis — excluding minor edits such as spell-check or grammar correction), THEN the Research_Methodology SHALL classify that output as AI_Generated_Content, not as Primary_Evidence.
2. WHEN AI-generated content is used to support a research conclusion, THEN the Research_Methodology SHALL require verification, defined as the researcher independently locating the cited primary source and confirming that the specific claim exists in that source, before the content can support a conclusion.
3. WHEN an AI-generated response, summary, or explanation is incorporated into research findings, THEN the Research_Methodology SHALL require labeling it as AI-generated with: tool name, date of generation, a description of the query intent (maximum 200 characters), and a verification status field indicating one of: verified, unverified, or source-not-found.
4. IF an AI tool provides a factual claim and the underlying primary source has not been independently located and verified by the researcher through direct access (not through the same AI tool), THEN the Research_Methodology SHALL prohibit citing that claim as evidence in any research conclusion.
5. WHEN AI tools are used for analysis or synthesis, THEN the Research_Methodology SHALL permit their use as analytical aids while requiring that every conclusion presented as a research finding rests on at least one verified primary source, not solely on the AI output.
6. IF a researcher attempts to verify an AI-generated factual claim and the cited primary source cannot be located or does not contain the claimed information, THEN the Research_Methodology SHALL require the researcher to discard the claim as unsupported and record the failed verification attempt in the research log with the date and source sought.

### Requirement 23: Domain-specific adaptations

**User Story:** As a Fundador, I want a framework for domain-specific adaptations, so that the methodology accommodates differences in evidence types, validation methods, and constraints across the diverse LabOS portfolio.

#### Acceptance Criteria

1. WHEN the Research_Methodology defines adaptations, THEN the Research_Methodology SHALL specify which methodology elements are fixed (non-negotiable across domains) and which are adaptable (can be customized per domain), listing each element explicitly with its classification.
2. WHEN a Domain_Adaptation is defined, THEN the Research_Methodology SHALL specify: domain name, applicable evidence types (minimum 1), available validation methods (minimum 1), relevant tools, domain-specific constraints, typical research types (minimum 1), and at least one example application consisting of a scenario description, the methodology steps applied, and the expected output type.
3. WHEN Domain_Adaptations are defined, THEN the Research_Methodology SHALL provide adaptations for at least: technical domains (AWS, Kubernetes, DevOps, AIOps), quantitative domains (trading, finance, data analysis), creative domains (photography, music, content creation), educational domains (English, training, longevity), and business domains (marketing, SaaS, AI agents).
4. IF a domain does not permit controlled experimentation, THEN the Domain_Adaptation SHALL define at least one alternative validation approach specifying: the validation technique name, the type of evidence it produces, the acceptance threshold for considering a hypothesis validated or refuted, and any limitations of the approach compared to controlled experimentation.
5. WHEN a new domain is added to the LabOS portfolio, THEN the Research_Methodology SHALL provide a template for creating its Domain_Adaptation containing at minimum the following sections: domain name, evidence types, validation methods, tools, constraints, research types, and example application.
6. WHEN a Domain_Adaptation is defined, THEN the Research_Methodology SHALL verify that no adaptable element in the Domain_Adaptation contradicts or omits any element classified as fixed in criterion 1.

### Requirement 24: Research metrics

**User Story:** As a Fundador, I want defined metrics for research activity, so that the health and productivity of the research process can be measured, tracked, and improved over time.

#### Acceptance Criteria

1. WHEN research metrics are defined, THEN the Research_Methodology SHALL define the following metrics, each with a measurement method and measurement period of one calendar month: investigations initiated per month, investigations completed per month, average elapsed days per investigation grouped by effort category (small: ≤4 hours, medium: 5–16 hours, large: 17–40 hours), assets produced per investigation, product hypotheses generated per month, quality gate pass rate (percentage of investigations passing quality gate on first submission), distinct domains investigated per month, and ratio of completed-to-abandoned investigations per month.
2. WHEN metrics are reviewed, THEN the Research_Methodology SHALL define a review cadence of at least once per calendar month in which all metrics from criterion 1 are evaluated and the results are recorded with date and reviewer.
3. IF any of the following conditions is met, THEN the Research_Methodology SHALL flag a warning signal: an investigation exceeds its assigned timebox by more than 50% of the timebox duration, fewer than 1 asset is produced per 2 completed investigations in a month, an investigation is closed without a documented conclusion, the same investigation fails the quality gate 2 or more times, or more than 70% of investigations in a month belong to a single domain.
4. WHEN a warning signal is flagged, THEN the Research_Methodology SHALL document at least one recommended corrective action per signal, stating the observed problem and a suggested adjustment to process, scope, or resource allocation, without mandating a specific implementation solution.

### Requirement 25: Critical final review

**User Story:** As a Fundador, I want a structured final review process for each investigation, so that quality, completeness, and compliance are verified before an investigation is archived.

#### Acceptance Criteria

1. WHEN an investigation reaches the Review stage, THEN the Research_Methodology SHALL require evaluation against the following checklist where each item is marked pass or fail: (a) research question explicitly answered with a stated conclusion, (b) at least 3 independent evidence items supporting the conclusion, (c) all cited sources verified as accessible and dated within 5 years unless historical context requires otherwise, (d) each conclusion traceable to specific evidence items by reference, (e) uncertainties and confidence level (high/medium/low) documented for each conclusion, (f) at least one reusable asset extracted and registered, (g) limitations of scope and method explicitly stated, and (h) compliance with the project's documented ethical guidelines.
2. WHEN the final review identifies one or more checklist items marked as fail, THEN the Research_Methodology SHALL require a documented remediation entry for each failed item that references the specific section being corrected, and SHALL allow a maximum of 3 remediation cycles before the investigation must be classified as abandoned or completed-with-limitations.
3. WHEN all 8 checklist items are marked pass after review or remediation, THEN the Research_Methodology SHALL classify the investigation as "completed"; WHEN 6 or more checklist items are marked pass and the remaining failures are documented as acceptable limitations, THEN the Research_Methodology SHALL classify the investigation as "completed-with-limitations"; WHEN fewer than 6 checklist items are marked pass or remediation cycles are exhausted without resolution, THEN the Research_Methodology SHALL classify the investigation as "abandoned" with a documented rationale.
4. IF a deficiency identified during final review cannot be remediated because the required information is unavailable or the scope is no longer relevant, THEN the Research_Methodology SHALL require the Fundador to document the reason for irresolvability and classify the investigation as "completed-with-limitations" or "abandoned" based on the pass threshold defined in criterion 3.

### Requirement 26: Research lifecycle stages

**User Story:** As a Fundador, I want a complete research lifecycle definition, so that investigations progress through defined stages with clear transitions, inputs, outputs, and governance.

#### Acceptance Criteria

1. WHEN the Research_Lifecycle is defined, THEN the Research_Lifecycle SHALL include the following ordered stages: Intake, Problem Framing, Research Question, Scope, Assumptions, Source Collection, Evidence Evaluation, Analysis, Experimentation, Findings, Conclusion, Review, Asset Extraction, Product Hypothesis, Publication or Archive, Feedback and Iteration.
2. WHEN a lifecycle stage is defined, THEN the Research_Lifecycle SHALL specify for each stage: stage name, input (what artifact or information is needed to enter), activity (what work is performed), output (what artifact is produced upon completion), responsible party (Fundador or AI agent), completion criteria (observable conditions that indicate the stage is done), risks (what could block or degrade the stage), and applicable tools.
3. WHEN a stage transition is defined, THEN the Research_Lifecycle SHALL specify: the minimum completion criteria that must be satisfied to advance to the next stage, and the specific conditions (such as invalidated assumptions or insufficient evidence) that trigger a return to a previous stage.
4. WHEN the Research_Lifecycle supports non-linear progression, THEN the Research_Lifecycle SHALL require documenting the justification for any loop-back to a previous stage including: the triggering condition, the target stage, the reason the current stage output is insufficient (1-3 sentences), and the expected outcome of repeating the target stage.
5. IF a research investigation loops back to the same stage more than 3 times, THEN the Research_Lifecycle SHALL require a decision record documenting whether to continue, pivot the research question, or close the investigation with a closure rationale.
6. WHEN a stage has a recommended maximum duration, THEN the Research_Lifecycle SHALL document that duration in hours or calendar days and specify the escalation action: the Fundador reviews progress, documents the blocker, and decides whether to extend (with revised deadline), skip the stage with documented rationale, or close the investigation.
7. WHEN a research investigation completes the lifecycle, THEN the Research_Lifecycle SHALL require that at least one output qualifies as an asset per the asset extraction criteria (name, type, description, usage hypothesis, and state), or that a closure note is registered explaining why no asset was produced.

### Requirement 27: Research types taxonomy

**User Story:** As a Fundador, I want a comprehensive taxonomy of research types, so that I can select the appropriate methodology for each investigation context and domain.

#### Acceptance Criteria

1. WHEN the Research_Methodology defines research types, THEN the following types SHALL be included: Exploratory, Descriptive, Comparative, Experimental, Diagnostic, Market, Product, Technical, Quantitative, Qualitative, Educational, and Creative.
2. WHEN a research type is defined, THEN the Research_Methodology SHALL specify the following fields for each type: purpose (1–3 sentences describing the goal), at least 3 typical questions addressed, at least 2 applicable domains from the active labs portfolio, at least 2 evidence types typically produced, at least 1 validation method, expected outputs (as a list of deliverable categories), and at least 2 scenarios of when to use and at least 2 scenarios of when not to use.
3. WHEN an investigation is initiated, THEN the Research_Brief SHALL declare which research type (or combination of up to 3 types) applies and include a 1–2 sentence justification for each selected type explaining why it fits the investigation's question.
4. WHEN 2 or more research types are combined in a single investigation, THEN the Research_Brief SHALL document how each type contributes to the overall research question and specify which phase or aspect of the investigation each type addresses.
5. WHEN a research type definition includes the "when to use vs when not to use" field, THEN the Research_Methodology SHALL reference at least one contrasting type to clarify boundaries between types that may overlap in scope.

### Requirement 28: Tooling responsibilities and workflow

**User Story:** As a Fundador, I want defined tool responsibilities and handoff protocols, so that each tool in the LabOS ecosystem has a clear role without overlap, and traceability is maintained across tool boundaries.

#### Acceptance Criteria

1. WHEN tool responsibilities are defined, THEN the Research_Methodology SHALL assign the following exclusive roles: ChatGPT Projects (contextual conversation, debate, draft generation, review, planning), NotebookLM (documentary consultation, source comparison, referenced summaries from uploaded documents), Deepnote (data analysis, reproducible notebooks, quantitative experimentation, visualizations), Obsidian (permanent knowledge, atomic notes, conceptual relationships, personal knowledge base), GitHub (versioned documentation, code, datasets, templates, decision records, traceability), and Kiro (spec-driven development, requirements, design, tasks, implementation).
2. WHEN a research stage requires tool usage, THEN the Research_Methodology SHALL specify which tools are applicable and what role each plays in that stage, referencing the role assignments defined in criterion 1.
3. WHEN work transitions between tools, THEN the Research_Methodology SHALL define a handoff protocol that includes at minimum: a summary of work completed in the source tool, source references used, decisions made with rationale, and a version identifier or commit linking to the prior state.
4. WHEN a tool produces output, THEN the Research_Methodology SHALL classify that output as one of: analytical aid (tool used for processing, not stored as permanent record), repository content (permanent record committed to GitHub), or generated content (AI-produced, marked with origin tool and date, requiring human review before promotion to repository content).
5. IF a task could be performed by more than one tool based on the role assignments, THEN the Research_Methodology SHALL resolve the overlap by designating one tool as primary for that task and documenting the selection rationale in the stage specification.

### Requirement 29: Quality gates

**User Story:** As a Fundador, I want defined quality gates at critical lifecycle transitions, so that investigations maintain rigor and prevent advancement without sufficient evidence or documentation.

#### Acceptance Criteria

1. WHEN the Research_Methodology defines Quality_Gates, THEN the following gates SHALL be included: gate to initiate research, gate to begin experiments, gate to accept findings, gate to approve conclusions, gate to extract assets, gate to publish or share externally, and gate to utilize commercially.
2. WHEN a Quality_Gate is defined, THEN the Research_Methodology SHALL specify: gate name, position in lifecycle, required inputs (≥1 named input per gate), evaluation criteria (checklist with ≥3 verifiable items per gate), pass conditions (binary pass/fail outcome), fail actions, and responsible party (Fundador in current stage).
3. IF an investigation fails a Quality_Gate, THEN the Research_Methodology SHALL require ≥1 remediation action per failure, each specifying: assignee, deadline (≤30 days), and completion criterion, before re-evaluation is permitted.
4. IF an investigation fails the same Quality_Gate 3 consecutive times, THEN the Research_Methodology SHALL require a documented decision to either abandon the investigation or escalate with a revised approach before further re-evaluation is permitted.
5. WHEN the Research_Methodology defines Quality_Gates, THEN the gates SHALL provide an alternative evidence path for domains where the Fundador documents ≥1 constraint preventing controlled experimentation (ethical, legal, cost, or time), replacing experimentation requirements with equivalent rigor criteria such as literature review, expert consultation, or observational evidence.

### Requirement 30: Anti-patterns

**User Story:** As a Fundador, I want documented research anti-patterns, so that common mistakes are identified, recognizable, and preventable across all research activities.

#### Acceptance Criteria

1. WHEN anti-patterns are defined, THEN the Research_Methodology SHALL provide for each: a name (≤5 words), a description (2-4 sentences), observable symptoms (at least 2), consequences if not corrected (at least 1), and a recommended correction (at least 1 actionable step).
2. WHEN anti-patterns are defined, THEN the Research_Methodology SHALL include at minimum the following 7 general anti-patterns: treating extensive documentation as validated knowledge, treating AI-generated responses as primary evidence, affirming validation without explicit criteria, conducting indefinite research without completion criteria, automatically converting every investigation into a commercial product, confusing activity (hours spent) with progress (questions answered), and ignoring negative results.
3. WHEN anti-patterns are defined, THEN the Research_Methodology SHALL include at minimum the following 4 AI-specific anti-patterns: accepting AI summaries without verifying sources, using AI confidence as a proxy for evidence quality, delegating judgment to AI without human review, and treating AI consensus across tools as independent confirmation.
4. WHEN anti-patterns are defined, THEN the Research_Methodology SHALL map each anti-pattern to at least one research lifecycle stage (question formulation, source discovery, evidence gathering, analysis, synthesis, validation, or asset production) and provide at least one checklist question per stage that enables detection of applicable anti-patterns during that stage.

### Requirement 31: Prudent monetization

**User Story:** As a Fundador, I want explicit rules for prudent monetization of research, so that commercial opportunities are identified without forcing products from insufficient evidence or premature conclusions.

#### Acceptance Criteria

1. WHEN an investigation identifies a potential commercial application, THEN the Research_Methodology SHALL require documenting the opportunity as a hypothesis with the 3 minimum monetization fields (target segment, delivery format, revenue model) and classifying it with the epistemic label [Hipótesis] until at least 1 verifiable external demand signal (message, meeting, request, or documented search) exists.
2. IF a monetization opportunity lacks at least 1 verifiable external demand signal, OR the domain has no documented target segment willing to pay, OR the asset does not meet the minimum asset registration criteria (name, type, description, usage hypothesis, and declared state), THEN the Research_Methodology SHALL not permit initiation of product development and SHALL require the opportunity to remain in hypothesis status.
3. WHEN a Product_Hypothesis or Revenue_Hypothesis is formulated, THEN the Research_Methodology SHALL require that it passes the commercial utilization Quality_Gate — defined as having all 3 monetization fields documented, a validation experiment designed with a numeric success metric and a deadline of 30 days maximum, and at least 1 verifiable external demand signal — before any development investment exceeding 2 hours per week begins.
4. WHEN research produces knowledge that has been registered as a valid asset (meeting the 5-field minimum criteria) but has generated 0 external demand signals after 30 days of availability, THEN the Research_Methodology SHALL permit archiving it as a Knowledge Asset without requiring a monetization plan, documenting the date and the absence of commercial signal.
5. IF a Product_Hypothesis or Revenue_Hypothesis fails its Quality_Gate validation experiment (does not meet its numeric success metric within its defined deadline), THEN the Research_Methodology SHALL require documenting the failure result and either reformulating the hypothesis with a new experiment or archiving the opportunity as a Knowledge Asset within 7 days of the deadline expiration.

### Requirement 32: Research journal and decision log

**User Story:** As a Fundador, I want structured research journals and decision logs, so that the chronological progression and decision rationale of investigations are preserved for future reference and reproducibility.

#### Acceptance Criteria

1. WHEN a work session on an investigation concludes, THEN the Research_Journal SHALL record an entry with: date (ISO 8601), stage (current lifecycle stage from the investigation's defined stages), activity performed (1-3 sentences), findings (summary of results or observations), decisions made (if any), next steps (at least 1 concrete action), time invested (in minutes), and tools used (list of tool names).
2. WHEN the Research_Journal maintains entries, THEN the Research_Journal SHALL maintain entries in chronological order by date, with each entry uniquely identifiable by its sequential position within the journal.
3. WHEN a Decision_Log entry is created, THEN the Decision_Log SHALL record: decision description (1-3 sentences), context (situation that prompted the decision), alternatives considered (at least 2 options evaluated), selection rationale (why the chosen option was selected over alternatives), evidence supporting the decision (at least 1 referenced source or observation), consequences expected (anticipated outcomes), reversibility assessment (one of: easily reversible, reversible with effort, irreversible), and date (ISO 8601).
4. WHEN a decision changes the scope, direction, or methodology of an investigation, THEN the Decision_Log SHALL document the change with a reference to the triggering evidence or event, where a valid reference is: a link to a document, a dated journal entry number, a quoted observation, or a named external source.
5. WHEN an investigation exceeds 4 hours of cumulative effort, THEN the Research_Methodology SHALL require maintaining a Research_Journal (aligned with Package 000 Regla 3: investigación mayor a 4h como activo). IF the 4-hour threshold is reached without an existing Research_Journal, THEN the Fundador SHALL create the Research_Journal retroactively, reconstructing entries from available records within the same work session in which the threshold is identified.

### Requirement 33: Templates

**User Story:** As a Fundador, I want reusable, domain-agnostic templates for all research artifacts, so that investigations follow a consistent structure, reduce setup time, and enable comparison across investigations.

#### Acceptance Criteria

1. WHEN the Research_Methodology defines templates, THEN the Research_Methodology SHALL provide the following 9 templates: research brief, research plan, source register, experiment design, research journal, decision log, conclusion, research asset handoff, and research review.
2. WHEN a template is defined, THEN the Research_Methodology SHALL include: purpose (1–3 sentences), required fields section, optional fields section, usage instructions (step-by-step, minimum 3 steps), a domain-specific optional sections area separated by a "## Domain-Specific Sections" header, and one completed example that fills all required fields with realistic sample data.
3. WHEN templates are created, THEN the Research_Methodology SHALL store them in docs/templates/research/ using kebab-case file names in English matching the pattern `{artifact-name}-template.md` (e.g., `research-brief-template.md`, `research-plan-template.md`).
4. WHEN templates are designed, THEN the Research_Methodology SHALL ensure that required fields contain no references to a specific industry, technology, or subject domain, and that optional domain-specific sections are marked with a `[DOMAIN-SPECIFIC]` label prefix in the section header.
5. WHEN templates are stored in docs/templates/research/, THEN the Research_Methodology SHALL provide an index file (docs/templates/research/README.md) listing each template with its file name, purpose summary, and the count of required fields.

### Requirement 34: Package deliverables and structure

**User Story:** As a Fundador, I want a complete and defined package structure, so that all methodology documents are organized, navigable, and reviewable as a cohesive unit.

#### Acceptance Criteria

1. WHEN the Package is produced, THEN the Package SHALL deliver 26 numbered documents (001 through 026) in docs/packages/package-001-research-methodology/, where each document contains at minimum: a title header, a purpose section, a body section with substantive content, and an epistemic classification tag ([Hecho], [Hipótesis], [Visión], or [Decisión]).
2. WHEN the Package is produced, THEN the Package SHALL deliver 9 templates in docs/templates/research/, where each template contains at minimum: a title header, a purpose statement, placeholder sections with instructions for the user, and at least one usage example or guidance note.
3. WHEN the Package is produced, THEN the Package SHALL include a README serving as: a document index listing all 26 documents with file name and one-line description, an authoritative glossary defining every domain-specific term introduced in the package (minimum one definition per term with no undefined terms referenced across documents), and a state declaration indicating the current package status (one of: pendiente, en progreso, completo, en revisión).
4. WHEN the Package is produced, THEN the Package SHALL include a package summary (document 025) that lists every methodology decision made within the package (with document of origin and rationale reference), and includes a consistency declaration stating that no internal contradictions exist between the 26 documents regarding terminology, principles, or process definitions.
5. WHEN the Package is produced, THEN the Package SHALL include a package review (document 026) with: an approval checklist covering structural completeness of all 26 documents and 9 templates, a traceability verification confirming that each document traces back to at least one objective stated in the package README, and a reviewer sign-off section with fields for reviewer name, date, and approval result (approved, approved with observations, or rejected).
6. WHEN the Package is produced, THEN the Package SHALL not contradict principles, decisions, or terminology established in Package 000 — Foundation, where contradiction is defined as: using a term with a different meaning than its Package 000 glossary definition, asserting a statement that negates a principle in 006-operating-principles or 005-manifesto, or establishing a process that violates a rule documented in Package 000.
7. WHEN the Package is produced, THEN the Package SHALL use file naming convention NNN-descriptive-name.md (kebab-case, English) for all 26 numbered documents and maintain sequential numbering from 001 to 026 with no gaps.

### Requirement 35: Package approval criteria

**User Story:** As a Fundador, I want explicit and verifiable approval criteria for the package, so that completion is unambiguous and all stakeholders agree on what "done" means.

#### Acceptance Criteria

1. WHEN the Package is evaluated for approval, THEN the Package SHALL be considered approvable only when all of the following conditions are independently verified as "pasa" or "no pasa": (a) the lifecycle defines named stages with entry/exit criteria applicable to at least 2 distinct portfolio domains, (b) each tool's responsibility is documented with input, output, and boundary such that no two tools claim the same input-output pair, (c) every research question is linked to a documented conclusion or explicit "inconclusive" declaration with rationale, (d) every investigation references at least one extracted asset by name and location, (e) sources are documented with epistemic classification (Hecho, Hipótesis, or Visión) per the project's documentation standards, (f) each lifecycle stage has at least one completion criterion expressed as an observable condition, (g) every research activity has a maximum duration or maximum iteration count after which it must produce a deliverable or be closed, (h) templates contain no domain-specific content and include usage instructions referencing at least 2 example domains, (i) domain differences are listed with the specific adaptation required per domain, (j) ethics, privacy, and quality controls each have at least one defined verification method, and (k) no statement in the package contradicts a statement in Package 000 as verified by cross-referencing the Package 000 glossary and principles.
2. WHEN the Package is submitted for approval, THEN the Research_Methodology SHALL require Fundador review consisting of a recorded evaluation date, a binary result (pasa/no pasa) per each condition in criterion 1, and an explicit sign-off statement before the package state changes to "completed".
3. IF the package review identifies one or more conditions from criterion 1 evaluated as "no pasa", THEN the Package SHALL document each deficiency with: the specific condition identifier (a-k) that failed, a reference to the affected section, and a description of the required correction sufficient for a reviewer to verify resolution.
4. IF a deficiency documented per criterion 3 is corrected, THEN the Package SHALL require re-evaluation of only the previously failed conditions before the package state may change to "completed".

### Requirement 36: Restrictions and boundaries

**User Story:** As a Fundador, I want explicit restrictions documenting what this package does NOT do, so that scope is contained, expectations are clear, and the package does not overpromise.

#### Acceptance Criteria

1. WHEN the Package defines its scope, THEN the Package SHALL explicitly exclude: software implementation, API development, database creation, technical infrastructure deployment, SaaS platform definition, functional integrations that exchange data between external tools at runtime, storage of credentials or tokens, and creation of commercial products.
2. WHEN the Package defines evidence standards, THEN the Package SHALL prohibit: treating AI-generated responses as primary evidence, affirming validation without explicit verifiable criteria, requiring experimentation in domains where it would require capital investment exceeding available resources or regulatory authorization not yet obtained, equating documentation volume alone with validated knowledge, and automatically converting every investigation into a commercial product.
3. WHEN the Package defines its relationship to other packages, THEN the Package SHALL declare: the packages it depends on (by number and name), and for each expected consumer package (at minimum Packages 002 through 009), what specific methodology or definition from this Package that consumer will reference.
4. IF any document within the Package contains content that matches an item on the exclusion list in criterion 1 or the prohibition list in criterion 2, THEN the Package SHALL be considered non-conformant and the violating content SHALL be identified by document name and section.
