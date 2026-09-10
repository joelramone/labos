# Package 004 — Product Factory Boundary Map

## Authority flow

```text
P001 Research ──evidence──► P002 Knowledge ──handoff──► P003 Assets
                                                        │
                                      CANONICAL + eligibility/dependency record
                                                        │
                                                        ▼
P004 Product Candidate → evaluation → READY → APPROVED → ACTIVE Product
                                                        │
                                      Product→Revenue handoff record
                                                        │
                                                        ▼
                                      P005 Revenue Engine (DORMANT)
```

Package 004 may reference a VALIDATED Asset while forming/evaluating a Candidate, but an effective Product attachment requires Package 003 `CANONICAL` eligibility and its complete handoff gate. Reference is not attachment.

## Entity and authority boundary

| Concern | Authoritative owner | P004 may | P004 must not |
|---|---|---|---|
| Research/evidence | Package 001 | Reference evidence and validation records | Rewrite research results or call demand proven without evidence |
| Knowledge | Package 002 | Reference canonical Knowledge/provenance | Change Knowledge lifecycle, confidence, ownership or SOT |
| Asset | Package 003 | Consume eligibility/dependency/restriction records; reference VALIDATED Assets during Candidate evaluation | Change Asset identity/lifecycle/version/owner/SOT; attach a non-eligible Asset |
| Product | Package 004 | Define identity, lifecycle, composition, quality, risk, readiness, approval, packaging, sharing and retirement | Infer commercialization or revenue from Product status |
| Revenue | Package 005 | Produce a governed Product→Revenue handoff | Execute pricing, payment, transactions, accounting or revenue optimization |
| AI Workspace/Automation | Packages 006/007 | Permit optional assistance after authorization | Require or activate either Package |
| Future infrastructure | Architecture governance | Declare an authorized dependency when it truly exists | Silently require persistence, RAG, MCP, agents or a technology |

## Attachment eligibility resolution

| Situation | Allowed in P004 | Classification |
|---|---|---|
| CANDIDATE/UNDER_REVIEW Asset | Cite as unavailable/gap evidence only | NOT_COMPOSABLE |
| VALIDATED, NOT_CANONICAL Asset | Reference in hypothetical Candidate composition and evaluate gap | REFERENCE_ONLY / NOT_ATTACHABLE |
| CANONICAL Asset lacking stability/licensing/maintainability/version/support gates | Evaluate, but do not attach | NOT_ELIGIBLE |
| CANONICAL Asset with complete Package 003 handoff eligibility | Record a proposed attachment during Product review | ELIGIBLE_FOR_GOVERNED_ATTACHMENT |
| Human Product approval without eligible Asset handoff | Does not cure the Asset gap | BLOCKED_COMPOSITION |

Package 003 decides and records Asset eligibility. Package 004 decides whether an eligible input fits a Product composition. Both decisions are required; neither substitutes for the other.

## Product→Revenue handoff boundary

Package 004 supplies:

- approved Product ID/version and lifecycle;
- Product Owner and source of truth;
- target consumer/problem/value proposition;
- demand-evidence status and limitations;
- composition and dependency manifest;
- delivery assumptions and sharing scope;
- licensing/risk/restriction summary;
- readiness/approval evidence;
- proposed monetization hypothesis reference, if present.

Package 004 stops before price execution, payment, transaction, revenue accounting, commercial optimization or declaring revenue validation. Package 005 remains dormant until its separate trigger and authorization.

## Manual-first operations

The following must remain executable through governed documents and human decisions without software infrastructure:

1. Candidate registration and identity check.
2. Composition/dependency declaration.
3. Evidence, demand, quality and risk review.
4. Readiness and approval decision recording.
5. Packaging manifest and restriction review.
6. Sharing, deprecation and retirement decisions.
7. Product→Revenue handoff preparation.

## Reference-case boundary

ASSET-1, ASSET-2 and ASSET-3 test whether requirements can represent Framework, Herramienta and Template dependencies. They remain `REFERENCE_CASES`; no Candidate, Product or attachment is created. Crypto-specific terminology and trading outcomes are prohibited as universal Product semantics. Human Performance remains paused and is not an active use case.
