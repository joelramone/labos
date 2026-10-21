# Reusable Lab Inception Template Cloud Branch Amendment Founder Decision

## Decision and provenance

| Field | Value |
|---|---|
| Decision ID | `FD-LABOS-REUSABLE-LAB-INCEPTION-TEMPLATE-CLOUD-BRANCH-AMENDMENT-001` |
| Status | `APPROVED_BY_FOUNDER` |
| Classification | `FOUNDER_DECISION` |
| Date | 2026-10-17 (`America/Buenos_Aires`) |
| Provenance | Explicit Founder instruction in this conversation, supplied as `LABOS_CLOUD_BRANCH_AMENDMENT_DOCUMENTATION_AND_STATUS_RECONCILIATION` |
| Parent authorization | `FD-LABOS-REUSABLE-LAB-INCEPTION-TEMPLATE-REGISTRATION-001` |
| Registration execution by this action | `NOT_AUTHORIZED / NOT_PERFORMED` |

[Hecho] The Founder explicitly approved the narrowly scoped branch-gate amendment in the conversation and authorized creation of this record only. The instruction expressly withheld registration execution and Git staging, commit, push, merge, rebase, tags and PR authority. This record documents that instruction; it does not manufacture a new approval or establish Git durability for itself.

## Exact exception

[Decisión] For a future, separately authorized registration execution, the literal condition `branch is main` in gate 1 of the parent authorization may alternatively be satisfied by the existing isolated Codex Cloud branch `work` in `joelramone/labos`, subject to every verification gate below.

The original authorization at `docs/architecture/reusable-lab-inception-template-registration-authorization-decision.md` remains intact. This exception changes only its branch condition for this exact template, version, baseline and execution context. It is not a general Cloud branch policy and does not waive any other original gate.

## Exact identity and baseline

| Field | Required value |
|---|---|
| Repository | `joelramone/labos` |
| Permitted alternative execution branch | Isolated Codex Cloud `work` |
| Execution baseline HEAD | `1ccf421e63394f6cac4fbf27aaa32cac90fa95f0` |
| Historical durability commit | `f545d24a0a46da2a24fb535f679bc56d176bf3dd` |
| Artifact ID | `LABOS-LAB-INCEPTION-TEMPLATE` |
| Template path | `labs/lab-inception-template-v1.md` |
| Template version | `1.1.0` |
| Template SHA-256 | `65344d5cf45bf4299e5ed2a8d6caaba6e7bcc186c23db1690d11ed0fbd063048` |

The execution baseline does not replace the historical durability commit or reinterpret its evidence.

## Mandatory future verification gates

1. A separate explicit instruction must authorize registration execution. Approval of this amendment and documentation of it do not authorize that execution.
2. Before execution, verify repository identity, isolated branch `work`, and a clean working tree with no staged changes. This newly created, uncommitted decision record does not waive the clean-tree requirement or authorize a commit to satisfy it.
3. Verify `work` HEAD, local `origin/main`, and GitHub `refs/heads/main` directly against the exact execution baseline above. A cached remote-tracking ref alone is insufficient.
4. Main must remain unchanged throughout execution. Verify GitHub main before and after the documentary edit and stop on divergence, failed verification or concurrency uncertainty. Endpoint equality alone does not prove continuous immobility; do not infer or manufacture a concurrency guarantee.
5. The parent authorization, this amendment, historical durability commit and complete governance chain must remain reconstructable. Template identity, independent acceptance, Git durability, Architecture Freeze and all remaining original gates continue to apply.
6. Registration must remain unexecuted and free of duplicate entries before the future write. Any unresolved status ambiguity must be clarified explicitly before execution; this branch amendment does not reconcile `APPROVED` and `REGISTERED` or supersede either historical prescription.
7. Use the existing register schema and conventions without architecture semantic changes, baseline modification or extension. Any failed or ambiguous gate requires `STOP`; do not remediate automatically.

## Separate write boundaries

[Decisión] This documentation action may create exactly this new decision record. It may not modify the original authorization, template, register or any other existing file.

For the future separately authorized registration execution, the only permitted edit target remains:

```text
docs/architecture/architecture-document-register-v1.0.md
```

That future execution must preserve the original authorization's exact artifact identity and bounded registration scope. It must not edit this amendment, the original authorization, template, acceptance evidence, Package records or Lab-instance files.

## Review and Git boundaries

[Decisión] Independent review of the exact registration diff and applicable verification evidence is required before any integration or merge. Review does not itself authorize integration.

No staging, commits, pushes, merges, rebases, tags, PR creation, branch changes or history rewrite are authorized by this amendment. Any such operation requires separate explicit approval. Recording this amendment does not authorize publishing or committing it.

## Preserved governance boundaries

- Package 003 and Package 004 remain `CLOSED`; no Package lifecycle change is authorized.
- Architecture Freeze remains `PRESERVED`; `MODIFY_BASELINE=NO`, `EXTENDS_BASELINE=NO`. This branch exception changes no architectural definition or invariant.
- No Lab creation, inception approval, registration, activation, resumption or execution is authorized.
- No template modification, Product or Asset operation, implementation, infrastructure, research or experiment is authorized.
- Human Performance remains `PAUSED_BY_FOUNDER`; Packages 005/006/007 remain `DORMANT`.
- RAG, MCP, AI Agents and `EXP-000024` remain unauthorized by this action.

## Result and next safe action

The branch amendment is `APPROVED_BY_FOUNDER` and documented. Registration execution remains `NOT_AUTHORIZED_BY_THIS_ACTION / NOT_PERFORMED`. This record is not a status-reconciliation decision and infers no supersession.

Next safe action: obtain any required Founder status clarification, then separately request a read-only registration readiness review. No follow-up operation is executed automatically.
