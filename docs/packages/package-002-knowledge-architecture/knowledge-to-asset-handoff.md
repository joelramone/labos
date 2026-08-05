# Handoff Conocimiento → Activo

## Propósito

Este documento define el puente crítico entre la etapa Knowledge y la etapa Assets dentro del Knowledge-to-Value Pipeline (Research → **Knowledge** → **Assets** → Products → Revenue). [Decisión] Establece cuándo, cómo y bajo qué criterios un Knowledge Object se transforma en un Asset reutilizable.

---

## Principio fundamental

**No todo conocimiento se convierte en activo.** [Decisión]

El handoff es selectivo. La mayoría de los KOs cumplen su función informando decisiones o alimentando otros KOs sin necesidad de convertirse en Asset. Solo el conocimiento que demuestra potencial de reutilización, estabilidad y valor independiente amerita la inversión de crear un Asset formal.

---

## Criterios de elegibilidad para handoff

Un KO debe cumplir TODOS los siguientes criterios para ser candidato a handoff: [Decisión]

| Criterio | Mínimo requerido | Justificación |
|----------|-----------------|---------------|
| Estado lifecycle | `validated` o `canonical` | Conocimiento en `captured`, `disputed` o `deprecated` no tiene la madurez necesaria. [Decisión] |
| Confianza | MEDIO o ALTO | Solo conocimiento con base sólida justifica inversión en Asset. [Decisión] |
| Procedencia | PARTIAL o superior (COMPLETE, INDIRECT) | El Asset necesita trazabilidad a sus fuentes. [Decisión] |
| Freshness | CURRENT o REVIEW_DUE | No crear Assets a partir de conocimiento potencialmente obsoleto. [Decisión] |
| Reutilización | El conocimiento puede empaquetarse en uno de los 7 tipos de Asset sin perder su valor esencial. | Si solo tiene valor dentro de su contexto original, no es candidato. [Decisión] |
| Independencia | El Asset resultante puede usarse sin leer el contexto completo de investigación. | Conocimiento que solo tiene sentido leyendo toda la research no genera Asset standalone. [Decisión] |

---

## Condiciones de trigger (cuándo considerar handoff)

Estas señales indican que un KO es candidato a convertirse en Asset: [Decisión]

| Señal | Descripción | Fuerza de señal |
|-------|-------------|-----------------|
| Demanda interna | El KO ha sido referenciado por ≥2 otros documentos/decisiones. | Fuerte. [Decisión] |
| Potencial de reuso | El KO responde una pregunta que probablemente se hará de nuevo (patrón repetible). | Moderada. [Decisión] |
| Hipótesis de monetización | El KO tiene potencial comercial identificable (per Asset_First_Model). | Fuerte. [Decisión] |
| Estabilidad | El KO ha sido estable por ≥1 ciclo de revisión completo sin cambios MAJOR. | Moderada. [Decisión] |
| Obligación Asset_First_Model | Investigación >4h → al menos 1 Asset O nota de cierre. | Obligatoria cuando aplica. [Hecho] |

**Nota sobre Asset_First_Model:** La regla de Package 000 establece que investigación >4h acumuladas debe producir al menos un activo. [Hecho] Este handoff es el MECANISMO para cumplir esa regla. Pero: no todo KO individual necesita convertirse en Asset — solo aquellos que cumplen elegibilidad y tienen señal de trigger.

---

## Qué cambia durante el handoff

| Aspecto | Antes del handoff | Después del handoff |
|---------|-------------------|---------------------|
| Entidades | Solo existe el KO. | Existe el KO + existe un Asset nuevo (entidad separada). [Decisión] |
| Lifecycle del Asset | — | Inicia en `borrador` (per ADR-0002: borrador → validado → productizado). [Hecho] |
| Referencia cruzada | — | El Asset referencia el/los KO(s) fuente en su metadata. [Decisión] |
| KO original | En su estado actual. | Persiste sin cambios — no se consume ni se elimina. [Decisión] |
| Ownership | Lab posee el KO. | El Asset pertenece al mismo Lab que posee el KO fuente (o a LabOS si el KO es compartido). [Decisión] |

