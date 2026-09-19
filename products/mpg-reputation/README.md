# MPG Reputation — Authoritative Product Direction

| Metadata | Value |
|---|---|
| Product / WIP subject | MPG Reputation / Review & Reputation Automation — `PROD-REP-001` |
| Status | V0.1 TECHNICAL FOUNDATION ACCEPTED; V0.2 CONTROLLED STAGING PROVEN BASELINE; MARKET-READY BUILD PROGRAM AUTHORIZED (MPG-DEC-046) |
| Company stage | Stage 1 active; Stage 2 and all later company stages not activated |
| Owner | MPG Founder |
| Last Updated | 2026-09-19 |
| Public Safe | Yes — synthetic examples only |
| Authority | [Decision register](../../docs/02-decision-register.md): `MPG-DEC-038` through `MPG-DEC-046` |

This is the single authoritative Company OS product-direction document. It consolidates the owner's requirements and identifies recommendations and unresolved decisions. [PRD v0.1](PRD.md) is the owner-authorized implementation baseline under this direction. Neither document is a live offer, evidence of delivery readiness, final commercial model, marketing approval or launch authority.

## Authority and current boundaries

| Matter | Decision status and governing boundary |
|---|---|
| Track | **ACCEPTED**, `MPG-DEC-046`: temporary primary execution focus for a bounded market-ready product-development program. Active productization work on Professional Business Websites is temporarily paused so MPG Reputation can receive primary attention, though Professional Business Websites remains first in the accepted commercial productization sequence (`MPG-DEC-029`). `MPG-DEC-046` supersedes only the execution/WIP allocation portions of prior decisions (`MPG-DEC-008`, `MPG-DEC-020`, `MPG-DEC-038`). |
| Product surface | **ACCEPTED**, `MPG-DEC-039`: a dedicated product website/application may be designed, built, tested and eventually operated without waiting for the future MPG umbrella website. |
| Company website | **ACCEPTED**, `MPG-DEC-040`: Stage 7 remains inactive. No corporate-site design, temporary umbrella site, MPG-wide catalogue, or restructuring of umbrella-site strategy is authorized. |
| Experience principle | **ACCEPTED**, `MPG-DEC-041`: seamless for the business, customer and MPG; automate normal work and surface exceptions. |
| Validation geography | **ACCEPTED**, `MPG-DEC-042`: United States and Canada first; Australian technical compatibility later. |
| Working identity | **ACCEPTED**, `MPG-DEC-043`: MPG → MPG Reputation; subordinate product/system, not a separate unrelated company. No final name/trademark freeze. |
| Implementation baseline | **ACCEPTED**, `MPG-DEC-044`: PRD v0.1, separate repository creation and the first synthetic vertical slice are authorized. No service activation, production messaging or public launch follows. |
| V0.1 technical milestone | **ACCEPTED**, `MPG-DEC-045`: the internal technical foundation and synthetic vertical slice passed engineering acceptance. |
| V0.2 baseline & Market-ready program | **ACCEPTED**, `MPG-DEC-046`: V0.2 controlled staging and founder product-usability validation forms the proven baseline. Market-ready product-development program is owner-authorized across sequential milestones (MR-0 through MR-11). Commercial release remains gated. |
| Development scope | Production engineering, production email architecture, onboarding/activation, universal completion sources, evidence-based integrations, trial/usage controls, commercial-model research, billing architecture/implementation, admin/support tooling, trust/security/privacy controls, product website, free check acquisition experience, independent acquisition pipeline, controlled pilot preparation, and launch readiness are authorized under `MPG-DEC-046`. |
| Commercial release | **NOT AUTHORIZED** by the build decision: no unrestricted solicitation, public launch, real-customer messaging, final prices, blanket legal-compliance claims, service lifecycle `ACTIVE`, or marketing approval. |
| Implementation choices | Stack, providers, trial terms, sequencing and commercial hypotheses below are **RECOMMENDED / VALIDATION REQUIRED**, not immutable decisions or adopted tools. |

The [service registry](../../registry/services.json) records the secondary slot as `ACTIVE` WIP. This means allocated work only; it is not a service lifecycle state. No separate MPG Reputation service record or market approval is asserted. `REP-GOV-002` must establish that record and its evidence before any pilot lifecycle claim or commercial release. Existing service records and the accepted seven-family commercial sequence remain unchanged. Public offers require applicable G1–G13 readiness, owner approval, `lifecycleStatus = ACTIVE` and `marketingApproved = true`.

## Market-Ready Roadmap (MR-0 through MR-11)

