# 014 — Experiment Design

> **Etiqueta epistémica:** [Decisión]
>
> **Requirements:** R10.1, R10.2, R10.3, R10.4, R10.5, R19.2

---

## Propósito

Este documento define el framework de diseño de experimentos de LabOS: la estructura obligatoria, clasificación, métodos alternativos para dominios sin experimentación controlada, estados terminales y reglas de abandono. [Decisión]

El framework asegura que todo experimento dentro de LabOS tenga un protocolo explícito antes de ejecutarse, criterios predefinidos de éxito y fracaso, y documentación completa de resultados independientemente del outcome. [Decisión]

---

## 1. Campos obligatorios del Experiment Record

Todo experimento diseñado dentro de LabOS debe completar los siguientes campos antes de iniciar ejecución: [Decisión]

```
Experiment Record
├── experiment_id       : string
│   Formato: EXP-{investigation_id}-{sequential_number}
│   Ejemplo: EXP-INV-042-001
│
├── hypothesis_id       : string
│   Referencia a la hipótesis bajo prueba (HYP-{id}).
│   La hipótesis debe estar formulada según 005-hypothesis-framework.md.
│
├── classification      : enum
│   Tipo de experimento (ver Sección 2).
│   Valores: research_experiment | commercial_validation_experiment
│
├── independent_variables : string[]
│   Variables que se manipulan o varían deliberadamente.
│   Mínimo 1. Cada variable debe ser observable y medible.
│   Ejemplo: ["Precio del producto (USD 9, USD 19, USD 29)"]
│
├── dependent_variables   : string[]
│   Variables que se miden como resultado de la manipulación.
│   Mínimo 1. Cada variable debe tener unidad o escala definida.
│   Ejemplo: ["Tasa de conversión (%)", "Tiempo de respuesta (ms)"]
│
├── controlled_variables  : string[]
│   Variables que se mantienen constantes durante el experimento.
│   Mínimo 1. Documentar cómo se controlan.
│   Ejemplo: ["Segmento de usuarios (solo early adopters)",
│             "Canal de adquisición (solo orgánico)"]
│
├── method              : string
│   Descripción del método experimental. Incluye:
│   - Diseño (A/B test, pre/post, observacional, etc.)
│   - Procedimiento paso a paso
│   - Tamaño de muestra o volumen esperado
│   - Duración planificada
│   Ejemplo: "A/B test con 2 variantes de pricing.
│             Landing page con tráfico orgánico dividido 50/50.
│             Mínimo 200 visitantes por variante durante 14 días."
│
├── success_criterion   : string
│   Condición observable (numérica o binaria) que confirma la hipótesis.
│   Debe ser específico y medible, no ambiguo.
│   Ejemplo: "Conversión ≥ 3% en al menos una variante de precio."
│
├── failure_criterion   : string
│   Condición observable (numérica o binaria) que refuta la hipótesis.
│   Debe ser específico y medible, no ambiguo.
│   Ejemplo: "Conversión < 1% en todas las variantes después de 200
│             visitantes por variante."
│
├── time_limit          : string
│   Tiempo máximo para ejecutar el experimento.
│   Máximo absoluto: 90 días calendario. [Decisión]
│   Formato: "{N} días" o "{N} horas".
│   Ejemplo: "30 días"
│
├── resources           : string[]
│   Recursos necesarios para ejecutar el experimento.
│   Incluye: herramientas, accesos, datos, presupuesto, tiempo humano.
│   Ejemplo: ["Landing page (Vercel)", "Google Analytics",
│             "USD 0 (tráfico orgánico)", "2h setup + 1h/semana monitoreo"]
│
├── data_format         : string
│   Formato esperado de los datos producidos por el experimento.
│   Ejemplo: "CSV con columnas: date, variant, visitors, conversions,
│             revenue. Exportado de Google Analytics."
│
├── risks               : string[]
│   Riesgos que pueden invalidar el experimento o impedir su conclusión.
│   Mínimo 1. Cada riesgo debe indicar impacto y mitigación posible.
│   Ejemplo: ["Tráfico insuficiente → extender duración o usar paid ads",
│             "Cambio de algoritmo de Google → documentar fecha y evaluar
│              impacto en resultados"]
│
├── environment         : string
│   Entorno de ejecución para reproducibilidad (R19.2).
│   Incluye: sistema operativo, hardware relevante, servicios cloud.
│   Ejemplo: "macOS 14.2, Vercel (free tier), Google Analytics 4"
│
├── tools_with_versions : string[]
│   Herramientas utilizadas con versiones exactas.
│   Ejemplo: ["Next.js 14.1.0", "Google Analytics 4", "Vercel CLI 33.0.1"]
│
├── configuration       : string
│   Configuración aplicada. Referencia a archivos o inline.
│   Ejemplo: "Split test 50/50 configurado en Vercel Edge Config.
│             Ver archivo: experiments/exp-042-001/config.json"
│
├── steps               : string[]
│   Pasos de ejecución en orden secuencial.
│   Cada paso debe ser reproducible por un tercero.
│   Ejemplo: ["1. Deploy landing page variante A (precio USD 9)",
│             "2. Deploy landing page variante B (precio USD 19)",
│             "3. Configurar split test en Vercel",
│             "4. Verificar tracking de conversiones",
│             "5. Monitorear semanalmente durante 30 días"]
│
└── created_at          : date (formato YYYY-MM-DD)
    Fecha de diseño del experimento.
```

