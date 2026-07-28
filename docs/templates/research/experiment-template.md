# Experiment Template

> **Propósito:** Plantilla para diseñar experimentos con protocolo explícito, variables definidas, criterios de éxito/fracaso y campos de reproducibilidad. Asegura que todo experimento dentro de LabOS tenga documentación completa antes de ejecutarse, independientemente del dominio.
>
> **Campos requeridos:** 14 (hypothesis, variables ×3, method, success criterion, failure criterion, time limit, resources, data format, risks, classification, environment, tools, configuration, steps)
>
> **Requirements:** R10.1, R10.2, R19.2, R33.1, R33.2, R33.3, R33.4

---

## Instrucciones de uso

1. **Copiar** este template a la ubicación del experimento dentro de la investigación correspondiente (por ejemplo: `research/{investigation-id}/experiments/EXP-{id}-{seq}.md`).
2. **Completar todos los campos requeridos** antes de iniciar la ejecución del experimento. Ningún campo requerido puede quedar vacío; si un campo no aplica al contexto, indicar "No aplica: [justificación]".
3. **Clasificar el experimento** como `research_experiment` o `commercial_validation_experiment` según su propósito primario (ver Sección de Clasificación).
4. **Verificar los campos de reproducibilidad** (environment, tools_with_versions, configuration, steps) — un tercero debe poder replicar el procedimiento leyendo únicamente este documento.
5. **Vincular la hipótesis** referenciando el ID de la hipótesis formulada según `005-hypothesis-framework.md`. No diseñar experimentos sin hipótesis previa.
6. **Revisar los riesgos** y asegurarse de tener al menos una mitigación identificada por riesgo antes de ejecutar.

---

## Campos requeridos

### Identificación

| Campo | Valor |
|-------|-------|
| **Experiment ID** | `EXP-{investigation_id}-{sequential_number}` |
| **Hypothesis ID** | `HYP-{type-abbreviation}-{sequential-number}` |
| **Classification** | `research_experiment` \| `commercial_validation_experiment` |
| **Created at** | YYYY-MM-DD |

### Hipótesis bajo prueba

> Transcribir o referenciar la hipótesis exacta que este experimento busca validar o refutar.

{Hipótesis vinculada aquí — assertion de la hipótesis}

### Variables

#### Variables independientes

> Variables que se manipulan o varían deliberadamente. Mínimo 1. Cada variable debe ser observable y medible.

| # | Variable | Valores/Rango | Unidad/Escala |
|---|----------|---------------|---------------|
| 1 | {nombre de la variable} | {valores que tomará} | {unidad} |

#### Variables dependientes

> Variables que se miden como resultado de la manipulación. Mínimo 1. Cada variable debe tener unidad o escala definida.

| # | Variable | Unidad/Escala | Método de medición |
|---|----------|---------------|-------------------|
| 1 | {nombre de la variable} | {unidad} | {cómo se mide} |

#### Variables controladas

> Variables que se mantienen constantes durante el experimento. Mínimo 1. Documentar cómo se controlan.

| # | Variable | Valor constante | Método de control |
|---|----------|----------------|-------------------|
| 1 | {nombre de la variable} | {valor fijo} | {cómo se mantiene constante} |

### Método

> Descripción del método experimental. Incluye: diseño (A/B test, pre/post, observacional, etc.), procedimiento, tamaño de muestra o volumen esperado, duración planificada.

{Descripción del método}

### Criterios de éxito y fracaso

| Tipo | Criterio |
|------|----------|
| **Success criterion** | {Condición observable — numérica o binaria — que confirma la hipótesis} |
| **Failure criterion** | {Condición observable — numérica o binaria — que refuta la hipótesis} |

### Time limit

> Tiempo máximo para ejecutar el experimento. Máximo absoluto: 90 días calendario.

| Campo | Valor |
|-------|-------|
| **Duración máxima** | {N} días \| {N} horas |
| **Fecha límite** | YYYY-MM-DD |

### Recursos

