# Package 004 — Product Factory Task Plan

## Control

| Field | Value |
|---|---|
| Version | 1.0 |
| Status | `TASKS_APPROVED` |
| Date | 2026-09-03 |
| Requirements | v1.0 `APPROVED` — `FD-P004-REQ-001` |
| Design | v1.0 `APPROVED` — `FD-P004-DESIGN-001` |
| Tasks authorization | `FD-P004-TASKS-AUTH-001` |
| Founder Task Plan approval | `FD-P004-TASKS-001` |
| Package state | `TASKS_GENERATION_AUTHORIZED` |
| Task execution / implementation | `W0_COMPLETE / W1_COMPLETE / W2_AUTHORIZED_NOT_STARTED / W3–W7_NOT_AUTHORIZED` / `NOT_AUTHORIZED` |
| Wave status | W0 `COMPLETE`; W1 `COMPLETE`; W2 `AUTHORIZED_FOR_EXECUTION / NOT_STARTED`; W3–W7 `NOT_AUTHORIZED_FOR_EXECUTION` |
| Tasks | 32 (T004-001–005 `COMPLETE`; T004-006–010 `AUTHORIZED_FOR_EXECUTION / NOT_STARTED`; T004-011–032 `NOT_STARTED / NOT_AUTHORIZED_FOR_EXECUTION`) |

T004-001 is `COMPLETE` with evidence in `wave-0-baseline-integrity-record.md`. T004-002–005 are `COMPLETE` with evidence in `wave-1-execution-record.md`; T004-006–010 are `AUTHORIZED_FOR_EXECUTION / NOT_STARTED` under `FD-P004-W2-AUTH-001`; T004-011–032 remain `NOT_STARTED / NOT_AUTHORIZED_FOR_EXECUTION`. The planning states follow Package 003 precedent: `NOT_STARTED`, `BLOCKED`, `COMPLETE`.

## TASKS_SOURCE_MAP

| Code | Authoritative source | Planning contract consumed |
|---|---|---|
| ARCH | `LABOS-ARCH-BASELINE-001` v1.0, Freeze, change control and approved roadmap | Pipeline, documentation-first, human governance, freeze and change escalation |
| P003 | Closed Asset lifecycle/ownership/SOT/provenance/version/restriction and Asset→Product handoff; Package 003 Task precedent | Read-only attachment decision, upstream authority, Task contract, DAG/waves and execution separation |
| P004-REQ | Requirements v1.0, matrix, review and `FD-P004-REQ-001` | 25 Requirements and 100 acceptance criteria |
| P004-DES | Design v1.0, specialized designs, traceability, D001–D015, review and `FD-P004-DESIGN-001` | C01–C20, structures, records, interfaces and non-blocking realization notes |
| P004-AUTH | `FD-P004-TASKS-AUTH-001` | Task creation only; documentary-first, no execution or implementation |
| P005 | Revenue boundary and roadmap state | Dossier only; no Revenue operation; Package remains DORMANT |
| P006/7 | Package state records and roadmap | DORMANT; no mandatory AI/automation dependency |

Precedence: Founder decisions/frozen architecture within scope → approved Requirements → approved Design → closed upstream authority for its entities → supporting reviews and indexes. A Task requiring absent behavior stops as `DESIGN_CHANGE_REQUIRED` or `REQUIREMENTS_CHANGE_REQUIRED`.

## Task contract legend

- **Boundary:** execution requires an explicit wave decision. T004-001/W0 and T004-002–005/W1 are `COMPLETE`; T004-006–010/W2 are `AUTHORIZED_FOR_EXECUTION / NOT_STARTED`; T004-011–032 remain `PLANNED / NOT_AUTHORIZED_FOR_EXECUTION`. Implementation classification appears per Task.
- **Prohibited:** always includes real Candidate/Product/attachment creation, upstream mutation, technology selection and unauthorized execution unless a narrower prohibition is stated in addition.
- **Manual path:** identifies how a human can execute later using governed documents only.
- **Risk:** planning caution, not Product risk status.

## W0 — Preconditions and integrity

### T004-001 — Establish Tasks baseline and execution boundary

| Contract field | Plan |
|---|---|
| Authorization / status | `AUTHORIZED_FOR_EXECUTION / COMPLETE` — `FD-P004-W0-AUTH-001`; evidence: `wave-0-baseline-integrity-record.md` |
| Purpose / type | Verify authoritative baselines, authorization, package states and source precedence; `AUDIT` |
| Requirements / AC | R01–R25; R01.4, R03.1, R19.1–R19.4, R20.4, R21.3–R21.4, R25.2 |
| Design / decisions | C01–C20; D001–D015 |
| Inputs | Approved Requirements/Design and Founder decisions; Architecture Freeze; P003/P005 boundaries; P006/7 state |
| Expected outputs | Tasks source map, baseline checklist, initial integrity snapshot and named conflicts/gaps |
| Dependencies | None; W0 blocker for T004-002–032 |
| Boundary / prohibited | `DOCUMENTARY`; do not change any baseline, create operational records or authorize execution |
| Acceptance evidence | Checklist confirms Requirements/Design approval, Tasks-generation authority, Freeze preserved, P003 closed, P005–7 dormant, Assets unchanged, Human Performance paused and infrastructure optional |
| Completion / risk / manual path | Complete when every source and state resolves or a blocking change classification is recorded; MEDIUM risk of stale metadata; human cross-checks records and signs checklist |

