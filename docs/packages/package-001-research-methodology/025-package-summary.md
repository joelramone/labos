# 025 — Package Summary

> **Etiqueta epistémica:** [Hecho]
>
> **Requirements cubiertos:** R34.4, R34.5, R36.1, R36.2, R36.3, R36.4

## Propósito

Este documento consolida todas las decisiones metodológicas registradas en los 26 documentos del Package 001 — Research Methodology, declara el estado de consistencia inter-documentos, documenta exclusiones explícitas de alcance y establece las relaciones con otros packages del portafolio LabOS. [Hecho]

Funciona como inventario de decisiones clave que conforman la metodología de investigación de LabOS, permitiendo verificar coherencia sin necesidad de recorrer los 26 archivos individualmente. [Hecho]

---

## Decisiones metodológicas por documento

### README.md

- [Decisión] El glosario del README.md es la **fuente de verdad terminológica** del package. Todo término de dominio se define aquí y se referencia desde los demás documentos sin redefinición.
- [Decisión] Se definen **23 términos canónicos** en el glosario (Research_Methodology, Research_Lifecycle, Research_Question, Research_Brief, Evidence_Framework, Source_Register, Hypothesis, Quality_Gate, Research_Asset, Product_Hypothesis, Revenue_Hypothesis, Research_Journal, Decision_Log, Experiment, Domain_Adaptation, Epistemic_Classification, Anti_Pattern, Timebox, Primary_Evidence, AI_Generated_Content, Fundador, LabOS, Package).
- [Decisión] El estado del package se declara con valores válidos: `pendiente`, `en progreso`, `completo`, `en revisión`.

### 001-research-principles.md

- [Decisión] Se establecen **12 principios fundacionales** que gobiernan toda investigación independientemente del dominio.
  - **Rationale:** R1.1 requiere entre 10-15 principios universales; 12 provee cobertura suficiente sin redundancia.
- [Decisión] Se define **investigación** como toda actividad que consume >4h de esfuerzo acumulado O produce output reutilizable.
  - **Rationale:** R1.4 requiere una definición explícita del umbral.
- [Decisión] Los principios 2 (Evidencia sobre opinión) y 9 (AI como herramienta) **no admiten excepción completa** — solo parcial de alcance limitado.
  - **Rationale:** Proteger la integridad epistémica del sistema contra degradación.
- [Decisión] Máximo **3 excepciones simultáneas** por investigación; más de 3 requiere reevaluar si la actividad califica como investigación.
  - **Rationale:** Evitar que las excepciones se conviertan en la norma.
- [Decisión] Toda investigación incluye un **compliance assessment** contra los 12 principios como condición de cierre.
  - **Rationale:** R1.5 define investigación sin assessment como incompleta.

### 002-research-lifecycle.md

- [Decisión] El lifecycle define **16 etapas secuenciales** con modelo de estados y loop-back documentado.
  - **Rationale:** R2.1, R26.1 requieren etapas definidas con inputs/outputs/gates.
- [Decisión] Se define un **modelo de 11 estados** (Proposed, Framed, Planned, In Progress, Blocked, Under Review, Completed, Converted to Asset, Published, Archived, Rejected) con transiciones permitidas y prohibidas.
  - **Rationale:** R26.3 requiere transiciones documentadas con criterios explícitos.
- [Decisión] Loop-back a la misma etapa **más de 3 veces** activa decisión obligatoria: continuar, pivotar, o cerrar.
  - **Rationale:** R26.5 requiere mecanismo de escalación para prevenir ciclos infinitos.
- [Decisión] Cada etapa tiene **duración máxima recomendada** con protocolo de escalación (extender, saltar, cerrar).
  - **Rationale:** R26.6 requiere límites temporales por etapa.
- [Decisión] Artefactos mínimos varían por **effort category**: Small (<4h), Medium (4-16h), Large (>16h).
  - **Rationale:** R26.7 requiere proporcionalidad entre esfuerzo y documentación.