> Recursos necesarios para ejecutar el experimento: herramientas, accesos, datos, presupuesto, tiempo humano.

| # | Recurso | Tipo | Costo estimado |
|---|---------|------|----------------|
| 1 | {recurso} | {herramienta/acceso/dato/presupuesto/tiempo} | {costo o "sin costo"} |

### Formato de datos esperado

> Formato esperado de los datos producidos por el experimento.

{Descripción del formato: tipo de archivo, columnas/campos, fuente de exportación}

### Riesgos

> Riesgos que pueden invalidar el experimento o impedir su conclusión. Mínimo 1.

| # | Riesgo | Impacto | Mitigación |
|---|--------|---------|------------|
| 1 | {descripción del riesgo} | {qué pasaría si ocurre} | {acción para mitigar} |

### Clasificación del experimento

> Marcar exactamente una opción.

- [ ] **Research Experiment** — Valida conocimiento probando una hipótesis causal o explicativa. Busca entender por qué algo ocurre o confirmar relaciones entre variables.
- [ ] **Commercial Validation Experiment** — Valida demanda o willingness-to-pay midiendo comportamiento real de mercado. Busca confirmar que un segmento pagaría por una solución.

**Justificación de clasificación:** {Por qué se seleccionó esta clasificación}

---

## Reproducibilidad (R19.2)

### Environment

> Entorno de ejecución. Un tercero debe poder replicar el entorno leyendo esta sección.

| Campo | Valor |
|-------|-------|
| **Sistema operativo** | {OS y versión} |
| **Hardware relevante** | {CPU, RAM, GPU si afecta resultados — o "No relevante"} |
| **Servicios cloud/plataformas** | {nombre y tier} |

### Tools with versions

> Herramientas utilizadas con versiones exactas. Para herramientas web sin versión semántica: incluir fecha de acceso.

| # | Herramienta | Versión | Fecha de acceso |
|---|-------------|---------|-----------------|
| 1 | {nombre} | {versión exacta} | {YYYY-MM-DD si aplica} |

### Configuration

> Configuración aplicada. Referencia a archivos de configuración o descripción inline si es breve.

{Referencia a archivo de configuración o descripción inline de la configuración aplicada}

### Steps (pasos de ejecución)

> Pasos en orden secuencial. Cada paso debe ser reproducible por un tercero. Usar verbos de acción concretos.

1. {Paso 1 — acción concreta}
2. {Paso 2 — acción concreta}
3. {Paso 3 — acción concreta}
4. {Paso N — acción concreta}

---

## Campos opcionales

### Notas adicionales

> Cualquier contexto adicional relevante para la ejecución o interpretación del experimento.

{Notas adicionales}

### Dependencias de otros experimentos

> Si este experimento depende de resultados de otros experimentos previos.

| Experiment ID | Dependencia | Estado |
|---------------|-------------|--------|
| {EXP-id} | {qué resultado se necesita} | {completado/pendiente} |

### Criterio de parada anticipada

> Condición bajo la cual se detiene el experimento antes del time limit (por ejemplo, si se alcanza significancia estadística antes de la fecha límite).

{Condición de parada anticipada — si aplica}

---

## [DOMAIN-SPECIFIC] Secciones específicas por dominio

### [DOMAIN-SPECIFIC] Consideraciones de trading/finanzas

> Para experimentos en dominios financieros (Crypto Scalping Core, Atlas Wealth Labs).

- **Periodo de backtesting:** {fecha inicio — fecha fin}
- **Condiciones de mercado:** {bull/bear/lateral/volatile}
- **Capital simulado:** {monto en USD}
- **Comisiones consideradas:** {sí/no — porcentaje}
- **Slippage simulado:** {sí/no — modelo}

### [DOMAIN-SPECIFIC] Consideraciones de rendimiento técnico

> Para experimentos técnicos (SoftwareFactoryAgentsAI, SentinelOps).