## W1 — Core Product, Candidate and governance structures

### T004-002 — Create Product Candidate governance template

| Contract field | Plan |
|---|---|
| Authorization / status | `COMPLETE` — authorized by `FD-P004-W1-AUTH-001`; evidence `wave-1-execution-record.md` |
| Purpose / type | Realize provisional Candidate identity, intake gaps, evaluation links and unapproved visibility; `TEMPLATE` |
| Requirements / AC | R02; R02.1–R02.4; R07.1; R08.1; R23.1 |
| Design / decisions | C01; D002, D010 |
| Inputs | Product aggregate/Candidate Design, common terminology and T004-001 |
| Expected outputs | Candidate template with identity, owner, problem, consumer, hypothesis, context, proposed inputs, evidence/restrictions, SOT, state and review trigger |
| Dependencies | T004-001; blocks T004-017, T004-020, T004-028 |
| Boundary / prohibited | `DOCUMENTARY`; template only; no Candidate instance or Product claim |
| Acceptance evidence | Field/gap audit proves incomplete intake is named, complete intake starts only in CANDIDATE and causes zero Asset/Product/commercial effect |
| Completion / risk / manual path | Complete after independent field and wording review; MEDIUM misclassification risk; human fills a blank dry-run without registering it |

### T004-003 — Create governed Product aggregate record template

| Contract field | Plan |
|---|---|
| Authorization / status | `COMPLETE` — authorized by `FD-P004-W1-AUTH-001`; evidence `wave-1-execution-record.md` |
| Purpose / type | Realize Product identity/version aggregate and distinguish it from upstream/downstream entities; `TEMPLATE` |
| Requirements / AC | R01; R01.1–R01.4; R07.1, R07.3; R25.1 |
| Design / decisions | C02; D001, D002, D010 |
| Inputs | Approved aggregate/cardinalities and T004-001 |
| Expected outputs | Product record template referencing owner, consumer/problem/value, composition, context, evidence, dependencies, restrictions, SOT, lifecycle and version |
| Dependencies | T004-001; blocks T004-005–010, T004-018–024 |
| Boundary / prohibited | `DOCUMENTARY`; no Product instance, approval or duplicated Asset truth |
| Acceptance evidence | Entity/mandatory-gap audit and duplicate-identity flag contract |
| Completion / risk / manual path | Complete when every R01 identity element is present-or-missing and upstream definitions remain referenced; MEDIUM authority-leak risk; manual inspection |

### T004-004 — Create reusable Governance Decision Record

| Contract field | Plan |
|---|---|
| Authorization / status | `COMPLETE` — authorized by `FD-P004-W1-AUTH-001`; evidence `wave-1-execution-record.md` |
| Purpose / type | Realize one common envelope with event-specific sections; `GOVERNANCE_ARTIFACT` |
| Requirements / AC | R03.2–R03.4, R07.2, R12.3, R15.3, R16.1–R16.4, R22.3, R24.1–R24.3, R25.4 |
| Design / decisions | C05, C17, C19; D004, D008, D009, D012 |
| Inputs | Governance Design and T004-001 |
| Expected outputs | Reusable record: action, subject/state, evidence, restrictions, decision, authority/delegation, timestamp, rationale, resulting/unchanged state and follow-up |
| Dependencies | T004-001; blocks T004-005, T004-012, T004-015–018, T004-021–024 |
| Boundary / prohibited | `DOCUMENTARY`; no decision instance, automatic state change or merged decision semantics |
| Acceptance evidence | Event-to-common-envelope matrix covers review/readiness/approval/activation/risk/sharing/review/deprecation/retirement/handoff without duplicate physical systems |
| Completion / risk / manual path | Complete when common and event-specific fields are separable; MEDIUM over-generalization risk; human prepares and signs a blank exemplar |

### T004-005 — Create Product ownership and SOT declaration templates

| Contract field | Plan |
|---|---|
| Authorization / status | `COMPLETE` — authorized by `FD-P004-W1-AUTH-001`; evidence `wave-1-execution-record.md` |
| Purpose / type | Realize human ownership/transfer and exactly-one Product SOT distinctions; `TEMPLATE` |
| Requirements / AC | R07–R08; R07.1–R08.4 |
| Design / decisions | C02, C19; D001, D008, D010 |
| Inputs | T004-003–004; upstream ownership/SOT contracts |
| Expected outputs | Ownership/transfer section plus SOT declaration distinguishing Asset SOT, evidence, managed mirror, working/derived/unmanaged copy |
| Dependencies | T004-003, T004-004; blocks T004-010, T004-020 |
| Boundary / prohibited | `DOCUMENTARY`; no ownership transfer, storage choice or competing authority |
| Acceptance evidence | Role and single-SOT conflict scenarios; AI rejected as owner/authority; Product ownership does not transfer Asset ownership |
| Completion / risk / manual path | Complete when one authoritative Product/version source resolves and conflicts fail closed; HIGH authority risk; human source/role audit |

