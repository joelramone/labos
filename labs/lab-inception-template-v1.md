# Lab Inception Template v1.1.0

> Domain-neutral template. Replace every `{placeholder}` and preserve epistemic labels.

## Governance metadata

| Field | Value |
|---|---|
| Artifact ID | `LABOS-LAB-INCEPTION-TEMPLATE` |
| Artifact type | `REUSABLE_LAB_INCEPTION_TEMPLATE` |
| Semantic version | `1.1.0` |
| Classification | `PROPOSED_REUSABLE_GOVERNANCE_ARTIFACT` |
| Registration | `NOT_REGISTERED` |
| Operational status | `NON_OPERATIONAL` |
| Execution status | `NON_EXECUTABLE` |
| Activation authority | `NONE` |
| Source template path | `labs/lab-inception-template-v1.md` |
| Governance owner | `LabOS Founder Governance Authority` |
| Effective date | `2026-09-18` |
| Template source-of-truth path | `labs/lab-inception-template-v1.md` |

This is a reusable LabOS governance template. It is not a Lab or Lab instance, Product, Asset, Package, implementation artifact, execution record, or authority to activate anything.

The governance owner governs this reusable template only. It does not own future Lab instances, transfer Founder authority, or delegate authority. The template source-of-truth designation applies only to this reusable artifact; it does not make the template a source of truth for instantiated Labs and does not confer Architecture Baseline `CANONICAL` status, registration, Lab activation, or portfolio registration.

## Fail-closed authority boundary

[Decisión] Reading, referencing, copying, or populating this template does **not** create, register, recognize, activate, resume, prioritize, or execute a Lab. It does not authorize implementation, infrastructure, research, external validation, evidence collection, lifecycle transitions, Product creation or approval, Asset creation or promotion, Package activation, Architecture modification, or RAG, MCP, AI Agents, automation, or canonical persistence.

Absent a separate explicit governance decision granting a specific authority, that authority is `DENIED`.

## Template and instance separation

```text
TEMPLATE != LAB INSTANCE
```

The reusable source template contains structure, governance prompts, and inception requirements only. A Lab-specific instance contains its own identity, owner, domain, governance state, authoritative source of truth, portfolio classification, inception scope, and Founder decisions.

The reusable source template itself must never be populated with Lab-specific state. Populate only a copy at a distinct Lab-specific path.

The following artifact and governance states are distinct and non-equivalent:

```text
POPULATED TEMPLATE DRAFT
!= APPROVED LAB INCEPTION
!= LAB CONTRACT
!= PORTFOLIO REGISTRATION
!= LAB LIFECYCLE STATE
!= EXECUTION AUTHORIZATION
```

None automatically creates, grants, implies, or substitutes for another. Populating or copying the template does not create a Lab. Approved inception does not authorize execution. A Lab Contract does not constitute portfolio registration. Portfolio registration does not authorize execution. A lifecycle state does not implicitly grant unrelated authority. Execution requires the applicable separate explicit authorization. Template reuse grants no operational authority.

## Instantiation and provenance model

```text
COPY TEMPLATE
→ LAB-SPECIFIC PATH
→ RECORD TEMPLATE PROVENANCE
→ LAB-SPECIFIC FOUNDER INCEPTION DECISION
→ SEPARATE EXECUTION AUTHORIZATION WHEN REQUIRED
```

Neither a reference nor a copy alone instantiates or authorizes a Lab. Every future instance must record at minimum:

- source template artifact identity;
- source template path;
- source template version;
- instantiation date; and
- Lab-specific destination path.

This provenance is documentary. It does not create an automated registry or provenance system.

## Founder inception and execution authority

Every future Lab requires its own explicit Founder inception decision defining at minimum:

- Lab identity;
- owner;
- domain;
- initial governance state;
- authoritative source of truth;
- portfolio classification; and
- inception scope.

Template reuse cannot substitute for that decision.

A Lab-specific inception decision does not automatically authorize lifecycle transitions, research execution, external validation, evidence collection, software implementation, infrastructure implementation, Product operations, or Asset operations. Each requires separate explicit authority when applicable.

## Governance separation

The following authorities remain independent and no authority transfers implicitly between them:

- Template Governance;
- Lab Governance;
- Architecture Governance;
- Package Governance;
- Asset Governance;
- Product Governance;
- Implementation Authority; and
- AI / RAG / MCP Authority.

## Versioning and compatibility

- `PATCH`: non-semantic clarification or correction that does not alter required governance behavior.
- `MINOR`: backward-compatible addition to template structure, metadata, or governance requirements.
- `MAJOR`: breaking change to required fields, authority boundaries, instantiation semantics, or compatibility expectations.

Version changes never automatically migrate existing Lab instances. Future template versions do not automatically alter existing Labs. Existing Labs do not automatically inherit later template requirements or authority. Each instance remains associated with its recorded source version unless an explicit review and governance decision authorizes migration. Automatic cross-version mutation is prohibited.

Prior template versions must remain reconstructable through immutable repository history or equivalent governed durable history. Newer versions must not silently overwrite the historical meaning of previous versions. Instantiated Labs remain attributable to the exact template version used, and historical provenance must remain reconstructable.

## Domain neutrality and registration boundary

