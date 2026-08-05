# Change Log — Package 003 Requirements

## Metadata

| Campo | Valor |
|-------|-------|
| **Documento** | Requirements Change Log |
| **Package** | 003 — Asset System |
| **Versión original** | v1.0 (baseline sin correcciones) |
| **Versión v1.1** | Correcciones C1–C8 aplicadas por reviewer independiente |
| **Versión v1.2** | Correcciones C9–C12 aplicadas por Principal Architect (esta revisión) |
| **Fecha v1.2** | 2025-07-31 |

---

## Correcciones v1.1 (Pre-existentes)

Las siguientes correcciones ya fueron aplicadas a la versión v1.1 del requirements.md antes de esta revisión. Se documentan aquí para trazabilidad completa.

---

### C1 — Contradicción resuelta: referencia a estado productizado en R14.1

| Campo | Valor |
|-------|-------|
| **Change ID** | C1 |
| **Original Req ID** | R14.1 |
| **Tipo** | CLARIFIED |
| **Issue original** | R14.1 referenciaba "estado productizado del ciclo borrador→validado→productizado de Package 000" como condición de elegibilidad para product_attachment. Esto contradecía el governance lifecycle de Package 003, donde el estado equivalente es CANONICAL. Los dos modelos de estado son dimensiones separadas. |
| **Resultado** | R14.1 ahora requiere explícitamente "Asset en estado CANONICAL (lifecycle state de Package 003)" como condición de elegibilidad. Nota aclaratoria añadida sobre la separación entre content_state de Package 000 y governance lifecycle de Package 003. |
| **Impacto arquitectónico** | Elimina contradicción entre Package 000 (content_state) y Package 003 (governance lifecycle). |
| **Tipo de bloqueo** | Bloqueante (corregido) |

---

### C2 — Gap resuelto: first-time assets sin historial de reutilización en R4.1

| Campo | Valor |
|-------|-------|
| **Change ID** | C2 |
| **Original Req ID** | R4.1 |
| **Tipo** | CLARIFIED |
| **Issue original** | La dimensión "evidencia de reutilización" en R4.1 solo aceptaba uso demostrado fuera del contexto de origen. Esto impedía que cualquier primer activo de un Lab pudiera alcanzar CANONICAL sin historial previo, creando un bloqueo circular. |
| **Resultado** | R4.1(a) ahora acepta dos formas: Forma A (DEMONSTRATED) — al menos 1 uso documentado fuera del contexto de origen; Forma B (DESIGNED-FOR-REUSE) — declaración escrita con ≥1 Lab o dominio destino específico y ≥1 escenario de uso concreto, con review trigger automático a los 90 días. |
| **Impacto arquitectónico** | Permite la primera promoción a CANONICAL con hipótesis fundada en lugar de historial. |
| **Tipo de bloqueo** | Bloqueante (corregido) |

---

### C3 — Inconsistencia resuelta: trigger de deprecación no diferenciado por sharing_scope en R11.4

| Campo | Valor |
|-------|-------|
| **Change ID** | C3 |
| **Original Req ID** | R11.4 |
| **Tipo** | CLARIFIED |
| **Issue original** | R11.4 usaba ausencia de reutilización cross-Lab como trigger de deprecación para todos los Assets, incluyendo Assets Lab-Private que por definición no tienen cross-Lab reuse. Esto causaba que Assets Lab-Private quedaran permanentemente marcados para deprecación. |
| **Resultado** | R11.4 diferencia: para Assets LabOS-Shared/Cross-Lab/Public el trigger es ausencia de reutilización por Labs distintos; para Assets Lab-Private el trigger es ausencia de uso documentado dentro del originating_Lab. |
| **Impacto arquitectónico** | Coherencia entre sharing_scope y criterios de deprecación. |
| **Tipo de bloqueo** | Bloqueante (corregido) |

---

### C4 — Ambigüedad resuelta: "compartibles por defecto" sin nivel explícito en R2.2

| Campo | Valor |
|-------|-------|
| **Change ID** | C4 |
| **Original Req ID** | R2.2 |
| **Tipo** | CLARIFIED |
| **Issue original** | R2.2 decía "compartibles por defecto" sin especificar a qué nivel de sharing_scope correspondía ese default. La lista de niveles de R9.1 define 5 valores posibles. |
| **Resultado** | R2.2 ahora mapea explícitamente "compartibles por defecto" al nivel LabOS-Shared per R9.1. La nota de corrección [CORRECCIÓN 4] fue añadida al criterio. |
| **Impacto arquitectónico** | Alineación con R9.1 y ADR-0002. |
| **Tipo de bloqueo** | No bloqueante |


---

