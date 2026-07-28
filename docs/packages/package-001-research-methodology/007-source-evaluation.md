# 007 — Source Evaluation

[Decisión]

## Propósito

Este documento define el **Source Evaluation Framework** de LabOS: el sistema de registro, evaluación y calificación de fuentes que aplica a todas las investigaciones independientemente del dominio. [Hecho]

El framework establece:

- Los campos obligatorios del Source_Register para catalogar toda fuente consultada
- 10 dimensiones de evaluación con criterio binario (0/1) por dimensión
- Un sistema de scoring agregado de 0 a 10
- Un umbral mínimo de calidad (score 6) con reglas de peso para fuentes debajo
- Un protocolo de registro inmediato (misma sesión que la consulta)
- Reglas para cuando ninguna fuente alcanza el umbral

Toda fuente consultada dentro de LabOS debe registrarse y evaluarse bajo este framework antes de ser citada en hallazgos o conclusiones. [Decisión]

---

## 1. Campos obligatorios del Source_Register

Toda fuente consultada durante una investigación se registra con los siguientes campos obligatorios: [Decisión]

```
Source Record
├── source_id           : string
│   Formato: SRC-{investigation_id}-{sequential_number}
│   Identificador único dentro de la investigación.
│   Ejemplo: SRC-INV-042-007
│
├── type                : enum
│   Clasificación del tipo de fuente.
│   Valores: document | API | dataset | person | tool_output | observation
│
├── access_date         : date (formato YYYY-MM-DD)
│   Fecha en que la fuente fue consultada.
│
├── author_or_origin    : string
│   Autor, organización o sistema que produce la fuente.
│   Ejemplo: "Martin Fowler", "AWS Documentation Team", "OpenAI GPT-4"
│
├── relevance_statement : string
│   1 a 3 oraciones que vinculan la fuente con la research question.
│   Ejemplo: "Esta fuente documenta los límites de concurrencia de Lambda,
│             directamente relevante para RQ-2 sobre escalabilidad."
│
├── initial_quality_score : integer (1-5)
│   Evaluación rápida inicial antes del análisis dimensional.
│   1 = calidad mínima, 5 = calidad máxima.
│   Propósito: triaje rápido; no reemplaza la evaluación de 10 dimensiones.
│
├── aggregate_quality_score : integer (0-10)
│   Score resultante de la evaluación dimensional (Sección 2).
│   Se completa tras aplicar las 10 dimensiones.
│
├── dimensions_failed   : string[]
│   Lista de dimensiones que obtuvieron score 0.
│   Ejemplo: ["reproducibility", "independence"]
│
├── limitation_note     : string | null
│   Obligatorio si aggregate_quality_score < 6.
│   Documenta las dimensiones fallidas y su impacto.
│
├── evaluation_timestamp : datetime
│   Momento en que se completó la evaluación dimensional.
│   Debe ser dentro de la misma sesión que access_date.
│
└── confidence_weight   : enum
    Peso asignado para uso en conclusiones.
    Valores: full (score ≥6) | reduced (score <6, máximo 50% de peso)
```

### 1.1 Tipos de fuente

| Tipo | Definición | Ejemplo |
|------|------------|---------|
| **document** | Material escrito: papers, reportes, libros, artículos, documentación técnica. | Paper de IEEE, documentación oficial de Kubernetes. |
| **API** | Interfaz programática consultada para obtener datos o resultados. | Respuesta de la API de GitHub para estadísticas de repositorio. |
| **dataset** | Conjunto de datos estructurado consultado para análisis. | Dataset de Kaggle con métricas de startups. |
| **person** | Información obtenida de una persona mediante entrevista, conversación o consulta. | Entrevista con CTO sobre decisiones de arquitectura. |
| **tool_output** | Resultado generado por una herramienta (incluye IA). | Output de ChatGPT, resultado de un profiler, reporte de SonarQube. |
| **observation** | Información obtenida por observación directa del investigador. | Observación de comportamiento de usuarios en un prototipo. |

