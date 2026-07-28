# Research Asset Handoff Template

> **Propósito:** Plantilla para documentar la extracción y entrega formal de activos reutilizables producidos por una investigación. Asegura que cada activo tiene metadata completa, hipótesis de uso, trazabilidad a la investigación origen, y cumple los criterios de calidad antes de ser transferido al repositorio de assets.
>
> **Campos requeridos:** 9 (asset name, type, description, usage hypothesis, target audience, source investigation, state, monetization potential, dependencies)
>
> **Requirements:** R15.2, R15.3, R33.1, R33.2, R33.3, R33.4

---

## Instrucciones de uso

1. **Copiar** este template al directorio de la investigación correspondiente (por ejemplo: `research/{investigation-id}/handoff/ASSET-{id}.md`) al momento de extraer un activo de una investigación completada.
2. **Completar todos los campos requeridos** antes de transferir el activo al repositorio de assets (`assets/{type}/`). Ningún campo requerido puede quedar vacío; si un campo no aplica, indicar "No aplica: [justificación]".
3. **Verificar el quality gate** — los 4 criterios deben evaluarse como "Pasa" antes de que el activo avance de estado "draft" a "ready". Documentar la evaluación en la sección correspondiente.
4. **Vincular la investigación fuente** referenciando el ID de investigación, la fecha de conclusión y la referencia a la conclusión específica que originó el activo.
5. **Clasificar el tipo de activo** seleccionando exactamente uno de los 5 tipos definidos. El tipo determina la carpeta destino en el repositorio.
6. **Transferir al repositorio** una vez que el quality gate sea aprobado: mover o copiar el activo a `assets/{type}/{nombre-del-activo}.md` y actualizar el documento de conclusión de la investigación con la referencia al activo.

---

## Campos requeridos

### Identificación del activo

| Campo | Valor |
|-------|-------|
| **Asset name** | {Nombre del activo — máximo 80 caracteres} |
| **Asset ID** | `ASSET-{investigation_id}-{sequential_number}` |
| **Type** | `knowledge` \| `technical` \| `educational` \| `commercial` \| `data` |
| **State** | `draft` \| `ready` \| `published` |
| **Created at** | YYYY-MM-DD |
| **Last updated** | YYYY-MM-DD |

### Descripción

> Descripción del activo en 1-3 oraciones. Debe explicar qué es, qué contiene y para qué sirve sin requerir contexto adicional.

{Descripción del activo — mínimo 1 oración, máximo 3 oraciones}

### Hipótesis de uso (Usage Hypothesis)

> Describe quién usaría este activo y cómo. Debe ser específica y verificable.

{Quién usaría este activo, en qué contexto, y qué resultado esperaría obtener}

### Audiencia objetivo (Target Audience)

> Segmento o perfil específico que se beneficiaría de este activo.

| Campo | Valor |
|-------|-------|
| **Perfil primario** | {Rol, tipo de profesional o segmento} |
| **Necesidad que resuelve** | {Problema o necesidad específica} |
| **Nivel de expertise requerido** | {Principiante / Intermedio / Avanzado} |

### Investigación fuente (Source Investigation)

> Trazabilidad completa a la investigación que produjo este activo.

| Campo | Valor |
|-------|-------|
| **Investigation ID** | {ID de la investigación origen} |
| **Conclusion date** | YYYY-MM-DD |
| **Conclusion reference** | {Referencia a la sección/documento de conclusión específica} |
| **Research question** | {Pregunta de investigación que originó este activo} |

### Potencial de monetización (Monetization Potential)

> Evaluación de la oportunidad comercial del activo. Debe basarse en evidencia o señales observables, no en especulación.

| Campo | Valor |
|-------|-------|
| **Monetizable** | Sí \| No \| Por evaluar |
| **Mecanismo propuesto** | {venta directa / suscripción / freemium / licencia / contenido / servicio / N/A} |
| **Señal de demanda** | {Evidencia observable: búsquedas, peticiones, competidores, etc. — o "Sin señal identificada"} |
| **Hipótesis de precio** | {Rango estimado con justificación — o "No definido"} |
| **Product Hypothesis ID** | {HYP-PROD-NNN si existe — o "No formulada"} |

### Dependencias

> Recursos, herramientas, conocimientos previos o activos de los que depende este activo para ser utilizado.

| # | Dependencia | Tipo | Criticidad |
|---|-------------|------|------------|
| 1 | {nombre de la dependencia} | {activo / herramienta / conocimiento / acceso / dato} | {Bloqueante / Deseable / Opcional} |