Under `MPG-DEC-046`, MPG Reputation is developed independently through a bounded market-ready build program before broad MPG company/brand development resumes.

> [!IMPORTANT]
> Roadmap inclusion authorizes development planning and bounded technical/operational implementation, but DOES NOT imply that each gate is already passed. Real customer messaging, live pilot, commercial release, pricing, legal readiness, and marketing approval remain separately gated.

| Milestone | Title | Focus & Scope | Gate / Prerequisite Before Consequential Action |
|---|---|---|---|
| **MR-0** | Governance Reconciliation | Synchronize Company OS and product repository governance, decisions, status, roadmap, and agent instructions. | **COMPLETE / ACCEPTED BASELINE.** |
| **MR-1** | Production Messaging Core | Resend production email architecture, templates, sender identity, domain authentication, bounce/complaint webhooks, delivery monitoring, and retry hardening. | **ACTIVE MILESTONE (MR-1A in progress).** Synthetic and developer-controlled validation first; LIVE customer messaging remains OFF until separately authorized. SMS gated. |
| **MR-2** | Customer Activation | Business onboarding flow, location setup, verified Google destination confirmation, and activation checklist with actionable recovery states. | Valid destination confirmation required; no automation without confirmed destination. |
| **MR-3** | Completion Source Platform | Universal completion API/webhook with authentication, replay protection, deduplication, and adapter contracts; native CRM connector architecture. | Adapter contracts and verification tests before external system adoption. |
| **MR-4** | Trial / Usage / Economics | Configurable server-side trial entitlement engine (current hypothesis: 30 review requests / 30 days; final structure TBD / validation-required), usage metering ledger, cost attribution models, and COGS validation. | No unlimited usage; evidence-backed cost inputs and owner approval before commercial trial commitments. |
| **MR-5** | Billing | Stripe billing architecture, subscription lifecycles, payment webhooks, checkout flows, customer portal, and invoice accounting. | Final pricing and refund policies must be owner-approved under the pricing framework before enablement. |
| **MR-6** | Admin / Support / Observability | MPG operational tooling, tenant inspection, automation health monitoring, deliverability alerts, exception handling, and audit trails. | Role-based access controls and secure operations; no direct DB tampering for support. |
| **MR-7** | Trust / Security / Compliance | Technical controls supporting applicable US/Canada messaging and privacy requirements, unsubscribe/opt-out durability, suppression sync, consent provenance, RLS audit, and data retention/deletion. | Qualified legal/compliance review before real-customer messaging or public release; technical controls do not replace legal review. |
| **MR-8** | Controlled Pilot | Bounded real-customer pilot with a small, owner-approved cohort, participant safeguards, stop triggers, operational support, and objective evaluation. | Separate owner pilot authorization and participant agreements required; pilot does not pre-decide positive validation. |
| **MR-9** | Product Website / Acquisition Funnel | Independent product website, Free Reputation Check experience, Reputation Opportunity Report generator, and trial onboarding funnel; define appropriate performance and quality targets. | Truthful claims review; publication gate applies before public availability. |
| **MR-10** | Marketing Engine | Acquisition channels, content, campaign infrastructure, and lead tracking for MPG Reputation. | Public solicitation must respect the publication and marketing approval gates. |
| **MR-11** | Market Release | Formal commercial release, public marketing launch, lifecycle advancement to `ACTIVE`, and public customer intake. | Mandatory gates: `lifecycleStatus = ACTIVE`, `marketingApproved = true`, full G1–G13 readiness. |

### Product identity and code ownership

```text
MPG
└── MPG Reputation

mpg-company-os → company governance and product direction
mpg-reputation → future product website/application source code
```

The dedicated site is a **product operating surface**, not the corporate MPG website. It may prominently use MPG Reputation with an appropriate MPG relationship. It does not change BUILD/GROW/CONNECT, activate other divisions/services, or require Trade/CONNECT navigation. The future umbrella website remains a separate later-stage company project and must remain untouched.

The authorized working software repository name is `techwithmpg/mpg-reputation`, with private visibility by default when remote creation is available. `MPG-DEC-044` authorizes establishing it for the first implementation baseline. Production application code does not belong in Company OS. The product website and authenticated application may share that codebase. Development authorization does not require building any part of the main MPG website.

## Purpose, customer and market

MPG Reputation is intended to help businesses consistently request **genuine customer reviews** after legitimate completed transactions, jobs, services, appointments or projects. MPG controls legitimate requests, not customer participation, published reviews or ratings. No number of reviews, positive ratings, revenue gain or ranking improvement is guaranteed.

