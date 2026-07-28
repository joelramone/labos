# 006 — Evidence Framework

[Decisión]

## Propósito

Este documento define el **Evidence Framework** de LabOS: el sistema de categorización, evaluación y registro de evidencia que aplica a todas las investigaciones independientemente del dominio. [Hecho]

El framework establece:

- 12 categorías mutuamente exclusivas para clasificar evidencia
- Una escala de confianza de 5 niveles con definiciones precisas
- Un modelo completo de Evidence Record con todos los campos obligatorios
- Reglas de integridad que gobiernan la relación entre tipo de evidencia, confianza y conclusiones
- Un proceso estructurado de registro de resultados
- Estados de verificación con reglas de transición

Todo hallazgo dentro de LabOS debe registrarse bajo este framework para garantizar trazabilidad, evaluabilidad y consistencia. [Decisión]

---

## 1. Categorías de evidencia

Las siguientes 12 categorías son **mutuamente exclusivas**. Cada pieza de evidencia se clasifica en exactamente una categoría. [Decisión]

| # | Categoría | Definición | Ejemplo ilustrativo (no resultado real) |
|---|-----------|------------|----------------------------------------|
| 1 | **Primary Evidence** | Evidencia obtenida directamente de la fuente original verificable sin intermediarios ni interpretación de terceros. | Medición directa de latencia de un API endpoint en un benchmark controlado. |
| 2 | **Secondary Evidence** | Evidencia derivada de fuentes que reportan, sintetizan o interpretan evidencia primaria de otros. | Reporte de Gartner que sintetiza benchmarks realizados por equipos independientes. |
| 3 | **Direct Observation** | Registro de lo que se percibe directamente durante una actividad investigativa, sin instrumentación formal. | Observación de que usuarios abandonan un formulario en el paso 3 durante una sesión de usabilidad. |
| 4 | **Measurement** | Dato cuantitativo obtenido mediante instrumentación definida con unidades y condiciones especificadas. | Registro de 2,340 visitas únicas/día medidas con analytics configurado en un dominio específico. |
| 5 | **Experiment Result** | Resultado producido por un experimento diseñado con variables controladas y criterios predefinidos. | Resultado de un A/B test que muestra 12% de mejora en conversión con p<0.05. |
| 6 | **Professional Experience** | Conocimiento derivado de la práctica profesional directa del investigador en un dominio relevante. | Experiencia de 3 años implementando microservicios indica que la complejidad operativa escala no-linealmente. |
| 7 | **Official Documentation** | Información proveniente de documentación oficial de organismos, empresas o instituciones con autoridad reconocida. | Documentación oficial de AWS sobre límites de concurrencia de Lambda. |
| 8 | **Scientific Literature** | Evidencia publicada en revistas o conferencias con proceso de peer review o revisión editorial formal. | Paper en IEEE que demuestra correlación entre tamaño de equipo y defectos por línea de código. |
| 9 | **Market Data** | Datos sobre comportamiento de mercado: precios, volúmenes, tendencias, transacciones o señales de demanda. | Datos de App Annie mostrando 15% de crecimiento YoY en la categoría de productivity apps. |
| 10 | **Testimony** | Declaración de una persona sobre su experiencia, percepción o conocimiento directo de un evento o situación. | Declaración de un CTO entrevistado sobre los desafíos de adopción de una tecnología en su organización. |
| 11 | **Inference** | Conclusión lógica derivada de evidencia existente mediante razonamiento deductivo, inductivo o abductivo, sin observación directa del fenómeno inferido. | Inferencia de que si el mercado X crece 20% y el competidor Y no cubre el segmento Z, existe oportunidad. |
| 12 | **Opinion** | Juicio subjetivo basado en perspectiva personal, preferencias o interpretación no fundamentada en evidencia directa. | Opinión de un blogger sobre qué framework es "mejor" sin datos comparativos. |

### 1.1 Regla de clasificación

