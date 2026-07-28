# Conclusion Template

[Decisión]

## Propósito

Template para formular conclusiones de investigación trazables, clasificadas por nivel de certidumbre, con documentación explícita de incertidumbre y limitaciones. Toda conclusión dentro de LabOS debe formularse usando esta estructura para garantizar que las afirmaciones son verificables, diferenciadas por fortaleza de evidencia, y acompañadas de uncertainty documentada.

Este template implementa la estructura definida en [017-conclusion-framework.md](../../packages/package-001-research-methodology/017-conclusion-framework.md) y utiliza las categorías de evidencia y niveles de confianza de [006-evidence-framework.md](../../packages/package-001-research-methodology/006-evidence-framework.md).

---

## Campos obligatorios

Toda conclusión requiere **todos** los campos siguientes sin excepción (R12.1):

| # | Campo | Tipo | Descripción |
|---|-------|------|-------------|
| 1 | **research_question** | string | Research question que esta conclusión responde |
| 2 | **evidence_summary** | object | Resumen de evidencia con referencias (≥1 entrada del Source_Register o Evidence_Framework) |
| 3 | **confidence_level** | object | Nivel de confianza (high/medium/low) con justificación escrita |
| 4 | **conclusion_type** | enum | Tipo de conclusión según fortaleza de evidencia |
| 5 | **limitations** | string[] | Al menos una limitación de alcance o aplicabilidad |
| 6 | **implications** | string | Implicaciones para el problema original |
| 7 | **recommended_actions** | object[] | ≥1 acción recomendada con resultado esperado |
| 8 | **open_questions** | string[] | Preguntas que permanecen sin respuesta |
| 9 | **uncertainty_section** | object | Sección de incertidumbre con categorías, impacto y clasificación |

### Niveles de confianza

| Nivel | Criterio | Evidencia requerida |
|-------|----------|---------------------|
| **High** | Soportada por evidencia de alta calidad | Confidence levels 4-5 en las evidencias de soporte |
| **Medium** | Soportada por evidencia de calidad moderada | Confidence level 3 en las evidencias de soporte |
| **Low** | Soportada por evidencia limitada o débil | Confidence levels 1-2 en las evidencias de soporte |

La justificación debe explicar por qué se asigna el nivel elegido, referenciando los confidence levels de la evidencia que soporta la conclusión.

### Tipos de conclusión

| Tipo | Nombre | Criterio operativo |
|------|--------|-------------------|
| **strong_evidence** | Evidencia fuerte | ≥2 fuentes independientes con confidence ≥4 |
| **limited_evidence** | Evidencia limitada | Una sola fuente, o todas las evidencias con confidence ≤3 |
| **inference** | Inferencia | Sin confirmación directa; derivada por razonamiento lógico de evidencia indirecta |

**Reglas de comunicación por tipo:**

- `strong_evidence`: Puede presentarse como hallazgo respaldado. Incluir fuentes y limitaciones de generalización.
- `limited_evidence`: Acompañar con declaración visible de que la evidencia es limitada y por qué.
- `inference`: Presentar explícitamente como inferencia. Incluir razonamiento y declarar que no hay confirmación directa. **No puede presentarse como hallazgo confirmado.**

---

## Sección de uncertainty (R13.1)

Toda conclusión debe incluir una sección de uncertainty con items en las siguientes categorías:

| Categoría | Clave | Definición |
|-----------|-------|------------|
| **Known unknowns** | `known_unknown` | Gaps identificados: preguntas que se sabe que no se han respondido |
| **Methodological limitations** | `methodological_limitation` | Limitaciones del método de investigación que pueden afectar la validez |
| **Evidence gaps** | `evidence_gap` | Evidencia necesaria que no fue posible obtener |
| **Scope limitations** | `scope_limitation` | Restricciones deliberadas del alcance que limitan la aplicabilidad |

Cada item de uncertainty requiere:

| Campo | Descripción |
|-------|-------------|
| **description** | Descripción clara del elemento de incertidumbre |
| **affected_conclusions** | Conclusiones afectadas por esta incertidumbre |
| **impact** | `high` (puede invalidar), `medium` (reduce confianza), `low` (caveat menor) |
| **classification** | Clasificación epistémica: `reducible`, `irreducible`, `temporal` |
| **recommended_action** | Acción para abordar la incertidumbre (null si irreducible sin acción posible) |

### Clasificación de uncertainty (R13.2)

