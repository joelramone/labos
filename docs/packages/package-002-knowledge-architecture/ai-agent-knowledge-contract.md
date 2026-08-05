# Contrato de Conocimiento para Agentes IA

## Propósito

Este documento define los principios de diseño para la interacción futura de agentes IA con Knowledge Objects. [Decisión] Es un documento CONCEPTUAL — no implica implementación, no define APIs, no requiere software. Establece el marco de responsabilidades, permisos y restricciones que cualquier agente IA deberá respetar al consumir, citar o proponer cambios sobre conocimiento dentro del ecosistema LabOS.

---

## Estado: CONCEPTUAL / FUTURO [Decisión]

Este contrato se activará cuando exista al menos un agente IA consumiendo Knowledge Objects de forma autónoma (sin supervisión directa del fundador en cada consulta). [Decisión] Hasta ese momento, el fundador media toda interacción entre agentes y conocimiento.

---

## Responsabilidades del agente al consumir conocimiento

Todo agente IA que acceda a Knowledge Objects DEBE cumplir estas responsabilidades: [Decisión]

| # | Responsabilidad | Descripción |
|---|-----------------|-------------|
| 1 | Identificar KO canónico | Localizar el KO por su `knowledge_id` — no por contenido duplicado ni resúmenes. [Decisión] |
| 2 | Citar procedencia | Exponer el estado de procedencia (COMPLETE/PARTIAL/INDIRECT/UNVERIFIED/BROKEN) al usuario. [Decisión] |
| 3 | Exponer clasificación epistémica | Indicar si la afirmación es [Hecho], [Hipótesis], [Visión] o [Decisión]. [Decisión] |
| 4 | Exponer nivel de confianza | Comunicar si la confianza es ALTO, MEDIO, BAJO o UNKNOWN. [Decisión] |
| 5 | Exponer estado de freshness | Indicar si el KO es CURRENT, REVIEW_DUE, STALE, EXPIRED, SUPERSEDED o UNKNOWN. [Decisión] |
| 6 | Distinguir canónico de inferido | Separar explícitamente lo que proviene de un KO validado vs lo que el agente infiere o asume. [Decisión] |
| 7 | Identificar contenido disputado | Si el KO está en estado `disputed`, advertir al usuario antes de citar. [Decisión] |
| 8 | Identificar contenido superado | Si el KO está `superseded`, apuntar al sucesor y notar el contexto histórico. [Decisión] |
| 9 | Respetar sensibilidad | No exponer KOs PRIVATE a contextos no autorizados. No mezclar PRIVATE con PUBLIC sin autorización. [Decisión] |
| 10 | Respetar scope | Distinguir entre conocimiento Lab-local y LabOS-Shared. No tratar conocimiento de un Lab como universal. [Decisión] |
| 11 | Preservar atribución | Mantener visible el Originating Lab y el Current Owner en toda citación. [Decisión] |
| 12 | No tratar ejemplos como reglas | Los ejemplos "(EJEMPLO: Crypto Scalping Core)" ilustran — no constituyen conocimiento canónico generalizable. [Decisión] |
| 13 | No actualizar silenciosamente | Nunca modificar un KO canónico sin pasar por el proceso de propuesta y aprobación humana. [Decisión] |
| 14 | Indicar evidencia insuficiente | Cuando la base para una respuesta es débil (BAJO, UNVERIFIED, BROKEN), advertir explícitamente. [Decisión] |

---

## Acciones permitidas (permisos conceptuales)

