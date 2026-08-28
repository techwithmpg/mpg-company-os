# MPG Company OS

| Metadata | Value |
|---|---|
| Document | Executive repository overview |
| Status | ACTIVE GOVERNANCE — STAGE 0 REVIEW PENDING |
| Stage | Stage 0 — Governance and Source of Truth |
| Owner | MPG Founder |
| Last Updated | 2026-08-28 |
| Public Safe | Yes |
| Authority | Owner-directed Stage 0 baseline; subordinate only to a later explicit owner decision |

MPG Company OS is the durable operating system for building **MPG** into a credible, diversified company without allowing ambition to outrun delivery capability. It records decisions, controls service development, protects focus, and separates strategic possibilities from offers that customers can actually buy.

This is a company repository, not merely a website repository. The website is one future expression of the system; it must eventually publish only services that the system has approved for market.

> MPG plans broadly, builds sequentially, validates capability, and markets only what it can reliably deliver.

## Current state

| Item | Current state |
|---|---|
| Company development stage | **Stage 0 — Governance and Source of Truth** |
| Commercial priority | **Professional Business Websites** |
| Primary build track | Website service productization |
| Secondary learning track | TBD / owner decision |
| Publicly marketable services | Determined only by the service registry and publication gate; never inferred from this README |
| Next gate | Owner review and explicit Stage 0 acceptance |

Stage 1 has **not** begun. No future stage, service, price, customer segment, partnership, capability claim, or marketing claim is activated merely because its framework exists in this repository.

## Company direction

MPG is the master company brand. Its accepted working architecture is:

| Strategic domain | Working pillar | Capability direction |
|---|---|---|
| MPG Technologies | **BUILD** | Web development, business systems, automation, and mobile applications |
| MPG Media | **GROW** | Future Brand & Content, digital marketing, and social media management capability areas |
| MPG Trade & Distribution | **CONNECT** | Sourcing, procurement, representation, import/export coordination, distribution, wholesale sourcing, and logistics coordination through qualified partners |

These are **strategic capability domains**, not proof of active divisions or active commercial services. Each capability must pass the applicable readiness and approval gates before MPG markets it.

`Build. Grow. Connect.` is a **working brand idea**. It is not a frozen or immutable tagline unless the owner later records that decision.

## Founder and company

The system keeps two related identities distinct:

- **Malcom Gwanmesia** is the founder brand: leadership, trust, expertise, journey, thinking, and relationships.
- **MPG** is the company: systems, offers, processes, delivery, and commercial operations.

Founder learning and practical ability can be broad. Company productization must remain narrow and evidence-led. The founder's owner-declared practical capability in Web Development, Business Systems, Automation, and Mobile Applications is recorded separately from evidence maturity; it does not validate granular capabilities or authorize MPG to sell the associated service.

## Capability-gated growth

MPG may plan broadly but must sell narrowly. The accepted commercial build order is:

1. Professional business websites
2. Custom business systems
3. AI and workflow automation
4. Mobile applications
5. Digital marketing
6. Social media management
7. Trade, sourcing, and distribution

This sequence controls **company productization**, not the founder's personal learning. By default, MPG productizes only one major new service family at a time and may run at most one meaningful secondary learning or incubation track unless the owner explicitly authorizes another arrangement.

The quality standard is simple:

> MPG should prefer doing fewer things extremely well over offering many things poorly.

## From idea to market

Services move through a controlled lifecycle:

`IDEA → RESEARCH → PLANNED → PREREQUISITES_REQUIRED → BUILDING_CAPABILITY → INTERNAL_READY → PILOT_READY → PILOTING → DELIVERY_READY → MARKET_APPROVED → ACTIVE → PAUSED / RETIRED`

Status progression requires evidence. A course, demo, tool subscription, or potential supplier does not by itself establish professional delivery readiness.

Before launch, a service is assessed across customer need, capability, tools, assets, delivery process, quality assurance, commercial readiness, client experience, legal/compliance risk, capacity, proof, partner readiness, and marketing readiness.

### Publication gate

A service may be presented as an active offer only when **both** conditions are true in the authoritative service record:

1. `lifecycleStatus = ACTIVE`
2. `marketingApproved = true`

Owner authorization is required for marketing approval. A registry entry, strategic domain, framework document, or generated idea is not an offer. The future website catalogue must be derived only from records that pass this gate.

## Authority and source of truth

When sources conflict, use this order:

1. Latest explicit owner decision
2. Latest `ACCEPTED` or `FROZEN` repository documentation
3. Current project context
4. Individual chat or conversation history

Chat is not durable authority. Accepted decisions must be recorded in the repository. Decision states are `PROPOSED`, `RECOMMENDED`, `ACCEPTED`, `FROZEN`, and `DEPRECATED`; a proposal never becomes accepted silently.

Start with:

- [Project status](docs/01-project-status.md) for the current stage, active work, risks, and next gate.
- [Decision register](docs/02-decision-register.md) for owner-approved direction and decision history.
- [Project charter](docs/00-project-charter.md) for scope, principles, and success conditions.
- [Company OS backlog](docs/19-backlog.md) for the authoritative `WEB-001` through `WEB-027` Professional Business Websites readiness audit and the separately deferred Client Project Readiness requirement.

## Repository map

| Area | Purpose |
|---|---|
| `docs/` | Charter, status, decisions, accepted architecture, and stage frameworks |
| `operating-model/` | Lifecycle, launch gates, focus, claims, partner, quality, risk, information, and tool policies |
| `registry/` | Machine-readable services, capabilities, tools, assets, and public-safe partner records |
| `templates/` | Reusable decision, readiness, delivery, commercial, risk, and due-diligence tools |
| `generated/` | Derived outputs; never an independent source of truth |
| `scripts/` | Governance validation and approved-service generation |
| `brand/`, `sales/`, `marketing/`, `operations/`, `research/` | Domain workspaces governed by the stage and decision system |
| `.github/workflows/` | Automated governance validation |

Framework documents for later stages intentionally contain questions, inputs, outputs, dependencies, and activation gates—not invented decisions.

## Company development stages

| Stage | Purpose | Current? |
|---|---|---|
| 0 | Governance and source of truth | **Yes** |
| 1 | Company and brand foundation | No |
| 2 | Services, offers, and pricing | No |
| 3 | Sales system | No |
| 4 | Delivery and client experience | No |
| 5 | Visual identity and design system | No |
| 6 | Marketing and content engine | No |
| 7 | MPG website | No |
| 8 | Internal operations and automation | No |
| 9 | Launch, measurement, and growth | No |

Every major stage transition requires explicit owner acceptance. Creating a framework does not activate its stage.

## Instructions for AI and development agents

All agents—including Codex, ChatGPT, Antigravity, Claude, Gemini, and future tools—must read [AGENTS.md](AGENTS.md) before substantial work. At minimum they must:

- inspect current status and accepted decisions before changing scope;
- distinguish facts, proposals, recommendations, and accepted decisions;
- preserve frozen decisions and record supersession instead of erasing history;
- respect the one-primary-track work-in-progress limit;
- never promote a planned capability into an active offer;
- avoid fabricated customers, proof, prices, credentials, partners, staff, metrics, or capabilities;
- keep changes small, public-safe, and auditable; and
- validate affected machine-readable records and generated outputs.

## Public repository warning

This repository is public. Treat every tracked file, commit, branch, issue, log excerpt, and generated artifact as public information.

Never store secrets, credentials, personal IDs, bank details, private financial information, private client or supplier data, confidential contracts, unapproved names, private partner contacts, or commercially sensitive records here. Confidential operations must use owner-approved private storage. Repository visibility must be reassessed before confidential operational data is introduced.

See [SECURITY.md](SECURITY.md) and the information-handling policy before adding operational data.

## Governing outcome

The Company OS is not intended to make MPG look large. It is intended to help MPG become strong. Validated skills, tools, assets, processes, economics, capacity, proof, compliance, and partners create deliverable services. Deliverable services plus owner approval create marketable offers. The public brand must never run ahead of MPG's ability to deliver.
