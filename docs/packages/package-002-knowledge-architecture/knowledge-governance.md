# Gobernanza del Conocimiento

## Propósito

Este documento define los roles, autoridades y cadencias de revisión para la gestión del conocimiento en LabOS. [Decisión] Establece quién puede hacer qué, cuándo se revisa, y qué triggers activarían un modelo de gobernanza más complejo en el futuro.

---

## Roles conceptuales

La gobernanza del conocimiento distingue 6 roles. En nivel SOLO (1 fundador), el fundador ocupa todos simultáneamente. La separación existe para escalar sin reestructurar. [Decisión]

| Rol | Definición | Quién lo ocupa (SOLO) |
|-----|-----------|----------------------|
| **Creator** | Produce contenido del KO (síntesis, observación, importación). [Decisión] | Fundador o agente IA. |
| **Owner** | Mantiene el KO actualizado. Decide su destino (deprecar, superseder, compartir). [Decisión] | Fundador. |
| **Reviewer** | Valida calidad, coherencia y confianza asignada. [Decisión] | Fundador. |
| **Canonical Authority** | Promueve a Capa 3. Tiene última palabra sobre conocimiento canónico. [Decisión] | Fundador (exclusivamente). |
| **Consumer** | Usa el KO para decisiones, síntesis o creación de activos. [Decisión] | Fundador, Labs, agentes IA futuros. |
| **System Administrator** (futuro) | Gestiona infraestructura de almacenamiento y acceso al conocimiento. [Visión] | Dormido — no activado hasta implementación de software. |

---

## Acciones de gobernanza y autoridad

| Acción | Autoridad (en SOLO) | Formato requerido |
|--------|---------------------|-------------------|
| Crear KO | Fundador directamente, o agente IA (resultado entra en `captured`, requiere revisión). [Decisión] | Cumplir campos obligatorios del [Knowledge Object Contract](./knowledge-object-contract.md). |
| Validar KO | Fundador. [Decisión] | Camino rápido (≤2 min, verificación de 4 criterios) o `under_review` para alto impacto. |
| Promover a canónico | Fundador como Canonical Authority. [Decisión] | Verificar 6 criterios del gate validated → canonical (ref: [knowledge-quality-gates.md](./knowledge-quality-gates.md)). |
| Registrar disputa | Cualquiera que detecte contradicción (fundador, agente IA). [Decisión] | Documentar: qué se disputa + qué lo contradice + fecha. |
| Resolver disputa | Fundador como Canonical Authority. [Decisión] | ≤3 oraciones de rationale + decisión explícita. |
| Superseder KO | Fundador (crea KO nuevo + marca antiguo como `superseded`). [Decisión] | Nuevo KO creado + `superseded_by` completado en el original. |
| Deprecar KO | Fundador, o por expiración de freshness sin revalidación (conceptual). [Decisión] | ≤2 oraciones de rationale de deprecación. |
| Archivar KO | Transición conceptual tras 30 días en `deprecated` o `superseded`. No requiere aprobación adicional. [Decisión] | Automático — detectable en revisión mensual. |
| Compartir (publicar) KO | Fundador como owner del Lab. [Decisión] | Cambiar `sensitivity` a PUBLIC + agregar `summary` ≤300 caracteres. |
| Cambiar sensibilidad | Fundador como owner. [Decisión] | Decisión explícita documentada. |
| Aprobar handoff Knowledge → Asset | Fundador. [Decisión] | Verificar elegibilidad + confirmar trigger (ref: [knowledge-to-asset-handoff.md](./knowledge-to-asset-handoff.md)). |
| Proponer handoff Knowledge → Capability | Fundador vía ADR (cuando se active). [Decisión] | ADR requerido — entidad Capability es dormida (ref: [knowledge-to-capability-handoff.md](./knowledge-to-capability-handoff.md)). |

---

## Cadencia de revisión (SOLO-proporcional)

