# Compartición del Conocimiento

## Propósito

Este documento define las reglas operativas para compartir Knowledge Objects entre Labs y con el ecosistema LabOS. [Decisión] Construye sobre los 4 tipos de boundary ([knowledge-boundaries.md](./knowledge-boundaries.md)), el modelo de propiedad ([knowledge-ownership.md](./knowledge-ownership.md)) y la clasificación de sensibilidad ([knowledge-classification.md](./knowledge-classification.md)).

---

## Elegibilidad para compartición

No todo conocimiento es elegible para ser compartido fuera de su Lab de origen. Un KO debe cumplir TODOS los siguientes criterios para ser elegible: [Decisión]

| Criterio | Mínimo requerido | Justificación |
|----------|-----------------|---------------|
| Estado lifecycle | `validated` (Capa 2+) | Conocimiento en `captured` no ha pasado revisión — compartirlo prematuramente puede propagar errores. [Decisión] |
| Procedencia | PARTIAL o superior (COMPLETE, INDIRECT) | Conocimiento con procedencia UNVERIFIED o BROKEN no tiene base trazable para que otros Labs confíen en él. [Decisión] |
| Sensibilidad | PUBLIC | Solo conocimiento clasificado como PUBLIC es compartible fuera del Lab. Conocimiento PRIVATE requiere promoción explícita primero. [Decisión] |
| Confianza | MEDIO o ALTO | Conocimiento con confianza BAJO no tiene madurez suficiente para uso cross-Lab. [Decisión] |

**Implicación práctica:** Un KO recién capturado (Capa 1, confianza UNKNOWN, PRIVATE por defecto) no es elegible por ningún criterio. Debe madurar antes de compartirse. [Hecho]

---

## Mecanismo de compartición: basado en referencias

El modelo de compartición es **reference-based**, no copy-based: [Decisión]

| Principio | Regla | Referencia |
|-----------|-------|-----------|
| Enlace a fuente canónica | Siempre referenciar — nunca copiar contenido. | Principio 2 (fuente única). [Decisión] |
| Fuente de verdad única | El Lab propietario mantiene la versión canónica. | [knowledge-source-of-truth.md](./knowledge-source-of-truth.md). [Decisión] |
| Atribución | El Lab de origen siempre se acredita como Originating Lab. | [knowledge-ownership.md](./knowledge-ownership.md). [Decisión] |
| Vigencia | El Lab propietario revisa per su `validity_window` definida. | [knowledge-freshness.md](./knowledge-freshness.md). [Decisión] |

**(EJEMPLO: Crypto Scalping Core)** Si Atlas Wealth Labs necesita usar el hallazgo KO-CSC-025 ("Metodología de evaluación de latencia de exchanges"), referencia el KO por su knowledge_id — no copia el contenido a sus propios documentos.

---

## Responsabilidades del owner (Lab que comparte)

Cuando un Lab comparte un KO al ecosistema, asume las siguientes responsabilidades: [Decisión]

| Responsabilidad | Descripción |
|-----------------|-------------|
| Mantener versión canónica | El Lab actualiza el contenido cuando hay nueva evidencia o cambio de contexto. [Decisión] |
| Actualizar índice compartido | Cuando el estado del KO cambia (deprecated, superseded), el Lab actualiza el índice compartido dentro de 7 días. [Decisión] |
| Notificar consumidores | Si el KO es deprecado o superado, la actualización del índice compartido sirve como notificación. [Decisión] |
| Responder a issues | Si un Lab consumidor reporta un problema con el KO compartido, el owner responde dentro de 14 días. [Decisión] |

---

## Responsabilidades del consumidor (Lab que usa conocimiento compartido)

| Responsabilidad | Descripción |
|-----------------|-------------|
| Referenciar por ID y versión | Citar el knowledge_id y la versión consultada. No copiar contenido. [Decisión] |
| Reportar problemas al owner | Si detecta que el KO está desactualizado o tiene errores, notifica al Lab owner. [Decisión] |
| No modificar el original | Si necesita una versión adaptada, crea un fork con atribución explícita al KO de origen. [Decisión] |
| Verificar freshness antes de usar | Antes de basar una decisión importante en un KO compartido, verificar que su freshness sea CURRENT o REVIEW_DUE. [Decisión] |

---

## Manejo de referencias desactualizadas (stale references)

| Escenario | Acción del consumidor |
|-----------|----------------------|
| KO referenciado pasa a STALE/EXPIRED | El consumidor lo detecta en su revisión mensual y decide si sigue confiando o busca alternativa. [Decisión] |
| KO referenciado es deprecado | El consumidor busca KO alternativo o elimina la dependencia de su operación. [Decisión] |
| KO referenciado se vuelve inaccesible | El consumidor marca la referencia como BROKEN en su propio registro y notifica vía índice compartido. [Decisión] |

