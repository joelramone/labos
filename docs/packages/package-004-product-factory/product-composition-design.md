# Package 004 — Product Composition Design

## Composition model

A composition snapshot belongs to one Candidate/Product version and references `1..N` governed inputs. It supports one or many Asset references, shared Assets, and `0..N` external dependencies. At least one coherent input is required, but no rule forces software, multiple Assets or any particular domain.

Each Asset reference carries Asset ID, version expectation, contribution type, P003 SOT reference, consumed eligibility decision, applicable restrictions and dependency relationship. These are references/snapshots for decision reproducibility, not P004-owned Asset truth.

## Attachment Eligibility Adapter

```mermaid
sequenceDiagram
  participant CM as P004 Composition Manager
  participant EA as Eligibility Adapter
  participant P3 as Package 003 Authority
  participant HG as Human Governance Gate
  CM->>EA: Asset ID + version + intended contribution/use
  EA->>P3: READ eligibility/handoff decision
  P3-->>EA: lifecycle, owner, SOT, restrictions, dependencies, eligibility + evidence ref
  EA-->>CM: immutable consumed decision
  CM->>HG: composition fit proposal
  HG-->>CM: fit decision; never eligibility override
```

| P003 result | P004 behavior |
|---|---|
| CANDIDATE / UNDER_REVIEW | `NOT_COMPOSABLE` |
| VALIDATED / NOT_CANONICAL | `REFERENCE_ONLY / NOT_ATTACHABLE` |
| CANONICAL + incomplete handoff | `NOT_ELIGIBLE` with named gaps |
| CANONICAL + complete handoff | `ELIGIBLE_FOR_GOVERNED_ATTACHMENT`; P004 may still reject Product fit |

The adapter is unidirectional: `READ / REFERENCE / CONSUME DECISION`. It exposes no `WRITE / OVERRIDE` operation. P003 handoff includes identity, version, lifecycle, human owner, SOT, provenance, restrictions, attachment eligibility, contribution/support/exit expectations and dependencies.

## Composition integrity

Composition preserves the most restrictive applicable licensing, sensitivity, sharing, risk and dependency constraint unless competent human authority and evidence validly change that constraint at its owning layer. P004 cannot cure Asset ineligibility. Packaging copies neither Asset authority nor rights.

## Current reference scenario

ASSET-1, ASSET-2 and ASSET-3 are `VALIDATED / NOT_CANONICAL`. The adapter therefore returns `REFERENCE_ONLY / NOT_ATTACHABLE` for each. They may test hypothetical structure only; no Candidate, composition record or attachment is created.

Trace: R04–R06, R10, R17–R18, R22.
