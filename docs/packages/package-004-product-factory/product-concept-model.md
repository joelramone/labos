# Package 004 — Product Concept Model

## Status and authority

Requirements-supporting conceptual model for `PACKAGE_004_REQUIREMENTS`, version 0.1, dated 2026-09-03. It defines no real Product, Candidate or attachment and selects no implementation technology.

## Product definition

A **Product** is a governed LabOS offering with a stable identity that composes eligible inputs and supporting material into a coherent solution for an identified target consumer and problem, has an explicit value proposition, has passed the Product-level quality, risk, demand and readiness gates applicable to its intended use, and has received explicit human Product approval.

A Product is distinct from:

| Entity | Distinction |
|---|---|
| Idea | An ungoverned possibility; it lacks Candidate identity and evidence gates |
| Research | An evidence-producing activity governed by Package 001 |
| Knowledge | A governed claim/object under Package 002; it may support evidence but is not an offering |
| Asset | A reusable governed input under Package 003; an Asset alone is not automatically a Product |
| Product Candidate | A governed proposal being formed/evaluated; not approved, active, commercial or revenue-ready |
| Revenue | Economic outcome/transaction governed downstream by Package 005 |
| Capability | A conceptual ability boundary; it is not a Product identity or approval |
| Lab | The organizational context that originates/owns work; it is not an offering |

Minimum Product identity is: `product_id`, name, purpose, target consumer, problem, value proposition, composition, originating context, human Product_Owner, evidence references, dependencies, restrictions, source of truth, lifecycle state and version.

## Product Candidate

A **Product Candidate** is a distinct governed proposal that connects an identifiable user/problem/value hypothesis to a proposed composition of Assets and other declared dependencies for Product-level evaluation. It exists so formation evidence can be preserved without mislabeling an idea or Asset as an approved Product.

Minimum entry requires a provisional ID, name, problem, target consumer, value proposition hypothesis, human owner, originating context, proposed composition, upstream references/restrictions, evidence references, one source of truth and lifecycle state `CANDIDATE`. Entry means neither Product approval, market validation, commercialization nor Revenue readiness.

## Product lifecycle

Exactly seven v1 states are defined for Product governance:

| State | Meaning | Entry | Permitted | Prohibited | Exit | Human authority | Evidence |
|---|---|---|---|---|---|---|---|
| `CANDIDATE` | Governed formation proposal | Minimum Candidate identity complete | Refine problem, consumer, composition and evidence | Claim approval/readiness/commercial status; attach ineligible Assets | Formation record complete and review initiated, or rejection | Product_Owner creates; Founder initiates review | Candidate record and upstream references |
| `UNDER_REVIEW` | Formal Product evaluation | Candidate complete; owner and review authority assigned | Evaluate quality, risk, demand, dependencies and restrictions | Automatic promotion, commercialization, Revenue execution | Gates support READY, remediation, or rejection | Human reviewer recommends; Founder decides transition | Review record and gate matrix |
| `READY` | Product definition and package are ready for human approval, not yet approved | Applicable quality/risk/demand/readiness gates pass | Prepare approval record and controlled delivery assumptions | Public/commercial release or ACTIVE claim | Explicit approval to APPROVED, or remain/re-enter review through new review record | Founder or explicitly delegated human Product Authority | Readiness decision and evidence package |
| `APPROVED` | Human-approved Product identity/version; release/operation still separate | READY plus valid human approval | Authorize a separately governed activation/release decision | Automatic ACTIVE/Public/commercial status | Explicit activation to ACTIVE, or retirement decision | Founder or delegated human Product Authority | Approval record, restrictions and effective scope |
| `ACTIVE` | Approved Product version available for its explicitly authorized non-commercial or commercial operating scope | APPROVED plus explicit activation, delivery scope and operational controls | Operate within approved scope; collect feedback | Exceed sharing/licensing/commercial authority | Deprecation decision or approved successor | Human Product Authority | Activation/release record and operational evidence |
| `DEPRECATED` | Product being retired or replaced | ACTIVE/APPROVED plus documented reason and impact | Maintain notices, migration and limited support | New consumers outside migration/exception scope | Retirement conditions satisfied | Human Product Authority | Consumer/dependency impact and exit plan |
| `RETIRED` | Terminal historical Product record | DEPRECATED with consumers/migrations resolved and history preserved | Historical reference only | Reactivation or new delivery under same lifecycle record | Terminal; renewed demand creates new Candidate/version as governed | Human Product Authority | Retirement decision and immutable history |