This template must remain domain-neutral. It must not encode assumptions or governed state from any particular Lab, project, Package, Product, Asset, or domain.

Registration remains `NOT_REGISTERED` and requires the separate sequence:

```text
REMEDIATION ACCEPTANCE
→ REGISTRATION AUTHORIZATION
→ REGISTRATION
```

Remediation alone does not make this template canonical, registered, durable, accepted, or operational.

## Architecture classification

| Control | Result |
|---|---|
| Architecture Freeze | `PRESERVED` |
| Evolution classification | `ORDINARY_GOVERNED_DOCUMENT_EVOLUTION` |
| `MODIFY_BASELINE` | `NO` |
| `EXTENDS_BASELINE` | `NO` |
| `ADR_REQUIRED` | `NO` |

## 1. Lab identity

| Field | Value |
|---|---|
| Lab ID | `{LAB-ID}` |
| Working name | `{working name; not automatically a brand}` |
| Lab state | `{idea|explorando|validando|operando|pausado}` |
| Owner | `{human owner}` |
| Domain | `{independent domain}` |
| Source of truth | `{canonical repository path}` |
| Inception date | `{YYYY-MM-DD}` |

## 2. Founder intent

- [Visión] `{long-term intent}`
- [Decisión] `{why investigate now}`
- Capacity: `{hours/timebox}`

## 3. Problem space

- Target users: `{roles/contexts; do not over-segment without evidence}`
- [Hipótesis] Problem: `{important/frequent problem}`
- Current alternatives: `{known or evidence pending}`
- Consequence: `{observable cost/outcome}`
- Explicit unknowns: `{what must not be assumed}`

## 4. Research

| Field | Value |
|---|---|
| Research ID | `{LAB-SIGLA-RES-NNNN}` |
| Principal Research Question | `{answerable question that enables a decision}` |
| Research types | `{exploratory/market/user/product/technical/comparative/etc.}` |
| Timebox | `{duration}` |
| Completion criteria | `{observable outputs}` |

## 5. Hypotheses

| ID | Hypothesis `[Hipótesis]` | Evidence needed | Status |
|---|---|---|---|
| `{H-001}` | `{claim}` | `{evidence}` | proposed |

## 6. Assumptions

| ID | Assumption `[Hipótesis]` | Impact if wrong | Validation |
|---|---|---|---|
| `{A-001}` | `{assumption}` | `{impact}` | `{method}` |

## 7. Risks and safety

| ID | Risk | Impact | Mitigation/gate |
|---|---|---|---|
| `{R-001}` | `{risk}` | `{impact}` | `{control}` |

- Safety boundary: `{what the Lab/product must not claim or do}`
- Escalation: `{when human/expert review is mandatory}`
- Privacy/data boundary: `{consent, minimization, retention}`

## 8. Evidence

- Evidence hierarchy: `{behavior/payment > observed use > stated preference}`
- Evidence register location: `{path}`
- Required fields: `{source, date, method, observation, limitation, claim}`
- Next evidence collection: `{method; do not collect before approvals}`

## 9. Monetization

| Package 000 field | Hypothesis |
|---|---|
| Segment | `{who might pay}` |
| Delivery format | `{service/product/content/tool/hybrid}` |
| Revenue model | `{one-time/subscription/license/etc.}` |

- [Decisión] Payment validation method: `{offer/deposit/pre-sale/purchase}`
- Stop condition: `{what evidence ends commercial exploration}`

## 10. Product hypotheses

| ID | Product hypothesis `[Hipótesis]` | Competing alternative | Evidence gate |
|---|---|---|---|
| `{PH-001}` | `{solution}` | `{manual/non-software/other}` | `{behavior/payment}` |

[Decisión] Do not assume software or an app is required.

## 11. Assets

| Candidate ID | Name | Type hypothesis | Reuse hypothesis | Status |
|---|---|---|---|---|
| `{AC-001}` | `{name}` | `{one of 7 canonical types or pending}` | `{second context}` | CANDIDATE |

[Decisión] Asset Candidates are not canonical until Package 003 governance approves them.

## 12. Potential Capabilities

| Working capability | Reuse contexts | State | Activation evidence |
|---|---|---|---|
| `{name}` | `{3+ consumers/contexts}` | FUTURE/DORMANT/HYPOTHESIS | `{canonical trigger}` |

## 13. LabOS integration

- Package 000: `{state, portfolio, monetization}`
- Package 001: `{research lifecycle}`
- Package 001A: `{identity, autonomy, contract/integration}`
- Package 002: `{knowledge and provenance}`
- Package 003: `{asset candidate dependency}`
- Product Factory/future: `{product boundary only}`

## 14. Boundaries

- In scope: `{scope}`
- Out of scope: `{non-goals}`
- Existing projects that must not be modified: `{list}`
- Autonomy statement: `{how the Lab operates independently}`

## 15. Validation sequence

`Idea → Intake → Problem Space → Research → Knowledge → Asset Candidates → Product Hypotheses → Commercial Validation → Product Decision`

Only when evidence supports it: `→ Software`.

## 16. Next validation gate

| Gate | Required evidence | Founder decision |
|---|---|---|
| `{next gate}` | `{observable evidence}` | `{approve/refine/pause/stop}` |
