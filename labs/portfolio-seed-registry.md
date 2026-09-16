# Portfolio Seed Registry

## Purpose

[Decisión] Este registro separa proyectos conocidos de Labs activos y evita convertir automáticamente toda idea, proyecto, Asset o Capability Candidate en un Lab.

## Classification framework

| Classification | Criterion |
|---|---|
| `ACTIVE_LAB` | Completó el mínimo de inception o integración y tiene actividad compatible con su Lab State |
| `REFERENCE_LAB` | Completó integración end-to-end y los criterios formales de Reference Lab |
| `CANDIDATE_LAB` | Vertical e hipótesis documentadas, pero inception/integración o decisión pendiente |
| `CAPABILITY_CANDIDATE` | Función potencialmente compartible; no activa ni canónica |
| `PRODUCT` | Oferta concreta para un segmento; no implica Lab independiente |
| `SUPPORTING_PROJECT` | Proyecto que habilita distribución, operación o evidencia sin justificar Lab propio |
| `KNOWLEDGE_DOMAIN` | Cuerpo de investigación que puede alimentar uno o más Labs |
| `INSUFFICIENT_EVIDENCE` | No existe evidencia suficiente para clasificar responsablemente |

## Evidence sources used

- [Hecho] Package 000 `012-portfolio-model.md` registra LabOS, SoftwareFactoryAgentsAI, CommunityManagerBotCrew, Mindzers, SentinelOps, Crypto Scalping Core, Atlas Wealth Labs, Human Performance Lab, Photography Lab, Music Lab y English Learning Lab.
- [Hecho] `labs/README.md` registra varios de esos nombres como `idea` y establece que se crea carpeta al pasar a `explorando`.
- [Hecho] Package 001A registra Crypto Scalping Core como `LABOS-REF-LAB-0001`.
- [Hecho] La inspección local no encontró directorios identificables por nombre para Mindzers, CommunityManagerBotCrew, SoftwareFactoryAgentsAI, Photography, OPEX, Music, Shakespeare, Online CV, English Learning, TYANA o Atlas Wealth.
- [Decisión] Las descripciones proporcionadas por el fundador se conservan como hipótesis, no como evidencia de existencia o madurez.

## Seed registry

| Seed | Provisional classification | Lab state / status | Confidence | Evidence and rationale | Next gate |
|---|---|---|---|---|---|
| Crypto Scalping Core | `REFERENCE_LAB` | `explorando`; `LABOS-REF-LAB-0001` | High | Package 001A records completed integration, approval and Reference Lab status | No action; do not modify |
| Human Performance 40+ | `ACTIVE_LAB` | `explorando`; inception approved; `LAB-HP40`; execution `PAUSED_BY_FOUNDER` | High | Complete inception source of truth plus `FD-HP40-INCEPTION-001`; pause authority `FD-HP40-PAUSE-001` | Do not execute Phase 1 unless the Founder separately resumes it |
| Mindzers | `CANDIDATE_LAB` | Historical `idea`; not active | Medium | Package 000 documents a vertical and product hypothesis; no inception/integration evidence found | Repository/evidence intake before activation |
| CommunityManagerBotCrew | `CAPABILITY_CANDIDATE` | Dormant hypothesis | Low | Historical content/distribution hypothesis plus Founder-proposed cross-Lab role; no Lab inception evidence | Prove shared reuse or independent Lab mission |
| SoftwareFactoryAgentsAI | `CANDIDATE_LAB` | Historical `explorando` claim not accepted as current activation evidence | Medium | Package 000 documents a vertical, but no minimum inception/integration evidence was found | Reconcile current artifacts and complete inception/integration |
| Photography | `CANDIDATE_LAB` | Historical `idea`; not active | Medium | Package 000 documents a vertical and product hypothesis; no inception/integration evidence found | Intake actual artifacts, mission and monetization hypothesis |
| OPEX / Training Methodology | `INSUFFICIENT_EVIDENCE` | Unclassified | Low | No identifiable local evidence found | Determine provenance and overlap with `LAB-HP40`; do not create Lab |
| Music | `CANDIDATE_LAB` | Historical `idea`; not active | Medium | Package 000 documents a vertical and product hypothesis; no inception/integration evidence found | Evidence intake before defining product or audience |
| Shakespeare / To Be or Not To Be | `INSUFFICIENT_EVIDENCE` | Unclassified | Low | No identifiable local evidence found | Determine whether Product, Supporting Project or broader domain input |
| Online CV / Research Portfolio | `SUPPORTING_PROJECT` | Provisional; not Lab | Low | Founder description indicates portfolio/distribution intent; no independent Lab evidence | Validate purpose and consumers; default to no Lab |
| English Learning | `CANDIDATE_LAB` | Historical `idea`; not active | Medium | Package 000 documents a vertical and product hypothesis; no inception/integration evidence found | Validate independent product hypothesis versus Knowledge Domain |
| TYANA | `INSUFFICIENT_EVIDENCE` | Unclassified | Low | No identifiable local evidence found | Inventory existing IP before classification; do not modify |
| Atlas Wealth Labs | `CANDIDATE_LAB` | Historical `idea`; not active | Medium | Package 000 documents a finance vertical and product hypothesis; no inception/integration evidence found | Confirm independent mission and complete inception/integration |

## Reconciliation record — 2026-08-12

| Previous classification | Corrected classification | Reason |
|---|---|---|
| Crypto Scalping Core: Existing Lab + Reference Lab | `REFERENCE_LAB` | Reference eligibility is evidenced by Package 001A |
| Human Performance 40+: Existing Lab in inception | `CANDIDATE_LAB` | Inception exists; Founder activation/identity confirmation remains pending |
| Mindzers, Photography, Music, English Learning, Atlas Wealth: Existing Lab | `CANDIDATE_LAB` | Historical portfolio mention does not prove inception/integration |
| CommunityManagerBotCrew: Existing Lab / Capability Candidate | `CAPABILITY_CANDIDATE` | Cross-Lab role is plausible; independent Lab evidence is absent |
| SoftwareFactoryAgentsAI: Existing/active Lab | `CANDIDATE_LAB` | Historical state alone is insufficient under the evidence rule |
| Human Performance 40+: Candidate Lab after reconciliation | `ACTIVE_LAB` | Founder approved identity, priority, boundary and Phase 1 after complete inception |

## Provisional portfolio summary

- `REFERENCE_LAB`: Crypto Scalping Core.
- `ACTIVE_LAB`: Human Performance 40+ (`LAB-HP40`, inception).
- `CANDIDATE_LAB`: Mindzers, SoftwareFactoryAgentsAI, Photography, Music, English Learning and Atlas Wealth Labs.
- `CAPABILITY_CANDIDATE`: CommunityManagerBotCrew.
- `SUPPORTING_PROJECT`: Online CV / Research Portfolio.
- `INSUFFICIENT_EVIDENCE`: OPEX / Training Methodology, Shakespeare / To Be or Not To Be and TYANA.

Current execution note: Human Performance 40+ remains `PAUSED_BY_FOUNDER`. Its `ACTIVE_LAB` portfolio classification and `explorando` Lab State do not authorize Phase 1 execution or resume the Lab.

## Governance notes

- [Decisión] Historical portfolio registration does not establish `ACTIVE_LAB`.
- [Decisión] No other Lab is initiated by this registry.
- [Decisión] A classification can change only when new evidence is linked and the founder records the decision.
- [Decisión] Assets require Package 003; Capabilities remain dormant until the canonical activation trigger is satisfied.
