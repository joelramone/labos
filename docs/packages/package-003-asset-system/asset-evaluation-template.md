# Template — Asset Evaluation

> Evalúa un Candidate sin promoverlo. Referencias: [qualification](./asset-qualification-framework.md), [quality gates](./asset-quality-gates.md), [risk](./asset-risk-model.md) y [value](./asset-value-model.md).

## References — REQUIRED

- `asset_id`: `<reference>`
- Candidate record: `<relative reference>`
- Evaluation date: `<YYYY-MM-DD>`
- Evaluator: `<human identity>`

Tier 1 se consume por referencia; no reingresarlo.

## Five qualification dimensions — REQUIRED (5/5)

| # | Dimensión | Resultado | Evidencia / referencia | Gap o remediation |
|---:|---|---|---|---|
| 1 | Evidencia de reutilización | `<SATISFECHA / NO_SATISFECHA>` | `<reference>` | `<acción / NONE>` |
| 2 | Calidad mínima documentable | `<SATISFECHA / NO_SATISFECHA>` | `<reference>` | `<acción / NONE>` |
| 3 | Provenance trazable | `<SATISFECHA / NO_SATISFECHA>` | `<reference>` | `<acción / NONE>` |
| 4 | Ownership asignado | `<SATISFECHA / NO_SATISFECHA>` | `<reference>` | `<acción / NONE>` |
| 5 | Source of truth identificado | `<SATISFECHA / NO_SATISFECHA>` | `<reference>` | `<acción / NONE>` |

## Reuse — REQUIRED

- Classification: `<PROJECTED_REUSE / DEMONSTRATED_REUSE / NONE>`
- Target Lab/domain and concrete scenario: `<value>`
- Demonstrated use reference: `<reference / NOT_APPLICABLE>`
- If PROJECTED_REUSE, 90-day review trigger: `<YYYY-MM-DD or trigger rule>`

## Quality, risk and restrictions — REQUIRED

- Base exposure: `<Level 1 / Level 2 / Level 3>`
- Quality gate result: `<PASS / FAIL / EVIDENCE_REQUIRED>`
- Risk level: `<LOW / MEDIUM / HIGH / CRITICAL>`
- Risk override: `<BASE / ELEVATED + rationale>`
- Licensing/restrictions: `<value / NONE_KNOWN>`
- Sensitivity: `<value>`
- Ownership acceptance reference: `<reference>`
- Source-of-truth verification: `<PASS / FAIL + reference>`
- Value status: `<DEMOSTRADO / PROYECTADO / INDETERMINADO + evidence>`

No usar score agregado.

## Result — REQUIRED

- Remediation: `<actions / NONE>`
- Contradictory or missing evidence: `<references / NONE>`
- Recommendation: `<READY_FOR_REVIEW / NEEDS_REMEDIATION / NOT_AN_ASSET / EVIDENCE_REQUIRED>`
- Next review trigger: `<date/event>`

La recommendation no cambia lifecycle ni constituye promotion.