### 1.1 Regla de completitud

Ningún experimento puede iniciar ejecución sin todos los campos obligatorios completados. [Decisión] Si un campo no aplica al contexto (por ejemplo, `controlled_variables` en un estudio observacional), se debe indicar explícitamente "No aplica: [justificación]" en lugar de dejarlo vacío.

### 1.2 Relación con hypothesis framework

El campo `hypothesis_id` vincula directamente el experimento con una hipótesis formulada según `005-hypothesis-framework.md`. Los 6 tipos de hipótesis (research, technical, product, business, revenue, learning) pueden requerir experimentación, pero el tipo de experimento y método varían según el tipo de hipótesis. [Hecho]

---

## 2. Clasificación de experimentos

Todo experimento se clasifica en exactamente una de las siguientes categorías: [Decisión]

| Clasificación | Definición | Propósito | Ejemplo |
|---------------|-----------|-----------|---------|
| **Research Experiment** | Valida conocimiento probando una hipótesis causal o explicativa. Busca entender por qué algo ocurre o confirmar relaciones entre variables. | Producir conocimiento verificable sobre relaciones causa-efecto o mecanismos explicativos. | Benchmark comparativo de 3 frameworks de testing para medir tiempo de ejecución bajo carga constante. |
| **Commercial Validation Experiment** | Valida demanda o willingness-to-pay midiendo comportamiento real de mercado. Busca confirmar que un segmento pagaría por una solución. | Producir evidencia de demanda comercial que justifique inversión en desarrollo. | Landing page con botón de compra para medir tasa de conversión de un producto hipotético. |

### 2.1 Criterios de clasificación

| Criterio | Research Experiment | Commercial Validation |
|----------|--------------------|-----------------------|
| **Hipótesis típica** | Research, technical, learning | Product, business, revenue |
| **Variable dependiente típica** | Métricas técnicas, de rendimiento, de comprensión | Conversión, revenue, engagement, willingness-to-pay |
| **Éxito medido por** | Confirmación/refutación de relación causal | Señal de demanda real (acción del usuario, transacción) |
| **Evidencia producida** | Experiment result, measurement | Market data, experiment result |
| **Validación posterior** | Reproducción del resultado | Transacción real, revenue |

### 2.2 Regla de clasificación

Si un experimento combina elementos de ambos tipos (por ejemplo, un A/B test que mide tanto rendimiento técnico como comportamiento de usuario), se clasifica según su **propósito primario**: [Decisión]

- Si el objetivo principal es entender un mecanismo → `research_experiment`
- Si el objetivo principal es validar demanda comercial → `commercial_validation_experiment`

La clasificación secundaria se documenta en el campo `method` como nota.

---

## 3. Métodos alternativos de validación

Cuando las variables independientes de un dominio no pueden aislarse o manipularse por el investigador, la experimentación controlada no es factible. En estos casos, se debe seleccionar al menos un método alternativo de validación y documentar la justificación. [Decisión]

### 3.1 Métodos alternativos disponibles

