# Governance y Aprobaciones del Asset System

## Governance SOLO

[Hecho] El Fundador es el único operador actual. [Decisión] Puede ocupar múltiples roles, pero creator, Asset_Owner, maintainer, reviewer y Canonical_Authority permanecen conceptualmente separados. AI puede asistir en evidencia, gaps y drafts; nunca ejerce ownership ni autoridad canónica final.

## Cuatro triggers críticos de aprobación

| # | Acción | Autoridad final |
|---:|---|---|
| 1 | VALIDATED → CANONICAL | Fundador |
| 2 | Lab-Private → LabOS-Shared o superior | Fundador |
| 3 | Publicación Public | Fundador |
| 4 | Deprecación con ≥1 consumer activo | Fundador |

Una aprobación válida contiene decisor `Fundador`, fecha ISO 8601, asset_id y justificación de 10–280 caracteres. Puede registrarse en commit, Asset Record o template. Campo ausente/fuera de rango invalida el acto y bloquea la acción sin cambiar el estado. [Decisión]

## Matriz de autoridad

| Acción | Iniciador | Evaluador | Decisor final |
|---|---|---|---|
| Candidate creation | creator/Asset_Owner | Validación de Tier 1 | Asset_Owner humano |
| Qualification | Asset_Owner | reviewer humano o AI supervisada | Asset_Owner; Fundador inicia transición crítica |
| Promotion | Asset_Owner/reviewer recomienda | Gates y risk | Fundador/Canonical_Authority |
| Sharing | Asset_Owner solicita | Licensing/sensitivity/gates | Fundador cuando R18 aplica |
| Ownership transfer | Owner saliente | Verificación de aceptación | Owner entrante humano; cambio de Canonical_Authority requiere ADR |
| Sensitivity change | Asset_Owner | reviewer | Fundador si amplía exposición crítica |
| product_attachment futuro | Asset_Owner solicita | Eligibility/impact | Fundador; Package 004 debe existir para Product real |
| Deprecation | Asset_Owner propone | Consumers/attachments/risk | Fundador cuando hay consumers; Canonical_Authority siempre registrada |
| Archive | Asset_Owner verifica | Migración/tiempo | Fundador |
| Reactivation | Asset_Owner propone nuevo record | Qualification completa | Fundador por proceso normal; original no cambia |

## Promotion governance

[Decisión] Sistemas y AI pueden verificar, sugerir, detectar gaps y preparar evidencia. Solo una decisión explícita humana produce CANONICAL. No existe `AUTO_PROMOTE`.

## Change control

- PATCH: redacción/link sin cambio semántico.
- MINOR: extensión compatible con aprobación al cierre cuando corresponda.
- MAJOR: cambio de taxonomy, gates, roles o invariantes; requiere ADR, impacto, migración y aprobación explícita.

## Approval scenarios

| Caso | Resultado |
|---|---|
| AI recomienda promoción, sin registro del Fundador | Bloqueado; permanece en estado actual |
| Justificación de 5 caracteres | Aprobación inválida; indicar campo fuera de rango |
| Lab-Private solicitado como Public | Licensing/sensitivity/Nivel 3 + aprobación Founder |
| Cambio de Canonical_Authority Cross-Lab | ADR requerido |

## Validación

| Control | Resultado |
|---|---|
| Critical approval triggers | 4/4 |
| Invalid approval changes state | No |
| AI Canonical_Authority | Prohibido |
| Automatic promotion | Prohibida |
| ADR escalation | Preservada |
