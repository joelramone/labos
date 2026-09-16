# Deprecación y Archivo de Assets

## Regla de retiro

[Decisión] El retiro controlado sigue exclusivamente `CANONICAL → DEPRECATED → ARCHIVED`. Deprecation comunica que el Asset dejará de ser la referencia activa; archive conserva el registro histórico. Ninguno elimina evidencia ni crea regresiones de lifecycle.

## Evaluación previa a deprecation

Antes de decidir `CANONICAL → DEPRECATED`, Canonical_Authority debe registrar:

| Control | Evidencia mínima |
|---|---|
| Consumers activos | Identidad, versión consumida y contacto responsable |
| Product attachments | Dependencia y criticidad declaradas, sin crear ni gobernar Products |
| Alternativa o sucesor | Referencia canónica, o justificación de ausencia |
| Migración | Acción, responsable y fecha objetivo por consumer/dependencia |
| Risk | Impacto financiero, licensing, security, privacy, operational, customer, Product y publicación |
| Restrictions | Sensitivity, licencia y límites que continúan vigentes |

[Decisión] La presencia de consumers o Product attachments no impide deprecation, pero impide un archive silencioso. Riesgo HIGH/CRITICAL eleva review y puede extender la ventana de migración.

## Autoridad y transición

| Acción | Autoridad | Condición |
|---|---|---|
| Proponer deprecation | Owner, maintainer o consumer | Motivo y evidencia |
| Decidir deprecation | Fundador como Canonical_Authority | Evaluación previa completa y decisión explícita |
| Notificar | Owner/maintainer | Consumers y dependencias conocidas |
| Confirmar migración | Consumer responsable | Referencia nueva, remoción o aceptación de impacto |
| Decidir archive | Fundador | ≥30 días en DEPRECATED y condición de salida satisfecha |

AI puede detectar señales, preparar impacto o sugerir acciones; no decide deprecation, archive ni reactivation. [Decisión]

## Comportamiento de DEPRECATED

- El canonical source permanece accesible y claramente marcado.
- No se recomiendan nuevos consumers salvo excepción explícita y temporal.
- Los consumers activos reciben sucesor/alternativa, plan de migración o aceptación de riesgo.
- Defectos y restricciones siguen registrándose.
- Si supera 180 días sin resolución, se dispara revisión; no se archiva automáticamente.
- `sharing_scope` y `consumption_state` continúan siendo dimensiones separadas del estado.

## Gate de ARCHIVED

Se permite `DEPRECATED → ARCHIVED` sólo cuando:

1. transcurrieron al menos 30 días;
2. no existen consumers activos, o todos confirmaron migration/removal/aceptación explícita del impacto;
3. Product attachments conocidos tienen exit action registrada;
4. owner, successor/alternative y restricciones quedan preservados;
5. history, provenance, decisiones y prior versions son consultables.

Fallar cualquier condición preserva `DEPRECATED`, registra el gap y programa review. No existe auto-archive. [Decisión]

## Historia y source of truth

[Decisión] Archive preserva el `asset_id`, canonical source histórico, provenance, approval/deprecation records, versiones y relaciones de supersession. Las copias no gestionadas no se vuelven autoridad. Un successor usa su propio source of truth y mantiene referencias bidireccionales.

## Reactivación

ARCHIVED y REJECTED son terminales. Nueva demanda, evidencia o corrección crea un nuevo `CANDIDATE` con nuevo `asset_id` y provenance hacia el registro original; debe atravesar qualification y promotion. No se restaura silenciosamente el estado anterior. [Decisión]

## Escenarios de control

| Caso | Acción permitida | Acción prohibida | Trigger |
|---|---|---|---|
| DEPRECATED con consumer activo | Migrar, reemplazar o aceptar impacto explícito | Archive silencioso | Consumer activo |
| Product attachment futuro | Registrar exit action y compatibilidad | Definir Product lifecycle | Cambio/deprecation |
| Defecto posterior a canonicalización | Evaluar risk, corregir versión o deprecar | Borrar versión defectuosa | Defect report |
| Lab originador archivado | Transferir ownership/maintenance preservando autoridad | Perder canonical source | Lab boundary change |
| Demanda luego de archive | Crear nuevo Candidate referenciado | ARCHIVED → CANONICAL | Evidencia nueva |

## Validación

| Control | Resultado |
|---|---|
| Lifecycle states agregados | 0 |
| Consumers evaluados antes de retiro | Sí |
| Product impact evaluado | Sí, sólo dependency boundary |
| Minimum deprecation window | 30 días |
| Unresolved long-tail review | 180 días |
| Historia/provenance/versiones preservadas | Sí |
| Reactivación directa | Prohibida |
| Automatic deprecation/archive | Prohibidos |
