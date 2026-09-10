# Package 004 — Product Factory Requirements

## Document control

| Field | Value |
|---|---|
| Version | 1.0 |
| Date | 2026-09-03 |
| Status | `APPROVED` |
| Package state | `AUTHORIZED_FOR_DESIGN` |
| Authorization | `FD-P004-ACTIVATION-001` |
| Founder approval | `FD-P004-REQ-001` |
| Scope | Normative requirements only |
| Design / Tasks / Implementation | `AUTHORIZED / NOT_AUTHORIZED / NOT_AUTHORIZED` |

Normative terms `SHALL`, `SHALL NOT`, `MUST`, `MUST NOT` and `MAY` are binding within these Requirements. “System” means the technology-neutral Product Factory governance system and may be operated manually.

## AUTHORITATIVE_SOURCE_MAP

| Code | Authority | Sources | Contract consumed |
|---|---|---|---|
| ARCH | Architecture | Architecture Baseline v1.0, Freeze decision `FD-FREEZE-001`, change control, approved roadmap and post-P003 reconciliation | Value pipeline, package identity, invariants, proportional/manual governance, freeze/change control |
| P000 | Package 000 | Foundation README; company, business and portfolio models | Asset-first model, target problem/value discipline, human SOLO governance, demand before investment |
| P001 | Package 001 | Research lifecycle, evidence framework, research-to-product hypothesis, quality gates | Evidence classes, falsifiability, demand-validation discipline and research safety |
| P001A | Package 001A | Lab integration framework/contract and closure records | Lab boundary, originating context, Reference Lab and provenance |
| P002 | Package 002 | Knowledge lifecycle, provenance, source of truth and Knowledge→Asset handoff | Knowledge authority, one SOT, references and traceable handoff |
| P002A | Package 002A | Baseline, invariants, roadmap and change control | Package sequence, immutable closed packages and compatible extension rules |
| P003 | Package 003 | Asset definition/taxonomy/lifecycle/quality/risk/value/SOT/ownership/governance/versioning/promotion and Asset→Product handoff | Asset authority; CANONICAL attachment eligibility; restrictions and dependency declaration |
| FD004 | Founder decision | `FD-P004-ACTIVATION-001` plus readiness/blocker/trigger records | Requirements-only authority and mandatory activation conditions |
| DER | Derived | Combination of the above, explained in traceability matrix | Product-specific governance needed to make the Products stage operable without authority leakage |

No source authorizes real Product creation, attachment, commercialization, Design, Tasks or implementation in this document.

## Requirements

### P004-R01 — Product identity and distinction

The Product Factory SHALL govern Product as a distinct entity with `product_id`, name, purpose, target consumer, problem, value proposition, composition, originating context, human owner, evidence, dependencies, restrictions, source of truth, lifecycle and version; it SHALL distinguish Product from Idea, Research, Knowledge, Asset, Product Candidate, Revenue, Capability and Lab. `[ARCH, P000, P002, P003, DER]`

Acceptance criteria:

1. **R01.1** WHERE a Product record is inspected, all minimum identity elements SHALL be present or individually marked missing. `[document inspection]`
2. **R01.2** IF an object is only an Asset or sellability hypothesis, THEN the system SHALL NOT classify it as a Product. `[controlled scenario]`
3. **R01.3** WHEN two Product records claim the same identity, the system SHALL flag duplication before approval. `[governance record]`
4. **R01.4** WHERE entity definitions are reviewed, none SHALL redefine upstream Research, Knowledge, Asset, Revenue, Capability or Lab. `[document inspection]`

### P004-R02 — Product Candidate

The Product Factory SHALL use Product Candidate as a distinct governed proposal with provisional identity, problem, target consumer, value proposition hypothesis, owner, context, proposed composition, evidence, restrictions, source of truth and lifecycle; Candidate status SHALL NOT imply approval, market validation, commercialization or Revenue readiness. `[ARCH, P000, FD004, DER]`

Acceptance criteria:

1. **R02.1** WHEN a proposal lacks any entry field, the system SHALL return the named gaps and SHALL NOT register a complete Candidate. `[controlled scenario]`
2. **R02.2** WHEN entry fields are complete, the system MAY register a Candidate only in `CANDIDATE`. `[governance record]`
3. **R02.3** IF a Candidate is cited externally, THEN its unapproved status and restrictions SHALL remain visible. `[document inspection]`
4. **R02.4** Candidate creation SHALL create zero Asset lifecycle, Product approval or commercialization effects. `[governance audit]`

### P004-R03 — Product lifecycle

The Product Factory SHALL implement exactly these v1 lifecycle states: `CANDIDATE`, `UNDER_REVIEW`, `READY`, `APPROVED`, `ACTIVE`, `DEPRECATED`, `RETIRED`; each state SHALL have entry, permitted/prohibited actions, exit, human authority and evidence rules, and governance-significant transitions MUST NOT be automatic. `[ARCH, P003, FD004, DER]`

Acceptance criteria:

1. **R03.1** A state-table audit SHALL find exactly seven states and no orthogonal attribute used as a state. `[document inspection]`
2. **R03.2** WHEN a transition is requested, the system SHALL verify its source state, target state, evidence and human authority. `[future implementation test]`
3. **R03.3** IF a transition is not listed or its guard fails, THEN the state SHALL remain unchanged with named failures. `[controlled scenario]`
4. **R03.4** A rejected review SHALL be preserved as a terminal outcome record, not silently deleted or added as an eighth state. `[governance record]`

### P004-R04 — Asset composition

The Product Factory SHALL support proposed one-to-one, many-to-one and shared Asset composition plus declared external dependencies while preserving every Asset as a referenced independent entity. `[P003, DER]`

Acceptance criteria:

1. **R04.1** A composition SHALL list each Asset ID, version expectation and contribution type. `[document inspection]`
2. **R04.2** Multiple Assets MAY compose one Candidate without merging their identities or ownership. `[controlled scenario]`
3. **R04.3** A shared Asset SHALL retain one upstream SOT and MAY be referenced by multiple Products. `[governance record]`
4. **R04.4** External dependencies SHALL be separately identified from Asset dependencies. `[document inspection]`

### P004-R05 — Attachment eligibility

The Product Factory MUST consume Package 003 attachment eligibility: `CANONICAL` is mandatory and the full stability, ownership, relevance, Revenue_Thesis-presence, maintainability, licensing/sensitivity, version and dependency gates MUST pass before effective attachment; a `VALIDATED / NOT_CANONICAL` Asset MAY be referenced for Candidate evaluation but MUST NOT be attached. `[P003, FD004]`

Acceptance criteria:

1. **R05.1** IF an Asset is VALIDATED but not CANONICAL, THEN composition SHALL label it `REFERENCE_ONLY / NOT_ATTACHABLE`. `[controlled scenario]`
2. **R05.2** IF an Asset is CANONICAL but any P003 handoff criterion fails, THEN attachment SHALL be rejected with named gaps. `[controlled scenario]`
3. **R05.3** WHEN P003 records complete eligibility, P004 MAY evaluate Product fit but SHALL NOT override the Asset decision. `[governance record]`
4. **R05.4** Product approval SHALL NOT cure or bypass failed Asset eligibility. `[governance audit]`

### P004-R06 — Composition integrity

The Product Factory SHALL preserve Asset provenance, licensing, restrictions, ownership, version, SOT and risk in every composition; aggregation MUST NOT reduce the most restrictive applicable upstream constraint without explicit competent human authority. `[P003, FD004, DER]`

Acceptance criteria:

1. **R06.1** A composition review SHALL map every upstream restriction to its Product effect or justified non-applicability. `[document inspection]`
2. **R06.2** IF two inputs have different sharing limits, THEN the proposed Product scope SHALL respect the most restrictive applicable limit. `[controlled scenario]`
3. **R06.3** Copying content into a package SHALL NOT replace the Asset SOT or ownership record. `[governance audit]`
4. **R06.4** An unresolved licensing or risk conflict SHALL block the affected Product gate, not mutate the Asset. `[controlled scenario]`

