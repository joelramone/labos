# Product Risk Evaluation and Acceptance Template

> **TEMPLATE — NOT_A_GOVERNED_INSTANCE**  
> Blank documentary structure. It records no actual risk acceptance, Product decision, Asset decision or lifecycle transition.

## Purpose and authority

Evaluate aggregate Product risk qualitatively while preserving upstream authority and restrictions. Only the Founder or explicitly delegated human competent for the risk may accept or escalate a disposition. AI and automation cannot accept risk.

## Subject identity

| Field | Entry |
|---|---|
| Product/Product Candidate reference | `<REQUIRED>` |
| Exact Product version | `<VALUE or NOT_APPLICABLE>` |
| Product SOT | `<REQUIRED>` |
| Composition and dependency references | `<REQUIRED exact versions>` |
| Risk evaluation ID/version | `<REQUIRED>` |
| Gate/context evaluated | `<REQUIRED>` |
| Truth classification | `<CURRENT_TRUTH / HISTORICAL_TRUTH>` |
| Evaluation timestamp | `<ISO 8601 with offset>` |
| Supersedes | `<REFERENCE or NONE>` |

## Nine-category risk matrix

Likelihood, impact, mitigation, residual status and blocking decision are qualitative and evidence-backed. No new lifecycle-like enum is established.

| # | Category | Source/evidence | Upstream restriction | Likelihood | Impact | Mitigation | Residual status | Blocking decision/rationale | Competent authority |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Financial | `<REFERENCE or MISSING>` | `<VALUE>` | `<DESCRIPTIVE>` | `<DESCRIPTIVE>` | `<VALUE>` | `<DESCRIPTIVE>` | `<VALUE>` | `<REFERENCE>` |
| 2 | Legal/licensing | `<REFERENCE or MISSING>` | `<VALUE>` | `<DESCRIPTIVE>` | `<DESCRIPTIVE>` | `<VALUE>` | `<DESCRIPTIVE>` | `<VALUE>` | `<REFERENCE>` |
| 3 | Operational | `<REFERENCE or MISSING>` | `<VALUE>` | `<DESCRIPTIVE>` | `<DESCRIPTIVE>` | `<VALUE>` | `<DESCRIPTIVE>` | `<VALUE>` | `<REFERENCE>` |
| 4 | Technical | `<REFERENCE or MISSING>` | `<VALUE>` | `<DESCRIPTIVE>` | `<DESCRIPTIVE>` | `<VALUE>` | `<DESCRIPTIVE>` | `<VALUE>` | `<REFERENCE>` |
| 5 | Evidence | `<REFERENCE or MISSING>` | `<VALUE>` | `<DESCRIPTIVE>` | `<DESCRIPTIVE>` | `<VALUE>` | `<DESCRIPTIVE>` | `<VALUE>` | `<REFERENCE>` |
| 6 | User-impact | `<REFERENCE or MISSING>` | `<VALUE>` | `<DESCRIPTIVE>` | `<DESCRIPTIVE>` | `<VALUE>` | `<DESCRIPTIVE>` | `<VALUE>` | `<REFERENCE>` |
| 7 | Misuse | `<REFERENCE or MISSING>` | `<VALUE>` | `<DESCRIPTIVE>` | `<DESCRIPTIVE>` | `<VALUE>` | `<DESCRIPTIVE>` | `<VALUE>` | `<REFERENCE>` |
| 8 | Dependency | `<REFERENCE or MISSING>` | `<VALUE>` | `<DESCRIPTIVE>` | `<DESCRIPTIVE>` | `<VALUE>` | `<DESCRIPTIVE>` | `<VALUE>` | `<REFERENCE>` |
| 9 | Reputational | `<REFERENCE or MISSING>` | `<VALUE>` | `<DESCRIPTIVE>` | `<DESCRIPTIVE>` | `<VALUE>` | `<DESCRIPTIVE>` | `<VALUE>` | `<REFERENCE>` |

## Human acceptance/escalation payload

Use the common envelope in `governance-decision-record-template.md`; this section supplies its risk-specific payload and does not compete with it.

| Field | Entry |
|---|---|
| Governance decision record | `<REQUIRED for actual disposition>` |
| Unresolved HIGH/CRITICAL risks | `<LIST or NONE>` |
| Affected gate(s) blocked | `<approval / sharing / activation / other>` |
| Acceptance or escalation scope | `<REQUIRED>` |
| Competent human authority and basis | `<REQUIRED>` |
| Rationale/evidence | `<REQUIRED>` |
| Expiry/review trigger | `<REQUIRED>` |
| Upstream restrictions preserved/elevated | `<YES; NO fails closed>` |

Product status is not financial, legal or safety assurance. Unresolved HIGH/CRITICAL risk blocks the affected gate. Conflicting or missing authority fails closed and leaves state unchanged.

## Validation checklist

- [ ] All nine categories are present with likelihood, impact, mitigation, residual status and blocking decision.
- [ ] Licensing, usage, sharing, distribution, dependency and risk restrictions are preserved or elevated.
- [ ] Only competent human authority can accept or escalate risk.
- [ ] Status and narrative do not substitute for evidence.
- [ ] No automated acceptance, lifecycle change or upstream Asset mutation occurs.
- [ ] Current/historical evidence and supersession are preserved.

## Traceability

| Trace type | Approved source |
|---|---|
| Task | `T004-012` |
| Requirements / acceptance criteria | `R06`, `R12`; `R06.1–R06.4`, `R12.1–R12.4` |
| Design components | `C08`, `C19` |
| Design Decisions | `P004-D007`, `P004-D008`, `P004-D012` |
| Inputs | `governance-decision-record-template.md`, composition and dependency records |