---

## Quality Gate (R15.3)

> Los 4 criterios deben evaluarse como "Pasa" antes de que el activo avance de `draft` a `ready`. Un solo "No pasa" bloquea la transición.

| # | Criterio | Descripción | Resultado | Evidencia/Nota |
|---|----------|-------------|-----------|----------------|
| 1 | **Autocontenido** | El activo es comprensible y utilizable sin necesidad de acceder a la investigación fuente. Toda información necesaria está incluida en el activo mismo. | {Pasa / No pasa} | {Justificación} |
| 2 | **Uso identificado** | Existe al menos una hipótesis de uso concreta con audiencia, contexto y resultado esperado definidos. | {Pasa / No pasa} | {Justificación} |
| 3 | **Metadata completa** | Todos los campos requeridos están completados con información precisa y actualizada. El nombre tiene ≤80 caracteres, la descripción tiene 1-3 oraciones, el tipo es válido. | {Pasa / No pasa} | {Justificación} |
| 4 | **Sin información sensible** | El activo no contiene datos personales, credenciales, tokens, información de clientes, ni datos regulados sin autorización explícita. | {Pasa / No pasa} | {Justificación} |

### Resultado del quality gate

| Campo | Valor |
|-------|-------|
| **Resultado global** | {Aprobado / No aprobado} |
| **Evaluado por** | {Nombre del evaluador} |
| **Fecha de evaluación** | YYYY-MM-DD |
| **Transición autorizada** | {draft → ready / No autorizada} |

---

## Campos opcionales

### Notas de extracción

> Contexto adicional sobre el proceso de extracción: decisiones tomadas, contenido excluido deliberadamente, transformaciones aplicadas.

{Notas sobre el proceso de extracción}

### Versiones previas

> Si el activo tiene iteraciones anteriores.

| Versión | Fecha | Cambio principal |
|---------|-------|-----------------|
| {v1.0} | {YYYY-MM-DD} | {Descripción del cambio} |

### Activos relacionados

> Otros activos producidos por la misma investigación o que complementan este.

| Asset ID | Nombre | Relación |
|----------|--------|----------|
| {ASSET-id} | {nombre} | {complementa / extiende / depende de / reemplaza} |

### Métricas de uso esperadas

> Indicadores para evaluar si el activo cumple su hipótesis de uso una vez publicado.

| Métrica | Definición | Target |
|---------|-----------|--------|
| {nombre} | {cómo se mide} | {valor esperado} |

---

## [DOMAIN-SPECIFIC] Secciones específicas por dominio

### [DOMAIN-SPECIFIC] Activos de trading/finanzas

> Para activos extraídos de investigaciones en dominios financieros (Crypto Scalping Core, Atlas Wealth Labs).

- **Periodo de validez de datos:** {fecha inicio — fecha fin}
- **Condiciones de mercado aplicables:** {bull/bear/lateral/volatile/todas}
- **Regulaciones relevantes:** {ninguna / listado de regulaciones}
- **Disclaimer requerido:** {texto del disclaimer — o "Estándar"}

### [DOMAIN-SPECIFIC] Activos técnicos/software

> Para activos técnicos extraídos de investigaciones en SoftwareFactoryAgentsAI, SentinelOps.

- **Stack tecnológico:** {lenguajes, frameworks, herramientas}
- **Compatibilidad:** {versiones compatibles}
- **Licencia propuesta:** {MIT / Apache 2.0 / Propietaria / Por definir}
- **Mantenimiento requerido:** {frecuencia estimada de actualización}

### [DOMAIN-SPECIFIC] Activos educativos/contenido

> Para activos de tipo educativo o de contenido (English Learning Lab, Photography Lab, Music Lab).

- **Formato de entrega:** {artículo / tutorial / video-script / curso / guía}
- **Plataforma target:** {blog / YouTube / curso online / newsletter}
- **Nivel de audiencia:** {principiante / intermedio / avanzado / mixto}
- **Contenido evergreen:** {Sí / No — si No, vigencia estimada}

---

## Ejemplo completo

> A continuación un ejemplo realista con todos los campos requeridos completados.

---

### Identificación del activo

| Campo | Valor |
|-------|-------|
| **Asset name** | Framework de evaluación de agentes LLM para soporte técnico |
| **Asset ID** | `ASSET-INV-023-001` |
| **Type** | `knowledge` |
| **State** | `ready` |
| **Created at** | 2025-03-15 |
| **Last updated** | 2025-03-22 |

