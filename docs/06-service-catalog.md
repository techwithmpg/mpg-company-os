# MPG Service Catalogue Framework

| Metadata | Value |
|---|---|
| Document | Service catalogue and priority-service readiness framework |
| Status | FRAMEWORK — NOT YET ACTIVATED |
| Stage | Stage 2 — Services, Offers and Pricing |
| Owner | MPG Founder |
| Last Updated | 2026-09-17 |
| Public Safe | Yes |
| Authority | Framework only; authoritative service state remains in `registry/services.json` |

**STATUS: FRAMEWORK — NOT YET ACTIVATED**

## Purpose

Define how MPG will convert strategic capability areas into bounded, evidence-backed service definitions and maintain a clear separation between the internal strategic catalogue and publicly marketable offers. This file governs the future catalogue structure; the single authoritative detailed readiness backlog for **Professional Business Websites**, the accepted first commercial productization priority, is maintained in `docs/19-backlog.md`.

## Bounded product-build authorization

[MPG Reputation](../products/mpg-reputation/README.md) is authorized under `MPG-DEC-038` through `MPG-DEC-043` as the secondary incubation/build track, independently of the future umbrella website. This does not activate this Stage 2 framework. Its WIP subject `PROD-REP-001` identifies a product initiative, not an active service record. The seven-family commercial sequence and all current service lifecycle/marketing flags remain unchanged. Before any pilot lifecycle claim or commercial release, define the bounded product service record and assess the applicable lifecycle and G1–G13 evidence (`REP-GOV-002`, `REP-PILOT-001`, `REP-LAUNCH-001`).

## Questions the stage must answer

### Catalogue and service-record questions

- What stable service ID, division, name, description, priority, and version identify the service?
- What customer, problem, bounded outcome, inclusions, exclusions, and client responsibilities define it?
- Which canonical lifecycle status and delivery mode accurately describe current evidence?
- Which capabilities, tools, assets, partners, processes, risks, proof, and capacity does the service require?
- How will each G1–G13 readiness result link to evidence, unresolved gaps, an owner, and a review trigger?
- Which SOP, QA checklist, pricing-method status, pilot record, and client-experience controls apply?
- Which facts may be published, which need permission, and which must remain in approved private storage?
- Which lifecycle transition is justified, and what explicit owner authority remains required?
- How will `marketingApproved` and the derived `publiclyMarketable` result remain consistent with lifecycle state?
- How will generated public content remain derived solely from authoritative approved records?
- How will a broad owner capability declaration remain separate from granular evidence maturity and G2 readiness?
- How will future client-project readiness identify genuine prerequisites without silently expanding an offer or encouraging unnecessary upselling?

### Professional Business Websites readiness handoff

- Which items in the authoritative `WEB-001` through `WEB-027` audit in `docs/19-backlog.md` remain unassessed, blocked, in progress, satisfied, or properly not applicable?
- What evidence and owner decisions are required to close those items without starting an unrelated productization track?
- What changes must flow from the backlog into the service, capability, tool, asset, partner, policy, template, and risk records?
- Do the current lifecycle status and publication flags accurately reflect the audit, including the rule that priority or in-development status is never an active offer?

## Required inputs

- The accepted commercial sequence: Professional Business Websites; Custom Business Systems; AI and Workflow Automation; Mobile Applications; Digital Marketing; Social Media Management; Trade, Sourcing and Distribution.
- Current project status, with Professional Business Websites as the primary productization track and MPG Reputation allocated as the secondary incubation/build track under `MPG-DEC-038`.
- Accepted decisions and brand architecture.
- Authoritative service, capability, tool, asset, and public-safe partner registries.
- The authoritative Professional Business Websites readiness backlog in `docs/19-backlog.md`.
- Service lifecycle, capability maturity, launch gates, work-in-progress, public claims, partner, quality, risk, information, and tool-adoption policies.
- Evidence-backed customer and market decisions from the activated earlier stage.
- Current proof, delivery capacity, process maturity, and resource availability records.
- Verified legal, compliance, licensing, privacy, security, insurance, tax, and jurisdiction input where applicable.
- Reusable service-definition, readiness-review, pilot, offer, SOP, risk, and delivery templates.

## Required outputs

