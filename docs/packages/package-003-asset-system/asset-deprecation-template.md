# Template — Asset Deprecation and Archive

> Registra `CANONICAL → DEPRECATED → ARCHIVED` sin borrar historia. Ver [deprecation model](./asset-deprecation-and-archive.md) y [versioning](./asset-versioning.md).

## Deprecation proposal — REQUIRED

- Asset ID: `<asset_id>`
- Canonical record/version: `<reference>`
- Reason / qualifying condition: `<value + evidence>`
- Owner: `<human identity/reference>`
- Proposed deprecation date: `<YYYY-MM-DD>`
- Restrictions that remain active: `<value / NONE_KNOWN>`
- Replacement/successor: `<reference / NONE>`

## Dependency analysis — REQUIRED

- Active consumers: `<list with contact/version / NONE>`
- Product dependencies / `product_attachments`: `<references / NONE>`
- Migration required: `<YES / NO + rationale>`
- Migration plan: `<action, responsible, target date / NOT_APPLICABLE>`
- Communication requirement: `<recipients, channel, date>`
- Consumer confirmations: `<references / PENDING / NOT_APPLICABLE>`
- Product impact / exit action: `<reference / NOT_APPLICABLE>`
- Risk level and exception review: `<LOW / MEDIUM / HIGH / CRITICAL + reference>`

## Explicit decisions — REQUIRED

- Deprecation authority: `<Fundador>`
- Deprecation decision/date: `<APPROVED / REJECTED / DEFERRED> — <YYYY-MM-DD>`
- Archive criteria: `<30-day minimum + consumers/migrations/dependencies resolved>`
- Proposed archive date: `<YYYY-MM-DD / NOT_YET_REQUIRED>`
- Archive decision/date: `<APPROVED / BLOCKED / NOT_YET_REQUIRED>`
- Historical retention: `<asset_id, versions, provenance, decisions and source preserved reference>`
- Reactivation condition: `<new CANDIDATE with new asset_id and provenance to archived record>`
- Next review trigger: `<pending consumer, 180 days, risk event or date>`

Archive inmediato está prohibido cuando existen dependencies no tratadas. Una emergencia de riesgo puede restringir uso de inmediato, pero no elimina el análisis, la autoridad ni el historial.
