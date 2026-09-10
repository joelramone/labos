# Package 004 — Design Decision Register

Design baseline: v1.0 `APPROVED` by `FD-P004-DESIGN-001`. The decisions below are the fifteen decisions reviewed from Design v0.1 and approved unchanged as the v1.0 baseline.

## Decisions

| ID | Decision | Rationale | Requirements trace | Alternatives considered | Constraints / consequences |
|---|---|---|---|---|---|
| P004-D001 | Use Product identity as aggregate root with version children | Separates stable offering identity from evolving governed versions | R01, R08–R10, R25 | Version as independent Product; flat record | One Product SOT per governed version; history retained |
| P004-D002 | Keep Candidate and Product records linked but distinct | Prevents proposal from inheriting approval | R02–R03, R09 | Single mutable record | Explicit human lifecycle decisions required |
| P004-D003 | Represent REJECTED as terminal review outcome | Implements exact seven-state Requirement and review note | R03 | Eighth state; RETIRED mapping | Rejected record remains UNDER_REVIEW historically with no forward transition |
| P004-D004 | Use guarded transition records for lifecycle | Makes evidence/authority/failure auditable | R03, R15–R16, R24–R25 | Direct state edits | All significant transitions human-controlled |
| P004-D005 | Use a read-only Attachment Eligibility Adapter | Preserves P003 authority | R04–R06 | Recompute/copy eligibility in P004 | P004 can reject fit but never grant eligibility |
| P004-D006 | Model composition as versioned reference snapshot | Reproduces decisions without copying upstream truth | R04, R06, R09–R10, R17–R18 | Embed Asset data | Upstream SOT remains authoritative |
| P004-D007 | Express readiness as an evidence matrix, not score | Avoids opaque compensation between mandatory controls | R11–R15 | Weighted numeric score | Outcomes are not lifecycle states |
| P004-D008 | Reuse a common governance envelope | Reduces record proliferation while preserving specialized evidence | R07, R12, R15–R16, R22–R25 | Unique unrelated formats | Human authority and immutable history uniform |
| P004-D009 | Separate approval from activation | APPROVED is authority; ACTIVE is scoped availability | R15–R16, R22 | One combined event | ACTIVE does not imply Public/commercial/revenue |
| P004-D010 | Use one conceptual Registry with distinct views | Answers governance questions without selecting storage | R01–R02, R08–R10, R23–R25 | Candidate/Product databases | Manual documents remain conforming |
| P004-D011 | Keep value, demand, readiness and Revenue orthogonal | Prevents evidence inflation | R13–R15, R21–R22 | Single maturity score | Each needs its own evidence and authority |
| P004-D012 | Treat sharing as a separate human decision | Lifecycle cannot broaden rights | R06, R12, R22 | Derive from ACTIVE | Most restrictive applicable constraint preserved |
| P004-D013 | Make AI permissions operation-based | Technology-neutral authority enforcement | R19–R20 | Agent-specific roles | AI remains optional and non-authoritative |
| P004-D014 | Support domain evidence profiles as extension points | Enables cross-domain use without changing core governance | R11–R12, R18–R20, R23 | Domain-specific lifecycle forks | First real cross-domain Candidate triggers review |
| P004-D015 | Use dossier-only P005 handoff | Preserves Revenue boundary | R21–R22 | Execute pricing/transaction in P004 | P005 remains dormant and separately authorized |

No decision changes the frozen baseline or warrants an ADR. No alternative rejected here is prohibited beyond what Requirements already establish.