### P004-R07 — Ownership and authority

Every Product Candidate and Product SHALL have one explicit human owner; Product approval authority SHALL be the Founder by default or an explicitly delegated human, and creator, owner, reviewer, Product Authority, Asset Owner and consumer roles SHALL remain distinguishable. `[P000, P003, FD004, DER]`

Acceptance criteria:

1. **R07.1** A Candidate/Product without a named human owner SHALL fail its applicable gate. `[controlled scenario]`
2. **R07.2** Ownership transfer SHALL record outgoing owner, incoming human owner, acceptance, date and affected identity. `[governance record]`
3. **R07.3** Product ownership SHALL NOT transfer Asset ownership. `[governance audit]`
4. **R07.4** AI or a software system SHALL NOT be accepted as owner or final Product Authority. `[controlled scenario]`

### P004-R08 — Product source of truth

Each Product Candidate and governed Product version SHALL have exactly one identifiable Product SOT; references and managed mirrors MAY exist but SHALL NOT become competing authority, and Product SOT SHALL remain distinct from each Asset SOT. `[ARCH, P002, P003, DER]`

Acceptance criteria:

1. **R08.1** A registry audit SHALL resolve exactly one current SOT for each governed record/version. `[document inspection]`
2. **R08.2** IF two locations claim authority, THEN approval SHALL stop pending reconciliation. `[controlled scenario]`
3. **R08.3** A Product SOT SHALL reference Asset SOTs rather than silently copying their current state. `[document inspection]`
4. **R08.4** Technology choice SHALL NOT be required to satisfy the conceptual SOT contract. `[document inspection]`

### P004-R09 — Product provenance

The Product Factory SHALL preserve traceability `Product → Product Candidate → Assets → Knowledge → Research/Evidence` where applicable; absent historical links SHALL be explicit gaps and MUST NOT be fabricated retroactively. `[P001, P002, P003, DER]`

Acceptance criteria:

1. **R09.1** Every Product SHALL reference its originating Candidate and composition evidence. `[document inspection]`
2. **R09.2** Every attached Asset SHALL retain its P003 provenance reference. `[governance audit]`
3. **R09.3** IF no formal Knowledge/Research link exists, THEN the record SHALL state the accepted upstream provenance form and reason. `[document inspection]`
4. **R09.4** Missing provenance SHALL produce a gap/risk decision, never invented evidence. `[controlled scenario]`

### P004-R10 — Product versioning

Product versions SHALL use `MAJOR.MINOR.PATCH`; incompatible consumer/problem/value/composition/delivery changes SHALL be MAJOR, compatible extensions MINOR and compatible corrections PATCH; a fundamentally different offering SHALL receive a new Product identity. `[ARCH, P003, DER]`

Acceptance criteria:

1. **R10.1** Every governed Product version SHALL record version, effective date and change rationale. `[document inspection]`
2. **R10.2** WHEN an Asset version changes, the system SHALL perform compatibility/readiness impact review before relying on it. `[governance record]`
3. **R10.3** An Asset version change SHALL NOT automatically change Product version or lifecycle. `[controlled scenario]`
4. **R10.4** A change classified MAJOR/PATCH SHALL be demonstrably consistent with the definitions above or be rejected. `[document inspection]`

### P004-R11 — Product quality

Product quality SHALL be evaluated independently of Asset quality across composition correctness, completeness, usability, reproducibility where relevant, dependency integrity, documentation, consumer suitability, failure modes and operational readiness. `[P001, P003, DER]`

Acceptance criteria:

1. **R11.1** A quality review SHALL evaluate all nine dimensions as PASS, PARTIAL, FAIL or NOT_APPLICABLE with evidence. `[document inspection]`
2. **R11.2** Strong Asset quality SHALL NOT substitute for a failed Product-level mandatory control. `[controlled scenario]`
3. **R11.3** PARTIAL controls SHALL identify whether they block the requested Product gate and preserve restrictions. `[governance record]`
4. **R11.4** Product approval SHALL require all mandatory applicable quality controls to pass. `[governance audit]`

