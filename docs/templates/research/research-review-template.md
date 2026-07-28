# Research Review Template

## Propósito

Template para ejecutar la revisión final de una investigación antes de su aceptación como conocimiento validado. Evalúa calidad, completitud y cumplimiento mediante un checklist de 8 ítems, documenta deficiencias con acciones de remediación, y registra la aprobación formal del revisor.

Este template implementa el quality gate de la etapa Review del Research_Lifecycle, garantizando que ninguna investigación se archive sin verificación humana de sus conclusiones y evidencia.

---

## Campos requeridos — Encabezado

| # | Campo | Tipo | Descripción | Formato |
|---|-------|------|-------------|---------|
| 1 | **investigation_name** | string | Nombre de la investigación bajo revisión | Texto descriptivo (≤120 caracteres) |
| 2 | **investigation_id** | string | Identificador único de la investigación | Patrón: INV-YYYY-NNN |
| 3 | **review_date** | string | Fecha en que se ejecuta la revisión | ISO 8601 (YYYY-MM-DD) |
| 4 | **reviewer** | string | Identidad del revisor | Nombre completo o rol |
| 5 | **review_cycle** | integer | Número de ciclo de revisión actual | 1-3 (máximo 3 ciclos permitidos) |

---

## Checklist de revisión (8 ítems — R25.1)

Cada ítem se evalúa como **pass** o **fail**. Todos los ítems deben evaluarse — no se permite dejar ítems sin evaluar.

| # | Ítem | Criterio de evaluación | Resultado |
|---|------|------------------------|-----------|
| 1 | **Pregunta de investigación respondida** | La conclusión responde explícitamente la research question con una afirmación clara | pass / fail |
| 2 | **≥3 ítems de evidencia independientes** | Al menos 3 piezas de evidencia independientes soportan la conclusión | pass / fail |
| 3 | **Fuentes verificadas** | Todas las fuentes citadas son accesibles y con fecha dentro de 5 años (excepto contexto histórico justificado) | pass / fail |
| 4 | **Trazabilidad conclusión → evidencia** | Cada conclusión traza a ítems de evidencia específicos por referencia explícita | pass / fail |
| 5 | **Incertidumbres documentadas** | Incertidumbres y nivel de confianza (high/medium/low) documentados para cada conclusión | pass / fail |
| 6 | **≥1 activo extraído** | Al menos un Research_Asset extraído y registrado, o ausencia justificada | pass / fail |
| 7 | **Limitaciones documentadas** | Limitaciones de alcance y método explícitamente declaradas | pass / fail |
| 8 | **Cumplimiento ético** | Cumplimiento verificado con las directrices éticas y de privacidad del proyecto | pass / fail |

### Reglas de clasificación

| Condición | Clasificación resultante |
|-----------|--------------------------|
| 8/8 ítems pass | **Completed** — investigación aceptada como conocimiento validado |
| ≥6/8 ítems pass + fallos documentados como limitaciones aceptables | **Completed-with-limitations** — aceptada con observaciones |
| <6/8 ítems pass o ciclos de remediación agotados | **Abandoned** — requiere rationale documentado |

---

## Detalle de evaluación por ítem

Para cada ítem del checklist, documentar la evidencia de la evaluación:

```markdown
### Ítem [#]: [Nombre del ítem]

- **Resultado:** pass / fail
- **Evidencia de evaluación:** [Descripción de qué se verificó y cómo]
- **Notas:** [Observaciones adicionales, si aplica]
```

---

## Campos opcionales

| Campo | Descripción | Cuándo usar |
|-------|-------------|-------------|
| **previous_review_date** | Fecha de la revisión anterior | Cuando review_cycle > 1 |
| **domain_notes** | Observaciones específicas del dominio | Cuando el dominio tiene particularidades de evidencia |
| **time_spent_review** | Tiempo invertido en la revisión (minutos) | Para tracking de esfuerzo de revisión |
| **priority_items** | Ítems que requieren atención inmediata | Cuando hay deficiencias críticas |

---

## Remediación (R25.2)

Cuando uno o más ítems del checklist resultan en **fail**, se requiere una entrada de remediación por cada ítem fallido.

### Campos de remediación

| # | Campo | Tipo | Descripción | Restricciones |
|---|-------|------|-------------|---------------|
| 1 | **section** | string | Sección de la investigación con la deficiencia | Referencia al documento y sección específica |
| 2 | **corrective_action** | string | Acción correctiva requerida | Descripción verificable de qué debe hacerse |
| 3 | **responsible** | string | Persona responsable de ejecutar la corrección | Nombre o rol asignado |
| 4 | **target_date** | string | Fecha límite para resolver la deficiencia | ISO 8601 (YYYY-MM-DD), máximo 30 días calendario desde la fecha de revisión |

