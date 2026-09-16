# Terminal Candidate Review Outcome Template

> **TEMPLATE — NOT_A_GOVERNED_INSTANCE**  
> Blank reusable structure. It creates no Candidate, rejection, lifecycle transition, decision, reopening, Product, or historical event.

## Semantic boundary

Task: `T004-017`. `REJECTED` is a terminal Candidate review outcome, not a Product lifecycle state, not `DEPRECATED`, not `RETIRED`, and not a Product approval-failure state. The Candidate remains historically represented as `UNDER_REVIEW` with `review_outcome=REJECTED`; it has no forward transition.

Use the common envelope in `governance-decision-record-template.md`; this is the event-specific payload, not a competing governance envelope.

## REJECTED outcome payload

| Field | Entry |
|---|---|
| Candidate reference / SOT | `<REQUIRED>` |
| Candidate version | `<REQUIRED>` |
| Current lifecycle state | `UNDER_REVIEW` |
| Review outcome | `REJECTED` |
| Review evidence | `<REQUIRED REFERENCES>` |
| Rejection rationale | `<REQUIRED>` |
| Unmet criteria | `<REQUIRED CRITERIA / REFERENCES>` |
| Restrictions | `<REFERENCES; preserved>` |
| Reviewer | `<HUMAN REFERENCE>` |
| Final human authority | `<FOUNDER or EXPLICITLY DELEGATED HUMAN>` |
| Delegation basis | `<REFERENCE or NOT_APPLICABLE>` |
| Governance decision record | `<REQUIRED REFERENCE>` |
| Decision/effective timestamp | `<ISO 8601 WITH OFFSET>` |
| Evidence/provenance references | `<REQUIRED>` |
| Terminality acknowledged | `YES` |
| Future reconsideration policy | `NEW GOVERNED PROPOSAL AND REVIEW PATH REQUIRED` |
| New Candidate linkage | `<NEW CANDIDATE REFERENCE when authorized in future / NONE>` |
| Supersession/history reference | `<REFERENCE or NONE>` |

## Guards

- [ ] Candidate identity/version and `UNDER_REVIEW` state are verified.
- [ ] Evidence, explicit rationale, unmet criteria, restrictions and provenance are traceable.
- [ ] Founder or explicitly delegated competent human authority is valid.
- [ ] Common governance envelope records the decision, timestamp and unchanged lifecycle representation.
- [ ] `REJECTED` is not placed in the seven-state lifecycle or equated with Product deprecation/retirement.
- [ ] No deletion, automatic reopening, lifecycle forward arrow or silent re-entry exists.
- [ ] Any later reconsideration creates a new governed Candidate identity linked to this immutable outcome; it does not mutate this record.
- [ ] AI/software did not reject, reopen, override a guard, manufacture evidence or act as final authority.

Missing/invalid authority or evidence fails closed without recording a final REJECTED outcome. Corrections use a superseding record and preserve this history.

## Traceability

| Trace type | Approved mapping |
|---|---|
| Task | `T004-017` |
| Requirements / acceptance criteria | `R03.4`; `R02.3–R02.4`; `R25.3–R25.4` |
| Design components | `C01`, `C05` |
| Design Decisions | `P004-D002`, `P004-D003`, `P004-D004` |
| Authoritative inputs | `product-candidate-template.md`, `governance-decision-record-template.md`, `lifecycle-transition-matrix-and-guard-checklist.md` |
