# Package 004 — Controlled Verification Plan

## Scope

This plan defines future documentary verification only. It runs no scenario and changes no governed state.

| Verification domain | Planned assertions | Fixtures/evidence | Task |
|---|---|---|---|
| Lifecycle | Exactly seven states; listed transitions/guards only; invalid requests fail closed | State/transition count and F02 | T004-029 |
| REJECTED | Terminal outcome; identity/evidence/authority/time/reason preserved; no re-entry | F02 historical comparison | T004-029 |
| Readiness | Eleven controls, no score/threshold, no automatic lifecycle transition | F05–F06 | T004-029 |
| Human authority | Missing/AI authority leaves state unchanged; approval/activation separate | F06–F08 | T004-029 |
| AI boundary | Allowed/draft/prohibited operations match matrix; prohibited calls fail closed | Permission scenario matrix | T004-029 |
| P003 eligibility | Four exact mappings; P004 cannot grant/override | F03–F04 plus two variants | T004-030 |
| Restrictions | Upstream licensing/risk/sharing constraints preserved or elevated | F09 | T004-030 |
| Sharing/activation | Lifecycle ≠ sharing; ACTIVE ≠ PUBLIC/commercial/revenue | F07–F09 | T004-030 |
| P005 boundary | Dossier completeness; forbidden Revenue operations absent | F10 | T004-030 |
| Registry/SOT/history | Required lookups; one Product SOT; current/history distinction; silent rewrite rejected | Registry query/conflict matrices | T004-031 |
| Provenance/version | Missing lineage explicit; exact Asset versions; changes trigger review only | Lineage and compatibility scenarios | T004-031 |
| Manual-first | Full workflow operable using documents with no platform dependency | Tabletop walkthrough | T004-031 |
| Domain neutrality | No trading/profit/backtest/optimizer/journal/software assumptions; extension cannot fork governance | Neutral extension inspection | T004-031 |

## Evidence contract

Every future verification record must identify scenario/fixture, source versions, precondition, procedure, observed result, expected result, pass/fail, discrepancies, authority/reviewer, timestamp and affected Task/Requirement/Design reference. Failure cannot be converted into a pass by narrative judgment; it produces a named remediation or upstream change classification.

Execution status: `NOT_AUTHORIZED`.

