# Company OS Backlog

**STATUS: FRAMEWORK — NOT YET ACTIVATED**

**Bounded exception:** MPG Reputation secondary incubation/build work is authorized under `MPG-DEC-038`; its separate `REP-*` backlog below does not activate this framework as a whole or any later company stage.

- **Document:** Company OS Backlog
- **Stage:** Cross-stage planning; current active company stage is Stage 1
- **Owner:** MPG Founder
- **Last Updated:** 2026-09-18
- **Public Safe:** Yes
- **Authority:** Framework and readiness questions; `REP-*` build scope separately authorized by `MPG-DEC-038`. Inclusion alone does not authorize execution, spend or release.

## Purpose

Maintain a public-safe, decision-oriented backlog for authorized future-stage work. The first concrete readiness audit is Professional Business Websites, MPG's current commercial priority and primary productization track. Every website readiness item below remains NOT_ASSESSED until evidence and an owner decision are recorded; no item launches or prices the service. The separately authorized Reputation backlog has explicit item statuses.

## Questions This Stage Must Answer

### Professional Business Websites readiness audit

| ID | Gate | Readiness Question | Evidence or Decision Required |
|---|---|---|---|
| WEB-001 | G1 Customer Need | Which exact customer segments and business problems will the first offer serve? | Dated customer evidence and owner-approved segment |
| WEB-002 | G1 Customer Need | Which website outcomes matter to those customers, and what is outside MPG's control? | Problem and outcome definition with claim limits |
| WEB-003 | G1 / G5 | Which website types will MPG accept, defer, refer, or reject? | In-scope and out-of-scope matrix |
| WEB-004 | G2 Capability | Which discovery, UX or UI, content, development, deployment, domain or DNS, security, QA, and support skills are required and validated? | Capability records with evidence and gaps |
| WEB-005 | G11 Proof | What portfolio artifacts, demos, completed work, or pilot evidence may be shown publicly? | Evidence inventory, quality review, and permissions |
| WEB-006 | G3 Tools | What technical delivery approach fits the approved scope and can MPG maintain reliably? | Options assessment and owner decision |
| WEB-007 | G3 / G4 | Which environments, accounts, reusable components, templates, devices, and licenses are required and available? | Tool and asset readiness records |
| WEB-008 | G5 Delivery | What discovery and requirements process will produce a testable scope baseline? | Service-specific workflow and templates |
| WEB-009 | G5 / G8 | How will the design process work, including references, wireframes, prototypes, review, and approval? | Design workflow, roles, and approval criteria |
| WEB-010 | G5 / G8 | Who is responsible for copy, images, brand assets, legal text, product data, and timely content approval? | Content responsibility matrix and client-input rules |
| WEB-011 | G5 / G9 | Who owns and administers the domain, DNS, hosting, email-impacting records, analytics, and third-party accounts? | Ownership, access, authorization, and handover model |
| WEB-012 | G5 / G13 | What technical, on-page, or local SEO work is included, excluded, referred, or separately assessed? | Narrow SEO scope and truthful claim rules |
| WEB-013 | G5 / G7 | What counts as an included revision, defect, clarification, or chargeable change? | Revision and change-request policy |
| WEB-014 | G5 / G10 | How will delivery time be estimated, paused, re-baselined, and protected from missing client inputs? | Estimation method, dependency rules, and capacity evidence |
| WEB-015 | G6 Quality | Which functional, responsive, browser, content, accessibility, performance, security, form, analytics, metadata, and link checks apply? | Website QA checklist and acceptance thresholds |
| WEB-016 | G6 Quality | What backup, deployment, rollback, approval, and production verification controls are required? | Release and rollback procedure with test evidence |
| WEB-017 | G7 Commercial | What verified effort, cost floor, complexity, risk, revision, third-party, support, margin, fee, tax, and currency inputs shape pricing? | Pricing-method record; no invented numbers |
| WEB-018 | G7 Commercial | Is a project minimum appropriate, and what evidence would justify it? | Owner decision based on cost, capacity, and market evidence |
| WEB-019 | G7 / G8 | What payment, cancellation, delay, refund, quote-expiry, and project-start conditions are sustainable and lawful? | Professionally reviewed commercial rules |
| WEB-020 | G8 Client Experience | What onboarding materials, communications, milestones, approvals, and escalation path will clients receive? | Client journey and communication standard |
| WEB-021 | G8 Client Experience | What deployment, documentation, ownership transfer, credential transfer, handover, and training are required? | Handover checklist and private access-transfer method |
| WEB-022 | G5 / G7 / G8 | Are hosting, maintenance, updates, backups, incident response, and post-launch support offered, excluded, or partner-dependent? | Service boundaries, capacity, economics, and support SOP |
| WEB-023 | G9 Risk | What contract, privacy, data, accessibility, intellectual-property, licensing, cookie, consumer, tax, and jurisdiction questions require qualified review? | Risk review and applicable professional advice |
| WEB-024 | G10 Capacity | How many projects and support obligations can MPG fulfill without reducing quality or compromising existing clients? | Capacity model and stop-selling trigger |
| WEB-025 | G12 Partner | Which specialist tasks, if any, require a partner and has each required partner passed governance? | Delivery-mode decision and approved partner evidence |
| WEB-026 | G13 Marketing | What audience, offer wording, proof, limitations, call to action, and enquiry capacity support truthful publication? | Marketing-readiness record |
| WEB-027 | Publication Gate | Do all required gates pass, does the owner approve marketing, and does authoritative data enforce lifecycleStatus = ACTIVE plus marketingApproved = true? | Signed readiness decision, valid registry record, validator pass, and generated-catalogue review |

