# Manual-First Product Factory Operating Procedure

> **DOCUMENTARY PROCEDURE — NOT_A_GOVERNED_INSTANCE**  
> This procedure creates no Candidate, Product, attachment, Registry entry, evidence result, governance decision, lifecycle transition, sharing permission, handoff or commercial action. It implements no software or infrastructure.

## Purpose, scope and authority

Task: `T004-027`. This procedure integrates T004-002–026 so the Founder can operate Package 004 using governed files and templates only. Manual-first means every action remains evidence-backed, reviewable and human-controlled; it does not waive a guard or create new authority.

Final authority is the Founder or an explicitly delegated competent human. AI assistance is optional and `NON_AUTHORITATIVE`, governed by `ai-permission-matrix.md`. Package 003 remains authoritative for Assets. Package 005 remains dormant. Packages 006/007, Persistence, Historical Truth infrastructure, database, API, UI, workflow engine, automation, RAG, MCP and AI Agent Runtime are not dependencies.

## Binding invariants

- Lifecycle is exactly `CANDIDATE → UNDER_REVIEW → READY → APPROVED → ACTIVE → DEPRECATED → RETIRED`; `REJECTED` is a terminal Candidate review outcome, not a state; `NO_PRODUCT_FAST_PATH_IN_V1` applies.
- `READY ≠ APPROVED`; `APPROVED ≠ ACTIVE`; `ACTIVE ≠ PUBLIC`; `ACTIVE ≠ COMMERCIALIZED`; `ACTIVE ≠ REVENUE_GENERATING`.
- Quality ≠ Risk ≠ Readiness; Value ≠ Demand Validation; Demand Validation ≠ transaction; Asset Quality/Value ≠ Product Quality/Value.
- Product SOT ≠ Asset SOT. Current Truth is distinct from immutable documentary Historical Truth. Working/derived copies are non-authoritative.
- Licensing, usage, sharing, distribution, dependency and risk restrictions propagate fail closed.
- Governance decisions use `governance-decision-record-template.md`; no local or competing decision envelope is permitted.

## Roles

| Role | Manual responsibility | Cannot do by role implication |
|---|---|---|
| Founder / delegated Product Authority | Final governed decisions within documented competence/delegation | Override another authority layer or missing evidence |
| Product Owner | Maintain Product/Candidate SOT, coordinate evidence and reviews | Self-approve absent explicit authority |
| Reviewer / domain specialist | Evaluate assigned evidence and disclose gaps/competence | Execute lifecycle or accept unrelated risk |
| Asset Authority (P003) | Own Asset truth and attachment eligibility decisions | Product approval/activation by Asset decision alone |
| Registry maintainer | Reconcile reference views and history manually | Become Product/Asset/evidence authority |
| AI assistant | Allowed analysis/drafting/gap detection under matrix | Decide, approve, execute, own, rewrite or remove restrictions |

## Required manual sequence

At every step: verify exact identity/version/SOT, use the named artifact, cite evidence, preserve restrictions/history, obtain the required human decision, and stop with a named gap on any failed guard.

