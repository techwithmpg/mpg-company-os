# MPG Company OS — Decision Register

| Metadata | Value |
|---|---|
| Document | Durable decision register |
| Status | ACTIVE |
| Stage | Stage 0 — Governance and Source of Truth |
| Owner | MPG Founder |
| Last Updated | 2026-08-28 |
| Public Safe | Yes |
| Authority | Authoritative record of explicit owner decisions under the accepted Stage 0 governance baseline |

## How this register works

Decision states are:

- `PROPOSED` — option offered for consideration;
- `RECOMMENDED` — preferred option without final approval;
- `ACCEPTED` — explicitly approved direction;
- `FROZEN` — explicitly protected from routine change;
- `DEPRECATED` — superseded but retained for history.

The entries below are marked `ACCEPTED` only where an explicit owner instruction establishes the decision. None are marked `FROZEN` because no explicit owner instruction has frozen them.

When a decision changes, add a new stable ID, retain the earlier entry, update its state only with owner authority, and cross-reference the replacement. Never erase superseded history.

## Registered decisions

| ID | State | Decision | Constraint or implication |
|---|---|---|---|
| MPG-DEC-001 | ACCEPTED | **MPG is the master company brand.** | Products, divisions, and services remain subordinate to the MPG company architecture unless a later owner decision changes it. |
| MPG-DEC-002 | ACCEPTED | **Malcom Gwanmesia is the founder brand.** | Malcom represents founder leadership, trust, expertise, journey, thinking, and relationships; MPG represents company systems, offers, delivery, and commercial operations. |
| MPG-DEC-003 | ACCEPTED | **Build/Grow/Connect is the current brand architecture.** | MPG Technologies owns BUILD, MPG Media owns GROW, and MPG Trade & Distribution owns CONNECT as strategic capability domains. This does not prove active divisions or services. |
| MPG-DEC-004 | ACCEPTED | **`Build. Grow. Connect.` is a working brand idea, not a frozen final tagline.** | Future brand work may evaluate it; no contributor may describe it as immutable without a later owner decision. |
| MPG-DEC-005 | ACCEPTED | **The website is one business component, not the whole MPG project.** | The Company OS governs the future website. Website delivery must not replace company, service, sales, delivery, or operations governance. |
| MPG-DEC-006 | ACCEPTED | **Commercial capability is developed progressively.** | Strategic inclusion may precede delivery readiness. Learning, tooling, or a potential partner alone does not authorize a service. |
| MPG-DEC-007 | DEPRECATED | **The commercial productization sequence was: Professional Business Websites; Custom Business Systems; AI and Workflow Automation; Digital Marketing; Social Media Management; Trade, Sourcing and Distribution.** | Superseded by `MPG-DEC-029`, which inserts Mobile Applications after Automation. Retained as the original Stage 0 baseline decision. |
| MPG-DEC-008 | ACCEPTED | **Professional Business Websites are the first commercial priority.** | They are the first service family to undergo readiness review. Priority is not `ACTIVE` status or marketing approval. |
| MPG-DEC-009 | ACCEPTED | **Custom Business Systems follow Professional Business Websites.** | Systems remain a future productization family until the applicable stage, evidence, and owner authorization. |
| MPG-DEC-010 | ACCEPTED | **AI and workflow automation follow Custom Business Systems.** | Automation requires a defined problem, reliable workflow, data/security review, fallback, monitoring, error handling, cost clarity, ownership, and maintenance expectations before selling. |
| MPG-DEC-011 | ACCEPTED | **Media capabilities follow later and may activate separately.** | Strategy, creative, copywriting, organic social, paid media, tracking, analytics, SEO, and conversion optimization must not be collapsed into an unsupported full-service claim. |
| MPG-DEC-012 | ACCEPTED | **Trade, sourcing, and distribution are long-term capability areas.** | MPG must not claim to be a freight forwarder, customs broker, licensed importer, manufacturer representative, distributor, or shipping company without evidence and an accurate delivery role. |
| MPG-DEC-013 | ACCEPTED | **GitHub is the durable repository source of truth.** | Accepted decisions belong in the repository; chat history alone is not durable authority. The repository remains public-safe. |
| MPG-DEC-014 | ACCEPTED | **The source hierarchy is: latest explicit owner decision; latest ACCEPTED/FROZEN repository documentation; current project context; individual chat/history.** | Lower sources cannot silently override higher-authority sources. |
| MPG-DEC-015 | ACCEPTED | **Company development uses Stages 0 through 9, and major stage transitions require owner approval.** | Current state remains Stage 0 — Governance and Source of Truth. Creating framework files does not activate Stage 1. |
| MPG-DEC-016 | ACCEPTED | **Evidence over hype governs public and internal claims.** | Do not fabricate customers, testimonials, revenue, staff, offices, locations, relationships, experience, results, certifications, infrastructure, or metrics. |
| MPG-DEC-017 | ACCEPTED | **Undeveloped capabilities cannot be marketed as active.** | Planned or internal capability records may exist without becoming public offers. |
| MPG-DEC-018 | ACCEPTED | **Custom systems are not priced like simple websites.** | Future pricing must account for requirements, complexity, risk, integrations, change load, support, and other service-specific economics; no final prices are set at Stage 0. |
| MPG-DEC-019 | ACCEPTED | **MPG may plan broadly but sells narrowly.** | Long-term diversification is encouraged; premature commercialization is prohibited. |
| MPG-DEC-020 | ACCEPTED | **One primary commercial capability is productized at a time by default.** | At most one meaningful secondary learning/research/incubation track may run alongside it unless the owner explicitly authorizes otherwise. |
| MPG-DEC-021 | ACCEPTED | **Public service publication requires readiness plus owner marketing approval.** | Public marketing requires `lifecycleStatus = ACTIVE` and `marketingApproved = true`; both conditions are mandatory. |
| MPG-DEC-022 | ACCEPTED | **A service uses an explicit delivery mode: OWNED DELIVERY, PARTNER DELIVERY, or HYBRID DELIVERY.** | MPG must disclose roles accurately and must never imply ownership of partner infrastructure. |
| MPG-DEC-023 | ACCEPTED | **Partner-dependent services cannot become active until required partnerships are sufficiently validated.** | A vendor is not an official MPG partner merely because it was researched or contacted. |
| MPG-DEC-024 | ACCEPTED | **MPG should prefer doing fewer things extremely well over offering many things poorly.** | A service launches only when MPG can reliably deliver a defined outcome, not merely because it appears profitable. |
| MPG-DEC-025 | ACCEPTED | **Public communication has three categories: active-offer content, capability-journey content, and thought leadership.** | Only active-offer content may solicit clients, and it requires the publication gate. Journey and thought-leadership language must not imply an unapproved offer. |
| MPG-DEC-026 | ACCEPTED | **The public repository must contain only public-safe information.** | Confidential operations require approved private storage or an explicit repository-visibility and access-control decision before storage. |
| MPG-DEC-027 | ACCEPTED | **MPG Technologies / BUILD includes four internal capability families: Web Development, Business Systems, Automation, and Mobile Applications.** | Internal architecture is broader than active public offers. Inclusion does not validate a capability, allocate WIP, or authorize marketing. |
| MPG-DEC-028 | ACCEPTED | **The founder declares practical capability in Web Development, Business Systems, Automation, and Mobile Applications.** | Owner declaration is recorded separately from evidence maturity. It does not satisfy G2, validate granular skills, prove delivery, or authorize a public capability or service claim. |
| MPG-DEC-029 | ACCEPTED | **The commercial productization sequence is: Professional Business Websites; Custom Business Systems; AI and Workflow Automation; Mobile Applications; Digital Marketing; Social Media Management; Trade, Sourcing and Distribution.** | This replaces `MPG-DEC-007`. It governs company productization, not founder learning; Professional Business Websites remains the sole primary track and the secondary slot remains unallocated. |
| MPG-DEC-030 | ACCEPTED | **Brand & Content is a future MPG Media / GROW capability area.** | It may address genuine brand and content dependencies discovered in future projects, but it is not an active service, current WIP, or automatic component of website work. |
| MPG-DEC-031 | ACCEPTED | **Client Project Readiness & Dependency Detection is a future Company OS backlog requirement.** | It will distinguish client-specific prerequisites from MPG service readiness and classify dependencies as `REQUIRED`, `RECOMMENDED`, or `OPTIONAL`; implementation remains deferred to later authorized stages. |
| MPG-DEC-032 | ACCEPTED | **Stage 0 — Governance and Source of Truth is accepted as the governing baseline for the MPG Company OS.** | Acceptance closes the Stage 0 governance gate. Stage 1 remains inactive and requires a separate explicit owner activation decision. This decision does not activate services, approve marketing, validate capabilities, set pricing, allocate new WIP, or override readiness controls. |
| MPG-DEC-033 | ACCEPTED | **Stage 1 — Company and Brand Foundation is activated under the accepted Stage 0 governance baseline.** | Stage 1 is the active company-development stage. Stage 0 remains the accepted governance baseline; Stage 2 and all later stages remain inactive. This decision does not activate services, approve marketing, validate capabilities, set final service pricing, allocate a secondary productization track, or override readiness, lifecycle, evidence, publication, WIP, public-safety, or decision controls. |
| MPG-DEC-034 | ACCEPTED | **MPG's Company Intent is to build a sustainable, internationally capable company that solves practical business problems, develops long-term client relationships, builds project-based and recurring income, creates employment as it grows, strengthens delivery capability and repeatable systems, and eventually connects opportunities between businesses and markets.** | Expansion across BUILD, GROW, and CONNECT must follow evidence and real delivery readiness. The intent is future-facing and does not claim current recurring clients, employees, international operations, trade capability, infrastructure, or partners. Growth must preserve honesty, relationships, human values, quality, and financial resilience. |
| MPG-DEC-035 | ACCEPTED | **MPG exists to help businesses solve practical problems, save time, and move forward with greater confidence through thoughtful technology, commercial understanding, and dependable human service.** | This Company Purpose guides company and brand decisions but does not establish an active service, guaranteed outcome, final positioning, or marketing approval. |
| MPG-DEC-036 | ACCEPTED | **MPG's Company Vision is to become a trusted international company with recurring client relationships, strong delivery capability, and a growing team—creating technology, growth, and commercial solutions while developing meaningful connections between businesses and markets across Africa, Asia, and beyond.** | This is an intended future state, not a current operating claim. MPG should become financially sustainable enough to provide reliable owner compensation, create employment, meet operating obligations, maintain resilience, and reinvest responsibly. Private household details and exact private income milestones remain outside the public repository. |
| MPG-DEC-037 | ACCEPTED | **MPG's Brand Beliefs are: Understand Before Recommending; Truth Before Hype; Solve What Matters; Relationships Over Short-Term Gain; Dependability by Design; and Ambition with Discipline.** | The beliefs govern observable decisions and behaviour across BUILD, GROW, and CONNECT. They do not create unlimited client scope, require unsustainable concessions, guarantee outcomes outside MPG's control, activate a service, validate capability, finalize a tagline, or grant marketing approval. |

