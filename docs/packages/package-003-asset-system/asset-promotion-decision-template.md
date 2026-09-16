# Template — Asset Promotion Decision

> Registra una decisión explícita; no ejecuta `AUTO_PROMOTE`. Referencias: [promotion process](./asset-promotion-process.md), [governance](./asset-governance.md) y [registry contract](./asset-registry-contract.md).

## Input references — REQUIRED

- Candidate record / `asset_id`: `<reference>`
- Evaluation record: `<reference>`

Tier 1 se referencia; duplicate manual Tier 1 entry: **0**.

## Tier 2 additional — REQUIRED (8/8)

| # | Field name | Completar o referenciar |
|---:|---|---|
| 1 | `estado_lifecycle` | `<VALIDATED / fast-path evidence reference>` |
| 2 | `versión` | `<1.0.0 al promover / NOT_ASSIGNED si no se promueve>` |
| 3 | `Asset_Owner` | `<human identity + acceptance reference>` |
| 4 | `fecha_de_creación` | `<original intake ISO 8601 reference>` |
| 5 | `nivel_de_compartición` | `<sharing_scope>` |
| 6 | `consumption_state` | `<NO_ACTIVE_EXTERNAL_CONSUMERS / ACTIVE_EXTERNAL_CONSUMERS>` |
| 7 | `dimensiones_calificación` | `<evaluation reference con 5/5 results>` |
| 8 | `aprobación_fundador` | `<decision record reference; completar luego de decisión>` |

## Decision record — REQUIRED

- Canonical authority / decisor: `<Fundador>`
- Decision date: `<YYYY-MM-DD>`
- Path: `<STANDARD / FAST_PATH>`
- Effective exposure: `<Level 1 / Level 2 / Level 3>`
- Applicable quality gates verified: `<references>`
- Explicit decision: `<PROMOTED / REJECTED / DEFERRED / REMEDIATION_REQUIRED>`
- Rationale: `<10–280 caracteres>`
- Restrictions: `<value / NONE_KNOWN>`
- Effective version: `<version / NOT_APPLICABLE>`
- Review trigger: `<date/event>`
- Source of truth: `<Tier 1 reference; no re-entry>`
- Owner: `<Tier 2 reference; no re-entry>`

Outcome no es lifecycle state. Sólo `PROMOTED` con record válido permite la transición aprobada; este template no la ejecuta automáticamente.
