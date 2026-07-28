# 011 — NotebookLM Guidelines

> **Etiqueta epistémica:** [Decisión]
>
> **Requirements cubiertos:** R28.1, R28.2, R22.1, R22.2, R22.3

## Propósito

Este documento define el **rol exclusivo** de NotebookLM dentro del ecosistema de herramientas LabOS, las **reglas de uso responsable de IA**, las **restricciones sobre sus outputs**, la **integración con el lifecycle** de investigación y los **protocolos de exportación**.

NotebookLM es una herramienta de análisis clasificada como **temporal**. Sus outputs no constituyen fuente de verdad y deben exportarse a GitHub u Obsidian antes de que se pierda contexto.

---

## Tabla de contenidos

1. [Rol exclusivo](#rol-exclusivo)
2. [Clasificación de la herramienta](#clasificación-de-la-herramienta)
3. [Funciones permitidas](#funciones-permitidas)
4. [Funciones prohibidas](#funciones-prohibidas)
5. [Reglas de IA responsable](#reglas-de-ia-responsable)
6. [Clasificación de outputs](#clasificación-de-outputs)
7. [Integración con lifecycle stages](#integración-con-lifecycle-stages)
8. [Protocolo de exportación](#protocolo-de-exportación)
9. [Reglas de verificación](#reglas-de-verificación)
10. [Buenas prácticas](#buenas-prácticas)
11. [Anti-patrones específicos](#anti-patrones-específicos)

---

## Rol exclusivo

NotebookLM tiene un rol exclusivo y delimitado dentro del ecosistema LabOS:

| Campo | Valor |
|-------|-------|
| **Herramienta** | NotebookLM (Google) |
| **Rol exclusivo** | Consulta documental con referencias |
| **Clasificación** | Herramienta de análisis |
| **Permanencia** | Temporal |

### Funciones principales

- **Consulta documental:** Formular preguntas sobre documentos cargados y obtener respuestas ancladas a las fuentes.
- **Comparación de fuentes:** Contrastar información entre múltiples documentos cargados, identificando coincidencias y divergencias.
- **Resúmenes con referencias:** Generar síntesis de documentos con citas verificables que apuntan a secciones específicas de las fuentes originales.

### Diferenciación con otras herramientas

| Tarea | NotebookLM | ChatGPT Projects |
|-------|-----------|-----------------|
| Comparar fuentes documentales | ✅ Herramienta primaria — ancla respuestas a documentos con citas | ❌ No garantiza fidelidad a la fuente |
| Resumir papers o artículos | ✅ Herramienta primaria — resumen con citas | ❌ Puede alucinar o parafrasear sin respaldo |
| Debate libre y exploración | ❌ Limitado a documentos cargados | ✅ Herramienta primaria |
| Generar borradores | ❌ No es su función | ✅ Herramienta primaria |

---

## Clasificación de la herramienta

### Temporal — No fuente de verdad

NotebookLM está clasificada como **temporal**. Esto implica:

1. **No se versiona:** Los notebooks y sus outputs no constituyen versionado formal.
2. **No se referencia como evidencia:** Los outputs de NotebookLM no pueden citarse como fuente verificada en documentos formales sin verificación independiente.
3. **Exportación obligatoria:** Todo insight relevante debe exportarse a GitHub (citas verificadas) u Obsidian (conexiones e insights) antes de que se pierda contexto.
4. **Dependencia de documentos cargados:** La calidad del output depende de los documentos subidos, que pueden cambiar o eliminarse sin trazabilidad.

### Regla operativa

> Los outputs de NotebookLM son efímeros. Si una decisión, hallazgo o comparación no se exporta a GitHub u Obsidian, se considera no registrado y no puede referenciarse en documentos formales del proyecto.

---

## Funciones permitidas

| Función | Descripción | Output esperado |
|---------|-------------|-----------------|
| **Consulta documental** | Preguntar sobre contenido de documentos cargados | Respuesta con citas que apuntan a pasajes específicos |
| **Comparación de fuentes** | Solicitar comparaciones entre 2+ documentos cargados | Tabla o listado de coincidencias, divergencias y gaps |
| **Resumen con citas** | Solicitar síntesis de uno o más documentos | Resumen estructurado con referencias verificables |
| **Identificación de gaps** | Preguntar qué temas no están cubiertos por las fuentes | Lista de gaps con contexto de por qué se consideran ausentes |
| **Extracción de claims** | Solicitar listado de afirmaciones clave de un documento | Claims listados con ubicación en el documento fuente |
| **Verificación cruzada** | Consultar si una afirmación específica tiene soporte en las fuentes cargadas | Confirmación o negación con referencia al pasaje relevante |

---

## Funciones prohibidas

Las siguientes funciones **no deben realizarse** en NotebookLM:

| Función prohibida | Razón | Herramienta correcta |
|-------------------|-------|---------------------|
| Generar borradores de documentos completos | No es su rol; produce contenido generado sin estructura de documento | ChatGPT Projects |
| Análisis cuantitativo de datos | No tiene capacidad de ejecución de código | Deepnote |
| Almacenar conocimiento permanente | Es temporal; no persiste como fuente de verdad | Obsidian, GitHub |
| Registrar decisiones formales | Las decisiones requieren versionado | GitHub |
| Crear specs o requirements | Requiere spec-driven development | Kiro |
| Debatir ideas o explorar libremente | Limitado a documentos cargados; no tiene contexto amplio | ChatGPT Projects |

---

## Reglas de IA responsable

NotebookLM es una herramienta de IA. Todo output que produce está sujeto a las reglas de AI responsable definidas en R22.

### Regla 1: Clasificación como AI_Generated_Content

Todo output sustantivo de NotebookLM (resúmenes, claims factuales, explicaciones, análisis) se clasifica como **AI_Generated_Content**, no como Primary_Evidence.

> **Restricción explícita:** Un resumen o respuesta de NotebookLM NO es evidencia verificada, independientemente de que cite fuentes. La cita indica dónde buscar verificación, no constituye verificación en sí misma.

### Regla 2: Verificación obligatoria

Cuando un output de NotebookLM se utiliza para soportar una conclusión de investigación:

1. El investigador DEBE localizar independientemente la fuente primaria citada.
2. El investigador DEBE confirmar que el claim específico existe en esa fuente.
3. La verificación debe realizarse accediendo directamente a la fuente original, NO a través de NotebookLM ni otra herramienta de IA.

### Regla 3: Etiquetado obligatorio

Cuando un output de NotebookLM se incorpora en hallazgos de investigación, DEBE etiquetarse con:

| Campo | Descripción | Ejemplo |
|-------|-------------|---------|
| **Herramienta** | Nombre de la herramienta | NotebookLM |
| **Fecha de generación** | Fecha en que se generó el output | 2025-01-15 |
| **Intención de consulta** | Descripción del query (≤200 caracteres) | "Comparar definiciones de evidence framework en papers de Kitchenham y Webster" |
| **Estado de verificación** | Uno de: `verified`, `unverified`, `source-not-found` | verified |

### Regla 4: Prohibición de citación sin verificación

Si NotebookLM provee un claim factual y la fuente primaria subyacente NO ha sido localizada y verificada independientemente por el investigador mediante acceso directo:

> **PROHIBIDO:** Citar ese claim como evidencia en cualquier conclusión de investigación.

### Regla 5: Uso permitido como analytical aid

NotebookLM puede usarse como herramienta analítica (analytical aid) libremente, siempre que:

- Toda conclusión presentada como hallazgo de investigación descanse en al menos una fuente primaria verificada.
- El output de NotebookLM solo guíe la búsqueda, no sustituya la verificación.

### Regla 6: Verificación fallida

Si el investigador intenta verificar un claim de NotebookLM y la fuente citada no puede localizarse, o no contiene la información afirmada, entonces el investigador DEBE:

1. Descartar el claim como no soportado.
2. Registrar el intento de verificación fallido en el research journal con fecha y fuente buscada.

---

## Clasificación de outputs

Todo output de NotebookLM se clasifica según la taxonomía de outputs del tooling workflow:

| Tipo de output | Clasificación | Tratamiento |
|----------------|---------------|-------------|
| Respuesta a consulta rápida | Analytical aid | Se usa para orientar búsqueda; no se registra formalmente |
| Resumen de documento | Generated content | Requiere verificación antes de promoción; se marca con origen y fecha |
| Comparación de fuentes | Generated content | Requiere verificación de cada divergencia/coincidencia citada |
| Citas extraídas | Generated content | Requiere confirmación contra documento original |
| Insights o conexiones | Analytical aid | Se exporta a Obsidian como nota para explorar; no es evidencia |

### Reglas de promoción desde NotebookLM

| Promoción | Requisitos |
|-----------|-----------|
| Generated content → Repository content | Verificación humana explícita + marcado `verified_by: "human"` + commit a GitHub |
| Analytical aid → Repository content | No aplica directamente; debe recrearse como documento nuevo en herramienta apropiada |
| Generated content → Analytical aid | El contenido se usa para informar trabajo pero no se registra; no requiere verificación formal |

---

## Integración con lifecycle stages

NotebookLM participa en etapas específicas del research lifecycle según su rol exclusivo.

### Etapas donde NotebookLM es herramienta primaria

| Etapa | Rol de NotebookLM | Output esperado |
|-------|-------------------|-----------------|
| **6. Source Collection** | Consultar fuentes cargadas, comparar documentos, evaluar calidad de fuentes | Source_Register poblado con fuentes evaluadas, gaps documentados |
| **7. Evidence Evaluation** | Verificar claims contra fuentes cargadas, comparar evidencia entre documentos, scoring | Evidence register con claims clasificados, conflictos identificados |

### Etapas donde NotebookLM es herramienta de apoyo

| Etapa | Rol de apoyo | Aporte |
|-------|-------------|--------|
| **2. Problem Framing** | Consultar documentación previa sobre el problema | Contexto documental para articular el problema |
| **3. Research Question** | Verificar que las preguntas no están ya respondidas en fuentes disponibles | Validación de novedad de la pregunta |
| **8. Analysis** | Síntesis de hallazgos documentales para triangulación | Inputs para análisis más amplio |
| **10. Findings** | Verificación cruzada de hallazgos contra fuentes originales | Confirmación o señalamiento de discrepancias |

### Etapas donde NotebookLM NO participa

| Etapa | Razón de exclusión |
|-------|-------------------|
| 1. Intake | Requiere exploración libre (ChatGPT) |
| 4. Scope | Requiere decisión, no consulta documental |
| 5. Assumptions | Requiere challenge de ideas (ChatGPT) |
| 9. Experimentation | Requiere ejecución (Deepnote) |
| 11-16. Conclusion en adelante | Requiere documentación formal (GitHub) y síntesis (ChatGPT) |

---

## Protocolo de exportación

### Destinos de exportación

| Destino | Qué se exporta | Cuándo |
|---------|----------------|--------|
| **GitHub** | Citas verificadas contra fuentes, comparaciones con referencias claras | Cuando las citas han sido verificadas independientemente y soportan una conclusión formal |
| **Obsidian** | Insights de lectura, conexiones entre fuentes, ideas para explorar | Cuando el output sugiere conexiones o perspectivas útiles pero no verificadas |

### Qué NO se exporta

- Respuestas completas sin editar de NotebookLM.
- Resúmenes no verificados presentados como hechos.
- Outputs que no han sido revisados por humano.
- Contexto conversacional completo con la herramienta.

### Formato de exportación a GitHub

Cuando se exporta un insight verificado de NotebookLM a GitHub, incluir:

```markdown
## [Título del hallazgo]

**Origen:** NotebookLM — [fecha de generación]
**Verificación:** [verified | unverified | source-not-found]
**Fuente primaria verificada:** [referencia a la fuente original consultada directamente]
**Intención de consulta:** [descripción breve del query original]

[Contenido del hallazgo verificado]
```

### Formato de exportación a Obsidian

Cuando se exporta un insight a Obsidian para exploración:

```markdown
---
origen: NotebookLM
fecha: YYYY-MM-DD
verificado: false
tipo: insight-exploratorio
---

# [Título del insight]

[Contenido del insight con contexto]

## Próximos pasos
- [ ] Verificar contra fuente primaria: [referencia]
- [ ] Conectar con: [[nota-relacionada]]
```

---

## Reglas de verificación

### Checklist de verificación para outputs de NotebookLM

Antes de que cualquier output de NotebookLM se promueva a repository content o se cite en una conclusión:

| # | Verificación | Obligatoria |
|---|-------------|-------------|
| 1 | ¿Se localizó la fuente primaria citada de forma independiente (sin usar NotebookLM)? | Sí |
| 2 | ¿El claim específico existe en la fuente primaria tal como fue reportado? | Sí |
| 3 | ¿Se etiquetó el output con herramienta, fecha, intención y estado de verificación? | Sí |
| 4 | ¿El output se clasifica como Generated content (no como Primary_Evidence)? | Sí |
| 5 | ¿La conclusión que referencia este output tiene al menos una fuente primaria verificada? | Sí |
| 6 | ¿Se documentaron los intentos de verificación fallidos en el research journal? | Sí (si aplica) |

### Niveles de confianza aplicables

| Estado de verificación | Confianza máxima permitida en Evidence_Framework |
|------------------------|--------------------------------------------------|
| `verified` | Confianza determinada por la fuente primaria (1-5) |
| `unverified` | Máximo confianza 2 (plausible inference without direct evidence) |
| `source-not-found` | Confianza 0 — claim descartado, no citable |

---

## Buenas prácticas

### Para maximizar valor de NotebookLM

1. **Cargar documentos de calidad:** La calidad del output está directamente ligada a la calidad de las fuentes cargadas. Priorizar fuentes con score ≥6 en el Source_Register.
2. **Formular consultas específicas:** Preguntas amplias producen resúmenes genéricos. Preferir consultas delimitadas con variable, contexto y tipo de respuesta esperada.
3. **Comparar antes de sintetizar:** Usar la función de comparación para identificar divergencias entre fuentes antes de intentar una síntesis.
4. **Verificar inmediatamente:** Verificar citas mientras se tiene acceso a las fuentes originales. No postergar la verificación.
5. **Exportar lo relevante antes de cerrar:** NotebookLM es temporal. Exportar decisiones, citas verificadas e insights antes de que se pierda el contexto del notebook.

### Para evitar riesgos

1. **No confiar en que las citas sean exactas:** NotebookLM puede parafrasear o asociar incorrectamente. Siempre verificar contra la fuente.
2. **No acumular notebooks sin exportar:** Un notebook cerrado sin exportación es conocimiento perdido.
3. **No usar como sustituto de lectura:** NotebookLM es un acelerador, no un reemplazo de la lectura directa de fuentes.

---

## Anti-patrones específicos

| Anti-patrón | Descripción | Síntomas | Corrección |
|-------------|-------------|----------|-----------|
| **Cita ciega** | Tomar una cita de NotebookLM y copiarla a un documento formal sin verificar que la fuente original dice exactamente eso | Claims en documentos formales que al verificarse no coinciden con la fuente | Implementar checklist de verificación antes de cada exportación |
| **Notebook eterno** | Mantener un notebook abierto indefinidamente sin exportar insights, acumulando consultas sin trazabilidad | Notebooks con semanas de uso sin ningún export a GitHub u Obsidian | Establecer regla de exportación semanal: todo notebook activo exporta o se cierra |
| **Sustitución de lectura** | Usar resúmenes de NotebookLM como sustituto de leer las fuentes directamente, especialmente para fuentes críticas | Conclusiones basadas únicamente en resúmenes sin evidencia de lectura directa | Para fuentes con score ≥7, lectura directa obligatoria; NotebookLM solo como guía de navegación |
| **Falsa independencia** | Tratar la respuesta de NotebookLM como "confirmación independiente" cuando está generada por la misma IA que procesa los documentos | Investigaciones donde "NotebookLM confirma" se usa como segunda fuente | NotebookLM nunca es fuente independiente; solo señala dónde buscar verificación |

---

## Referencias

- [009-tooling-workflow.md](./009-tooling-workflow.md) — Roles de herramientas, handoffs y clasificación de outputs
- [002-research-lifecycle.md](./002-research-lifecycle.md) — Definición de las 16 etapas del lifecycle
- [006-evidence-framework.md](./006-evidence-framework.md) — Categorías de evidencia y niveles de confianza
- [README.md](./README.md) — Índice del package y glosario