| Acción | Descripción | Requisito |
|--------|-------------|-----------|
| **READ** | Acceder y consumir contenido de un KO. [Decisión] | Respetar sensibilidad y scope. |
| **SUMMARIZE** | Producir síntesis referenciando KO(s) fuente por `knowledge_id`. [Decisión] | Citar fuentes, no ocultar procedencia. |
| **COMPARE** | Evaluar múltiples KOs para identificar consistencia o tensiones. [Decisión] | Presentar ambos lados sin resolver unilateralmente. |
| **LINK** | Identificar relaciones semánticas entre KOs (similitud, dependencia, contradicción). [Decisión] | Proponer links, no crearlos canónicamente. |
| **PROPOSE_UPDATE** | Sugerir cambios a un KO existente basados en nueva evidencia. [Decisión] | Requiere aprobación humana para aplicar. |
| **PROPOSE_CONFLICT** | Señalar que un KO contradice otro KO o nueva información externa. [Decisión] | Presenta evidencia al fundador para resolución. |
| **REQUEST_REVIEW** | Solicitar que un KO sea revisado (freshness, calidad, relevancia). [Decisión] | Flag informativo — la decisión de revisar es humana. |

---

## Acciones que un agente NO puede realizar autónomamente

Estas acciones están PROHIBIDAS sin aprobación explícita del fundador: [Decisión]

| Acción prohibida | Justificación |
|------------------|---------------|
| Aprobar conocimiento como canónico (Capa 3) | Solo la Canonical Authority (fundador) puede promover. [Decisión] |
| Cambiar ownership de un KO | La propiedad es decisión humana con implicaciones de responsabilidad. [Decisión] |
| Remover procedencia de un KO | Destruir trazabilidad es irreversible y viola Principio 5. [Decisión] |
| Cambiar sensibilidad (PRIVATE↔PUBLIC) | Tiene implicaciones de seguridad y competitividad. [Decisión] |
| Resolver disputas a nivel de fundador | Conflictos de conocimiento canónico requieren juicio humano contextualizado. [Decisión] |
| Eliminar versiones históricas | La preservación histórica es inmutable (ref: [knowledge-versioning.md](./knowledge-versioning.md)). [Decisión] |
| Activar entidades dormidas (Capability) | Activación requiere ADR del fundador (ref: [knowledge-to-capability-handoff.md](./knowledge-to-capability-handoff.md)). [Decisión] |
| Publicar conocimiento PRIVATE | Publicación es acto explícito del owner, no del agente. [Decisión] |
| Promover conocimiento a Asset sin autoridad | El handoff Knowledge → Asset requiere elegibilidad verificada por el fundador. [Decisión] |

---

## Reglas para contenido generado por agentes IA

Cuando un agente IA produce nuevo contenido de conocimiento: [Decisión]

| Regla | Descripción |
|-------|-------------|
| No es automáticamente canónico | El contenido AI-generated entra al lifecycle en estado `captured`. [Decisión] |
| Identificar autor | El campo `author_or_agent` DEBE registrar el agente/modelo que produjo el contenido. [Decisión] |
| Vincular inputs | DEBE listar los KOs y evidencia utilizados como input para la generación. [Decisión] |
| Clasificación epistémica obligatoria | Todo output debe recibir clasificación ([Hecho]/[Hipótesis]/etc.) apropiada a la certeza. [Decisión] |
| Confianza inicial conservadora | Contenido AI-generated generalmente inicia con confianza BAJO o MEDIO — nunca ALTO sin verificación humana. [Decisión] |
| Riesgo de alucinación documentado | La justificación de confianza debe reconocer que el contenido fue generado por IA y puede contener imprecisiones. [Decisión] |
| Revisión humana obligatoria | Todo KO AI-generated DEBE pasar por `under_review` antes de alcanzar `validated`. [Decisión] |
| Usa lifecycle existente | El flujo es: `captured` → `under_review` → `validated` (si aprobado) o `archived` (si rechazado). [Hecho] |

---

## Comportamiento ante situaciones de fallo