- **Baseline de rendimiento:** {métrica actual antes del experimento}
- **Infraestructura de testing:** {descripción del entorno de pruebas}
- **Carga simulada:** {descripción del patrón de carga}
- **Warm-up:** {tiempo de calentamiento antes de medir}

### [DOMAIN-SPECIFIC] Consideraciones de validación comercial

> Para experimentos de validación de mercado (productos, SaaS, contenido).

- **Segmento target:** {descripción del segmento}
- **Canal de adquisición:** {orgánico/paid/referral/otro}
- **Landing page URL:** {URL}
- **Métrica de conversión primaria:** {definición exacta de conversión}
- **Embudo:** {pasos del embudo de conversión}

---

## Ejemplo completo

> A continuación un ejemplo realista con todos los campos requeridos completados.

---

### Identificación

| Campo | Valor |
|-------|-------|
| **Experiment ID** | `EXP-INV-017-001` |
| **Hypothesis ID** | `HYP-TECH-012` |
| **Classification** | `research_experiment` |
| **Created at** | 2025-02-10 |

### Hipótesis bajo prueba

> "Utilizar streaming de respuestas con LangChain reduce el tiempo percibido de respuesta del agente de soporte en ≥40% comparado con respuesta completa, sin degradar la calidad de la respuesta medida por relevancia."

### Variables

#### Variables independientes

| # | Variable | Valores/Rango | Unidad/Escala |
|---|----------|---------------|---------------|
| 1 | Modo de entrega de respuesta | Streaming vs. Respuesta completa | Categórica (2 niveles) |

#### Variables dependientes

| # | Variable | Unidad/Escala | Método de medición |
|---|----------|---------------|-------------------|
| 1 | Tiempo percibido hasta primera información útil | Milisegundos (ms) | Timestamp del primer token con contenido relevante |
| 2 | Calidad de respuesta | Escala 1-5 | Evaluación humana con rúbrica predefinida (relevancia, completitud, precisión) |

#### Variables controladas

| # | Variable | Valor constante | Método de control |
|---|----------|----------------|-------------------|
| 1 | Modelo LLM | GPT-4o (snapshot 2025-01-15) | Pin de versión en configuración de LangChain |
| 2 | Prompts del sistema | Prompt v2.3 sin modificaciones | Archivo de prompts versionado en Git |
| 3 | Set de preguntas de prueba | 50 preguntas predefinidas del dataset de evaluación | Dataset fijo: `eval/questions-v1.json` |

### Método

A/B test con 2 modos de entrega sobre el mismo set de 50 preguntas de evaluación.

- **Diseño:** Within-subject — cada pregunta se ejecuta en ambos modos.
- **Procedimiento:** Ejecutar las 50 preguntas primero en modo completo (batch A), luego en modo streaming (batch B). Registrar tiempos. Evaluación de calidad por el Fundador usando rúbrica de 3 criterios.
- **Tamaño de muestra:** 50 preguntas × 2 modos = 100 ejecuciones.
- **Duración planificada:** 3 días (1 día setup, 1 día ejecución, 1 día evaluación).

### Criterios de éxito y fracaso

| Tipo | Criterio |
|------|----------|
| **Success criterion** | Tiempo hasta primera información útil en modo streaming es ≥40% menor que en modo completo (mediana), Y la calidad promedio en streaming es ≥4.0/5.0. |
| **Failure criterion** | Diferencia de tiempo <20% entre modos, O calidad promedio en streaming <3.5/5.0. |

### Time limit

| Campo | Valor |
|-------|-------|
| **Duración máxima** | 7 días |
| **Fecha límite** | 2025-02-17 |

### Recursos

| # | Recurso | Tipo | Costo estimado |
|---|---------|------|----------------|
| 1 | API OpenAI (GPT-4o) | Herramienta | ~USD 5 (100 llamadas × ~$0.05 promedio) |
| 2 | Entorno de desarrollo local | Infraestructura | Sin costo |
| 3 | Dataset de evaluación (50 preguntas) | Dato | Sin costo (interno) |
| 4 | Tiempo del Fundador | Tiempo humano | ~6h total |