| Clasificación | Definición | Acción típica |
|---------------|------------|---------------|
| **Reducible** | Puede eliminarse o reducirse con más investigación o experimentación | Diseñar investigación adicional, buscar más fuentes, ejecutar experimento |
| **Irreducible** | Inherente al dominio o contexto; no se elimina con más información | Documentar como limitación permanente; diseñar para robustez |
| **Temporal** | Se resolverá con el paso del tiempo o la ocurrencia de eventos futuros | Establecer recordatorio; reevaluar cuando la información esté disponible |

> **Regla de zero uncertainties:** Si la sección no contiene ningún item, se requiere una justificación explícita de por qué no se identificaron incertidumbres. Esta justificación está sujeta a verificación durante human review.

---

## Sección de epistemic classification

Toda conclusión debe declarar la clasificación epistémica de su contenido:

| Etiqueta | Significado | Cuándo aplica |
|----------|-------------|---------------|
| **[Hecho]** | Información verificada o verificable | Afirmaciones con evidencia confidence 4-5, verificada contra fuentes |
| **[Hipótesis]** | Suposición por validar | Afirmaciones derivadas por inferencia sin confirmación directa |
| **[Decisión]** | Elección tomada con contexto y fecha | Cuando la conclusión implica una elección metodológica o de dirección |
| **[Visión]** | Aspiración no comprometida | Implicaciones a largo plazo derivadas de la conclusión |

Al final de cada conclusión, incluir una tabla epistémica que contabilice cuántas afirmaciones corresponden a cada clasificación.

---

## Instrucciones de uso

### Paso 1: Verificar que la investigación tiene evidencia registrada

Antes de formular una conclusión, confirmar que existe al menos una pieza de evidencia registrada en el Source_Register o Evidence_Framework de la investigación. Sin evidencia registrada, no se puede formular una conclusión válida bajo este framework.

### Paso 2: Completar todos los campos obligatorios del Conclusion Record

Copiar el template de entrada (abajo) y completar cada campo. No dejar campos vacíos. Si un campo no aplica (como `contradiction_notes` cuando no hay contradicciones), indicar explícitamente `null` o "No aplica".

Prestar especial atención a:
- **evidence_summary**: Debe contener al menos una referencia válida (EVD-xxx o SRC-xxx).
- **confidence_level**: El nivel asignado debe ser coherente con los confidence levels de la evidencia citada.
- **limitations**: Documentar al menos una limitación, incluso si parece menor.

### Paso 3: Clasificar el tipo de conclusión y completar uncertainty

1. Determinar el tipo de conclusión (`strong_evidence`, `limited_evidence`, `inference`) usando los criterios operativos — no es una elección subjetiva.
2. Completar la sección de uncertainty con al menos un item. Si genuinamente no hay incertidumbres, documentar la justificación.
3. Clasificar cada uncertainty como `reducible`, `irreducible`, o `temporal`.

### Paso 4: Verificar trazabilidad y coherencia

Antes de enviar a review:
- Confirmar que cada `evidence_reference` corresponde a un registro existente.
- Verificar que el confidence_level es coherente con la evidencia (high requiere evidence confidence 4-5).
- Asegurar que el `conclusion_type` refleja objetivamente la fortaleza de la evidencia.
- Revisar que las `recommended_actions` tienen `expected_outcome` definido.

### Paso 5: Asignar clasificación epistémica y enviar a review

Etiquetar cada afirmación con su clasificación epistémica ([Hecho], [Hipótesis], [Decisión], [Visión]). Completar la tabla epistémica. Cambiar el status a `under_review`.

---

## Template de entrada