## W2 — Composition, upstream interface and delivery inputs

### T004-006 — Create Product composition record template

| Contract field | Plan |
|---|---|
| Authorization / status | `AUTHORIZED_FOR_EXECUTION / NOT_STARTED` — `FD-P004-W2-AUTH-001` |
| Purpose / type | Realize one/many/shared Asset references and separate external inputs without merging authority; `TEMPLATE` |
| Requirements / AC | R04, R06; R04.1–R04.4, R06.1–R06.4 |
| Design / decisions | C03; D005, D006 |
| Inputs | T004-003, P003 Asset authority and composition Design |
| Expected outputs | Versioned composition snapshot with input identity/version, contribution type, relationship, SOT/provenance/restriction and fit result references |
| Dependencies | T004-003; blocks T004-007–010, T004-011–015, T004-020, T004-028 |
| Boundary / prohibited | `DOCUMENTARY`; no embedded Asset authority, attachment or eligibility grant |
| Acceptance evidence | Cardinality/restriction mapping for one, many, shared and external cases; unresolved license/risk blocks Product gate only |
| Completion / risk / manual path | Complete when every upstream constraint maps to effect/non-applicability; HIGH restriction risk; human reference audit |

### T004-007 — Create P003 attachment-eligibility reference contract

| Contract field | Plan |
|---|---|
| Authorization / status | `AUTHORIZED_FOR_EXECUTION / NOT_STARTED` — `FD-P004-W2-AUTH-001`; start gated by T004-006 `COMPLETE` |
| Purpose / type | Realize read-only consumption of P003 eligibility; `INTERFACE_CONTRACT` |
| Requirements / AC | R05; R05.1–R05.4; R06.3–R06.4 |
| Design / decisions | C04; D005 |
| Inputs | T004-006 and closed P003 Asset→Product handoff |
| Expected outputs | Eligibility-reference template capturing P003 decision/evidence, intended Product use and immutable consumption result |
| Dependencies | T004-006; blocks T004-009, T004-020, T004-028, T004-030 |
| Boundary / prohibited | `DOCUMENTARY`; `WRITE / OVERRIDE / RECOMPUTE` prohibited; no real Asset update |
| Acceptance evidence | Contract exposes only READ/REFERENCE/CONSUME and exact four P003 outcome mappings |
| Completion / risk / manual path | Complete when P004 can reject fit but never grant eligibility; HIGH upstream-authority risk; human compares against P003 handoff |

### T004-008 — Create Product dependency declaration

| Contract field | Plan |
|---|---|
| Authorization / status | `AUTHORIZED_FOR_EXECUTION / NOT_STARTED` — `FD-P004-W2-AUTH-001`; start gated by T004-006 `COMPLETE` |
| Purpose / type | Realize Asset, external, operational and platform dependencies; `REGISTRY` |
| Requirements / AC | R18; R18.1–R18.4; R23.1–R23.3 |
| Design / decisions | C11; D006, D010 |
| Inputs | T004-003, T004-006 and dependency Design |
| Expected outputs | Dependency template with identity, type, version/compatibility, purpose, criticality, provider, restrictions, status, failure impact, fallback/exit and review trigger |
| Dependencies | T004-003, T004-006; blocks T004-009, T004-011–015, T004-020, T004-022–024 |
| Boundary / prohibited | `DOCUMENTARY`; no implicit RAG/MCP/agents/automation/Persistence dependency |
| Acceptance evidence | Four-class completeness and undeclared/critical-change scenario criteria |
| Completion / risk / manual path | Complete when all four classes and failure behavior are inspectable; MEDIUM hidden-dependency risk; human register review |

### T004-009 — Create Product packaging manifest

| Contract field | Plan |
|---|---|
| Authorization / status | `AUTHORIZED_FOR_EXECUTION / NOT_STARTED` — `FD-P004-W2-AUTH-001`; start gated by T004-006–008 `COMPLETE` |
| Purpose / type | Realize technology-neutral presentation/delivery manifest; `TEMPLATE` |
| Requirements / AC | R17; R17.1–R17.4; R22.4 |
| Design / decisions | C14; D006, D012 |
| Inputs | T004-003, T004-006–008 |
| Expected outputs | Manifest for Product/version, eligible Asset/SOT references, documentation, guidance, restrictions, dependencies, provenance, consumer and delivery assumptions |
| Dependencies | T004-003, T004-006–008; blocks T004-015, T004-021, T004-024 |
| Boundary / prohibited | `DOCUMENTARY`; no ZIP/container/installer/package-manager or broadened right |
| Acceptance evidence | Required-element/gap audit, exact input-version references and point-of-delivery restriction visibility |
| Completion / risk / manual path | Complete when missing items are explicit and rights remain unchanged; HIGH licensing risk; human manifest checklist |

### T004-010 — Create Product provenance record

