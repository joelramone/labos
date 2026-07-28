# Source Register Template

## Propósito

Template para el registro estructurado de todas las fuentes consultadas durante una investigación. Permite catalogar, evaluar y trazar cada fuente con scoring de calidad por 10 dimensiones, campos de propiedad intelectual y licenciamiento, garantizando trazabilidad completa desde la consulta hasta su uso en conclusiones.

---

## Campos requeridos

### Registro de fuente

| Campo | Descripción | Formato |
|-------|-------------|---------|
| **Source ID** | Identificador único dentro de la investigación | `SRC-{investigation_id}-{sequential_number}` |
| **Type** | Tipo de fuente | `document` \| `API` \| `dataset` \| `person` \| `tool_output` \| `observation` |
| **Access Date** | Fecha en que se consultó la fuente | `YYYY-MM-DD` |
| **Author / Origin** | Autor, organización o entidad responsable del contenido | Texto libre, nombre verificable |
| **Relevance Statement** | Explicación de cómo la fuente se relaciona con la research question | 1–3 oraciones |
| **Initial Quality Score** | Evaluación inicial rápida de calidad | Entero 1–5 (1=mínima, 5=máxima) |

### Evaluación de 10 dimensiones

Cada dimensión se evalúa con 0 (no cumple) o 1 (cumple). El puntaje agregado es la suma de las 10 dimensiones (rango 0–10).

| # | Dimensión | Pregunta evaluadora | Score |
|---|-----------|--------------------:|-------|
| 1 | **Authority** | ¿La fuente proviene de un autor o entidad con credenciales verificables y reconocidas en el dominio? | 0 \| 1 |
| 2 | **Currency** | ¿La información es actual o vigente para el contexto de la investigación? | 0 \| 1 |
| 3 | **Independence** | ¿La fuente es independiente del tema que evalúa (sin interés comercial o conflicto directo)? | 0 \| 1 |
| 4 | **Methodology** | ¿La fuente describe o emplea una metodología verificable para producir sus afirmaciones? | 0 \| 1 |
| 5 | **Reproducibility** | ¿Un tercero podría reproducir los resultados o verificar las afirmaciones siguiendo la misma metodología? | 0 \| 1 |
| 6 | **Bias** | ¿La fuente está libre de sesgos evidentes (ideológicos, comerciales, de selección)? | 0 \| 1 |
| 7 | **Conflict of Interest** | ¿La fuente está libre de conflictos de interés declarados o detectables? | 0 \| 1 |
| 8 | **Precision** | ¿Las afirmaciones son específicas, cuantificadas y delimitadas (vs. generalizaciones vagas)? | 0 \| 1 |
| 9 | **Applicability** | ¿La información es directamente aplicable al contexto de esta investigación sin adaptación significativa? | 0 \| 1 |
| 10 | **Traceability** | ¿La fuente cita sus propias fuentes o provee referencias verificables para sus afirmaciones? | 0 \| 1 |

| | | **Aggregate Score** | __/10 |

### Campos de IP / Licensing

| Campo | Descripción | Formato |
|-------|-------------|---------|
| **Source Name** | Nombre completo de la fuente tal como aparece publicada | Texto |
| **Author / Rights Holder** | Persona u organización que posee los derechos | Texto |
| **License Type** | Tipo de licencia bajo la cual se publica la fuente | Ej: MIT, CC-BY-4.0, All Rights Reserved, Propietaria, Desconocida |
| **Permitted Uses** | Usos permitidos según la licencia | Ej: uso académico, comercial, redistribución, derivados |
| **Attribution Requirements** | Requisitos de atribución especificados por la licencia | Texto describiendo formato y ubicación requerida |

### Reglas de IP

- Si la licencia es desconocida o no puede determinarse, marcar como **"IP-unresolved"** y restringir uso comercial.
- Si la fuente prohíbe uso comercial, documentar explícitamente y excluir de outputs destinados a distribución comercial.
- Toda fuente con license type distinto de "All Rights Reserved" o "Propietaria" debe verificarse antes de uso comercial.