```markdown
## Conclusión #[número secuencial]

### Metadata

- **Conclusion ID:** CON-[investigation_id]-[seq]
- **Fecha de formulación:** YYYY-MM-DD
- **Status:** draft | under_review | approved | revision_needed | rejected

### Research Question

[Research question que esta conclusión responde, con referencia al identificador o texto completo]

### Evidence Summary

**Síntesis narrativa:**

[Resumen de 1-3 párrafos de la evidencia evaluada]

**Referencias de evidencia:**

- [EVD-xxx-xxx o SRC-xxx-xxx] — [descripción breve del claim soportado]
- [EVD-xxx-xxx o SRC-xxx-xxx] — [descripción breve del claim soportado]

**Total de evidencias consideradas:** [N]

### Confidence Level

- **Nivel:** [high | medium | low]
- **Justificación:** [Explicación de por qué se asigna este nivel, referenciando los confidence levels de la evidencia]
- **Niveles de evidencia de soporte:** [lista de confidence levels, e.g., 4, 4, 3]

### Conclusion Type

- **Tipo:** [strong_evidence | limited_evidence | inference]
- **Declaración de cualificación:** [Obligatoria si el tipo es limited_evidence o inference. Describe el tipo de incertidumbre y su impacto potencial]

### Limitations

- [Limitación 1: alcance, aplicabilidad o generalización]
- [Limitación 2] _(si aplica)_

### Implications

[Cómo esta conclusión afecta el entendimiento del problema original, las decisiones posibles o el curso de acción. 1-3 párrafos.]

### Recommended Actions

| # | Acción | Resultado esperado | Prioridad |
|---|--------|--------------------|-----------|
| 1 | [Descripción de la acción recomendada] | [Qué se espera lograr] | high / medium / low |
| 2 | [Acción adicional] _(si aplica)_ | [Resultado esperado] | high / medium / low |

### Open Questions

- [Pregunta que permanece sin respuesta]
- [Pregunta adicional] _(si aplica)_

### Contradiction Notes

[null si no hay contradicciones con findings previos]

_(Si hay contradicción:)_

- **Finding previo:** [referencia al finding contradecido]
- **Claim previo:** [el claim que se contradice]
- **Claim actual:** [el claim actual]
- **Análisis:** [por qué ocurre la contradicción]
- **Comparación de evidencia:** Previo: [fortaleza]. Actual: [fortaleza].
- **Resolución:** [accept_new | retain_previous | unresolved]

---

### Uncertainty Section

#### Known Unknowns

| # | Descripción | Conclusiones afectadas | Impacto | Clasificación | Acción recomendada |
|---|-------------|------------------------|---------|---------------|-------------------|
| 1 | [Gap identificado] | [CON-xxx] | high/medium/low | reducible/irreducible/temporal | [Acción o null] |

#### Methodological Limitations

| # | Descripción | Conclusiones afectadas | Impacto | Clasificación | Acción recomendada |
|---|-------------|------------------------|---------|---------------|-------------------|
| 1 | [Limitación del método] | [CON-xxx] | high/medium/low | reducible/irreducible/temporal | [Acción o null] |

#### Evidence Gaps

| # | Descripción | Conclusiones afectadas | Impacto | Clasificación | Acción recomendada |
|---|-------------|------------------------|---------|---------------|-------------------|
| 1 | [Evidencia faltante] | [CON-xxx] | high/medium/low | reducible/irreducible/temporal | [Acción o null] |

#### Scope Limitations

| # | Descripción | Conclusiones afectadas | Impacto | Clasificación | Acción recomendada |
|---|-------------|------------------------|---------|---------------|-------------------|
| 1 | [Restricción de alcance] | [CON-xxx] | high/medium/low | reducible/irreducible/temporal | [Acción o null] |

_(Si no hay items en ninguna categoría:)_

**Justificación de zero uncertainties:** [Explicación positiva de por qué no se identificaron incertidumbres]

---

### Epistemic Classification

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho] | [n] | [%] |
| [Decisión] | [n] | [%] |
| [Hipótesis] | [n] | [%] |
| [Visión] | [n] | [%] |
```

---

## Template del documento completo

```markdown
# Conclusions — [Nombre de la Investigación]

> **Investigation ID:** [ID]
> **Fecha:** YYYY-MM-DD
> **Research Questions:** [Número total de questions abordadas]
> **Dominio:** [Dominio de la investigación]

---

## Conclusión #1

[Usar template de entrada completo]

---

## Conclusión #2

[Usar template de entrada completo]

---

## Resumen de conclusiones

| # | Research Question | Tipo | Confidence | Uncertainties |
|---|-------------------|------|------------|---------------|
| 1 | [RQ resumida] | strong_evidence / limited_evidence / inference | high / medium / low | [N items] |
| 2 | [RQ resumida] | [tipo] | [nivel] | [N items] |

## Resumen de uncertainty consolidado

| Categoría | Total items | High impact | Medium impact | Low impact |
|-----------|-------------|-------------|---------------|------------|
| Known unknowns | [n] | [n] | [n] | [n] |
| Methodological limitations | [n] | [n] | [n] | [n] |
| Evidence gaps | [n] | [n] | [n] | [n] |
| Scope limitations | [n] | [n] | [n] | [n] |

| Clasificación epistémica | Reducible | Irreducible | Temporal |
|--------------------------|-----------|-------------|----------|
| Total | [n] | [n] | [n] |

## Tabla epistémica global

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho] | [n] | [%] |
| [Decisión] | [n] | [%] |
| [Hipótesis] | [n] | [%] |
| [Visión] | [n] | [%] |
```

---

## Ejemplo completo

El siguiente ejemplo muestra una conclusión realista de una investigación sobre selección de herramientas de análisis de datos para LabOS.

