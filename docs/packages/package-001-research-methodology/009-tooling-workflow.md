# 009 — Tooling Workflow

> **Etiqueta epistémica:** [Decisión]
>
> **Requirements cubiertos:** R28.1, R28.2, R28.3, R28.4, R28.5

## Propósito

Este documento define los **roles exclusivos** de cada herramienta en el ecosistema LabOS, el **protocolo de handoff** entre herramientas, la **clasificación de outputs**, las **restricciones de transferencia** y la **resolución de conflictos** cuando una tarea podría realizarse en más de una herramienta.

El objetivo es eliminar overlap funcional, mantener trazabilidad entre herramientas y garantizar que cada artefacto tiene un origen claro y un destino definido.

---

## Tabla de contenidos

1. [Roles exclusivos de herramientas](#roles-exclusivos-de-herramientas)
2. [Clasificación de permanencia](#clasificación-de-permanencia)
3. [Qué origina cada herramienta](#qué-origina-cada-herramienta)
4. [Qué exporta cada herramienta](#qué-exporta-cada-herramienta)
5. [Qué versiona cada herramienta](#qué-versiona-cada-herramienta)
6. [Clasificación de outputs](#clasificación-de-outputs)
7. [Protocolo de handoff](#protocolo-de-handoff)
8. [Restricciones de transferencia](#restricciones-de-transferencia)
9. [Diagrama de flujo de información](#diagrama-de-flujo-de-información)
10. [Resolución de conflictos entre herramientas](#resolución-de-conflictos-entre-herramientas)
11. [Mapeo de herramientas a lifecycle stages](#mapeo-de-herramientas-a-lifecycle-stages)

---

## Roles exclusivos de herramientas

Cada herramienta tiene un rol exclusivo. Ninguna otra herramienta debe asumir las funciones asignadas a otra.

| Herramienta | Rol exclusivo | Funciones principales |
|-------------|---------------|----------------------|
| **ChatGPT Projects** | Conversación contextual y generación exploratoria | Debate estructurado, draft generation, revisión crítica, planificación, challenge de ideas |
| **NotebookLM** | Consulta documental con referencias | Comparación de fuentes cargadas, resúmenes con citas verificables, respuestas ancladas a documentos subidos |
| **Deepnote** | Análisis de datos y experimentación cuantitativa | Notebooks reproducibles, visualizaciones, experimentación de datos, análisis estadístico |
| **Obsidian** | Conocimiento permanente y relaciones conceptuales | Notas atómicas, mapas conceptuales, índice personal de conocimiento, conexiones entre investigaciones |
| **GitHub** | Documentación versionada y trazabilidad formal | Código, datasets, templates, decision records, documentos formales versionados, fuente de verdad |
| **Kiro** | Spec-driven development | Requirements formales, design documents, task planning, implementación guiada por specs |

---

## Clasificación de permanencia

Las herramientas se clasifican según la permanencia de sus outputs:

| Clasificación | Herramientas | Regla operativa |
|---------------|-------------|-----------------|
| **Temporal** | ChatGPT Projects, NotebookLM | Outputs son efímeros. Todo lo relevante debe exportarse a GitHub u Obsidian antes de que se pierda contexto. No se garantiza persistencia. |
| **Semi-permanente** | Deepnote, Obsidian | Contenido persiste en la herramienta pero no constituye fuente de verdad formal hasta que se exporta a GitHub. |
| **Fuente de verdad** | GitHub | Documentación formal, decisiones, versiones finales, templates, código. Todo lo que existe en GitHub se considera el estado oficial del proyecto. |

### Implicaciones de la clasificación

- **Temporal:** No referenciar outputs temporales como evidencia verificada. Si una decisión se toma en ChatGPT, debe registrarse en GitHub para ser oficial.
- **Semi-permanente:** Se puede referenciar contenido en Deepnote/Obsidian para trabajo en progreso, pero conclusiones formales requieren exportación a GitHub.
- **Fuente de verdad:** GitHub es el punto de referencia para resolver cualquier discrepancia entre herramientas.

---

## Qué origina cada herramienta

| Herramienta | Origina (crea por primera vez) |
|-------------|-------------------------------|
| **ChatGPT Projects** | Borradores de documentos, análisis exploratorios, planes iniciales, debates estructurados, críticas de ideas, opciones con trade-offs |
| **NotebookLM** | Resúmenes documentales con citas, comparaciones estructuradas de fuentes, respuestas contextuales ancladas a documentos cargados |
| **Deepnote** | Análisis cuantitativos, visualizaciones de datos, resultados de experimentos computacionales, modelos estadísticos |
| **Obsidian** | Notas atómicas de conocimiento, mapas conceptuales, conexiones inter-investigación, índices temáticos personales |
| **GitHub** | Documentos formales finales, versiones oficiales, código funcional, datasets estructurados, templates reutilizables, decision records |
| **Kiro** | Specs formales (requirements, design, tasks), plans de implementación, definiciones de features |

---

## Qué exporta cada herramienta

| Herramienta | Se exporta a | Qué se exporta |
|-------------|-------------|----------------|
| **ChatGPT Projects** | GitHub | Decisiones refinadas, conclusiones validadas, planes finalizados |
| **ChatGPT Projects** | Obsidian | Insights parciales, ideas para explorar, conexiones identificadas |
| **NotebookLM** | GitHub | Citas verificadas contra fuentes, comparaciones con referencias claras |
| **NotebookLM** | Obsidian | Insights de lectura, conexiones entre fuentes |
| **Deepnote** | GitHub | Notebooks finales limpios, resultados de experimentos, visualizaciones exportadas |
| **Obsidian** | GitHub | Notas que maduran a documentos formales (cuando cumplen criteria de completitud) |
| **GitHub** | — | Es el destino final; no exporta a otras herramientas |
| **Kiro** | GitHub | Specs formales (se almacenan dentro de `.kiro/` en el repositorio) |

---

## Qué versiona cada herramienta

| Herramienta | Se versiona en | Mecanismo |
|-------------|----------------|-----------|
| **ChatGPT Projects** | No se versiona | Contenido temporal; historial de conversación no constituye versionado formal |
| **NotebookLM** | No se versiona | Contenido temporal; depende de documentos subidos que pueden cambiar |
| **Deepnote** | GitHub | Notebooks exportados como archivos de código; versionado via git |
| **Obsidian** | Obsidian (git interno) | Versionado local via git del vault; no es fuente de verdad formal |
| **GitHub** | GitHub (git nativo) | Commits, branches, tags; versionado formal del proyecto |
| **Kiro** | GitHub (dentro de `.kiro/`) | Specs versionadas como parte del repositorio |

---

## Clasificación de outputs

Todo output producido por una herramienta debe clasificarse en una de tres categorías:

| Clasificación | Definición | Tratamiento | Herramientas típicas |
|---------------|-----------|-------------|---------------------|
| **Analytical aid** | Herramienta utilizada para procesamiento o exploración; el output no se almacena como registro permanente | Se usa y descarta. No se cita como fuente. No requiere registro formal. | ChatGPT (debates), NotebookLM (consultas rápidas) |
| **Repository content** | Registro permanente committed a GitHub como artefacto oficial del proyecto | Se versiona, se puede citar, es fuente de verdad. Requiere review antes de commit. | GitHub (documentos), Deepnote (notebooks finales), Obsidian (notas maduras exportadas) |
| **Generated content** | Contenido producido por IA que requiere verificación humana antes de promoción | Se marca con herramienta de origen y fecha. No puede usarse como Primary_Evidence. Requiere human review para promoción a repository content. | ChatGPT (borradores), NotebookLM (resúmenes), Kiro (código generado) |

### Reglas de promoción

1. **Generated content → Repository content:** Requiere verificación humana explícita, marcado de verificación (`verified_by: "human"`), y commit a GitHub.
2. **Analytical aid → Repository content:** No aplica directamente. Si un analytical aid produce un insight valioso, debe recrearse como documento nuevo en la herramienta apropiada.
3. **Generated content → Analytical aid:** El contenido se usa para informar trabajo pero no se registra. No requiere verificación formal.

---

## Protocolo de handoff

Cuando trabajo transita de una herramienta a otra, se debe documentar un **handoff record** con los siguientes campos mínimos:

### Campos obligatorios del handoff

| Campo | Descripción | Ejemplo |
|-------|------------|---------|
| **Resumen de trabajo completado** | Descripción concisa de qué se realizó en la herramienta de origen (2-5 oraciones) | "Se debatieron 3 opciones de arquitectura para el pipeline de datos. Se evaluaron trade-offs de costo, complejidad y mantenibilidad." |
| **Referencias de fuentes** | Lista de fuentes consultadas o documentos utilizados durante el trabajo | "Documentación de Apache Kafka, paper de Martin Kleppmann (2017), benchmark interno INV-003" |
| **Decisiones con rationale** | Cada decisión tomada durante el trabajo, con su justificación | "Se eligió event sourcing porque permite replay de eventos (rationale: auditabilidad requerida por compliance)" |
| **Versión o commit link** | Identificador que ancla el handoff a un estado específico del proyecto | "Commit `a3f2b1c` en branch `feature/pipeline-design`" o "Obsidian note: `2024-01-15-pipeline-options.md`" |

### Campos opcionales del handoff

| Campo | Descripción |
|-------|------------|
| **Preguntas abiertas** | Dudas no resueltas que la herramienta destino debe abordar |
| **Siguiente acción esperada** | Qué se espera que se realice en la herramienta destino |
| **Clasificación del output** | Si el output es analytical aid, repository content, o generated content |

### Dónde se registra el handoff

- Si el destino es **GitHub**: el handoff se documenta en el commit message o en el documento destino (sección "Origen").
- Si el destino es **Obsidian**: el handoff se documenta como metadata al inicio de la nota.
- Si el destino es **Deepnote**: el handoff se documenta en la primera celda del notebook.

---

## Restricciones de transferencia

Los siguientes tipos de contenido **NO deben copiarse** entre herramientas bajo ninguna circunstancia:

| Contenido prohibido | Razón | Acción correcta |
|--------------------|-------|-----------------|
| **Credenciales, tokens o API keys** | Riesgo de exposición en herramientas sin control de acceso adecuado | Usar variables de entorno o gestores de secretos; nunca registrar en documentos |
| **Datos personales identificables (PII) sin anonimización** | Violación de privacidad; riesgo legal | Anonimizar antes de mover a cualquier herramienta compartida o versionada |
| **AI output sin verificación como evidencia** | Presentar contenido generado como evidencia verificada degrada la integridad del sistema | Verificar contra fuentes originales antes de promover; marcar siempre como `generated content` |
| **Notebooks con datos sensibles** | Riesgo de exposición en repositorios públicos o compartidos | Sanitizar datos antes de exportar; usar datasets de ejemplo para documentación |
| **Contexto completo de conversación** | Ruido, irrelevancia, potencial PII o información confidencial embebida | Exportar solo decisiones, conclusiones y rationale; descartar el flujo conversacional |

### Regla general

> En caso de duda sobre si un contenido debe transferirse: **no transferir**. Consultar las restricciones y, si persiste la duda, registrar la pregunta en el Decision Log para revisión del Fundador.

---

## Diagrama de flujo de información

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                        FLUJO DE INFORMACIÓN ENTRE HERRAMIENTAS              │
└─────────────────────────────────────────────────────────────────────────────┘

[Trigger: pregunta, problema, idea, incidente, oportunidad]
       │
       ▼
┌──────────────────────┐
│  ChatGPT Projects    │──── debate, exploración, borrador ────────┐
│  (TEMPORAL)          │                                           │
└──────────┬───────────┘                                           │
           │ insights parciales                                    │
           ▼                                                       │
┌──────────────────────┐                                           │
│  NotebookLM          │──── consulta documental, comparación ────┤
│  (TEMPORAL)          │                                           │
└──────────┬───────────┘                                           │
           │ citas verificadas                                     │
           ▼                                                       │
┌──────────────────────┐                                           │
│  Deepnote            │──── análisis cuantitativo, experimentos ──┤
│  (SEMI-PERMANENTE)   │                                           │
└──────────┬───────────┘                                           │
           │ resultados validados                                  │
           ▼                                                       ▼
┌──────────────────────┐                              ┌────────────────────┐
│  Obsidian            │◄──── insights, notas ────────│    [Síntesis]      │
│  (SEMI-PERMANENTE)   │      atómicas                │  Integración de    │
└──────────┬───────────┘                              │  outputs parciales │
           │ documentos maduros                       └────────────────────┘
           ▼
┌──────────────────────┐
│  GitHub              │◄──── documento formal, versión final, activo
│  (FUENTE DE VERDAD)  │
└──────────┬───────────┘
           │ spec requerida para implementación
           ▼
┌──────────────────────┐
│  Kiro                │──── spec-driven development
│  (FUENTE DE VERDAD)  │      requirements → design → tasks → implementación
└──────────────────────┘
```

### Direccionalidad

- El flujo principal es **de izquierda a derecha y de arriba hacia abajo**: desde herramientas temporales hacia fuentes de verdad.
- **No hay flujo inverso** de GitHub hacia herramientas temporales (no se "desversiona" para re-debatir).
- Obsidian puede alimentar a ChatGPT/NotebookLM como **contexto de lectura**, pero nunca como destino de outputs formales de esas herramientas.

---

## Resolución de conflictos entre herramientas

Cuando una tarea podría realizarse en más de una herramienta, se aplica el siguiente protocolo:

### Principio general

> Se designa **una herramienta primaria** por tarea. La selección se documenta con rationale en la especificación de etapa correspondiente.

### Matriz de resolución de conflictos comunes

| Tarea | Herramientas candidatas | Herramienta primaria | Rationale |
|-------|------------------------|---------------------|-----------|
| Generar borrador de documento | ChatGPT Projects, Kiro | **ChatGPT Projects** | Los borradores requieren exploración libre y debate; Kiro es para specs formales, no exploración |
| Comparar fuentes documentales | ChatGPT Projects, NotebookLM | **NotebookLM** | NotebookLM ancla respuestas a documentos subidos con citas verificables; ChatGPT carece de citación precisa |
| Analizar dataset cuantitativo | Deepnote, ChatGPT Projects | **Deepnote** | Reproducibilidad y visualización requieren ambiente de ejecución; ChatGPT no ejecuta código de forma persistente |
| Registrar decisión formal | GitHub, Obsidian | **GitHub** | Las decisiones formales requieren versionado y trazabilidad oficial; Obsidian es para conocimiento personal |
| Crear nota de conocimiento personal | Obsidian, GitHub | **Obsidian** | Las notas atómicas y conexiones son el rol exclusivo de Obsidian; GitHub es para documentos finales |
| Definir requirements de feature | Kiro, ChatGPT Projects | **Kiro** | Los requirements formales se gestionan con spec-driven development; ChatGPT puede asistir en exploración previa |
| Resumir un paper o artículo | NotebookLM, ChatGPT Projects | **NotebookLM** | El resumen con citas ancladas es el rol exclusivo de NotebookLM; ChatGPT no garantiza fidelidad a la fuente |
| Explorar idea sin estructura | ChatGPT Projects, Obsidian | **ChatGPT Projects** | La exploración libre con debate es temporal por naturaleza; Obsidian registra insights ya procesados |

### Protocolo de resolución para casos no listados

1. **Identificar** qué herramientas podrían realizar la tarea según sus roles exclusivos.
2. **Evaluar** cuál herramienta tiene el rol más cercano a la naturaleza de la tarea.
3. **Priorizar** según clasificación de permanencia: si la tarea produce un artefacto formal, priorizar herramientas de mayor permanencia.
4. **Documentar** la decisión con rationale en el documento de etapa o en el Decision Log si el conflicto es recurrente.
5. **Registrar** el nuevo caso en esta sección para referencia futura si se convierte en patrón.

---

## Mapeo de herramientas a lifecycle stages

Referencia: las 16 etapas están definidas en [002-research-lifecycle.md](./002-research-lifecycle.md).

| Etapa del lifecycle | Herramienta primaria | Herramientas de apoyo | Rol en la etapa |
|--------------------|---------------------|----------------------|-----------------|
| 1. Intake | ChatGPT Projects | GitHub, Obsidian | Contextualizar trigger, explorar alcance inicial |
| 2. Problem Framing | ChatGPT Projects | NotebookLM | Debatir perspectivas, desafiar supuestos iniciales |
| 3. Research Question | ChatGPT Projects | NotebookLM | Formular y refinar preguntas, validar especificidad |
| 4. Scope | ChatGPT Projects | GitHub | Definir boundaries, documentar exclusiones |
| 5. Assumptions | ChatGPT Projects | — | Identificar y registrar supuestos |
| 6. Source Collection | NotebookLM | ChatGPT Projects, Deepnote | Consultar fuentes, comparar, evaluar calidad |
| 7. Evidence Evaluation | NotebookLM | Deepnote | Verificar claims contra fuentes, scoring |
| 8. Analysis | Deepnote | ChatGPT Projects | Análisis cuantitativo, patrones, correlaciones |
| 9. Experimentation | Deepnote | GitHub | Ejecutar experimentos, registrar resultados |
| 10. Findings | ChatGPT Projects | Deepnote, NotebookLM | Sintetizar hallazgos, identificar patrones |
| 11. Conclusion | ChatGPT Projects | GitHub | Formular conclusiones, validar contra evidencia |
| 12. Review | GitHub | ChatGPT Projects | Evaluar completitud y calidad del registro formal |
| 13. Asset Extraction | GitHub | Obsidian | Formalizar activos, documentar metadata |
| 14. Product Hypothesis | ChatGPT Projects | GitHub | Formular hipótesis de producto/monetización |
| 15. Publication/Archive | GitHub | — | Publicar o archivar formalmente |
| 16. Feedback & Iteration | ChatGPT Projects | GitHub | Integrar feedback, planificar iteración |

### Herramientas transversales

Las siguientes herramientas tienen presencia en **todas** las etapas como soporte:

- **Obsidian:** Captura continua de notas atómicas y conexiones durante cualquier etapa.
- **GitHub:** Registro formal disponible en cualquier momento que se produzca un artefacto committeable.
- **Kiro:** Se activa cuando una etapa requiere implementación de software (spec-driven development).

---

## Referencias

- [002-research-lifecycle.md](./002-research-lifecycle.md) — Definición de las 16 etapas del lifecycle
- [README.md](./README.md) — Índice del package y glosario