### 003-research-types.md

- [Decisión] Se definen **12 tipos de investigación** mutuamente exclusivos con guía de selección y combinación.
  - **Rationale:** R27.1 requiere taxonomía completa de tipos de investigación.
- [Decisión] **Máximo 3 tipos** por investigación; más de 3 indica necesidad de descomposición.
  - **Rationale:** R27.3 requiere reglas de combinación.
- [Decisión] Cada tipo seleccionado requiere **justificación de 1-2 oraciones** en el Research_Brief.
  - **Rationale:** R27.4 requiere justificación de selección documentada.

### 004-research-question-framework.md

- [Decisión] Las research questions requieren **5 componentes**: subject, scope boundary, constraints, expected answer type, verification method.
  - **Rationale:** R4.1 define los componentes obligatorios.
- [Decisión] Evaluación contra **4 criterios de calidad**: specificity, answerability, relevance, time-boundedness.
  - **Rationale:** R4.2 define los criterios de evaluación.
- [Decisión] **Máximo 3 intentos** de reformulación antes de escalación.
  - **Rationale:** R4.3 requiere límite de iteraciones.
- [Decisión] Descomposición con **máximo 3 niveles** de profundidad.
  - **Rationale:** R4.4 define el límite de descomposición.

### 005-hypothesis-framework.md

- [Decisión] Se definen **6 tipos de hipótesis**: research, technical, product, business, revenue, learning.
  - **Rationale:** R9.1 define los tipos obligatorios.
- [Decisión] Identificador único con formato **HYP-[type-abbreviation]-[sequential-number]**.
  - **Rationale:** R9.5 requiere trazabilidad mediante ID único.
- [Decisión] Hipótesis que excede time limit permite **máximo 2 extensiones** antes de revisión o abandono.
  - **Rationale:** R9.3 define el mecanismo de timeout.

### 006-evidence-framework.md

- [Decisión] Se definen **12 categorías mutuamente exclusivas** de evidencia.
  - **Rationale:** R8.1 requiere categorías definidas y mutuamente exclusivas.
- [Decisión] Escala de confianza de **5 niveles** (1=unverified opinion → 5=corroborated evidence).
  - **Rationale:** R8.2 define la escala.
- [Decisión] Confidence ceiling: `opinion` e `inference` máximo 3; evidencia `unverified` máximo 2 en conclusiones.
  - **Rationale:** R8.3 requiere reglas de integridad entre tipo y confianza.
- [Decisión] AI-generated content **no puede ser Primary Evidence** sin verificación humana contra fuente original.
  - **Rationale:** R22 requiere restricciones sobre contenido IA.
- [Decisión] Evidencia contestada requiere documentación del conflicto sin descarte silencioso.
  - **Rationale:** R8.3 requiere manejo explícito de conflictos.
- [Decisión] Resultados negativos e inconclusos usan **mismos campos obligatorios** que positivos.
  - **Rationale:** R11.2 requiere paridad de documentación.

### 007-source-evaluation.md

- [Decisión] Evaluación de fuentes contra **10 dimensiones** (authority, currency, independence, methodology, reproducibility, bias, conflict of interest, precision, applicability, traceability).
  - **Rationale:** R7.2 define las 10 dimensiones.
- [Decisión] Fuente con score **<6/10** requiere limitation note y weight máximo 50%.
  - **Rationale:** R7.3 define el umbral de calidad mínima.
- [Decisión] Si ninguna fuente alcanza ≥6, se documenta como **gap limitation** de la investigación.
  - **Rationale:** R7.4 requiere documentación de ausencia de fuentes de calidad.

### 008-research-workflow.md

- [Decisión] Workflow integra problem framing (R3), scope definition (R5), assumptions (R6) y results registration (R11) en un flujo operativo coherente.
  - **Rationale:** Múltiples requirements requieren un workflow unificado.