| # | Método | Definición | Evidencia que produce | Cuándo usar |
|---|--------|------------|----------------------|-------------|
| 1 | **Observational Study** | Registro sistemático de fenómenos sin manipulación de variables. El investigador observa y documenta lo que ocurre naturalmente. | Direct observation, measurement (pasiva) | Variables no manipulables (mercados financieros, comportamiento de usuarios existentes, fenómenos naturales). |
| 2 | **Comparative Analysis** | Comparación estructurada de alternativas existentes usando criterios predefinidos. No se crea una condición experimental sino que se analizan condiciones pre-existentes. | Secondary evidence, measurement, professional experience | Evaluar herramientas, frameworks, metodologías donde no es práctico implementar todas las alternativas. |
| 3 | **Expert Review** | Evaluación formal por uno o más expertos con criterios definidos. El juicio experto sustituye la medición controlada cuando esta no es factible. | Testimony, professional experience | Dominios creativos, evaluaciones de calidad subjetiva, arquitecturas complejas donde la implementación de prueba es costosa. |
| 4 | **Triangulation** | Convergencia de múltiples tipos de evidencia independiente sobre la misma hipótesis. Si ≥3 fuentes independientes convergen, se considera validación. | Múltiples categorías combinadas | Hipótesis que no pueden probarse con un solo método pero donde múltiples señales débiles pueden converger. |

### 3.2 Estructura de documentación para método alternativo

Cuando se utiliza un método alternativo, el Experiment Record se adapta de la siguiente manera: [Decisión]

```
Alternative Validation Record
├── experiment_id       : string (mismo formato: EXP-{id}-{seq})
├── hypothesis_id       : string
├── classification      : enum (research_experiment | commercial_validation_experiment)
├── validation_method   : enum
│   Valores: observational_study | comparative_analysis |
│            expert_review | triangulation
│
├── justification       : string
│   Por qué la experimentación controlada no es factible.
│   Debe referenciar la naturaleza del dominio y las variables.
│   Ejemplo: "Las variables de mercado financiero (precio de BTC,
│             volumen de trading) no pueden manipularse por un
│             investigador individual."
│
├── method              : string
│   Procedimiento del método alternativo seleccionado.
│
├── acceptance_threshold : string
│   Umbral para considerar la hipótesis validada o refutada.
│   Debe ser explícito y verificable.
│   Ejemplo (triangulación): "≥3 fuentes independientes convergen
│             en la misma dirección con confidence ≥3 cada una."
│   Ejemplo (comparativo): "La alternativa seleccionada supera en
│             ≥2 de 5 criterios definidos con ventaja medible."
│
├── limitations_vs_controlled : string[]
│   Limitaciones de este método comparado con experimentación controlada.
│   Ejemplo: ["No establece causalidad, solo correlación",
│             "Sesgo de selección en las alternativas comparadas",
│             "Dependencia del juicio del evaluador"]
│
├── success_criterion   : string
├── failure_criterion   : string
├── time_limit          : string (máximo 90 días)
├── resources           : string[]
├── data_format         : string
├── risks               : string[]
├── environment         : string
├── tools_with_versions : string[]
├── steps               : string[]
└── created_at          : date
```

### 3.3 Dominios donde la experimentación controlada es limitada

Los siguientes dominios del portafolio LabOS presentan limitaciones frecuentes para experimentación controlada: [Hecho]

| Dominio | Limitación principal | Método alternativo recomendado |
|---------|---------------------|-------------------------------|
| **Crypto Scalping Core** | Variables de mercado no manipulables (precio, volumen, liquidez). Condiciones de mercado no reproducibles exactamente. | Observational study (backtesting con datos históricos), comparative analysis (estrategias). |
| **Atlas Wealth Labs** | Regulaciones financieras limitan experimentación con dinero real. Past performance ≠ future results. | Comparative analysis (modelos), observational study (paper portfolio). |
| **Photography Lab** | Calidad estética es subjetiva. No existe variable dependiente objetiva universal. | Expert review (criterios de composición), comparative analysis (portfolio comparison). |
| **Music Lab** | Producción musical involucra juicio artístico no cuantificable. Audiencia variable. | Expert review (peer review), triangulation (métricas de audiencia + peer + autoevaluación). |
| **Human Performance Lab** | n=1 experiments. Variabilidad individual. Efectos confounding (sueño, estrés, dieta). | Observational study (self-tracking longitudinal), triangulation (literatura + medición personal). |

### 3.4 Regla de selección de método alternativo

Cuando se documenta la justificación para usar un método alternativo, se deben cumplir las siguientes condiciones: [Decisión]

