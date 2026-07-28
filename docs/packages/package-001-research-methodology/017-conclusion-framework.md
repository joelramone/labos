# 017 — Conclusion Framework

[Decisión]

## Propósito

Este documento define el **Conclusion Framework** de LabOS: el sistema estructurado para formular, clasificar y documentar conclusiones de investigación con trazabilidad completa a la evidencia que las soporta. [Hecho]

El framework establece:

- Campos obligatorios para toda conclusión
- Trazabilidad obligatoria a evidencia registrada en el Source_Register o Evidence_Framework
- Tres tipos de conclusión diferenciados por fortaleza de evidencia
- Reglas para manejar contradicciones con findings previos
- Documentación de resultados inconclusos
- Sección de uncertainty con clasificación completa

Toda conclusión dentro de LabOS debe formularse bajo este framework para garantizar que las afirmaciones son trazables, diferenciadas por nivel de certidumbre, y acompañadas de documentación explícita de limitaciones e incertidumbre. [Decisión]

---

## 1. Campos obligatorios de una conclusión

Toda conclusión formulada en una investigación LabOS debe contener los siguientes campos sin excepción: [Decisión]

### 1.1 Estructura de Conclusion Record

```
Conclusion Record
├── conclusion_id            : string
│   Formato: CON-{investigation_id}-{sequential_number}
│   Ejemplo: CON-INV-042-001
│
├── research_question        : string
│   La research question que esta conclusión responde.
│   Referencia al identificador de la question o texto completo.
│   Ejemplo: "RQ-1: ¿Cuál es la latencia real del sistema bajo carga?"
│
├── evidence_summary         : object
│   Resumen de la evidencia que soporta la conclusión.
│   ├── summary_text         : string
│   │   Síntesis narrativa (1-3 párrafos) de la evidencia evaluada.
│   ├── evidence_references  : string[]
│   │   Al menos una referencia al Source_Register o Evidence_Framework.
│   │   Formato: evidence_id (EVD-xxx) o source_id (SRC-xxx).
│   │   Ejemplo: ["EVD-INV-042-003", "EVD-INV-042-007", "SRC-INV-042-012"]
│   └── evidence_count       : integer
│       Número total de piezas de evidencia consideradas.
│
├── confidence_level         : object
│   Nivel de confianza de la conclusión.
│   ├── level                : enum (high | medium | low)
│   ├── justification        : string
│   │   Explicación escrita de por qué se asigna este nivel.
│   └── supporting_evidence_levels : integer[]
│       Niveles de confianza (1-5) de las evidencias que soportan.
│
├── conclusion_type          : enum
│   Tipo de conclusión según fortaleza de evidencia.
│   Valores: strong_evidence | limited_evidence | inference
│   (Ver Sección 3 para definiciones completas.)
│
├── limitations              : string[]
│   Al menos una limitación de alcance, aplicabilidad o generalización.
│   Ejemplo: ["Válida solo para configuraciones con ≤1000 req/s",
│             "No probado en ambiente de producción"]
│
├── implications             : string
│   Implicaciones para el problema original que motivó la investigación.
│   Describe cómo esta conclusión afecta el entendimiento del problema,
│   las decisiones posibles, o el curso de acción.
│
├── recommended_actions      : object[]
│   Al menos una acción recomendada con resultado esperado.
│   Cada entrada contiene:
│   ├── action               : string
│   │   Descripción de la acción recomendada.
│   ├── expected_outcome     : string
│   │   Resultado esperado si se ejecuta la acción.
│   └── priority             : enum (high | medium | low)
│       Prioridad relativa de la acción.
│   Ejemplo: [{ action: "Migrar a configuración X",
│               expected_outcome: "Reducción de latencia p95 en 40%",
│               priority: "high" }]
│
├── open_questions           : string[]
│   Preguntas que permanecen sin respuesta tras la conclusión.
│   Ejemplo: ["¿Se mantiene el comportamiento bajo tráfico real?",
│             "¿Cuál es el costo operativo de la configuración propuesta?"]
│
├── contradiction_notes      : object[] | null
│   Si la conclusión contradice findings previos, se documenta aquí.
│   (Ver Sección 4 para estructura completa.)
│   null si no hay contradicciones.
│
├── uncertainty_section      : object
│   Sección obligatoria de uncertainty.
│   (Ver Sección 5 para estructura completa.)
│
├── formulated_at            : date (formato YYYY-MM-DD)
│   Fecha de formulación de la conclusión.
│
└── status                   : enum
    Estado de la conclusión.
    Valores: draft | under_review | approved | revision_needed | rejected
```