---

## 2. Dimensiones de evaluación

Toda fuente registrada se evalúa contra **10 dimensiones**. Cada dimensión recibe un score binario: **1** (cumple) o **0** (no cumple). [Decisión]

### 2.1 Tabla de dimensiones

| # | Dimensión | Definición | Criterio de cumplimiento (score = 1) | Pregunta orientadora |
|---|-----------|------------|--------------------------------------|---------------------|
| 1 | **Authority** | La fuente proviene de un autor, organización o entidad con credenciales verificables y reconocimiento en el dominio. | El autor tiene credenciales verificables (publicaciones, posición institucional, experiencia demostrable) relevantes al tema. | ¿Quién escribió esto y por qué deberíamos confiar en su expertise? |
| 2 | **Currency** | La información es suficientemente reciente para el contexto de la investigación. | La fuente fue publicada o actualizada dentro del período de relevancia del dominio (varía: tecnología ≤2 años, academia ≤5 años, legislación según vigencia). | ¿La información sigue siendo válida dado cuándo fue producida? |
| 3 | **Independence** | La fuente es independiente del sujeto que evalúa o describe. | No existe relación financiera, contractual o de dependencia entre la fuente y el sujeto evaluado. | ¿La fuente tiene incentivos para presentar información sesgada sobre el tema? |
| 4 | **Methodology** | La fuente describe o se basa en una metodología explícita y evaluable. | El proceso de obtención de datos o conclusiones está descrito de forma que un tercero puede evaluar su validez. | ¿Puedo entender cómo llegaron a estas conclusiones? |
| 5 | **Reproducibility** | Los resultados o claims de la fuente pueden ser verificados o reproducidos. | Existe suficiente información (datos, pasos, configuración) para que un tercero intente reproducir los resultados. | ¿Podría alguien más replicar este resultado siguiendo la misma metodología? |
| 6 | **Bias** | La fuente está libre de sesgo evidente que comprometa la objetividad de sus claims. | No se detecta sesgo de selección, confirmación, supervivencia u otro sesgo sistemático que invalide las conclusiones. Score 1 = libre de sesgo evidente. | ¿La presentación de información es equilibrada o favorece una narrativa específica? |
| 7 | **Conflict of interest** | La fuente no tiene conflictos de interés que comprometan la confiabilidad de su información. | El autor o publicador no tiene interés económico, reputacional o político directo en el outcome de la información presentada. Score 1 = libre de conflicto. | ¿El autor se beneficia directamente si el lector acepta sus conclusiones? |
| 8 | **Precision** | Los claims de la fuente son específicos, cuantificados cuando aplica, y evitan generalidades vagas. | La fuente proporciona datos específicos, rangos, condiciones de aplicabilidad, o calificadores que delimitan sus afirmaciones. | ¿Las afirmaciones son concretas y delimitadas, o vagas y generalizadas? |
| 9 | **Applicability** | La fuente es directamente aplicable al contexto de la investigación actual. | El contexto de la fuente (industria, escala, geografía, tecnología) es suficientemente similar al contexto de la investigación para que sus conclusiones sean transferibles. | ¿El contexto de esta fuente es comparable al nuestro? |
| 10 | **Traceability** | La fuente permite rastrear sus propias afirmaciones hasta datos o fuentes originales. | La fuente cita sus propias fuentes, proporciona referencias, o indica claramente el origen de sus datos. | ¿Puedo seguir la cadena de evidencia hasta su origen? |

### 2.2 Reglas de evaluación dimensional

1. **Evaluación binaria estricta.** Cada dimensión se evalúa como 0 o 1. No existen valores intermedios. Si hay duda razonable, se asigna 0. [Decisión]
2. **Evaluación completa obligatoria.** Las 10 dimensiones deben evaluarse para toda fuente. No se permite omitir dimensiones por considerarlas "no aplicables". [Decisión]
3. **Documentación de dimensiones fallidas.** Toda dimensión que recibe 0 debe tener una justificación breve (1 oración) en el campo `dimensions_failed`. [Decisión]

