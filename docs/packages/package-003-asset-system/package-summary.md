# Package 003 — Asset System Summary

## Objective and scope

Package 003 supplies a technology-independent governance system for recognizing, qualifying, promoting, maintaining, sharing and retiring reusable Assets. It extends the canonical definition of Asset without redefining Package 000, ADR-0001 or ADR-0002.

Package 003 does not implement software, a registry service, Product Factory, Capability activation or changes to any Lab.

## Operating model

| Concern | Summary | Canonical document |
|---|---|---|
| Asset boundary | File, Artifact, Knowledge Object, Candidate, Canonical Asset, Capability and Product remain distinct | [Boundaries](./asset-definition-and-boundaries.md) |
| Taxonomy | Seven ADR-0002 types; five LabOS-Shared and two Lab-Private defaults | [Taxonomy](./asset-taxonomy.md) |
| Lifecycle | CANDIDATE, UNDER_REVIEW, VALIDATED, CANONICAL, DEPRECATED, ARCHIVED, REJECTED | [Lifecycle](./asset-lifecycle.md) |
| Qualification | Five mandatory dimensions; projected and demonstrated reuse separated | [Qualification](./asset-qualification-framework.md) |
| Promotion | Evaluation plus explicit Founder decision; no automatic promotion | [Promotion](./asset-promotion-process.md) |
| Ownership | One accountable human owner; SOLO roles may be accumulated but remain distinct | [Ownership](./asset-ownership.md) |
| Source of truth | One canonical source per Asset version; provenance references Package 002 | [Source of truth](./asset-source-of-truth.md) |
| Versioning | Proportional evolution; same lineage distinguished from derived, fork and replacement | [Versioning](./asset-versioning.md) |
| Quality | Effective exposure plus risk override; Fast Path retains all five dimensions | [Quality gates](./asset-quality-gates.md) |
| Sharing/reuse | Reference-based sharing; scope remains independent from consumption | [Sharing](./asset-sharing-and-reuse.md) |
| Value/metrics | Evidence-linked value without composite vanity score; metrics drive decisions | [Value](./asset-value-model.md), [metrics](./asset-metrics.md) |
| Registry | Conceptual metadata contract: 8 Tier 1 + 8 additional Tier 2 | [Registry contract](./asset-registry-contract.md) |
| Governance/risk | Explicit human authority; proportional risk can elevate gates | [Governance](./asset-governance.md), [risk](./asset-risk-model.md) |
| Retirement | Controlled deprecation/archive with consumers, migration and history preserved | [Deprecation](./asset-deprecation-and-archive.md) |

## Handoff boundaries

- [Knowledge → Asset](./knowledge-to-asset-integration.md): Package 002 remains authority over Knowledge Objects; Package 003 starts at Asset Candidate intake. Knowledge remains after handoff.
- [Asset → Product](./asset-to-product-handoff.md): Package 003 ends at readiness and dependency declaration. Package 004 remains unauthorized.

## Operational instruments

The workflow is supported by five distinct templates:

1. [Candidate intake](./asset-candidate-template.md) — exactly eight required Tier 1 fields and a 3–5 minute low-risk target.
2. [Evaluation](./asset-evaluation-template.md) — qualification, evidence, reuse, risk and recommendation.
3. [Promotion decision](./asset-promotion-decision-template.md) — eight additional Tier 2 fields and explicit authority.
4. [Review](./asset-review-template.md) — scheduled and event-triggered maintenance.
5. [Deprecation](./asset-deprecation-template.md) — consumers, Product dependencies, migration, archive and history.

## Architecture and validation

- [Architecture diagrams](./asset-architecture-diagrams.md) represent lifecycle, orthogonal axes, source, sharing, versioning and both handoffs without adding architecture.
- [Reference Lab assessment](./crypto-scalping-core-asset-candidate-assessment.md) evaluated five Crypto Scalping Core candidates read-only: five NEEDS_REMEDIATION, zero promoted.
- Practical Reference Lab taxonomy coverage is 2/7: Herramienta and Template. This is a validation limitation, not an architecture defect.
- [Wave reviews](./package-003-wave-status.md) preserve validation evidence for W0–W5; final W6 evidence is produced separately.

## Known limitations and future dependencies

- Practical evidence does not yet cover Dataset, Framework, Playbook, Documento or Componente.
- Manual evidence/reference discovery creates moderate SOLO friction.
- Optional structured locators could support future AI assistance without expanding Tier 1/Tier 2; AI remains non-authoritative.
- Package 004 may later consume the Asset→Product handoff but is not started or authorized here.

Open issues, if any, are authoritative only in [the unresolved remediation register](./package-003-unresolved-remediation-register.md). Package status and closure authority remain in [README](./README.md).
