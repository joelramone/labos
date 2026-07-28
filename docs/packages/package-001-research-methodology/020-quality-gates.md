# 020 — Quality Gates

> **Etiqueta epistémica:** [Decisión]
>
> **Requirements cubiertos:** R29.1, R29.2, R29.3, R29.4, R29.5, R14.1, R14.2, R14.3, R14.4, R14.5

## Propósito

Este documento define los **7 quality gates** del Research_Lifecycle de LabOS. Cada gate es un punto de control con criterios explícitos que una investigación debe superar para avanzar a la siguiente fase. Los gates garantizan rigor, trazabilidad y previenen el avance sin evidencia o documentación suficiente.

Los gates integran **human review obligatorio** en puntos críticos y definen un **alternative evidence path** para dominios donde la experimentación controlada no es factible.

---

## Tabla de contenidos

1. [Principios generales](#principios-generales)
2. [Gate 1: Initiate — Gate de inicio de investigación](#gate-1-initiate--gate-de-inicio-de-investigación)
3. [Gate 2: Experiment — Gate de inicio de experimentos](#gate-2-experiment--gate-de-inicio-de-experimentos)
4. [Gate 3: Findings — Gate de aceptación de hallazgos](#gate-3-findings--gate-de-aceptación-de-hallazgos)
5. [Gate 4: Conclusions — Gate de aprobación de conclusiones](#gate-4-conclusions--gate-de-aprobación-de-conclusiones)
6. [Gate 5: Assets — Gate de extracción de activos](#gate-5-assets--gate-de-extracción-de-activos)
7. [Gate 6: Publish — Gate de publicación externa](#gate-6-publish--gate-de-publicación-externa)
8. [Gate 7: Commercial — Gate de utilización comercial](#gate-7-commercial--gate-de-utilización-comercial)
9. [Reglas de remediación](#reglas-de-remediación)
10. [Alternative evidence path](#alternative-evidence-path)
11. [Human review requirements](#human-review-requirements)
12. [Resumen de gates](#resumen-de-gates)

---

## Principios generales

1. **Binario:** Cada gate tiene un resultado pass/fail. No hay estados intermedios.
2. **Documentado:** El resultado de cada evaluación se registra con fecha, evaluador y evidencia.
3. **Remediable:** Un fail no es permanente — se permite remediación dentro de límites definidos.
4. **Trazable:** Cada criterio de evaluación es verificable por un tercero sin juicio subjetivo.
5. **Responsable:** El Fundador es responsable de todos los gates en la etapa actual de LabOS.

---

## Gate 1: Initiate — Gate de inicio de investigación

| Campo | Valor |
|-------|-------|
| **Nombre** | Initiate |
| **Posición en lifecycle** | Transición de Planned → In Progress (entre etapas 5 y 6) |
| **Responsable** | Fundador |

### Required inputs

- Research_Brief completo (con todos los campos obligatorios según effort category)
- Research questions formuladas y evaluadas contra criterios de calidad
- Scope definido con timebox, deadline y exclusiones
- Assumptions documentadas (≥1 o justificación de ausencia)

### Evaluation criteria (checklist)

| # | Criterio | Verificación |
|---|----------|-------------|
| 1 | Research_Brief existe con trigger, context, requester, expected value, domain classification, effort category | Campos no vacíos en el documento |
| 2 | ≥1 research question formulada con subject, scope boundary, constraints, answer type, verification method | Estructura completa verificable |
| 3 | Scope incluye inclusiones, exclusiones, timebox (1-40h), deadline (YYYY-MM-DD), y completion criteria | Campos presentes con valores válidos |
| 4 | Assumptions documentadas con statement, confidence, basis, impact-if-wrong, validation approach | ≥1 assumption o justificación explícita de ausencia |
| 5 | Research type declarado con justificación (1-2 oraciones) | Campo presente en Research_Brief |

### Pass/fail

- **Pass:** Los 5 criterios evaluados como cumplidos.
- **Fail:** ≥1 criterio evaluado como no cumplido.

### Fail actions

1. Identificar criterios fallidos específicos.
2. Documentar deficiencia con referencia al campo o sección faltante.
3. Asignar remediación al Fundador con deadline ≤30 días.
4. Bloquear avance a Source Collection hasta resolución.

---

## Gate 2: Experiment — Gate de inicio de experimentos

| Campo | Valor |
|-------|-------|
| **Nombre** | Experiment |
| **Posición en lifecycle** | Transición de Analysis → Experimentation (entre etapas 8 y 9) |
| **Responsable** | Fundador |

### Required inputs

- Hipótesis formulada con todos los campos requeridos (assertion, prior evidence, variables, validation method, success/failure criteria, time limit)
- Protocolo de experimento documentado
- Evidence register con ≥1 evidencia que soporta la hipótesis

### Evaluation criteria (checklist)

| # | Criterio | Verificación |
|---|----------|-------------|
| 1 | Hipótesis con ID único (HYP-[type]-[seq]), assertion ≤280 chars, prior evidence, variables, success criterion, failure criterion, time limit | Campos completos en hypothesis record |
| 2 | Protocolo de experimento incluye: independent variables, dependent variables, controlled variables, method, success/failure criteria numéricos, time limit ≤90 días, resources, expected data format | Documento de protocolo verificable |
| 3 | Experimento clasificado como research experiment o commercial validation experiment | Campo de clasificación presente |
| 4 | Riesgos documentados con ≥1 riesgo identificado y mitigación propuesta | Sección de riesgos no vacía |
| 5 | Si el dominio no permite experimentación controlada: alternative evidence path documentado (ver sección dedicada) | Justificación presente o N/A si experimentación es factible |

### Pass/fail

- **Pass:** Los 5 criterios evaluados como cumplidos (criterio 5 es N/A si experimentación controlada es factible).
- **Fail:** ≥1 criterio evaluado como no cumplido.

### Fail actions

1. Identificar criterios fallidos.
2. Si falta hipótesis completa: regresar a etapa de Analysis para completar formulación.
3. Si falta protocolo: documentar protocolo antes de ejecutar experimento.
4. Asignar remediación con deadline ≤30 días.
5. Bloquear ejecución de experimento hasta resolución.

---

## Gate 3: Findings — Gate de aceptación de hallazgos

| Campo | Valor |
|-------|-------|
| **Nombre** | Findings |
| **Posición en lifecycle** | Transición de Findings → Conclusion (entre etapas 10 y 11) |
| **Responsable** | Fundador |

### Required inputs

- Findings document consolidado
- Evidence register con evidencia clasificada y evaluada
- Source Register con fuentes evaluadas contra 10 dimensiones
- Experiment records (si aplica) con resultados documentados

### Evaluation criteria (checklist)

| # | Criterio | Verificación |
|---|----------|-------------|
| 1 | Cada research question tiene ≥1 finding asociado (incluyendo "insuficiente evidencia" como finding válido) | Mapeo verificable question → finding |
| 2 | Cada finding tiene: classification (positive/negative/inconclusive), confidence level (1-5), evidence category, supporting references | Campos completos por finding |
| 3 | Conflictos entre evidencias documentados con claims, análisis de discrepancia, y resolución | Sección de conflictos presente (o declaración de ausencia) |
| 4 | Resultados negativos e inconclusos documentados con el mismo rigor que positivos | Todos los resultados siguen la misma estructura |
| 5 | Verification status asignado a cada resultado: preliminary, confirmed, o contested | Campo presente por resultado |

### Pass/fail

- **Pass:** Los 5 criterios evaluados como cumplidos.
- **Fail:** ≥1 criterio evaluado como no cumplido.

### Fail actions

1. Identificar findings incompletos o research questions sin cobertura.
2. Si faltan findings: regresar a etapa de Analysis o Experimentation según corresponda.
3. Si faltan campos en findings existentes: completar documentación.
4. Asignar remediación con deadline ≤30 días.
5. Bloquear formulación de conclusiones hasta resolución.

---

## Gate 4: Conclusions — Gate de aprobación de conclusiones

| Campo | Valor |
|-------|-------|
| **Nombre** | Conclusions |
| **Posición en lifecycle** | Transición de Conclusion → Review → Completed (entre etapas 11 y 12) |
| **Responsable** | Fundador |

### Required inputs

- Conclusion document con todos los campos requeridos
- Evidence summary con referencias verificables
- Uncertainty section documentada
- Findings trazables a la conclusión

### Evaluation criteria (checklist)

| # | Criterio | Verificación |
|---|----------|-------------|
| 1 | Conclusión responde explícitamente a la research question con: evidence summary, confidence level (high/medium/low con justificación), limitations, implications, ≥1 recommended action, open questions | Campos completos en conclusion document |
| 2 | Toda conclusión traza a ≥1 evidencia registrada en Source_Register o Evidence_Framework | Referencias verificables presentes |
| 3 | Conclusiones clasificadas correctamente: strong evidence (≥2 fuentes independientes confidence 4-5), limited evidence (single source o confidence 1-3), inference (derivación lógica sin fuente directa) | Clasificación presente y coherente con evidencia citada |
| 4 | Uncertainty section presente con: known unknowns, methodological limitations, evidence gaps, scope limitations, areas for further investigation — cada ítem con description, affected conclusion(s), impact assessment (high/medium/low) | Sección no vacía con estructura completa |
| 5 | **Human review completado** (ver sección Human Review Requirements): reviewer identity, date, review result (approved/revision-needed/rejected), findings verification | Registro de human review firmado |

### Pass/fail

- **Pass:** Los 5 criterios evaluados como cumplidos, incluyendo human review aprobado.
- **Fail:** ≥1 criterio evaluado como no cumplido, O human review con resultado "revision-needed" o "rejected".

### Fail actions

1. Si human review identifica deficiencias: documentar remediation actions con deficiency, corrective action, responsible party, target date ≤30 días.
2. Si conclusión no traza a evidencia: identificar gaps y regresar a findings si necesario.
3. Si uncertainty section está vacía: requerir justificación explícita (sujeta a verificación en human review).
4. Bloquear aceptación como validated knowledge hasta resolución.
5. Si human review resulta "rejected": requiere reformulación completa de la conclusión.

---

## Gate 5: Assets — Gate de extracción de activos

| Campo | Valor |
|-------|-------|
| **Nombre** | Assets |
| **Posición en lifecycle** | Transición de Completed → Converted to Asset (entre etapas 12 y 13) |
| **Responsable** | Fundador |

### Required inputs

- Investigación con status "Completed" (Gate 4 aprobado)
- ≥1 Research_Asset identificado para extracción
- Metadata del asset preparada

### Evaluation criteria (checklist)

| # | Criterio | Verificación |
|---|----------|-------------|
| 1 | Asset tiene: name (≤80 chars), type (Knowledge/Technical/Educational/Commercial/Data), description (1-3 oraciones), usage hypothesis, target audience, source investigation reference, initial state = "draft" | Campos completos en asset record |
| 2 | Asset colocado en la carpeta correspondiente del assets repository (`assets/{type}/`) | Archivo existe en ubicación correcta |
| 3 | Asset incluye metadata header referencing source investigation identifier | Header presente con ID de investigación |
| 4 | Extracción registrada en conclusion document con nombre del asset y ubicación en repository | Referencia cruzada presente en conclusion |
| 5 | Asset es self-contained: utilizable sin requerir acceso a la investigación fuente | Revisión de contenido confirma independencia |

### Pass/fail

- **Pass:** Los 5 criterios evaluados como cumplidos.
- **Fail:** ≥1 criterio evaluado como no cumplido.

### Fail actions

1. Si faltan campos de metadata: completar antes de proceder.
2. Si asset no es self-contained: editar para incluir contexto necesario.
3. Si no se identifica ningún asset extractable: documentar justificación (1-3 oraciones) en conclusion document.
4. Asignar remediación con deadline ≤30 días.
5. No se requiere asset si justificación es aceptada — la investigación puede avanzar a Archive.

---

## Gate 6: Publish — Gate de publicación externa

| Campo | Valor |
|-------|-------|
| **Nombre** | Publish |
| **Posición en lifecycle** | Transición de Converted to Asset → Published (etapa 15) |
| **Responsable** | Fundador |

### Required inputs

- Asset(s) extraídos con Gate 5 aprobado
- Privacy/IP assessment completado
- Formato de publicación preparado

### Evaluation criteria (checklist)

| # | Criterio | Verificación |
|---|----------|-------------|
| 1 | Privacy checklist aprobado: no personal data expuesto, datos anonimizados si aplica, no client information en repositorio público | Checklist de privacy firmado |
| 2 | IP checklist aprobado: todas las fuentes tienen license type documentado, todas permiten el uso pretendido, attribution requirements cumplidos | Checklist de IP firmado |
| 3 | No AI_Generated_Content sin verificación tratado como Primary_Evidence en la publicación | Verificación de labeling de contenido AI |
| 4 | Formato adecuado para destino (público vs interno, audiencia identificada) | Revisión de formato y audiencia |
| 5 | Reproducibility: fuentes referenciadas accesibles o archivadas, pasos documentados | Sources verificables o archived |

### Pass/fail

- **Pass:** Los 5 criterios evaluados como cumplidos.
- **Fail:** ≥1 criterio evaluado como no cumplido.

### Fail actions

1. Si privacy/IP fail: remover contenido problemático o resolver licensing antes de publicar.
2. Si AI content sin verificación: verificar contra fuentes o remover del output publicable.
3. Si formato inadecuado: adaptar al canal de destino.
4. Asignar remediación con deadline ≤30 días.
5. Bloquear publicación externa hasta resolución completa.

---

## Gate 7: Commercial — Gate de utilización comercial

| Campo | Valor |
|-------|-------|
| **Nombre** | Commercial |
| **Posición en lifecycle** | Transición de Published → utilización comercial activa |
| **Responsable** | Fundador |

### Required inputs

- Asset publicado con Gate 6 aprobado
- Product_Hypothesis o Revenue_Hypothesis formulada
- ≥1 external demand signal documentado

### Evaluation criteria (checklist)

| # | Criterio | Verificación |
|---|----------|-------------|
| 1 | Product_Hypothesis completa con los 7 campos requeridos: problema + evidencia, target segment, asset, formato, commercial evidence, validation assumption, minimum experiment | Campos verificables en hypothesis |
| 2 | Confidence level es "emerging" o "supported" (no "speculative") | Campo de confidence verificable |
| 3 | ≥1 demand signal externo al Fundador: search volume, direct request, competitor existence, o stated willingness to pay | Señal documentada con fuente verificable |
| 4 | Validation experiment diseñado con: numeric success metric, deadline ≤30 días, pass/fail criteria | Experimento documentado con métricas |
| 5 | Asset cumple minimum asset registration criteria: name, type, description, usage hypothesis, declared state | 5 campos presentes y completos |

### Pass/fail

- **Pass:** Los 5 criterios evaluados como cumplidos.
- **Fail:** ≥1 criterio evaluado como no cumplido.

### Fail actions

1. Si hypothesis incompleta: completar campos faltantes antes de invertir en desarrollo.
2. Si no hay demand signal externo: la oportunidad permanece en status [Hipótesis] — no se permite iniciar desarrollo >2h/semana.
3. Si confidence es "speculative": obtener evidencia adicional antes de avanzar.
4. Si validation experiment falla (no cumple metric en deadline): documentar failure y reformular o archivar como Knowledge Asset dentro de 7 días.
5. Bloquear inversión de desarrollo hasta que el gate sea aprobado.

---

## Reglas de remediación

Las siguientes reglas aplican a todos los gates:

### Límites temporales

| Regla | Valor |
|-------|-------|
| **Deadline máximo por remediación** | 30 días calendario desde la fecha de fail |
| **Intentos máximos por gate** | 3 intentos consecutivos |
| **Grace period para revisión** | 14 días antes de flag como "review-overdue" |

### Proceso de remediación

1. **Primer fail:** Se documenta la deficiencia, se asigna corrective action con deadline ≤30 días, se permite re-evaluación.
2. **Segundo fail:** Se documenta la nueva deficiencia, se revisa si el approach es viable, se asigna nueva corrective action con deadline ≤30 días.
3. **Tercer fail (máximo):** Se requiere decision record documentando una de las siguientes opciones:
   - **Abandonar** la investigación con closure rationale y partial findings preservados.
   - **Replantear** la investigación con research question revisada y nuevo scope.
   - **Completar con limitaciones** aceptando las deficiencias documentadas como limitaciones explícitas.

### Estructura de remediación

Cada remediación debe documentar:

| Campo | Descripción |
|-------|-------------|
| **Deficiency** | Qué criterio falló y por qué |
| **Corrective action** | Qué se hará para resolver |
| **Assignee** | Quién es responsable (Fundador en etapa actual) |
| **Deadline** | Fecha límite (≤30 días desde fecha de fail) |
| **Completion criterion** | Cómo se verificará que la remediación es exitosa |
| **Attempt number** | 1, 2, o 3 (máximo) |

---

## Alternative evidence path

### Aplicabilidad

El alternative evidence path aplica cuando el Fundador documenta ≥1 constraint que previene experimentación controlada. Los constraints válidos son:

| Constraint | Ejemplo |
|-----------|---------|
| **Ético** | Experimentar con datos de salud de personas reales sin consentimiento |
| **Legal** | Regulaciones que prohíben ciertos tipos de pruebas en el dominio |
| **Costo** | Recursos necesarios exceden el presupuesto disponible significativamente |
| **Temporal** | Resultados del experimento requieren más tiempo del timebox disponible |

### Requisitos para activar el alternative path

1. Documentar el constraint específico con justificación (1-3 oraciones).
2. Identificar qué hipótesis no puede validarse mediante experimentación controlada.
3. Seleccionar ≥1 método alternativo de la tabla siguiente.

### Métodos alternativos con rigor equivalente

| Método | Tipo de evidencia que produce | Acceptance threshold | Limitaciones vs experimentación |
|--------|-------------------------------|---------------------|-------------------------------|
| **Literature review** | Secondary evidence, scientific literature | ≥3 fuentes independientes con consensus, quality score ≥6/10 cada una | No produce evidencia primaria, depende de calidad de fuentes existentes |
| **Expert consultation** | Testimony, professional experience | ≥2 expertos independientes con consensus documentado, credentials verificables | Sujeto a bias del experto, no reproducible directamente |
| **Observational evidence** | Direct observation, measurement | ≥3 observaciones en condiciones documentadas, con consistency verificable | No permite control de variables, correlación ≠ causación |
| **Triangulation** | Multiple evidence types combinados | ≥3 tipos de evidencia diferentes convergiendo en la misma conclusión | Cada tipo individual puede ser weak, la fuerza está en la convergencia |

### Reglas del alternative path

1. El alternative path no reduce el rigor — reemplaza el método pero mantiene los estándares de evidencia.
2. El confidence ceiling para conclusiones derivadas de alternative path es **4** (no alcanza "Very High" = 5 que requiere reproducibilidad).
3. Las limitaciones del método alternativo deben documentarse en la uncertainty section de la conclusión.
4. El Gate 2 (Experiment) se evalúa con criterio 5 activado: debe documentarse el constraint y el método alternativo seleccionado.

---

## Human review requirements

### Principio

El human review garantiza que decisiones críticas y conclusiones son validadas por juicio humano antes de aceptarse como conocimiento validado. En la etapa actual de LabOS, el Fundador es el único reviewer.

### Cuándo es obligatorio

| Situación | Human review obligatorio | Gate asociado |
|-----------|--------------------------|---------------|
| Investigación alcanza Conclusion stage | **Sí** — siempre | Gate 4 (Conclusions) |
| Findings en dominio regulado (finance, health, legal) | **Sí** — con approval documentado explícito | Gate 3 (Findings) + Gate 4 |
| >50% de analysis steps realizados por AI tools | **Sí** — verificación de cada finding vs fuente original | Gate 4 (Conclusions) |
| Publicación externa | **Sí** — privacy/IP review | Gate 6 (Publish) |
| Utilización comercial | **Sí** — validation del hypothesis | Gate 7 (Commercial) |

### Proceso de human review (Gate 4 — obligatorio)

1. **Lectura completa:** Reviewer lee la conclusión íntegramente.
2. **Verificación de claims:** Reviewer verifica que claims están soportados por evidencia citada.
3. **Verificación AI:** Si >50% de analysis fue AI-assisted, reviewer verifica cada finding contra ≥1 fuente original.
4. **Registro de resultado:**

| Campo | Valor |
|-------|-------|
| **Reviewer identity** | Nombre del reviewer |
| **Date** | Fecha de revisión (YYYY-MM-DD) |
| **Review result** | approved / revision-needed / rejected |
| **Findings reviewed** | Lista de findings verificados |
| **Conditions/caveats** | Condiciones o notas del reviewer |

### Human review en dominios regulados

Para investigaciones en dominios regulados (finance, health, legal), el human review requiere documentación adicional:

| Campo adicional | Descripción |
|-----------------|-------------|
| **Domain** | Dominio regulado específico |
| **Regulatory constraints identified** | Constraints regulatorios aplicables |
| **Approval decision** | Decisión explícita de approval |
| **Conditions noted** | Condiciones o restricciones |

### Regla de overdue

- Si una conclusión permanece en review status sin resultado registrado por **>14 días calendario**, la investigación se flag como **"review-overdue"**.
- Se notifica al Fundador que acción es requerida.
- El flag no auto-rechaza la investigación — sólo señala inacción.

### Deficiencias encontradas en human review

Cuando human review identifica findings unsupported, contradicted, o insufficiently evidenced:

1. Se documenta cada deficiencia identificada.
2. Se asigna remediation action con:
   - Deficiency identificada
   - Corrective action
   - Responsible party (Fundador)
   - Target resolution date ≤30 días
3. La conclusión NO se acepta como validated knowledge hasta resolución.
4. Se permite re-evaluación tras remediación (máximo 3 intentos totales por gate).

---

## Resumen de gates

| # | Gate | Posición | Inputs principales | Human review | Criterios |
|---|------|----------|-------------------|--------------|-----------|
| 1 | Initiate | Planned → In Progress | Brief, questions, scope, assumptions | No | 5 |
| 2 | Experiment | Analysis → Experimentation | Hypothesis, protocol, evidence | No | 5 |
| 3 | Findings | Findings → Conclusion | Findings, evidence register, sources | Sí (dominios regulados) | 5 |
| 4 | Conclusions | Conclusion → Review → Completed | Conclusion, evidence, uncertainty | **Sí (siempre)** | 5 |
| 5 | Assets | Completed → Converted to Asset | Investigation completed, asset metadata | No | 5 |
| 6 | Publish | Converted to Asset → Published | Assets, privacy/IP assessment | Sí (privacy/IP) | 5 |
| 7 | Commercial | Published → Commercial use | Hypothesis, demand signal, experiment | Sí (validation) | 5 |

### Flujo visual

```
[Planned] ──── Gate 1: Initiate ────► [In Progress]
                                            │
                                            ▼
[Analysis] ──── Gate 2: Experiment ────► [Experimentation]
                                            │
                                            ▼
[Findings] ──── Gate 3: Findings ────► [Conclusion]
                                            │
                                            ▼
[Conclusion] ──── Gate 4: Conclusions ★ ────► [Completed]
                                            │
                                            ▼
[Completed] ──── Gate 5: Assets ────► [Converted to Asset]
                                            │
                                            ▼
[Asset] ──── Gate 6: Publish ────► [Published]
                                            │
                                            ▼
[Published] ──── Gate 7: Commercial ────► [Commercial Use]

★ = Human review obligatorio
```

---

## Referencias cruzadas

| Documento | Relación |
|-----------|----------|
| 002-research-lifecycle.md | Define las 16 etapas donde se insertan los gates |
| 008-research-workflow.md | Define el flujo de trabajo que atraviesa los gates |
| 017-conclusion-framework.md | Define la estructura de conclusión evaluada en Gate 4 |
| 014-experiment-design.md | Define el protocolo evaluado en Gate 2 |
| 018-research-to-asset.md | Define el proceso de extracción evaluado en Gate 5 |
| 019-research-to-product-hypothesis.md | Define las hipótesis evaluadas en Gate 7 |
| 022-domain-specific-adaptations.md | Define adaptaciones que activan el alternative evidence path |
