# Ownership y Autoridad de Assets

## Roles conceptuales

| Rol | Responsabilidad | Autoridad | Restricción |
|---|---|---|---|
| creator | Produce el artefacto original | Autoría del contenido producido | No adquiere ownership automáticamente |
| originating_Lab | Aporta contexto y boundary de origen | Fuente inicial de Canonical_Authority | Es un Lab, no una persona |
| Asset_Owner | Mantiene el Asset y decide su gestión cotidiana | Mantenimiento, versiones y evaluación | Debe ser humano |
| maintainer | Ejecuta cambios autorizados | Edición técnica bajo instrucciones | Puede ser AI bajo supervisión humana |
| reviewer | Evalúa evidencia y gates | Recomienda resultado; identifica gaps | Puede ser AI bajo supervisión; no decide promoción final |
| Canonical_Authority | Decide promoción, deprecación y scope crítico | Autoridad final de governance | Debe ser humano |
| consumer | Usa el Asset por referencia | Uso compatible y feedback | No adquiere ownership ni autoridad |

[Decisión] Creator, Asset_Owner, maintainer, reviewer, Canonical_Authority y consumer son funciones distintas. `originating_Lab` es el contexto organizacional de origen. AI no se convierte en owner, creator legal ni Canonical_Authority por generar o modificar contenido.

## Mapping SOLO

[Hecho] Una sola persona —el Fundador— opera LabOS. [Decisión] Puede ocupar simultáneamente creator, Asset_Owner, maintainer, reviewer, Canonical_Authority y consumer, pero cada rol se registra conceptualmente por separado. La concentración operativa no fusiona responsabilidades.

## Matriz de decisiones

| Acción | Responsable | Aprobación final |
|---|---|---|
| Crear Candidate | creator / Asset_Owner | Asset_Owner |
| Mantener contenido | maintainer | Asset_Owner |
| Evaluar gates | reviewer | Asset_Owner; Fundador donde la transición lo exige |
| Promover a CANONICAL | — | Canonical_Authority humana / Fundador |
| Cambiar sharing_scope | Asset_Owner propone | Fundador |
| Deprecar o archivar | Asset_Owner propone | Fundador |
| Consumir | consumer | Según scope autorizado |

## Transferencia

Una transferencia registra `asset_id`, owner saliente, owner entrante humano, fecha ISO 8601 y aceptación explícita de responsabilidad. El historial se preserva. [Decisión]

## Sharing y boundaries de Lab

[Decisión] Compartir no transfiere ownership. La Canonical_Authority del originating_Lab se conserva incluso en Cross-Lab o Public. Co-governance requiere ADR. Package 001A conserva autoridad sobre integración y boundaries del Lab; Package 003 no modifica contratos ni identidad del Lab.

## Validación

| Control | Resultado |
|---|---|
| Roles conceptuales | 7/7 |
| Owner/Authority humanos | PASS |
| AI como owner/authority | PROHIBIDO |
| Roles SOLO fusionados conceptualmente | NO |
| Sharing transfiere autoridad | NO |