El overhead total de gobernanza del conocimiento no debe exceder 2 horas/mes (per Principio 6). [Decisión]

### Revisión event-triggered (inmediata)

Se ejecuta cuando ocurre el evento, no por calendario: [Decisión]

| Evento | Acción de revisión | Tiempo estimado |
|--------|-------------------|-----------------|
| Nueva contradicción detectada | Registrar como `disputed`. Evaluar urgencia. | 5-10 min. |
| Fuente original actualizada significativamente | Verificar si el KO derivado sigue siendo válido. | 5-15 min. |
| Experimento produce resultado opuesto a KO existente | Evaluar si marcar como `disputed` o aclarar alcance. | 10-15 min. |
| ADR aprobado que afecta conocimiento | Revisar KOs afectados por consistencia. | 15-30 min. |

### Revisión mensual de higiene (~1 hora)

Una sesión mensual cubre las siguientes verificaciones: [Decisión]

| Verificación | Qué buscar | Acción |
|-------------|-----------|--------|
| KOs con freshness REVIEW_DUE o STALE | Identificar por ventana de validez expirada. | Revalidar o deprecar. |
| KOs en estado `disputed` >30 días | No deben permanecer indefinidamente sin resolución. | Resolver o tomar mejor decisión disponible. |
| Procedencia BROKEN | Fuentes que se volvieron inaccesibles. | Buscar alternativa o degradar confianza. |
| KOs huérfanos | Lab pausado con KOs Lab-Private sin mantenedor. | Reasignar, promover o archivar. |
| Duplicados potenciales | Misma información en múltiples ubicaciones sin referencia. | Reconciliar (ref: [knowledge-source-of-truth.md](./knowledge-source-of-truth.md)). |
| KOs en `captured` >30 días | Capturados sin transitar. | Validar o archivar. |
| Compartición riesgosa | KOs PRIVATE referenciados desde contextos que podrían exponerlos. | Verificar integridad de boundary. |

### Revisión a nivel de package

Cuando un package se completa o hay decisiones arquitectónicas que cambian el baseline: [Decisión]

| Trigger | Acción |
|---------|--------|
| Package completado | Verificar que los KOs producidos/referenciados son consistentes con el nuevo package. |
| ADR aprobado que modifica invariantes | Revisar impacto en KOs canónicos afectados. |
| Nuevo Lab activado | Verificar que el Lab tiene acceso a KOs compartidos relevantes. |

### Antes de publicación externa

Si conocimiento va a ser publicado fuera del ecosistema LabOS: [Decisión]

| Verificación | Descripción |
|-------------|-------------|
| Auditoría completa de procedencia | Toda la cadena debe ser verificable y sin BROKEN. |
| Freshness check | Solo conocimiento CURRENT es publicable externamente. |
| Sensibilidad confirmada | Verificar que no contiene información PRIVATE embebida. |
| Confianza ≥ MEDIO | No publicar externamente con confianza BAJO. |

### Antes de uso de alto riesgo (financiero/legal)

Cuando un KO informa decisiones con impacto financiero o legal significativo: [Decisión]

| Gate adicional | Descripción |
|---------------|-------------|
| Confianza ALTO requerida | No actuar sobre conocimiento con confianza MEDIO o BAJO en decisiones financieras irreversibles. |
| Procedencia COMPLETE | La cadena completa debe ser auditable. |
| Freshness CURRENT | No basar decisiones financieras en conocimiento que podría estar desactualizado. |
| Sin disputas activas | No usar KOs en `disputed` para decisiones de alto impacto. |

---

## Qué NO se revisa mensualmente

La revisión mensual es de excepciones y flags, no de todos los KOs: [Decisión]

- NO se revisa cada KO individualmente cada mes. [Decisión]
- NO se re-evalúa confianza de KOs CURRENT sin trigger. [Decisión]
- NO se verifica procedencia de KOs estables sin señal de cambio en fuentes. [Decisión]
- NO se re-clasifica sensibilidad sin motivo. [Decisión]