Permitted transitions:

```text
CANDIDATE → UNDER_REVIEW → READY → APPROVED → ACTIVE → DEPRECATED → RETIRED
                  └──────→ REJECTED is not introduced in v1; an unapproved Candidate
                           remains UNDER_REVIEW with a terminal rejection outcome record.
APPROVED → DEPRECATED is permitted when activation never occurs or becomes unsafe.
```

To keep exactly seven lifecycle states, rejection is a governed decision outcome, not a lifecycle state. A rejected Candidate remains historically recorded with `review_outcome=REJECTED` and no permitted forward transition; any renewed proposal receives a new Product Candidate identity. No transition with governance significance is automatic.

## Ownership and authority model

| Role | Responsibility | Authority limit |
|---|---|---|
| creator/author | Drafts Candidate/Product material | Does not acquire ownership or approval authority automatically |
| Product_Candidate_Owner | Maintains formation/evaluation record | Must be human; cannot override upstream restrictions |
| Product_Owner | Maintains approved Product identity/version and dependencies | Must be human; distinct from Asset owners |
| reviewer | Evaluates evidence and gates | Recommends; does not automatically approve |
| Product_Authority | Decides READY/APPROVED/ACTIVE/deprecation/retirement gates | Founder by default or explicitly delegated human authority |
| Asset_Owner | Retains authority over referenced Assets | Product ownership never transfers Asset ownership |
| consumer | Uses within authorized scope | Gains no ownership or governance authority |

AI may assist with inspection, comparison, drafts and recommendations. AI cannot occupy Product owner or Product Authority roles.

## Product value and validation

Product value is independent of Asset value:

- `HYPOTHESIZED`: identified consumer/problem/value proposition without direct demand evidence.
- `EVIDENCED`: credible non-transactional demand evidence from the target context supports the problem and proposed solution.
- `DEMONSTRATED`: documented real Product use produces an attributable user outcome; a transaction is not required.

These statuses do not change lifecycle automatically. `PRODUCT_VALIDATION` evaluates problem, target user, solution fit and non-revenue demand evidence. `REVENUE_VALIDATION` requires transaction/revenue evidence and belongs to Package 005.

## Source, provenance and versions

Each Product Candidate and each governed Product version has exactly one Product source of truth. It references, but never replaces, Asset/Knowledge/Research sources of truth. Minimum trace is `Product → Product Candidate → Assets → Knowledge → Research/Evidence` where links exist; missing historical links are recorded as gaps, not invented.

Product versioning uses `MAJOR.MINOR.PATCH`:

- MAJOR: incompatible target consumer/problem/value proposition, composition contract or delivery behavior; a fundamentally different offering requires a new Product identity.
- MINOR: compatible capability/composition/delivery extension with reassessed readiness.
- PATCH: compatible correction with no intended consumer, composition or delivery-contract change.

Any Asset version change triggers compatibility and readiness impact review; it does not automatically change Product version or status.

## V1 fast-path decision

`NO_PRODUCT_FAST_PATH_IN_V1`.

Current evidence comes from one originating Lab, all value/reuse remains projected and no real Product Candidate has exercised the governance path. Product risk aggregates multiple inputs and user impact. V1 therefore requires the complete human-gated lifecycle; future fast-path consideration requires new evidence and separately authorized requirements change.
