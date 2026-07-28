# Propiedad del Conocimiento

## Propósito

Este documento define quién es responsable de cada Knowledge Object a lo largo de su ciclo de vida completo. [Decisión] Establece roles, reglas de transferencia y el modelo de propiedad para gobernanza SOLO (1 fundador).

---

## Distinción fundamental: propiedad ≠ autoría ≠ autoridad canónica

Tres conceptos separados que no deben confundirse: [Decisión]

| Concepto | Definición | Ejemplo |
|----------|-----------|---------|
| **Autoría** | Quién produjo el contenido del KO. | Un agente IA genera una síntesis de 5 papers sobre latencia de exchanges. |
| **Propiedad** | Quién es responsable de mantenerlo actualizado y decidir su destino. | El fundador es owner aunque el agente IA sea el autor. |
| **Autoridad canónica** | Quién puede promover a Capa 3 y declarar como canónico. | Solo el fundador en nivel SOLO. |

Un Lab puede crear conocimiento que LabOS eventualmente posee (tras promoción a LabOS-Shared). [Hecho] Un agente IA puede ser autor de conocimiento cuyo owner es el fundador. [Hecho] La autoría es permanente e inmutable; la propiedad puede transferirse. [Decisión]

---

## Roles en el ciclo de vida del KO

| Rol | Definición | Quién lo ocupa (nivel SOLO) |
|-----|-----------|----------------------------|
| **Creator** | Quien produce el contenido del KO. | Fundador, agente IA, o fuente externa importada. |
| **Originating Lab** | Lab donde se generó el conocimiento. | El Lab activo que ejecutó la investigación o capturó el insight. |
| **Current Owner** | Lab o entidad responsable de mantener el KO actualizado. | El Lab de origen (por defecto) o LabOS (tras promoción). |
| **Reviewer** | Quien valida contenido y asigna confianza. | Fundador (único reviewer en nivel SOLO). |
| **Canonical Authority** | Quien puede promover a Capa 3. | Fundador (exclusivamente). |
| **Consumer** | Quien usa el KO para decisiones, activos o procesos. | Otros Labs, decisiones del fundador, agentes IA futuros. |

**Para gobernanza SOLO:** el fundador ocupa TODOS los roles simultáneamente. [Decisión] La separación de roles es conceptual — existe para escalar en el futuro sin reestructurar la arquitectura. No se requiere aprobación multi-persona para ninguna transición. [Decisión]

---

## Reglas de propiedad por origen

### Conocimiento generado dentro de un Lab

| Origen | Creator | Owner | Regla |
|--------|---------|-------|-------|
| Fundador investiga y sintetiza | Fundador | Lab donde investiga | El fundador es creator Y owner simultáneamente. [Decisión] |
| Agente IA sintetiza por instrucción del fundador | Agente IA | Lab del fundador | Agente es creator, fundador retiene ownership y autoridad. La máquina no posee conocimiento. [Decisión] |
| Captura de fuente externa (paper, API docs, etc.) | Lab que importó | Lab que importó | El Lab posee la versión sintetizada, no la fuente original. [Decisión] |
| Observación operativa directa | Fundador | Lab donde se observó | Conocimiento operativo pertenece al Lab de contexto. [Decisión] |

### Conocimiento compartido (LabOS-Shared)

| Escenario | Owner antes | Owner después | Condición |
|-----------|-------------|---------------|-----------|
| Promoción Lab-Private → LabOS-Shared | Lab de origen | LabOS | El Lab retiene atribución como Originating Lab, pero la responsabilidad de mantenimiento pasa a LabOS. [Decisión] |
| Conocimiento metodológico creado directamente para LabOS | LabOS | LabOS | Conocimiento que nace como infraestructura transversal. [Decisión] |
| Cross-Lab knowledge | Labs participantes | LabOS (si se promueve) | Co-propiedad documentada hasta promoción. [Decisión] |

### Conocimiento AI-asistido

El modelo de propiedad para conocimiento generado con asistencia de IA: [Decisión]

1. **El agente IA NUNCA es owner.** La autoridad humana prevalece siempre. [Decisión]
2. El campo `author_or_agent` registra qué agente participó en la creación. [Decisión]
3. La verificación humana (campo `human_verification_status` en provenance) determina si el KO está listo para validación. [Decisión]
4. Un KO creado enteramente por agente IA permanece en `captured` hasta revisión humana. [Decisión]

---

## Transferencia de propiedad

La propiedad de un KO puede transferirse en las siguientes situaciones: [Decisión]