### C5 — Incompleto resuelto: metadata de registro sin diferenciación de fases en R16.1-2

| Campo | Valor |
|-------|-------|
| **Change ID** | C5 |
| **Original Req ID** | R16.1, R16.2 |
| **Tipo** | SPLIT |
| **Issue original** | La metadata del registro mezclaba todos los campos en una sola lista, sin distinguir qué se requiere al registrar un CANDIDATE (intake) y qué se requiere al promover a CANONICAL. Esto creaba una barrera de entrada excesiva para el registro inicial. |
| **Resultado** | R16.1 define metadata de intake (8 campos: los necesarios para registrar un CANDIDATE). R16.2 define metadata adicional obligatoria para promoción a CANONICAL (8 campos adicionales). La separación permite un registro inicial en 3–5 min y una promoción completa sin sorpresas. |
| **Impacto arquitectónico** | Reduce overhead de intake sin sacrificar completitud al promover. |
| **Tipo de bloqueo** | Bloqueante para usabilidad (corregido) |

---

### C6 — Ambigüedad resuelta: sharing_scope y product_attachment como estados en R3.1

| Campo | Valor |
|-------|-------|
| **Change ID** | C6 |
| **Original Req ID** | R3.1 |
| **Tipo** | CLARIFIED |
| **Issue original** | El documento original no era explícito sobre si sharing_scope y product_attachment eran estados del ciclo de vida o atributos ortogonales. Esto generaba riesgo de tratar "compartido" como un estado lifecyle en lugar de un atributo. |
| **Resultado** | R3.1 ahora incluye nota explícita: sharing_scope y product_attachment son atributos ortogonales al lifecycle state. Un Asset puede ser CANONICAL y Lab-Private simultáneamente. También fueron añadidos al Glosario como entradas separadas. |
| **Impacto arquitectónico** | Previene estados compuestos no definidos. Alinea con arquitectura de dimensiones ortogonales. |
| **Tipo de bloqueo** | No bloqueante |

---

### C7 — Gap resuelto: KO en estado disputed no manejado en R20

| Campo | Valor |
|-------|-------|
| **Change ID** | C7 |
| **Original Req ID** | R20.7 (criterio nuevo) |
| **Tipo** | ADDED |
| **Issue original** | R20 cubría superseded, deprecated, MAJOR y MINOR pero omitía el estado `disputed` del KO fuente. Un KO disputed indica información cuya validez está en duda — esto debería generar una señal al Asset derivado. |
| **Resultado** | R20.7 añade: cuando un KO fuente cambia a estado `disputed`, se agrega un review flag informativo al Asset con motivo "KO fuente en estado disputed", sin invalidar el lifecycle state ni marcar review_required. El Asset_Owner decide si actuar. |
| **Impacto arquitectónico** | Completa la cobertura de propagación de cambios KO → Asset. |
| **Tipo de bloqueo** | No bloqueante |

---

### C8 — Gap resuelto: distinción nueva versión / derivado / fork en R8.7

| Campo | Valor |
|-------|-------|
| **Change ID** | C8 |
| **Original Req ID** | R8.7 (criterio nuevo) |
| **Tipo** | ADDED |
| **Issue original** | R8 definía versionado semántico y el caso de Asset superseded, pero no distinguía explícitamente entre (a) nueva versión del mismo Asset, (b) Asset derivado para un contexto específico, y (c) fork para desarrollo independiente. Sin esta distinción, los tres casos podían confundirse. |
| **Resultado** | R8.7 define los tres casos con criterios distintos: nueva versión (mismo asset_id, versión incrementada), Asset derivado (nuevo asset_id, provenance que referencia original), fork (nuevo asset_id, desarrollo nuevo e independiente). El Asset original permanece inmutable en los tres casos. |
| **Impacto arquitectónico** | Clarifica el modelo de evolución de Assets y protege la inmutabilidad del original. |
| **Tipo de bloqueo** | No bloqueante |

---

## Correcciones v1.2 (Esta revisión — Principal Architect)

---

### C9 — Clarificación: review_required como flag ortogonal al lifecycle state

| Campo | Valor |
|-------|-------|
| **Change ID** | C9 |
| **Original Req ID** | R3.1, R4.6, R20 |
| **Tipo** | CLARIFIED |
| **Issue original** | El término `review_required` aparece en R4.6 y R20 como estado de revisión del Asset. Sin embargo, no aparece en los 7 estados del ciclo de vida definidos en R3.1. Esto crea ambigüedad: ¿es un octavo estado o un atributo? Si se trata como estado, hay transiciones no definidas. |
| **Resultado** | Se agrega `review_required` al Glosario del documento como flag/atributo ortogonal al lifecycle state. La nota en R3.1 se extiende para incluirlo en la lista de atributos ortogonales (junto con sharing_scope y product_attachment). R4.6 y R20 mantienen su redacción pero ahora son coherentes con la definición del glosario. |
| **Impacto arquitectónico** | Mantiene el modelo de 7 estados del ciclo de vida sin añadir un octavo estado no definido. Preserva los atributos como dimensión ortogonal. |
| **Tipo de bloqueo** | Bloqueante para coherencia interna |

