# Public Claims Policy

> **Document:** Public Claims Policy
> **Status:** RECOMMENDED — pending Stage 0 owner acceptance
> **Stage:** Stage 0 — Governance and Source of Truth
> **Owner:** MPG Founder
> **Last Updated:** 2026-08-28
> **Public Safe:** Yes
> **Authority:** Accepted evidence-over-hype and publication rules, including `MPG-DEC-028`

## Policy

The public brand must never run ahead of MPG's ability to deliver. Every material external claim must be accurate, supportable, current, permissioned where necessary, and limited to the scope the evidence proves.

This applies to websites, social posts, profiles, directories, presentations, advertisements, proposals, quotations, sales conversations, email, events, press material, case studies, partner announcements, and AI-generated copy. “Public” includes direct claims to a prospect even when the message is not indexed online.

## Three communication categories

### A. Active offer content

Content may solicit a client only when the referenced service satisfies both authoritative publication conditions:

```text
lifecycleStatus == ACTIVE
AND marketingApproved == true
```

The registry field `publiclyMarketable` must be derived from that exact predicate; it is not a third approval. A mismatched derived value is a governance defect and the record must be excluded from generated publication until corrected. The content must stay within the approved service definition, delivery mode, evidence, geography, capacity, exclusions, and claim language. If the service is paused, retired, loses approval, or a material gate becomes unresolved, calls to action and active-offer language must be removed or disabled promptly.

### B. Capability journey content

MPG or the founder may truthfully discuss learning, research, experiments, practice, events, industry study, or tools without implying present sale or validated mastery.

Acceptable: “We are currently studying supplier-verification workflows for possible future MPG Trade operations.”

Not acceptable unless the service is publication-eligible: “MPG provides end-to-end supplier verification.”

Journey content should use precise state language such as *researching*, *learning*, *testing*, *building*, or *planning* and, where ambiguity is likely, state that the capability is not currently an active MPG offer.

### C. Thought leadership

Malcom Gwanmesia may share accurate lessons, ideas, observations, and project experience without turning every discussed topic into a company service. Opinion must be recognizable as opinion. Advice in legal, financial, compliance, safety, or other professional domains must not imply unverified credentials or replace qualified advice.

## Founder and company distinction

- **Malcom:** founder, leadership, trust, expertise, journey, thinking, and relationships.
- **MPG:** company systems, approved offers, delivery processes, and commercial operations.

Personal learning, experience, or a broad owner capability declaration cannot be rewritten as an MPG service unless the service lifecycle and launch controls are complete. `OWNER_DECLARED_CAPABLE` is not evidence validation, does not satisfy G2, and cannot support a stronger public claim than the evidence record permits. Company copy must not turn the founder into an implausible list of simultaneous expert identities.

## Evidence-over-hype rules

Never fabricate or inflate:

- customers, client names, testimonials, permission, or case studies;
- revenue, savings, conversions, reach, performance, or other results;
- team size, employees, offices, facilities, locations, or service coverage;
- partnerships, supplier relationships, clients, affiliations, or endorsements;
- years of experience, qualifications, certifications, awards, or licenses;
- completed projects, infrastructure, proprietary technology, inventory, or capacity;
- guarantees, market position, “best” claims, or business metrics.

A real small company is more credible than a fictional large one. If evidence is unavailable, narrow the claim, label it as a plan or hypothesis, or do not publish it.

## Claim substantiation record

Before publishing a material claim, record:

- exact proposed words and communication category;
- related service or capability ID;
- evidence reference, date, source, and owner;
- what the evidence proves and does not prove;
- calculation method and baseline for numerical claims;
- client, partner, trademark, image, or testimonial permission where required;
- geography, period, sample, conditions, and other material qualifications;
- review date or expiry trigger;
- reviewer and approval decision.

Evidence stored in private systems should be referenced by a public-safe identifier, not copied into this repository. A testimonial must preserve the speaker's intended meaning and approved attribution. A result from one project must not be presented as a guaranteed or typical result without support.

## Mandatory pre-publication check

The publisher must answer yes to each applicable question:

1. Is the content correctly classified as active offer, capability journey, or thought leadership?
2. If it solicits work, does the exact service satisfy `ACTIVE` plus marketing approval, with the derived publication field matching that result?
3. Does each factual or performance claim have current, inspectable evidence?
4. Are scope, limitations, delivery mode, partner role, and infrastructure ownership represented accurately?
5. Are permissions and required legal/platform reviews recorded?
6. Is the content public-safe and free of confidential or restricted information?
7. Does the call to action match current capacity and an approved offer?

A “no,” `TBD`, or missing record stops publication.

## Division safeguards

### Trade and distribution

Do not call MPG a freight forwarder, customs broker, licensed importer, manufacturer representative, distributor, shipping company, or owner of partner infrastructure unless current evidence and applicable authority support the exact statement. Where MPG coordinates third parties, describe that coordination and the third party's role plainly. Do not make an “official partner” claim without a real, approved relationship and permission to disclose it.

### Media

Do not use “full-service marketing” merely because MPG can produce posts. Distinguish strategy, creative, copywriting, organic social, paid media, tracking, analytics, SEO, and conversion optimization; only active and approved components may be offered.

### AI and automation

Avoid vague “AI transformation,” guaranteed savings, autonomous-operation, or error-free claims. Describe the bounded workflow, human controls, monitoring, data treatment, maintenance, vendor dependencies, and evidence-supported outcome.

## Corrections and withdrawal

Anyone who finds a potentially false, outdated, ambiguous, or permissionless claim must stop further use and notify the content owner. The owner must:

1. preserve the claim and publication location for the audit record;
2. assess client, legal, privacy, partner, and reputation impact;
3. correct, qualify, or withdraw the claim in every controlled channel;
4. notify affected parties when needed;
5. record root cause, corrective action, and any gate or status change;
6. pause the related service when reliable delivery or approval is in doubt.

Deleting a post does not erase the governance record.

## AI and contributor rule

AI may help draft or review language, but it is not an evidence source or approval authority. It must not fill unknowns with plausible claims, infer market approval, invent a client or partner, or convert proposed wording into accepted copy. The human publisher remains accountable for verification.