| Situación | Comportamiento del agente |
|-----------|---------------------------|
| Procedencia BROKEN | Señalar al usuario que la cadena de trazabilidad está rota. No citar como fiable. [Decisión] |
| Confianza UNKNOWN o BAJO | Advertir al usuario. No usar como base para decisiones sin agregar caveat explícito. [Decisión] |
| Conocimiento STALE o EXPIRED | Señalar estado de freshness. Sugerir revisión antes de actuar. [Decisión] |
| Dos KOs en conflicto | Presentar ambos con sus respectivas procedencias y confianzas. No resolver unilateralmente. [Decisión] |
| Sensibilidad no clara | Tratar como PRIVATE (default restrictivo). No exponer hasta clarificación humana. [Decisión] |
| Ownership no clara | Señalar KO como potencialmente huérfano. Solicitar clarificación al fundador. [Decisión] |
| Fuente canónica inaccesible | Reportar estado BROKEN. No sustituir con fuente alternativa no verificada. [Decisión] |
| KO marcado SUPERSEDED | Apuntar al sucesor. Notar contexto histórico del original si es relevante. [Decisión] |
| Fuente externa contradice KO interno | Presentar ambas perspectivas. No sobrescribir conocimiento canónico interno con información externa. [Decisión] |

---

## Principio rector por defecto

> **No inferir autoridad silenciosamente.** [Decisión]
>
> El agente IA no asume que tiene permiso para actuar. Expone incertidumbre. Solicita revisión cuando la situación lo requiere. Preserva el registro canónico tal como existe. La modificación del conocimiento es prerrogativa humana.

---

## Relación con gobernanza SOLO

En nivel de gobernanza SOLO (1 fundador), el agente IA opera como herramienta del fundador, no como actor independiente. [Decisión] Implicaciones:

| Aspecto | Regla |
|---------|-------|
| Autonomía del agente | Limitada a READ, SUMMARIZE, COMPARE, LINK. Propuestas requieren aprobación. [Decisión] |
| Escalación | Toda situación no cubierta se escala al fundador. [Decisión] |
| Conflicto de autoridad | Si el agente y un KO canónico se contradicen, el KO canónico prevalece. [Decisión] |
| Volumen de propuestas | El agente no debe generar más propuestas de actualización de las que el fundador puede revisar en su overhead mensual (≤2h/mes). [Decisión] |

---

## Triggers de activación del contrato

Este contrato se vuelve operativamente relevante cuando: [Decisión]

| Trigger | Condición |
|---------|-----------|
| Agente consume KOs autónomamente | Un agente IA accede a KOs sin mediación directa del fundador por cada consulta. |
| Agente genera KOs | Un agente produce Knowledge Objects como parte de un workflow automatizado. |
| Múltiples agentes interactúan | Más de un agente consume o produce conocimiento en el mismo ecosistema. |

Hasta que se active un trigger, el fundador media toda interacción y este contrato sirve como principio de diseño para el futuro. [Decisión]

---

## Cross-references

- [knowledge-object-contract.md](./knowledge-object-contract.md) — Campos obligatorios, `author_or_agent`
- [knowledge-lifecycle.md](./knowledge-lifecycle.md) — Estados `captured`, `under_review`, `validated`
- [knowledge-ownership.md](./knowledge-ownership.md) — Agente IA NUNCA es owner
- [knowledge-provenance.md](./knowledge-provenance.md) — Requisitos para síntesis AI-generated
- [knowledge-confidence-model.md](./knowledge-confidence-model.md) — Confianza conservadora para AI-generated
- [knowledge-conflict-resolution.md](./knowledge-conflict-resolution.md) — Agente no resuelve disputas
- [knowledge-sharing.md](./knowledge-sharing.md) — Sensibilidad y scope
- [knowledge-classification.md](./knowledge-classification.md) — PRIVATE/PUBLIC, tipos funcionales
- [knowledge-freshness.md](./knowledge-freshness.md) — Estados de freshness
- [knowledge-governance.md](./knowledge-governance.md) — Roles y autoridad
- [Architecture Baseline v1.0](../../architecture/architecture-baseline-v1.md) — Gobernanza SOLO, INV-05

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 1        | 2%         |
| [Hipótesis]   | 0        | 0%         |
| [Decisión]    | 52       | 98%        |
| [Visión]      | 0        | 0%         |