### 1.2 Regla de completitud

Todos los campos del Conclusion Record son obligatorios. No se permite formular una conclusión con campos vacíos. Si un campo no aplica en un contexto específico (por ejemplo, `contradiction_notes` cuando no hay contradicciones), se indica explícitamente con `null` o una declaración de ausencia. [Decisión]

### 1.3 Regla de mínimos

- `evidence_references` debe contener **al menos una** referencia válida.
- `limitations` debe contener **al menos una** limitación.
- `recommended_actions` debe contener **al menos una** acción con su `expected_outcome`.
- `open_questions` puede estar vacío solo si se justifica explícitamente en `uncertainty_section`.

---

## 2. Trazabilidad a evidencia

Toda conclusión debe ser trazable a la evidencia que la soporta. Esta sección define las reglas de trazabilidad. [Decisión]

### 2.1 Regla de trazabilidad obligatoria

Cada conclusión formulada dentro de LabOS debe trazar a **al menos una pieza de evidencia registrada** en el Source_Register o Evidence_Framework de la investigación. [Decisión]

No se acepta una conclusión cuya única base sea:
- Intuición no documentada
- Conversación no registrada
- Output de IA sin verificación ni registro en el Evidence_Framework

### 2.2 Formato de referencia

Las referencias de evidencia utilizan los identificadores definidos en el Evidence_Framework (documento 006):

| Tipo de referencia | Formato | Ejemplo |
|--------------------|---------|---------|
| Evidence Record | `EVD-{investigation_id}-{seq}` | EVD-INV-042-003 |
| Source Register | `SRC-{investigation_id}-{seq}` | SRC-INV-042-012 |
| Experiment Record | `EXP-{investigation_id}-{seq}` | EXP-INV-042-001 |

### 2.3 Validación de trazabilidad

Durante el review de una conclusión, se verifica que: [Decisión]

1. Cada `evidence_reference` citada corresponde a un registro existente y accesible.
2. El claim registrado en la evidencia citada es consistente con lo que la conclusión afirma.
3. El `confidence` de la evidencia citada es compatible con el `confidence_level` de la conclusión (ver Sección 2.4).

### 2.4 Coherencia entre evidencia y conclusión

El nivel de confianza de una conclusión debe ser coherente con los niveles de confianza de la evidencia que la soporta: [Decisión]

| Confidence de conclusión | Evidencia requerida |
|--------------------------|---------------------|
| **High** | Soportada por evidencia con confidence levels 4-5 |
| **Medium** | Soportada por evidencia con confidence level 3 |
| **Low** | Soportada por evidencia con confidence levels 1-2 |

Si la evidencia más fuerte tiene confidence 3, la conclusión no puede clasificarse como `high`. Esta regla previene conclusiones sobreconfiadas respecto a la evidencia disponible.

---

## 3. Tipos de conclusión

Toda conclusión se clasifica en exactamente uno de tres tipos según la fortaleza de la evidencia que la soporta. [Decisión]

### 3.1 Definición de tipos

| Tipo | Nombre | Definición | Criterio operativo |
|------|--------|------------|-------------------|
| **strong_evidence** | Conclusión con evidencia fuerte | Conclusión soportada por 2 o más fuentes independientes con evidencia a confidence level 4-5. | ≥2 evidence_references con confidence ≥4, provenientes de fuentes independientes (source_ids distintos sin relación de dependencia). |
| **limited_evidence** | Conclusión con evidencia limitada | Conclusión soportada por una sola fuente o evidencia a confidence level 1-3. | Una sola evidence_reference, o todas las references tienen confidence ≤3. |
| **inference** | Conclusión por inferencia | Conclusión derivada lógicamente de evidencia indirecta sin confirmación directa del fenómeno por ninguna fuente. | No hay evidence_reference que confirme directamente el claim. La conclusión se construye por razonamiento deductivo, inductivo o abductivo a partir de evidencia de contextos análogos o relacionados. |

### 3.2 Reglas de clasificación