### P004-R12 — Product risk

Every Candidate/Product gate SHALL evaluate aggregated financial, legal/licensing, operational, technical, evidence, user-impact, misuse, dependency and reputational risk qualitatively; composition SHALL NOT lower upstream risk without evidence and competent human authority. `[P001, P003, FD004, DER]`

Acceptance criteria:

1. **R12.1** A risk record SHALL include each category, likelihood, impact, mitigation, residual status and blocking decision. `[document inspection]`
2. **R12.2** IF an upstream restriction applies, THEN Product risk SHALL preserve or elevate it until resolved. `[controlled scenario]`
3. **R12.3** HIGH/CRITICAL unresolved risk SHALL block the affected approval, sharing or activation gate. `[governance record]`
4. **R12.4** Product status SHALL NOT be cited as financial, legal or safety assurance beyond recorded evidence. `[governance audit]`

### P004-R13 — Product value

Product value SHALL be assessed separately from Asset value as `HYPOTHESIZED`, `EVIDENCED` or `DEMONSTRATED`, tied to a target consumer/problem/outcome, and SHALL NOT be upgraded without the evidence defined for that class. `[P000, P003, DER]`

Acceptance criteria:

1. **R13.1** HYPOTHESIZED SHALL require an identified consumer, problem and value proposition. `[document inspection]`
2. **R13.2** EVIDENCED SHALL require dated non-transactional demand evidence from the target context. `[governance record]`
3. **R13.3** DEMONSTRATED SHALL require documented real use and attributable user outcome; projected Asset value alone SHALL fail. `[controlled scenario]`
4. **R13.4** Value status SHALL NOT automatically change Product lifecycle or authorize commercialization. `[governance audit]`

### P004-R14 — Demand validation

Product validation SHALL capture falsifiable evidence that a real problem exists, a target user is identifiable and the proposed Product addresses that problem; it SHALL distinguish product/demand evidence from revenue or transaction validation. `[P000, P001, ARCH, DER]`

Acceptance criteria:

1. **R14.1** A demand plan SHALL state hypothesis, target segment, method, observable signal, success/failure criterion, timeframe and evidence source. `[document inspection]`
2. **R14.2** Evidence SHALL record date, context, participant/source, result, limitations and privacy/sensitivity handling. `[governance record]`
3. **R14.3** IF evidence fails the criterion, THEN the system SHALL record failed/inconclusive validation rather than approval. `[controlled scenario]`
4. **R14.4** A sale, price or revenue target MAY be referenced as a future hypothesis but SHALL NOT be executed or counted as Product validation by P004. `[governance audit]`

### P004-R15 — Product readiness

Readiness SHALL be a governed decision based on composition, evidence, quality, risk, provenance, ownership, dependencies, restrictions, target consumer, demand evidence and documentation; it SHALL NOT be a vague composite score or commercialization authorization. `[P001, P003, FD004, DER]`

Acceptance criteria:

1. **R15.1** A readiness matrix SHALL report every listed control with evidence and blocking status. `[document inspection]`
2. **R15.2** A mandatory FAIL or insufficient-evidence control SHALL prevent transition to READY. `[controlled scenario]`
3. **R15.3** Readiness approval SHALL identify human decisor, date, Product/Candidate, rationale and restrictions. `[governance record]`
4. **R15.4** READY SHALL NOT imply APPROVED, ACTIVE, Public, commercial or revenue-generating. `[governance audit]`

### P004-R16 — Product approval and activation

Only the Founder or explicitly delegated human Product Authority MAY approve or activate a Product; automatic approval and automatic lifecycle promotion SHALL be prohibited, and APPROVED SHALL remain distinct from ACTIVE. `[P000, P003, FD004, DER]`

Acceptance criteria:

1. **R16.1** An approval record SHALL identify authority, date, Product/version, evidence basis, scope, restrictions and rationale. `[document inspection]`
2. **R16.2** AI recommendation without valid human approval SHALL leave lifecycle unchanged. `[controlled scenario]`
3. **R16.3** APPROVED → ACTIVE SHALL require a separate activation/release decision with delivery and operational scope. `[governance record]`
4. **R16.4** Invalid or missing approval SHALL fail closed and name the missing fields. `[future implementation test]`

