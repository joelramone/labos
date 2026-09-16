# Template — Asset Review

> Para reviews scheduled, event-triggered, defect, reuse, value, risk, source-of-truth o Product dependency. No reemplaza ni repite la promotion decision. Ver [metrics](./asset-metrics.md) y [lifecycle](./asset-lifecycle.md).

## Review identity — REQUIRED

- `asset_id`: `<reference>`
- Current canonical record/version: `<reference>`
- Review type: `<SCHEDULED / EVENT_TRIGGERED / DEFECT / REUSE / VALUE / RISK / SOURCE_OF_TRUTH / PRODUCT_DEPENDENCY>`
- Reason / trigger: `<value>`
- Review date: `<YYYY-MM-DD>`
- Reviewer: `<human identity>`
- Asset_Owner: `<reference>`

## Evidence and current status — REQUIRED

- Current lifecycle status: `<reference>`
- Evidence reviewed: `<references>`
- Seven-metric cycle record: `<asset-metrics.md-compatible reference>`
- Value classification: `<DEMOSTRADO / PROYECTADO / INDETERMINADO + evidence>`
- Reuse status and consumers: `<reference>`
- Risk/restrictions status: `<value>`
- Source-of-truth status: `<AVAILABLE / REMEDIATION_REQUIRED + reference>`
- KO/upstream change: `<NONE / MINOR / MAJOR / SUPERSEDED / DEPRECATED / DISPUTED>`
- Product dependency impact: `<reference / NOT_APPLICABLE>`

## Review result — REQUIRED

- Changes observed: `<value / NONE>`
- Defects/conflicts: `<value / NONE>`
- Remediation: `<actions, owner, due date / NONE>`
- Owner decision: `<MAINTAIN / UPDATE / RESTRICT / PROPOSE_DEPRECATION / ESCALATE>`
- Next review trigger/date: `<value>`
- `review_required`: `<CLEAR / REMAINS_ACTIVE + rationale>`

Forma B / PROJECTED_REUSE requiere review a 90 días. Este record no repite Founder promotion approval y no cambia lifecycle sin autorización separada.