The prospective buyer is a business owner/operator with completed customer work and a review-request process to improve. The final vertical remains **TBD**; there is no accepted vertical in the current repository. Any future vertical suggestions are research candidates only.

The accepted initial product-validation markets are **United States and Canada**. Architecture should remain compatible with **Australia later**, without treating it as an initial primary validation market. This does not assert local offices, employees, legal entities, validated demand or current market availability. The separate company/website-service market hypotheses remain in [customer and market discovery](../../docs/05-customer-market.md).

```text
COMPLETED CUSTOMER → CUSTOMER ELIGIBILITY → AUTOMATED REVIEW REQUEST
→ EMAIL / SMS → TRACKED REVIEW LINK → GOOGLE REVIEW DESTINATION
→ REVIEW DETECTION → ATTRIBUTION → REPUTATION ANALYTICS → BUSINESS REPORTING
```

This is the intended full product flow. Review detection and outcome attribution depend on permitted data access; a tracked redirect alone does not prove a review was submitted.

## Three-sided seamless experience

**Seamless for the business.** Configure or connect the customer source, correct review destination and communication rules once, where practical. Routine eligible requests should then happen automatically. Adapt to existing business systems without requiring a new full CRM. Target near-zero routine workload after a successful integration; setup and exceptions still need attention.

**Seamless for the customer.** Receive a recognizable request from the business, click one CTA and reach the correct review destination. No MPG account, installation, understanding of internal systems or unnecessary steps. Google-controlled sign-in or review requirements remain outside MPG's control.

**Seamless for MPG.** Automate routine work; manage failed integrations, messaging failures, compliance exceptions, invalid destinations, account problems, unusual usage and support cases. MPG should not manually process normal messages or inspect databases for ordinary support.

> Automate the normal. Surface the exception.

These are architectural targets, not current performance claims. A feature that materially increases routine workload for all three sides requires strong justification and an explicit scope review.

## Acquisition and free reputation check

The proposed product-site funnel, subject to readiness and marketing approval, is:

```text
BUSINESS OWNER → MPG REPUTATION WEBSITE → FREE REPUTATION CHECK
→ REPUTATION OPPORTUNITY REPORT → START FREE TRIAL
→ 30 FREE REVIEW REQUESTS → TRIAL RESULTS → PAID MONTHLY SUBSCRIPTION
```

Use **30 Free Review Requests**. Never advertise **30 Free Reviews**: customer publication is not controlled by MPG.

The future free check may inspect available, permitted information or ask the business about current Google rating, total review count, approximate customer/job volume, current manual/automated request process, customer-management software and major process gaps. Identify user-supplied estimates and unavailable data clearly. Do not fabricate a proprietary reputation score.

The output is a practical **Reputation Opportunity Report** showing observed process gaps, data limits and possible next steps, without unsupported promises. No present public funnel, trial availability, conversion result or live website is claimed.

## Trial recommendation

**RECOMMENDED / VALIDATION HYPOTHESIS:** 30 review requests **or** 30 days, whichever occurs first; **EMAIL-FIRST**.

Email-first is expected to reduce marginal delivery and acquisition cost, simplify activation and speed validation, without provisioning a dedicated SMS number or US A2P/10DLC identity for each non-paying trial. SMS may be part of paid activation later. This is an economic/design rationale, not exemption from email consent, sender identity or unsubscribe obligations.

The PRD must define the trial start event, what consumes a request, failed-send/retry accounting, expiry, and how pending reminders behave at the limit. Meter initial requests separately from reminders and provider message attempts. Enforce limits server-side, with concurrency and replay protection; do not silently extend the trial or infer paid consent. Final trial terms remain subject to validation and owner approval.

## Business onboarding and activation

Recommended flow: establish the organization and location; configure a completion source; connect the Google review destination; configure permitted channel, sender identity and country rules; verify suppression/consent handling; capture an available baseline; perform a controlled test; then enable automation only when all applicable prerequisites pass.

### Connect Your Google Review Profile

This is a required activation step. V1 must let the business paste a direct Google review URL, validate it, test/open it and explicitly confirm that it reaches the correct business/location. Support **one review destination per location**. No review automation becomes active without a valid destination.

Validation must reject malformed, unsupported or unsafe destinations and prevent an arbitrary open redirect; exact allowed Google URL forms and safe validation mechanics belong in the PRD. A business confirmation is not proof that Google API access or review syncing exists.

