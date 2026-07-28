# Research Plan Template

## Propósito

Este template estructura el plan ejecutable de una investigación, definiendo las preguntas de investigación, el alcance con límites explícitos, el timebox, el deadline, los criterios de finalización, las asunciones que deben validarse y el número máximo de fuentes a consultar. Garantiza que toda investigación comience con boundaries claros y condiciones de éxito verificables.

---

## Campos obligatorios

### Metadata

| Campo | Valor |
|-------|-------|
| **Investigation ID** | `[ID único de la investigación]` |
| **Título** | `[Nombre descriptivo de la investigación]` |
| **Research Brief asociado** | `[Referencia al Research Brief que origina este plan]` |
| **Fecha de creación** | `[YYYY-MM-DD]` |
| **Estado** | `[Planned / In Progress / Completed / Rejected]` |
| **Effort category** | `[Small <4h / Medium 4-16h / Large >16h]` |

---

### Research Questions

Formular las preguntas que esta investigación busca responder. Cada pregunta debe contener los 5 componentes obligatorios.

#### Pregunta principal

| Componente | Descripción |
|------------|-------------|
| **Subject** | `[Tema o variable central que se investiga]` |
| **Scope boundary** | `[Qué está incluido y qué está excluido del alcance de la pregunta]` |
| **Constraints** | `[Restricciones de recursos, tiempo, acceso o contexto]` |
| **Expected answer type** | `[Tipo de respuesta esperada: comparativa, causal, descriptiva, evaluativa, predictiva]` |
| **Verification method** | `[Cómo se verificará que la respuesta es válida]` |

#### Sub-preguntas (si aplica)

| # | Subject | Scope boundary | Constraints | Expected answer type | Verification method | Dependencia |
|---|---------|----------------|-------------|---------------------|--------------------:|-------------|
| 1 | `[...]` | `[...]` | `[...]` | `[...]` | `[...]` | `[Ninguna / Pregunta #N]` |
| 2 | `[...]` | `[...]` | `[...]` | `[...]` | `[...]` | `[Ninguna / Pregunta #N]` |

---

### Scope

| Campo | Valor |
|-------|-------|
| **Inclusions** | `[Qué temas, áreas, tecnologías o perspectivas se incluyen]` |
| **Exclusions** | `[Qué queda explícitamente fuera del alcance]` |
| **Depth level** | `[superficial / moderate / deep]` |
| **Domains** | `[Dominios de conocimiento involucrados]` |
| **Max sources** | `[Número entero entre 3 y 50]` |

#### Definición de depth levels

| Nivel | Descripción |
|-------|-------------|
| **Superficial** | Resumen de fuentes existentes. No se genera análisis original. Lectura rápida y síntesis. |
| **Moderate** | Síntesis y comparación entre fuentes. Se identifican patrones y contradicciones. |
| **Deep** | Análisis original con cross-validation de claims. Se producen conclusiones nuevas respaldadas por múltiples fuentes independientes. |

---

### Timebox y Deadline

| Campo | Valor | Restricciones |
|-------|-------|---------------|
| **Timebox** | `[N horas]` | Mínimo: 1 hora. Máximo: 40 horas. |
| **Deadline** | `[YYYY-MM-DD]` | Fecha calendario límite para concluir. |

#### Regla de 80% del timebox

Cuando se haya consumido el 80% del timebox sin alcanzar una conclusión, se debe seleccionar una de las siguientes opciones:

- [ ] **Extender** — Nuevo timebox: `[N horas]`. Justificación: `[...]`
- [ ] **Reducir scope** — Elementos removidos: `[...]`
- [ ] **Concluir parcialmente** — Qué queda sin resolver: `[...]`

---

### Completion Criteria

Definir las condiciones observables que determinan cuándo la investigación se considera completa.

| # | Criterio | Verificable por |
|---|----------|-----------------|
| 1 | `[Condición observable que indica que la pregunta fue respondida]` | `[Método de verificación]` |
| 2 | `[Condición observable]` | `[Método de verificación]` |
| 3 | `[Condición observable]` | `[Método de verificación]` |

---

### Assumptions Register

Documentar las asunciones que podrían afectar las conclusiones de la investigación.

| # | Statement | Confidence | Basis | Impact if wrong | Validation approach |
|---|-----------|------------|-------|-----------------|---------------------|
| 1 | `[Afirmación asumida como cierta]` | `[High / Medium / Low]` | `[Base para el nivel de confianza asignado]` | `[Consecuencia si la asunción resulta incorrecta]` | `[Cómo se validará o invalidará esta asunción]` |
| 2 | `[...]` | `[...]` | `[...]` | `[...]` | `[...]` |
| 3 | `[...]` | `[...]` | `[...]` | `[...]` | `[...]` |

> **Nota:** Se requiere documentar al menos 1 asunción. Si no existen asunciones, se debe proveer justificación explícita de por qué no aplican.

#### Clasificación de asunciones

Cada asunción debe clasificarse como una de:

| Tipo | Descripción |
|------|-------------|
| **Domain** | Sobre el tema o materia investigada |
| **Methodological** | Sobre el enfoque o herramientas de investigación |
| **Resource** | Sobre tiempo, capacidad o materiales disponibles |
| **Contextual** | Sobre condiciones externas o del entorno |

---

## Campos opcionales

### Recursos necesarios

| Recurso | Disponibilidad | Notas |
|---------|---------------|-------|
| `[Herramienta, acceso, dataset, etc.]` | `[Disponible / Pendiente / Requiere acción]` | `[...]` |

### Riesgos identificados

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|-------------|---------|------------|
| `[Descripción del riesgo]` | `[Alta / Media / Baja]` | `[Alto / Medio / Bajo]` | `[Acción preventiva]` |

### Dependencias externas

| Dependencia | Estado | Impacto en timeline |
|-------------|--------|---------------------|
| `[Investigación previa, acceso, decisión pendiente]` | `[Resuelta / Pendiente]` | `[Bloquea / No bloquea]` |

---

## [DOMAIN-SPECIFIC] Secciones por dominio

### [DOMAIN-SPECIFIC] Technical Research

| Campo adicional | Valor |
|-----------------|-------|
| **Versiones a evaluar** | `[Versiones específicas de tecnología]` |
| **Environment de pruebas** | `[Descripción del environment]` |
| **Reproducibility requirements** | `[Qué debe ser reproducible]` |

### [DOMAIN-SPECIFIC] Quantitative Research

| Campo adicional | Valor |
|-----------------|-------|
| **Dataset period** | `[Rango temporal de datos]` |
| **Statistical methods** | `[Métodos estadísticos a emplear]` |
| **Significance threshold** | `[Umbral de significancia]` |

### [DOMAIN-SPECIFIC] Market Research

| Campo adicional | Valor |
|-----------------|-------|
| **Target segment** | `[Segmento de mercado objetivo]` |
| **Validation signals** | `[Señales que indicarían demanda]` |
| **Competitive landscape** | `[Competidores a analizar]` |

### [DOMAIN-SPECIFIC] Health and Performance Research

| Campo adicional | Valor |
|-----------------|-------|
| **Biomarkers tracked** | `[Métricas de salud o rendimiento]` |
| **Baseline period** | `[Periodo de baseline antes de intervención]` |
| **Safety considerations** | `[Consideraciones de seguridad]` |

---

## Instrucciones de uso

### Paso 1: Verificar prerequisitos

Antes de completar este template, confirmar que:
- Existe un Research Brief aprobado con todos los campos obligatorios
- El problem statement está documentado con síntomas y causa raíz separados
- Se tiene claridad sobre el effort category (small, medium, large)

### Paso 2: Formular research questions

1. Redactar la pregunta principal con sus 5 componentes (subject, scope boundary, constraints, expected answer type, verification method)
2. Evaluar contra quality criteria: specificity, answerability, relevance, time-boundedness
3. Si la pregunta involucra más de una variable independiente o dos dominios distintos, descomponer en sub-preguntas con dependencias explícitas
4. Máxima profundidad de descomposición: 3 niveles

### Paso 3: Definir scope y timebox

1. Documentar inclusiones y exclusiones de forma explícita — lo no incluido se asume excluido
2. Seleccionar depth level según el esfuerzo disponible y la complejidad de la pregunta
3. Asignar timebox entre 1 y 40 horas basado en el effort category
4. Establecer deadline como fecha calendario (formato YYYY-MM-DD)
5. Definir max sources como un entero entre 3 y 50

### Paso 4: Documentar assumptions

1. Listar al menos 1 asunción que podría afectar las conclusiones
2. Para cada asunción completar los 5 campos: statement, confidence, basis, impact-if-wrong, validation approach
3. Clasificar cada asunción por tipo (domain, methodological, resource, contextual)
4. Si genuinamente no existen asunciones, documentar la justificación explícita

### Paso 5: Definir completion criteria

1. Escribir al menos 2 condiciones observables que determinen cuándo la investigación está completa
2. Cada criterio debe ser verificable por un tercero sin juicio subjetivo
3. Vincular cada criterio a la research question que resuelve

### Paso 6: Revisión final

1. Verificar que todos los campos obligatorios están completos
2. Confirmar que el timebox es coherente con el depth level y el número de sources
3. Validar que las assumptions no contradicen el scope definido
4. Aprobar el plan antes de iniciar la etapa de Source Collection

---

## Ejemplo completo

### Metadata

| Campo | Valor |
|-------|-------|
| **Investigation ID** | INV-2024-007 |
| **Título** | Evaluación de frameworks de orquestación de agentes de IA |
| **Research Brief asociado** | RB-2024-007 |
| **Fecha de creación** | 2024-11-15 |
| **Estado** | Planned |
| **Effort category** | Medium 4-16h |

---

### Research Questions

#### Pregunta principal

