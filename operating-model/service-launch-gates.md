# Service Launch Gates

> **Document:** Service Launch Gates
> **Status:** ACCEPTED — STAGE 0 BASELINE
> **Stage:** Stage 0 — Governance and Source of Truth
> **Owner:** MPG Founder
> **Last Updated:** 2026-08-28
> **Public Safe:** Yes
> **Authority:** MPG Company OS Master Repository Bootstrap v2 and `MPG-DEC-028`

## Purpose

The thirteen gates below provide the minimum evidence review before a service may transition to `MARKET_APPROVED` or `ACTIVE`. A promising idea, a completed course, a successful one-off task, a purchased tool, or an available partner does not satisfy these gates by itself.

Stage 0 remains the accepted governance baseline, and **Stage 1 — Company and Brand Foundation** is active. The first service-readiness audit remains for **Professional Business Websites**; Stage 1 activation and this policy do not price or launch that service.

## Canonical gate states

| Registry state | Review meaning | Launch effect |
|---|---|---|
| `NOT_ASSESSED` | No current assessment supports a conclusion. This is the safe default. | Unresolved; blocks launch. |
| `BLOCKED` | A required criterion is absent, contradicted, materially inadequate, or dependent on an unresolved issue. | Blocks launch. |
| `IN_PROGRESS` | Evidence or remediation work is underway but not complete. | Unresolved; blocks launch. |
| `SATISFIED` | Required criteria are met and supported by current, inspectable evidence. | Eligible, subject to every other gate. |
| `NOT_APPLICABLE` | The gate genuinely does not apply to the defined service scope. | Allowed only with written rationale and reviewer approval. |

Human review language such as “pass” or “fail” must map back to `SATISFIED` or `BLOCKED`; it is not a competing registry vocabulary. `UNKNOWN`, `TBD`, blank fields, and expired evidence cannot produce `SATISFIED`. Every required gate must be `SATISFIED`, or `NOT_APPLICABLE` with defensible rationale, before owner market approval. G12 may be `NOT_APPLICABLE` only where delivery has no material partner dependency.

## Review record

For every gate record: outcome, criterion-by-criterion evidence references, gaps, corrective actions, action owner, due or review condition, reviewer, review date, and expiry/revalidation trigger. Sensitive evidence belongs in approved private storage; only a public-safe reference may appear here.

Registry references use `repo:<relative-path>[#optional-anchor]` for public-safe repository evidence or `private:<public-safe-id>` for evidence retained in approved private storage. The owner market-approval decision must use a repository reference so authorization is auditable. `NONE`, `TBD`, `UNKNOWN`, a missing target, or a path outside this repository is not traceable evidence.

## G1 — Customer Need

**Decision:** Is there a defined customer with a real problem and reasonable evidence of demand?

Required evidence:

- target customer and exclusions are specific enough to qualify work;
- the problem, desired outcome, and current alternative are described without invented facts;
- demand evidence is traceable, such as interviews, qualified enquiries, observed repeated needs, paid pilots, or credible research;
- the offer does not depend solely on founder enthusiasm or a broad market-size claim;
- problem urgency and buying constraints are understood well enough to scope a pilot or offer.

G1 is `BLOCKED` when “everyone” is the customer, the problem is vague, or demand is assumed without evidence.

## G2 — Capability

**Decision:** Can the required work be performed to the promised standard within defined boundaries?

Required evidence:

- all required knowledge and practical skills are mapped to stable capability records;
- each critical direct capability is suitably assessed and `VALIDATED` for the claimed scope;
- a broad owner capability declaration is not substituted for granular assessment evidence;
- any limitations are built into acceptance criteria and exclusions;
- partner-dependent capabilities are identified rather than represented as MPG-owned;
- a course, certificate, tool, or isolated experiment is not used as sole proof of professional delivery.

Unresolved critical capability gaps leave G2 `BLOCKED` or `IN_PROGRESS`. `OWNER_DECLARED_CAPABLE` does not satisfy G2. A partner-supported resolution also requires G12 to be `SATISFIED`.

## G3 — Tools & Technology

**Decision:** Are the necessary tools available, reliable, lawful to use, and economically understood?

Required evidence:

- minimum toolset and technical environment are identified;
- required accounts, subscriptions, licenses, access, and environments are available;
- reliability, security, access ownership, backup, and failure handling are assessed;
- setup, recurring, usage, support, and exit costs are understood;
- data sensitivity and vendor terms are compatible with the service;
- loss of a critical tool has a defined response or contingency.

Popularity or ownership of a tool does not make G3 `SATISFIED`.

## G4 — Assets

**Decision:** Do all non-skill inputs needed for repeatable delivery exist and meet the required standard?

As applicable, verify templates, reusable components, brand materials, test environments, devices, photography, documentation, software licenses, sample deliverables, legal documents, and handover materials. Each required asset must have an owner, availability status, version or location, quality check, and usage rights.

Unknown ownership, missing licenses, or inaccessible critical assets leave G4 `BLOCKED`.

## G5 — Delivery Process

**Decision:** Can another authorized person understand how the service moves from accepted scope to closure?

Required evidence:

- end-to-end workflow and stage owners are defined;
- inclusions, exclusions, assumptions, dependencies, and client responsibilities are explicit;
- an approved SOP or equivalent controlled process exists;
- change requests, decisions, handoffs, delays, exceptions, and escalation are handled;
- owned, partner, and hybrid delivery boundaries are visible;
- records produced at each control point are named.

A sequence that exists only in the founder's memory does not make G5 `SATISFIED`.

## G6 — Quality Assurance

