# Vigencia del Conocimiento (Freshness)

## Propósito

Este documento formaliza el sistema de ventanas de validez y detección de obsolescencia para Knowledge Objects. [Decisión] Operacionaliza el Principio 4 (El conocimiento tiene fecha de caducidad) de [knowledge-architecture-principles.md](./knowledge-architecture-principles.md).

---

## Ventanas de validez por defecto

Las ventanas de validez son DEFAULTS configurables, no límites rígidos: [Decisión]

| Capa | Rango permitido | Default | Significado |
|------|----------------|---------|-------------|
| Capa 1 — Capturado | 7-30 días | 14 días | Conocimiento reciente que debe validarse rápido o descartarse. [Decisión] |
| Capa 2 — Validado | 30-90 días | 60 días | Conocimiento de trabajo útil para operación a mediano plazo. [Decisión] |
| Capa 3 — Canónico | 90-365 días | 180 días | Conocimiento estable referenciado activamente. [Decisión] |

### Configuración por dominio

Las ventanas son configurables con rationale explícito por dominio: [Decisión]

| Dominio | Ventana sugerida (Capa 3) | Justificación |
|---------|--------------------------|---------------|
| Datos de mercado crypto | 7-30 días (incluso en Capa 3) | Alta volatilidad, condiciones cambian semanalmente. (EJEMPLO: Crypto Scalping Core). [Decisión] |
| Conocimiento metodológico | 365 días | Procesos y métodos son estables por naturaleza. [Decisión] |
| Conocimiento regulatorio | Event-driven (sin ventana fija) | Se revisa cuando hay cambio regulatorio, no por calendario. [Decisión] |
| Infraestructura técnica | 90-180 días | APIs y herramientas cambian con releases, pero no diariamente. [Decisión] |
| Conocimiento operacional | 30-60 días | Procesos operativos evolucionan con la práctica. [Decisión] |

---

## Estados de freshness

| Estado | Definición | Acción requerida |
|--------|-----------|------------------|
| **CURRENT** | Dentro de ventana de validez, ningún trigger de revisión activo. [Decisión] | Ninguna — estado óptimo. |
| **REVIEW_DUE** | Ventana de validez expirada, pendiente de revisión. [Decisión] | Revisar contenido en próxima sesión de mantenimiento. |
| **STALE** | Revisión pendiente >14 días desde expiración de ventana. [Decisión] | Priorizar revisión. Flag visible en cualquier consumo del KO. |
| **EXPIRED** | Stale >30 días sin revisar. Candidato a deprecación. [Decisión] | Fundador decide: revalidar (actualiza fechas) o deprecar. |
| **SUPERSEDED** | Reemplazado por KO más reciente. Freshness ya no es relevante. [Decisión] | Ninguna — el nuevo KO es la referencia activa. |
| **UNKNOWN** | Recién capturado, validity_window no evaluada aún. [Decisión] | Asignar ventana de validez apropiada al dominio. |

---

## Fechas clave del sistema de freshness

| Fecha | Descripción | Fuente |
|-------|-------------|--------|
| `created_date` | Cuándo se creó el KO. | Campo obligatorio del [Knowledge Object Contract](./knowledge-object-contract.md). [Hecho] |
| `last_reviewed_date` | Cuándo se revisó por última vez el contenido como vigente. | Campo opcional, recomendado para Capa 2+. [Decisión] |
| `next_review_date` | Calculado: `last_reviewed_date` + `validity_window`. | Derivado, no almacenado explícitamente en etapa pre-software. [Decisión] |
| `expiration_date` | `next_review_date` + 14 días (período de gracia). | Derivado. Tras esta fecha, el KO pasa a STALE. [Decisión] |

### Cálculo de freshness status

```text
SI last_reviewed_date + validity_window > hoy → CURRENT
SI last_reviewed_date + validity_window ≤ hoy → REVIEW_DUE
SI last_reviewed_date + validity_window + 14 días ≤ hoy → STALE
SI last_reviewed_date + validity_window + 44 días ≤ hoy → EXPIRED
```

Para KOs sin `last_reviewed_date`: usar `created_date` como base de cálculo. [Decisión]

---

## Triggers de revisión (conceptuales, no automatizados)

Más allá de la expiración de ventana, estos eventos también disparan revisión: [Decisión]

| Trigger | Descripción | Urgencia |
|---------|-------------|----------|
| Ventana de validez expirada | El KO superó su `validity_window` sin revisión. | Normal — incluir en próxima revisión mensual. |
| Nueva evidencia contradictoria | Se descubre información que contradice el KO. | Alta — evaluar si requiere transición a `disputed`. |
| Fuente actualizada o retractada | La fuente original cambió significativamente. | Alta — verificar si el KO sigue siendo válido. |
| Cambio regulatorio externo | Nueva regulación afecta el dominio del KO. | Alta — revisar independientemente de ventana. |
| Versión de plataforma/herramienta | Tool o API referenciada cambió de versión. | Media — verificar en próximo ciclo. |
| Experimento fallido que contradice | Un experimento produce resultado opuesto al KO. | Alta — candidato a `disputed`. |
| Cambio de objetivo de negocio | Nuevo objetivo recontextualiza el KO. | Media — revisar relevancia. |
| Cambio de ownership del Lab | Lab pausado o transferido. | Media — verificar si KO queda huérfano. |
| ADR que modifica decisiones relevantes | Arquitectura cambia en forma que afecta el KO. | Alta — revisar consistencia. |

