# Reusable Lab Inception Template Registration Baseline Renewal Founder Decision

## 1. Decision metadata

| Field | Value |
|---|---|
| Decision ID | `FD-LABOS-REUSABLE-LAB-INCEPTION-TEMPLATE-REGISTRATION-BASELINE-RENEWAL-001` |
| Decision status | `APPROVED_BY_FOUNDER` |
| Classification | `FOUNDER_DECISION` |
| Approval date | 2026-10-24 |
| Provenance | Explicit Founder approval in the ChatGPT LabOS conversation on 2026-10-24 |
| Scope | Registration execution baseline renewal only |
| Documentation state | `LOCAL_FILE_CREATED` — Founder-approved decision documented locally; Git durability and publication not established |
| Registration execution | `NOT_AUTHORIZED_BY_THIS_DECISION / NOT_EXECUTED` |

## 2. Founder approval and provenance

[Hecho] The Founder explicitly approved renewal of the registration execution baseline and the exact baseline condition of the Cloud branch amendment, preserving every other authorization gate.

This text documents the approval supplied in the conversation. Approval of the renewal does not authorize file creation, Git write operations, publication or registration execution. Creation of this local file was separately authorized by the Founder instruction `LABOS_BASELINE_RENEWAL_DECISION_CONTROLLED_FILE_CREATION`, limited to this document and documentary metadata normalization. It grants no Git durability or publication authority.

## 3. Exact artifact identity

| Field | Required value |
|---|---|
| Artifact ID | `LABOS-LAB-INCEPTION-TEMPLATE` |
| Artifact path | `labs/lab-inception-template-v1.md` |
| Version | `1.1.0` |
| SHA-256 | `65344d5cf45bf4299e5ed2a8d6caaba6e7bcc186c23db1690d11ed0fbd063048` |
| Governance owner | `LabOS Founder Governance Authority` |

This renewal applies exclusively to this artifact, version, digest and registration. It does not apply to future versions or Lab-specific copies.

## 4. Original and renewed execution baseline

| Field | Commit |
|---|---|
| Original execution baseline | `1ccf421e63394f6cac4fbf27aaa32cac90fa95f0` |
| Renewed execution baseline | `9b89f379894ae6e6603012571c6015f9ee72960d` |
| Historical acceptance-evidence durability commit | `f545d24a0a46da2a24fb535f679bc56d176bf3dd` |

[Decisión] The execution baseline is renewed from the original commit to the renewed commit above.

The historical Git commit is not replaced. Its role as durable acceptance evidence, its parentage and its historical meaning remain unchanged.

## 5. Verified evidence supporting renewal

[Hecho] Read-only review verified that:

- GitHub main equals the renewed execution baseline at review time.
- The original execution baseline is its ancestor.
- Intervening history contains the approved governance commit `b32c03639b80d297caf3c6eea63576aa624e91d6` and merge commit `9b89f379894ae6e6603012571c6015f9ee72960d`, corresponding to PR #1.
- Net changes are limited to the two approved Founder decision documents.

| Document | Verified SHA-256 |
|---|---|
| `docs/architecture/reusable-lab-inception-template-cloud-branch-amendment-founder-decision.md` | `c2793cf38c65ef4dfee2f35e25676ead00dba1675e66754224a2b1afe182181f` |
| `docs/architecture/reusable-lab-inception-template-status-clarification-founder-decision.md` | `c368140c57cde891cbd973c59b4f028d87edeef05b6bc253f1bdb43652aab8f8` |

The template retains its authorized version and digest. The original registration authorization and architecture document register remain unchanged. The register contains 44 entries; REG-045 is available and the template has no registration entry.

These observations are evidence at review time, not a guarantee of unchanged future state.

## 6. Explicit renewal of both baseline gates

[Decisión] For this registration only:

1. The applicable execution-baseline requirement associated with `FD-LABOS-REUSABLE-LAB-INCEPTION-TEMPLATE-REGISTRATION-001` shall use the renewed execution baseline.
2. The exact execution-baseline condition, including the pre-execution comparison of work HEAD, origin/main and GitHub main, in `FD-LABOS-REUSABLE-LAB-INCEPTION-TEMPLATE-CLOUD-BRANCH-AMENDMENT-001` shall use the same renewed execution baseline instead of `1ccf421e63394f6cac4fbf27aaa32cac90fa95f0`.

This changes execution-baseline applicability only. It does not replace the historical durable-baseline evidence recorded in the original authorization.