### Formato de datos esperado

CSV con columnas: `question_id, mode (streaming|complete), time_to_first_useful_token_ms, total_response_time_ms, quality_relevance (1-5), quality_completeness (1-5), quality_precision (1-5), quality_avg, notes`.

Exportado desde script de evaluación: `experiments/exp-017-001/evaluate.py`.

### Riesgos

| # | Riesgo | Impacto | Mitigación |
|---|--------|---------|------------|
| 1 | Rate limiting de OpenAI durante ejecución batch | Interrupción de mediciones, tiempos inflados | Implementar backoff exponencial; ejecutar con delays de 2s entre llamadas |
| 2 | Variabilidad de latencia de red | Ruido en mediciones de tiempo | Ejecutar desde misma red y horario; tomar mediana no promedio |
| 3 | Sesgo de evaluación de calidad (Fundador evalúa sabiendo el modo) | Calificaciones sesgadas a favor de hipótesis | Evaluar respuestas sin indicar qué modo las generó (blind review) |

### Clasificación del experimento

- [x] **Research Experiment** — Valida conocimiento probando una hipótesis causal o explicativa. Busca entender por qué algo ocurre o confirmar relaciones entre variables.
- [ ] **Commercial Validation Experiment** — Valida demanda o willingness-to-pay midiendo comportamiento real de mercado. Busca confirmar que un segmento pagaría por una solución.

**Justificación de clasificación:** El propósito primario es entender si el streaming reduce el tiempo percibido sin degradar calidad — una relación causal técnica. No se está validando demanda ni willingness-to-pay.

---

### Reproducibilidad (R19.2)

#### Environment

| Campo | Valor |
|-------|-------|
| **Sistema operativo** | macOS 14.3 (Sonoma) |
| **Hardware relevante** | MacBook Pro M2, 16GB RAM — No relevante para resultados (la latencia depende de API) |
| **Servicios cloud/plataformas** | OpenAI API (pay-as-you-go tier) |

#### Tools with versions

| # | Herramienta | Versión | Fecha de acceso |
|---|-------------|---------|-----------------|
| 1 | Python | 3.12.1 | — |
| 2 | LangChain | 0.1.5 | — |
| 3 | OpenAI Python SDK | 1.12.0 | — |
| 4 | pandas | 2.2.0 | — |
| 5 | GPT-4o (modelo) | snapshot 2025-01-15 | 2025-02-10 |

#### Configuration

Archivo de configuración: `experiments/exp-017-001/config.yaml`

```yaml
model: gpt-4o-2025-01-15
temperature: 0.3
max_tokens: 1024
streaming: true  # alternado con false para modo completo
system_prompt_file: prompts/support-agent-v2.3.txt
eval_dataset: eval/questions-v1.json
delay_between_calls_s: 2
```

#### Steps (pasos de ejecución)

1. Clonar repositorio y verificar que el branch `experiment/exp-017-001` contiene el dataset y scripts.
2. Instalar dependencias: `pip install -r experiments/exp-017-001/requirements.txt`.
3. Configurar variable de entorno `OPENAI_API_KEY` con clave válida.
4. Ejecutar batch en modo completo: `python experiments/exp-017-001/run.py --mode complete --output results-complete.csv`.
5. Esperar 10 minutos para evitar rate limiting acumulado.
6. Ejecutar batch en modo streaming: `python experiments/exp-017-001/run.py --mode streaming --output results-streaming.csv`.
7. Combinar resultados: `python experiments/exp-017-001/merge.py --files results-complete.csv results-streaming.csv --output results-merged.csv`.
8. Evaluar calidad en blind review: `python experiments/exp-017-001/evaluate_quality.py --input results-merged.csv --output results-evaluated.csv` (presenta respuestas sin indicar modo).
9. Generar reporte: `python experiments/exp-017-001/report.py --input results-evaluated.csv`.
10. Registrar resultado terminal según criterios de éxito/fracaso.

---
