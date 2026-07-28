# 013 — Obsidian Guidelines

> **Etiqueta epistémica:** [Decisión]
>
> **Requirements cubiertos:** R28.1, R28.2

## Propósito

Este documento define el rol de Obsidian dentro del ecosistema LabOS, las reglas de uso, los criterios de maduración de contenido hacia documentos formales en GitHub, y la integración con todas las etapas del Research Lifecycle.

Obsidian es el **repositorio de conocimiento permanente** del Fundador. Su función es acumular, conectar y organizar conocimiento a través del tiempo, a diferencia de GitHub que almacena documentos formales versionados con trazabilidad oficial.

---

## Tabla de contenidos

1. [Rol exclusivo de Obsidian](#rol-exclusivo-de-obsidian)
2. [Diferenciación respecto a GitHub](#diferenciación-respecto-a-github)
3. [Qué se crea en Obsidian](#qué-se-crea-en-obsidian)
4. [Qué NO se crea en Obsidian](#qué-no-se-crea-en-obsidian)
5. [Estructura de notas atómicas](#estructura-de-notas-atómicas)
6. [Reglas de maduración a documento formal](#reglas-de-maduración-a-documento-formal)
7. [Integración con lifecycle stages](#integración-con-lifecycle-stages)
8. [Relación con Source Register y Evidence records](#relación-con-source-register-y-evidence-records)
9. [Versionado y permanencia](#versionado-y-permanencia)
10. [Anti-patrones de uso](#anti-patrones-de-uso)

---

## Rol exclusivo de Obsidian

| Campo | Valor |
|-------|-------|
| **Herramienta** | Obsidian |
| **Clasificación** | Repositorio de conocimiento |
| **Permanencia** | Semi-permanente |
| **Rol exclusivo** | Conocimiento permanente, notas atómicas, relaciones conceptuales, índice personal |

### Funciones principales

1. **Notas atómicas:** Captura de unidades discretas de conocimiento, cada una con un solo concepto o idea.
2. **Mapas conceptuales:** Conexiones explícitas entre notas mediante links internos (`[[nota]]`), visualizables en el graph view.
3. **Índice personal de conocimiento:** Organización temática que permite navegar el conocimiento acumulado por dominio, por investigación, o por concepto.
4. **Conexiones inter-investigación:** Relaciones entre hallazgos de diferentes investigaciones que revelan patrones transversales.
5. **Captura rápida de insights:** Registro inmediato de ideas, conexiones y observaciones durante cualquier etapa del lifecycle.

### Lo que Obsidian NO es

- No es la fuente de verdad formal del proyecto (eso es GitHub).
- No es una herramienta de debate o exploración libre (eso es ChatGPT Projects).
- No es un repositorio de fuentes documentales con citas (eso es NotebookLM).
- No es un ambiente de ejecución de código o análisis de datos (eso es Deepnote).

---

## Diferenciación respecto a GitHub

La distinción entre Obsidian y GitHub es crítica para el ecosistema LabOS:

| Dimensión | Obsidian | GitHub |
|-----------|----------|--------|
| **Naturaleza del contenido** | Conocimiento en evolución, conexiones emergentes, ideas en maduración | Documentos formales, decisiones aprobadas, versiones finales |
| **Estado del contenido** | Borrador, parcial, especulativo, en desarrollo | Completo, revisado, aprobado |
| **Audiencia** | Fundador (uso personal) | Cualquier stakeholder del proyecto |
| **Trazabilidad** | Interna (links entre notas, graph view) | Formal (commits, PRs, tags, referencias cruzadas) |
| **Versionado** | Git local del vault (sin garantía de review) | Git con commits atómicos y mensajes descriptivos |
| **Citable como evidencia** | No directamente; requiere exportación a GitHub | Sí, citable como fuente verificable |
| **Estándar de calidad** | Suficiente para comprensión personal | Verificable por terceros, estructura completa |
| **Permanencia** | Semi-permanente (persiste pero no es fuente de verdad) | Fuente de verdad (estado oficial del proyecto) |

### Regla general

> Obsidian contiene conocimiento que **evoluciona**. GitHub contiene conocimiento que **se ha validado**.

---

## Qué se crea en Obsidian

| Tipo de contenido | Descripción | Ejemplo |
|-------------------|-------------|---------|
| **Nota atómica** | Un concepto, definición o idea expresada en ≤300 palabras | "Definición de evidence ceiling para AI-generated content" |
| **Mapa conceptual** | Nota que conecta ≥3 notas atómicas con relación explícita | "Relación entre hypothesis types y experiment design" |
| **Índice temático** | Nota que organiza un dominio o tema con links a notas relevantes | "MOC: Research Methodology — todos los conceptos clave" |
| **Insight de investigación** | Hallazgo parcial o conexión descubierta durante trabajo investigativo | "Patrón: investigaciones de >16h siempre requieren decomposición" |
| **Pregunta emergente** | Pregunta surgida durante una investigación que puede originar investigación futura | "¿Es posible automatizar la evaluación de sources con scoring algorítmico?" |
| **Conexión inter-dominio** | Relación entre conceptos de diferentes labs o investigaciones | "El concepto de timebox en research es análogo a sprint en development" |
| **Resumen personal** | Síntesis para comprensión propia de un paper, libro o fuente consultada | "Resumen personal de 'Thinking in Systems' — principios aplicables a LabOS" |

---

## Qué NO se crea en Obsidian

| Contenido | Razón | Herramienta correcta |
|-----------|-------|---------------------|
| Documentos formales del proyecto | Requieren versionado formal y revisión | GitHub |
| Decision records oficiales | Requieren trazabilidad y aprobación | GitHub |
| Análisis de datos con código | Requiere ambiente de ejecución | Deepnote |
| Comparaciones de fuentes con citas verificables | Requiere anclaje a documentos subidos | NotebookLM |
| Debates exploratorios y borradores extensos | Naturaleza temporal, no permanente | ChatGPT Projects |
| Credenciales, tokens o API keys | Riesgo de seguridad | Gestores de secretos |
| Specs de features o requirements | Proceso spec-driven formal | Kiro |

---

## Estructura de notas atómicas

Cada nota atómica en Obsidian debe seguir esta estructura mínima:

```markdown
# [Título del concepto]

**Fecha:** YYYY-MM-DD
**Dominio:** [lab o área temática]
**Estado:** borrador | consolidado | exportado
**Investigación origen:** [ID o nombre, si aplica]

## Contenido

[Descripción del concepto en ≤300 palabras. Un solo concepto por nota.]

## Conexiones

- [[nota-relacionada-1]] — relación
- [[nota-relacionada-2]] — relación

## Fuentes

- [referencia 1]
- [referencia 2]

## Tags

#dominio #tema #estado
```

### Reglas de notas atómicas

1. **Una idea por nota.** Si una nota cubre más de un concepto independiente, debe descomponerse.
2. **Título descriptivo.** El título debe permitir entender el contenido sin abrir la nota.
3. **Conexiones explícitas.** Toda nota debe tener al menos 1 link a otra nota existente (excepto la primera nota de un dominio nuevo).
4. **Estado declarado.** Cada nota indica si es borrador, consolidada (revisada por el Fundador) o exportada (ya maduró a GitHub).

---

## Reglas de maduración a documento formal

Una nota (o conjunto de notas) en Obsidian madura a documento formal en GitHub cuando cumple **todos** los siguientes criterios:

### Criterios de maduración

| # | Criterio | Verificación |
|---|----------|-------------|
| 1 | **Completitud conceptual** | El contenido responde una pregunta completa o define un proceso completo, sin placeholders ni "[pendiente]" |
| 2 | **Estabilidad** | El contenido no ha cambiado sustancialmente en ≥7 días (indicando que la idea se estabilizó) |
| 3 | **Verificabilidad** | Las afirmaciones están soportadas por fuentes referenciables o evidencia documentada |
| 4 | **Audiencia expandida** | El contenido es útil para stakeholders más allá del Fundador (o será referenciado por otros documentos) |
| 5 | **Estructura formal** | El contenido puede adaptarse al formato de documentos LabOS (headers, secciones, etiqueta epistémica) |
| 6 | **Sin dependencias abiertas** | No hay preguntas sin resolver que bloqueen la comprensión del documento |

### Proceso de maduración

1. **Identificar candidato:** El Fundador revisa notas con estado "consolidado" que podrían formalizarse.
2. **Evaluar criterios:** Verificar los 6 criterios de maduración contra la nota o cluster de notas.
3. **Preparar documento:** Reformular el contenido al formato formal de LabOS (agregar etiqueta epistémica, estructura de headers, referencias formales).
4. **Exportar a GitHub:** Crear el documento en la ubicación correspondiente con commit descriptivo.
5. **Actualizar estado en Obsidian:** Marcar la nota como "exportado" y agregar link al documento en GitHub.
6. **Registrar handoff:** Documentar el handoff en el commit message o en la sección "Origen" del documento destino.

### Cuándo NO madurar

- Cuando el contenido es especulativo y no tiene soporte evidencial.
- Cuando la nota es un resumen personal que no agrega valor al proyecto.
- Cuando el conocimiento es tan específico que solo tiene sentido en el contexto personal del Fundador.
- Cuando ya existe un documento en GitHub que cubre el mismo tema (evitar duplicación).

---

## Integración con lifecycle stages

Obsidian participa como **herramienta transversal** en todas las 16 etapas del Research Lifecycle, operando como base de conocimiento continua que captura, conecta y enriquece el trabajo investigativo.

### Participación por etapa

| Etapa | Rol de Obsidian | Tipo de nota creada |
|-------|-----------------|---------------------|
| 1. Intake | Captura rápida del trigger, conexión con investigaciones previas | Nota de trigger, links a notas existentes |
| 2. Problem Framing | Conexiones conceptuales que informan el problema | Mapa de relaciones del problema |
| 3. Research Question | Mapeo de relaciones entre preguntas y conocimiento previo | Nota de pregunta con contexto |
| 4. Scope | Referencia a conocimiento previo para estimar alcance | Consulta de notas existentes |
| 5. Assumptions | Registro de supuestos vinculados a conocimiento previo | Notas de assumptions con links |
| 6. Source Collection | Registro de insights de fuentes consultadas | Resúmenes personales de fuentes |
| 7. Evidence Evaluation | Mapeo de evidencia, identificación de patrones | Mapas de evidencia conectada |
| 8. Analysis | Mapeo conceptual de patrones y relaciones emergentes | Notas de patrones, mapas conceptuales |
| 9. Experimentation | Registro de insights de experimentos | Notas de aprendizaje experimental |
| 10. Findings | Síntesis de hallazgos, conexión con conocimiento previo | Notas de hallazgos con links |
| 11. Conclusion | Conexión de conclusión al knowledge base existente | Nota de conclusión conectada |
| 12. Review | Referencia para verificar consistencia con conocimiento previo | Consulta (no creación) |
| 13. Asset Extraction | Conexiones para identificar valor reutilizable | Índice de activos extraídos |
| 14. Product Hypothesis | Conexiones entre hallazgos y oportunidades comerciales | Notas de oportunidad |
| 15. Publication/Archive | Actualización del índice de conocimiento | Índice actualizado |
| 16. Feedback & Iteration | Registro de feedback y nuevas conexiones | Notas de feedback, preguntas derivadas |

### Patrón de uso transversal

En **cada sesión de trabajo** de cualquier etapa, el Fundador puede:

1. **Consultar** Obsidian para contextualizar el trabajo con conocimiento previo.
2. **Capturar** insights emergentes como notas atómicas sin interrumpir el flujo de trabajo principal.
3. **Conectar** hallazgos nuevos con notas existentes mediante links internos.
4. **Actualizar** notas existentes si nueva evidencia las enriquece o las contradice.

---

## Relación con Source Register y Evidence records

### Source Register

Obsidian **no reemplaza** al Source_Register. La relación es complementaria:

| Aspecto | Source_Register (GitHub) | Obsidian |
|---------|------------------------|----------|
| **Propósito** | Registro formal de fuentes con evaluación de calidad (10 criterios) | Comprensión personal de lo que la fuente aporta |
| **Contenido** | Metadata formal: ID, tipo, access date, quality score (0-10), limitaciones | Resumen personal, insights extraídos, conexiones con otros conceptos |
| **Formato** | Campos estructurados obligatorios por R7 | Nota libre con estructura atómica sugerida |
| **Citabilidad** | Citable como referencia oficial en conclusiones | No citable directamente; informa el análisis personal |
| **Cuándo se crea** | Cuando una fuente se consulta formalmente durante Source Collection | Cuando una fuente genera un insight o conexión que vale registrar |

### Evidence records

Obsidian **no reemplaza** los Evidence records del Evidence_Framework. La relación:

| Aspecto | Evidence Record (GitHub) | Obsidian |
|---------|--------------------------|----------|
| **Propósito** | Clasificación formal de evidencia con confidence level y verificación | Mapeo personal de cómo piezas de evidencia se relacionan entre sí |
| **Contenido** | evidence_id, source_id, evidence_type, confidence (1-5), limitations, verified_by | Nota de patrón, mapa de evidencia conectada, insight sobre relaciones |
| **Verificación** | Requiere clasificación formal y verificación humana | No requiere verificación formal; es herramienta de pensamiento |
| **Citabilidad** | Puede soportar conclusiones formales | No puede soportar conclusiones; informa el razonamiento |

### Flujo de información

```text
[Fuente consultada]
       │
       ├──── Source_Register (GitHub) ──── registro formal con evaluación
       │
       └──── Obsidian ──── insight personal, conexiones, comprensión
                │
                ▼
         [Informa análisis]
                │
                ▼
         Evidence Record (GitHub) ──── clasificación formal de evidencia
                │
                └──── Obsidian ──── mapeo de relaciones entre evidencias
```

### Regla de citación

> Nunca citar una nota de Obsidian como fuente en una conclusión formal. Las conclusiones deben trazar a Source_Register entries o Evidence records en GitHub. Obsidian informa el razonamiento; GitHub valida la evidencia.

---

## Versionado y permanencia

| Campo | Valor |
|-------|-------|
| **Mecanismo de versionado** | Git local del vault de Obsidian |
| **Frecuencia de commit** | Al final de cada sesión de trabajo o cuando se acumulen ≥5 cambios significativos |
| **Clasificación** | Semi-permanente |
| **Regla de persistencia** | El contenido persiste en el vault pero no constituye fuente de verdad formal |
| **Exportación** | A GitHub cuando cumple criterios de maduración |
| **Backup** | Responsabilidad del Fundador; se recomienda remote git (privado) |

### Implicaciones

- Se puede referenciar contenido de Obsidian en conversaciones de trabajo en progreso (ChatGPT, reuniones internas).
- Las conclusiones formales **no** pueden depender exclusivamente de contenido que solo existe en Obsidian.
- Si una nota de Obsidian se exporta a GitHub, la nota de Obsidian se marca como "exportado" pero se mantiene como referencia rápida.

---

## Anti-patrones de uso

| Anti-patrón | Descripción | Consecuencia | Corrección |
|-------------|-------------|--------------|------------|
| **Obsidian como archivo muerto** | Crear notas y nunca revisitarlas, sin conexiones ni mantenimiento | Knowledge base se degrada; notas obsoletas coexisten con actuales | Revisar notas mensualmente; archivar las obsoletas; mantener conexiones activas |
| **Obsidian como GitHub** | Tratar notas como documentos formales sin exportarlos | Conocimiento validado queda inaccesible para el proyecto formal | Aplicar criterios de maduración; exportar cuando se cumplen |
| **Notas monolíticas** | Crear notas extensas que cubren múltiples conceptos | Dificulta conexiones, reutilización y navegación | Descomponer en notas atómicas (1 concepto = 1 nota) |
| **Citar Obsidian como evidencia** | Referenciar notas personales como fuente en conclusiones formales | Viola trazabilidad; la evidencia no es verificable por terceros | Trazar siempre a Source_Register o Evidence records en GitHub |
| **Duplicar GitHub en Obsidian** | Copiar documentos formales de GitHub a Obsidian | Crea versiones divergentes; confusión sobre cuál es la actual | En Obsidian mantener solo links a documentos de GitHub, no copias |
| **Ignorar conexiones** | Crear notas sin links a notas existentes | Se pierde el valor principal de Obsidian (relaciones emergentes) | Toda nota debe tener ≥1 link; revisar graph view periódicamente |

---

## Referencias

- [009-tooling-workflow.md](./009-tooling-workflow.md) — Roles, handoffs y flujo entre herramientas
- [002-research-lifecycle.md](./002-research-lifecycle.md) — Definición de las 16 etapas del lifecycle
- [006-evidence-framework.md](./006-evidence-framework.md) — Framework de evidencia y confidence levels
- [README.md](./README.md) — Índice del package y glosario
