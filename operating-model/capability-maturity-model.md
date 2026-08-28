# Capability Maturity Model

> **Document:** Capability Maturity Model
> **Status:** RECOMMENDED — pending Stage 0 owner acceptance
> **Stage:** Stage 0 — Governance and Source of Truth
> **Owner:** MPG Founder
> **Last Updated:** 2026-08-28
> **Public Safe:** Yes
> **Authority:** MPG Company OS Master Repository Bootstrap v2

## Purpose

This policy governs how MPG records what it may be able to do without overstating what it can deliver professionally. A capability is knowledge, skill, process, asset, relationship, or operating capacity. It is not automatically a service.

The governing chain is:

> New skills create possibilities. Validated skills create capabilities. Capabilities combined with tools, assets, processes, economics, capacity, proof, compliance, and any required partners create a deliverable service. A deliverable service combined with explicit owner approval may become a marketable offer.

Current project stage is **Stage 0 — Governance and Source of Truth**. This model does not activate Stage 1 or validate any person's proficiency.

## Canonical capability statuses

| Status | Meaning | Minimum record needed |
|---|---|---|
| `UNASSESSED` | No reliable assessment has been recorded. This is the safe default. | Capability name, intended use, and owner. |
| `LEARNING` | Structured learning is underway; professional delivery is not established. | Learning objective and review point. |
| `PRACTICING` | Practical work is underway in a controlled setting. | Practice artifact or assessment plan. |
| `COMPETENT` | An assessment indicates the capability can be performed to a defined standard, but external or repeated delivery evidence is not yet sufficient for validation. | Assessor, standard, date, evidence reference, limits. |
| `VALIDATED` | Suitable evidence demonstrates the capability can support reliable delivery within stated boundaries. | Verifiable evidence, scope, validator, validation date, and revalidation trigger. |
| `PARTNER_DEPENDENT` | MPG does not claim direct validated capability; delivery depends on an identified and approved third party. | Required partner role, due-diligence status, delivery boundary, and fallback. |
| `NOT_REQUIRED` | A documented service design does not require the capability. | Rationale and approving reviewer. |

`UNKNOWN`, blank fields, course completion, tool ownership, self-description, or interest must never be translated into `COMPETENT` or `VALIDATED`.

## Evidence standard

Evidence must be relevant to the exact capability and delivery boundary. Suitable evidence may include:

- a completed project with reviewable outputs;
- a controlled practical assessment against written criteria;
- a portfolio artifact with known authorship and scope;
- repeated successful delivery with quality records;
- a recognized certification where that certification is materially relevant;
- validated partner capability when the status remains `PARTNER_DEPENDENT`.

Evidence is insufficient when it only shows attendance, course completion, access to software, unverified claims, activity without an evaluated result, or work outside the claimed scope.

Each assessment must record:

- stable capability ID and capability name;
- present status and requested status;
- why the capability is needed and which service records depend on it;
- assessment criteria and delivery boundary;
- evidence references that a reviewer can inspect;
- evidence date, assessor or validator role, and limitations;
- next review or revalidation trigger;
- decision authority and decision date.

Evidence references in this public repository must not expose confidential client, personal, partner, or commercial information. Store sensitive evidence in approved private storage and reference it by a non-sensitive identifier.

## Progression and regression

Normal direct-delivery progression is:

`UNASSESSED` → `LEARNING` → `PRACTICING` → `COMPETENT` → `VALIDATED`

Steps may be skipped only when the evidence already satisfies the destination status. A recorded assessment is still required.

A capability must be downgraded or placed under review when:

- repeated defects show the standard is no longer met;
- the delivery context or required technology materially changes;
- evidence expires or can no longer be verified;
- a required person, asset, license, or partner is unavailable;
- legal, security, quality, or capacity conditions change;
- the validated boundary is exceeded.

Downgrading a capability is a control, not a punishment. All dependent services must be reviewed immediately; no service may remain `ACTIVE` on capability evidence that is no longer valid.

## Direct and partner-supported capability

- **Direct capability / `OWNED_DELIVERY`:** MPG performs the work and holds evidence for the people and process involved.
- **Partner-dependent capability / `PARTNER_DELIVERY`:** a qualified third party performs substantial delivery; MPG must not restate that capability as its own.
- **Hybrid capability / `HYBRID_DELIVERY`:** direct and partner-dependent elements are mapped separately. Each element needs an accountable owner, evidence, and an interface or handoff control.

Partner evidence must meet [Partner Governance](partner-governance.md). Finding a vendor, receiving a quotation, or having an informal conversation does not validate partner capability.

## Relationship to service readiness

A service definition must map every required capability to the capability registry. For readiness gate G2:

1. required capabilities are complete and scoped;
2. each critical capability is `VALIDATED` or properly `PARTNER_DEPENDENT`;
3. limitations are reflected in the service scope and public claims;
4. partner-dependent items also reach `SATISFIED` at G12;
5. unresolved gaps leave G2 `BLOCKED` or `IN_PROGRESS` and prevent `MARKET_APPROVED` or `ACTIVE` status.

Capability validation alone does not satisfy the other launch gates and does not authorize marketing.

## Review responsibility

The service owner proposes assessments and supplies evidence. A reviewer checks the evidence against the stated standard. The MPG Founder approves material status changes or delegates that authority in an accepted decision record. No AI agent may infer proficiency or promote a capability without recorded evidence and authority.

## Stage 0 rule

During Stage 0, unknown capabilities remain `UNASSESSED`. Professional Business Websites is the first commercial service family to undergo a later readiness audit, but this priority does not itself validate any required capability or approve the service for sale.