- A stable, bounded service definition for every service advanced beyond strategic planning.
- An authoritative lifecycle state, delivery mode, marketing-approval flag, and public-marketability result for each service record.
- Completed readiness reviews that record evidence, unknowns, gaps, owners, dependencies, and required gates.
- Clear service inclusions, exclusions, client responsibilities, change boundaries, QA, acceptance, handover, and support rules.
- Capability, tool, asset, partner, process, risk, capacity, proof, and marketing dependencies linked by stable IDs where available.
- A repeatable pricing method and commercial model without unsupported prices or margins.
- A controlled pilot definition and success evidence where client validation is required.
- An internal strategic catalogue that may include future capabilities without marketing them.
- A generated public catalogue containing only records with `lifecycleStatus = ACTIVE` and `marketingApproved = true`.
- Explicit owner decisions for lifecycle advancement, marketing approval, and any public claims.
- A public-safe record of unresolved website readiness items before the first offer can be considered for market.
- Separation between owner-declared capability, evidence maturity, service readiness, and public-market approval.
- A later-stage Client Project Readiness method that may compose genuine required, recommended, and optional dependencies without treating them as hidden work or automatic upsells.
- Updates to `docs/19-backlog.md` when the authoritative website audit status, evidence requirement, or dependency changes; this catalogue framework must not maintain a duplicate checklist.

Machine-validated registry evidence references use `repo:<relative-path>[#optional-anchor]` for public-safe repository evidence or `private:<public-safe-id>` for evidence held in approved private storage. Release authorization itself must remain inspectable in the repository: `marketApprovalDecision` must point to the governing repository decision, while `readinessReview` and supporting evidence may use either traceable form as permitted by the information-handling policy. Placeholder values such as `NONE`, `TBD`, or `UNKNOWN` never satisfy a release gate.

## Activation gate

- The MPG Founder has explicitly accepted Stage 0 and activated Stage 2 at the appropriate point in the company stage sequence.
- Required Stage 1 customer and brand decisions have been accepted or their absence has been explicitly authorized as a bounded exception.
- The service registry and readiness policies validate successfully.
- Professional Business Websites remains the sole primary productization family unless the owner has recorded a superseding decision.
- Evidence and confidential operational records have approved storage locations and handling rules.
- Activation is recorded in project status before service-framework outputs are treated as current commercial decisions.

Passing an internal readiness review does not itself grant marketing approval. Public release still requires explicit owner authorization, final `ACTIVE` status, and `marketingApproved = true` in the authoritative record.

## Dependencies

- `docs/00-project-charter.md`
- `docs/01-project-status.md`
- `docs/02-decision-register.md`
- `docs/03-brand-architecture.md`
- `docs/04-brand-strategy.md`
- `docs/05-customer-market.md`
- `docs/07-pricing-commercial-model.md`
- `docs/19-backlog.md` — the single authoritative detailed Professional Business Websites readiness backlog
- `operating-model/service-lifecycle.md`
- `operating-model/service-launch-gates.md`
- `operating-model/capability-maturity-model.md`
- `operating-model/work-in-progress-policy.md`
- `operating-model/public-claims-policy.md`
- `operating-model/partner-governance.md`
- `operating-model/quality-standard.md`
- `operating-model/risk-management.md`
- `operating-model/information-handling.md`
- `registry/services.json`, `registry/capabilities.json`, `registry/tools.json`, `registry/assets.json`, and `registry/partners.json`
- Relevant service, readiness, pilot, commercial, delivery, risk, and due-diligence templates

## What must NOT yet be assumed

- That Stage 2 is active merely because Stage 0 is accepted, or that required Stage 1 decisions already exist.
- That a service registry entry is an offer.
- That Professional Business Websites—or any service—is `ACTIVE`, market-approved, priced, validated, or available.
- That priority, `BUILDING_CAPABILITY`, internal readiness, pilot readiness, delivery readiness, or `MARKET_APPROVED` alone authorizes public selling.
- That any service is publicly marketable unless both `lifecycleStatus = ACTIVE` and `marketingApproved = true` are true in the authoritative record.
- That target customers, demand, scope, technology, timeline, revisions, hosting, maintenance, support, pricing, contract, capacity, QA, or handover rules have been decided.
- That founder learning, a completed course, a tool subscription, a demo, or an unverified partner proves professional delivery capability.
- That the founder's owner-declared BUILD capability satisfies G2, validates any granular capability, or proves service readiness.
- That Mobile Applications or Brand & Content is active, current WIP, platform-defined, priced, or market-approved.
- That the deferred Client Project Readiness requirement is an implemented intake, sales, quoting, scoring, or delivery system.
- That MPG owns partner infrastructure or may publicly name a supplier, contractor, freight provider, broker, specialist, or professional adviser.
- That every strategic capability should become one bundled full-service offer or appear on the future website.
- That legal, licensing, regulatory, tax, insurance, privacy, security, accessibility, or compliance requirements have been professionally verified.
- That custom systems should share simple website pricing logic, or that any final price may be invented at this stage.
- That a generated catalogue is an independent source of truth or may override registry data and owner decisions.