| Contract field | Plan |
|---|---|
| Authorization / status | `AUTHORIZED_FOR_EXECUTION / NOT_STARTED` — `FD-P004-W2-AUTH-001`; start gated by T004-006 `COMPLETE` |
| Purpose / type | Realize lineage from Research/Knowledge through Candidate/Product and future P005 handoff; `REGISTRY` |
| Requirements / AC | R09; R09.1–R09.4; R17.2; R21.1; R25.3 |
| Design / decisions | C12; D001, D002, D006, D015 |
| Inputs | T004-002–003, T004-005–006 and upstream provenance references |
| Expected outputs | Provenance graph record with source authority, exact versions, Candidate origin, decision references and explicit missing-link gaps |
| Dependencies | T004-002, T004-003, T004-005, T004-006; blocks T004-015, T004-020, T004-024 |
| Boundary / prohibited | `DOCUMENTARY`; no copied authority, fabricated evidence or overwritten history |
| Acceptance evidence | Complete/partial/external-origin lineage scenarios answer evidence, Assets/versions and approving decisions |
| Completion / risk / manual path | Complete when absent links remain honest gaps; HIGH evidence-integrity risk; human follows each reference |

## W3 — Product evidence and readiness

### T004-011 — Create Product Quality evaluation matrix

| Contract field | Plan |
|---|---|
| Purpose / type | Realize nine Product-level quality dimensions independently of Asset quality; `MATRIX` |
| Requirements / AC | R11; R11.1–R11.4 |
| Design / decisions | C07; D007, D011 |
| Inputs | T004-006, T004-008 and Product quality Design |
| Expected outputs | PASS/PARTIAL/FAIL/NOT_APPLICABLE matrix for composition correctness, completeness, usability, applicable reproducibility, dependency integrity, documentation, consumer suitability, failure behavior and operational readiness, with evidence/blocking disposition |
| Dependencies | T004-006, T004-008; blocks T004-015 |
| Boundary / prohibited | `DOCUMENTARY`; no invented metrics, composite score or Asset-quality substitution |
| Acceptance evidence | 9/9 dimension audit and mandatory-failure scenario |
| Completion / risk / manual path | Complete when applicability/evidence/blocking are explicit; MEDIUM false-assurance risk; human dimension review |

### T004-012 — Create Product Risk evaluation and acceptance sections

| Contract field | Plan |
|---|---|
| Purpose / type | Realize nine-category aggregate risk, propagation and human acceptance/escalation; `MATRIX` |
| Requirements / AC | R06, R12; R06.1–R06.4, R12.1–R12.4 |
| Design / decisions | C08, C19; D007, D008, D012 |
| Inputs | T004-004, T004-006–008 |
| Expected outputs | Financial, legal/licensing, operational, technical, evidence, user-impact, misuse, dependency and reputational risk matrix plus event-specific common-record section with likelihood, impact, mitigation, residual/blocking status, scope and review trigger |
| Dependencies | T004-004, T004-006, T004-008; blocks T004-015, T004-021, T004-024 |
| Boundary / prohibited | `DOCUMENTARY`; no silent upstream risk/restriction reduction or automated acceptance |
| Acceptance evidence | 9/9 categories, HIGH/CRITICAL block, conflicting restriction and status-not-assurance scenarios |
| Completion / risk / manual path | Complete when only competent human acceptance can change disposition; HIGH safety/legal risk; human category and authority audit |

### T004-013 — Create Product Value evidence record

| Contract field | Plan |
|---|---|
| Purpose / type | Realize HYPOTHESIZED/EVIDENCED/DEMONSTRATED progression; `TEMPLATE` |
| Requirements / AC | R13; R13.1–R13.4 |
| Design / decisions | C09; D007, D011 |
| Inputs | T004-003 and value Design |
| Expected outputs | Value record tied to consumer/problem/outcome with dated evidence and transition rationale |
| Dependencies | T004-003; blocks T004-015, T004-024 |
| Boundary / prohibited | `DOCUMENTARY`; no real value claim, revenue inference or automatic lifecycle change |
| Acceptance evidence | Three-state evidence matrix; projected Asset value fails DEMONSTRATED scenario |
| Completion / risk / manual path | Complete when each upgrade requires its approved evidence; MEDIUM evidence-inflation risk; human reference review |

### T004-014 — Create Demand Validation plan/result template

| Contract field | Plan |
|---|---|
| Purpose / type | Realize falsifiable non-transactional Product-demand evidence; `TEMPLATE` |
| Requirements / AC | R14; R14.1–R14.4 |
| Design / decisions | C10; D007, D011 |
| Inputs | T004-003 and demand Design |
| Expected outputs | Hypothesis, segment, method, signal, criterion, timeframe, source, dated context/participant, result, limitations, privacy and review authority sections |
| Dependencies | T004-003; blocks T004-015, T004-024 |
| Boundary / prohibited | `DOCUMENTARY`; no interviews, market validation, pricing or transaction execution |
| Acceptance evidence | Plan/result completeness and failed/inconclusive/no-revenue-inference scenarios |
| Completion / risk / manual path | Complete when pass/fail is falsifiable and privacy handling visible; MEDIUM privacy/inference risk; human documentary scenario |

