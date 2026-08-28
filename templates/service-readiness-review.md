# Service Readiness Review

> **Document:** Service Readiness Review Template
> **Template Status:** CONTROLLED TEMPLATE
> **Stage:** Stage 0 — Governance and Source of Truth
> **Template Owner:** MPG Founder
> **Last Updated:** 2026-08-28
> **Public Safe:** Yes while blank; completed evidence may be confidential
> **Authority:** Service Launch Gates G1–G13

## Use rule

Use this review before `MARKET_APPROVED`, `ACTIVE`, and whenever a material change invalidates prior evidence. `UNKNOWN`, `TBD`, blanks, and expired evidence cannot make a gate `SATISFIED`. Record missing evidence as a gap with an owner; never fabricate it.

When a completed review feeds a registry record, use `repo:<relative-path>[#optional-anchor]` or `private:<public-safe-id>` for traceable evidence. Private identifiers must disclose no confidential facts; the owner market-approval decision remains a repository-backed record.

## Review control

| Field | Entry |
|---|---|
| Review ID / version | `[ID]` |
| Service ID / definition version | `[ID / version]` |
| Current → requested lifecycle status | `[FROM → TO]` |
| Delivery mode | `[OWNED_DELIVERY / PARTNER_DELIVERY / HYBRID_DELIVERY]` |
| Review scope / geography | `[Boundaries]` |
| Reviewer | `[Accountable function]` |
| Review date | `[YYYY-MM-DD]` |
| Evidence cutoff date | `[YYYY-MM-DD]` |
| Sensitive evidence location | `[Public-safe reference only]` |

## State rule

Use only `NOT_ASSESSED`, `BLOCKED`, `IN_PROGRESS`, `SATISFIED`, or `NOT_APPLICABLE`. A gate is `SATISFIED` only when every required criterion has current evidence. `NOT_APPLICABLE` needs written rationale and reviewer approval; G12 cannot be `NOT_APPLICABLE` for `PARTNER_DELIVERY`, `HYBRID_DELIVERY`, or any material external dependency.

For each gate, list exact evidence—not “complete,” “experienced,” or “industry standard.”

## G1 — Customer Need

- Target customer and explicit exclusions: `[Entry]`
- Defined problem and desired outcome: `[Entry]`
- Demand evidence, date, source, and limitations: `[References]`
- Alternative/current behaviour and buying constraints: `[Entry]`
- Unproven assumptions: `[Entry]`

**State:** `[STATE]`<br>
**Gap/action/owner:** `[Entry]`<br>
**Reviewer rationale:** `[Why evidence does or does not satisfy G1]`

## G2 — Capability

- Required capability IDs and boundaries: `[Entry]`
- Direct capability validation evidence: `[References]`
- Partner-dependent capability mapping: `[References or NOT_APPLICABLE]`
- Limits reflected in scope: `[Entry]`
- Critical gaps or single-person dependency: `[Entry]`

**State:** `[STATE]`<br>
**Gap/action/owner:** `[Entry]`<br>
**Reviewer rationale:** `[Entry]`

## G3 — Tools & Technology

- Critical tool/environment IDs and availability: `[Entry]`
- Accounts, licenses, access ownership, and reliability evidence: `[Entry]`
- Setup/recurring/usage/exit costs: `[Evidence]`
- Data/security suitability and contingency: `[Entry]`

**State:** `[STATE]`<br>
**Gap/action/owner:** `[Entry]`<br>
**Reviewer rationale:** `[Entry]`

## G4 — Assets

- Required asset IDs, versions, owners, and availability: `[Entry]`
- Quality/usability and rights evidence: `[Entry]`
- Missing or inaccessible critical assets: `[Entry]`

**State:** `[STATE]`<br>
**Gap/action/owner:** `[Entry]`<br>
**Reviewer rationale:** `[Entry]`

## G5 — Delivery Process

- End-to-end workflow and accountable functions: `[Reference]`
- Scope boundaries, dependencies, and client responsibilities: `[Entry]`
- SOP, handoffs, change, exception, and escalation controls: `[References]`
- Delivery-mode interfaces: `[Entry]`

**State:** `[STATE]`<br>
**Gap/action/owner:** `[Entry]`<br>
**Reviewer rationale:** `[Entry]`

## G6 — Quality Assurance

- Acceptance criteria and QA checklist: `[References]`
- Test/review environment, roles, and release authority: `[Entry]`
- Defect, rework, retest, exception, and evidence controls: `[Entry]`
- Known unresolved quality concerns: `[Entry]`

**State:** `[STATE]`<br>
**Gap/action/owner:** `[Entry]`<br>
**Reviewer rationale:** `[Entry]`

