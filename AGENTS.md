# Instructions for AI and Development Agents

| Metadata | Value |
|---|---|
| Document | Repository-wide agent instructions |
| Status | ACTIVE |
| Stage | Stage 1 — Company and Brand Foundation |
| Owner | MPG Founder |
| Last Updated | 2026-08-28 |
| Public Safe | Yes |
| Authority | Mandatory repository instruction subject to the source-of-truth hierarchy |

These instructions apply to Codex, ChatGPT, Antigravity, Claude, Gemini, automated development tools, and all future agents working anywhere in this repository. A more specific `AGENTS.md` may add local constraints but may not weaken these rules.

## Mission

Help MPG build a durable, truthful, capability-gated company operating system. Optimize for reliable delivery, evidence, focus, traceability, and public safety—not the appearance of scale.

**Stage 0 — Governance and Source of Truth** is the accepted governance baseline. **Stage 1 — Company and Brand Foundation** is the current active development stage under `MPG-DEC-033`. The current commercial priority remains **Professional Business Websites**. Agents may work within approved Stage 1 scope, but must not begin Stage 2 or activate a service without separate explicit owner authorization and the required evidence.

## Mandatory reading order

Before substantial work, read:

1. `README.md`
2. `docs/01-project-status.md`
3. `docs/02-decision-register.md`
4. Relevant domain documentation
5. Applicable `operating-model/` policy
6. Applicable `registry/` data

Also inspect the current Git status and existing files in the work area. If a document is marked `FROZEN`, do not change it without an explicit owner decision. If evidence or authority conflicts, stop the conflicting edit and report it.

## Authority hierarchy

Resolve conflicts in this order:

1. Latest explicit owner decision
2. Latest `ACCEPTED` or `FROZEN` repository documentation
3. Current project context
4. Individual chat or conversation history

Chat alone is not durable authority. Record accepted decisions in `docs/02-decision-register.md` when authorized.

Use decision states precisely:

- `PROPOSED` — an option offered for consideration;
- `RECOMMENDED` — a preferred option, not yet approved;
- `ACCEPTED` — explicitly approved direction;
- `FROZEN` — explicitly protected from routine change;
- `DEPRECATED` — retained history that no longer governs.

Never silently convert `PROPOSED` or `RECOMMENDED` content into `ACCEPTED` content. Preserve superseded decisions and link the replacement instead of deleting the record.

## Non-negotiable operating rules

### Tell the truth

Never fabricate or imply unsupported:

- customers, testimonials, revenue, results, or metrics;
- team members, offices, locations, infrastructure, or years of experience;
- skills, certifications, licences, legal compliance, or professional status;
- partners, suppliers, relationships, approvals, or available accounts;
- prices, margins, capacity, assets, tools, or completed processes.

Use `UNKNOWN`, `TBD`, an empty collection, or an explicit proposal when evidence is missing. Evidence over hype is mandatory.

### Protect the founder/company distinction

- Malcom Gwanmesia represents founder leadership, trust, expertise, learning, thinking, and relationships.
- MPG represents company systems, offers, processes, delivery, and commercial operations.

Do not turn broad founder learning into a list of company services or unsupported personal expertise claims.

### Protect focus

MPG productizes one major new service family at a time by default. The primary track is Professional Business Websites. At most one meaningful secondary learning/incubation track may run concurrently, and the current secondary track is `UNALLOCATED / owner decision required`.

Do not introduce unrelated scope or advance parked work. Learning, purchasing a tool, or identifying a partner does not authorize productization.

### Protect the service gate

The service lifecycle is:

`IDEA`, `RESEARCH`, `PLANNED`, `PREREQUISITES_REQUIRED`, `BUILDING_CAPABILITY`, `INTERNAL_READY`, `PILOT_READY`, `PILOTING`, `DELIVERY_READY`, `MARKET_APPROVED`, `ACTIVE`, `PAUSED`, `RETIRED`.

Do not advance a lifecycle status without evidence and required authorization. Do not infer capability from a course, prototype, subscription, or unverified third party.

A service may be marketed as an active offer only when its authoritative record has:

- `lifecycleStatus = ACTIVE`; **and**
- `marketingApproved = true` through explicit owner authorization.