1. Explicar específicamente por qué las variables independientes no pueden manipularse o aislarse.
2. Indicar cuál de los 4 métodos alternativos se selecciona y por qué.
3. Documentar las limitaciones del método seleccionado comparado con experimentación controlada.
4. Definir un `acceptance_threshold` explícito que permita declarar la hipótesis como validada o refutada.

---

## 4. Estados terminales y documentación de resultados

Todo experimento alcanza eventualmente un estado terminal. [Decisión] Los 4 estados terminales posibles son:

### 4.1 Definición de estados terminales

| Estado | Definición | Condición de entrada |
|--------|------------|---------------------|
| **Success** | El success criterion se cumplió dentro del time limit. La hipótesis se considera confirmada con la confianza indicada por la evidencia. | success_criterion evaluado como verdadero con datos recopilados. |
| **Failure** | El failure criterion se cumplió dentro del time limit. La hipótesis se considera refutada con la confianza indicada por la evidencia. | failure_criterion evaluado como verdadero con datos recopilados. |
| **Timeout** | El time limit se alcanzó sin que ni el success ni el failure criterion se cumplieran. El resultado es inconcluso. | time_limit expirado + ni success ni failure criterion cumplido. |
| **Abandoned** | El experimento se abandona antes de alcanzar cualquier criterion por decisión explícita del Fundador. | Decisión documentada del Fundador antes de que se cumpla success, failure o timeout. |

### 4.2 Campos obligatorios de resultado terminal

Independientemente del estado terminal, todo experimento completado debe documentar: [Decisión]

```
Experiment Result Record
├── experiment_id           : string
├── outcome_classification  : enum
│   Valores: success | failure | timeout | abandoned
│
├── outcome_summary         : string
│   Resumen del resultado en 1-3 párrafos.
│   Qué se observó, qué datos se recopilaron, qué significa.
│
├── negative_results        : string[]
│   Resultados negativos obtenidos (incluso en experimentos exitosos).
│   Si no hubo resultados negativos: ["Ninguno identificado"].
│   Ejemplo: ["La variante de precio USD 29 tuvo 0 conversiones",
│             "El tiempo de carga excedió 3s en mobile"]
│
├── unexpected_findings     : string[]
│   Hallazgos no anticipados que emergieron durante el experimento.
│   Si no hubo hallazgos inesperados: ["Ninguno identificado"].
│   Ejemplo: ["El 60% del tráfico provino de un país no target",
│             "Los usuarios preguntaron por una feature no contemplada"]
│
├── deviations_from_protocol : string[]
│   Desviaciones del protocolo original documentadas.
│   Si no hubo desviaciones: ["Ninguna"].
│   Ejemplo: ["Se extendió de 14 a 21 días por tráfico insuficiente",
│             "Se cambió la herramienta de analytics de día 3"]
│
├── data_collected          : string
│   Referencia a los datos recopilados (ubicación, formato).
│   Ejemplo: "experiments/exp-042-001/results.csv — 1,247 registros"
│
├── evidence_produced       : string[]
│   IDs de Evidence Records producidos por este experimento.
│   Vincula con el Evidence Framework (006-evidence-framework.md).
│   Ejemplo: ["EVD-INV-042-005", "EVD-INV-042-006"]
│
├── hypothesis_update       : string
│   Nuevo estado de la hipótesis tras el resultado.
│   Valores: confirmed | refuted | inconclusive | revised | abandoned
│
├── confidence              : integer (1-5)
│   Confianza en el resultado según escala del Evidence Framework.
│
├── subsequent_decision     : string
│   Decisión tomada basándose en el resultado.
│   Ejemplo: "Proceder con precio USD 19. Diseñar siguiente
│             experimento para validar canal de adquisición."
│
├── completed_at            : date (formato YYYY-MM-DD)
│   Fecha de finalización del experimento.
│
└── reproducibility_note    : string
    Nota sobre reproducibilidad del experimento.
    Si es reproducible: referenciar steps y environment.
    Si no es reproducible: documentar razón (datos efímeros,
    condiciones de mercado únicas, etc.) según R19.3.
```

### 4.3 Regla de paridad de documentación

Los resultados de failure y timeout se documentan con **exactamente el mismo nivel de detalle** que los resultados de success. [Decisión] No existe un formato reducido para experimentos fallidos. Esta regla se alinea con la regla de paridad del Evidence Framework (006-evidence-framework.md, Sección 5.3).