---

### C10 — Clarificación: Fundador puede ocupar rol de maintainer en contexto SOLO

| Campo | Valor |
|-------|-------|
| **Change ID** | C10 |
| **Original Req ID** | R6.7 |
| **Tipo** | CLARIFIED |
| **Issue original** | R6.7 declara que el Fundador en contexto SOLO puede ocupar los roles de creator, Asset_Owner, reviewer y Canonical_Authority. El rol de maintainer (ejecutor de actualizaciones) no está mencionado, dejando un gap ya que en contexto SOLO el Fundador es también el único mantenedor. |
| **Resultado** | R6.7 actualizado para incluir maintainer en la lista de roles que el Fundador puede ocupar simultáneamente en contexto SOLO. |
| **Impacto arquitectónico** | Ninguno. Cierra el gap sin cambiar el modelo de roles. |
| **Tipo de bloqueo** | Bloqueante para coherencia interna |

---

### C11 — Clarificación: path Research → Asset sin KO formalizado en R7.1/R7.6

| Campo | Valor |
|-------|-------|
| **Change ID** | C11 |
| **Original Req ID** | R7.1, R7.6 |
| **Tipo** | CLARIFIED |
| **Issue original** | R7.1 requiere "al menos un knowledge_id válido" como campo obligatorio de provenance. R7.6 permite sustituirlo con URL o referencia bibliográfica para fuentes externas sin KO. Sin embargo, el canonical-domain-map.md muestra que Research puede producir Assets directamente (sin pasar por Package 002). Este path directo no está cubierto: no hay KO externo ni knowledge_id disponible, sino investigación propia no formalizada como Knowledge Object. |
| **Resultado** | R7.6 se extiende para incluir un tercer caso de sustitución: cuando el Asset se origina en investigación propia no formalizada como Knowledge Object en Package 002, se acepta el research_id (identificador de la investigación de Package 001) como referencia de provenance en lugar del knowledge_id, documentando el motivo de la ausencia de KO. |
| **Impacto arquitectónico** | Alinea R7 con el diagrama del canonical-domain-map.md (Research → Asset directo). No contradice el handoff de Package 002 (que sigue siendo el camino preferido cuando aplica). |
| **Tipo de bloqueo** | Bloqueante para coherencia interna |

---

### C12 — Clarificación: Canonical Authority después de cross-Lab promotion

| Campo | Valor |
|-------|-------|
| **Change ID** | C12 |
| **Original Req ID** | R6 (nuevo criterio R6.9) |
| **Tipo** | ADDED |
| **Issue original** | El documento no define explícitamente quién tiene Canonical_Authority sobre un Asset después de que su sharing_scope cambia a Cross-Lab o Public. En contexto SOLO la respuesta es siempre el Fundador, pero no quedaba explícito para preparar el escalamiento futuro. |
| **Resultado** | Se añade R6.9: la Canonical_Authority del originating_Lab retiene autoridad canónica sobre el Asset después de cualquier cambio de sharing_scope, incluyendo Cross-Lab y Public. Un cambio de Canonical_Authority hacia co-governance o autoridad compartida requiere un ADR formal que establezca el nuevo modelo de gobernanza. |
| **Impacto arquitectónico** | Clarifica el modelo de gobernanza sin cambiar el modelo actual. Prepara el escalamiento futuro de forma ordenada bajo el architecture-change-control. |
| **Tipo de bloqueo** | Bloqueante para coherencia interna |

---

## Resumen de Cambios

| Versión | Cambios | Bloqueantes resueltos | No bloqueantes |
|---------|---------|----------------------|----------------|
| v1.1 | C1–C8 | C1, C2, C3, C5 | C4, C6, C7, C8 |
| v1.2 | C9–C12 | C9, C10, C11, C12 | — |
| **Total** | **12** | **8** | **4** |

### Recuento por tipo de cambio

| Tipo | Cantidad |
|------|----------|
| CLARIFIED | 8 (C1, C3, C4, C6, C9, C10, C11, C12) |
| ADDED | 2 (C7, C8) |
| SPLIT | 1 (C5) |
| MERGED | 0 |
| REMOVED | 0 |
| SIMPLIFIED | 1 (C2) |

