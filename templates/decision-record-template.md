# Decision Record Template

> **Document:** Decision Record Template
> **Template Status:** CONTROLLED TEMPLATE
> **Stage:** Stage 0 — Governance and Source of Truth
> **Template Owner:** MPG Founder
> **Last Updated:** 2026-08-28
> **Public Safe:** Yes while blank; classify completed decisions
> **Authority:** MPG source-of-truth hierarchy and decision-state rules

## Decision rule

A recommendation is not an accepted decision. Record evidence, authority, and state explicitly; unknown facts remain unknown. Preserve superseded records rather than rewriting history.

## Record control

| Field | Entry |
|---|---|
| Decision ID / title | `[DEC-NNN / precise decision]` |
| Domain / affected IDs | `[Stage, service, capability, tool, partner, risk, document]` |
| Decision owner | `[Accountable function]` |
| Proposed by / date | `[Function / YYYY-MM-DD]` |
| Decision state | `[PROPOSED / RECOMMENDED / ACCEPTED / FROZEN / DEPRECATED]` |
| Authority/source | `[Explicit owner instruction, accepted repository record, etc.]` |
| Effective date or trigger | `[Condition; not arbitrary if unknown]` |
| Review trigger | `[Evidence/change that reopens review]` |
| Public-safe? | `[Yes/No; approved private location if No]` |

## Authority check

Use the hierarchy in order:

1. latest explicit owner decision;
2. latest `ACCEPTED` or `FROZEN` repository documentation;
3. current project context;
4. individual chat/history.

- **Higher-authority records checked:** `[IDs/dates]`
- **Possible conflict:** `[Conflict and why, or NONE]`
- **Frozen decision affected:** `[ID or NONE — do not proceed silently]`
- **Authority to accept/freeze/deprecate:** `[Role and accepted delegation record]`

## Decision question

`[One question with a concrete choice, boundary, and decision consequence]`

## Context and constraints

- **Current verified state:** `[Facts and evidence references]`
- **Problem/opportunity:** `[Why a decision is needed now]`
- **Non-negotiable constraints:** `[Stage, WIP, capability, legal, budget, public-safety, client commitments]`
- **Unknowns:** `[Unknown + owner + next action]`
- **Decision deadline/trigger and consequence of delay:** `[Evidence-based]`

## Options considered

| Option | Benefits supported by evidence | Costs/risks/dependencies | Reversibility | Why select/reject/defer |
|---|---|---|---|---|
| A — `[Option]` | `[Evidence]` | `[Evidence/unknowns]` | `[Assessment]` | `[Rationale]` |
| B — `[Option]` | | | | |
| Do nothing/defer | | | | |

## Recommendation

- **Recommended option:** `[Option]`
- **Evidence-based rationale:** `[Why this best fits the constraints]`
- **Trade-offs accepted:** `[What MPG gives up or risks]`
- **Conditions before implementation:** `[Actions/evidence/owners]`
- **Dissent or unresolved concern:** `[Record accurately or NONE]`

This section may remain `RECOMMENDED`; do not word it as already accepted.

## Accepted decision

Complete only when an authorized decision is explicit.

- **Decision:** `[Exact chosen rule/action and scope]`
- **State:** `[ACCEPTED / FROZEN / DEPRECATED]`
- **Conditions/exceptions:** `[Boundaries]`
- **Rejected interpretations:** `[What this decision does not authorize]`
- **Decided by / date:** `[Authority / YYYY-MM-DD]`
- **Evidence of decision:** `[Public-safe repository reference]`

`FROZEN` requires explicit owner intent. Silence, document generation, implementation work, or AI inference is not acceptance.

## Consequences and implementation

| Required change | Owner | Dependency | Completion evidence | Status |
|---|---|---|---|---|
| `[Registry/document/process/content update]` | `[Function]` | `[ID]` | `[Reference]` | `[Open/Done]` |

- **Lifecycle/WIP/marketing effect:** `[Exact effect; no implied service activation]`
- **Clients/partners/tools/information affected:** `[Impact]`
- **Risks created/changed:** `[Risk IDs]`
- **Communications required:** `[Audience, approved wording, permission]`

## Supersession history

| Prior decision | Relationship | Preserved rationale | New status/date |
|---|---|---|---|
| `[ID]` | `[Supersedes/amends/does not conflict]` | `[Reference]` | `[DEPRECATED/etc.]` |

Do not delete the prior decision. Link both directions and update the decision register.