## MPG Reputation secondary incubation/build backlog

**OWNER-AUTHORIZED SECONDARY BUILD SCOPE — NOT COMMERCIAL RELEASE**

Authority: `MPG-DEC-038` through `MPG-DEC-045`. Product/WIP subject: `PROD-REP-001`. The [authoritative product direction](../products/mpg-reputation/README.md) and [PRD v0.1](../products/mpg-reputation/PRD.md) own requirements and the implementation baseline; this section owns task status and closure evidence. These `REP-*` IDs do not alter or duplicate the `WEB-001` through `WEB-027` audit above. The MPG Founder is accountable for prioritization and acceptance; no staffing or budget is inferred.

`RECORDED` means governance direction exists, not product readiness. `VERIFIED` means a bounded internal technical closure has passed its recorded engineering checks; it does not imply pilot, delivery, market or legal readiness. `IN_PROGRESS` means active work remains inside the authorized boundary. `TODO` means work is within the authorized development boundary but not completed. `GATED` means dependent evidence or separate authorization is required before the consequential action. `DEFERRED` means excluded from the first build. No row advances a service lifecycle or approves public solicitation.

| ID | Category | Status | Bounded deliverable / closure evidence | Dependencies or gate |
|---|---|---|---|---|
| REP-GOV-001 | GOV | RECORDED | Owner decisions `MPG-DEC-038`–`045`, product direction and secondary WIP allocation linked and consistent | Preserve Stage 1, website primary, one secondary and dormant umbrella site |
| REP-GOV-002 | GOV | TODO | Define bounded product service record, lifecycle evidence and mappings to relevant capabilities/tools/assets; no unsupported readiness claims | PRD scope; G1–G13 and lifecycle policy before pilot/release claims |
| REP-GOV-003 | GOV | RECORDED | Separate product-repository creation and first implementation baseline authorized by `MPG-DEC-044`; establish local repository and private remote where safely available | Keep Company OS as governance; no public release or production customer messaging |
| REP-PRD-001 | PRD | RECORDED | Owner-authorized [PRD v0.1](../products/mpg-reputation/PRD.md) defines the bounded vertical slice, security, test and failure requirements | Final vertical, trial terms, commercial terms and later-product requirements remain unresolved |
| REP-ECON-001 | ECON | TODO | Verify full fixed/variable cost model, support/onboarding effort, segment/number/registration costs, market references, willingness to pay and risk allowance | Dated provider sources; private COGS/margins in approved storage |
| REP-ECON-002 | ECON | GATED | Owner-approved bounded usage, monthly pricing, overages, billing/payment/refund/tax rules supported by evidence | REP-ECON-001; professional review; $59–$79 is hypothesis only |
| REP-LEGAL-001 | LEGAL | GATED | Qualified US/Canada messaging/privacy and Google-policy review; retention, export/deletion, suppression, identity, consent, quiet-hours and terms decisions | Before real-data/customer messaging or public launch as applicable; AU compatibility is not AU launch authority |
| REP-ARCH-001 | ARCH | IN_PROGRESS | Implement and verify the PRD boundaries, provider/adaptor contracts, event flow, deployment/monitoring options, retries, failure recovery and resource assessment in the product repository | REP-PRD-001 recorded; production providers/infrastructure remain unadopted |
| REP-DATA-001 | DATA | TODO | Organization/location model, normalized completion events, minimal contacts/consent, requests, suppression, observations, versioned attribution and usage ledger | REP-ARCH-001; explicit ownership, idempotency, access and retention contracts |
| REP-UX-001 | UX | TODO | Business onboarding/Google confirmation, direct customer CTA, neutral private feedback and exception-based admin flows with validation/failure/recovery states | No forced CRM or customer MPG account; no review gating; accessibility criteria |
| REP-MSG-001 | MSG | TODO | Email-first provider interface, sender/Reply-To model, delivery/bounce/unsubscribe processing, tracked link and one-reminder workflow | Synthetic end-to-end tests first; permission, suppression, destination and trial gates before actual sends |
| REP-MSG-002 | MSG | GATED | Paid SMS interface/provisioning, local-capable identity, segments, inbound/opt-out/status handling and country policy including applicable US A2P 10DLC | REP-LEGAL-001, REP-ECON-001, provider adoption and registration evidence |
| REP-INT-001 | INT | TODO | Quick Complete and universal webhook feeding the same canonical pipeline; authentication, replay and duplicate tests | REP-DATA-001; no historical database dependency |
| REP-INT-002 | INT | GATED | One demand-validated native connector, then supported Completion Inbox parsing and integration-health recovery | REP-INT-001, access/terms and customer-source validation; first CRM remains TBD |
| REP-GOOGLE-001 | GOOGLE | TODO | Per-location direct review URL validation, test/open and business confirmation; block automation without valid destination; baseline with data limits | Exact safe URL handling and permitted observation source in PRD |
| REP-GOOGLE-002 | GOOGLE | GATED | OAuth/profile/location selection, link retrieval where supported, permitted review sync/notifications and response workflow | API access/permissions/quotas, security and privacy checks; no existing integration asserted |
| REP-ATTR-001 | ATTR | TODO | Validate attribution signals, thresholds, time windows, uncertainty and method versioning for three outcome classes | Permitted review observations and privacy review; clicks alone cannot prove reviews or causation |
| REP-REPORT-001 | REPORT | TODO | Distinct activity, attribution and reputation movement; baseline, missing-data handling, trial result report and admin health/cost views | Defined metrics/denominators; no invented results; attribution conditional on REP-ATTR-001 |
| REP-PILOT-001 | PILOT | GATED | Synthetic internal validation, then approved bounded pilot plan, eligibility, safeguards, success/failure metrics, capacity, remedy and stop conditions | Internal pilots are within build authority; real-data/customer pilots require readiness and participant safeguards |
| REP-LAUNCH-001 | LAUNCH | GATED | G1–G13 readiness, legal/commercial/support/claims evidence, owner marketing approval and explicit lifecycle activation | No launch date; no release until authoritative service record is ACTIVE with marketingApproved=true |
| REP-PRD-002 | PRD | DEFERRED | Full CRM, native mobile apps, HighLevel clone, drag-and-drop workflow builder, dozens of integrations, automatic AI review replies, white-label agency/reseller platform, unlimited messaging, complex marketing platform, microservices/Kubernetes | Excluded from first build; any later scope needs evidence and WIP review |
| REP-GOV-004 | GOV | DEFERRED | Full MPG umbrella website stays in the separate Stage 7 company project | Not a Reputation prerequisite or deliverable; Stage 7 remains inactive |
| REP-GOV-005 | GOV | VERIFIED | V0.1 internal technical foundation and synthetic vertical slice accepted under `MPG-DEC-045`, supported by the recorded clean database reset, 73 passing tests with zero skips, lint, typecheck and production build | Internal milestone only; no real-customer pilot, production messaging, delivery readiness, legal readiness, marketing or launch authority |
| REP-UX-002 | UX | IN_PROGRESS | Controlled staging and founder product-usability validation: authenticated owner walkthrough, truthful route inventory, business-readable exceptions, responsive critical paths and secret-free owner access instructions | Synthetic data and Console email only; external hosted accounts/credentials may require owner action |