---

## Qué NO cambia durante el handoff

| Aspecto | Regla |
|---------|-------|
| Estado del KO | El KO permanece en su lifecycle state actual (`validated`, `canonical`). No se altera. [Decisión] |
| Ownership del KO | No se transfiere. El KO sigue perteneciendo a su owner actual. [Decisión] |
| Procedencia del KO | No se modifica. La cadena de procedencia del KO permanece intacta. [Decisión] |
| Confianza del KO | No se altera por el hecho de haber generado un Asset. [Decisión] |

---

## Relaciones KO ↔ Asset

Las relaciones son many-to-many: [Decisión]

| Relación | Descripción |
|----------|-------------|
| 1 KO → múltiples Assets | Un mismo KO puede contribuir como fuente a varios Assets diferentes. [Decisión] |
| Múltiples KOs → 1 Asset | Un Asset puede sintetizar información de varios KOs. [Decisión] |
| KO independiente del Asset | El KO tiene valor propio — si el Asset se depreca, el KO sigue siendo válido. [Decisión] |

---

## Trazabilidad obligatoria

**Todo Asset DEBE referenciar al menos un KO fuente** (knowledge_id). [Decisión]

Esta referencia crea la cadena de auditoría completa:

```text
Asset → Knowledge Object(s) → Research/Evidence → Source
```

Sin esta referencia, el Asset pierde su conexión con el pipeline y no puede auditarse su origen. [Hecho]

---

## Propagación de actualizaciones

Cuando un KO fuente cambia DESPUÉS de que el Asset fue creado: [Decisión]

| Evento en el KO fuente | Efecto en el Asset |
|------------------------|-------------------|
| KO es `superseded` | El Asset se marca para revisión: ¿sigue siendo válido sin el KO original? [Decisión] |
| KO es `deprecated` | El Asset se marca para revisión: ¿tiene validación independiente? [Decisión] |
| KO cambia versión MAJOR | El Asset se evalúa: ¿el cambio invalida el Asset o es compatible? [Decisión] |
| KO cambia versión MINOR | Sin efecto — el Asset no necesita revisión. [Decisión] |

**Regla clave:** El Asset NO se invalida automáticamente cuando su KO fuente cambia. [Decisión] El Asset puede tener validación independiente (uso real, feedback de usuarios, pruebas propias). El owner del Asset decide si actualizar, mantener o deprecar.

---

## Criterios de rechazo (cuándo NO crear un Asset)

| Criterio | Razón |
|----------|-------|
| El conocimiento es demasiado específico de un momento temporal. | Assets deben tener vida útil razonable. Conocimiento operativo efímero no justifica la inversión. [Decisión] |
| El conocimiento requiere contexto completo de research para ser útil. | El Asset debe ser standalone — si necesita 20 páginas de contexto, no es un buen Asset. [Decisión] |
| El conocimiento es PRIVATE sin audiencia externa. | Si nadie más que el Lab lo usaría, y el Lab ya lo tiene como KO, crear un Asset es overhead sin valor. [Decisión] |
| Crear el Asset tomaría >4h sin hipótesis clara de reuso. | La inversión de creación debe justificarse con expectativa de retorno. [Decisión] |
| El conocimiento está en estado `disputed` o tiene confianza BAJO. | Inestable o poco confiable — no se invierte en empaquetar algo que puede cambiar. [Decisión] |

---

## Mapping KO types → Asset types más comunes

| Tipo de KO | Asset type más natural | Ejemplo |
|------------|----------------------|---------|
| `finding` | Documento, Dataset | Análisis publicable, dataset curado. [Hecho] |
| `methodology` | Template, Playbook, Framework | Plantilla de proceso, guía paso a paso. [Hecho] |
| `decision-context` | Documento | Guía de decisión para un dominio. [Hecho] |
| `market-insight` | Documento, Dataset | Reporte de mercado, datos curados. [Hecho] |
| `technical-insight` | Herramienta, Documento | Script útil, guía técnica. [Hecho] |
| `operational` | Playbook, Template | Procedimiento operativo estandarizado. [Hecho] |