Si una evidencia no puede clasificarse inequívocamente en una sola categoría, se debe: [Decisión]

1. Asignar la categoría **más representativa** del origen y naturaleza de la evidencia.
2. Documentar la ambigüedad en el campo `limitations` del Evidence Record.
3. Justificar brevemente la elección de categoría.

### 1.2 Categorías disponibles por dominio

No todos los dominios producen las 12 categorías con igual frecuencia. Cuando se aplica el framework a un dominio específico, se debe documentar cuáles categorías son esperables y cuáles son infrecuentes o no disponibles. [Decisión] Ninguna evidencia se rechaza únicamente porque su categoría sea inusual en el dominio — se evalúa por sus méritos individuales.

---

## 2. Escala de confianza

La escala de confianza es un valor entero de 1 a 5 que expresa el grado de certidumbre que se puede depositar en una pieza de evidencia. [Decisión]

| Nivel | Nombre | Definición | Criterio operativo |
|-------|--------|------------|-------------------|
| **1** | Unverified opinion | Opinión no verificada sin datos de soporte. No hay evidencia directa ni indirecta que respalde la afirmación. | Fuente única sin credenciales verificables, sin datos, sin referencias. |
| **2** | Plausible inference | Inferencia plausible sin evidencia directa. El razonamiento es coherente pero no hay observación ni medición que lo confirme. | Lógica razonable pero sin fuente que la valide directamente; o una fuente de calidad baja/no verificada. |
| **3** | Indirect evidence | Evidencia indirecta de contexto análogo. Existe evidencia, pero proviene de un contexto diferente o no es directamente aplicable sin adaptación. | Una fuente confiable de un contexto similar; o múltiples fuentes de baja calidad que convergen. |
| **4** | Direct evidence (single source) | Evidencia directa de una fuente confiable única. Hay observación, medición o documentación directa del fenómeno, pero de un solo origen. | Una fuente confiable (score ≥6/10) con evidencia directa y verificable del fenómeno. |
| **5** | Corroborated evidence | Evidencia directa corroborada por múltiples fuentes independientes. Hay confirmación cruzada entre fuentes que no dependen una de otra. | Dos o más fuentes independientes confiables (score ≥6/10) que confirman el mismo hallazgo. |

### 2.1 Reglas de asignación de confianza

- La confianza se asigna **por pieza de evidencia**, no por conclusión global. [Decisión]
- La confianza refleja la calidad y verificabilidad de la evidencia, no su utilidad o relevancia.
- Cuando la calidad de la fuente (según Source_Register) es inferior a 6/10, la confianza asignada no puede exceder 3.
- La confianza puede revisarse a la baja si nueva información invalida o contradice la evidencia.

---

## 3. Modelo de Evidence Record

Toda evidencia registrada en una investigación LabOS utiliza la siguiente estructura: [Decisión]