El sistema opera por excepción: solo se revisa lo que tiene flags activos (freshness expirada, disputas, huérfanos, etc.). [Decisión]

---

## Nota sobre el camino rápido (≤2 minutos)

El camino rápido de validación (captured → validated en ≤2 minutos) es un objetivo de usabilidad operativa, NO una garantía ni un SLA. [Decisión]

| Aspecto | Regla |
|---------|-------|
| Aplicabilidad | Para KOs de bajo riesgo con procedencia clara y confianza asignable rápidamente. [Decisión] |
| NO aplica a | KOs de alto impacto financiero, KOs AI-generated sin supervisión, KOs que contradigan conocimiento existente. [Decisión] |
| Subordinado a calidad | Si los 4 criterios del gate no se cumplen en 2 minutos, el KO permanece en `captured` — no se baja el estándar para cumplir el tiempo. [Decisión] |
| No es SLA | Es un target de diseño para mantener el overhead bajo. No genera obligación ni penalización si se excede. [Decisión] |

---

## Triggers de complejidad dormiente (gobernanza futura)

El modelo actual asume 1 fundador controlando todo. Se expandirá cuando se active alguno de estos triggers: [Decisión]

| Trigger | Gobernanza adicional requerida |
|---------|-------------------------------|
| Múltiples contribuidores activos | Delegación de rol Reviewer. Definir quién puede validar qué. [Visión] |
| Consumidores externos (no-Lab) | Gobernanza de publicación. Responsabilidad legal de contenido publicado. [Visión] |
| Uso regulado (financiero/legal) | Revisión de compliance. Auditoría formal de procedencia. [Visión] |
| ≥3 Labs con operadores distintos | Gobernanza cross-Lab. Resolución de conflictos multi-parte. [Visión] |
| Ownership delegada | Workflows de aprobación. Niveles de autoridad. [Visión] |
| Revenue material dependiente de conocimiento | SLAs de freshness. Garantías de calidad. [Visión] |
| Disputas recurrentes sin resolución | Comité de conflictos o proceso de escalación formal. [Visión] |

**Hasta que se active un trigger, el modelo SOLO prevalece.** [Decisión] Ninguna de las expansiones anteriores se implementa preventivamente.

---

## Cross-references

- [knowledge-ownership.md](./knowledge-ownership.md) — 6 roles, propiedad por estado
- [knowledge-sharing.md](./knowledge-sharing.md) — Reglas de publicación y compartición
- [knowledge-quality-gates.md](./knowledge-quality-gates.md) — Criterios de transición por gate
- [knowledge-lifecycle.md](./knowledge-lifecycle.md) — 8 estados, transiciones válidas
- [knowledge-freshness.md](./knowledge-freshness.md) — Estados de freshness, revisión
- [knowledge-conflict-resolution.md](./knowledge-conflict-resolution.md) — Proceso de resolución, 30 días max
- [knowledge-source-of-truth.md](./knowledge-source-of-truth.md) — Duplicados, reconciliación
- [knowledge-to-asset-handoff.md](./knowledge-to-asset-handoff.md) — Handoff Knowledge → Asset
- [knowledge-to-capability-handoff.md](./knowledge-to-capability-handoff.md) — Capability dormida
- [ai-agent-knowledge-contract.md](./ai-agent-knowledge-contract.md) — Permisos y restricciones de agentes IA
- [knowledge-architecture-principles.md](./knowledge-architecture-principles.md) — Principio 6 (proporcionalidad)
- [Architecture Baseline v1.0](../../architecture/architecture-baseline-v1.md) — Gobernanza SOLO, INV-05

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 0        | 0%         |
| [Hipótesis]   | 0        | 0%         |
| [Decisión]    | 42       | 86%        |
| [Visión]      | 7        | 14%        |