### T004-015 — Create Product Readiness matrix and decision section

| Contract field | Plan |
|---|---|
| Purpose / type | Realize eleven-control readiness without opaque scoring; `MATRIX` |
| Requirements / AC | R15; R15.1–R15.4; R16.2 |
| Design / decisions | C06, C19; D007, D008, D009, D011 |
| Inputs | T004-004, T004-006, T004-008–014 |
| Expected outputs | Evidence/blocking matrix for composition, evidence, quality, risk, provenance, ownership, dependencies, restrictions, target consumer, demand evidence and documentation, plus READY/NOT_READY/REVIEW_REQUIRED decision section |
| Dependencies | T004-004, T004-006, T004-008–014; blocks T004-016, T004-018, T004-020, T004-028–029 |
| Boundary / prohibited | `DOCUMENTARY`; no score, automatic threshold, approval, activation or commercialization |
| Acceptance evidence | 11/11 controls; mandatory fail prevents READY; human/date/rationale/restrictions; READY implications explicitly denied |
| Completion / risk / manual path | Complete when record result and lifecycle transition are structurally separate; HIGH hidden-state risk; human matrix/gate review |

## W4 — Lifecycle, approval, versioning and Registry

### T004-016 — Create lifecycle transition matrix and guard checklist

| Contract field | Plan |
|---|---|
| Purpose / type | Realize exactly seven states and every approved guarded transition; `WORKFLOW` |
| Requirements / AC | R03; R03.1–R03.4; R16.3–R16.4; R24.2 |
| Design / decisions | C05; D003, D004, D009 |
| Inputs | T004-004, T004-015 and approved lifecycle Design |
| Expected outputs | State table, transition matrix, guard checklist, invalid-transition response and historical transition section |
| Dependencies | T004-004, T004-015; blocks T004-017–018, T004-020, T004-023, T004-027–029 |
| Boundary / prohibited | `DOCUMENTARY`; no eighth state, automatic promotion or actual transition |
| Acceptance evidence | Diagram/table has seven states; each transition has source/destination/trigger/evidence/guard/authority/record; invalid requests fail closed |
| Completion / risk / manual path | Complete after transition enumeration equivalence audit; HIGH lifecycle risk; human walks each row |

### T004-017 — Create terminal Candidate review-outcome section

| Contract field | Plan |
|---|---|
| Purpose / type | Realize Founder-confirmed REJECTED history without lifecycle mutation; `TEMPLATE` |
| Requirements / AC | R03.4, R02.3–R02.4, R25.3–R25.4 |
| Design / decisions | C01, C05; D002, D003, D004 |
| Inputs | T004-002, T004-004, T004-016 |
| Expected outputs | REJECTED event section preserving Candidate ID, evidence, authority, timestamp, reason, terminality and reconsideration link rule |
| Dependencies | T004-002, T004-004, T004-016; blocks T004-020, T004-028–029 |
| Boundary / prohibited | `DOCUMENTARY`; not a state, DEPRECATED, RETIRED or forward transition |
| Acceptance evidence | State-count and historical-preservation controlled checks |
| Completion / risk / manual path | Complete when no field or arrow permits silent re-entry; HIGH semantic risk; human lifecycle comparison |

### T004-018 — Create Product approval and activation event sections

| Contract field | Plan |
|---|---|
| Purpose / type | Realize separate human READY→APPROVED and APPROVED→ACTIVE decisions; `GOVERNANCE_ARTIFACT` |
| Requirements / AC | R16; R16.1–R16.4; R22.1 |
| Design / decisions | C05, C19; D004, D008, D009 |
| Inputs | T004-003–004, T004-015–016 |
| Expected outputs | Approval and activation sections referencing exact Product/version, evidence/readiness, restrictions, authority, scope, timestamp and reason |
| Dependencies | T004-003, T004-004, T004-015, T004-016; blocks T004-020–021, T004-023–024, T004-029 |
| Boundary / prohibited | `DOCUMENTARY`; no real approval/activation, AI authority or Public/commercial/revenue inference |
| Acceptance evidence | Missing/invalid authority fails closed; APPROVED≠ACTIVE and ACTIVE≠Public/commercial/revenue scenarios |
| Completion / risk / manual path | Complete when two records and guards cannot collapse; HIGH authority risk; human side-by-side audit |

### T004-019 — Create Product version and compatibility record

| Contract field | Plan |
|---|---|
| Purpose / type | Realize Requirements-defined MAJOR/MINOR/PATCH, supersession and Asset-version review; `TEMPLATE` |
| Requirements / AC | R10; R10.1–R10.4; R23.1–R23.3 |
| Design / decisions | C13; D001, D004, D006 |
| Inputs | T004-003, T004-006, T004-008 and version Design |
| Expected outputs | Product identity/version, effective date, rationale, supersedes, input versions, compatibility, classification and review trigger |
| Dependencies | T004-003, T004-006, T004-008; blocks T004-020, T004-022–024 |
| Boundary / prohibited | `DOCUMENTARY`; no invented version semantics or automatic Product/Asset lifecycle/version change |
| Acceptance evidence | MAJOR/MINOR/PATCH and fundamentally-different-offering scenarios match R10 exactly |
| Completion / risk / manual path | Complete when every material change routes to compatibility/readiness review; MEDIUM compatibility risk; human classification table |