### 2.3 Guía de aplicación por tipo de fuente

| Tipo de fuente | Dimensiones típicamente más difíciles de cumplir | Nota |
|----------------|--------------------------------------------------|------|
| **document** | currency (si es antiguo) | Verificar fecha de última actualización, no solo publicación. |
| **API** | methodology, traceability | APIs suelen no documentar cómo generan sus datos. |
| **dataset** | bias, methodology | Evaluar cómo se recolectaron los datos. |
| **person** | reproducibility, traceability | Testimonios son difíciles de reproducir; documentar verbatim cuando sea posible. |
| **tool_output** | authority, independence, reproducibility | Herramientas de IA pueden generar contenido no verificable. |
| **observation** | reproducibility, precision | Observaciones son contextuales; documentar condiciones. |

---

## 3. Sistema de scoring agregado

El **aggregate quality score** es la suma de las 10 dimensiones evaluadas: [Decisión]

```
aggregate_quality_score = authority + currency + independence + methodology
                        + reproducibility + bias + conflict_of_interest
                        + precision + applicability + traceability
```

| Rango | Clasificación | Interpretación |
|-------|---------------|----------------|
| 9-10 | Excelente | Fuente de alta confiabilidad. Uso sin restricciones. |
| 7-8 | Buena | Fuente confiable con limitaciones menores documentadas. |
| 6 | Aceptable | Cumple el umbral mínimo. Usar con atención a dimensiones fallidas. |
| 4-5 | Deficiente | Por debajo del umbral. Uso restringido (ver Sección 4). |
| 0-3 | Insuficiente | Fuente de baja confiabilidad. Uso muy restringido (ver Sección 4). |

---

## 4. Umbral de calidad y reglas de peso

### 4.1 Umbral mínimo

El umbral mínimo de calidad es **6 sobre 10**. [Decisión]

Fuentes con score ≥ 6 se consideran aceptables para uso general en la investigación. Fuentes con score < 6 tienen restricciones de uso.

### 4.2 Reglas para fuentes con score < 6

Cuando una fuente obtiene un aggregate quality score inferior a 6: [Decisión]

1. **Uso permitido, pero restringido.** La fuente puede citarse, pero solo con una nota de limitación explícita (`limitation_note`) que indique:
   - Qué dimensiones fallaron (lista)
   - Por qué la fuente se usa a pesar de su score bajo
   - Qué impacto potencial tiene la baja calidad en las conclusiones

2. **Peso de confianza reducido.** La fuente recibe un `confidence_weight: reduced`, lo que significa que su contribución a conclusiones tiene como máximo el **50% del peso** asignado a fuentes con score ≥ 6.

3. **Ceiling de confianza en evidencia.** Según el Evidence Framework (006), una fuente con calidad < 6/10 **no puede producir evidencia con confidence > 3**. Esta restricción aplica independientemente de la naturaleza de la evidencia.

### 4.3 Ejemplo de aplicación (ilustrativo, no resultado real)

> **SRC-INV-015-003** — Blog post de un developer sobre rendimiento de base de datos.
>
> - Authority: 0 (autor sin credenciales verificables en DBs)
> - Currency: 1 (publicado hace 6 meses)
> - Independence: 1 (no vende el producto evaluado)
> - Methodology: 0 (no describe cómo hizo las pruebas)
> - Reproducibility: 0 (no comparte configuración ni datos)
> - Bias: 1 (presentación equilibrada)
> - Conflict of interest: 1 (sin conflicto identificado)
> - Precision: 1 (incluye números concretos)
> - Applicability: 1 (mismo stack tecnológico)
> - Traceability: 0 (no cita fuentes de sus afirmaciones)
>
> **Aggregate score: 6/10** — Cumple umbral mínimo. Dimensiones fallidas documentadas.
> Uso: aceptable, con nota sobre falta de reproducibilidad y methodology.

---

## 5. Regla para ausencia total de fuentes de calidad

