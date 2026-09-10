# Package 004 — Requirements Traceability Matrix

## Control

| Field | Value |
|---|---|
| Requirements version | 1.0 (`APPROVED`, `FD-P004-REQ-001`) |
| Date | 2026-09-03 |
| Top-level requirements | 25 |
| Acceptance criteria | 100 |
| Trace classes | ARCHITECTURE, UPSTREAM_PACKAGE, FOUNDER_DECISION, ACTIVATION_CONDITION, DERIVED_REQUIREMENT |

Source codes are defined in [requirements.md](./requirements.md#authoritative_source_map). Derived requirements turn upstream boundaries into Product-specific controls; they do not invent Founder decisions or modify upstream authority.

## Matrix

| Requirement | Topic | Primary trace | Trace class | Derivation | Verification coverage |
|---|---|---|---|---|---|
| P004-R01 | Product identity | ARCH, P000, P002, P003 | ARCHITECTURE + UPSTREAM + DERIVED | Product is the missing Products-stage governed entity and must remain distinct from upstream/downstream entities | R01.1–R01.4: document, scenario, governance |
| P004-R02 | Product Candidate | ARCH, P000, FD004 | ARCHITECTURE + FOUNDER_DECISION + DERIVED | A distinct proposal preserves unapproved formation evidence without calling an Asset/Product approved | R02.1–R02.4 |
| P004-R03 | Product lifecycle | ARCH, P003, FD004 | ARCHITECTURE + UPSTREAM + ACTIVATION_CONDITION + DERIVED | Product governance needs states distinct from Asset lifecycle and explicit human transitions | R03.1–R03.4 |
| P004-R04 | Asset composition | P003 | UPSTREAM_PACKAGE + DERIVED | P003 permits future Products to depend on one/multiple Assets and defines contribution/dependency concepts | R04.1–R04.4 |
| P004-R05 | Attachment eligibility | P003, FD004 | UPSTREAM_PACKAGE + ACTIVATION_CONDITION | P003 explicitly requires CANONICAL plus handoff gates; activation condition forbids CANONICAL assumption | R05.1–R05.4 |
| P004-R06 | Composition integrity | P003, FD004 | UPSTREAM_PACKAGE + ACTIVATION_CONDITION + DERIVED | Composition must propagate rather than erase upstream governance | R06.1–R06.4 |
| P004-R07 | Ownership | P000, P003, FD004 | UPSTREAM_PACKAGE + ACTIVATION_CONDITION + DERIVED | SOLO human authority and distinct Asset ownership require separate Product roles | R07.1–R07.4 |
| P004-R08 | Product SOT | ARCH, P002, P003 | ARCHITECTURE + UPSTREAM + DERIVED | One-source/multiple-reference invariant applies to the new Product entity | R08.1–R08.4 |
| P004-R09 | Provenance | P001, P002, P003 | UPSTREAM_PACKAGE + DERIVED | Product must extend, not replace, the existing evidence chain | R09.1–R09.4 |
| P004-R10 | Versioning | ARCH, P003 | ARCHITECTURE + UPSTREAM + DERIVED | Product compatibility needs an independent semantic version and Asset-change impact rule | R10.1–R10.4 |
| P004-R11 | Product quality | P001, P003 | UPSTREAM_PACKAGE + DERIVED | Asset quality cannot certify composed consumer-facing Product quality | R11.1–R11.4 |
| P004-R12 | Product risk | P001, P003, FD004 | UPSTREAM + ACTIVATION_CONDITION + DERIVED | Risk aggregates across composition and intended consumer exposure | R12.1–R12.4 |
| P004-R13 | Product value | P000, P003 | UPSTREAM_PACKAGE + DERIVED | Product value must be tied to user outcomes and separated from Asset value | R13.1–R13.4 |
| P004-R14 | Demand validation | P000, P001, ARCH | ARCHITECTURE + UPSTREAM + DERIVED | P004 owns demand validation before the P005 Revenue boundary | R14.1–R14.4 |
| P004-R15 | Readiness | P001, P003, FD004 | UPSTREAM + ACTIVATION_CONDITION + DERIVED | Readiness consolidates Product gates but cannot be a vague score or commercial approval | R15.1–R15.4 |
| P004-R16 | Approval/activation | P000, P003, FD004 | UPSTREAM + FOUNDER_DECISION + DERIVED | Human authority and prohibition of automatic promotion extend to Product decisions | R16.1–R16.4 |
| P004-R17 | Packaging | P003 | UPSTREAM_PACKAGE + DERIVED | Productization must expose composition, usage, restrictions and delivery assumptions without choosing technology | R17.1–R17.4 |
| P004-R18 | Dependencies | P003, ARCH | ARCHITECTURE + UPSTREAM + DERIVED | Product dependencies extend P003 handoff fields and keep optional platform layers explicit | R18.1–R18.4 |
| P004-R19 | Manual-first | ARCH, FD004 | ARCHITECTURE + ACTIVATION_CONDITION | SOLO governance and activation decision require operation without P006/P007/infrastructure | R19.1–R19.4 |
| P004-R20 | AI authority | P002, P003, FD004 | UPSTREAM + ACTIVATION_CONDITION | Upstream human authority and dormant infrastructure bound optional AI assistance | R20.1–R20.4 |
| P004-R21 | P005 handoff | ARCH, P000, FD004 | ARCHITECTURE + ACTIVATION_CONDITION + DERIVED | Frozen pipeline requires a documented boundary from ready Product to separately governed Revenue | R21.1–R21.4 |
| P004-R22 | Commercialization/sharing | P003, FD004 | UPSTREAM + ACTIVATION_CONDITION + DERIVED | Product status cannot erase licensing or create commercial authority | R22.1–R22.4 |
| P004-R23 | Review/freshness | P001, P002, P003 | UPSTREAM_PACKAGE + DERIVED | Existing evidence/source/dependency freshness rules must propagate to Products | R23.1–R23.4 |
| P004-R24 | Deprecation/retirement | ARCH, P002, P003 | ARCHITECTURE + UPSTREAM + DERIVED | Product history/consumer impact needs controlled retirement without silent deletion | R24.1–R24.4 |
| P004-R25 | Registry/history | ARCH, P002, P003 | ARCHITECTURE + UPSTREAM + DERIVED | Product governance needs a technology-neutral current/historical truth contract | R25.1–R25.4 |

## Coverage by required area

| Required area | Requirements | Status |
|---|---|---|
| Identity / Candidate / lifecycle | R01–R03 | COVERED |
| Composition / eligibility | R04–R06 | COVERED |
| Ownership / SOT / provenance / versioning | R07–R10 | COVERED |
| Quality / risk / value / demand / readiness | R11–R15 | COVERED |
| Approval / packaging / dependencies | R16–R18 | COVERED |
| Manual operation / AI authority | R19–R20 | COVERED |
| Revenue handoff / commercialization | R21–R22 | COVERED |
| Review / retirement / sharing / registry | R22–R25 | COVERED |

Orphan requirements: 0. Required areas without a normative control: 0. Requirements without acceptance criteria: 0.