## Decision dependencies

- `MPG-DEC-008`, `020`, and `029` govern current work prioritization; `MPG-DEC-007` is retained only as superseded history.
- `MPG-DEC-006`, `016`, `017`, `021`, `022`, and `023` govern service readiness and public claims.
- `MPG-DEC-001` through `004`, `027`, `028`, and `030` govern brand architecture, capability architecture, and founder/company language.
- `MPG-DEC-013` through `015` govern repository authority and stage transitions.
- `MPG-DEC-031` governs the deferred Client Project Readiness requirement without activating its implementation.
- `MPG-DEC-032` closes the Stage 0 acceptance gate while preserving the separate Stage 1 activation requirement.
- `MPG-DEC-033` satisfies that separate Stage 1 activation requirement while preserving the separate Stage 2 gate and all commercial controls.
- `MPG-DEC-034` through `037` establish the accepted Stage 1 company intent, purpose, vision, economic principle, and behavioural brand foundation without completing Stage 1.

## Superseded decisions

| Deprecated decision | Replacement | Reason |
|---|---|---|
| `MPG-DEC-007` | `MPG-DEC-029` | The owner added Mobile Applications between Automation and Media in the accepted commercial productization sequence. |

## Pending owner decisions

The following remain unresolved and are **not** accepted decisions:

- secondary capability-development track;
- Stage 1 completion/acceptance and Stage 2 activation;
- final tagline and remaining detailed brand strategy outputs;
- priority customer segment and geography;
- final service scope, pricing, capacity, and delivery model;
- any service lifecycle advancement to `ACTIVE`;
- any marketing approval or named partner relationship; and
- implementation or activation of Client Project Readiness & Dependency Detection.
