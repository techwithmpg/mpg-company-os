# Partner Governance

> **Document:** Partner Governance
> **Status:** ACCEPTED — STAGE 0 BASELINE
> **Stage:** Stage 0 — Governance and Source of Truth
> **Owner:** MPG Founder
> **Last Updated:** 2026-08-28
> **Public Safe:** Yes
> **Authority:** Accepted partner-dependent capability safeguards in MPG Company OS Master Repository Bootstrap v2

## Purpose

This policy controls services that depend on contractors, vendors, suppliers, professional advisers, specialists, logistics providers, or other third parties. It prevents an available contact from being mistaken for a validated capability or publicly announced partnership.

No partner is implied by this policy. The public-safe partner registry may legitimately contain no approved partners.

## Delivery modes

Every service must use one registry value:

| Registry value | Display label | Meaning |
|---|---|---|
| `OWNED_DELIVERY` | Owned Delivery | MPG performs core delivery directly and holds the required evidence. Incidental vendors must still be controlled. |
| `PARTNER_DELIVERY` | Partner Delivery | A qualified third party performs substantial delivery; MPG's coordination, accountability, and limitations are explicit. |
| `HYBRID_DELIVERY` | Hybrid Delivery | MPG and one or more qualified partners each perform defined parts with controlled interfaces. |

MPG must never imply it employs partner personnel, owns partner infrastructure, holds a partner's license, or directly performs partner work when it does not.

## Partner lifecycle control

The partner record must distinguish at least: category, relationship status, due-diligence status, approval for a defined delivery scope, and permission for public disclosure. These are separate decisions.

The normal control path is:

1. **Need definition:** identify the capability, geography, capacity, risk, and service boundary required.
2. **Candidate identification:** record only public-safe facts; no relationship claim follows.
3. **Initial screen:** assess apparent fit, conflicts, sanctions or reputational concerns where relevant, and willingness to proceed.
4. **Due diligence:** gather and verify evidence proportionate to risk.
5. **Controlled validation:** test samples, references, trial work, site/process review, or professional verification as appropriate.
6. **Terms and interface:** document responsibilities, service levels, price basis, data, compliance, client communication, remedy, and exit.
7. **Approval:** authorize the specific partner for a specific capability, service, geography, and period or review trigger.
8. **Monitoring:** review quality, reliability, incidents, capacity, changes, and evidence.
9. **Suspend or exit:** stop new reliance when approval conditions fail and execute the contingency plan.

Discovery, a meeting, a quotation, a referral, or informal willingness is not due diligence or delivery approval.

## Minimum due-diligence domains

Assess and document, where applicable:

- legal identity and authority to contract;
- exact capability, experience, qualifications, licenses, and scope limits;
- quality controls, samples, references, and performance evidence;
- capacity, lead times, operating geography, facilities, and critical dependencies;
- pricing, currency, taxes/fees, payment risk, commissions, and change conditions;
- communication, escalation, reporting, language, and time-zone requirements;
- privacy, security, confidentiality, intellectual property, access, and data location;
- relevant regulatory, customs, insurance, safety, sanctions, and professional checks;
- financial, continuity, subcontracting, conflict-of-interest, and reputation risks;
- complaint, dispute, defect, refund/remedy, recall, and incident procedures;
- backup provider, substitution, transition, records return, and exit plan;
- whether and how the relationship may be disclosed publicly.

The reviewer must distinguish verified evidence, self-attestation, external professional advice, and unresolved questions. Do not claim legal compliance where competent verification has not occurred.

## Approval record

Approval must state:

- partner ID and public-safe identity reference;
- approved capability, service ID, delivery mode, geography, and boundaries;
- due-diligence evidence references and unresolved limitations;
- required terms, service levels, insurance, licenses, or professional review;
- data classification and approved systems;
- price basis and commercial dependencies;
- monitoring owner and review/expiry trigger;
- fallback and client-impact plan;
- public disclosure permission and exact approved relationship language;
- approver and decision date.

Approval is not transferable to another service, affiliate, geography, subcontractor, or materially changed scope without review.

## Service and marketing gates

Any material partner dependency requires G12 to be `SATISFIED`; `PARTNER_DELIVERY` and `HYBRID_DELIVERY` can never mark G12 `NOT_APPLICABLE`. Partner readiness does not satisfy the other twelve gates and does not authorize service activation.

A partner-dependent service may become publicly marketable only when the service is `ACTIVE` and marketing approval is true, all required gates are current, and partner approval covers the exact published offer. The derived `publiclyMarketable` field must equal the `ACTIVE` plus marketing-approval predicate; it is not a third approval.

## Client-facing safeguards

Before commitment, the client must receive a clear description of:

- MPG's role and the partner's role;
- who contracts, invoices, controls work, communicates, and accepts deliverables;
- material dependencies, exclusions, lead times, and geographic limits;
- handling of client data, access, funds, goods, and intellectual property;
- escalation, remedy, substitution, and support route;
- any material commission or conflict disclosure required by law, contract, or trust.

Partner terms must not be promised to the client until confirmed. MPG remains accountable for the obligations it accepts even when a third party performs work.

## Trade and distribution safeguards

Trade-related services remain strategic/planned until evidence addresses sourcing competence, supplier-verification methods, applicable import/export and local business requirements, payment and fraud risk, freight/customs dependencies, contracts, insurance, commissions, representation authority, buyer/supplier disputes, goods inspection, and contingency.

MPG must not hold itself out as a freight forwarder, customs broker, licensed importer, manufacturer representative, distributor, or shipping company without verified authority. When MPG coordinates qualified providers, language must describe coordination rather than ownership of regulated functions or infrastructure.

## Monitoring, suspension, and exit

Monitor against defined indicators such as defects, missed commitments, complaints, incident response, communication, capacity, license/insurance status, data handling, cost changes, and subcontracting. Immediately review or suspend approval after a material incident, unapproved subcontracting, evidence expiry, legal/compliance concern, repeated quality failure, loss of capacity, misleading public claim, or material ownership/terms change.

Suspension requires MPG to stop new reliance, assess active client obligations, secure data/assets/funds, activate fallback, update G12 and service status, and remove unsupported partner claims. Preserve the decision history.

## Information handling

The public repository must not contain private contacts, contracts, bank details, IDs, non-public pricing, confidential diligence findings, or sensitive partner data. Store those records in approved private storage. The registry may contain stable IDs, categories, public facts, high-level statuses, and disclosure-safe notes only.