Cuando **ninguna fuente** consultada para una research question alcanza el score de 6 o superior: [Decisión]

### 5.1 Documentación obligatoria del gap

Se debe crear un registro de limitación que incluya:

| Campo | Descripción |
|-------|-------------|
| **Research question afectada** | Texto completo de la research question que carece de fuentes de calidad. |
| **Número de fuentes evaluadas** | Total de fuentes consultadas y evaluadas para esa pregunta. |
| **Score más alto alcanzado** | El aggregate quality score máximo entre todas las fuentes evaluadas. |
| **Dimensiones más comúnmente fallidas** | Las 3 dimensiones que fallaron con mayor frecuencia entre las fuentes evaluadas. |
| **Impacto en la investigación** | Declaración del efecto de este gap en las conclusiones posibles. |
| **Acciones recomendadas** | Pasos sugeridos para mejorar la cobertura de fuentes (buscar en otros repositorios, consultar expertos, etc.). |

### 5.2 Consecuencias

- La investigación **no se detiene**, pero la limitación debe documentarse explícitamente como parte de los findings. [Decisión]
- Ninguna conclusión derivada exclusivamente de fuentes con score < 6 puede presentarse como definitiva.
- El gap se registra como una limitación estructural de la investigación en la sección de limitaciones del reporte final.

---

## 6. Protocolo de registro inmediato

### 6.1 Regla de timing

La evaluación de una fuente debe completarse **dentro de la misma sesión** en que la fuente es consultada, y **antes** de que la fuente sea citada en cualquier hallazgo o conclusión. [Decisión]

### 6.2 Definición de "misma sesión"

Una sesión se define como un período continuo de trabajo investigativo. Si el investigador interrumpe el trabajo y lo retoma más tarde, la nueva sesión es un período distinto. [Decisión]

| Situación | ¿Cumple el protocolo? |
|-----------|----------------------|
| Consulto fuente, evalúo dimensiones, luego cito en conclusión → misma sesión. | ✅ Sí |
| Consulto fuente hoy, evalúo mañana antes de citarla. | ❌ No — la evaluación debió ser en la sesión de consulta. |
| Consulto fuente, cito en borrador de conclusión, evalúo después. | ❌ No — la evaluación debe preceder a la cita. |
| Consulto fuente, evalúo inmediatamente, no la uso en esta sesión. | ✅ Sí — evaluación a tiempo, uso futuro permitido. |

### 6.3 Justificación

El registro inmediato previene: [Hecho]

- **Sesgo de confirmación**: evaluar la fuente después de usarla puede sesgar la evaluación hacia justificar una conclusión ya escrita.
- **Pérdida de contexto**: el juicio sobre dimensiones como methodology o bias es más preciso cuando la fuente está fresca en memoria.
- **Fuentes fantasma**: fuentes citadas pero nunca formalmente evaluadas, que debilitan la trazabilidad.

### 6.4 Procedimiento

1. **Consultar la fuente** — leer, analizar o interactuar con ella.
2. **Registrar campos básicos** — completar `source_id`, `type`, `access_date`, `author_or_origin`, `relevance_statement`, `initial_quality_score`.
3. **Evaluar 10 dimensiones** — asignar 0 o 1 a cada dimensión con justificación para las que reciben 0.
4. **Calcular aggregate score** — sumar las 10 dimensiones.
5. **Asignar confidence_weight** — `full` si score ≥ 6, `reduced` si score < 6.
6. **Completar limitation_note** — obligatorio si score < 6.
7. **Registrar evaluation_timestamp** — confirmar que está dentro de la misma sesión.

Solo después de completar los 7 pasos, la fuente puede citarse en hallazgos o conclusiones.

---

## 7. Relación con Evidence Framework

El Source Evaluation Framework y el Evidence Framework (006) operan en conjunto. La calidad de la fuente impacta directamente la confianza asignable a la evidencia derivada de ella. [Decisión]