```markdown
# Conclusions — Evaluación de Herramientas de Análisis de Datos

> **Investigation ID:** INV-2025-007
> **Fecha:** 2025-02-10
> **Research Questions:** 2
> **Dominio:** Technical

---

## Conclusión #1

### Metadata

- **Conclusion ID:** CON-INV-2025-007-001
- **Fecha de formulación:** 2025-02-10
- **Status:** approved

### Research Question

RQ-1: ¿Qué herramienta de análisis de datos ofrece la mejor combinación de reproducibilidad, colaboración y compatibilidad con el stack técnico de LabOS para investigaciones cuantitativas?

### Evidence Summary

**Síntesis narrativa:**

Se evaluaron 4 herramientas de análisis de datos (Deepnote, Jupyter local, Google Colab, Observable) contra 6 criterios ponderados: reproducibilidad, colaboración, integración con GitHub, soporte para Python/R, capacidad de visualización, y costo operativo. [Hecho]

Deepnote obtuvo la puntuación más alta en 4 de 6 criterios (reproducibilidad, colaboración, integración con GitHub, soporte Python). Jupyter local superó en control total del entorno pero falló en colaboración. Google Colab tuvo limitaciones en reproducibilidad por dependencia de sesiones efímeras. Observable no soporta Python nativamente. [Hecho]

La evaluación se basó en pruebas directas de cada herramienta durante 2 sesiones de 2 horas cada una, complementadas con documentación oficial y 2 reviews independientes publicados en 2024.

**Referencias de evidencia:**

- EVD-INV-2025-007-001 — Benchmark de reproducibilidad: Deepnote mantiene estado entre sesiones sin pérdida (confidence: 4)
- EVD-INV-2025-007-003 — Documentación oficial de Deepnote sobre integración con GitHub (confidence: 5)
- EVD-INV-2025-007-005 — Review independiente de DataScienceWeekly comparando notebooks en la nube (confidence: 4)
- SRC-INV-2025-007-008 — Review de TowardsDataScience sobre colaboración en notebooks (confidence: 4)

**Total de evidencias consideradas:** 8

### Confidence Level

- **Nivel:** high
- **Justificación:** La conclusión se basa en 4 piezas de evidencia con confidence levels 4-5, provenientes de fuentes independientes (benchmark propio, documentación oficial, y 2 reviews de publicaciones distintas sin relación editorial entre sí). La convergencia de evidencia directa e independiente soporta un nivel alto de confianza.
- **Niveles de evidencia de soporte:** [4, 5, 4, 4]

### Conclusion Type

- **Tipo:** strong_evidence
- **Declaración de cualificación:** N/A (strong_evidence no requiere cualificación)

### Limitations

- Evaluación limitada a las necesidades actuales de LabOS (investigaciones cuantitativas con Python). No aplica a necesidades futuras no identificadas.
- Las pruebas se realizaron con el plan gratuito de Deepnote. Funcionalidades de planes pagos no fueron evaluadas.
- No se evaluó el rendimiento con datasets >1GB, que podrían requerir infraestructura diferente.

### Implications

Deepnote es la herramienta óptima para análisis cuantitativo dentro de LabOS en su configuración actual. [Decisión] Esto permite estandarizar los notebooks de investigación en una sola plataforma, reduciendo fricción de onboarding y facilitando la reproducibilidad entre investigaciones de distintos labs. La integración nativa con GitHub permite que los notebooks se versionen junto con el resto de la documentación del package.

### Recommended Actions

| # | Acción | Resultado esperado | Prioridad |
|---|--------|--------------------|-----------|
| 1 | Adoptar Deepnote como herramienta estándar para análisis cuantitativo en investigaciones LabOS | Estandarización de workflows de análisis, reproducibilidad garantizada entre sesiones | high |
| 2 | Configurar integración Deepnote-GitHub para el repositorio LabOS | Versionado automático de notebooks junto con documentación | high |
| 3 | Documentar guía de uso de Deepnote específica para contexto LabOS | Reducción de tiempo de setup para nuevas investigaciones cuantitativas | medium |

### Open Questions

- ¿Cuál es el límite de rendimiento de Deepnote con datasets grandes (>1GB)?
- ¿El plan gratuito será suficiente a medida que aumente el volumen de investigaciones?
- ¿Cómo se manejarán notebooks que requieran librerías con dependencias de sistema no disponibles en Deepnote?

### Contradiction Notes

null

---

### Uncertainty Section

#### Known Unknowns

| # | Descripción | Conclusiones afectadas | Impacto | Clasificación | Acción recomendada |
|---|-------------|------------------------|---------|---------------|-------------------|
| 1 | Comportamiento de Deepnote con datasets >1GB no evaluado | CON-INV-2025-007-001 | medium | reducible | Ejecutar benchmark con dataset de 2GB en próxima investigación cuantitativa |

#### Methodological Limitations

| # | Descripción | Conclusiones afectadas | Impacto | Clasificación | Acción recomendada |
|---|-------------|------------------------|---------|---------------|-------------------|
| 1 | Evaluación realizada solo con plan gratuito; features de planes pagos no consideradas | CON-INV-2025-007-001 | low | reducible | Evaluar plan Team si el uso crece significativamente |
| 2 | Sesiones de prueba de 2h por herramienta pueden no capturar problemas que emergen con uso prolongado | CON-INV-2025-007-001 | medium | temporal | Reevaluar después de 3 meses de uso real |

#### Evidence Gaps

| # | Descripción | Conclusiones afectadas | Impacto | Clasificación | Acción recomendada |
|---|-------------|------------------------|---------|---------------|-------------------|
| 1 | No se encontraron benchmarks independientes de rendimiento para datasets grandes en Deepnote | CON-INV-2025-007-001 | medium | reducible | Buscar o producir benchmarks propios en Q2 |

#### Scope Limitations

| # | Descripción | Conclusiones afectadas | Impacto | Clasificación | Acción recomendada |
|---|-------------|------------------------|---------|---------------|-------------------|
| 1 | Conclusión aplica exclusivamente a análisis cuantitativo con Python; no cubre análisis cualitativo ni otros lenguajes | CON-INV-2025-007-001 | low | irreducible | null |

---

### Epistemic Classification

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho] | 3 | 43% |
| [Decisión] | 3 | 43% |
| [Hipótesis] | 0 | 0% |
| [Visión] | 1 | 14% |

---

## Resumen de conclusiones

| # | Research Question | Tipo | Confidence | Uncertainties |
|---|-------------------|------|------------|---------------|
| 1 | Herramienta óptima para análisis cuantitativo | strong_evidence | high | 5 items |

## Resumen de uncertainty consolidado

| Categoría | Total items | High impact | Medium impact | Low impact |
|-----------|-------------|-------------|---------------|------------|
| Known unknowns | 1 | 0 | 1 | 0 |
| Methodological limitations | 2 | 0 | 1 | 1 |
| Evidence gaps | 1 | 0 | 1 | 0 |
| Scope limitations | 1 | 0 | 0 | 1 |

| Clasificación epistémica | Reducible | Irreducible | Temporal |
|--------------------------|-----------|-------------|----------|
| Total | 3 | 1 | 1 |

## Tabla epistémica global

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho] | 3 | 43% |
| [Decisión] | 3 | 43% |
| [Hipótesis] | 0 | 0% |
| [Visión] | 1 | 14% |
```