**Implementación actual:** En etapa pre-software, estos triggers se detectan durante la revisión mensual de conocimiento (overhead ≤2h/mes). [Decisión] El fundador mantiene consciencia de cambios externos relevantes como parte de su operación normal.

---

## Relación freshness ↔ confianza

Freshness y confianza son dimensiones DIFERENTES pero se influyen mutuamente: [Decisión]

| Freshness | Confianza | Interpretación |
|-----------|-----------|---------------|
| CURRENT + ALTO | Estado ideal. Conocimiento actual y bien soportado. |
| CURRENT + BAJO | Recién capturado, poco evidencia. Normal para Capa 1. |
| STALE + ALTO | Dominio estable, probablemente sigue siendo válido pero DEBE revisarse. No degradar automáticamente. [Decisión] |
| STALE + BAJO | Conocimiento débil y viejo. Candidato fuerte a deprecación. |
| EXPIRED + cualquiera | Requiere acción inmediata: revalidar o deprecar. |

**Reglas clave:** [Decisión]

1. Freshness STALE/EXPIRED → flag para revisión de confianza, NO degradación automática.
2. Un KO CURRENT puede tener confianza BAJA (recién capturado, poca evidencia).
3. Un KO STALE puede mantener confianza ALTA si el dominio es estable (tras revisión que confirme).
4. Freshness es sobre TIEMPO transcurrido; confianza es sobre CALIDAD de evidencia.
5. La revisión de freshness PUEDE resultar en downgrade de confianza si se descubre que las condiciones cambiaron.

---

## Proceso de revisión de freshness

Cuando un KO entra en REVIEW_DUE, el proceso es: [Decisión]

1. **Verificar vigencia:** ¿La afirmación sigue siendo válida con la información actual? (~2-5 minutos). [Decisión]
2. **Verificar fuentes:** ¿Las fuentes referenciadas siguen accesibles y sin cambios? (~1-2 minutos). [Decisión]
3. **Decidir:**
   - Si sigue vigente: actualizar `last_reviewed_date` → freshness vuelve a CURRENT. [Decisión]
   - Si cambió parcialmente: actualizar contenido del KO + `last_reviewed_date`. [Decisión]
   - Si ya no es válido: transicionar a `deprecated` o `superseded` según corresponda. [Decisión]
   - Si hay contradicción: transicionar a `disputed` (ref: [knowledge-conflict-resolution.md](./knowledge-conflict-resolution.md)). [Decisión]

**Overhead esperado por KO:** 3-7 minutos por revisión. [Hecho] Con el volumen estimado de KOs activos en año 1 (30-50 en Capa 2-3), el overhead mensual se mantiene dentro del límite de 1-2 horas. [Hipótesis]

---

## Ejemplo de evolución de freshness

**(EJEMPLO: Crypto Scalping Core)**

```text
KO-CSC-017: "Spread BTC/USDT se ensancha 40-60% durante 02:00-04:00 UTC"
- validity_window: 60 días (dominio crypto, datos de mercado)
- created_date: 2025-05-01
- last_reviewed_date: 2025-07-10

Timeline:
- 2025-07-10: Revisado → CURRENT
- 2025-09-08: validity_window expira (60 días) → REVIEW_DUE
- 2025-09-22: +14 días sin revisión → STALE
- 2025-10-08: +30 días desde expiración → EXPIRED
- 2025-10-08: Fundador revisa, Binance actualizó matching engine
  → Contenido parcialmente invalidado → transición a DISPUTED
```

---

## Cross-references

- [knowledge-architecture-principles.md](./knowledge-architecture-principles.md) — Principio 4 (Fecha de caducidad)
- [knowledge-object-contract.md](./knowledge-object-contract.md) — Campo `validity_window`, `last_reviewed_date`
- [knowledge-lifecycle.md](./knowledge-lifecycle.md) — Trigger automático de alerta de validez
- [knowledge-confidence-model.md](./knowledge-confidence-model.md) — Relación freshness↔confianza
- [knowledge-conflict-resolution.md](./knowledge-conflict-resolution.md) — Transición a `disputed` por obsolescencia
- [knowledge-layers.md](./knowledge-layers.md) — Ventanas de validez por capa
- [Architecture Baseline v1.0](../../architecture/architecture-baseline-v1.md) — INV-05 (Proporcionalidad)

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 2        | 5%         |
| [Hipótesis]   | 1        | 2%         |
| [Decisión]    | 39       | 93%        |
| [Visión]      | 0        | 0%         |