Both conditions are mandatory. A strategic domain, documentation page, registry entry, roadmap item, or generated catalogue mention does not independently authorize public selling.

### Keep later stages dormant

The owner must accept major stage transitions. Documents for Stage 2 and later must remain frameworks until activation and must use the exact notice:

**STATUS: FRAMEWORK — NOT YET ACTIVATED**

Frameworks may define purpose, questions, inputs, outputs, dependencies, activation gates, and non-assumptions. They must not invent the decisions that their future stage is meant to make. Active Stage 1 work must likewise preserve open questions and may record outputs as `PROPOSED` or `RECOMMENDED` until the owner explicitly accepts them.

## Public-safety rules

Assume all repository content and Git history are public. Do not add:

- passwords, tokens, private keys, API keys, credentials, or secret configuration;
- personal IDs, bank information, private financial statements, or personal contact data;
- confidential client data, unapproved client names, or client credentials;
- supplier private contacts, private partner details, confidential contracts, or commercially sensitive terms;
- raw production data, private logs, or files copied from private systems.

Use redacted, synthetic, or structural examples only. Confidential records belong in approved private storage; if operations require them here, stop and request a visibility/storage decision first. Follow `SECURITY.md` and `operating-model/information-handling.md`.

## Working method

### Before changing files

1. Confirm the current stage and active build track.
2. Read accepted and frozen decisions relevant to the task.
3. Inspect existing content and Git status; upgrade in place rather than creating duplicate sources of truth.
4. Identify the policy and registry records that govern the change.
5. Separate facts from assumptions. Research current external facts when freshness matters and cite authoritative sources where the repository format permits.
6. Check whether the task needs owner authority, especially for stage transitions, decision state changes, lifecycle advancement, marketing approval, pricing, public claims, or partner designation.

### While changing files

- Keep the change small, coherent, reviewable, and within the requested scope.
- Preserve stable IDs and history in registries and decision records.
- Update derived files from authoritative inputs; do not hand-edit generated outputs as if they were sources.
- Use public-safe placeholders such as `TBD` or `UNKNOWN`, never invented facts.
- Make relationships explicit: link the governing decision, policy, readiness evidence, or registry record where practical.
- Do not silently resolve a genuine conflict with a later owner-approved decision.

### Before handing off

1. Read every changed file for contradictions and unsupported claims.
2. Confirm **Stage 0 — Governance and Source of Truth** remains the accepted governance baseline, **Stage 1 — Company and Brand Foundation** remains the current active stage, and Stage 2 remains inactive unless the owner explicitly changes them.
3. Confirm Professional Business Websites remains the first commercial priority unless an accepted decision supersedes it.
4. Confirm no future capability was made active or marketable by implication.
5. Validate JSON and run the repository validator when registries, policies, generators, or publication logic are affected.
6. Regenerate marketable services when authoritative service data changes.
7. Inspect the final diff and Git status.
8. Report changes, validation, open questions, risks, and any authority still required.

## Git safety and auditability

- Never force-push, rewrite history, destructively reset unknown work, or delete legitimate material without explicit scope and justification.
- Do not discard another contributor's uncommitted work.
- Prefer small branches and pull requests, or otherwise clearly reviewable commits, for significant future changes.
- Do not mix unrelated refactors or formatting with governance decisions.
- Do not commit or push unless the task explicitly authorizes it.
- Never bypass validation to make a change appear complete.

## Change-specific authority checks

Explicit owner authorization is required before an agent may:

- accept a major company stage transition;
- mark a decision `ACCEPTED`, `FROZEN`, or `DEPRECATED` unless the owner's instruction clearly establishes that state;
- grant marketing approval or present a service as active;
- claim a partner relationship or disclose a partner publicly;
- publish final pricing, financial targets, legal/compliance claims, or binding terms;
- change the accepted commercial build order or work-in-progress limit.

When authorization is absent, record the matter as `PROPOSED`, `RECOMMENDED`, `UNKNOWN`, `TBD`, backlog, or framework content as appropriate.

## Definition of a good agent contribution

A good contribution makes the repository more truthful, usable, consistent, auditable, and focused. It does not make MPG look more mature than the evidence supports. The public brand must never run ahead of MPG's ability to deliver.
