# 012 — ChatGPT Projects Guidelines

> **Etiqueta epistémica:** [Decisión]
>
> **Requirements cubiertos:** R28.1, R28.2, R22.1, R22.2, R22.3, R22.4, R22.5, R22.6

## Propósito

Este documento define el **rol, restricciones, reglas de uso responsable y protocolo de exportación** de ChatGPT Projects dentro del ecosistema de herramientas de investigación de LabOS.

ChatGPT Projects es una **herramienta de análisis** clasificada como **temporal**. Sus outputs son efímeros por naturaleza y no constituyen evidencia verificada, conocimiento permanente ni fuente de verdad. Todo output relevante debe exportarse antes de que se pierda contexto.

---

## Tabla de contenidos

1. [Rol exclusivo](#rol-exclusivo)
2. [Clasificación y permanencia](#clasificación-y-permanencia)
3. [Funciones permitidas](#funciones-permitidas)
4. [Reglas de IA responsable](#reglas-de-ia-responsable)
5. [Restricciones de uso](#restricciones-de-uso)
6. [Protocolo de exportación](#protocolo-de-exportación)
7. [Handoff desde ChatGPT Projects](#handoff-desde-chatgpt-projects)
8. [Mapeo a etapas del lifecycle](#mapeo-a-etapas-del-lifecycle)
9. [Anti-patrones específicos](#anti-patrones-específicos)

---

## Rol exclusivo

ChatGPT Projects tiene un rol exclusivo dentro de LabOS:

| Campo | Valor |
|-------|-------|
| **Rol** | Conversación contextual y generación exploratoria |
| **Clasificación** | Herramienta de análisis |
| **Permanencia** | Temporal |
| **Funciones principales** | Debate estructurado, generación de borradores, revisión crítica, planificación, challenge de ideas |

### Qué es ChatGPT Projects dentro de LabOS

ChatGPT Projects es el espacio donde se **explora, debate, estructura y genera borradores** antes de que las ideas maduren a documentos formales. Es una herramienta de pensamiento asistido, no una fuente de conocimiento.

### Qué NO es ChatGPT Projects

- **No es una fuente de evidencia.** Sus respuestas no constituyen Primary_Evidence bajo ninguna circunstancia.
- **No es un repositorio.** No se debe confiar en la persistencia de su contenido.
- **No es un sustituto de verificación humana.** Todo output sustantivo requiere validación independiente.
- **No es un oráculo de hechos.** Las afirmaciones factuales de ChatGPT requieren verificación contra fuentes primarias.

---

## Clasificación y permanencia

### Clasificación como herramienta temporal

| Aspecto | Regla |
|---------|-------|
| **Permanencia de outputs** | Efímera. El historial de conversación no constituye versionado formal ni registro permanente. |
| **Referencialidad** | No se debe referenciar una conversación de ChatGPT como fuente verificable en documentos formales. |
| **Garantía de persistencia** | Ninguna. El contexto puede perderse por límites de la herramienta, cierre de proyecto o actualización del modelo. |
| **Implicación operativa** | Toda decisión, conclusión o insight valioso debe exportarse a GitHub u Obsidian en la misma sesión de trabajo. |

### Regla de temporalidad

> Si un output de ChatGPT Projects no se exporta durante la sesión de trabajo en que se genera, se considera **perdido por defecto**. No se debe asumir que estará disponible en sesiones futuras.

---

## Funciones permitidas

ChatGPT Projects se utiliza exclusivamente para las siguientes funciones dentro del proceso investigativo:

### 1. Contexto y contextualización

- Explorar el espacio de un problema antes de formalizarlo.
- Articular triggers de investigación.
- Generar contexto inicial para un Research_Brief.

### 2. Debate estructurado

- Presentar opciones con trade-offs para decisiones.
- Confrontar ideas con argumentos opuestos (challenge de ideas).
- Explorar perspectivas alternativas sobre un problema.
- Debatir supuestos antes de documentarlos como assumptions.

### 3. Generación de borradores

- Producir drafts iniciales de documentos metodológicos.
- Generar estructuras y outlines para documentos formales.
- Redactar versiones preliminares de conclusiones para refinamiento.

### 4. Revisión y crítica

- Revisar documentos en borrador identificando gaps o inconsistencias.
- Evaluar calidad de research questions contra criterios definidos.
- Identificar debilidades en argumentación o evidencia.

### 5. Planificación

- Estimar esfuerzo para investigaciones.
- Estructurar planes de trabajo con etapas y dependencias.
- Identificar recursos necesarios para una investigación.

### 6. Challenge de ideas

- Cuestionar premisas explícitas e implícitas.
- Identificar anti-patrones en el razonamiento.
- Proponer contraejemplos a hipótesis formuladas.
- Señalar sesgos potenciales en el enfoque.

---

## Reglas de IA responsable

### Clasificación obligatoria: AI_Generated_Content

Todo output sustantivo de ChatGPT Projects se clasifica automáticamente como **AI_Generated_Content**. [Decisión]

| Criterio | Regla |
|----------|-------|
| **¿Qué se clasifica como AI_Generated_Content?** | Resúmenes, explicaciones, afirmaciones factuales, análisis, síntesis, borradores, opciones con argumentos — cualquier contenido sustantivo generado por la herramienta. |
| **¿Qué NO requiere clasificación?** | Correcciones menores de ortografía o gramática (spell-check, grammar correction). |
| **Nivel de confianza máximo sin verificación** | 3 (Medium). El contenido de ChatGPT no puede exceder confidence level 3 sin verificación humana contra fuentes primarias. |

### Regla R22.1 — Clasificación

> Cuando ChatGPT genera contenido sustantivo durante investigación (incluyendo resúmenes, afirmaciones factuales, explicaciones o análisis), ese output se clasifica como **AI_Generated_Content**, nunca como **Primary_Evidence**.

### Regla R22.2 — Verificación obligatoria

> Cuando contenido generado por ChatGPT se usa para soportar una conclusión de investigación, el investigador **debe independientemente localizar la fuente primaria citada y confirmar que la afirmación específica existe en esa fuente** antes de que el contenido pueda soportar la conclusión.

**Proceso de verificación:**

1. Identificar la afirmación factual generada por ChatGPT.
2. Localizar la fuente primaria (documento, paper, documentación oficial) de forma independiente — NO a través del mismo ChatGPT.
3. Confirmar que la afirmación existe tal como se reporta en la fuente primaria.
4. Registrar el resultado de verificación: `verified`, `unverified`, o `source-not-found`.

### Regla R22.3 — Etiquetado

> Todo contenido de ChatGPT incorporado a findings de investigación debe etiquetarse con:

| Campo | Descripción | Ejemplo |
|-------|-------------|---------|
| **Herramienta** | Nombre de la herramienta que generó el contenido | ChatGPT Projects |
| **Fecha de generación** | Fecha en que se generó el output | 2025-01-15 |
| **Intención de la consulta** | Descripción del query intent (≤200 caracteres) | "Comparar approaches de event sourcing vs CQRS para pipelines de datos con alta volumetría" |
| **Estado de verificación** | Una de tres opciones | `verified` / `unverified` / `source-not-found` |

### Regla R22.4 — Prohibición de citación sin verificación

> Si ChatGPT proporciona una afirmación factual y la fuente primaria subyacente **no ha sido independientemente localizada y verificada** por el investigador (sin usar la misma herramienta de IA para la verificación), se **prohíbe** citar esa afirmación como evidencia en cualquier conclusión de investigación.

### Regla R22.5 — Techo de confianza

> El contenido generado por ChatGPT no puede exceder **confidence level 3** sin verificación humana.

| Situación | Confidence máximo permitido |
|-----------|----------------------------|
| Output de ChatGPT sin verificación | ≤ 3 (Medium) |
| Output de ChatGPT verificado contra 1 fuente primaria | ≤ 4 (High) |
| Output de ChatGPT verificado contra 2+ fuentes independientes | ≤ 5 (Very High) |

### Regla R22.6 — Prohibición de presentar como investigación original

> Se **prohíbe** presentar output de ChatGPT como investigación original. Si ChatGPT contribuye a conclusiones, se debe declarar explícitamente la contribución de la herramienta de IA en la sección correspondiente del documento.

**Formulación correcta:** "Se utilizó ChatGPT Projects como herramienta de análisis para explorar opciones de [X]. Las conclusiones fueron verificadas contra [fuentes primarias citadas]."

**Formulación prohibida:** "Tras analizar [X], se concluye que..." (sin revelar que el análisis fue realizado por IA).

---

## Restricciones de uso

### Contenido que NO debe generarse en ChatGPT

| Contenido | Razón | Alternativa |
|-----------|-------|-------------|
| Decisiones formales finales | Las decisiones requieren registro versionado | Documentar en GitHub como Decision Record |
| Evidencia primaria | ChatGPT no produce evidencia verificable | Consultar fuentes primarias directamente |
| Datos sensibles o PII | Sin control de acceso adecuado | Usar herramientas con acceso controlado |
| Código de producción | Requiere testing, review y versionado | Usar Kiro para spec-driven development |
| Análisis cuantitativo reproducible | Requiere ambiente de ejecución persistente | Usar Deepnote |
| Consulta documental con citas | ChatGPT no garantiza fidelidad a fuentes | Usar NotebookLM |

### Contenido que NO debe copiarse desde ChatGPT sin transformación

- **Respuestas literales completas** → Extraer solo decisiones y rationale.
- **Contexto de conversación completo** → Exportar solo conclusiones y justificaciones.
- **Afirmaciones factuales** → Verificar contra fuentes primarias antes de incorporar.
- **Datos numéricos o estadísticos** → Confirmar contra fuente original.

### Límite de delegación

ChatGPT Projects es una **herramienta de asistencia**, no un sustituto del juicio del investigador. Las siguientes actividades requieren juicio humano y no pueden delegarse:

- Evaluación final de evidencia.
- Decisiones sobre qué conclusiones soporta la evidencia.
- Clasificación de confidence levels de conclusiones finales.
- Aprobación de quality gates.
- Review formal de investigaciones.

---

## Protocolo de exportación

### Qué se exporta desde ChatGPT Projects

| Destino | Qué se exporta | Cuándo |
|---------|----------------|--------|
| **GitHub** | Decisiones refinadas con rationale, conclusiones validadas, planes finalizados | Cuando un output madura de borrador a documento formal |
| **Obsidian** | Insights parciales, ideas para explorar, conexiones identificadas entre conceptos | Cuando se identifica un insight relevante que no es aún un documento formal |

### Qué NO se exporta

- El historial completo de conversación.
- Debates intermedios que no produjeron una decisión.
- Borradores descartados sin valor residual.
- Contexto de prueba o experimentación con la herramienta.

### Regla de exportación inmediata

> Todo output de ChatGPT que contenga una **decisión**, **conclusión** o **plan** que se pretenda usar en la investigación debe exportarse a GitHub u Obsidian **durante la misma sesión de trabajo**. No se permite postergar la exportación a sesiones futuras.

### Formato de exportación a GitHub

Cuando se exporta contenido de ChatGPT a GitHub, el documento destino debe incluir:

```markdown
## Origen

- **Herramienta:** ChatGPT Projects
- **Fecha:** YYYY-MM-DD
- **Intención:** [descripción del query intent, ≤200 caracteres]
- **Clasificación:** AI_Generated_Content
- **Verificación:** [verified | unverified | source-not-found]
- **Fuentes primarias consultadas:** [lista de fuentes contra las que se verificó]
```

---

## Handoff desde ChatGPT Projects

Cuando trabajo transita de ChatGPT Projects a otra herramienta, se registra un handoff con los siguientes campos:

| Campo | Obligatorio | Descripción |
|-------|-------------|-------------|
| **Resumen de trabajo completado** | Sí | 2-5 oraciones describiendo qué se realizó en ChatGPT |
| **Referencias de fuentes** | Sí | Fuentes mencionadas durante la conversación (para verificación posterior) |
| **Decisiones con rationale** | Sí | Cada decisión tomada con su justificación |
| **Versión o commit link** | Sí | Identificador que ancla el handoff al estado del proyecto |
| **Preguntas abiertas** | No | Dudas no resueltas para la herramienta destino |
| **Siguiente acción esperada** | No | Qué se espera que se realice en la herramienta destino |
| **Clasificación del output** | No | analytical aid, repository content, o generated content |

### Clasificación de outputs de ChatGPT

| Clasificación | Cuándo aplica | Tratamiento |
|---------------|---------------|-------------|
| **Analytical aid** | Debate exploratorio, brainstorming, challenge — output no se almacena | Se usa y descarta. No requiere registro formal. |
| **Generated content** | Borradores, planes, análisis — output que podría incorporarse a documentos | Se marca con herramienta de origen y fecha. Requiere human review para promoción. |
| **Repository content** | Nunca directamente desde ChatGPT | ChatGPT no produce repository content. Todo debe pasar por verificación y commit a GitHub. |

---

## Mapeo a etapas del lifecycle

ChatGPT Projects es **herramienta primaria** en las siguientes etapas:

| Etapa | Rol de ChatGPT | Tipo de output esperado |
|-------|----------------|------------------------|
| 1. Intake | Contextualizar trigger, explorar alcance inicial | Analytical aid |
| 2. Problem Framing | Debatir perspectivas, desafiar supuestos | Analytical aid / Generated content |
| 3. Research Question | Formular y refinar preguntas, evaluar calidad | Generated content |
| 4. Scope | Definir boundaries, estimar esfuerzo | Generated content |
| 5. Assumptions | Identificar y registrar supuestos, challenge | Analytical aid |
| 10. Findings | Sintetizar hallazgos, identificar patrones | Generated content |
| 11. Conclusion | Formular conclusiones, validar contra evidencia | Generated content |
| 14. Product Hypothesis | Formular hipótesis de producto/monetización | Generated content |
| 16. Feedback & Iteration | Integrar feedback, planificar siguiente ciclo | Analytical aid |

### Herramienta de apoyo en:

| Etapa | Rol de apoyo |
|-------|--------------|
| 6. Source Collection | Búsqueda contextual (NO como fuente verificada) |
| 12. Review | Revisión de completitud (NO sustituye human review) |

---

## Anti-patrones específicos

Los siguientes anti-patrones son particularmente relevantes al usar ChatGPT Projects:

### 1. Tratamiento como fuente de evidencia

| Campo | Valor |
|-------|-------|
| **Síntoma** | Citar una respuesta de ChatGPT como evidencia en un documento formal sin verificación contra fuente primaria |
| **Consecuencia** | Degradación de la integridad del sistema de evidencia; conclusiones potencialmente falsas |
| **Corrección** | Verificar toda afirmación factual contra fuente primaria independiente; marcar como `unverified` hasta completar verificación |

### 2. Delegación de juicio

| Campo | Valor |
|-------|-------|
| **Síntoma** | Aceptar la evaluación de ChatGPT sobre calidad de evidencia, confidence levels o validez de conclusiones sin revisión humana |
| **Consecuencia** | Juicio humano ausente en decisiones críticas; quality gates sin rigor |
| **Corrección** | Usar ChatGPT como input para la evaluación, no como evaluador final; mantener human review obligatorio |

### 3. Confianza en persistencia

| Campo | Valor |
|-------|-------|
| **Síntoma** | Asumir que un insight o decisión "está en ChatGPT" y no exportarlo a GitHub/Obsidian |
| **Consecuencia** | Pérdida de conocimiento cuando el contexto se pierde o la conversación expira |
| **Corrección** | Exportar decisiones y conclusiones en la misma sesión; tratar ChatGPT como memoria volátil |

### 4. Consenso artificial entre herramientas de IA

| Campo | Valor |
|-------|-------|
| **Síntoma** | Usar el acuerdo entre ChatGPT y NotebookLM (u otra IA) como "confirmación independiente" de una afirmación |
| **Consecuencia** | Falsa sensación de corroboración; las herramientas de IA pueden compartir sesgos de entrenamiento |
| **Corrección** | Solo fuentes primarias independientes constituyen confirmación. El acuerdo entre IAs no incrementa confidence level. |

### 5. Exportación de contexto completo

| Campo | Valor |
|-------|-------|
| **Síntoma** | Copiar la conversación completa de ChatGPT a un documento en GitHub |
| **Consecuencia** | Ruido, información no curada, potencial PII embebida, documentos inmanejables |
| **Corrección** | Extraer solo decisiones, conclusiones y rationale. Descartar el flujo conversacional. |

---

## Referencias

- [009-tooling-workflow.md](./009-tooling-workflow.md) — Roles exclusivos, handoffs y clasificación de permanencia
- [006-evidence-framework.md](./006-evidence-framework.md) — Evidence Framework con categorías y confidence levels
- [002-research-lifecycle.md](./002-research-lifecycle.md) — 16 etapas del lifecycle
- [README.md](./README.md) — Índice del package y glosario
