# Proceso de Promoción de Asset

## Regla central

[Decisión] Asset_Candidate ≠ Asset_Canónico. Promotion requiere evaluación completa y decisión explícita del Fundador; no existe `AUTO_PROMOTE`.

```text
Candidate intake → qualification → applicable gates/risk → explicit decision
                                                        ↓
                                                Canonical Asset
```

## Preconditions

Antes de decidir:

1. Tier 1: exactamente 8 campos presentes.
2. Qualification: cinco dimensiones SATISFECHAS.
3. Tier 2: exactamente 8 campos adicionales completos o correctamente referenciados, sin reingreso manual de Tier 1.
4. Provenance verificable y un source_of_truth.
5. Asset_Owner humano asignado.
6. Base exposure y risk override evaluados.
7. Applicable quality gate satisfecho.
8. Approval record válido del Fundador.

## Standard path

| Paso | Input | Output |
|---|---|---|
| Intake | Artifact + Tier 1 | CANDIDATE |
| Qualification | Cinco dimensiones | READY_FOR_REVIEW o remediation/rejection recommendation |
| Review | CANDIDATE qualified | UNDER_REVIEW |
| Validation | Base + exposure/risk gates | VALIDATED o permanece UNDER_REVIEW |
| Decision | Tier 2 + approval record | CANONICAL 1.0.0 o permanece VALIDATED |

## Fast Path

[Decisión] Para Nivel 1 efectivo sin override incompatible, una única aprobación del Fundador puede cubrir CANDIDATE → VALIDATED → CANONICAL. Debe registrar cinco dimensiones, risk evaluation, Tier 1, Tier 2 y justificación. Reduce ceremony; no elimina evidencia ni authority.

## Decision outcomes

| Outcome | Significado | Lifecycle effect |
|---|---|---|
| PROMOTED | Gates y approval válidos | VALIDATED → CANONICAL; versión 1.0.0 |
| REMEDIATION_REQUIRED | Gap subsanable | Permanece en estado actual; registra gaps |
| REJECTED | Irremediable por decisión humana | Solo CANDIDATE/UNDER_REVIEW → REJECTED según lifecycle |
| DEFERRED | No se decide promover | Permanece VALIDATED con razón/fecha o trigger |

[Decisión] Outcomes son resultados de decisión, no nuevos lifecycle states.

## AI assistance

AI puede evaluar, sugerir, detectar gaps y preparar evidencia. No puede firmar approval, ser Asset_Owner/Canonical_Authority ni ejecutar transición final. [Decisión]

## Failure behavior

Gate o approval inválido rechaza la transición, nombra criterios fallidos y conserva estado/metadata. Remediation reabre evaluación; no reinicia ni borra historia. [Decisión]

## Scenario walkthroughs

| Caso | Resultado |
|---|---|
| Lab-Private projected reuse, LOW risk | Fast Path posible con Forma B + trigger 90 días + aprobación |
| LabOS-Shared, cero consumers | Nivel 1 posible; scope no prueba uso; Fast Path condicionado a gates |
| AI recomienda PROMOTED | Recomendación sin efecto hasta decisión del Fundador |
| Tier 2 incompleto | REMEDIATION_REQUIRED; sin transición |

## Validación

| Control | Resultado |
|---|---|
| Tier 1 | 8 |
| Tier 2 additional | 8 |
| Cinco dimensiones Fast Path | 5/5 |
| Founder approval | Obligatoria |
| Failure preserves state | Sí |
| Outcomes usados como lifecycle states | 0 |
| Automatic promotion | Prohibida |