Later recommendations: Google OAuth, Business Profile selection, location selection and automated review-link retrieval **where API capabilities and permissions permit**. Review the actual API approval, scopes, quotas and data-use terms before implementation. The manual-link route must not depend on future OAuth availability.

Onboarding needs explicit success, user-fixable validation failure, system failure, safe retry and cleanup behavior. Partial setup must remain visibly inactive and resumable. The trusted organization/location configuration is the source of truth; client state cannot enable automation or bypass eligibility.

## Customer ingestion and normalized events

The key normalized event is **`CUSTOMER_COMPLETED`**: a genuine business/customer relationship has reached an appropriate completion state and may now qualify for a review request. Completion is a trigger for eligibility evaluation, not evidence of consent or permission to send. Importing the entire historical customer database is not required.

Collect only purpose-specific data. Candidate fields are organization, location, source system, source customer ID, transaction/job/order ID, customer name, email, phone, completion timestamp, country and communication/consent metadata. Exact required/optional fields belong in the PRD; email-first does not require a phone number. Do not add unrelated historical records or sensitive job details.

All sources must translate through adapters into one canonical internal event/entity model. The automation engine must not contain scattered Jobber-, Housecall-, Square- or other provider-specific assumptions. Normalize identities, country/channel formats, timestamps and consent provenance at the boundary; validate organization/location ownership and reject or quarantine invalid events. Define stable event IDs and deduplication keys so retries cannot create repeated requests.

### Source architecture priority

1. **Native CRM/business integrations:** future evaluation candidates include Jobber, Housecall Pro, ServiceTitan, GoHighLevel, HubSpot, Square and QuickBooks; add others only from validated demand. No connector is claimed to exist.
2. **Universal webhook/API:** external systems may eventually submit authenticated normalized completion events; define verification, tenant routing, replay protection and failure responses.
3. **Completion Inbox:** a unique inbound address such as `completed+business-id@in.mpg-domain.example` may parse supported completion notifications into normalized events. This is a synthetic address, not existing infrastructure. Validate sender/source, tenant routing and parser confidence; surface uncertain data instead of auto-sending from it.
4. **MPG Quick Complete:** a mobile-friendly trigger for businesses without a CRM: Customer Name, Email, Phone optional, and **Complete Customer/Job**. Keep it lightweight; it is not a full CRM or a way to bypass consent checks.
5. **MPG-created websites/business systems:** future systems may emit `CUSTOMER_COMPLETED` natively.
6. **CSV:** migration/fallback only, with preview, validation and deduplication; not the intended recurring workflow or permission to bulk solicit a historical database.

Source priority describes the desired customer experience. MVP implementation starts with Quick Complete and a universal webhook before the first validated native CRM connector, to test the shared pipeline with bounded scope.

## Communication and country policy

**Resend — RECOMMENDED email provider. Twilio — RECOMMENDED SMS provider.** These are tool/provider recommendations, not official MPG partnerships, adopted accounts or implemented integrations. Use internal `EmailProvider` and `SmsProvider` interfaces so vendor changes do not rewrite the domain engine.

### Email identity

V1 recommendation: MPG-managed reputation sending infrastructure/domain, the client business display name and client Reply-To, rather than requiring every client to configure a sending domain. Any illustrative domain, such as `reputation.mpg-domain.example`, is synthetic; no domain ownership is asserted. Evaluate sender authentication, reputation isolation, abuse controls, bounce/complaint webhooks, verified Reply-To ownership and unsubscribe behavior before real sends. Custom client sending domains may be an advanced/premium option later.

### Paid SMS activation

Paid activation may provision a messaging identity, appropriate local-capable number, country-specific registration, messaging service, opt-out handling and delivery/status webhooks. Verify provisioning success before enabling the channel; failures remain actionable exceptions. Sender type, country and use case determine the required review.