| Step | Operation | Required inputs | Manual output / decision | Fail-closed gate |
|---|---|---|---|---|
| 1 | Baseline and authority check | Approved Requirements/Design/Task Plan, Architecture Freeze, package states | Dated source/authority checklist | Any stale/contradictory baseline stops affected work |
| 2 | Candidate intake | `product-candidate-template.md` | Provisional Candidate record at CANDIDATE only | Missing identity, owner, problem, consumer, SOT or restrictions is explicit; no Product claim |
| 3 | Candidate review start | Candidate record, common governance envelope | Human decision for CANDIDATE→UNDER_REVIEW | No skipped state or implicit completeness |
| 4 | Composition | `product-composition-record-template.md` | Exact versioned input/reference snapshot | No attachment or embedded upstream authority |
| 5 | Asset eligibility | `p003-attachment-eligibility-reference-contract.md`, P003 decision | Read/reference/consume eligibility result | P004 cannot write, override, recompute, promote or downgrade |
| 6 | Dependencies | `product-dependency-declaration-template.md` | Asset/external/operational/platform dependency entries | Undeclared critical dependency blocks affected gate |
| 7 | Packaging/provenance | packaging manifest and provenance record | Exact delivery-input and lineage references | Packaging cannot broaden rights; missing lineage remains a gap |
| 8 | Product Quality | `product-quality-evaluation-matrix-template.md` | Nine separate evidence-backed results | No composite score or Asset-quality substitution |
| 9 | Product Risk | `product-risk-evaluation-and-acceptance-template.md` | Nine-category evaluation; separate human acceptance if needed | AI cannot accept; HIGH/CRITICAL unresolved risk blocks affected gate |
| 10 | Product Value | `product-value-evidence-record-template.md` | HYPOTHESIZED/EVIDENCED/DEMONSTRATED evidence state | No revenue, demand or lifecycle inference |
| 11 | Demand Validation | `demand-validation-plan-result-template.md` | Falsifiable documentary plan/result | No real activity unless separately authorized; no transaction inference |
| 12 | Readiness | `product-readiness-matrix-template.md` | Eleven-control READY/NOT_READY/REVIEW_REQUIRED decision | Result does not approve or activate |
| 13 | Lifecycle review outcome | lifecycle matrix; terminal outcome template | Human READY transition or REJECTED Candidate outcome | REJECTED is terminal outcome; invalid transition leaves state unchanged |
| 14 | Approval | approval payload + common envelope | Separate human READY→APPROVED record | Approval does not activate/share/commercialize |
| 15 | Activation | activation payload + prior approval | Separate human APPROVED→ACTIVE record | ACTIVE has no Public/commercial/Revenue implication |
| 16 | Version/compatibility | version/compatibility template | Human-reviewed Product version and evidence-based compatibility | Asset/dependency/composition/package/governance versions stay distinct |
| 17 | Registry reconciliation | `manual-product-registry-contract.md` | Updated documentary current views plus immutable history links | Conflicts/duplicates/broken history block update |
| 18 | Sharing | `product-sharing-decision-and-restriction-check.md` | Separate human audience/context permission | Most-restrictive scope; ACTIVE does not imply PUBLIC |
| 19 | Review/freshness | `product-review-and-freshness-record-checklist.md` | Human comparison and follow-up disposition | Trigger/staleness cannot silently change state |
| 20 | Deprecation | deprecation payload + common envelope | Human APPROVED/ACTIVE→DEPRECATED record | Impact, migration/exit and authority required |
| 21 | Retirement | retirement payload + prior deprecation | Human DEPRECATED→RETIRED record | No direct retirement, deletion or reactivation |
| 22 | Product→Revenue boundary | `product-revenue-handoff-dossier.md` | Documentary readiness or governed handoff record | No P005 activation or Revenue operation |

Domain-specific evidence uses `domain-extension-evidence-profile-template.md`. Before the first real cross-domain Candidate, complete a separately authorized `DOMAIN_NEUTRALITY_REVIEW`; the profile cannot fork core governance.

## Manual decision and record protocol

1. Copy the applicable blank template to a separately authorized governed-record path; never convert the template itself into an instance.
2. Verify human authority/delegation and exact subject/version/current state from authoritative sources.
3. Reference, do not duplicate, Asset SOT, evidence authority, dependencies and prior decisions.
4. Complete the common governance envelope and applicable specialized payload. Missing data is `MISSING — <named gap>`.
5. Apply event guards and the most restrictive upstream constraint. Any failure returns for review or fails with state unchanged.
6. Have the competent human decide and timestamp; AI drafts remain non-authoritative.
7. Add an immutable historical record and reconcile the manual Registry current view bidirectionally. Corrections supersede; they never overwrite history.
8. Schedule the next date/event review. A review trigger cannot execute a transition.