Review the secondary scope at each milestone and before spend, integration or pilot commitments. Pause secondary work when it displaces primary obligations or lacks material capacity, compliance, data or cost controls. No calendar deadline, supplier account, validated capability, production environment or completed implementation is implied.

**Immediate next action:** Establish controlled staging where available and complete founder product-usability validation of the accepted V0.1 workflow. Do not begin a real-customer pilot, production messaging, commercial launch or any deferred integration.


## Client Project Readiness & Dependency Detection

**BACKLOG — NOT CURRENTLY ACTIVE**

**Purpose:** Define a future client-specific readiness layer that asks, “What does this particular client need before MPG can successfully deliver the requested outcome?” This differs from Service Readiness, which asks whether MPG can professionally deliver a defined service. Recording the requirement does not implement an intake, scoring, CRM, quoting, sales, or delivery workflow and must not displace Professional Business Websites productization.

When applicable, future discovery should assess:

- **Brand Readiness:** usable logo, visual identity, positioning, messaging, and consistency;
- **Content Readiness:** photography, website copy, service or product information, team information, visual assets, and content structure;
- **Business Readiness:** objective, decision maker, workflow clarity, requirements, processes, roles, and responsibilities;
- **Technical Readiness:** domain, DNS, hosting, accounts, existing systems, data, integrations, infrastructure, and access; and
- **Compliance Readiness:** only relevant privacy, regulatory, legal-text, data-handling, licensing, accessibility, and other applicable obligations.