US architecture must anticipate A2P 10DLC registration for applicable local-number application messaging; other sender types have their own requirements. See [Twilio's A2P 10DLC guidance](https://www.twilio.com/docs/messaging/compliance/a2p-10dlc), retrieved 2026-09-17. Canada requires review of consent, identification and unsubscribe handling; [CRTC guidance](https://crtc.gc.ca/eng/com500/faq500.htm), retrieved 2026-09-17, describes these requirements for commercial electronic messages. Actual message classification, exceptions and implementation require professional verification. Australia remains technically supportable later, with its policy disabled until reviewed and authorized.

### Country policy engine

Centralize **US POLICY / CA POLICY / AU POLICY**, governing allowed channel, sender type, registration, consent state, opt-out behavior, templates and quiet hours where applicable. Unknown or unacceptable permission state must not be treated as consent. Legal/compliance implementation is unresolved and a required pre-launch review, including email. No blanket compliance claim is authorized.

## Eligibility and automation

```text
CUSTOMER_COMPLETED
→ VALID CONTACT?
→ CHANNEL AVAILABLE?
→ PERMISSION/CONSENT STATE ACCEPTABLE?
→ NOT SUPPRESSED?
→ NOT DUPLICATE?
→ OUTSIDE MINIMUM REPEAT-REQUEST WINDOW?
→ VALID REVIEW DESTINATION?
→ ELIGIBLE
```

Ineligibility must have an auditable reason, with suppression protected from retries or re-imports. Eligibility must never depend on expected satisfaction or rating. **Satisfaction filtering, predicted-rating filtering, positive-only solicitation and review gating are prohibited.** Genuine participation is the objective, not rating manipulation. Google's [Maps contribution policy](https://support.google.com/contributionpolicy/answer/7400114), retrieved 2026-09-17, prohibits selectively soliciting positive reviews; product design must preserve neutral access.

Recommended initial workflow:

```text
CUSTOMER_COMPLETED → WAIT CONFIGURED PERIOD → SEND REVIEW REQUEST → WAIT
                                                               ↓
                                                         LINK CLICKED?
                                                          /         \
                                                        YES         NO
                                                         ↓           ↓
                                                        STOP    ONE REMINDER
                                                                     ↓
                                                                    STOP
```

Initial maximum is **one reminder** per request unless future evidence supports a revised policy. Recheck eligibility, suppression, destination and account/trial limits immediately before every send, including reminders. A click stops the reminder; it does not prove review completion. Opt-out, an invalid destination, revoked permission or a disabled account must stop pending sends. Define retry limits, ambiguous provider acceptance, idempotency, failure queues and reconciliation so a technical retry does not become an extra customer reminder.

## Customer review experience and conversion

```text
MESSAGE → ONE CTA → MPG TRACKING LINK → RECORD CLICK
→ IMMEDIATE REDIRECT → GOOGLE REVIEW PAGE
```

Avoid intermediate screens or forms. Use opaque tracking tokens rather than personal information in URLs, validate destinations and ensure analytics failures do not trap the customer. The PRD must address expired/invalid links, automated email-security scans and the difference between a recorded click and likely human interaction.

Optional private feedback must offer **Leave a Google Review** and **Send Feedback Directly** neutrally. It must not intercept the default direct review path or route people based on satisfaction. **Happy → Google / Unhappy → Private is prohibited.**

A future **Review Conversion Engine** may optimize request timing, channel, reminder delay, message wording, CTA wording and email/SMS order. Changes must improve genuine participation, not selectively solicit positive ratings or weaken consent rules. Staff may appropriately tell customers that a review/feedback request will arrive after completion; no promised reward or positive-rating requirement is implied.

## Review detection, baseline and attribution

Before the first request, capture an available reputation baseline: activation date, total Google reviews, average rating, recent review volume and historical review velocity. Record source, observation time, coverage and unavailable values. If historical data is unavailable, leave it unknown rather than deriving fictitious history from one snapshot.

V1 manual-link onboarding does not provide automatic review detection. Later review sync/notifications depend on approved Google access and supported APIs. Until a permitted source exists, show outcome data as unavailable or clearly label business-supplied observations and their limits; do not substitute click counts for reviews or imply live syncing. Platform access and attribution feasibility must be resolved before promising automated outcome reports.

### Separate activity from outcome

Directly measurable MPG activity: request initiated, message sent, provider delivery status when available, tracked-link click and Google redirect. Provider acceptance is not guaranteed delivery, delivery is not a read, and redirect is not review publication.

Future review classifications:

| Classification | Intended meaning; exact thresholds remain TBD |
|---|---|
| `MPG_ATTRIBUTED` | A review meets a validated evidence threshold for association with an MPG request. This is a methodology-based inference, not proven causation. |
| `MPG_ASSISTED` | Signals suggest MPG involvement but do not meet the stronger attributed threshold. |
| `UNATTRIBUTED_OR_ORGANIC` | Evidence is insufficient to attribute to MPG; the label does not prove an organic cause. |

Potential signals: organization/location match, recent MPG request, successful delivery, tracking-link click, timing proximity, reviewer/customer-name similarity where lawful and technically available, and a unique candidate match. Do not force matches where names are missing, ambiguous, shared or changed. Do not claim every new review was caused by MPG.

Exact scoring, thresholds, lookback windows and confidence calibration are **TBD**, to be validated before authoritative use. Internally retain attribution methodology/version, evidence provenance, observation window and uncertainty. Reclassification must remain auditable and must not double-count outcomes. Data access, privacy and matching accuracy are dependencies, not assumed capabilities.

## Reporting and trial conversion

The future dashboard should distinguish:

| Area | Measures |
|---|---|
| MPG activity | Completed customers processed, eligible customers, requests sent, delivered messages, tracking-link clicks, reminders and opt-outs |
| Review attribution | MPG attributed, MPG assisted, organic/unattributed, with methodology and coverage limits |
| Reputation movement | Review count, average rating, review velocity and recency, compared with an available baseline |

Use evidence-based wording and defined denominators/time windows. Do not claim revenue, ranking gains or other downstream business outcomes without supporting data. Failed or unavailable observations must remain distinguishable from zero results.

At trial end, including an earlier day-limit expiry, show actual measured results and limits. **Synthetic illustration only — not actual MPG performance, a forecast or a guaranteed result:**

```text
30 review requests initiated
29 delivered
14 review links clicked
9 Google reviews observed
7 MPG-attributed
1 MPG-assisted
1 unattributed
```

The illustrative breakdown presumes a validated attribution method and permitted observations. Before those exist, do not show invented classifications. Proposed conversion CTA: **Keep Reputation Automation Running**. Public commercial activation remains gated; the CTA is not current marketing approval.

## Exception management and MPG administration

The future business dashboard should show **AUTOMATION: RUNNING / NO ACTION REQUIRED** only when setup is complete and health checks support that state. Otherwise surface customer-source disconnection, invalid Google link, message failure, missing customer data, high bounce rate, unusual opt-outs, payment problems, reviews requiring response and system failures. Show action, responsible party and recovery state without burying businesses in routine processing details.

The MPG Admin console must provide organization, trial/subscription, integration health, failed automation, messaging usage, provider usage/cost, Google status, email/SMS delivery, opt-out/bounce rate, client usage, support, compliance-alert and overall product-health visibility. Use role-restricted access and audit support actions. Ordinary support must not require direct database inspection. Support scope, response targets and SLA remain unresolved.

## Recommended technical architecture

All selections below are **RECOMMENDED**, pending fit, security, economics, maintenance and owner adoption review. No operating account or production infrastructure is asserted.

| Layer | Recommended direction |
|---|---|
| Frontend/application | Next.js + TypeScript |
| Hosting | Vercel |
| Database/auth | Supabase / PostgreSQL |
| Isolation/security | Organization access control and Row Level Security |
| Backend | Server APIs / Edge Functions as appropriate |
| Automation | Scheduled workers / Supabase Cron or equivalent |
| Email / SMS | Resend through `EmailProvider`; Twilio through `SmsProvider` |
| Monitoring | Sentry or equivalent |
| Google, later | Business Profile APIs and notifications, subject to permission/capability validation |
| Source control | GitHub; Company OS availability does not establish a product repository |

Recommended boundaries: source adapters → canonical completion events → eligibility/country policy → scheduled request workflow → provider interfaces → delivery/click events → review observations → versioned attribution → reporting and usage ledger. Provider callbacks need authentication, idempotency, organization routing and reconciliation. Domain rules must remain independent of vendor payloads.

Candidate internal entities for PRD/data modelling are Organization, Membership, Location, ReviewDestination, SourceConnection, CustomerReference, CompletionEvent, ConsentState, Suppression, ReviewRequest, MessageAttempt, ClickEvent, ReviewObservation, AttributionAssessment, ReputationBaseline, TrialEntitlement, UsageLedgerEntry and OperationalException. This is not a frozen schema; clarify ownership, cardinality, identifiers, constraints, retention and event transitions before implementation.

Existing [capability records](../../registry/capabilities.json), including `CAP-SYS-WORKFLOW-001`, `CAP-SYS-DB-001`, `CAP-SYS-ARCH-001`, `CAP-AUTO-WORKFLOW-001`, `CAP-AUTO-API-001`, `CAP-AUTO-MONITOR-001` and `CAP-TECH-SEC-001`, are relevant assessment inputs, not validated Reputation capabilities. Tool and asset registries remain evidence-based: a recommendation here does not mark a tool approved or an asset available. Map specific dependencies under `REP-ARCH-001` and `REP-GOV-002` before readiness claims.

### Future product routes

```text
/
/reputation-check
/how-it-works
/trial
/pricing
/login
/signup
/privacy
/terms
/app/*
```

These are intended product routes, not implemented pages, live endpoints, a corporate-site sitemap or authority to publish unapproved prices/active-service claims. Privacy and terms need appropriate review before real-data operation.

## Economics and commercial hypotheses

**Pricing: NOT FINAL / VALIDATION REQUIRED.** The discussed approximate **USD $59–$79/month** for an initial single-location product is a market-validation hypothesis only. Final prices require verified COGS, support and onboarding burden, payment costs, comparable market references, willingness to pay, margin logic, risk allowance and owner approval under the [pricing framework](../../docs/07-pricing-commercial-model.md).

```text
MONTHLY SUBSCRIPTION REVENUE
− messaging / SMS
− phone numbers
− registration and compliance-provider charges
− email
− database and hosting
− payment processing
− support and onboarding
− monitoring and other provider costs
= CONTRIBUTION MARGIN under a stated allocation methodology
```

Keep direct contribution and any allocation of shared costs explicit; do not equate contribution with total company profit. Do not reduce the analysis to revenue minus Twilio.

Shared/fixed platform costs include hosting, database baseline, monitoring and email-plan baseline. Variable/client-linked costs include SMS, number rental, A2P/registration, email volume, Google API usage if charged, payment fees and support load. Allocate shared costs transparently and avoid counting included usage twice.

### Dated public provider observations

Retrieved **2026-09-17**, USD public list-price observations only. These are provider facts, not MPG spend, adopted plans, guaranteed future prices or complete production costs; recheck taxes, seats, projects, quotas, overages and terms before commitment.

| Provider | Observation | Authoritative source |
|---|---|---|
| Vercel | Pro listed at $20/month; usage and seat details affect total cost | [Vercel pricing](https://vercel.com/pricing) |
| Supabase | Pro starts at $25/month; projects, compute and usage can add costs | [Supabase pricing](https://supabase.com/pricing) |
| Resend | Pro listed at $20/month for 50,000 emails/month | [Resend pricing](https://resend.com/pricing) |
| Twilio | SMS usage is charged by segment; numbers, carrier and applicable registration charges must also be assessed | [Twilio US SMS pricing](https://www.twilio.com/en-us/sms/pricing/us) |

Detailed private COGS, margins, negotiations and financial data belong in approved private storage. This public document records only the model, public list-price observations and explicitly labelled hypotheses.

### Trial economics

**Synthetic scenario:** 30 initial requests + up to 15 reminders = at most 45 emails **in that scenario**. It is not the system-wide maximum. With one reminder for each of 30 requests, the request/reminder workflow could send **60 emails**; account and other operational email would be additional. Validate the actual reminder pattern and expiry rules.

The working inference is that marginal email cost should be very low compared with provisioning local SMS identities for every non-paying trial. Included plan capacity is not evidence of zero total acquisition cost. Revalidate provider charges, deliverability, abuse, support and onboarding economics before launch.

### Paid usage and internal ledger

Commercial concept only: trial with 30 requests; entry paid plan with a bounded monthly allowance; growth plan with a higher bounded allowance; custom high volume. Exact limits, overages and prices remain **TBD**. Do not approve unlimited SMS or requests initially.

SMS economics vary by country, sender type, number cost, carrier fees, message segments, registration, inbound replies and reminder behavior. Meter segments per organization, use country-aware costs, and monitor provider pricing.

The architecture requires an internal usage ledger for `review_requests`, `emails_sent`, `sms_segments`, `inbound_sms`, `phone_number_months`, `google_api_usage`, `automation_jobs` and `integration_events`. Later add support time, onboarding time, payment fees and refunds. Track usage independently from whether a provider currently charges for it; preserve billable event uniqueness, units, organization, period and cost-source version for customer-level contribution analysis. Exact costing and entitlement rules are PRD work.

## Security, privacy and readiness dependencies

The future product will process customer personal information. Require minimum necessary data, organization isolation, role/access control, encrypted transport, protected secrets, secure OAuth, audit logging, retention rules, customer deletion/export, durable suppression and incident visibility. Deletion and suppression retention must be reconciled through professional review; exact retention periods remain **TBD**.

If Supabase is adopted, enable RLS for exposed tables and define grants plus organization/membership policies; an authenticated session alone must not grant cross-organization access. Keep privileged secrets server-side, restrict support/worker access, and test cross-tenant denial. The [Supabase RLS documentation](https://supabase.com/docs/guides/database/postgres/row-level-security), retrieved 2026-09-17, explains the separate grant and row-policy controls. These are future requirements, not implemented security evidence.

Use synthetic data for design/test examples. No production/customer data, real personal contact details, API keys, provider tokens, credentials, private legal advice or private commercial records belong in this public repository. Follow [information handling](../../operating-model/information-handling.md), [tool adoption](../../operating-model/tool-adoption-policy.md), [public claims](../../operating-model/public-claims-policy.md) and [launch gates](../../operating-model/service-launch-gates.md).

Before real-data pilots, establish lawful data authority, scope, participant safeguards, secure environments, access controls, consent/suppression, a remedy/stop plan, success criteria and capacity. Internal pilot authorization is not evidence that an external/customer pilot is ready. Before public launch, complete applicable service lifecycle/readiness evidence, provider and country review, validated economics, truthful claims, support capacity and explicit owner marketing/activation decisions.

## Recommended MVP build order

| Phase | Ordered work | Exit evidence before dependent work |
|---|---|---|
| Foundation | 1. Separately authorized product repository; 2. skeleton; 3. organization/auth; 4. database; 5. locations; 6. source abstraction; 7. normalized events | Finalized PRD, ownership/access model, isolation and event contracts |
| Reputation Core | 8. Google destination; 9. Quick Complete/manual ingestion; 10. universal webhook; 11. eligibility; 12. email; 13. tracked redirect; 14. suppression/unsubscribe; 15. one reminder; 16. baseline | End-to-end synthetic checks, tenant isolation, deduplication, suppression and delivery failure handling before real sends |
| Trial | 17. usage meter; 18. 30-request and 30-day enforcement; 19. dashboard; 20. result report | Accurate metering, expiry and reporting; unavailable outcomes explicitly identified |
| Integrations | 21. first validated CRM connector; 22. Completion Inbox; 23. integration health | Demand evidence, adapter contract, source verification and recovery checks |
| Paid Messaging | 24. Twilio architecture; 25. SMS; 26. country policy engine; 27. US registration workflow; 28. Canada messaging workflow | Reviewed identity, consent, opt-outs, country costs and approvals before enabling SMS |
| Google Advanced | 29. Google OAuth; 30. review sync; 31. notifications; 32. attribution engine; 33. response workflow | Approved API access, lawful observation/matching and validated attribution methodology |

These are build ordering recommendations, not permission to defer foundational safety: initial email also needs country-policy/consent controls; suppression must be operational before any real email; the later paid phase expands those controls. Reporting must not promise automated outcomes before the Google/attribution prerequisites exist.

## Bounded backlog and deferred scope

The single execution/readiness backlog is the **`REP-*` section in [Company OS Backlog](../../docs/19-backlog.md#mpg-reputation-secondary-incubationbuild-backlog)**. It is separate from the unchanged authoritative `WEB-*` audit. Categories are GOV, PRD, ECON, LEGAL, ARCH, DATA, UX, MSG, INT, GOOGLE, ATTR, REPORT, PILOT and LAUNCH. A listed task does not independently approve spend, legal claims, a pilot, launch or another WIP track.

Do not build first: full CRM, mobile-native apps, HighLevel clone, drag-and-drop workflow builder, dozens of integrations, automatic AI review replies, white-label agency platform, advanced reseller system, unlimited messaging, complex marketing platform, microservices/Kubernetes or the full MPG umbrella website. These remain explicitly deferred; the umbrella website stays in its separate Stage 7 project, not a Reputation deliverable.

## Open questions and next action

Unresolved: final vertical; final product name/brand freeze and trademark review; final monthly price; final usage allowances; overages; annual billing; payment provider; taxes; exact legal structure; final US/Canada compliance implementation; exact retention periods; exact attribution algorithm; first native CRM integration; customer-support model; SLA; final provider selection; production infrastructure; pilot eligibility; marketing approval; launch date. Also finalize trial counting/expiry rules, Google data availability, measurable pilot success criteria and resource budgets before dependent implementation or commitments.

Material risks: founder bandwidth and two concurrent tracks, messaging compliance, customer-data privacy, provider/API dependency, premature launch, uncontrolled integration scope, unvalidated economics and false certainty in attribution. The [current project status](../../docs/01-project-status.md#risks) records the controls; these risks are not accepted as resolved.

**Next action:** Execute MR-1 Production Messaging Core (MR-1A Transport + Provider Event Foundation active) under `MPG-DEC-046`. The V0.1 technical foundation remains ACCEPTED and V0.2 controlled staging / founder usability validation forms the proven baseline. Company OS remains the governance source of truth; commercial, pilot, live customer messaging, pricing, legal, and launch gates remain strictly closed until separately authorized.