### T004-020 — Create manual Product Registry contract and views

| Contract field | Plan |
|---|---|
| Purpose / type | Realize current Candidate/Product lookup and immutable governance history; `REGISTRY` |
| Requirements / AC | R01–R02, R08–R10, R18, R23–R25; R25.1–R25.4 |
| Design / decisions | C01, C02, C12, C13, C15; D001–D004, D006, D010 |
| Inputs | T004-002–019 applicable outputs |
| Expected outputs | Documentary Candidate/Product, composition/eligibility, evidence and history views with missing-data reporting |
| Dependencies | T004-002–019; blocks T004-021–024, T004-027–031 |
| Boundary / prohibited | `DOCUMENTARY`; no database/API/service, silent rewrite or competing SOT |
| Acceptance evidence | Lookup checklist answers identity/version/owner/lifecycle/composition/eligibility/restrictions/dependencies/evidence/readiness/approval/sharing/SOT/review; duplicate/unauthorized changes rejected |
| Completion / risk / manual path | Complete when current truth and history reconcile bidirectionally; HIGH historical-truth risk; human index/reference audit |

## W5 — Sharing, review, retirement, boundaries and manual operation

### T004-021 — Create Product sharing decision and restriction check

| Contract field | Plan |
|---|---|
| Purpose / type | Realize sharing as an orthogonal human decision; `GOVERNANCE_ARTIFACT` |
| Requirements / AC | R06, R12, R22; R22.1–R22.4 |
| Design / decisions | C08, C16, C19; D008, D012 |
| Inputs | T004-004, T004-009, T004-012, T004-018, T004-020 |
| Expected outputs | Audience/context, licensing, sensitivity, Product/upstream restrictions, risk, authority and effective-permission decision section |
| Dependencies | T004-004, T004-009, T004-012, T004-018, T004-020; blocks T004-024, T004-027, T004-030 |
| Boundary / prohibited | `DOCUMENTARY`; ACTIVE cannot imply PUBLIC; packaging cannot broaden rights |
| Acceptance evidence | Most-restrictive permission and external/Public review scenarios; approval/demand not commercialization |
| Completion / risk / manual path | Complete when every upstream restriction maps to effective scope; HIGH licensing risk; human restriction intersection |

### T004-022 — Create Product review and freshness record/checklist

| Contract field | Plan |
|---|---|
| Purpose / type | Realize event/date review triggers without lifecycle automation; `WORKFLOW` |
| Requirements / AC | R18.4, R23; R23.1–R23.4 |
| Design / decisions | C11, C15; D004, D010 |
| Inputs | T004-004, T004-008, T004-019–020 |
| Expected outputs | Trigger checklist and comparison record for Asset/Product/dependency/version/schema, licensing/risk, evidence/use, demand/consumer/context, source/exposure and schedule |
| Dependencies | T004-004, T004-008, T004-019, T004-020; blocks T004-023, T004-027, T004-031 |
| Boundary / prohibited | `DOCUMENTARY`; no automated notification requirement or state change |
| Acceptance evidence | Fired-trigger preserves state, compares prior decision and records stale/inaccessible sources |
| Completion / risk / manual path | Complete when every R23 trigger has human disposition; MEDIUM stale-evidence risk; periodic paper checklist |

### T004-023 — Create deprecation and retirement decision sections

| Contract field | Plan |
|---|---|
| Purpose / type | Realize APPROVED/ACTIVE→DEPRECATED→RETIRED with impact/history; `GOVERNANCE_ARTIFACT` |
| Requirements / AC | R24; R24.1–R24.4; R23.2–R23.4 |
| Design / decisions | C05, C17, C19; D004, D008, D010 |
| Inputs | T004-004, T004-016, T004-018–020, T004-022 |
| Expected outputs | Deprecation/retirement sections for reason, authority/date, consumers/dependencies, successor, migration/exit, exceptions and history |
| Dependencies | T004-004, T004-016, T004-018–020, T004-022; blocks T004-027, T004-029, T004-031 |
| Boundary / prohibited | `DOCUMENTARY`; no direct retirement, deletion or reactivation |
| Acceptance evidence | DEPRECATED historical entry required; obligations resolved/excepted; renewed demand creates governed new path |
| Completion / risk / manual path | Complete when terminal history remains immutable; HIGH consumer/history risk; human impact/exit review |

### T004-024 — Create Product→Revenue handoff dossier

