# 010 — Deepnote Guidelines

> **Etiqueta epistémica:** [Decisión]
>
> **Requirements cubiertos:** R28.1, R28.2

## Propósito

Este documento define el rol específico de Deepnote dentro del ecosistema de herramientas LabOS, sus reglas de uso, flujos de exportación, integración con el research lifecycle y política de versionado de notebooks. Complementa al documento [009-tooling-workflow.md](./009-tooling-workflow.md) que establece el marco general.

---

## Tabla de contenidos

1. [Rol exclusivo de Deepnote](#rol-exclusivo-de-deepnote)
2. [Qué se origina en Deepnote](#qué-se-origina-en-deepnote)
3. [Qué NO se origina en Deepnote](#qué-no-se-origina-en-deepnote)
4. [Cuándo usar Deepnote](#cuándo-usar-deepnote)
5. [Cuándo NO usar Deepnote](#cuándo-no-usar-deepnote)
6. [Integración con lifecycle stages](#integración-con-lifecycle-stages)
7. [Flujo de exportación a GitHub](#flujo-de-exportación-a-github)
8. [Reglas de versionado de notebooks](#reglas-de-versionado-de-notebooks)
9. [Clasificación de outputs](#clasificación-de-outputs)
10. [Reglas de datos y seguridad](#reglas-de-datos-y-seguridad)
11. [Relación con otras herramientas](#relación-con-otras-herramientas)

---

## Rol exclusivo de Deepnote

Deepnote es la herramienta de **análisis de datos y experimentación cuantitativa** dentro del ecosistema LabOS.

| Atributo | Valor |
|----------|-------|
| **Clasificación** | Herramienta de análisis + Repositorio (notebooks) |
| **Permanencia** | Semi-permanente |
| **Fuente de verdad** | No. El contenido persiste en Deepnote pero no constituye fuente de verdad formal hasta que se exporta a GitHub. |
| **Versionado formal** | GitHub (notebooks exportados como código) |

### Funciones principales

- Notebooks reproducibles para análisis de datos
- Visualizaciones de datos (gráficos, tablas, dashboards exploratorios)
- Experimentación cuantitativa (backtesting, simulaciones, modelos estadísticos)
- Análisis estadístico (correlaciones, distribuciones, significancia)
- Prototipado de pipelines de datos

### Funciones que Deepnote NO cumple

- No es repositorio formal de documentación (eso es GitHub)
- No es herramienta de debate o exploración conceptual (eso es ChatGPT Projects)
- No es base de conocimiento permanente (eso es Obsidian)
- No es herramienta de consulta documental con citas (eso es NotebookLM)
- No es herramienta de spec-driven development (eso es Kiro)

---

## Qué se origina en Deepnote

Los siguientes artefactos se **crean por primera vez** en Deepnote:

| Artefacto | Descripción | Ejemplo |
|-----------|-------------|---------|
| **Análisis cuantitativos** | Exploración y análisis de datos numéricos o estructurados | Análisis de distribución de retornos de una estrategia de trading |
| **Visualizaciones de datos** | Gráficos, plots, heatmaps que comunican patrones en datos | Scatter plot de correlación entre variables de un experimento |
| **Resultados de experimentos computacionales** | Outputs de experimentos ejecutados en código | Resultados de backtest con métricas de performance |
| **Modelos estadísticos** | Modelos construidos para validar hipótesis cuantitativas | Regresión lineal para predecir variable dependiente |
| **Notebooks de exploración de datos** | Análisis exploratorio inicial de un dataset | EDA de dataset de mercado para identificar patrones |

---

## Qué NO se origina en Deepnote

| Artefacto | Herramienta correcta | Razón |
|-----------|----------------------|-------|
| Conclusiones formales de investigación | GitHub | Las conclusiones requieren versionado formal y trazabilidad |
| Decision records | GitHub | Las decisiones oficiales se registran en el repositorio versionado |
| Notas atómicas de conocimiento | Obsidian | Las notas permanentes con relaciones conceptuales son rol de Obsidian |
| Borradores narrativos o debates | ChatGPT Projects | La exploración conceptual sin datos es conversación, no análisis |
| Resúmenes con citas de fuentes | NotebookLM | La consulta documental con referencias ancladas es rol de NotebookLM |

---

## Cuándo usar Deepnote

Usar Deepnote cuando la tarea cumple **al menos una** de estas condiciones:

1. **Requiere ejecución de código** para procesar, transformar o analizar datos
2. **Involucra datos cuantitativos** que necesitan exploración, limpieza o modelado
3. **Necesita visualización programática** (plots, gráficos generados con código)
4. **Requiere reproducibilidad computacional** (que otro pueda ejecutar el mismo análisis)
5. **Valida una hipótesis mediante experimento de datos** (backtesting, simulación, A/B test computacional)
6. **Produce métricas numéricas** como output principal del trabajo

---

## Cuándo NO usar Deepnote

**No** usar Deepnote cuando:

| Situación | Acción correcta |
|-----------|-----------------|
| Se debate una idea sin datos involucrados | Usar ChatGPT Projects |
| Se necesita comparar fuentes documentales | Usar NotebookLM |
| Se documenta una decisión formal | Registrar en GitHub |
| Se crea una nota de conocimiento con conexiones | Usar Obsidian |
| Se escribe documentación narrativa sin código | Usar GitHub directamente |
| Se necesita spec de un feature | Usar Kiro |
| El análisis es puramente cualitativo (sin datos numéricos ni código) | Usar ChatGPT Projects o NotebookLM |

---

## Integración con lifecycle stages

Deepnote participa como herramienta primaria o de apoyo en las siguientes etapas del [research lifecycle](./002-research-lifecycle.md):

### Etapas donde Deepnote es herramienta primaria

| Etapa | Rol de Deepnote | Outputs esperados |
|-------|-----------------|-------------------|
| **8. Analysis** | Análisis cuantitativo de evidencia, identificación de patrones, correlaciones | Notebooks con análisis, visualizaciones de patrones, métricas calculadas |
| **9. Experimentation** | Ejecución de experimentos computacionales, registro de resultados | Notebooks con protocolo ejecutado, resultados, gráficos de outcome |

### Etapas donde Deepnote es herramienta de apoyo

| Etapa | Rol de Deepnote | Outputs esperados |
|-------|-----------------|-------------------|
| **6. Source Collection** | Exploración de datasets como fuentes de evidencia | Notebook de exploración inicial del dataset, estadísticas descriptivas |
| **7. Evidence Evaluation** | Análisis cuantitativo de claims, validación numérica | Cálculos de verificación, comparaciones estadísticas |
| **10. Findings** | Visualización de hallazgos para comunicación | Gráficos finales que acompañan findings |

### Etapas donde Deepnote NO participa

Deepnote no tiene rol asignado en las etapas 1-5 (Intake, Problem Framing, Research Question, Scope, Assumptions) ni en las etapas 11-16 (Conclusion, Review, Asset Extraction, Product Hypothesis, Publication, Feedback). Estas etapas son de naturaleza conceptual, narrativa o administrativa.

---

## Flujo de exportación a GitHub

### Qué se exporta

| Artefacto | Se exporta | Formato de exportación | Destino |
|-----------|-----------|----------------------|---------|
| Notebooks finales (análisis completado) | Sí | `.ipynb` o `.py` (según convención del lab) | Repositorio GitHub del proyecto o investigación |
| Resultados numéricos | Sí | Tablas en markdown o CSV incluidos en el notebook | Junto al notebook en GitHub |
| Visualizaciones finales | Sí | Imágenes exportadas (`.png`, `.svg`) o generadas por el notebook | Directorio de assets o dentro del notebook |
| Notebooks de exploración sin conclusión | No | — | Permanecen en Deepnote como trabajo en progreso |
| Datos crudos sensibles | No | — | Nunca se exportan; usar datasets de ejemplo para documentación |

### Protocolo de exportación

1. **Limpiar el notebook** antes de exportar:
   - Eliminar celdas de exploración que no contribuyen al análisis final
   - Asegurar que las celdas se ejecutan en orden secuencial
   - Incluir markdown explicativo entre secciones de código
   - Verificar que no contiene datos sensibles, tokens o credenciales

2. **Documentar en la primera celda** del notebook:
   - Propósito del análisis (1-2 oraciones)
   - Investigación asociada (referencia al Research_Brief o ID)
   - Fecha de última ejecución
   - Dependencias requeridas (librerías, versiones)
   - Fuente de datos utilizada

3. **Commit a GitHub** con mensaje descriptivo:
   - Formato: `analysis: [descripción breve del análisis]`
   - Referenciar investigación o hipótesis si aplica

4. **Registrar el handoff** según protocolo definido en [009-tooling-workflow.md](./009-tooling-workflow.md):
   - Resumen de trabajo completado en Deepnote
   - Decisiones tomadas durante el análisis
   - Referencia al commit en GitHub

---

## Reglas de versionado de notebooks

### Principios

1. **Los notebooks son código.** Se versionan en GitHub como cualquier otro archivo de código fuente.
2. **Deepnote es el entorno de ejecución**, no el repositorio de versiones.
3. **Un notebook exportado a GitHub representa un estado finalizado** del análisis. No se exportan estados intermedios.

### Convenciones de nombres

```text
{investigation-id}-{descriptor}-v{version}.ipynb
```

Ejemplos:
- `inv-001-market-correlation-analysis-v1.ipynb`
- `inv-003-backtest-momentum-strategy-v2.ipynb`
- `exp-007-ab-test-pricing-v1.ipynb`

### Cuándo crear nueva versión

| Situación | Acción |
|-----------|--------|
| Análisis completado por primera vez | Exportar como `v1` |
| Corrección de error en análisis existente | Incrementar versión (`v1` → `v2`) con nota de cambio |
| Extensión del análisis con nuevos datos | Incrementar versión con documentación de qué se agregó |
| Nuevo enfoque analítico sobre los mismos datos | Crear notebook nuevo con descriptor diferente |
| Exploración que no llega a conclusión | No exportar; permanece en Deepnote |

### Estructura en GitHub

```text
research/{investigation-id}/notebooks/
├── {investigation-id}-{descriptor}-v{N}.ipynb
├── {investigation-id}-{descriptor}-v{N}.ipynb
└── README.md  (índice de notebooks con propósito de cada uno)
```

### Reglas de versionado

1. Nunca sobrescribir un notebook ya exportado en GitHub. Siempre incrementar versión.
2. Cada versión exportada debe ser ejecutable de forma independiente (no depender de estado de celdas previas no incluidas).
3. Incluir `requirements.txt` o equivalente cuando el notebook tenga dependencias externas.
4. Las visualizaciones se regeneran al ejecutar el notebook; no se guardan outputs binarios en git si pueden regenerarse.

---

## Clasificación de outputs

Según el marco definido en [009-tooling-workflow.md](./009-tooling-workflow.md):

| Output de Deepnote | Clasificación | Tratamiento |
|--------------------|---------------|-------------|
| Notebook final exportado a GitHub | **Repository content** | Se versiona, se puede citar, es evidencia formal |
| Notebook en progreso dentro de Deepnote | **Analytical aid** | Se usa para trabajo activo, no se referencia como fuente formal |
| Resultados numéricos no verificados | **Generated content** | Requiere verificación (revisión de código y datos) antes de promoción |
| Visualización exportada como imagen | **Repository content** (si acompaña notebook final) | Se incluye en documentación formal |

### Regla de promoción

Un notebook pasa de **analytical aid** a **repository content** cuando:
1. El análisis está completo y responde a la pregunta o hipótesis planteada
2. El notebook fue limpiado y es ejecutable secuencialmente
3. Se verificó que no contiene datos sensibles
4. Se exportó a GitHub con commit documentado
5. Se registró en el Source_Register de la investigación (si aplica como fuente de evidencia)

---

## Reglas de datos y seguridad

### Datos permitidos en Deepnote

| Tipo de dato | Permitido | Condición |
|-------------|-----------|-----------|
| Datos públicos (APIs, datasets abiertos) | Sí | Documentar fuente |
| Datos personales anonimizados | Sí | Verificar que la anonimización es irreversible |
| Datos de mercado (precios, volúmenes) | Sí | Documentar fuente y rango temporal |
| Datos sintéticos para testing | Sí | Marcar como sintéticos |
| Datos personales identificables (PII) | No | Anonimizar antes de cargar |
| Credenciales, tokens, API keys | No | Usar variables de entorno de Deepnote |
| Datos de clientes sin consentimiento | No | No aplicable hasta que existan clientes |

### Reglas de seguridad

1. **Nunca hardcodear credenciales** en celdas de código. Usar variables de entorno o integraciones nativas de Deepnote.
2. **Nunca exportar notebooks con datos sensibles** a GitHub sin sanitización previa.
3. **Documentar la fuente de todo dataset** utilizado en la primera celda del notebook.
4. **Verificar licencias** de datasets antes de incorporar a análisis que puedan exportarse o publicarse.

---

## Relación con otras herramientas

### Deepnote recibe de

| Herramienta origen | Qué recibe | Ejemplo |
|-------------------|------------|---------|
| ChatGPT Projects | Hipótesis a validar, preguntas cuantitativas a responder | "¿Existe correlación entre X y Y? Analiza con estos datos." |
| NotebookLM | Citas con claims cuantitativos a verificar | "El paper dice que el accuracy es 95%. Verifica con nuestro dataset." |
| GitHub | Datasets, código previo, resultados de análisis anteriores | Dataset CSV commiteado, notebook previo como punto de partida |

### Deepnote envía a

| Herramienta destino | Qué envía | Ejemplo |
|--------------------|-----------|---------|
| GitHub | Notebooks finales, resultados, visualizaciones | Notebook limpio con análisis de backtest exportado como `.ipynb` |
| Obsidian | Insights cuantitativos resumidos para notas atómicas | "La correlación entre X e Y es 0.73 (p<0.01)" como nota en Obsidian |
| ChatGPT Projects | Resultados que requieren interpretación o debate | "El modelo predice Z con error de ±15%. ¿Cómo interpretamos esto?" |

### Flujo típico de trabajo

```text
[Hipótesis formulada en ChatGPT]
       │
       ▼
[Datos cargados en Deepnote]
       │
       ▼
[Análisis exploratorio]
       │
       ▼
[Experimento ejecutado]
       │
       ├──── resultados significativos ────► [Exportar notebook a GitHub]
       │                                            │
       │                                            ▼
       │                                     [Registrar como evidencia]
       │
       └──── resultados inconclusos ────► [Iterar o documentar como hallazgo negativo]
```

---

## Referencias

- [009-tooling-workflow.md](./009-tooling-workflow.md) — Marco general de roles, handoffs y clasificación de herramientas
- [002-research-lifecycle.md](./002-research-lifecycle.md) — Definición de las 16 etapas del lifecycle
- [README.md](./README.md) — Índice del package y glosario