| Componente | Descripción |
|------------|-------------|
| **Subject** | Frameworks de orquestación de agentes de IA disponibles en el ecosistema open-source |
| **Scope boundary** | Incluye: frameworks con ≥500 estrellas en GitHub, documentación en inglés, soporte para Python o TypeScript. Excluye: soluciones propietarias, frameworks sin release estable (pre-alpha). |
| **Constraints** | Evaluación limitada a documentación pública y PoC de máximo 4 horas por framework. No se evaluará rendimiento en producción. |
| **Expected answer type** | Comparativa con recomendación fundamentada para el caso de uso de SoftwareFactoryAgentsAI |
| **Verification method** | Proof of concept funcional con el framework seleccionado ejecutando un workflow de 3 pasos |

#### Sub-preguntas

| # | Subject | Scope boundary | Constraints | Expected answer type | Verification method | Dependencia |
|---|---------|----------------|-------------|---------------------|--------------------:|-------------|
| 1 | Criterios de evaluación relevantes para orquestación multi-agente | Solo criterios aplicables a equipos de 1-3 personas | Basado en literatura y experiencia documentada | Lista priorizada de criterios | Validación contra ≥2 fuentes independientes | Ninguna |
| 2 | Comparativa de frameworks contra criterios definidos | Top 5 frameworks por popularidad que cumplan scope | Máximo 2 horas de evaluación por framework | Tabla comparativa con scores | Reproducibilidad del scoring por tercero | Pregunta #1 |
| 3 | Viabilidad de integración con stack existente (Python + GitHub Actions) | Solo el framework recomendado | PoC limitado a 4 horas | Evaluación binaria (viable / no viable) con evidence | PoC funcional ejecutable | Pregunta #2 |

---

### Scope

| Campo | Valor |
|-------|-------|
| **Inclusions** | Frameworks open-source de orquestación multi-agente; documentación oficial; ejemplos de uso; community feedback (GitHub issues, discussions) |
| **Exclusions** | Soluciones enterprise/propietarias; frameworks sin release estable; evaluación de rendimiento bajo carga; integración con herramientas no presentes en el stack actual |
| **Depth level** | moderate |
| **Domains** | Technical (AI Agents, Software Engineering) |
| **Max sources** | 15 |

---

### Timebox y Deadline

| Campo | Valor | Restricciones |
|-------|-------|---------------|
| **Timebox** | 12 horas | Mínimo: 1h. Máximo: 40h. |
| **Deadline** | 2024-11-29 | Fecha calendario límite. |

---

### Completion Criteria

| # | Criterio | Verificable por |
|---|----------|-----------------|
| 1 | Tabla comparativa de ≥3 frameworks con scores en cada criterio definido | Inspección del documento producido |
| 2 | Recomendación documentada con ≥2 evidencias que la soporten | Trazabilidad a Source_Register |
| 3 | PoC funcional ejecutable del framework recomendado con un workflow de 3 pasos | Ejecución exitosa del PoC en environment local |

---

### Assumptions Register

| # | Statement | Confidence | Basis | Impact if wrong | Validation approach | Tipo |
|---|-----------|------------|-------|-----------------|---------------------|------|
| 1 | Los frameworks evaluados tienen documentación suficiente para evaluar sin contactar a los autores | High | Los 5 frameworks más populares suelen tener docs completas | Se necesitaría más tiempo para evaluar frameworks con docs incompletas, afectando el timebox | Verificar disponibilidad de docs en los primeros 30 minutos de evaluación | Resource |
| 2 | El stack actual (Python + GitHub Actions) es compatible con al menos 2 de los frameworks candidatos | Medium | La mayoría de frameworks de agentes soportan Python, pero la integración con CI/CD varía | Si ninguno es compatible, la recomendación sería instalar un stack diferente, cambiando la pregunta de investigación | PoC de integración básica en la sub-pregunta #3 | Domain |
| 3 | La comunidad y mantenimiento activo son indicadores razonables de calidad para frameworks en etapa temprana | Medium | Experiencia previa con frameworks open-source y correlación observada entre actividad y estabilidad | Podría seleccionarse un framework popular pero con calidad técnica inferior | Cross-check con análisis técnico del código fuente (muestreo) | Methodological |

---

### Recursos necesarios

| Recurso | Disponibilidad | Notas |
|---------|---------------|-------|
| Acceso a GitHub para evaluar repositorios | Disponible | Cuenta existente |
| Environment Python 3.11+ local | Disponible | Setup actual soporta |
| Tiempo dedicado sin interrupciones (bloques de 2h) | Pendiente | Requiere planificación en calendario |

---

### Riesgos identificados

| Riesgo | Probabilidad | Impacto | Mitigación |
|--------|-------------|---------|------------|
| Frameworks evolucionan rápidamente y la evaluación queda obsoleta en semanas | Media | Medio | Documentar versiones exactas evaluadas y fecha de vigencia de la recomendación |
| PoC no es representativo de uso en producción | Alta | Bajo | Declarar explícitamente como limitación en conclusions; no extrapolar PoC a production readiness |

---

> **Etiqueta epistémica:** [Decisión]
>
> **Requirements cubiertos:** R33.1, R33.2, R33.3, R33.4, R4.1, R5.1, R5.2, R6.1