- [Decisión] Timebox expresado en horas (mín 1h, máx 40h) con deadline en formato YYYY-MM-DD.
  - **Rationale:** R5.2 define los rangos y formato.
- [Decisión] Al 80% del timebox sin conclusión: extender, reducir scope, o concluir con parciales.
  - **Rationale:** R5.3 define las opciones de escalación.

### 009-tooling-workflow.md

- [Decisión] Se asignan **roles exclusivos** a 6 herramientas: ChatGPT Projects, NotebookLM, Deepnote, Obsidian, GitHub, Kiro.
  - **Rationale:** R28.1 requiere responsabilidad definida por herramienta con input/output/boundary.
- [Decisión] Clasificación de permanencia: **temporal** (ChatGPT, NotebookLM), **semi-permanente** (Deepnote, Obsidian), **fuente de verdad** (GitHub).
  - **Rationale:** R28.2 requiere clasificación de outputs y reglas de preservación.
- [Decisión] **GitHub** es la fuente de verdad formal; discrepancias se resuelven a favor de GitHub.
  - **Rationale:** R28.3 requiere fuente de verdad definida.
- [Decisión] Protocolo de **handoff obligatorio** con 4 campos mínimos al transferir trabajo entre herramientas.
  - **Rationale:** R28.4 requiere protocolo de transferencia documentado.
- [Decisión] **5 restricciones de transferencia** (credenciales, PII, AI output sin verificación, datos sensibles, contexto completo de conversación).
  - **Rationale:** R28.5 define contenido que no puede transferirse.

### 010-deepnote-guidelines.md

- [Decisión] Deepnote se usa exclusivamente para **análisis de datos y experimentación cuantitativa** con notebooks reproducibles.
  - **Rationale:** R28.1 requiere rol definido por herramienta.

### 011-notebooklm-guidelines.md

- [Decisión] NotebookLM se usa exclusivamente para **consulta documental con referencias verificables** ancladas a documentos cargados.
  - **Rationale:** R28.1, R22 requieren rol definido y restricciones sobre contenido IA.

### 012-chatgpt-guidelines.md

- [Decisión] ChatGPT Projects se usa para **conversación contextual y generación exploratoria**; outputs son temporales y requieren verificación.
  - **Rationale:** R28.1, R22 requieren rol definido y restricciones sobre contenido IA.

### 013-obsidian-guidelines.md

- [Decisión] Obsidian se usa para **conocimiento permanente y relaciones conceptuales** mediante notas atómicas.
  - **Rationale:** R28.1 requiere rol definido por herramienta.

### 014-experiment-design.md

- [Decisión] Experimentos se clasifican como **research experiment** o **commercial validation experiment**.
  - **Rationale:** R10.2 requiere clasificación binaria de experimentos.
- [Decisión] Cuando variables no son aislables, se requiere **método alternativo** (observational study, comparative analysis, expert review, triangulation).
  - **Rationale:** R10.3 requiere alternativas cuando experimentación controlada no es viable.
- [Decisión] Experimento en estado terminal requiere **documented results** incluyendo negative results y unexpected findings.
  - **Rationale:** R10.4 requiere registro completo independiente del outcome.

### 015-research-journal.md

- [Decisión] Research_Journal es **obligatorio** para investigaciones que superan 4h de esfuerzo acumulado.
  - **Rationale:** R32.5 alinea con el umbral de investigación formal.
- [Decisión] Cada entrada requiere **8 campos**: date, stage, activity, findings, decisions, next steps, time invested, tools used.
  - **Rationale:** R32.1 define los campos obligatorios.

### 016-decision-log.md

- [Decisión] Cada decisión requiere **8 campos**: description, context, alternatives (≥2), rationale, evidence, consequences, reversibility, date.
  - **Rationale:** R32.3 define los campos obligatorios del Decision_Log.
- [Decisión] Reversibilidad clasificada como: easily reversible, reversible with effort, irreversible.
  - **Rationale:** R32.3 requiere assessment de reversibilidad.