### Reglas de remediación

- Máximo **3 ciclos de remediación** por investigación.
- Si tras 3 ciclos los ítems fallidos persisten, la investigación se clasifica como **abandoned** o **completed-with-limitations**.
- El `target_date` no puede exceder **30 días calendario** desde la fecha de revisión.
- Cada ítem fail debe tener exactamente una entrada de remediación asociada.

### Template de entrada de remediación

```markdown
#### Remediación — Ítem [#]

- **Section:** [Documento/sección con deficiencia]
- **Corrective action:** [Descripción de la acción correctiva]
- **Responsible:** [Nombre o rol]
- **Target date:** YYYY-MM-DD
```

---

## Sign-off (R14.1)

El sign-off es obligatorio para que una investigación sea aceptada como conocimiento validado. El revisor debe haber leído la conclusión y verificado que las claims están soportadas por evidencia citada.

| # | Campo | Tipo | Descripción | Valores válidos |
|---|-------|------|-------------|-----------------|
| 1 | **reviewer** | string | Identidad del revisor | Nombre completo |
| 2 | **date** | string | Fecha del sign-off | ISO 8601 (YYYY-MM-DD) |
| 3 | **result** | enum | Resultado de la revisión | `approved` / `revision-needed` / `rejected` |

### Significado de cada resultado

| Resultado | Significado | Acción siguiente |
|-----------|-------------|------------------|
| **approved** | Todos los ítems pass. Investigación aceptada como conocimiento validado. | Proceder a Asset Extraction y archivo. |
| **revision-needed** | ≥1 ítem fail con posibilidad de remediación. | Ejecutar acciones correctivas y re-evaluar (nuevo ciclo). |
| **rejected** | Deficiencias fundamentales que invalidan la investigación. | Clasificar como abandoned. Documentar rationale. |

### Template de sign-off

```markdown
## Sign-off

| Campo | Valor |
|-------|-------|
| **Reviewer** | [Nombre completo] |
| **Date** | YYYY-MM-DD |
| **Result** | approved / revision-needed / rejected |
| **Comments** | [Observaciones del revisor, si aplica] |
```

---

## [DOMAIN-SPECIFIC] Secciones por dominio

Agregar criterios de verificación adicionales según el dominio de investigación:

| Dominio | Verificaciones adicionales sugeridas |
|---------|--------------------------------------|
| Technical | Verificar reproducibilidad (environment, tools, versions documentados) |
| Quantitative | Verificar que datos y cálculos son replicables, métodos estadísticos apropiados |
| Market | Verificar que demand signals son externos y verificables |
| Creative | Verificar que IP/licensing está documentado para todos los assets |
| Regulated (finance, health) | Verificar cumplimiento regulatorio explícito y aprobación adicional |

---

## Instrucciones de uso

### Paso 1: Preparar la revisión

Antes de iniciar la revisión, reunir los artefactos de la investigación: conclusión, Source_Register, Research_Journal, y cualquier asset extraído. Copiar este template y completar el encabezado con los datos de la investigación. Verificar que la investigación ha completado la etapa de Conclusion antes de iniciar Review.

### Paso 2: Evaluar cada ítem del checklist

Evaluar los 8 ítems del checklist secuencialmente. Para cada ítem, documentar qué evidencia se revisó y la justificación del resultado (pass/fail). No dejar ítems sin evaluar — si un ítem no aplica por razones del dominio, marcarlo como pass con nota explicativa.

### Paso 3: Documentar remediaciones para ítems fallidos

Para cada ítem marcado como fail, crear una entrada de remediación con los 4 campos requeridos (section, corrective action, responsible, target date). Asegurarse de que las acciones correctivas son específicas y verificables — no usar descripciones vagas como "mejorar la sección".

### Paso 4: Registrar el sign-off

Completar la sección de sign-off con el resultado de la revisión (approved, revision-needed, o rejected). Si el resultado es revision-needed, las remediaciones documentadas en el Paso 3 definen el trabajo pendiente para el siguiente ciclo. Si el resultado es approved, la investigación puede proceder a Asset Extraction.

### Paso 5: Re-evaluar tras remediación (si aplica)