---

## Reglas operativas

1. **Completitud obligatoria:** No se permite formular una conclusión con campos vacíos. Si un campo no aplica, indicar explícitamente `null` o "No aplica".
2. **Trazabilidad verificable:** Toda `evidence_reference` debe corresponder a un registro existente y accesible en el Source_Register o Evidence_Framework.
3. **Coherencia de confidence:** El confidence_level de la conclusión debe ser coherente con los niveles de la evidencia que la soporta (high requiere evidence 4-5, medium requiere 3, low corresponde a 1-2).
4. **Clasificación objetiva:** El `conclusion_type` se determina por criterios operativos, no por preferencia del investigador.
5. **No presentación definitiva:** Conclusiones `limited_evidence` o `inference` nunca se presentan como definitivas o confirmadas.
6. **Uncertainty obligatoria:** Toda conclusión incluye sección de uncertainty. Zero uncertainties requiere justificación explícita.
7. **Paridad de inconclusos:** Resultados inconclusos se documentan con exactamente el mismo rigor que conclusiones positivas.

---

## Referencias

- [017-conclusion-framework.md](../../packages/package-001-research-methodology/017-conclusion-framework.md) — Definición completa del Conclusion Framework, tipos, reglas y uncertainty
- [006-evidence-framework.md](../../packages/package-001-research-methodology/006-evidence-framework.md) — Categorías de evidencia, escala de confianza 1-5, Evidence Record
- [007-source-evaluation.md](../../packages/package-001-research-methodology/007-source-evaluation.md) — Criterios de evaluación de fuentes, IDs válidos
- [002-research-lifecycle.md](../../packages/package-001-research-methodology/002-research-lifecycle.md) — Etapa 11 (Conclusion) del lifecycle