**Overhead esperado:** La verificación de referencias compartidas se incluye dentro de la revisión mensual de conocimiento (dentro del límite de ≤2h/mes per Principio 6). [Decisión]

---

## Flujo de promoción: Lab-local → LabOS compartido

Cuando un KO local merece ser compartido a todo el ecosistema LabOS: [Decisión]

| Paso | Acción | Responsable |
|------|--------|-------------|
| 1 | El KO debe ser PUBLIC (campo `sensitivity`). Si es PRIVATE, primero se promociona a PUBLIC. | Lab owner. [Decisión] |
| 2 | El KO cumple criterios de universalidad: es útil para TODOS los Labs sin adaptación específica. | Fundador evalúa. [Decisión] |
| 3 | Ownership se transfiere del Lab de origen a LabOS. | Fundador documenta transferencia. [Decisión] |
| 4 | El Lab de origen retiene atribución permanente como Originating Lab. | Automático — no se pierde. [Hecho] |
| 5 | La decisión de promoción se documenta por el fundador en ≤1 oración con motivo. | Fundador. [Decisión] |

**Criterio de universalidad:** El KO debe ser útil tal cual (sin adaptación de dominio) para cualquier Lab del portafolio. [Decisión] Si requiere adaptación específica, no es candidato a LabOS-Shared — puede permanecer como Lab-Published.

---

## Flujo de consumo: compartido → uso local

Cuando un Lab consume conocimiento compartido del ecosistema: [Decisión]

| Aspecto | Regla |
|---------|-------|
| Referencia sin copia | Los Labs referencian KOs compartidos sin duplicar contenido en su propia documentación. [Decisión] |
| Decisiones locales | Las decisiones tomadas a partir de un KO compartido pertenecen al Lab que las toma. [Decisión] |
| Derivados | KOs derivados (síntesis de KO compartido + conocimiento local propio) pertenecen al Lab consumidor. [Decisión] |

**(EJEMPLO: Crypto Scalping Core)** Atlas Wealth Labs referencia KO-CSC-025 (metodología de latencia) y produce KO-AWL-008 (evaluación de latencia para sus propios exchanges de interés). KO-AWL-008 pertenece a Atlas Wealth Labs; KO-CSC-025 sigue perteneciendo a Crypto Scalping Core.

---

## Clarificación: PRIVATE vs PUBLIC vs Lab-local vs compartido

Dos ejes distintos que no deben confundirse: [Decisión]

| Eje | Qué describe | Valores |
|-----|-------------|---------|
| **Sensibilidad** (PRIVATE/PUBLIC) | Quién PUEDE acceder | PRIVATE = solo el Lab; PUBLIC = cualquier Lab del ecosistema. [Hecho] |
| **Scope** (Lab-local / LabOS compartido) | Dónde VIVE y quién MANTIENE | Lab-local = el Lab almacena y mantiene; LabOS compartido = LabOS almacena y mantiene. [Hecho] |

### Combinaciones válidas

| Sensibilidad | Scope | Descripción | Frecuencia |
|-------------|-------|-------------|------------|
| PRIVATE + Lab-local | Conocimiento del Lab, solo accesible internamente. | Más común (default). [Hecho] |
| PUBLIC + Lab-local | Publicado al ecosistema pero el Lab mantiene la versión canónica. | Lab-Published. [Hecho] |
| PUBLIC + LabOS compartido | Universal, LabOS mantiene. Todos los Labs acceden. | LabOS-Shared. [Hecho] |

### Combinación inválida

| Sensibilidad | Scope | Por qué es inválida |
|-------------|-------|---------------------|
| PRIVATE + LabOS compartido | Contradicción: si LabOS lo comparte al ecosistema, por definición es PUBLIC. [Decisión] |

---

## Compartición Interna Autorizada de Conocimiento PRIVATE

La clasificación PRIVATE no prohíbe toda compartición — prohíbe la publicación abierta al ecosistema. [Decisión] Un KO con sensibilidad PRIVATE puede ser compartido internamente entre Labs autorizados cuando se cumplen TODAS las siguientes condiciones: [Decisión]