Not every project requires every dimension. Each genuine dependency must be classified as:

- `REQUIRED` — necessary for successful delivery of the accepted outcome;
- `RECOMMENDED` — beneficial but not essential to the accepted core outcome; or
- `OPTIONAL` — an elective addition that is not a prerequisite.

### Hidden-work protection

> MPG must not silently absorb unscoped prerequisite work into the price of the originally requested service.

Discovery should expose missing brand assets, photography, copy, content structure, technical access, or other dependencies before final scope and quotation. This protects project economics, founder capacity, client expectations, quality, delivery timing, and scope control. Dependencies must be genuine delivery needs, not a mechanism for unnecessary upselling.

### Project composition

A client's requested service and the eventual project composition may differ. For example, a requested Corporate Website may remain the core component while Brand Foundation, photography/content production, website copy, or domain setup are recorded as required prerequisites; an extended brand system may be recommended; and promotional video may be optional. A future proposal may present one coherent commercial scope while the Company OS tracks the underlying components and classifications separately. No price is set by this concept.

Implementation depends on later authorized customer discovery, service-definition, sales, scope/quotation, delivery, information-handling, and change-control work. Until those stages are explicitly activated, this initiative remains backlog architecture only.

## Backlog governance

- Which items are prerequisites, which can be researched in parallel within the WIP policy, and which must wait for an authorized stage?
- What evidence closes an item, who may accept it, and which source of truth must be updated?
- Which discoveries create a new risk, decision proposal, capability gap, tool assessment, asset requirement, SOP, or partner review?
- Which items should be split, deferred, parked, or removed to protect the primary build track?
- What owner decision is required before the next major stage or service-lifecycle transition?

## Required Inputs

- The accepted Stage 0 governing baseline and any later recorded corrections.
- Current project status, decision register, WIP policy, service lifecycle, and launch gates.
- Professional Business Websites service, capability, tool, asset, partner, and evidence records.
- Customer research, process observations, capacity facts, risk reviews, and qualified professional advice where applicable.
- Explicit owner authorization for work outside the active Stage 1 company and brand foundation scope.

## Required Outputs

- A sequenced readiness plan with dependencies, evidence required, owner function, status, and decision authority for each item.
- Updated registries and decision records when evidence or owner decisions change.
- A service definition, readiness review, pricing method, delivery process, QA checklist, pilot plan, and marketing-readiness record when their stages are authorized.
- A documented list of unresolved blockers and explicit no-go conditions.
- Ultimately, a validated service record and generated public-catalogue result that reflect the owner's decision without manual website overrides.

## Activation Gate

Stage 0 acceptance is recorded under `MPG-DEC-032`, and Stage 1 is active under `MPG-DEC-033`, but those decisions do not activate this cross-stage service-readiness backlog as a whole. Work within authorized Stage 1 company, customer, market, positioning, and brand-foundation scope may proceed. `MPG-DEC-038` separately authorizes the bounded MPG Reputation secondary build scope above; other later-stage backlog work requires its applicable stage or a separate bounded authorization. Professional Business Websites may advance through its lifecycle only on evidence; public marketing requires all applicable gates, explicit owner marketing approval, lifecycleStatus = ACTIVE, and marketingApproved = true.

## Dependencies

- Project status and decision register.
- Service catalogue and all five registries.
- Service lifecycle, launch gates, WIP, quality, risk, partner, public-claims, information-handling, and tool-adoption policies.
- Pricing, sales, delivery, visual, marketing, content, website, automation, operations, SOP, and metrics frameworks as their stages are authorized.

## What Must Not Yet Be Assumed

- No backlog item is complete, scheduled, staffed, funded, or authorized merely because it appears here.
- No customer segment, website type, technology, design process, domain or hosting role, content scope, SEO scope, revision rule, delivery time, maintenance offer, support term, project minimum, price, contract term, or handover method is approved.
- No capability, asset, account, proof, partner, capacity, permission, or professional review is presumed available.
- Professional Business Websites is the first service to undergo readiness work, but it is not automatically ACTIVE or market-approved.
- Stage 1 activation does not activate later-stage backlog implementation or any later company stage.