### Descripción

Framework estructurado para evaluar agentes conversacionales basados en LLMs en contextos de soporte técnico. Define 8 dimensiones de evaluación (precisión, relevancia, completitud, tono, tiempo de respuesta, escalación apropiada, seguimiento de protocolo y satisfacción simulada) con rúbricas cuantitativas para cada una. Incluye un dataset de 50 escenarios de evaluación categorizados por complejidad.

### Hipótesis de uso (Usage Hypothesis)

Equipos que desarrollan o evalúan agentes de soporte técnico basados en LLMs necesitan un framework estandarizado para medir calidad antes de desplegar en producción. Este framework permitiría reducir el tiempo de evaluación de 2 semanas ad-hoc a 3 días con rúbricas predefinidas, y proporcionaría métricas comparables entre versiones del agente.

### Audiencia objetivo (Target Audience)

| Campo | Valor |
|-------|-------|
| **Perfil primario** | Desarrolladores e ingenieros de ML que implementan agentes conversacionales |
| **Necesidad que resuelve** | Falta de métricas estandarizadas para evaluar calidad de agentes LLM antes de producción |
| **Nivel de expertise requerido** | Intermedio (familiaridad con LLMs y conceptos de evaluación de NLP) |

### Investigación fuente (Source Investigation)

| Campo | Valor |
|-------|-------|
| **Investigation ID** | INV-023 |
| **Conclusion date** | 2025-03-12 |
| **Conclusion reference** | `research/INV-023/conclusions/conclusion-001.md` — Sección "Hallazgo principal" |
| **Research question** | ¿Qué dimensiones de calidad son críticas para evaluar agentes LLM en soporte técnico y cómo pueden medirse de forma reproducible? |

### Potencial de monetización (Monetization Potential)

| Campo | Valor |
|-------|-------|
| **Monetizable** | Sí |
| **Mecanismo propuesto** | Contenido premium (guía completa con dataset) + consultoría de implementación |
| **Señal de demanda** | 3 publicaciones en r/MachineLearning preguntando por frameworks de evaluación (ene-mar 2025); término "LLM evaluation framework" con ~2.4K búsquedas/mes (Ahrefs) |
| **Hipótesis de precio** | USD 49-99 para guía completa con dataset; USD 200-500/h para consultoría de implementación |
| **Product Hypothesis ID** | HYP-PROD-007 |

### Dependencias

| # | Dependencia | Tipo | Criticidad |
|---|-------------|------|------------|
| 1 | Dataset de 50 escenarios de evaluación | Dato | Bloqueante |
| 2 | Acceso a API de OpenAI (GPT-4o) para ejecutar evaluaciones | Herramienta | Bloqueante |
| 3 | Conocimiento de prompting y evaluación de LLMs | Conocimiento | Deseable |
| 4 | Python ≥3.11 para scripts de evaluación automatizada | Herramienta | Opcional |

---

### Quality Gate (R15.3)

| # | Criterio | Descripción | Resultado | Evidencia/Nota |
|---|----------|-------------|-----------|----------------|
| 1 | **Autocontenido** | El activo es comprensible y utilizable sin necesidad de acceder a la investigación fuente. | Pasa | El framework incluye definiciones de dimensiones, rúbricas, y dataset — no requiere leer INV-023 para usarlo |
| 2 | **Uso identificado** | Existe al menos una hipótesis de uso concreta con audiencia, contexto y resultado esperado. | Pasa | Hipótesis de uso define perfil (devs de ML), contexto (pre-producción), resultado (evaluación en 3 días) |
| 3 | **Metadata completa** | Todos los campos requeridos completados. Nombre ≤80 chars, descripción 1-3 oraciones, tipo válido. | Pasa | Nombre: 62 caracteres. Descripción: 3 oraciones. Tipo: knowledge (válido). Todos los campos llenos |
| 4 | **Sin información sensible** | No contiene datos personales, credenciales, tokens ni información regulada. | Pasa | Revisado: no contiene PII, API keys, ni datos de clientes. Escenarios son sintéticos |

### Resultado del quality gate

| Campo | Valor |
|-------|-------|
| **Resultado global** | Aprobado |
| **Evaluado por** | Fundador |
| **Fecha de evaluación** | 2025-03-22 |
| **Transición autorizada** | draft → ready |

---
