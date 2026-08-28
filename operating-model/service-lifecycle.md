# Service Lifecycle

> **Document:** Service Lifecycle
> **Status:** ACCEPTED — STAGE 0 BASELINE
> **Stage:** Stage 0 — Governance and Source of Truth
> **Owner:** MPG Founder
> **Last Updated:** 2026-08-28
> **Public Safe:** Yes
> **Authority:** MPG Company OS Master Repository Bootstrap v2

## Purpose

This lifecycle separates strategic interest, capability building, delivery validation, owner release approval, and active sale. A service's presence in `registry/services.json` is not evidence that MPG sells it.

MPG may plan broadly but must sell narrowly.

## Canonical statuses

| Status | Operational meaning | Public sale permitted? |
|---|---|---:|
| `IDEA` | Interesting opportunity with no commitment. | No |
| `RESEARCH` | Need, feasibility, risks, or delivery requirements are being investigated. | No |
| `PLANNED` | Strategically accepted for future consideration; no delivery claim follows. | No |
| `PREREQUISITES_REQUIRED` | Known capability, tool, asset, process, legal, capacity, economic, or partner gaps prevent delivery. | No |
| `BUILDING_CAPABILITY` | MPG is developing the skills, assets, tools, systems, or processes required. | No |
| `INTERNAL_READY` | Core delivery appears possible internally but has not been client-validated. | No |
| `PILOT_READY` | A bounded, controlled pilot has an approved plan, safeguards, and success criteria. | No |
| `PILOTING` | A controlled pilot is underway. | No |
| `DELIVERY_READY` | Evidence from a pilot or equivalent validation supports reliable delivery; public release is not approved. | No |
| `MARKET_APPROVED` | The MPG Founder has explicitly approved commercial/public release after launch-gate review. This is a release decision, not yet the live-state flag. | No |
| `ACTIVE` | The service is currently deliverable and may be marketed only when marketing approval remains true. | Only with `marketingApproved: true` |
| `PAUSED` | New sale and solicitation are temporarily stopped. Existing obligations require an explicit fulfilment or transition plan. | No |
| `RETIRED` | The offer has been withdrawn and is no longer sold. | No |

Descriptions such as “in development” may be displayed for readers, but registry and governance records must use the canonical status.

## Publication predicate

A service is eligible for an automatically generated or actively solicited public catalogue only when both authoritative conditions are true:

```text
lifecycleStatus == ACTIVE
AND marketingApproved == true
```

`publiclyMarketable` is not a third approval. It is a derived enforcement field that must equal the result of the two-condition predicate above. A mismatch is a registry defect: exclude the record from generated output until the derived field is corrected. If either authoritative condition is false, the service must be excluded from active-offer content and service sales calls to action.

Marketing approval requires an explicit, traceable owner decision. Readiness, registry presence, pilot success, a tool purchase, partner availability, or draft website copy cannot imply that approval.

## Transition control

Every transition request must include:

- service ID, current status, requested status, and request date;
- reason for the transition;
- evidence references and readiness-gate results appropriate to the destination;
- unresolved gaps, risks, dependencies, and capacity impact;
- delivery mode: `OWNED_DELIVERY`, `PARTNER_DELIVERY`, or `HYBRID_DELIVERY` (displayed as Owned Delivery, Partner Delivery, or Hybrid Delivery);
- reviewer recommendation;
- approving authority and recorded decision;
- registry and dependent-document updates.

No agent or contributor may change a status merely to make another document, catalogue, or website build pass validation.

## Allowed normal transitions

| From | Normal next states | Required control |
|---|---|---|
| `IDEA` | `RESEARCH`, `RETIRED` | Research question or closure rationale. |
| `RESEARCH` | `PLANNED`, `PREREQUISITES_REQUIRED`, `RETIRED` | Findings, strategic fit, and owner decision where planning is requested. |
| `PLANNED` | `RESEARCH`, `PREREQUISITES_REQUIRED`, `BUILDING_CAPABILITY`, `RETIRED` | WIP capacity and explicit prioritization before capability building. |
| `PREREQUISITES_REQUIRED` | `PLANNED`, `BUILDING_CAPABILITY`, `RETIRED` | Gap list, owners, and evidence that work may begin. |
| `BUILDING_CAPABILITY` | `PREREQUISITES_REQUIRED`, `INTERNAL_READY`, `PAUSED` | Internal assessment and evidence for readiness. |
| `INTERNAL_READY` | `BUILDING_CAPABILITY`, `PILOT_READY`, `PAUSED` | Pilot plan, risk controls, capacity, acceptance criteria. |
| `PILOT_READY` | `BUILDING_CAPABILITY`, `PILOTING`, `PAUSED` | Authorized pilot and participant safeguards. |
| `PILOTING` | `BUILDING_CAPABILITY`, `DELIVERY_READY`, `PAUSED` | Pilot report, defects, outcomes, and repeatability decision. |
| `DELIVERY_READY` | `BUILDING_CAPABILITY`, `MARKET_APPROVED`, `PAUSED` | Complete G1–G13 review and explicit owner release approval. |
| `MARKET_APPROVED` | `DELIVERY_READY`, `ACTIVE`, `PAUSED` | Activation date, current capacity confirmation, marketing approval true, and registry validation. |
| `ACTIVE` | `PAUSED`, `RETIRED` | Client-impact plan, publication removal, and recorded reason. |
| `PAUSED` | A previously attained non-retired state, or `RETIRED` | Revalidation appropriate to elapsed time and pause cause; no automatic return to `ACTIVE`. |
| `RETIRED` | `IDEA` only as a newly reconsidered cycle | Owner authorization and preserved retirement history. |

Skipping intermediate states requires an explicit rationale showing that destination evidence is already satisfied. `MARKET_APPROVED` and the transition to `ACTIVE` may never be skipped.

## Destination evidence

- **Internal readiness:** core capabilities, tools, assets, draft process, and internal quality evidence.
- **Pilot readiness:** a bounded pilot scope, informed participant, success/failure criteria, legal/data review, rollback or remedy, and available capacity.
- **Delivery readiness:** completed pilot report or justified equivalent, resolved material defects, repeatable process, QA criteria, economics, and support model.
- **Market approval:** every required G1–G13 gate is `SATISFIED`; any `NOT_APPLICABLE` gate has a written rationale; the owner signs the release decision.
- **Active:** approval is still current, resources and capacity are available, operational records are linked, truthful offer copy is ready, and `marketingApproved` is true.

## Pause, incident, and regression

Pause a service when MPG cannot reliably honour new commitments, including loss of a critical capability, tool, license, asset, partner, legal basis, capacity, or quality control. Also pause it for material incidents or substantiated misleading claims while investigation occurs.

When paused:

1. stop new solicitation and remove active calls to action;
2. protect existing clients through a documented fulfilment, remediation, or transition plan;
3. record cause, owner, risk, and re-entry conditions;
4. reassess affected gates before any return;
5. preserve prior decisions and evidence rather than rewriting history.

## Current Stage 0 application

Professional Business Websites is the priority-one service family and may be recorded as `BUILDING_CAPABILITY` where the service registry follows the accepted bootstrap instruction. It is not automatically market-approved or active. Other strategic families generally remain `PLANNED` unless evidence and an authorized decision support another status. No Stage 1 work is authorized by this policy.

## Related controls

- [Service Launch Gates](service-launch-gates.md)
- [Work-in-Progress Policy](work-in-progress-policy.md)
- [Public Claims Policy](public-claims-policy.md)
- [Partner Governance](partner-governance.md)
- [Quality Standard](quality-standard.md)