```
Evidence Record
├── evidence_id         : string
│   Formato: EVD-{investigation_id}-{sequential_number}
│   Ejemplo: EVD-INV-042-003
│
├── source_id           : string
│   Referencia al Source_Register de la investigación.
│   Ejemplo: SRC-INV-042-007
│
├── evidence_type       : enum
│   Una de las 12 categorías definidas en Sección 1.
│   Valores: primary_evidence | secondary_evidence | direct_observation |
│            measurement | experiment_result | professional_experience |
│            official_documentation | scientific_literature | market_data |
│            testimony | inference | opinion
│
├── claim               : string
│   Afirmación que esta evidencia soporta. Una oración declarativa.
│   Ejemplo: "La latencia promedio del endpoint /users es inferior a 200ms
│             bajo carga de 1000 req/s."
│
├── observed_result     : string
│   Qué se observó o midió concretamente. Datos crudos o descripción factual.
│   Ejemplo: "Latencia medida: p50=120ms, p95=180ms, p99=210ms con
│             1000 req/s sostenidos durante 5 minutos."
│
├── confidence          : integer (1-5)
│   Nivel de confianza según escala definida en Sección 2.
│
├── limitations         : string[]
│   Al menos una limitación de alcance o aplicabilidad.
│   Ejemplo: ["Medido solo en ambiente de staging, no producción",
│             "Carga sintética, no tráfico real"]
│
├── collected_at        : date (formato YYYY-MM-DD)
│   Fecha en que la evidencia fue recopilada.
│
├── verified_by         : string
│   Quién verificó la evidencia.
│   Valores: "human" | "unverified" | "AI-assisted"
│
├── verification_note   : string
│   Cómo se verificó y contra qué fuente.
│   Ejemplo: "Verificado contra logs de CloudWatch del 2024-01-15."
│   Si verified_by = "unverified": "Pendiente de verificación."
│
├── verifiability       : enum
│   Evaluación de verificabilidad independiente.
│   Valores: independently_reproducible | verifiable_against_cited_source |
│            not_independently_verifiable
│
├── status              : enum
│   Estado actual de la evidencia.
│   Valores: preliminary | confirmed | contested
│
├── relevance           : string
│   Relación explícita con la research question que esta evidencia aborda.
│   Ejemplo: "Responde directamente a RQ-1: ¿Cuál es la latencia
│             real bajo carga?"
└──
```

### 3.1 Campos obligatorios

Todos los campos del Evidence Record son obligatorios. No se permite registrar evidencia con campos vacíos. Si un campo no aplica (por ejemplo, `verification_note` cuando `verified_by = "unverified"`), se debe indicar explícitamente "Pendiente de verificación" u otra declaración que refleje el estado. [Decisión]

### 3.2 Evaluación de verificabilidad

El campo `verifiability` clasifica cada evidencia según la posibilidad de que un tercero la verifique: [Decisión]

| Valor | Definición | Ejemplo |
|-------|------------|---------|
| **independently_reproducible** | Un tercero puede reproducir la evidencia siguiendo el mismo método sin acceso a la fuente original. | Un benchmark que puede re-ejecutarse con las mismas herramientas y configuración. |
| **verifiable_against_cited_source** | Un tercero puede verificar la evidencia consultando la fuente citada, pero no puede reproducir la observación de forma independiente. | Un dato extraído de un paper publicado o documentación oficial. |
| **not_independently_verifiable** | Un tercero no puede verificar ni reproducir la evidencia sin depender del testimonio del investigador original. | Experiencia profesional subjetiva o una observación no registrada en medios verificables. |

---

## 4. Reglas de integridad

Las siguientes reglas gobiernan la relación entre categorías de evidencia, confianza y su uso en conclusiones: [Decisión]

### 4.1 Ceiling de confianza por tipo

| Categoría | Confidence máximo permitido |
|-----------|----------------------------|
| Opinion | 3 |
| Inference | 3 |
| Todas las demás | 5 |

Una evidencia clasificada como `opinion` o `inference` **nunca** puede tener un confidence superior a 3, independientemente de la calidad de la fuente. La naturaleza subjetiva o derivada de estas categorías impone un techo epistémico. [Decisión]

### 4.2 Restricción de evidencia no verificada

Evidencia con `verified_by: "unverified"` no puede soportar una conclusión con confidence mayor a 2. [Decisión]

Esto significa que si toda la evidencia que soporta una conclusión está sin verificar, la conclusión resultante tiene un ceiling de confianza de 2 (plausible inference).

### 4.3 Restricción de contenido generado por IA

Evidencia producida por herramientas de IA (ChatGPT, NotebookLM, Copilot, etc.) debe: [Decisión]

1. Registrarse con `verified_by: "AI-assisted"`.
2. **No puede** tratarse como Primary Evidence hasta que sea verificada contra la fuente original citada por la herramienta.
3. Tras verificación exitosa contra fuente original, puede reclasificarse a la categoría correspondiente y actualizar `verified_by` a `"human"`.
4. Si la verificación falla (la fuente no confirma el claim), la evidencia se marca como `status: contested` o se retracta.

