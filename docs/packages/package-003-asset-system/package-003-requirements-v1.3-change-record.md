# Package 003 — Requirements v1.3 Change Record

## Metadata

| Campo | Valor |
|---|---|
| Change set | `PKG003-REQ-V1.3` |
| Previous version | v1.2 — `APPROVED` 2026-08-05 |
| Resulting version | v1.3 — `APPROVED` 2026-08-12 |
| Date | 2026-08-12 |
| Architecture baseline | `LABOS-ARCH-BASELINE-001` v1.0 |
| Tasks | `NOT_AUTHORIZED` |
| Implementation | `NOT_AUTHORIZED` |

[Hecho] Requirements v1.2 was formally approved. This record does not revoke or conceal that approval; it documents a subsequent normative reconciliation required by the Design review.

## Changes

| ID | Previous criterion | New criterion | Reason | Source conflict | Architecture authority | Design impact |
|---|---|---|---|---|---|---|
| C1 | R16.1 allowed `nombre` up to 120 characters while R1.2 required 80 | R16.1 requires maximum 80 characters | Restore one canonical limit | R1.2 vs R16.1 | Package 000 `007-company-model.md`; ADR-0001 | Remove provisional conflict language; use 80 everywhere |
| C2 | R16.6 mapped Package 000 `Estado` to `estado_lifecycle`; R16.1 omitted `content_state` | Tier 1 includes `content_state`; Tier 2 includes `estado_lifecycle`; neither derives from the other | Preserve content maturity and governance maturity as independent dimensions | R1.2/R3.1/R13.1/R14.1 vs R16.1/R16.6 | Package 000; ADR-0001; Architecture Baseline v1.0 | Tier 1 becomes exactly 8 owner fields; models and matrices separate both states |
| C3 | R5.5 said fast path required “only” five fields, internal use and approval | Fast path verifies all five R4 dimensions in one lightweight act; evidence/documentation depth is reduced, dimensions are not waived | Eliminate implicit exception to mandatory qualification | R4.1/R4.4 vs R5.5 | Requirements R4 plus INV-05 proportionality | Fast-path flow and gates explicitly include five dimensions |
| C4 | R5.4 left LabOS-Shared without dependencies outside clear classification and conflated authorized scope with exposure | Add independent `consumption_state`; Level 1 covers no effective external consumption, Level 2 covers active external consumption/dependencies, Level 3 covers Public/product attachment | Classify every Asset by actual use/risk while preserving sharing authorization | R2.2/R5.4/R9.1 | ADR-0002; Architecture Baseline INV-04/INV-05 | Exposure tables, registry model and sharing logic distinguish scope from consumption |

## Metadata cardinality after reconciliation

- Tier 1: exactly 8 owner-supplied fields: `nombre`, `tipo`, `descripción`, `hipótesis_de_uso`, `content_state`, `originating_Lab`, `source_of_truth`, `provenance`.
- The registry assigns provisional `asset_id`; it is not a ninth owner-supplied intake field.
- Tier 2: exactly 8 additional fields: `estado_lifecycle`, `versión`, `Asset_Owner`, `fecha_de_creación`, `nivel_de_compartición`, `consumption_state`, `dimensiones_calificación`, `aprobación_fundador`.
- The definitive `asset_id` refines the provisional identifier and is not counted twice.

## Approval effect

[Decisión] Requirements v1.3 received explicit Founder approval on 2026-08-12. The next authorized phase is `DESIGN_FINAL_REVIEW_AUTHORIZED`. Design v1.2 remains pending a separate Founder decision; Tasks and implementation remain unauthorized.