| Contract field | Plan |
|---|---|
| Purpose / type | Realize governed dossier at the P004→P005 boundary; `INTERFACE_CONTRACT` |
| Requirements / AC | R13–R16, R18, R21–R22; R21.1–R21.4 |
| Design / decisions | C18, C19; D008, D009, D011, D015 |
| Inputs | T004-003–004, T004-008–15, T004-18–21 |
| Expected outputs | Handoff checklist/record for approved Product identity/version/state, owner/SOT, consumer/problem/value, demand, composition/dependencies, delivery/sharing, restrictions, risk/readiness and provenance |
| Dependencies | T004-003, T004-004, T004-008–015, T004-018–021; blocks T004-027–028, T004-030 |
| Boundary / prohibited | `DOCUMENTARY`; no pricing, payment, transaction, accounting, optimization, Revenue validation or P005 activation |
| Acceptance evidence | Missing approval/license blocks; all dossier fields or gaps; creation produces neither revenue nor Package activation |
| Completion / risk / manual path | Complete when boundary exclusions are mechanically inspectable; HIGH scope risk; human dossier checklist |

### T004-025 — Create AI permission matrix

| Contract field | Plan |
|---|---|
| Purpose / type | Realize operation-based AI assistance boundaries; `MATRIX` |
| Requirements / AC | R20; R20.1–R20.4; R07.4, R16.2 |
| Design / decisions | C20; D013 |
| Inputs | AI boundary Design and T004-004 |
| Expected outputs | ALLOWED/ALLOWED_WITH_HUMAN_REVIEW/PROHIBITED matrix for all twelve approved operations plus authority failures |
| Dependencies | T004-004; blocks T004-027, T004-029, T004-031 |
| Boundary / prohibited | `DOCUMENTARY`; no Agent/RAG/MCP implementation or AI authority |
| Acceptance evidence | Non-authoritative labelling/source uncertainty and fail-closed prohibited-operation scenarios |
| Completion / risk / manual path | Complete when execute/approve/authority/provenance changes cannot be delegated; HIGH authority risk; human permission audit |

### T004-026 — Create domain-extension evidence profile template

| Contract field | Plan |
|---|---|
| Purpose / type | Allow domain quality/risk/dependency evidence without core lifecycle change; `TEMPLATE` |
| Requirements / AC | R11–R12, R18–R20, R23; applicable R11.1, R12.1, R18.1, R19.2–R19.4 |
| Design / decisions | C07, C08, C11, C20; D014 |
| Inputs | T004-011–012, T004-008, T004-022, approved domain-extension Design |
| Expected outputs | Extension profile and `DOMAIN_NEUTRALITY_REVIEW` trigger declaration |
| Dependencies | T004-008, T004-011, T004-012, T004-022; blocks T004-027, T004-031 |
| Boundary / prohibited | `DOCUMENTARY`; no Human Performance use, real cross-domain Candidate or lifecycle/governance fork |
| Acceptance evidence | Neutral example proves extension fields cannot change core states/authority/Registry truth |
| Completion / risk / manual path | Complete when domain evidence remains additive/reference-based; MEDIUM semantic-fork risk; human neutrality checklist |

### T004-027 — Create manual-first Product Factory operating procedure

| Contract field | Plan |
|---|---|
| Purpose / type | Integrate formation through retirement using documents only; `WORKFLOW` |
| Requirements / AC | R02–R03, R05, R07, R11–R16, R19–R25; R19.1–R19.4 |
| Design / decisions | C01–C20; D002–D015 |
| Inputs | T004-002–026 completed documentary artifacts |
| Expected outputs | Stepwise procedure, roles, inputs/outputs, fail-closed paths, record index and wave-independent manual fallback |
| Dependencies | T004-002–026; blocks T004-028–032 |
| Boundary / prohibited | `DOCUMENTARY`; no database, automation, P006/7, Persistence, RAG, MCP or Agent dependency |
| Acceptance evidence | Every named R19 operation has documentary path; manual decisions preserve authority/evidence/history; automation remains replaceable/auditable |
| Completion / risk / manual path | Complete after end-to-end tabletop walkthrough; HIGH integration risk; Founder can operate solely from files/templates |

## W6 — Controlled fixtures and verification

### T004-028 — Create controlled test-fixture set

| Contract field | Plan |
|---|---|
| Purpose / type | Define ten synthetic documentary cases without real governance effects; `CONTROLLED_VERIFICATION` |
| Requirements / AC | R02–R06, R09, R11–R18, R21–R25; scenario AC across these Requirements |
| Design / decisions | C01–C19; D002–D012, D015 |
| Inputs | T004-002–024, T004-027 and fixture plan |
| Expected outputs | Ten records explicitly labelled `CONTROLLED_TEST_FIXTURE`, expected outcomes and cleanup/non-authority statement |
| Dependencies | T004-002–024, T004-027; blocks T004-029–032 |
| Boundary / prohibited | `CONTROLLED_VERIFICATION`; plan fixture creation only; no real Candidate/Product/Asset/approval or evidence claim |
| Acceptance evidence | Fixture inventory covers simple/rejected Candidate, two eligibility cases, two readiness/approval cases, active-not-public, restriction propagation and P005 boundary |
| Completion / risk / manual path | Complete when every fixture is synthetic, reversible and expected-result mapped; HIGH accidental-authority risk; human labels/reviews documents |

### T004-029 — Verify lifecycle, readiness and human/AI authority