### 4.4 Manejo de evidencia contestada

Cuando dos o más evidencias presentan claims conflictivos sobre el mismo fenómeno: [Decisión]

1. Ambas evidencias se marcan con `status: contested`.
2. Se documenta el conflicto incluyendo:
   - Los claims conflictivos (textual o parafraseados)
   - Al menos una causa posible de la discrepancia
   - Un rationale de resolución que aborde cada pieza de evidencia conflictiva sin descartar ninguna sin razón explícita
3. La conclusión que dependa de evidencia contestada debe documentar el conflicto explícitamente y no puede presentarse como definitiva.

### 4.5 Regla de no descarte silencioso

Ninguna evidencia registrada puede ser descartada o ignorada sin documentar la razón. Si una evidencia se considera irrelevante o inválida posteriormente, su `status` se actualiza y se documenta la justificación en `verification_note`. [Decisión]

---

## 5. Registro de resultados

Todo resultado de actividad investigativa (análisis de fuente, experimento, observación, comparación) se registra utilizando los campos del Evidence Record más los siguientes campos de clasificación de resultado: [Decisión]

### 5.1 Clasificación de resultados

| Clasificación | Definición | Acción requerida |
|---------------|------------|------------------|
| **Positive** | El resultado confirma o soporta la hipótesis o responde la research question afirmativamente. | Registrar con todos los campos estándar. Vincular a hypothesis si aplica. |
| **Negative** | El resultado refuta la hipótesis o muestra que un enfoque no funciona. | Registrar con mismos campos obligatorios que un resultado positivo. Documentar qué se intentó, por qué no produjo resultado positivo, y qué se aprendió. |
| **Inconclusive** | La evidencia es insuficiente para confirmar o refutar. No se puede concluir. | Registrar con mismos campos obligatorios. Documentar los gaps de evidencia y qué se necesitaría para alcanzar una conclusión. |

### 5.2 Campos adicionales para registro de resultado

Además de todos los campos del Evidence Record (Sección 3), un registro de resultado incluye:

```
Result Record (extiende Evidence Record)
├── [todos los campos de Evidence Record]
├── activity            : string
│   Actividad que produjo el resultado.
│   Ejemplo: "Análisis comparativo de 5 frameworks de testing."
│
├── result_class        : enum
│   Clasificación del resultado.
│   Valores: positive | negative | inconclusive
│
├── result_description  : string
│   Descripción del hallazgo en 1-3 párrafos.
│
├── supporting_data     : string[]
│   Referencias a datos, archivos o fuentes que soportan el resultado.
│
└── research_question_link : string
    Referencia explícita a la research question que este resultado aborda.
```

### 5.3 Regla de paridad

Los resultados negativos e inconclusos se registran con **exactamente los mismos campos obligatorios** que los resultados positivos. [Decisión] No existe un formato reducido para resultados desfavorables. Esta regla previene el sesgo de publicación y garantiza que los aprendizajes de fallos se preserven con igual rigor.

---

## 6. Estados de verificación

Toda evidencia y resultado tiene un `status` que refleja su nivel de verificación. [Decisión]

### 6.1 Definición de estados

| Estado | Definición | Condición de entrada |
|--------|------------|---------------------|
| **Preliminary** | Evidencia registrada pero no verificada contra fuentes independientes. Estado inicial por defecto. | Toda evidencia nueva inicia en este estado. |
| **Confirmed** | Evidencia verificada contra al menos 2 fuentes independientes que corroboran el hallazgo. | Verificación exitosa contra ≥2 fuentes independientes con score ≥6/10. |
| **Contested** | Al menos 2 fuentes proporcionan evidencia conflictiva sobre el mismo hallazgo. | Identificación de conflicto entre fuentes sobre el mismo claim. |

### 6.2 Transiciones permitidas