| Score de fuente | Confidence máximo de evidencia | Peso en conclusiones |
|-----------------|-------------------------------|---------------------|
| ≥ 6/10 | 5 (sin restricción por fuente) | 100% (full) |
| < 6/10 | 3 (ceiling por calidad de fuente) | ≤ 50% (reduced) |

### 7.1 Flujo de evaluación

```
Fuente consultada
    │
    ▼
Source_Register (este documento)
    │ Evaluar 10 dimensiones → aggregate score
    │
    ▼
┌─────────────────────────────────────┐
│ Score ≥ 6:                          │
│   → confidence_weight: full         │
│   → Evidencia puede alcanzar        │
│     confidence 5 (si otros          │
│     criterios lo permiten)          │
├─────────────────────────────────────┤
│ Score < 6:                          │
│   → confidence_weight: reduced      │
│   → Evidencia NO puede exceder      │
│     confidence 3                    │
│   → Peso máximo 50% en conclusiones │
└─────────────────────────────────────┘
    │
    ▼
Evidence Record (006-evidence-framework.md)
    → Registrar evidencia con source_id vinculado
    → Aplicar ceiling de confidence según score de fuente
```

### 7.2 Interacción con estados de verificación

- Una evidencia con `status: confirmed` requiere ≥2 fuentes independientes con score ≥ 6/10.
- Si las fuentes corroborantes tienen score < 6, la evidencia no puede pasar a `confirmed`.
- Fuentes con score < 6 pueden contribuir como evidencia de soporte pero no como fuente de confirmación.

---

## 8. Resumen de reglas

Para referencia rápida, las reglas consolidadas del Source Evaluation Framework: [Decisión]

| # | Regla | Referencia |
|---|-------|-----------|
| 1 | Toda fuente consultada se registra con los 6 campos obligatorios básicos (source_id, type, access_date, author_or_origin, relevance_statement, initial_quality_score). | Sección 1 |
| 2 | Toda fuente se evalúa contra 10 dimensiones con score binario (0/1). | Sección 2 |
| 3 | El aggregate quality score es la suma de las 10 dimensiones (rango 0-10). | Sección 3 |
| 4 | Fuentes con score < 6 requieren limitation_note y reciben confidence_weight: reduced. | Sección 4.2 |
| 5 | Fuentes con score < 6 tienen peso máximo de 50% respecto a fuentes con score ≥ 6. | Sección 4.2 |
| 6 | Fuentes con score < 6 no pueden producir evidencia con confidence > 3. | Sección 4.2 |
| 7 | Si ninguna fuente alcanza score 6 para una research question, se documenta el gap como limitación. | Sección 5 |
| 8 | La evaluación se completa en la misma sesión que la consulta de la fuente. | Sección 6.1 |
| 9 | La evaluación debe preceder a cualquier cita de la fuente en hallazgos o conclusiones. | Sección 6.1 |
| 10 | Las 10 dimensiones se evalúan completas para toda fuente; no se omiten dimensiones. | Sección 2.2 |
| 11 | Cada dimensión que recibe 0 requiere justificación documentada. | Sección 2.2 |
| 12 | Evidencia `confirmed` requiere fuentes corroborantes con score ≥ 6. | Sección 7.2 |

---

## Trazabilidad

| Sección del documento | Requirements cubiertos |
|-----------------------|-----------------------|
| Sección 1 (Campos obligatorios del Source_Register) | R7.1 |
| Sección 2 (Dimensiones de evaluación) | R7.2 |
| Sección 3 (Sistema de scoring agregado) | R7.2 |
| Sección 4 (Umbral de calidad y reglas de peso) | R7.3 |
| Sección 5 (Ausencia total de fuentes de calidad) | R7.4 |
| Sección 6 (Protocolo de registro inmediato) | R7.5 |
| Sección 7 (Relación con Evidence Framework) | R7.2, R7.3 |

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho] | 2 | 12% |
| [Decisión] | 15 | 88% |
| [Hipótesis] | 0 | 0% |
| [Visión] | 0 | 0% |