### P004-R17 — Product packaging

Every Product package SHALL provide a coherent, technology-neutral manifest of included eligible Assets, supporting material, usage instructions, restrictions, dependencies, provenance, version, intended consumer and delivery assumptions. `[P003, DER]`

Acceptance criteria:

1. **R17.1** A packaging manifest SHALL enumerate all required elements or named gaps. `[document inspection]`
2. **R17.2** Packaging SHALL reference exact Asset versions and SOTs. `[governance audit]`
3. **R17.3** Restrictions and permitted-use assumptions SHALL be visible at the point of delivery. `[controlled scenario]`
4. **R17.4** Packaging requirements SHALL NOT prescribe archive, installer, cloud, repository or delivery technology. `[document inspection]`

### P004-R18 — Product dependencies

Each Candidate/Product SHALL declare Asset, external, operational and future-platform dependencies with identity, version/compatibility, purpose, criticality, owner/provider, restrictions, failure impact and fallback/exit expectation. `[P003, ARCH, DER]`

Acceptance criteria:

1. **R18.1** A dependency register SHALL distinguish the four dependency classes. `[document inspection]`
2. **R18.2** An undeclared dependency discovered during review SHALL produce a gap and impact assessment. `[controlled scenario]`
3. **R18.3** RAG, MCP, agents, Automation or Persistence SHALL NOT be implicit dependencies. `[governance audit]`
4. **R18.4** A critical dependency change SHALL trigger compatibility/readiness review before continued ACTIVE use. `[governance record]`

### P004-R19 — Manual-first operation

Candidate registration, composition declaration, evidence/risk/quality review, readiness/approval recording, packaging/restriction review, sharing/retirement decisions and Revenue handoff preparation SHALL remain possible manually under human governance; Package 006/007 or future infrastructure SHALL NOT be required. `[ARCH, FD004]`

Acceptance criteria:

1. **R19.1** Each named operation SHALL have a document/governance-record verification path. `[document inspection]`
2. **R19.2** Absence of automation, AI, database or external service SHALL NOT prevent a conforming process. `[controlled scenario]`
3. **R19.3** Manual decisions SHALL preserve authority, evidence and history requirements. `[governance audit]`
4. **R19.4** Any future automation SHALL remain replaceable by or auditable against the manual contract. `[future implementation test]`

### P004-R20 — AI authority boundary

AI MAY inspect, summarize, compare, detect missing/stale evidence, draft proposals and recommend; AI MUST NOT own or approve Products, override restrictions, promote Asset/Product lifecycle, approve commercialization, erase provenance or silently modify canonical records. `[P002, P003, FD004]`

Acceptance criteria:

1. **R20.1** An AI-produced proposal SHALL be marked non-authoritative until human decision. `[controlled scenario]`
2. **R20.2** Attempts by AI to execute prohibited authority SHALL fail closed and preserve state. `[future implementation test]`
3. **R20.3** AI assistance SHALL identify source references and material uncertainty. `[document inspection]`
4. **R20.4** No requirement SHALL make AI, RAG or MCP mandatory for Product Factory conformance. `[requirements audit]`

### P004-R21 — Product→Revenue handoff

Package 004 SHALL produce a Product→Revenue handoff record containing approved Product identity/version/state, owner/SOT, consumer/problem/value proposition, demand status, composition/dependencies, delivery/sharing assumptions, restrictions, risk/readiness evidence and any monetization-hypothesis reference; it MUST stop before pricing execution, payment, transaction, accounting or revenue optimization. `[ARCH, P000, FD004, DER]`

Acceptance criteria:

1. **R21.1** A handoff checklist SHALL include every specified field or named gap. `[document inspection]`
2. **R21.2** Missing Product approval or incompatible licensing SHALL block the handoff. `[controlled scenario]`
3. **R21.3** Handoff creation SHALL NOT activate Package 005 or record revenue. `[governance audit]`
4. **R21.4** Price execution, payment, transaction, accounting and revenue optimization SHALL be absent from P004 operations. `[boundary review]`