### 4.4 Documentación de resultados negativos

Los resultados negativos (hipótesis refutada, enfoque que no funciona) son valiosos y deben documentarse con el mismo rigor que los positivos. [Decisión] Un resultado negativo:

- Confirma que un camino no es viable, ahorrando esfuerzo futuro.
- Puede revelar variables no consideradas previamente.
- Contribuye al conocimiento del dominio incluso sin confirmar la hipótesis original.

### 4.5 Documentación de hallazgos inesperados

Los hallazgos inesperados (`unexpected_findings`) pueden ser más valiosos que el resultado principal del experimento. [Decisión] Cuando un hallazgo inesperado es significativo:

1. Se registra como Evidence Record independiente en el Evidence Framework.
2. Puede generar una nueva hipótesis (vinculada via `hypothesis_id`).
3. Puede derivar en un nuevo Research_Brief si el hallazgo merece investigación propia.

---

## 5. Reglas de abandono

El abandono de un experimento es una decisión legítima que requiere documentación explícita. [Decisión]

### 5.1 Condiciones válidas de abandono

Un experimento puede abandonarse cuando: [Decisión]

| # | Condición | Ejemplo |
|---|-----------|---------|
| 1 | Las assumptions del diseño resultan inválidas | Se descubre que el segmento target no existe o no tiene el problema asumido. |
| 2 | El costo de continuar excede el valor esperado | Recursos necesarios superan el presupuesto disponible o el time limit máximo (90 días). |
| 3 | Información nueva hace irrelevante la hipótesis | Un competidor lanza exactamente la solución propuesta, cambiando el contexto. |
| 4 | Riesgos no anticipados invalidan el diseño | Un cambio regulatorio impide la ejecución del experimento como fue diseñado. |
| 5 | Dependencias externas no se resuelven | Acceso a datos, herramientas o recursos no se materializa en tiempo razonable. |

### 5.2 Campos obligatorios de abandono

Cuando un experimento se abandona, se deben completar los siguientes campos además del Experiment Result Record: [Decisión]

```
Abandonment Record (extiende Experiment Result Record)
├── reason_for_abandonment  : string
│   Explicación clara de por qué se abandona.
│   Debe referenciar una de las 5 condiciones válidas.
│   Ejemplo: "Tráfico orgánico insuficiente para alcanzar muestra
│             estadísticamente significativa en 90 días (condición 2)."
│
├── partial_results         : string[]
│   Resultados parciales obtenidos antes del abandono.
│   Incluir cualquier dato, observación o aprendizaje rescatable.
│   Si no hay resultados parciales: ["Ninguno — abandonado antes
│   de recopilar datos"].
│   Ejemplo: ["42 visitantes en 14 días (insuficiente para conclusión)",
│             "3 usuarios preguntaron por pricing via email"]
│
├── lessons_learned         : string[]
│   Lecciones aprendidas del experimento abandonado.
│   Máximo 5 oraciones. Enfoque en qué haría diferente.
│   Ejemplo: ["Validar volumen de tráfico antes de diseñar A/B test",
│             "Considerar paid ads como respaldo para alcanzar muestra"]
│
└── hypothesis_status       : enum
    Estado de la hipótesis tras el abandono.
    Valores: open | reclassified
    - open: La hipótesis permanece sin validar. Puede retomarse
      con un nuevo diseño experimental.
    - reclassified: La hipótesis se revisa o descarta basándose
      en lo aprendido durante el intento de experimentación.
```

### 5.3 Reglas de abandono

1. **No abandonar silenciosamente.** Un experimento sin resultado documentado es un experimento incompleto, no abandonado. [Decisión]
2. **Preservar resultados parciales.** Incluso si el experimento no alcanzó un criterion, los datos parciales deben registrarse. [Decisión]
3. **Actualizar la hipótesis.** El abandono debe reflejarse en el estado de la hipótesis vinculada. [Decisión]
4. **No reutilizar el experiment_id.** Un experimento abandonado conserva su ID. Un nuevo intento genera un nuevo EXP-{id}. [Decisión]
5. **Máximo 2 abandonos por hipótesis sin revisión.** Si la misma hipótesis tiene 2 experimentos abandonados, se requiere revisar la hipótesis antes de diseñar un tercer intento. [Decisión]

---

## 6. Reproducibilidad

