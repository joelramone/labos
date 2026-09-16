# Sharing, Consumo y Reutilización de Assets

## Modelo de acceso

[Decisión] `sharing_scope` autoriza acceso; `consumption_state` registra consumo externo efectivo. Un scope autorizado no demuestra uso, valor ni exposición operativa por sí solo.

| sharing_scope | Acceso autorizado | Cambio requerido |
|---|---|---|
| Lab-Private | Solo originating_Lab | Para otro Lab, publicación explícita vía Asset_Sharing_Protocol y aprobación aplicable |
| Lab-Published | Otros Labs pueden descubrir/referenciar en lectura | Declaración del owner + aprobación del Fundador |
| LabOS-Shared | Todos los Labs autorizados del ecosistema | Documentación, mantenibilidad y aprobación |
| Cross-Lab | Labs participantes bajo acuerdo documentado | Gates Nivel 2 + acuerdo + aprobación |
| Public | Fuera de LabOS | Gates Nivel 3 + sensibilidad/licencia + aprobación |

## Lab-local y sharing interno

[Decisión] Un Asset Lab-local conserva `Lab-Private` y `NO_ACTIVE_EXTERNAL_CONSUMERS`. PRIVATE no significa imposible de compartir: significa que otro Lab no puede consumirlo mientras permanezca Lab-Private. El owner puede iniciar publicación interna si provenance, licensing, autorización y gates lo permiten; el scope autorizado cambia a Lab-Published, LabOS-Shared o Cross-Lab antes del consumo externo.

[Decisión] Una clasificación de sensibilidad interna/confidencial tampoco equivale automáticamente a sharing_scope. Un Asset confidencial no supera Lab-Private sin revisión explícita; licensing puede impedir cualquier publicación aunque el owner la solicite.

## Effective consumption

| Situación | sharing_scope | consumption_state | Evidencia de valor |
|---|---|---|---|
| Disponible en LabOS, nadie lo usa | LabOS-Shared | NO_ACTIVE_EXTERNAL_CONSUMERS | No demuestra reutilización |
| Referenciado por un Lab autorizado | LabOS-Shared/Cross-Lab/Public | ACTIVE_EXTERNAL_CONSUMERS | Uso documentado puede aportar evidencia |
| Deja de usarse durante un ciclo completo | Cualquier scope compartido | Puede desregistrarse consumer | Actualizar métricas; no cambia lifecycle automáticamente |

Cada consumer activo registra Lab, fecha de primer consumo y versión referenciada. La baja elimina consumo activo, no historia. [Decisión]

## Reference-based sharing

[Decisión] Consumer referencia `asset_id`, versión y canonical `source_of_truth`. Unmanaged copy no es autoritativa. Si necesita cambiar el Asset, debe elegir según [asset-versioning.md](./asset-versioning.md): nueva versión autorizada, derived Asset, fork o nuevo Asset. Derived/fork recibe nuevo ID y provenance al original.

## Responsabilidades proporcionales

### Asset_Owner

- Mantener canonical source y restrictions.
- Registrar changes, consumers y deprecation.
- Notificar MAJOR con ≥14 días cuando existan consumers.
- Proveer 30 días de gracia y migración para deprecation con consumers.
- Responder defect reports con evaluación/acción documentada, no con SLA enterprise.

### Consumer

- Usar canonical reference y atribuir asset_id/originating_Lab.
- Respetar scope, sensitivity y licensing.
- Registrar versión y compatibilidad contextual.
- Reportar defectos dentro de 7 días desde detección.
- Reaccionar a MAJOR, supersession y deprecation dentro del plan aplicable.
- No crear una segunda source of truth.

## Publication gates

| Acción | Gate mínimo |
|---|---|
| Lab-Private → Lab-Published/LabOS-Shared | Uso standalone documentado; owner; mantenibilidad; sin dependencia privada no autorizada; Founder approval cuando R18 aplica |
| Cross-Lab | Propósito, instrucciones, ejemplo, licencia, sensibilidad, maintainer/cadencia, acuerdo de ownership |
| Public | Nivel 3, licencia explícita, sensibilidad, external/customer risk y aprobación exclusiva del Fundador |

[Decisión] Public no elimina ownership, provenance, restrictions ni Canonical_Authority. Una licencia ausente o incompatible bloquea publicación externa y conserva el estado/scope anterior.

## Defectos y referencias obsoletas

| Evento | Acción |
|---|---|
| Defecto reportado | Registrar fecha, versión, consumer, impacto; owner evalúa patch/risk/deprecation; lifecycle no cambia automáticamente |
| PATCH/MINOR | Notificación informativa opcional según impacto |
| MAJOR | Identificar consumers, notificar ≥14 días y evaluar compatibilidad |
| SUPERSEDED | Referenciar sucesor y migrar antes de gracia |

## Conflictos

[Decisión] Conflicto de ownership/mantenimiento se registra con partes, naturaleza, resolución y fecha dentro de 14 días. En SOLO es un registro ligero; no crea comité ni workflow enterprise.

## Validación scope/consumption

| Control | Resultado |
|---|---|
| sharing_scope confundido con consumption_state | No |
| LabOS-Shared con cero consumers permitido | Sí |
| PRIVATE absolutamente unshareable | No; requiere publicación/autorización previa |
| Consumer crea source paralela | Prohibido |
| Public elimina authority/restrictions | No |
| Scope solo demuestra value | No |
