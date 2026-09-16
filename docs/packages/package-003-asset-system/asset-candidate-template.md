# Template — Asset Candidate Intake

> Objetivo: registrar un Candidate de bajo riesgo en 3–5 minutos. Completar exactamente los ocho campos requeridos. Ver [registry contract](./asset-registry-contract.md) y [boundaries](./asset-definition-and-boundaries.md).

## Referencia de registro

- `asset_id`: `SYSTEM_ASSIGNED` — no completar manualmente.

## Tier 1 — REQUIRED (8/8)

| # | Field name | Propósito breve | Valor esperado | Completar |
|---:|---|---|---|---|
| 1 | `nombre` | Identificar el Candidate | Texto único en el Lab, ≤80 caracteres | `<nombre>` |
| 2 | `tipo` | Clasificar por ADR-0002 | Documento / Template / Dataset / Herramienta / Componente / Framework / Playbook | `<tipo>` |
| 3 | `descripción` | Explicar qué es | 1–3 oraciones, ≤500 caracteres | `<descripción>` |
| 4 | `hipótesis_de_uso` | Nombrar usuario y contexto | `<usuario objetivo> necesita <uso> en <contexto>` | `<hipótesis>` |
| 5 | `content_state` | Registrar madurez del contenido | `borrador` / `validado` / `productizado` | `<estado>` |
| 6 | `originating_Lab` | Identificar origen | Lab ID válido | `<LABOS-LAB-ID>` |
| 7 | `source_of_truth` | Apuntar a una única fuente | Path o URL verificable | `<referencia>` |
| 8 | `provenance` | Preservar origen de evidencia | KO, research_id o fuente externa verificable | `<referencia>` |

## Future metadata

- Señal inicial de reutilización: `<OPTIONAL>`
- Esfuerzo estimado: `<OPTIONAL>`
- Evaluation record: `<NOT_YET_REQUIRED>`
- Tier 2 metadata: `<NOT_YET_REQUIRED>`

## Intake check

- [ ] Ocho campos Tier 1 completos.
- [ ] Tipo canónico válido; límites de nombre/descripción cumplidos.
- [ ] Tier 2 required en intake: **0**.
- [ ] Tiempo objetivo: 3–5 minutos para caso low-risk.

Output: `CANDIDATE`. Esto no inicia review ni autoriza promotion.