Si la revisión anterior resultó en revision-needed, incrementar el review_cycle, evaluar únicamente los ítems previamente fallidos, y registrar un nuevo sign-off. Repetir hasta que todos los ítems pasen (máximo 3 ciclos totales).

---

## Template del documento completo

```markdown
# Research Review — [Nombre de la Investigación]

> **Investigation ID:** [ID de la investigación]
> **Review date:** YYYY-MM-DD
> **Reviewer:** [Nombre del revisor]
> **Review cycle:** [1 | 2 | 3]

---

## Checklist de revisión

| # | Ítem | Resultado | Notas |
|---|------|-----------|-------|
| 1 | Pregunta de investigación respondida | pass / fail | [notas] |
| 2 | ≥3 ítems de evidencia independientes | pass / fail | [notas] |
| 3 | Fuentes verificadas | pass / fail | [notas] |
| 4 | Trazabilidad conclusión → evidencia | pass / fail | [notas] |
| 5 | Incertidumbres documentadas | pass / fail | [notas] |
| 6 | ≥1 activo extraído | pass / fail | [notas] |
| 7 | Limitaciones documentadas | pass / fail | [notas] |
| 8 | Cumplimiento ético | pass / fail | [notas] |

**Total pass:** [N] / 8

---

## Detalle de evaluación

### Ítem 1: Pregunta de investigación respondida

- **Resultado:** pass / fail
- **Evidencia de evaluación:** [qué se verificó]
- **Notas:** [observaciones]

### Ítem 2: ≥3 ítems de evidencia independientes

- **Resultado:** pass / fail
- **Evidencia de evaluación:** [qué se verificó]
- **Notas:** [observaciones]

[... repetir para ítems 3-8 ...]

---

## Remediación

### Remediación — Ítem [#]

- **Section:** [documento/sección]
- **Corrective action:** [acción correctiva]
- **Responsible:** [responsable]
- **Target date:** YYYY-MM-DD

[... repetir por cada ítem fail ...]

---

## Sign-off

| Campo | Valor |
|-------|-------|
| **Reviewer** | [Nombre completo] |
| **Date** | YYYY-MM-DD |
| **Result** | approved / revision-needed / rejected |
| **Comments** | [Observaciones] |

---

## Clasificación final

| Campo | Valor |
|-------|-------|
| **Classification** | completed / completed-with-limitations / abandoned |
| **Rationale** | [Justificación de la clasificación, si no es "completed"] |
```

---

## Ejemplo completo

El siguiente ejemplo muestra un Research Review realista de una investigación sobre frameworks de evaluación de evidencia, con un ítem fallido y su remediación.