```
preliminary → confirmed    (verificación exitosa)
preliminary → contested    (conflicto identificado)
confirmed → contested      (nueva evidencia contradice)
contested → confirmed      (resolución del conflicto con nueva evidencia)
```

**Transiciones NO permitidas:** [Decisión]

- `confirmed → preliminary` — Una vez confirmada, la evidencia no revierte a preliminar. Si nueva información la cuestiona, pasa a `contested`.
- `contested → preliminary` — La evidencia contestada se resuelve, no se "des-contesta" volviendo a un estado indeterminado.

### 6.3 Documentación de transición

Cuando el estado de una evidencia cambia, se debe documentar: [Decisión]

| Campo | Descripción |
|-------|-------------|
| **Nuevo estado** | El estado al que transiciona la evidencia. |
| **Fecha de cambio** | Fecha en formato YYYY-MM-DD. |
| **Evidencia que disparó la transición** | Qué nueva información motivó el cambio (referencia a evidence_id o source_id). |
| **Fuentes corroborantes o conflictivas** | Referencias a las fuentes que confirman o contradicen. |

### 6.4 Ejemplo de transición (ilustrativo, no resultado real)

> **EVD-INV-015-004** — Claim: "El mercado de edtech en LATAM creció 25% en 2023."
>
> - Estado anterior: `preliminary`
> - Nuevo estado: `confirmed`
> - Fecha de cambio: 2024-02-20
> - Evidencia que disparó la transición: Reporte de HolonIQ (SRC-INV-015-012) confirma 24.8% de crecimiento. Reporte de Statista (SRC-INV-015-014) indica 26.1%.
> - Fuentes corroborantes: SRC-INV-015-012, SRC-INV-015-014

---

## 7. Resumen de reglas

Para referencia rápida, las reglas consolidadas del Evidence Framework: [Decisión]

| # | Regla | Referencia |
|---|-------|-----------|
| 1 | Toda evidencia se clasifica en exactamente una de las 12 categorías mutuamente exclusivas. | Sección 1 |
| 2 | Si hay ambigüedad de categoría, se asigna la más representativa y se documenta en `limitations`. | Sección 1.1 |
| 3 | La confianza máxima para `opinion` e `inference` es 3. | Sección 4.1 |
| 4 | Evidencia `unverified` no puede soportar conclusión con confidence > 2. | Sección 4.2 |
| 5 | Contenido AI-generated requiere verificación antes de ser Primary Evidence. | Sección 4.3 |
| 6 | Evidencia contestada debe documentar el conflicto con análisis de discrepancia. | Sección 4.4 |
| 7 | No se descarta evidencia sin documentar la razón. | Sección 4.5 |
| 8 | Resultados negativos e inconclusos usan los mismos campos que positivos. | Sección 5.3 |
| 9 | Toda evidencia inicia como `preliminary`. | Sección 6.1 |
| 10 | Las transiciones de estado requieren documentación de fecha, causa y fuentes. | Sección 6.3 |
| 11 | Fuente con calidad < 6/10 no puede producir evidencia con confidence > 3. | Sección 2.1 |
| 12 | No se rechaza evidencia solo porque su categoría sea inusual en el dominio. | Sección 1.2 |

---

## Trazabilidad

| Sección del documento | Requirements cubiertos |
|-----------------------|-----------------------|
| Sección 1 (Categorías de evidencia) | R8.1, R8.4, R8.5 |
| Sección 2 (Escala de confianza) | R8.2 |
| Sección 3 (Evidence Record) | R8.2, R11.1 |
| Sección 4 (Reglas de integridad) | R8.3, R8.4 |
| Sección 5 (Registro de resultados) | R11.1, R11.2 |
| Sección 6 (Estados de verificación) | R11.3, R11.4 |

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho] | 3 | 16% |
| [Decisión] | 16 | 84% |
| [Hipótesis] | 0 | 0% |
| [Visión] | 0 | 0% |
