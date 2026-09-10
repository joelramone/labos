# Package 004 — Tasks Traceability Matrix

## Control

| Field | Value |
|---|---|
| Task Plan | v1.0 `TASKS_APPROVED` — `FD-P004-TASKS-001` |
| Requirements / Design | v1.0 `APPROVED` / v1.0 `APPROVED` |
| Requirements / acceptance criteria | `25/25` / `100/100` |
| Design components / decisions | `20/20` / `15/15` applicable |
| Tasks / orphan Tasks | `32` / `0` |

## TASKS_TRACEABILITY_MATRIX

Every Requirement row covers all four approved acceptance criteria. Task contracts in `tasks.md` supply inputs, outputs, boundaries and completion conditions.

| Requirement → AC | Producing/verifying Tasks | Design components | Design Decisions | Expected evidence |
|---|---|---|---|---|
| R01 → R01.1–R01.4 | T004-003, 020, 031–032 | C02 | D001–D002, D010 | Product identity/distinction and duplicate/gap audit |
| R02 → R02.1–R02.4 | T004-002, 017, 020, 028, 031–032 | C01 | D002–D003, D010 | Candidate template, terminal outcome and zero-effect scenarios |
| R03 → R03.1–R03.4 | T004-004, 016–018, 029, 032 | C05, C19 | D003–D004, D008–D009 | Seven-state matrix, guards and rejection outcome checks |
| R04 → R04.1–R04.4 | T004-006, 028, 030, 032 | C03 | D005–D006 | One/many/shared/external composition scenarios |
| R05 → R05.1–R05.4 | T004-007, 028, 030, 032 | C04 | D005 | Four P003 eligibility outcomes and no-override evidence |
| R06 → R06.1–R06.4 | T004-006–007, 012, 021, 030, 032 | C03, C04, C08, C16 | D005–D006, D012 | Restriction mapping, unresolved conflict and SOT preservation |
| R07 → R07.1–R07.4 | T004-004–005, 018, 025, 029, 032 | C02, C19, C20 | D008–D009, D013 | Human roles/transfer and AI-owner rejection evidence |
| R08 → R08.1–R08.4 | T004-005, 020, 031–032 | C02 | D001, D010 | Exactly-one Product SOT and conflicting-authority scenario |
| R09 → R09.1–R09.4 | T004-010, 020, 031–032 | C12 | D002, D006, D010 | Lineage graph, exact versions and explicit gaps |
| R10 → R10.1–R10.4 | T004-019–020, 031–032 | C13 | D001, D004, D006 | Version/change/compatibility classification scenarios |
| R11 → R11.1–R11.4 | T004-011, 015, 026, 029, 032 | C07 | D007, D011, D014 | Nine-dimension Product-quality matrix and failure checks |
| R12 → R12.1–R12.4 | T004-012, 015, 021, 026, 030, 032 | C08 | D007–D008, D012, D014 | Nine-category risk, propagation and human acceptance |
| R13 → R13.1–R13.4 | T004-013, 015, 024, 028, 031–032 | C09 | D007, D011, D015 | Three value states and non-transfer/non-lifecycle checks |
| R14 → R14.1–R14.4 | T004-014–015, 024, 028, 031–032 | C10 | D007, D011, D015 | Falsifiable demand plan/result and Revenue separation |
| R15 → R15.1–R15.4 | T004-015–016, 018, 028–029, 032 | C06, C19 | D007–D009, D011 | Eleven-control readiness and no-automatic-transition checks |
| R16 → R16.1–R16.4 | T004-004, 016, 018, 025, 028–029, 032 | C05, C19, C20 | D004, D008–D009, D013 | Separate valid approval/activation and fail-closed authority |
| R17 → R17.1–R17.4 | T004-006–010, 030, 032 | C03, C11, C12, C14 | D006, D012 | Technology-neutral manifest and rights visibility audit |
| R18 → R18.1–R18.4 | T004-008, 019–020, 022, 026, 030, 032 | C11, C15 | D006, D010, D014 | Four dependency classes and critical-change review |
| R19 → R19.1–R19.4 | T004-001, 027, 031–032 | C01–C20 | D013–D014 | Full manual tabletop and no-infrastructure dependency |
| R20 → R20.1–R20.4 | T004-025, 027, 029, 031–032 | C20 | D013 | AI permission/failure matrix and source uncertainty |
| R21 → R21.1–R21.4 | T004-024, 028, 030, 032 | C18 | D015 | Complete dossier, blocking gaps and zero Revenue operation |
| R22 → R22.1–R22.4 | T004-009, 012, 021, 024, 028, 030, 032 | C08, C14, C16, C18 | D011–D012, D015 | Sharing/commercial separation and most-restrictive scope |
| R23 → R23.1–R23.4 | T004-019–020, 022–023, 026, 031–032 | C11, C13, C15, C17 | D004, D010, D014 | Trigger checklist, prior comparison and unchanged state |
| R24 → R24.1–R24.4 | T004-016–018, 020, 023, 029, 032 | C05, C17, C19 | D004, D008, D010 | Deprecation/retirement impact and immutable history |
| R25 → R25.1–R25.4 | T004-002–005, 010, 016–020, 022–023, 031–032 | C01, C02, C05, C12, C13, C15, C17, C19 | D001–D004, D008, D010 | Registry completeness, change history and rejection checks |

## Design component coverage

| Components | Realization Tasks |
|---|---|
| C01–C02 | T004-002–003, T004-020 |
| C03–C04 | T004-006–007 |
| C05–C06 | T004-015–018 |
| C07–C10 | T004-011–014 |
| C11–C13 | T004-008, T004-010, T004-019 |
| C14–C18 | T004-009, T004-021–024 |
| C19–C20 | T004-004, T004-025 |

Verification/integration Tasks T004-027–032 cover all components. Result: `20/20`.

## Design Decision coverage

| Decisions | Primary Tasks |
|---|---|
| D001–D004 | T004-002–005, T004-016–020 |
| D005–D006 | T004-006–010, T004-019 |
| D007–D009 | T004-004, T004-011–018 |
| D010–D012 | T004-002–003, T004-013–015, T004-020–024 |
| D013–D015 | T004-024–027 |

Result: `15/15` applicable Design Decisions have realization and/or verification. No Task lacks a Requirement or approved Design source.