1. El tipo de conclusión se determina **objetivamente** según los criterios operativos. No es una elección subjetiva del investigador. [Decisión]
2. Si existe duda sobre si la evidencia califica como "independiente", se clasifica como `limited_evidence` por defecto.
3. Una conclusión clasificada como `inference` requiere que el campo `justification` en `confidence_level` explique el razonamiento lógico utilizado.
4. El tipo de conclusión determina cómo debe comunicarse (ver Sección 3.3).

### 3.3 Requisitos de comunicación por tipo

| Tipo | Requisito de comunicación |
|------|---------------------------|
| **strong_evidence** | Puede presentarse como hallazgo respaldado. Debe incluir las fuentes citadas y limitaciones de generalización. |
| **limited_evidence** | Debe acompañarse de una declaración visible que indique que la evidencia es limitada, especificando qué la hace limitada (fuente única, confianza baja, etc.). |
| **inference** | Debe presentarse explícitamente como inferencia. Debe incluir el razonamiento utilizado y la declaración de que no existe confirmación directa. No puede presentarse como hallazgo confirmado. |

### 3.4 Regla de no presentación definitiva

Ninguna conclusión clasificada como `limited_evidence` o `inference` puede presentarse como definitiva o confirmada. [Decisión] Cada conclusión con confidence level `medium` o `low` debe incluir una declaración visible de cualificación que identifique:

- El tipo de incertidumbre que afecta la conclusión
- El impacto potencial de esa incertidumbre en la validez de la conclusión

Esta regla implementa el requisito R13.3 de prohibir la presentación de conclusiones inciertas como definitivas.

---

## 4. Contradicciones con findings previos

Cuando una conclusión contradice un finding previamente aceptado dentro de LabOS, se aplican las siguientes reglas. [Decisión]

### 4.1 Obligación de documentación

Si una conclusión contradice un finding o conclusión previamente aceptada (aprobada en review), el investigador **debe** documentar explícitamente la contradicción. No se permite ignorar o no mencionar contradicciones conocidas. [Decisión]

### 4.2 Estructura de contradiction_notes

```
contradiction_notes: object[]
├── previous_finding_id      : string
│   Referencia al finding o conclusión previo que se contradice.
│   Ejemplo: "CON-INV-028-002" o "Finding #3 de INV-028"
│
├── previous_claim           : string
│   El claim previo que esta conclusión contradice (parafraseado).
│
├── current_claim            : string
│   El claim actual que contradice al previo.
│
├── analysis                 : string
│   Análisis de por qué ocurre la contradicción.
│   Debe explorar al menos una causa posible:
│   - Cambio en condiciones del contexto
│   - Evidencia previa insuficiente o errónea
│   - Diferencia de scope o definición
│   - Nueva evidencia que invalida la anterior
│
├── evidentiary_comparison   : object
│   Comparación de soporte evidenciario.
│   ├── previous_evidence_strength : string
│   │   Descripción de la fortaleza de evidencia del finding previo.
│   └── current_evidence_strength  : string
│       Descripción de la fortaleza de evidencia de la conclusión actual.
│
└── resolution               : enum
    Decisión tomada respecto a la contradicción.
    Valores:
    ├── accept_new       — Se acepta la conclusión nueva como más soportada.
    ├── retain_previous  — Se retiene el finding previo como más soportado.
    └── unresolved       — Se marca como no resuelto, pendiente de más evidencia.
```

### 4.3 Reglas de resolución

1. La resolución debe basarse en la **fortaleza comparativa de la evidencia**, no en la preferencia del investigador ni en la temporalidad (más reciente no implica más correcto). [Decisión]
2. Una resolución `accept_new` requiere que la evidencia actual sea estrictamente más fuerte que la previa (más fuentes independientes, mayor confidence, o evidencia directa vs inferencia).
3. Una resolución `unresolved` es válida y esperada cuando la evidencia disponible no permite determinar cuál finding tiene mayor soporte.
4. Toda contradicción con resolución `unresolved` se registra como un item en la `uncertainty_section`.

---

## 5. Sección de uncertainty

Toda conclusión debe incluir una sección de uncertainty que documente explícitamente las fuentes de incertidumbre. [Decisión]

### 5.1 Categorías de uncertainty

La sección de uncertainty contiene items en las siguientes categorías:

| Categoría | Definición | Ejemplo |
|-----------|------------|---------|
| **Known unknowns** | Gaps identificados: preguntas que se sabe que no se han respondido. | "No se evaluó el comportamiento del sistema bajo fallo parcial de red." |
| **Methodological limitations** | Limitaciones del método de investigación empleado que pueden afectar la validez de la conclusión. | "La medición se realizó solo en ambiente de staging; el comportamiento en producción puede diferir." |
| **Evidence gaps** | Evidencia que sería necesaria pero no fue posible obtener durante la investigación. | "No se encontraron benchmarks independientes de la herramienta evaluada." |
| **Scope limitations** | Restricciones deliberadas del alcance que limitan la aplicabilidad de la conclusión. | "La conclusión aplica solo a la versión 3.x; versiones anteriores no fueron evaluadas." |

### 5.2 Estructura de uncertainty item

```
uncertainty_item
├── category            : enum
│   Valores: known_unknown | methodological_limitation |
│            evidence_gap | scope_limitation
│
├── description         : string
│   Descripción clara del elemento de incertidumbre.
│
├── affected_conclusions : string[]
│   Identificadores de las conclusiones afectadas.
│   Ejemplo: ["CON-INV-042-001", "CON-INV-042-003"]
│
├── impact              : enum (high | medium | low)
│   ├── high   — Puede invalidar la conclusión.
│   ├── medium — Reduce la confianza en la conclusión.
│   └── low    — Caveat menor que no compromete la conclusión.
│
├── classification      : enum (reducible | irreducible | temporal)
│   Clasificación epistémica de la incertidumbre.
│   (Ver Sección 5.3 para definiciones.)
│
└── recommended_action  : string | null
    Acción sugerida para abordar la incertidumbre (si es reducible o temporal).
    null si es irreducible y no hay acción posible.
```

### 5.3 Clasificación de uncertainty

Cada item de incertidumbre se clasifica en exactamente una de tres categorías epistémicas: [Decisión]

| Clasificación | Definición | Ejemplo | Acción típica |
|---------------|------------|---------|---------------|
| **Reducible** | Incertidumbre que puede eliminarse o reducirse mediante más investigación, experimentación o recopilación de evidencia. | "No se evaluó la herramienta en escenarios de alta concurrencia." | Diseñar experimento adicional; buscar más fuentes. |
| **Irreducible** | Incertidumbre inherente al dominio o contexto que no puede eliminarse con más información. | "El comportamiento futuro del mercado es intrínsecamente impredecible." | Documentar como limitación permanente; diseñar para robustez ante variabilidad. |
| **Temporal** | Incertidumbre que se resolverá con el paso del tiempo o la ocurrencia de eventos futuros sin intervención activa del investigador. | "El proveedor anunciará su roadmap 2025 en Q4." | Establecer recordatorio; reevaluar cuando la información esté disponible. |

### 5.4 Evaluación de impacto

El impacto de cada item de incertidumbre se evalúa según su potencial efecto sobre la validez de la conclusión: [Decisión]

| Impacto | Definición | Consecuencia |
|---------|------------|-------------|
| **High** | La incertidumbre puede invalidar la conclusión si se resuelve de forma desfavorable. | La conclusión no puede presentarse como definitiva bajo ninguna circunstancia. Se requiere declaración prominente de riesgo. |
| **Medium** | La incertidumbre reduce la confianza en la conclusión pero no la invalida necesariamente. | La conclusión puede presentarse con cualificación visible. El confidence_level debe reflejarlo. |
| **Low** | La incertidumbre es un caveat menor que no compromete la validez fundamental de la conclusión. | La conclusión puede presentarse con nota al pie o en sección de limitaciones. |

### 5.5 Regla de zero uncertainties

Si la sección de uncertainty no contiene ningún item en ninguna categoría, se requiere una justificación explícita que explique por qué no se identificaron incertidumbres. [Decisión]

Esta justificación:
- Debe ser una declaración positiva (explica por qué no hay incertidumbre, no simplemente "no hay")
- Está sujeta a verificación durante el human review
- Su ausencia invalida la conclusión para efectos de aprobación

Ejemplo de justificación válida: "La conclusión se basa exclusivamente en documentación oficial del proveedor sobre un comportamiento determinístico del sistema, verificada mediante reproducción directa en ambiente controlado, sin variables externas identificadas."