### 017-conclusion-framework.md

- [Decisión] Toda conclusión traza a **≥1 evidencia** registrada en Source_Register o Evidence_Framework.
  - **Rationale:** R12.2 requiere trazabilidad obligatoria.
- [Decisión] Clasificación de conclusiones por soporte: **strong** (2+ fuentes confidence 4-5), **limited** (single source o confidence 1-3), **inference** (derivación lógica sin confirmación directa).
  - **Rationale:** R12.3 requiere distinción por nivel de soporte.
- [Decisión] Sección de **uncertainty obligatoria** con known unknowns, methodological limitations, evidence gaps.
  - **Rationale:** R13.1 requiere documentación explícita de incertidumbre.

### 018-research-to-asset.md

- [Decisión] Toda investigación completada debe producir **≥1 activo reutilizable** o documentar explícitamente por qué no es posible.
  - **Rationale:** R15 define el proceso de extracción de activos.
- [Decisión] Asset mínimo requiere **5 campos**: name, type, description, usage hypothesis, state.
  - **Rationale:** R15 define los campos mínimos de registro.

### 019-research-to-product-hypothesis.md

- [Decisión] Oportunidades comerciales se clasifican como **[Hipótesis]** hasta existir ≥1 señal de demanda externa verificable.
  - **Rationale:** R31.1 requiere epistemic label hasta señal de demanda.
- [Decisión] Se requieren **3 campos mínimos de monetización**: target segment, delivery format, revenue model.
  - **Rationale:** R31.1 define los campos obligatorios.
- [Decisión] Sin señal de demanda externa → **no se inicia desarrollo de producto**.
  - **Rationale:** R31.2 prohíbe desarrollo sin evidencia de demanda.
- [Decisión] Validation experiment con **deadline máximo de 30 días** y numeric success metric.
  - **Rationale:** R31.3 define las condiciones del Quality_Gate comercial.

### 020-quality-gates.md

- [Decisión] Se definen **7 quality gates** distribuidos en las etapas del lifecycle con checklists verificables.
  - **Rationale:** R29 requiere quality gates con criterios explícitos.
- [Decisión] Cada gate tiene **checklist de items pasa/no pasa** con remediación documentada si falla.
  - **Rationale:** R29 requiere que los gates sean operativos y remediables.

### 021-research-ethics-and-safety.md

- [Decisión] Se establecen reglas de **ética, privacidad, propiedad intelectual e IA responsable** aplicables a toda investigación.
  - **Rationale:** R20, R21, R22 cubren ética, privacidad e IA responsable.
- [Decisión] AI output requiere **verificación humana** antes de tratarse como conocimiento validado.
  - **Rationale:** R22 define restricciones sobre contenido generado por IA.

### 022-domain-specific-adaptations.md

- [Decisión] La metodología se adapta a **8+ dominios** del portafolio con ajustes específicos documentados por dominio.
  - **Rationale:** R23 requiere adaptaciones explícitas por dominio.
- [Decisión] Las adaptaciones no pueden contradecir los 12 principios — solo ajustar su aplicación operativa.
  - **Rationale:** Los principios son universales; las adaptaciones son de implementación.

### 023-research-metrics.md

- [Decisión] Se definen **métricas de salud**, cadence de revisión mensual y warning signals que disparan acción correctiva.
  - **Rationale:** R24 requiere métricas e indicadores de salud de la metodología.

### 024-anti-patterns.md

- [Decisión] Se documentan **7 anti-patrones generales** y **4 anti-patrones AI-específicos** con síntomas, consecuencias y correcciones.
  - **Rationale:** R30.2, R30.3 definen los anti-patrones obligatorios.
- [Decisión] Cada anti-patrón se mapea a **≥1 lifecycle stage** con checklist question de detección.
  - **Rationale:** R30.4 requiere detección integrada en el lifecycle.

---

## Declaración de consistencia

Tras la producción de los 26 documentos siguiendo el orden de dependencias definido en el diseño del package, se declara: [Hecho]