## Manual Registry and file controls

- Use one authoritative Product SOT per Product/version and reference it from Registry views.
- Maintain Candidate, Product, composition, evidence and history views defined by `manual-product-registry-contract.md`.
- Label working/derived copies and AI drafts as non-authoritative. Do not treat folder location, file creation or template completeness as governance status.
- Before/after each governed update, manually check identity, version, state, authority, restrictions, history and supersession links.
- No database, event store, API, automation or notification service is necessary. If future tooling is authorized, this manual contract remains the audit/fallback behavior.

## Exception and failure handling

| Failure | Manual response |
|---|---|
| Missing/invalid authority | Stop; record gap; preserve state/current truth |
| Missing/stale/inaccessible evidence | Stop affected gate; schedule human review; do not infer favorable status |
| Restriction conflict | Apply most restrictive scope; escalate to competent authority without weakening upstream truth |
| Invalid lifecycle request | Reject request; record attempted source/target; state unchanged |
| Product/Asset SOT conflict | Stop Registry/current-truth update; reconcile with each authority owner |
| Duplicate identity or silent history rewrite | Reject update; preserve both evidence and conflict record |
| Proposed P005/P006/P007 or infrastructure action | Stop; require separate Package/implementation authorization |
| AI requests prohibited action | Refuse authoritative portion; retain allowed draft/analysis only if useful |

## End-to-end documentary tabletop completion checklist

- [ ] Every R19 operation has a named artifact, role, input, output, decision gate and fail-closed response.
- [ ] Formation through retirement follows the seven-state lifecycle without fast paths.
- [ ] Candidate, composition, eligibility, evidence dimensions, Readiness, Approval, Activation and sharing remain separate.
- [ ] Version, Registry, Current Truth, Historical Truth and SOT relationships reconcile without copied authority.
- [ ] P003 remains CLOSED/read-only; ASSET-1/2/3 remain `VALIDATED / NOT_CANONICAL / NOT_ATTACHABLE` unless P003 separately decides otherwise.
- [ ] Product→Revenue boundary ends at a dossier; P005 remains DORMANT.
- [ ] Human governance and the common decision envelope apply throughout; AI remains optional/non-authoritative.
- [ ] Domain neutrality is preserved and the first real cross-domain Candidate triggers review.
- [ ] Manual operation works using files/templates alone; technology and automation remain replaceable and auditable.
- [ ] This W5 artifact created zero real entities, decisions, transitions, attachments, fixtures, validation activity or commercial operations.

## Record index

| Capability | Governing artifact |
|---|---|
| Candidate/Product/ownership | `product-candidate-template.md`; `product-record-template.md`; `product-ownership-sot-template.md` |
| Governance/lifecycle | `governance-decision-record-template.md`; `lifecycle-transition-matrix-and-guard-checklist.md`; `terminal-candidate-review-outcome-template.md`; `product-approval-and-activation-event-template.md` |
| Composition/eligibility/dependencies | `product-composition-record-template.md`; `p003-attachment-eligibility-reference-contract.md`; `product-dependency-declaration-template.md` |
| Packaging/provenance/version | `product-packaging-manifest-template.md`; `product-provenance-record-template.md`; `product-version-and-compatibility-record-template.md` |
| Quality/Risk/Value/Demand/Readiness | the five separately named T004-011–015 artifacts |
| Registry/sharing/review/end-of-life | `manual-product-registry-contract.md`; T004-021–023 outputs |
| Revenue boundary/AI/domain | T004-024–026 outputs |

## Traceability

| Trace | Approved source |
|---|---|
| Task | `T004-027` |
| Requirements / AC | `R02–R03`, `R05`, `R07`, `R11–R16`, `R19–R25`; `R19.1–R19.4` |
| Design components | `C01–C20` |
| Design Decisions | `P004-D002–P004-D015` |
| Inputs | Completed T004-002–026 documentary artifacts and `manual-first-workflow-design.md` |