Todo experimento debe diseñarse con reproducibilidad en mente. [Decisión] Los campos de reproducibilidad (environment, tools_with_versions, configuration, steps) cumplen R19.2.

### 6.1 Requisitos de reproducibilidad

| Campo | Propósito | Nivel de detalle requerido |
|-------|-----------|---------------------------|
| `environment` | Un tercero puede replicar el entorno de ejecución. | Sistema operativo, versión. Hardware si es relevante para el resultado. Servicios cloud con tier. |
| `tools_with_versions` | Evitar discrepancias por versiones diferentes. | Nombre exacto + versión semántica. Para herramientas web: fecha de acceso. |
| `configuration` | Reproducir exactamente la configuración aplicada. | Referencia a archivo de configuración o inline si es breve. |
| `steps` | Un tercero puede ejecutar el mismo procedimiento. | Pasos numerados, en orden, sin ambigüedad. Cada paso debe ser una acción concreta. |

### 6.2 Cuando la reproducibilidad no es posible

Algunos experimentos no pueden reproducirse exactamente. En estos casos, documentar: [Decisión]

1. **Razón** por la que la reproducción no es posible (datos efímeros, condiciones de mercado irrepetibles, eventos únicos).
2. **Fecha** en que se identificó la limitación.
3. **Evidencia preservada** como registro: screenshots, exports, logs, copias de datos, grabaciones.
4. **Qué aspectos sí son reproducibles** del procedimiento general (pasos, herramientas, configuración), aun si los datos de entrada no lo son.

---

## 7. Flujo de decisión del experiment design

```
¿Existe una hipótesis formulada?
│
├── NO → Formular hipótesis según 005-hypothesis-framework.md
│         antes de diseñar experimento.
│
└── SÍ → ¿Se pueden manipular las variables independientes?
          │
          ├── SÍ → Diseñar experimento controlado (Sección 1)
          │         ├── Clasificar (Sección 2)
          │         ├── Completar todos los campos obligatorios
          │         ├── Ejecutar según steps
          │         └── Documentar resultado terminal (Sección 4)
          │
          └── NO → Seleccionar método alternativo (Sección 3)
                    ├── Documentar justificación
                    ├── Definir acceptance_threshold
                    ├── Ejecutar método alternativo
                    └── Documentar resultado terminal (Sección 4)
```

---

## 8. Resumen de reglas

| # | Regla | Referencia |
|---|-------|-----------|
| 1 | Todo experimento completa todos los campos obligatorios antes de ejecutarse. | Sección 1.1 |
| 2 | Todo experimento se clasifica como research o commercial validation. | Sección 2 |
| 3 | El time limit máximo absoluto es 90 días calendario. | Sección 1 |
| 4 | Dominios sin experimentación controlada usan al menos 1 método alternativo con justificación. | Sección 3 |
| 5 | Los 4 estados terminales (success, failure, timeout, abandoned) requieren documentación completa. | Sección 4 |
| 6 | Resultados negativos se documentan con el mismo detalle que positivos. | Sección 4.3 |
| 7 | El abandono requiere reason, partial results, lessons, y hypothesis status. | Sección 5.2 |
| 8 | Máximo 2 abandonos por hipótesis sin revisión obligatoria de la hipótesis. | Sección 5.3 |
| 9 | Environment, tools, configuration y steps son obligatorios para reproducibilidad. | Sección 6 |
| 10 | Si la reproducibilidad no es posible, se documenta razón, fecha y evidencia preservada. | Sección 6.2 |
| 11 | No se abandona un experimento sin documentar; el silencio no es abandono. | Sección 5.3 |
| 12 | Hallazgos inesperados se registran como Evidence Records y pueden generar nuevas hipótesis. | Sección 4.5 |

---

## Trazabilidad

| Sección del documento | Requirements cubiertos |
|-----------------------|-----------------------|
| Sección 1 (Campos obligatorios) | R10.1, R19.2 |
| Sección 2 (Clasificación) | R10.2 |
| Sección 3 (Métodos alternativos) | R10.3 |
| Sección 4 (Estados terminales) | R10.4 |
| Sección 5 (Reglas de abandono) | R10.5 |
| Sección 6 (Reproducibilidad) | R19.2 |

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho] | 2 | 7% |
| [Decisión] | 28 | 93% |
| [Hipótesis] | 0 | 0% |
| [Visión] | 0 | 0% |