Estos mappings son tendencias, no restricciones. [Hecho] Cualquier tipo de KO puede generar cualquier tipo de Asset.

---

## Conexión con Asset_First_Model

| Aspecto | Regla del Asset_First_Model | Cómo este handoff lo implementa |
|---------|----------------------------|--------------------------------|
| Investigación >4h → ≥1 Asset | Obligación (ref: [007-company-model.md](../package-000-foundation/007-company-model.md)). | Este handoff es el mecanismo de conversión. Los KOs producidos por la investigación son candidatos. [Hecho] |
| Asset requiere 5 campos mínimos | Nombre, tipo, descripción, hipótesis de uso, estado. | El Asset creado durante handoff inicia en `borrador` y debe cumplir los 5 campos. [Hecho] |
| Nota de cierre si no hay Asset | Si la investigación no produce Asset, se documenta motivo. | Si ningún KO de la investigación cumple elegibilidad, se genera nota de cierre. [Decisión] |

**Clarificación importante:** No todo KO individual activa la obligación del Asset_First_Model. [Decisión] La obligación aplica a la investigación en su conjunto (>4h acumuladas), no a cada KO producido. KOs pequeños de observaciones rápidas no generan obligación de Asset.

---

## Ejemplo de handoff

**(EJEMPLO: Crypto Scalping Core)**

```text
KO fuente (canónico):
  KO-CSC-017: "Spread BTC/USDT se ensancha 40-60% durante 02:00-04:00 UTC"
  KO-CSC-023: "Ventanas óptimas de operación: 09:00-11:00 UTC y 14:00-16:00 UTC"
  KO-CSC-028: "Correlación entre volumen y spread: <$50M/h → spread >0.04%"

  Señales de trigger:
  - Los 3 KOs son referenciados por decisiones de timing operativo.
  - Responden una pregunta recurrente: "¿cuándo operar?"
  - Estables por >60 días.

  ↓ handoff ↓

Asset creado:
  - Nombre: "Guía de ventanas óptimas de trading para BTC/USDT en Binance"
  - Tipo: playbook
  - Estado: borrador
  - Descripción: "Guía que sintetiza 3 hallazgos sobre timing de operación
    en BTC/USDT, combinando análisis de spread, volumen y ventanas horarias."
  - Hipótesis de uso: "Operador de trading algorítmico que necesita
    configurar ventanas de operación basadas en evidencia."
  - source_knowledge: [KO-CSC-017, KO-CSC-023, KO-CSC-028]

Los 3 KOs permanecen independientes, válidos y referenciables.
El playbook es una NUEVA entidad con su propio lifecycle de Asset.
```

---

## Cross-references

- [knowledge-lifecycle.md](./knowledge-lifecycle.md) — Estados elegibles para handoff (validated, canonical)
- [knowledge-confidence-model.md](./knowledge-confidence-model.md) — Confianza mínima MEDIO para handoff
- [knowledge-provenance.md](./knowledge-provenance.md) — Procedencia mínima PARTIAL para handoff
- [knowledge-freshness.md](./knowledge-freshness.md) — Freshness CURRENT/REVIEW_DUE para handoff
- [knowledge-classification.md](./knowledge-classification.md) — 6 tipos de KO → mapping a Asset types
- [knowledge-ownership.md](./knowledge-ownership.md) — Ownership del Asset derivado
- [knowledge-versioning.md](./knowledge-versioning.md) — MAJOR version change → revisión de Asset
- [ADR-0002](../../decisions/0002-asset-taxonomy-consolidation.md) — 7 tipos canónicos de Asset
- [007-company-model.md](../package-000-foundation/007-company-model.md) — Asset_First_Model, criterio mínimo de activo
- [Architecture Baseline v1.0](../../architecture/architecture-baseline-v1.md) — Pipeline Knowledge → Assets

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 12       | 21%        |
| [Hipótesis]   | 0        | 0%         |
| [Decisión]    | 44       | 79%        |
| [Visión]      | 0        | 0%         |
