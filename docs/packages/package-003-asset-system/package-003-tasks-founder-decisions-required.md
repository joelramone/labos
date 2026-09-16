# Package 003 — Tasks Founder Decisions Required

## Status

No blocking Founder decisions remain. The historical item below is retained for traceability and marked `RESOLVED / NOT_REQUIRED_BY_CANONICAL_RULE`.

## FD-TASK-003-001 — Candidate template boundary — RESOLVED

| Field | Value |
|---|---|
| Question | Should `asset-candidate-template.md` remain a strict eight-field Tier 1 intake, with qualification/evaluation content owned only by `asset-evaluation-template.md`? |
| Recommendation | Yes. Approve a narrow Design 20.1 clarification that removes “Dimensiones obligatorias — evaluación inicial” and evaluator notes from the Candidate template, leaving exactly the eight owner-supplied Tier 1 fields plus the registry-assigned provisional ID note. |
| Alternative A | Keep Design 20.1 unchanged and allow preliminary qualification sections in Candidate intake. |
| Alternative B | Keep the extra sections but declare them optional and outside Tier 1 field count. |
| Trade-offs | Recommendation preserves the 3–5 minute intake target, prevents duplication with the evaluation template and keeps ownership clear. Alternative A increases intake overhead and duplicates evaluation. Alternative B retains ambiguity about what “Tier 1 only” means and makes field-count validation weaker. |
| Tasks affected | T003-026 directly; T003-027, T003-032, T003-033 and T003-035 downstream |
| Change classification | `DESIGN_CHANGE_REQUIRED` |
| Resolution | Design v1.2.1 PATCH DC-024 applied the already approved R16.1 canonical rule: Candidate intake requires exactly eight Tier 1 fields; evaluation/promotion owns Tier 2 completion |
| Decision status | `NOT_REQUIRED_BY_CANONICAL_RULE` — no conceptual choice remained after applying Requirements v1.3 |
| Founder reapproval | NOT REQUIRED under architecture-change-control-v1.0 PATCH policy |
| Blocking status | RESOLVED / NON_BLOCKING |

## Decision discipline

No other Founder decision was identified. Blocking Founder decisions: 0.

Tasks execution and Implementation remain `NOT_AUTHORIZED`.