| Situación | Desde | Hacia | Requisito |
|-----------|-------|-------|-----------|
| Promoción a LabOS-Shared | Lab de origen | LabOS | Cumplir criterios de universalidad (ref: [knowledge-boundaries.md](./knowledge-boundaries.md)). |
| Lab archivado/pausado con KO compartido | Lab pausado | LabOS | Si el KO era Lab-Published o LabOS-Shared, permanece con LabOS. |
| Lab archivado/pausado con KO privado | Lab pausado | Congelado | KO Lab-Private se congela (no se transfiere, no se elimina). [Decisión] |
| Reasignación explícita por fundador | Lab A | Lab B | Decisión documentada en ≤1 oración con motivo. |

**Toda transferencia de ownership requiere documentación explícita.** [Decisión] Formato mínimo: "Ownership de KO-XXX-NNN transferido de [Lab A] a [Lab B/LabOS] porque [motivo en 1 oración]." No se requiere más formalidad en nivel SOLO.

---

## Conocimiento huérfano

Un KO es **huérfano** cuando: [Decisión]

- Su Lab de origen fue archivado/pausado Y el KO es Lab-Private (congelado sin mantenedor activo). [Hecho]
- El KO no fue revisado dentro de su validity_window Y ningún Lab lo reclama. [Hecho]
- El Originating Lab ya no existe en el portafolio. [Hecho]

**Proceso para conocimiento huérfano:** [Decisión]

1. Se detecta durante la revisión mensual de conocimiento (dentro del overhead ≤2h/mes). [Decisión]
2. Se flag como "huérfano" con fecha de detección. [Decisión]
3. Dentro de 30 días el fundador decide: reasignar a otro Lab, promover a LabOS-Shared, o archivar. [Decisión]
4. Si no se decide en 30 días → se archiva automáticamente con motivo "huérfano no reclamado". [Decisión]

---

## Propiedad por estado del lifecycle

| Estado | Owner típico | Acción del owner |
|--------|-------------|------------------|
| `captured` | Lab que capturó | Decidir si validar o archivar. |
| `under_review` | Lab de origen + Reviewer (fundador) | Evaluar y decidir transición. |
| `validated` | Lab de origen | Mantener actualizado, usar para decisiones. |
| `canonical` | Lab de origen o LabOS (si compartido) | Proteger estabilidad, revalidar periódicamente. |
| `disputed` | Lab de origen + fundador como árbitro | Resolver conflicto. |
| `superseded` | Nadie activamente (histórico) | Preservar para trazabilidad. |
| `deprecated` | Nadie activamente (histórico) | Preservar para trazabilidad. |
| `archived` | Sistema (almacenamiento) | Solo reactivación excepcional por fundador. |

---

## Ejemplo completo

**(EJEMPLO: Crypto Scalping Core)**

```text
KO-CSC-017: "Spread BTC/USDT se ensancha 02:00-04:00 UTC"

- Creator: Fundador (investigación directa con datos de API)
- Originating Lab: Crypto Scalping Core
- Current Owner: Crypto Scalping Core (Lab-Private)
- Reviewer: Fundador
- Canonical Authority: Fundador
- Consumers: Crypto Scalping Core (decisión de timing operativo)

Si el fundador decide publicar este KO al ecosistema:
- Current Owner → LabOS (tras promoción a LabOS-Shared)
- Originating Lab → Crypto Scalping Core (atribución permanente)
- Motivo documentado: "Útil para Atlas Wealth Labs en evaluación de mercados crypto"
```

---

## Triggers de complejidad dormiente

El modelo actual asume 1 fundador = todos los roles. [Hecho] Se expandirá cuando: [Decisión]

| Trigger | Impacto |
|---------|---------|
| Primer operador distinto al fundador | Se necesita definir quién puede ser Reviewer además del fundador. |
| Primer agente IA con autonomía de escritura | Se necesita definir límites de creación autónoma vs supervisada. |
| ≥3 Labs activos produciendo conocimiento | Se necesita governance para conflictos de ownership inter-Lab. |

Hasta que se active un trigger, el modelo simplificado prevalece. [Decisión]

---

## Cross-references

- [knowledge-lifecycle.md](./knowledge-lifecycle.md) — Estados que determinan acciones del owner
- [knowledge-boundaries.md](./knowledge-boundaries.md) — Criterios de promoción Lab → LabOS
- [knowledge-object-contract.md](./knowledge-object-contract.md) — Campo `domain` y `author_or_agent`
- [knowledge-layers.md](./knowledge-layers.md) — Owner por capa
- [knowledge-provenance.md](./knowledge-provenance.md) — Trazabilidad de autoría
- [Architecture Baseline v1.0](../../architecture/architecture-baseline-v1.md) — Sección 5: Propiedad de Entidades, Sección 6: Gobernanza SOLO
- [ADR-0001](../../decisions/0001-terminology-hierarchy.md) — Jerarquía terminológica

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 6        | 14%        |
| [Hipótesis]   | 0        | 0%         |
| [Decisión]    | 36       | 86%        |
| [Visión]      | 0        | 0%         |