## G7 — Commercial Readiness

- Pricing method and cost-floor evidence: `[Reference; no arbitrary numbers]`
- Third-party, revision, risk, support, tax/fee, and partner costs: `[Entry]`
- Margin logic, payment structure, and change-request policy: `[References]`
- Conditions requiring decline or re-quotation: `[Entry]`

**State:** `[STATE]`<br>
**Gap/action/owner:** `[Entry]`<br>
**Reviewer rationale:** `[Entry]`

## G8 — Client Experience

- Qualification, discovery, and onboarding: `[References]`
- Communication, approvals, delay, and escalation expectations: `[Entry]`
- Handover, training, support, and closure: `[References]`
- Testimonial/case-study permission process: `[Entry]`

**State:** `[STATE]`<br>
**Gap/action/owner:** `[Entry]`<br>
**Reviewer rationale:** `[Entry]`

## G9 — Legal / Compliance / Risk

- Jurisdiction and regulatory questions: `[Entry]`
- License/registration/insurance/terms/professional checks: `[Evidence or unresolved]`
- Privacy, security, IP, consumer, advertising, and sector risks: `[Risk IDs]`
- Required verification and residual high/severe risks: `[Entry]`

**State:** `[STATE]`<br>
**Gap/action/owner:** `[Entry]`<br>
**Reviewer rationale:** `[Do not claim compliance without competent verification]`

## G10 — Capacity

- Delivery/support effort and lead-time basis: `[Evidence]`
- Named accountable function and actual availability: `[Entry]`
- Concurrent-work limit, bottleneck, and current commitment impact: `[Entry]`
- Intake throttle, waitlist, pause, decline, and contingency rules: `[Entry]`

**State:** `[STATE]`<br>
**Gap/action/owner:** `[Entry]`<br>
**Reviewer rationale:** `[Entry]`

## G11 — Proof

- Evidence type, reference, authorship, date, and service relevance: `[Entry]`
- Results, baseline, measurement method, and limitations: `[Entry]`
- Permission for names, testimonial, image, or public use: `[Entry]`
- Claims the evidence cannot support: `[Entry]`

**State:** `[STATE]`<br>
**Gap/action/owner:** `[Entry]`<br>
**Reviewer rationale:** `[Entry]`

## G12 — Partner Readiness

- Material partner capability and public-safe partner ID: `[Entry]`
- Approval scope, diligence evidence, terms, capacity, and geography: `[References]`
- Data/legal/compliance allocation and client disclosure: `[Entry]`
- Monitoring, interruption, substitution, dispute, and exit plan: `[Entry]`
- Public relationship language authorized: `[Exact words or prohibited]`

**State:** `[STATE]`<br>
**Gap/action/owner or NOT_APPLICABLE rationale:** `[Entry]`<br>
**Reviewer rationale:** `[Entry]`

## G13 — Marketing Readiness

- Exact target audience, offer, approved scope, and CTA: `[Entry]`
- Claim-to-evidence map and permissions: `[Reference]`
- Required assets and publication locations: `[Entry]`
- Delivery mode, partner role, and infrastructure ownership stated accurately: `[Entry]`
- Active-offer content separated from journey/thought leadership: `[Entry]`

**State:** `[STATE]`<br>
**Gap/action/owner:** `[Entry]`<br>
**Reviewer rationale:** `[Entry]`

## Gate summary

| Gate | State | Evidence version/date | Revalidation trigger |
|---|---|---|---|
| G1 | | | |
| G2 | | | |
| G3 | | | |
| G4 | | | |
| G5 | | | |
| G6 | | | |
| G7 | | | |
| G8 | | | |
| G9 | | | |
| G10 | | | |
| G11 | | | |
| G12 | | | |
| G13 | | | |

## Review conclusion

- **Conclusion:** `[DO NOT ADVANCE / RETURN TO CAPABILITY BUILDING / DELIVERY READY ONLY / RECOMMEND MARKET APPROVAL]`
- **Blocking items:** `[Gate, action, owner, trigger]`
- **Risks accepted/escalated:** `[Risk and decision IDs]`
- **Reviewer rationale:** `[Evidence-based explanation]`
- **Next review trigger:** `[Condition/date if evidence supports one]`

## Owner decision

Market approval is never inferred from this review.

| Decision | Entry |
|---|---|
| Owner decision | `[DECLINED / REMEDIATION REQUIRED / MARKET APPROVED]` |
| Decision record ID | `[ID]` |
| Approved service/review version | `[Version]` |
| Marketing approval set | `[true / false]` |
| Activation conditions | `[Current capacity, operational links, registry validation]` |
| Decided by / date | `[Authority / YYYY-MM-DD]` |