---

## 6. Resultados inconclusos

Cuando la evidencia disponible es insuficiente para formular una conclusión que responda la research question, se documenta un resultado inconcluso. [Decisión]

### 6.1 Estructura de resultado inconcluso

Un resultado inconcluso utiliza la misma estructura de Conclusion Record (Sección 1.1) con las siguientes particularidades:

| Campo | Valor para inconcluso |
|-------|----------------------|
| `confidence_level.level` | `low` |
| `conclusion_type` | `inference` o `limited_evidence` según corresponda |
| `recommended_actions` | Debe incluir al menos un paso concreto para obtener la evidencia faltante |

Adicionalmente, se documentan los siguientes campos específicos de resultado inconcluso:

```
inconclusive_details
├── evidence_gaps        : string[]
│   Qué evidencia específica falta para poder concluir.
│   Ejemplo: ["No se encontraron benchmarks para configuración X",
│             "Falta acceso a datos de producción"]
│
├── minimum_evidence     : string
│   Descripción de la evidencia mínima que permitiría llegar a una conclusión.
│   Ejemplo: "Se necesita al menos un benchmark independiente en
│             ambiente de producción con tráfico real durante ≥24h."
│
└── recommended_next_steps : object[]
    Pasos recomendados para obtener la evidencia faltante.
    Cada paso contiene:
    ├── step              : string
    ├── expected_evidence : string
    └── estimated_effort  : string (formato: Xh o Xd)
```

### 6.2 Regla de documentación de inconclusos

Los resultados inconclusos se documentan con el **mismo rigor** que las conclusiones positivas. [Decisión] No se permite:

- Omitir una research question sin conclusión documentada (aunque sea inconclusa)
- Documentar un inconcluso sin especificar los evidence gaps
- Marcar como inconcluso sin definir qué se necesitaría para concluir

---

## 7. Reglas consolidadas

Para referencia rápida, las reglas del Conclusion Framework: [Decisión]

| # | Regla | Referencia |
|---|-------|-----------|
| 1 | Toda conclusión contiene todos los campos obligatorios del Conclusion Record. | Sección 1 |
| 2 | Toda conclusión traza a ≥1 evidencia registrada en Source_Register o Evidence_Framework. | Sección 2.1 |
| 3 | El confidence de la conclusión es coherente con el confidence de la evidencia que la soporta. | Sección 2.4 |
| 4 | Toda conclusión se clasifica en exactamente uno de tres tipos: strong_evidence, limited_evidence, inference. | Sección 3 |
| 5 | Conclusiones con limited_evidence o inference no pueden presentarse como definitivas. | Sección 3.4 |
| 6 | Contradicciones con findings previos se documentan explícitamente con análisis y resolución. | Sección 4 |
| 7 | La resolución de contradicciones se basa en fortaleza de evidencia, no en temporalidad. | Sección 4.3 |
| 8 | Toda conclusión incluye sección de uncertainty con categorías, impacto y clasificación. | Sección 5 |
| 9 | Cada uncertainty se clasifica como reducible, irreducible o temporal. | Sección 5.3 |
| 10 | Zero uncertainties requiere justificación explícita sujeta a human review. | Sección 5.5 |
| 11 | Resultados inconclusos se documentan con evidence gaps y next steps. | Sección 6 |
| 12 | Ninguna conclusión se descarta o ignora sin documentar la razón. | Sección 2.1 |

---

## Trazabilidad

| Sección del documento | Requirements cubiertos |
|-----------------------|-----------------------|
| Sección 1 (Campos obligatorios) | R12.1 |
| Sección 2 (Trazabilidad a evidencia) | R12.2 |
| Sección 3 (Tipos de conclusión) | R12.3 |
| Sección 3.4 (No presentación definitiva) | R13.3 |
| Sección 4 (Contradicciones) | R12.4 |
| Sección 5 (Uncertainty) | R13.1, R13.2 |
| Sección 5.4 (Impacto) | R13.1 |
| Sección 5.5 (Zero uncertainties) | R13.4 |
| Sección 6 (Resultados inconclusos) | R12.5 |

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho] | 2 | 10% |
| [Decisión] | 18 | 90% |
| [Hipótesis] | 0 | 0% |
| [Visión] | 0 | 0% |
