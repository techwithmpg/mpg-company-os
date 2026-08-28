# Contributing to MPG Company OS

| Metadata | Value |
|---|---|
| Document | Contribution policy |
| Status | ACTIVE |
| Stage | Stage 0 — Governance and Source of Truth |
| Owner | MPG Founder |
| Last Updated | 2026-08-28 |
| Public Safe | Yes |
| Authority | Governing workflow for human and agent contributions |

MPG welcomes disciplined contributions that strengthen the company's source of truth. Humans and agents follow the same principles: preserve evidence, protect focus, separate proposals from decisions, and keep public content safe.

## Before proposing a change

Read, in order:

1. `README.md`
2. `AGENTS.md`
3. `docs/01-project-status.md`
4. `docs/02-decision-register.md`
5. Relevant domain documentation
6. Applicable operating-model policies and registry records

Then inspect the current Git status and existing implementation. Improve the existing source of truth rather than creating a parallel document for the same authority.

## Contribution boundaries

- Keep work aligned with the current stage and authorized scope.
- Do not begin a future stage because its framework exists.
- Do not introduce unrelated services, tools, channels, automations, or corporate scope.
- Respect the default work-in-progress limit: one primary commercial productization track and no more than one authorized secondary learning track.
- Preserve accepted and frozen decisions. If a change conflicts with one, identify the conflict and obtain owner direction.
- Never mark a service active or marketing-approved without explicit owner authorization and supporting readiness evidence.

## Proposal is not acceptance

Use the decision states consistently:

- `PROPOSED` for an option under consideration;
- `RECOMMENDED` for a preferred but unapproved option;
- `ACCEPTED` only for explicit owner-approved direction;
- `FROZEN` only when explicitly protected from routine change;
- `DEPRECATED` for superseded decisions retained as history.

Do not rewrite or remove a superseded decision. Add a new decision record, mark the earlier one `DEPRECATED` when authorized, and cross-reference them.

Updates to `docs/01-project-status.md`, `docs/02-decision-register.md`, lifecycle status, marketing approval, stage state, pricing, public claims, and named relationships require both evidence and the appropriate authority.

## Make reviewable changes

For significant future changes, prefer a small branch and pull request or another clearly reviewable commit sequence. Each change should:

- address one coherent purpose;
- explain why the change is needed;
- identify the governing decision or policy;
- list assumptions and unresolved questions;
- avoid drive-by restructuring or unrelated formatting;
- preserve stable IDs and historical records;
- update dependent documentation or generated outputs when necessary.

Suggested commit messages describe the outcome, for example:

```text
docs: clarify website readiness evidence
governance: add service gate validation
registry: record proposed capability prerequisite
```

Never force-push or use destructive Git operations on unknown work.

## Public-safe requirement

This is a public repository. Do not contribute secrets, credentials, personal IDs, bank details, private financial records, confidential client information, unapproved names, supplier private contacts, private partner information, sensitive contracts, or commercially confidential terms.

Use `TBD`, `UNKNOWN`, redacted examples, or synthetic data. Move confidential operational material to owner-approved private storage, or obtain an explicit repository-visibility decision before storing it. Follow `SECURITY.md`.

## Validation

Run checks in proportion to the change. When the baseline scripts are present, governance-affecting contributions should run:

```text
python scripts/generate_marketable_services.py
python scripts/test_company_os.py
python scripts/validate_company_os.py
```

Also:

- parse every edited JSON file;
- inspect generated content after authoritative data changes;
- check that no service is public unless `ACTIVE` and owner marketing approval is true;
- confirm future-stage documents still carry the required framework notice;
- review the final diff for unsupported claims and sensitive information.

If a check cannot run, say why. Do not describe unperformed validation as successful.

## Review checklist

A contribution is ready for review when:

- [ ] current stage and active priority remain correct;
- [ ] proposal and acceptance are clearly separated;
- [ ] owner-only decisions have not been inferred;
- [ ] claims are supported by evidence or marked unknown;
- [ ] service lifecycle and publication gates remain intact;
- [ ] public-safety review is complete;
- [ ] relevant validation passes;
- [ ] changed files and remaining questions are documented.

Stage 0 was explicitly accepted under `MPG-DEC-032`, and Stage 1 was separately activated under `MPG-DEC-033`. Stage 2 and every later-stage framework still require their own explicit owner activation decision.