---

## Campos opcionales

| Campo | Descripción |
|-------|-------------|
| **URL / Location** | Enlace o ubicación física de la fuente |
| **Language** | Idioma de la fuente |
| **Version** | Versión o edición consultada |
| **Notes** | Observaciones adicionales del investigador |
| **Limitation Note** | Obligatorio si aggregate score < 6: dimensiones que fallaron |

---

## [DOMAIN-SPECIFIC] Secciones por dominio

Agregar según dominio de investigación:

- **Technical**: campos adicionales para versión de software, compatibilidad, deprecación.
- **Market**: campos para fecha de corte de datos, cobertura geográfica, tamaño de muestra.
- **Health/Performance**: campos para diseño de estudio (RCT, observacional), tamaño de muestra, periodo de seguimiento.
- **Finance**: campos para regulador de origen, jurisdicción aplicable, fecha de vigencia.

---

## Instrucciones de uso

### Paso 1: Registrar la fuente al momento de consulta

Inmediatamente después de consultar una fuente, completar los **campos de registro** (Source ID, Type, Access Date, Author/Origin, Relevance Statement, Initial Quality Score). El registro debe ocurrir en la misma sesión de trabajo — no dejar para después.

### Paso 2: Evaluar las 10 dimensiones

Para cada dimensión, responder la pregunta evaluadora con un juicio binario:
- **1** = la fuente cumple claramente el criterio
- **0** = la fuente no cumple o no es posible determinarlo

Sumar las 10 puntuaciones para obtener el aggregate score. Si el score es inferior a 6, completar el campo "Limitation Note" indicando cuáles dimensiones fallaron.

### Paso 3: Documentar IP y licensing

Completar los campos de propiedad intelectual. Verificar la licencia directamente en la fuente (footer, página de términos, metadata del documento). Si no es posible determinar la licencia, registrar como "Desconocida" y marcar "IP-unresolved".

### Paso 4: Aplicar reglas de restricción

- Si aggregate score < 6: la fuente puede usarse solo con limitation note explícita y peso de confianza ≤ 50% respecto a fuentes con score ≥ 6.
- Si ninguna fuente para una research question alcanza score ≥ 6: documentar como limitación de la investigación.
- Si IP está como "IP-unresolved": no usar en outputs comerciales hasta resolución.

---

## Ejemplo completo

### Fuente registrada con evaluación completa

---

**Source ID:** SRC-INV-023-004

**Type:** document

**Access Date:** 2024-11-15

**Author / Origin:** Martin Fowler, ThoughtWorks

**Relevance Statement:** Proporciona framework de patrones de integración para microservicios que responde directamente a RQ-2 sobre mejores prácticas de comunicación inter-servicios en arquitecturas distribuidas.

**Initial Quality Score:** 5

---

#### Evaluación de 10 dimensiones

| # | Dimensión | Evaluación | Score |
|---|-----------|-----------|-------|
| 1 | Authority | Martin Fowler es referente reconocido en arquitectura de software con 25+ años de publicaciones. | 1 |
| 2 | Currency | Artículo actualizado en 2023, relevante para stack actual. | 1 |
| 3 | Independence | ThoughtWorks vende consultoría, pero el contenido técnico no promueve producto específico. | 1 |
| 4 | Methodology | Describe patrones con contexto, problema y solución; basado en experiencia documentada en múltiples clientes. | 1 |
| 5 | Reproducibility | Los patrones son implementables independientemente siguiendo las descripciones. | 1 |
| 6 | Bias | Sin sesgo comercial evidente; presenta trade-offs de cada patrón. | 1 |
| 7 | Conflict of Interest | Sin conflicto directo con el tema evaluado. | 1 |
| 8 | Precision | Patrones descritos con condiciones específicas de aplicabilidad y limitaciones. | 1 |
| 9 | Applicability | Directamente aplicable a la arquitectura evaluada en esta investigación. | 1 |
| 10 | Traceability | Cita fuentes, papers y casos de uso específicos. | 1 |