### P004-R22 — Commercialization and sharing

Product lifecycle, readiness, approval and activation SHALL remain independent from commercialization and sharing scope; sharing SHALL respect the most restrictive applicable Asset/external restriction unless explicit competent human authority and required evidence permit otherwise. `[P003, FD004, DER]`

Acceptance criteria:

1. **R22.1** Product approved SHALL NOT equal commercialization authorized. `[governance audit]`
2. **R22.2** Demand validated SHALL NOT equal transaction or revenue validated. `[governance audit]`
3. **R22.3** A Public/external sharing request SHALL receive a separate licensing, sensitivity, risk and human-authority review. `[controlled scenario]`
4. **R22.4** A Product containing restricted inputs SHALL NOT broaden their distribution rights by packaging. `[controlled scenario]`

### P004-R23 — Review and freshness

The Product Factory SHALL trigger review on material Asset/product/dependency/version/schema change, licensing/risk change, new or failed-use evidence, demand/consumer/context change, source failure, first external exposure and scheduled freshness date; triggers SHALL NOT cause automatic lifecycle change. `[P001, P002, P003, DER]`

Acceptance criteria:

1. **R23.1** Every Candidate/Product SHALL record a next review date or evidence-based event trigger. `[document inspection]`
2. **R23.2** WHEN a trigger fires, the system SHALL flag review required while preserving current state. `[controlled scenario]`
3. **R23.3** Review SHALL compare current evidence/dependencies/restrictions with the prior decision. `[governance record]`
4. **R23.4** Source inaccessibility or stale evidence SHALL be recorded, not silently replaced. `[controlled scenario]`

### P004-R24 — Deprecation and retirement

Products SHALL support governed deprecation and terminal retirement when superseded, dependencies invalidate composition, licensing/safety changes, evidence becomes stale, consumer need disappears or replacement occurs; historical truth and consumer/dependency impact MUST be preserved. `[ARCH, P002, P003, DER]`

Acceptance criteria:

1. **R24.1** A deprecation decision SHALL identify reason, authority, date, affected consumers/dependencies, successor and migration/exit plan. `[document inspection]`
2. **R24.2** ACTIVE/APPROVED Product SHALL NOT become RETIRED without a DEPRECATED historical entry. `[controlled scenario]`
3. **R24.3** Retirement SHALL require resolved active-consumer obligations or explicit documented exceptions. `[governance record]`
4. **R24.4** Retired records and prior evidence SHALL remain immutable; renewed demand creates a governed new Candidate/version. `[governance audit]`

### P004-R25 — Product Registry contract and history

The Product Factory SHALL define a technology-neutral Product Registry that can answer what Candidates/Products exist, state, owner, composition and versions, restrictions, dependencies, evidence, readiness, SOT and review timing; every governed change SHALL retain timestamp, prior/new value, actor/authority and reason. `[ARCH, P002, P003, DER]`

Acceptance criteria:

1. **R25.1** A registry completeness check SHALL answer every listed question for each record or explicitly report missing data. `[document inspection]`
2. **R25.2** Registry storage SHALL remain implementation-neutral and MAY be documentary. `[requirements audit]`
3. **R25.3** Current truth SHALL be distinguishable from immutable historical decisions and prior states. `[governance audit]`
4. **R25.4** Duplicate IDs, unauthorized state changes or silent history rewrites SHALL be rejected and reported. `[future implementation test]`

## Package state and explicit non-scope

Package 004 is `AUTHORIZED_FOR_DESIGN` under `FD-P004-DESIGN-AUTH-001`. Requirements v1.0 remains the approved normative baseline under `FD-P004-REQ-001`; Design authorization creates no Tasks, implementation, Product Candidate, Product, attachment, Asset transition, commercialization or downstream Package activation.

`NO_PRODUCT_FAST_PATH_IN_V1` applies. The next safe action is `PACKAGE_004_DESIGN`; no later phase is authorized.
