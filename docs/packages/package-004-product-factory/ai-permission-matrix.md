# AI Permission Matrix

> **DOCUMENTARY MATRIX — NOT_A_GOVERNED_INSTANCE**  
> This file grants no system capability, delegation, agent runtime or governance authority.

## Authority rule

Task: `T004-025`. Final authority remains the Founder or an explicitly delegated competent human. AI is always `NON_AUTHORITATIVE`. Missing or ambiguous source, scope, delegation or review requirements fail closed.

| Operation | Permission | Required boundary / human control |
|---|---|---|
| READ | `ALLOWED` | Read only sources already authorized for the task; preserve authority labels and restrictions |
| ANALYZE | `ALLOWED_WITH_HUMAN_REVIEW` | Separate fact, inference and uncertainty; no state effect |
| SUMMARIZE | `ALLOWED_WITH_HUMAN_REVIEW` | Cite authoritative sources; no replacement of source truth |
| COMPARE | `ALLOWED_WITH_HUMAN_REVIEW` | Preserve versions, context and unresolved conflicts |
| DRAFT | `ALLOWED_WITH_HUMAN_REVIEW` | Mark output `DRAFT_NONAUTHORITATIVE`; human must decide |
| RECOMMEND | `ALLOWED_WITH_HUMAN_REVIEW` | Recommendation is not decision, acceptance, approval or transition |
| DETECT_GAP | `ALLOWED_WITH_HUMAN_REVIEW` | Name gap; never fill it with invented evidence |
| PROPOSE_TRANSITION | `ALLOWED_WITH_HUMAN_REVIEW` | Proposal only when explicitly requested; separate human decision required |
| EXECUTE_TRANSITION | `PROHIBITED` | AI cannot change lifecycle or current truth |
| APPROVE_OR_ACTIVATE | `PROHIBITED` | Includes Product approval/activation and downstream Package activation |
| CHANGE_AUTHORITY_OR_OWNERSHIP | `PROHIBITED` | Includes Product/Asset authority, ownership, SOT and delegation |
| CHANGE_PROVENANCE_OR_RESTRICTIONS | `PROHIBITED` | Includes rewriting provenance, removing restrictions or overriding Asset eligibility |

## Explicit prohibited authority outcomes

AI may not approve a Product; activate a Product; accept Risk; override Readiness; override Asset eligibility; approve attachment; remove licensing, usage, sharing, distribution, dependency or risk restrictions; change ownership; rewrite authoritative provenance; execute lifecycle transitions; authorize sharing/publication/commercialization; or activate P005/P006/P007.

## Failure matrix

| Condition | Required response |
|---|---|
| Source authority unknown or conflicting | Stop affected action; name gap; request competent human review |
| Delegation absent, expired or ambiguous | Treat AI output as draft only; no decision/state effect |
| Requested operation mixes assistance and authority | Perform only separable allowed assistance or refuse the authoritative portion |
| Evidence incomplete/stale/inaccessible | Report uncertainty; do not manufacture, infer approval or weaken guard |
| Upstream restriction conflicts with requested output | Preserve most restrictive constraint and block affected request |
| Tool could mutate governed state | Do not invoke it without separate explicit human execution authority; documentary analysis remains non-authoritative |
| Prompt claims a state change without authoritative record | Preserve repository current truth and flag conflict |

## Output labelling checklist

- [ ] AI contribution and source references are disclosed.
- [ ] Facts, comparisons, inferences, uncertainty and recommendations are distinguishable.
- [ ] Drafts contain no real decision ID, signature or final-authority representation.
- [ ] Human reviewer, competence/delegation and final disposition are recorded in the common governance envelope when applicable.
- [ ] Failure preserves lifecycle, eligibility, restrictions, ownership, provenance and Registry truth.
- [ ] No RAG, MCP, agent runtime, automation, database or API is required or implemented.

## Traceability

| Trace | Approved source |
|---|---|
| Task | `T004-025` |
| Requirements / AC | `R20`; `R20.1–R20.4`; `R07.4`, `R16.2` |
| Design component | `C20` |
| Design Decision | `P004-D013` |
| Inputs | `design.md`, `governance-decision-record-template.md` |