**No se detectan contradicciones internas entre los 26 documentos.** [Hecho]

Justificación:

1. **Terminología unificada.** Cada término de dominio tiene una definición canónica en el glosario del README. Los documentos referencian estos términos sin redefinición. [Hecho]
2. **Producción secuencial por dependencias.** Los documentos se produjeron respetando el DAG de dependencias del diseño — cada documento posterior respeta definiciones y decisiones de sus predecesores. [Hecho]
3. **Principios no contradictorios.** Los 12 principios de 001-research-principles.md son complementarios entre sí y no prescriben acciones mutuamente excluyentes para la misma condición. [Hecho]
4. **Evidence Framework coherente con Source Evaluation.** La escala de confianza de 006-evidence-framework.md es consistente con el umbral de calidad de 007-source-evaluation.md (fuente <6/10 → confidence máx 3). [Hecho]
5. **Lifecycle coherente con Quality Gates.** Las 16 etapas de 002-research-lifecycle.md se alinean con los 7 quality gates de 020-quality-gates.md sin conflicto de precedencia. [Hecho]
6. **Tooling roles no solapados.** Los roles exclusivos de 009-tooling-workflow.md son mutuamente exclusivos — ninguna tarea tiene dos herramientas primarias en conflicto. [Hecho]
7. **Monetización prudente consistente.** Las reglas de 019-research-to-product-hypothesis.md no fuerzan monetización (coherente con etapa 14 del lifecycle que permite concluir sin producto comercial). [Hecho]
8. **Anti-patrones alineados con principios.** Los 11 anti-patrones de 024-anti-patterns.md representan violaciones de los principios de 001-research-principles.md sin contradicción. [Hecho]

Si en una revisión posterior se identifican contradicciones, deberán documentarse aquí con referencia a los documentos y afirmaciones en conflicto, y resolverse mediante actualización del documento no-autoritativo.

---

## Exclusiones explícitas

El Package 001 — Research Methodology es **exclusivamente documental**. [Hecho] Las siguientes exclusiones son explícitas y definitivas:

| # | Exclusión | Descripción | Rationale |
|---|-----------|-------------|-----------|
| 1 | **Software implementation** | Este package no produce código ejecutable, scripts, aplicaciones ni componentes de software. | R36.1 — El package produce documentación metodológica, no implementaciones. |
| 2 | **API development** | Este package no define, implementa ni documenta interfaces de programación de aplicaciones. | R36.1 — Las APIs son producto de packages de implementación. |
| 3 | **Database creation** | Este package no crea bases de datos, esquemas, modelos de datos ejecutables ni infraestructura de almacenamiento. | R36.1 — La persistencia de datos es responsabilidad de packages técnicos. |
| 4 | **Technical infrastructure deployment** | Este package no despliega servidores, containers, pipelines CI/CD ni infraestructura cloud. | R36.1 — La infraestructura es responsabilidad de packages de operaciones. |
| 5 | **SaaS platform definition** | Este package no define ni diseña plataformas SaaS, servicios web ni productos de software como servicio. | R36.1 — Los productos SaaS requieren validación de mercado y packages de implementación dedicados. |
| 6 | **Functional integrations** | Este package no crea integraciones que intercambien datos entre herramientas externas en runtime. | R36.1 — Las integraciones funcionales son implementación técnica. |
| 7 | **Credential storage** | Este package no almacena, gestiona ni documenta credenciales, tokens o secretos. | R36.1 — La seguridad de credenciales requiere infraestructura dedicada. |
| 8 | **Commercial product creation** | Este package no produce productos comerciales directamente — provee la metodología para que otros packages los produzcan con rigor. | R36.1 — La creación de productos es responsabilidad de packages de producto. |

### Prohibiciones sobre estándares de evidencia (R36.2)