```markdown
# Research Review — Evidence Evaluation Frameworks Comparison

> **Investigation ID:** INV-2025-003
> **Review date:** 2025-01-22
> **Reviewer:** Juan Diego (Fundador)
> **Review cycle:** 1

---

## Checklist de revisión

| # | Ítem | Resultado | Notas |
|---|------|-----------|-------|
| 1 | Pregunta de investigación respondida | pass | Conclusión responde "¿Qué framework de evaluación de evidencia se adapta mejor a los dominios heterogéneos de LabOS?" |
| 2 | ≥3 ítems de evidencia independientes | pass | 5 fuentes independientes soportan la conclusión (Smith 2022, Lee 2023, GRADE framework, Evidence-Based Practice Guidelines, ISO 9001 annex) |
| 3 | Fuentes verificadas | pass | 5/5 fuentes accesibles. Fecha más antigua: Smith 2022 (dentro de 5 años) |
| 4 | Trazabilidad conclusión → evidencia | pass | Cada claim en la conclusión referencia source IDs específicos (SRC-001 a SRC-005) |
| 5 | Incertidumbres documentadas | pass | 3 incertidumbres documentadas con clasificación (1 reducible, 1 temporal, 1 irreducible) y nivel de confianza medium |
| 6 | ≥1 activo extraído | pass | Asset extraído: "Evidence Evaluation Framework v1.0" (Knowledge Asset, estado: draft) |
| 7 | Limitaciones documentadas | fail | Falta documentar limitación de que el framework no ha sido probado en dominio Creative |
| 8 | Cumplimiento ético | pass | Sin datos personales. Sin contenido regulado. Sin conflictos de IP. |

**Total pass:** 7 / 8

---

## Detalle de evaluación

### Ítem 1: Pregunta de investigación respondida

- **Resultado:** pass
- **Evidencia de evaluación:** Sección "Conclusión" del documento 006-evidence-framework.md contiene respuesta explícita a la research question declarada en el Research Brief.
- **Notas:** La conclusión recomienda un framework combinado (Smith + Lee + adaptaciones propias) como el más adecuado.

### Ítem 2: ≥3 ítems de evidencia independientes

- **Resultado:** pass
- **Evidencia de evaluación:** Source_Register contiene 5 fuentes con scores ≥6/10 (SRC-001: 8.2, SRC-002: 7.5, SRC-003: 7.0, SRC-004: 6.5, SRC-005: 6.0). Las 5 son independientes entre sí (autores distintos, publicaciones distintas).
- **Notas:** 2 fuentes adicionales descartadas por score <6.

### Ítem 3: Fuentes verificadas

- **Resultado:** pass
- **Evidencia de evaluación:** Verifiqué accesibilidad de las 5 fuentes citadas el 2025-01-22. Todas accesibles. Rango de fechas: 2020-2023.
- **Notas:** Sin fuentes históricas que requieran excepción.

### Ítem 4: Trazabilidad conclusión → evidencia

- **Resultado:** pass
- **Evidencia de evaluación:** La sección de conclusiones contiene referencias explícitas (SRC-001, SRC-002, etc.) para cada afirmación. Se verificó que cada referencia existe en el Source_Register.
- **Notas:** Trazabilidad bidireccional correcta.

### Ítem 5: Incertidumbres documentadas

- **Resultado:** pass
- **Evidencia de evaluación:** Sección "Uncertainty" documenta 3 incertidumbres: (1) aplicabilidad a dominios creativos — reducible, (2) evolución de frameworks académicos — temporal, (3) subjetividad inherente en scoring — irreducible. Nivel de confianza: medium.
- **Notas:** Cada incertidumbre tiene impact assessment.

### Ítem 6: ≥1 activo extraído

- **Resultado:** pass
- **Evidencia de evaluación:** Asset "Evidence Evaluation Framework v1.0" registrado en assets/knowledge/ con metadata header referenciando INV-2025-003.
- **Notas:** Estado: draft. Pendiente de revisión para transición a complete.

### Ítem 7: Limitaciones documentadas

- **Resultado:** fail
- **Evidencia de evaluación:** La sección "Limitations" documenta limitaciones de método (solo fuentes en inglés) y de alcance (3 dominios evaluados). Sin embargo, NO documenta la limitación de cobertura para el dominio Creative, que fue identificada en las incertidumbres pero no en limitaciones.
- **Notas:** Inconsistencia entre sección de uncertainty y sección de limitations.

### Ítem 8: Cumplimiento ético

- **Resultado:** pass
- **Evidencia de evaluación:** Investigación no involucra datos personales, clientes, ni contenido regulado. Fuentes utilizadas tienen licencias compatibles con uso interno documentado.
- **Notas:** Sin issues éticos identificados.

---

## Remediación

### Remediación — Ítem 7

- **Section:** 006-evidence-framework.md → Sección "Limitations"
- **Corrective action:** Agregar limitación explícita indicando que el framework no ha sido validado en dominio Creative, referenciando la incertidumbre documentada sobre aplicabilidad a dominios creativos. Incluir impacto y recomendación de validación futura.
- **Responsible:** Juan Diego (Fundador)
- **Target date:** 2025-02-05

---

## Sign-off

| Campo | Valor |
|-------|-------|
| **Reviewer** | Juan Diego |
| **Date** | 2025-01-22 |
| **Result** | revision-needed |
| **Comments** | Investigación sólida. Una deficiencia menor en documentación de limitaciones. Se espera resolución en 1 ciclo de remediación. |

---

## Clasificación final

| Campo | Valor |
|-------|-------|
| **Classification** | Pendiente — en espera de remediación (ciclo 2) |
| **Rationale** | 7/8 ítems pass. Se espera que tras la remediación del ítem 7, la investigación alcance 8/8 y sea clasificada como "completed". |
```

---

## Referencias

- [020-quality-gates.md](../../packages/package-001-research-methodology/020-quality-gates.md) — Definición de quality gates del lifecycle
- [002-research-lifecycle.md](../../packages/package-001-research-methodology/002-research-lifecycle.md) — Etapa Review y sus criterios
- [017-conclusion-framework.md](../../packages/package-001-research-methodology/017-conclusion-framework.md) — Estructura de conclusiones evaluadas en la revisión
- [006-evidence-framework.md](../../packages/package-001-research-methodology/006-evidence-framework.md) — Framework de evidencia contra el cual se verifica trazabilidad