| | | **Aggregate Score** | **10/10** |

---

#### IP / Licensing

| Campo | Valor |
|-------|-------|
| **Source Name** | "Microservices Patterns: Integration Strategies" |
| **Author / Rights Holder** | Martin Fowler / ThoughtWorks Inc. |
| **License Type** | CC-BY-3.0 |
| **Permitted Uses** | Uso académico, comercial, redistribución con atribución, derivados permitidos |
| **Attribution Requirements** | Citar autor, título del artículo, URL original y licencia en cualquier redistribución |

---

#### Campos opcionales

| Campo | Valor |
|-------|-------|
| **URL** | https://martinfowler.com/articles/microservices-patterns.html |
| **Language** | Inglés |
| **Version** | Revisión 2023-09 |
| **Notes** | Complementar con documentación oficial de cada herramienta mencionada |

---

### Fuente con score bajo (ejemplo de restricción)

---

**Source ID:** SRC-INV-023-007

**Type:** tool_output

**Access Date:** 2024-11-16

**Author / Origin:** ChatGPT (OpenAI, GPT-4)

**Relevance Statement:** Generó un resumen comparativo de 3 frameworks de mensajería. Usado como punto de partida para búsqueda de fuentes primarias, no como evidencia directa.

**Initial Quality Score:** 2

---

#### Evaluación de 10 dimensiones

| # | Dimensión | Evaluación | Score |
|---|-----------|-----------|-------|
| 1 | Authority | Modelo de lenguaje sin credenciales verificables en el dominio. | 0 |
| 2 | Currency | Conocimiento con corte temporal; no puede confirmar vigencia actual. | 0 |
| 3 | Independence | Sin interés comercial en las herramientas comparadas. | 1 |
| 4 | Methodology | No describe metodología de análisis ni fuentes de entrenamiento. | 0 |
| 5 | Reproducibility | Respuestas no deterministas; mismo prompt puede generar resultados diferentes. | 0 |
| 6 | Bias | Posibles sesgos de entrenamiento no documentados. | 0 |
| 7 | Conflict of Interest | Sin conflicto de interés identificable. | 1 |
| 8 | Precision | Afirmaciones genéricas sin datos cuantitativos específicos verificables. | 0 |
| 9 | Applicability | Parcialmente aplicable; requiere verificación contra contexto real. | 0 |
| 10 | Traceability | No cita fuentes verificables para sus afirmaciones. | 0 |

| | | **Aggregate Score** | **2/10** |

---

**Limitation Note:** Score < 6. Dimensiones no cumplidas: authority, currency, methodology, reproducibility, bias, precision, applicability, traceability. Esta fuente puede usarse solo como guía exploratoria con peso de confianza ≤ 50% respecto a fuentes con score ≥ 6. No citar como evidencia en conclusiones sin verificación contra fuente primaria.

---

#### IP / Licensing

| Campo | Valor |
|-------|-------|
| **Source Name** | Output de ChatGPT — Comparación de frameworks de mensajería |
| **Author / Rights Holder** | OpenAI (generador) / Usuario (prompt owner) |
| **License Type** | Según ToS de OpenAI: usuario retiene derechos sobre output |
| **Permitted Uses** | Uso comercial permitido según ToS vigentes a fecha de acceso |
| **Attribution Requirements** | No requerido por licencia, pero metodología LabOS requiere etiquetar como AI_Generated_Content |

---

## Trazabilidad

| Sección | Requirements cubiertos |
|---------|----------------------|
| Campos de registro | R7.1, R33.2 |
| Evaluación 10 dimensiones | R7.2 |
| Campos de IP / Licensing | R21.1 |
| Instrucciones de uso | R33.2 |
| Estructura general de template | R33.1, R33.3, R33.4 |