| Contract field | Plan |
|---|---|
| Purpose / type | Plan controlled checks for state/outcome/gate separation; `CONTROLLED_VERIFICATION` |
| Requirements / AC | R03, R07, R15–R16, R20, R24–R25; all corresponding AC |
| Design / decisions | C01, C02, C05, C06, C17, C19, C20; D002–D004, D007–D010, D013 |
| Inputs | T004-015–018, T004-023, T004-025, T004-027–028 |
| Expected outputs | Verification evidence matrix for seven states, REJECTED, readiness separation, human approval, AI denial, activation and retirement history |
| Dependencies | T004-015–018, T004-023, T004-025, T004-027, T004-028; blocks T004-032 |
| Boundary / prohibited | `CONTROLLED_VERIFICATION`; no real transition or automated approval |
| Acceptance evidence | Each controlled result matches approved guards; failures preserve state and name gaps |
| Completion / risk / manual path | Complete when all planned cases have observable pass/fail evidence; HIGH lifecycle/authority risk; manual walkthrough and matrix sign-off |

### T004-030 — Verify attachment, restriction, sharing and Revenue boundaries

| Contract field | Plan |
|---|---|
| Purpose / type | Plan controlled P003/P005 and permission-boundary checks; `CONTROLLED_VERIFICATION` |
| Requirements / AC | R04–R06, R12, R17–R18, R21–R22; all corresponding AC |
| Design / decisions | C03, C04, C08, C11, C14, C16, C18, C19; D005–D006, D008, D012, D015 |
| Inputs | T004-006–012, T004-021, T004-024, T004-027–028 |
| Expected outputs | Four synthetic eligibility results, ASSET-1/2/3 read-only refusal evidence, restriction/sharing checks and P005 exclusion matrix |
| Dependencies | T004-006–012, T004-021, T004-024, T004-027, T004-028; blocks T004-032 |
| Boundary / prohibited | `CONTROLLED_VERIFICATION`; no Asset mutation/attachment, commercialization or P005 action |
| Acceptance evidence | Exact P003 mappings, most-restrictive rule, ACTIVE≠PUBLIC and zero forbidden Revenue operations |
| Completion / risk / manual path | Complete when read-only sources remain unchanged and every boundary result is cited; HIGH upstream/commercial risk; human before/after and checklist audit |

### T004-031 — Verify Registry, provenance, manual operation and domain neutrality

| Contract field | Plan |
|---|---|
| Purpose / type | Plan integrated current/history, lineage and no-infrastructure checks; `CONTROLLED_VERIFICATION` |
| Requirements / AC | R01–R02, R08–R10, R13–R14, R19, R23, R25; all corresponding AC |
| Design / decisions | C01, C02, C09, C10, C12, C13, C15, C20; D001–D002, D006, D010–D014 |
| Inputs | T004-002–005, T004-010, T004-013–014, T004-019–020, T004-022, T004-025–028 |
| Expected outputs | Registry-query, SOT conflict, provenance-gap, version-impact, manual tabletop and domain-neutrality verification matrices |
| Dependencies | T004-002–005, T004-010, T004-013–014, T004-019–020, T004-022, T004-025–028; blocks T004-032 |
| Boundary / prohibited | `CONTROLLED_VERIFICATION`; no storage/AI/automation implementation, real validation or Human Performance activity |
| Acceptance evidence | Registry answers all required questions; history immutable; missing lineage explicit; no trading/software assumptions; manual path works |
| Completion / risk / manual path | Complete when all queries/scenarios resolve from documents alone; HIGH integration risk; human documentary simulation |

## W7 — Final audit and closure preparation

### T004-032 — Produce final package audit and closure-candidate packet

| Contract field | Plan |
|---|---|
| Purpose / type | Reconcile outputs, validation, traceability, gaps and Founder closure readiness; `AUDIT` |
| Requirements / AC | R01–R25; R01.1–R25.4 |
| Design / decisions | C01–C20; D001–D015 |
| Inputs | T004-001–031 outputs and validation evidence |
| Expected outputs | Package summary, final traceability, independent execution review, remediation register, integrity audit and closure candidate |
| Dependencies | T004-001–031; terminal blocker; Founder closure remains separate |
| Boundary / prohibited | `DOCUMENTARY`; may set only `READY_FOR_FOUNDER_CLOSURE_REVIEW`; cannot self-close, execute missing work or approve itself |
| Acceptance evidence | 25/25 Requirements, 100/100 AC, 20/20 components, 15/15 decisions where applicable, 32/32 Tasks, 0 cycles/orphans/scope violations and all integrity counters |
| Completion / risk / manual path | Complete only after independent evidence-based audit and zero unresolved blockers or explicit block report; HIGH false-closure risk; human inventory/diff/reference review |

## Plan-level execution boundary

T004-001/W0 and T004-002–005/W1 are COMPLETE. T004-006–010/W2 are authorized but not started. T004-011–032 and W3–W7 remain unauthorized. The DAG supports wave-by-wave authorization and fail-closed downstream blocking. Software implementation, external research and real-world validation Tasks: `0 / 0 / 0`.

Approved baseline: v1.0 under `FD-P004-TASKS-001`. Task semantics remain unchanged. Next safe action: `PACKAGE_004_WAVE_2_EXECUTION`.