The isolated Codex Cloud `work` branch exception remains narrowly scoped and conditional. This renewal does not move that branch or authorize any operation to prepare it.

## 7. Preserved non-baseline conditions

All non-baseline gates remain applicable, including:

- Exact repository, template path, version and SHA-256.
- Reconstructable governance and immutable acceptance history.
- Independent acceptance verdict `POST_PACKAGE_004_REUSABLE_LAB_INCEPTION_TEMPLATE_ACCEPT`.
- Registration readiness `READY_FOR_AUTHORIZATION` and no blockers.
- Clean working tree and empty index before future execution.
- No existing or duplicate template registration.
- Existing register schema and conventions, without new categories or columns.
- Architecture Freeze `PRESERVED`.
- `MODIFY_BASELINE=NO`, `EXTENDS_BASELINE=NO`, `ADR_REQUIRED=NO`.
- Packages 003 and 004 remaining `CLOSED`.
- Independent review before integration and separate authority for any publication or integration.

The sole potential future registration-edit target remains:

`docs/architecture/architecture-document-register-v1.0.md`

No edit to that file is authorized by this decision.

## 8. Relationship to historical decisions

The original decisions remain unchanged:

- `FD-LABOS-REUSABLE-LAB-INCEPTION-TEMPLATE-REGISTRATION-001`.
- `FD-LABOS-REUSABLE-LAB-INCEPTION-TEMPLATE-CLOUD-BRANCH-AMENDMENT-001`.
- `FD-LABOS-REUSABLE-LAB-INCEPTION-TEMPLATE-STATUS-CLARIFICATION-001`.
- The applicable remediation, acceptance and durability decisions.

Their original text, dates and historical evidence remain preserved. This decision expressly renews only execution-baseline applicability; it does not silently rewrite or generally supersede their other terms.

The status clarification remains applicable: APPROVED identifies artifact approval; REGISTERED is the required Status for its future architecture register entry. No general status-vocabulary change is authorized.

Historical execution gates for already completed remediation or durability operations are not reopened or retroactively changed.

## 9. Explicit exclusions and prohibitions

This decision grants no authorization for:

- File creation or modification. The separate, bounded instruction to create this local decision record grants no authority over any other file.
- Git stage, commit, push, pull, fetch, PR creation, merge, rebase, reset, clean, tags, branch switching or checkout.
- Registration execution or automatic registration authority.
- Template modification or version change.
- Lab creation, approval, activation, resumption or execution.
- Architecture semantic changes or Package lifecycle changes.
- Product or Asset operations, implementation or infrastructure.
- Research, experiments, Human Performance resumption or EXP-000024.
- RAG, MCP, AI Agent or automation activation.

No permission to publish is implied. Git durability and publication each require separate authorization.

## 10. Future execution prerequisites

Before a separately authorized registration execution:

1. Obtain explicit authority for that execution and any required checkout-preparation operation.
2. Verify the approved renewal and governance chain are available as applicable evidence.
3. Verify the execution branch, HEAD, origin/main and GitHub main satisfy the renewed baseline and applicable branch conditions.
4. Independently revalidate concurrency and all remaining gates. Main must remain unchanged during execution. Stop on divergence, failed verification or concurrency uncertainty.
5. Revalidate template identity, acceptance, durability, register state and REG-045 availability.
6. Require a clean working tree and empty index; this decision does not waive those conditions to accommodate documentation.
7. Stop on any mismatch or ambiguity without automatic repair.

Endpoint equality alone does not establish continuous main immobility.

REG-045 remains NOT_EXECUTED: this decision neither inserts an entry nor reserves or consumes the identifier.

## 11. Decision status and traceability

| Dimension | State |
|---|---|
| Founder approval | `APPROVED_BY_FOUNDER` |
| Baseline renewal scope | Both execution-baseline gates only |
| Documentation | `LOCAL_FILE_CREATED` |
| Git durability of this document | `NOT_ESTABLISHED` |
| Remote publication of this document | `NOT_EXECUTED` |
| Registration execution | `NOT_EXECUTED` |
| REG-045 insertion | `NOT_EXECUTED` |
| Architecture Freeze | `PRESERVED` |
| Packages 003/004 | `CLOSED` |

Founder approval, documentary preservation, Git durability, publication and registration execution are distinct events.

Next safe action: independent review of the created file before requesting separate Git durability authority. No follow-up operation occurs automatically.