| # | Prohibición | Descripción |
|---|-------------|-------------|
| 1 | Tratar AI-generated responses como primary evidence | Todo output de IA requiere verificación contra fuentes primarias. |
| 2 | Afirmar validación sin criterios verificables explícitos | Toda validación debe tener criterios operativos medibles. |
| 3 | Requerir experimentación que exceda recursos disponibles o requiera autorización regulatoria | Se proporcionan métodos alternativos de validación. |
| 4 | Equiparar volumen de documentación con conocimiento validado | La calidad epistémica no se mide por cantidad. |
| 5 | Convertir automáticamente toda investigación en producto comercial | La monetización es una evaluación opcional, no una obligación. |

### Conformance check (R36.4)

Si cualquier documento del package contiene contenido que coincide con un item de la lista de exclusiones (R36.1) o de la lista de prohibiciones (R36.2), el package se considera **no conformante**. El contenido violador debe identificarse por nombre de documento y sección para su remediación.

**Estado actual:** Conforme — ningún documento del package contiene implementaciones de software, APIs, bases de datos, infraestructura, SaaS, integraciones funcionales, credenciales ni productos comerciales. [Hecho]

---

## Relación con otros packages

### Dependencias (packages de los que Package 001 depende)

| Package | Dependencia |
|---------|-------------|
| **Package 000 — Foundation** | Principios operativos (006-operating-principles.md), glosario fundacional, manifesto, modelo de empresa (Asset_First_Model) y reglas de negocio que Package 001 respeta y no contradice. |

### Consumers (packages que utilizan la metodología de Package 001)

| Package | Qué referencia de Package 001 |
|---------|-------------------------------|
| **002 — Knowledge Architecture** | Research_Lifecycle (16 etapas), Evidence_Framework (categorías y escala de confianza), Source_Register structure para organizar conocimiento con trazabilidad. |
| **003 — Asset System** | Proceso de asset extraction (018-research-to-asset.md), campos mínimos de asset, taxonomía de tipos de activos, quality gates de activos. |
| **004 — Product Factory** | Product_Hypothesis framework (019-research-to-product-hypothesis.md), Revenue_Hypothesis model, reglas de prudent monetization, Quality_Gate comercial. |
| **005 — Revenue Engine** | Revenue_Hypothesis model, validation experiment design (014-experiment-design.md), criterios de demanda externa verificable, reglas de no forzar monetización. |
| **006 — AI Workspace** | Tooling workflow (009-tooling-workflow.md), roles de herramientas IA, restricciones sobre AI-generated content, reglas de verificación humana. |
| **007 — Automation** | Research_Journal y Decision_Log structures (015, 016), templates reutilizables, protocolos de handoff entre herramientas. |
| **008 — Operating Model** | Quality gates (020-quality-gates.md), research metrics (023-research-metrics.md), compliance assessment model, domain adaptations. |
| **009 — Growth** | Market research type (003-research-types.md), hypothesis validation framework, experiment design para validación de demanda, anti-patterns de monetización prematura. |

---

## Trazabilidad a requirements

| Sección de este documento | Requirements cubiertos |
|---------------------------|------------------------|
| Decisiones metodológicas por documento | R34.4 (listar decisiones con origen y rationale) |
| Declaración de consistencia | R34.5 (declaración de no contradicción interna) |
| Exclusiones explícitas | R36.1 (8 exclusiones de alcance) |
| Prohibiciones sobre estándares de evidencia | R36.2 (5 prohibiciones sobre evidencia) |
| Relación con otros packages — Consumers | R36.3 (declarar consumers con referencia específica) |
| Conformance check | R36.4 (identificación de contenido violador) |

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho] | 14 | 100% |
| [Hipótesis] | 0 | 0% |
| [Visión] | 0 | 0% |
| [Decisión] | 0 | 0% |

Nota: Este documento reporta hechos sobre decisiones ya tomadas en otros documentos. Las decisiones listadas son factuales (se tomaron y están registradas); el acto de consolidarlas aquí es un registro factual, no una nueva decisión.