**Decision:** Can MPG determine, before handover, whether the promised output is acceptable?

Required evidence:

- service-specific acceptance criteria and QA checklist exist;
- review roles and independence appropriate to the risk are defined;
- defects, rework, retesting, exceptions, and release authority are controlled;
- accessibility, security, performance, accuracy, or compliance checks are included where relevant;
- quality records are retained safely;
- known defects cannot be silently transferred to the client.

Undefined quality or acceptance standards leave G6 `BLOCKED`.

## G7 — Commercial Readiness

**Decision:** Can MPG quote, contract, and deliver the work on economically defensible terms?

Required evidence:

- repeatable pricing method and cost-based floor exist without arbitrary invented prices;
- labour, third-party, transaction, revision, risk, tax/fee, support, and partner costs are addressed where relevant;
- margin logic and conditions that require re-quotation are defined;
- payment timing, deposits where applicable, cancellation, refunds/remedies, and collections are considered;
- change-request and out-of-scope charging rules exist;
- quote, proposal, and contract responsibilities are aligned.

Unknown material costs or a price copied without analysis leave G7 `BLOCKED`.

## G8 — Client Experience

**Decision:** Does the client have a clear, manageable path from enquiry through support?

Required evidence:

- qualification and discovery process;
- onboarding requirements and readiness checklist;
- communication channels, cadence, response expectations, and escalation;
- approval points and consequences of delayed client input;
- handover, training where required, support boundary, and closure;
- informed permission process for testimonials and case studies.

A delivery process that leaves access, approvals, ownership, or support ambiguous leaves G8 `BLOCKED`.

## G9 — Legal / Compliance / Risk

**Decision:** Are material obligations and risks identified, assigned, and treated honestly?

Required evidence, where relevant:

- applicable jurisdictions and regulatory questions are identified;
- licenses, registrations, permits, insurance, professional advice, and contract terms are checked or marked unresolved;
- privacy, data protection, information security, intellectual property, consumer, advertising, and sector-specific risks are assessed;
- risk owners, controls, residual ratings, and escalation thresholds are recorded;
- public language avoids claiming legal compliance or licensure without competent verification.

Unresolved legal authority, critical risk, or required professional verification leaves G9 `BLOCKED`.

## G10 — Capacity

**Decision:** Can MPG fulfil expected demand without degrading current commitments?

Required evidence:

- delivery and support effort assumptions;
- named accountable function and current availability;
- practical concurrent-work and throughput limits;
- bottlenecks, lead times, review load, and partner capacity;
- intake throttling, waitlist, pause, or decline rules;
- existing clients and founder sustainability are protected.

Optimistic availability or unbounded support leaves G10 `BLOCKED`.

## G11 — Proof

**Decision:** Is there evidence proportionate to the outcome and risk being claimed?

Evidence may include an internal demo, completed project, controlled pilot, case study, testimonial, measurable result, or repeated successful delivery. The review must verify authorship, scope, date, relevance, limitations, permission, and whether results can fairly support each public claim.

Fabricated, unverifiable, cherry-picked, permissionless, or materially different evidence leaves G11 `BLOCKED`. Proof requirements should be stricter for higher-risk or higher-impact services.

## G12 — Partner Readiness

**Decision:** Can every material third party reliably perform its disclosed part of delivery?

Required for `PARTNER_DELIVERY` and `HYBRID_DELIVERY`, and whenever a critical dependency is external.

Required evidence:

- capability, reliability, commercial terms, capacity, geography, communication, and service levels are evaluated;
- responsibilities, client interface, data handling, legal/compliance allocation, and public disclosure are clear;
- relationship status and authority to make partnership claims are verified;
- substitution, interruption, dispute, remediation, and exit plans exist;
- required written terms and professional checks are complete;
- partner approval is current for the exact service scope.

A vendor listing, informal contact, quotation, or assumed availability leaves G12 `BLOCKED`.

## G13 — Marketing Readiness

**Decision:** Can MPG describe and solicit the offer truthfully, specifically, and safely?

Required evidence:

- offer language matches the approved scope, delivery mode, and actual capability;
- target audience, problem, outcome, exclusions, and call to action are defined;
- every material claim maps to current evidence and permission;
- proof and required marketing assets are available and accurate;
- partner role and infrastructure ownership are not obscured;
- legal or platform reviews required for claims are complete;
- active-offer content is distinguishable from capability-journey and thought-leadership content.

G13 at `SATISFIED` does not itself authorize publication. The owner must separately set marketing approval to true and the service must become `ACTIVE`.

## Launch decision

The readiness reviewer recommends one of:

- **DO NOT ADVANCE:** one or more gates are `NOT_ASSESSED`, `BLOCKED`, or `IN_PROGRESS`;
- **RETURN TO CAPABILITY BUILDING:** material redesign or evidence work is needed;
- **DELIVERY READY ONLY:** delivery is supportable but public release is not authorized;
- **RECOMMEND MARKET APPROVAL:** all required gates are `SATISFIED` or validly `NOT_APPLICABLE`; owner decision still required.

Only the MPG Founder, or a role delegated in an accepted decision, may approve market release. The decision record must identify the reviewed service version and gate review. After approval, activation still requires current capacity, operational links, `lifecycleStatus: ACTIVE`, and `marketingApproved: true`.

## Revalidation

Re-run affected gates when scope, delivery mode, price method, critical capability, tool, asset, partner, jurisdiction, regulation, capacity, claims, or quality evidence changes; after a material incident; or when evidence reaches its stated review trigger. A prior `SATISFIED` state is not permanent.