| # | Condición | Descripción |
|---|-----------|-------------|
| 1 | El scope lo permite | El boundary del KO no excluye explícitamente al Lab receptor. [Decisión] |
| 2 | El owner lo autoriza | El Lab propietario del KO otorga autorización explícita y documentada. [Decisión] |
| 3 | El receptor tiene necesidad operativa legítima | El Lab consumidor necesita el KO para una decisión, investigación o proceso documentado. [Decisión] |
| 4 | Procedencia cumple el umbral | PARTIAL o superior (misma regla que compartición PUBLIC). [Decisión] |
| 5 | Confianza y freshness cumplen quality gate | MEDIO+ y CURRENT/REVIEW_DUE (misma regla que compartición PUBLIC). [Decisión] |
| 6 | Fuente canónica permanece controlada | El KO sigue almacenado y mantenido por el Lab propietario. No se transfiere ownership. [Decisión] |
| 7 | Acceso es reference-based | El Lab receptor referencia el KO por knowledge_id — no crea copia no gestionada. [Decisión] |
| 8 | Restricciones de reuso preservadas | Si el KO tiene `reuse_restrictions`, el receptor las respeta. [Decisión] |
| 9 | Revocabilidad | La autorización se revoca automáticamente si cambia la autorización, ownership o sensibilidad del KO. [Decisión] |
| 10 | Exclusiones absolutas | Información corporativa, de empleador, credenciales, secretos o material externamente restringido NUNCA se comparte, ni siquiera internamente. [Decisión] |

### Distinción clave: sensibilidad vs scope de compartición

| Concepto | Significado |
|----------|-------------|
| Sensibilidad PRIVATE | El KO no se publica al índice compartido del ecosistema. No cambia por compartición interna. [Decisión] |
| Compartición interna autorizada | Acceso controlado, documentado y revocable a un KO PRIVATE entre Labs específicos. [Decisión] |
| Publicación (cambio a PUBLIC) | El KO se publica abiertamente al ecosistema. Requiere cambio de sensitivity. [Hecho] |

**La compartición interna autorizada NO cambia la clasificación de sensibilidad.** [Decisión] El KO sigue siendo PRIVATE. Solo se otorga acceso controlado a un Lab específico para un propósito documentado.

### Formato de autorización (nivel SOLO)

Documentar en ≤2 oraciones: [Decisión]
- Qué KO se comparte (knowledge_id).
- Con quién (Lab receptor).
- Para qué propósito.

**(EJEMPLO: Crypto Scalping Core)** "KO-CSC-017 (spread nocturno BTC/USDT) compartido internamente con Atlas Wealth Labs para evaluar correlación crypto-commodities en ventanas de baja liquidez."

---

## Gobernanza SOLO para compartición

En nivel de gobernanza SOLO (1 fundador): [Decisión]

| Aspecto | Regla |
|---------|-------|
| Quién decide publicar | Fundador, directamente. [Decisión] |
| Formato de decisión | Cambiar campo `sensitivity` a PUBLIC + agregar `summary` ≤300 caracteres. [Decisión] |
| Aprobación | No se requiere aprobación formal — el fundador es el único decision-maker. [Decisión] |
| Retractabilidad | Un KO publicado puede retractarse en cualquier momento actualizando el índice compartido. [Decisión] |

---

## Triggers de complejidad dormiente

El modelo actual asume 1 fundador controlando todos los Labs. [Hecho] Se expandirá cuando: [Decisión]

| Trigger | Impacto |
|---------|---------|
| ≥3 Labs activos con operadores distintos | Se necesita governance formal para compartición (quién puede publicar en nombre de un Lab). |
| Primer consumidor externo (no-Lab) | Se necesita definir si PUBLIC incluye audiencias fuera del ecosistema LabOS. |
| ≥50 KOs compartidos en el índice | Se necesita mecanismo de descubrimiento y búsqueda. |

Hasta que se active un trigger, el modelo simplificado prevalece. [Decisión]

---

## Cross-references

- [knowledge-boundaries.md](./knowledge-boundaries.md) — 4 boundary types, criterios de publicación
- [knowledge-ownership.md](./knowledge-ownership.md) — Transferencia de ownership, 6 roles
- [knowledge-classification.md](./knowledge-classification.md) — PRIVATE/PUBLIC, 6 tipos funcionales
- [knowledge-lifecycle.md](./knowledge-lifecycle.md) — Estado mínimo `validated` para compartir
- [knowledge-provenance.md](./knowledge-provenance.md) — Provenance mínimo PARTIAL para compartir
- [knowledge-confidence-model.md](./knowledge-confidence-model.md) — Confianza mínima MEDIO para compartir
- [knowledge-freshness.md](./knowledge-freshness.md) — Verificación de vigencia antes de consumo
- [knowledge-source-of-truth.md](./knowledge-source-of-truth.md) — Fuente canónica del KO compartido
- [knowledge-architecture-principles.md](./knowledge-architecture-principles.md) — Principio 2 (fuente única), Principio 7 (compartido por diseño)
- [Architecture Baseline v1.0](../../architecture/architecture-baseline-v1.md) — Gobernanza SOLO, INV-04

---

## Tabla epistémica

| Clasificación | Cantidad | Porcentaje |
|---------------|----------|------------|
| [Hecho]       | 10       | 15%        |
| [Hipótesis]   | 0        | 0%         |
| [Decisión]    | 56       | 85%        |
| [Visión]      | 0        | 0%         |
