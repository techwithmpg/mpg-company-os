# Work-in-Progress Policy

> **Document:** Work-in-Progress Policy
> **Status:** ACCEPTED — STAGE 0 BASELINE
> **Stage:** Stage 0 — Governance and Source of Truth
> **Owner:** MPG Founder
> **Last Updated:** 2026-09-19
> **Public Safe:** Yes
> **Authority:** Accepted anti-scatter rule, `MPG-DEC-029`, and temporary execution allocation under `MPG-DEC-046`

## Policy

MPG may plan broadly but must sell narrowly. The default portfolio limit is:

- **one primary commercial build track** actively productizing one major new service family; and
- **at most one secondary capability-development track** under meaningful structured learning, research, or incubation.

Everything else remains `IDEA`, `RESEARCH`, `PLANNED`, backlog, or parked until capacity is deliberately released. A lifecycle record can remain in `RESEARCH` without consuming the secondary slot only when work is passive or trivial; scheduled experiments, deliverables, recurring meetings, a budget, or meaningful founder attention make it active WIP.

## Current allocation under Stage 1

`MPG-DEC-046` creates a temporary execution exception to the default primary-plus-secondary allocation without changing the accepted commercial productization sequence.

| Slot | Current allocation | State |
|---|---|---|
| Commercial sequence priority | Professional Business Websites | First in accepted sequence; active productization temporarily **PAUSED** under `MPG-DEC-046` |
| Temporary primary execution focus | MPG Reputation / Review & Reputation Automation (`PROD-REP-001`) | **ACTIVE MARKET-READY BUILD** under `MPG-DEC-046`; not service lifecycle `ACTIVE` |
| Secondary incubation/build track | None | **UNALLOCATED** while the focused Reputation program is active |

The current commercial build order is:

1. Professional Business Websites
2. Custom Business Systems
3. AI and Workflow Automation
4. Mobile Applications
5. Digital Marketing
6. Social Media Management
7. Trade, Sourcing and Distribution

This sequence controls company productization, not all personal learning or broad owner declarations. Adding Mobile Applications to internal architecture does not admit it to either WIP slot. Stage 0 governance work and authorized Stage 1 company/brand work do not create another service-family productization track or allocate the secondary slot. Stage 1 is active under `MPG-DEC-033`; Stage 2 remains inactive.

## MPG Reputation temporary execution-focus record

- **Subject/outcome:** `PROD-REP-001`; develop and validate the review-request product defined in [product direction](../products/mpg-reputation/README.md).
- **Allocation and authority:** temporary primary execution focus under `MPG-DEC-046` (2026-09-19). Professional Business Websites retains first position in the commercial sequence but its active productization work is paused.
- **Current milestone state:** MR-2 Customer Activation is complete / accepted; MR-3 Completion Source Platform is next and has not yet started.
- **Scope:** the bounded market-ready program authorized by `MPG-DEC-046`, including production engineering, messaging architecture, activation, completion sources, usage controls, billing preparation, operations, trust controls, product website/acquisition infrastructure, controlled pilot preparation and launch-readiness work within their sequential gates.
- **Resources:** founder capacity allocation, time/spend limits and provider accounts remain governed by milestone scope and applicable gates. No new provider spend, live customer messaging, pilot or public release follows automatically.
- **Review trigger:** each material product milestone and before integration expansion, provider spend, real-customer pilot, live messaging or launch commitments.
- **Pause/stop:** pause or re-scope when founder capacity is unavailable, scope exceeds the bounded product, unresolved security/data/compliance/economic risks become material, or another owner decision supersedes the focus.
- **Secondary slot:** no secondary capability/productization track is currently open during this focused execution period.

The registry `primaryExecutionFocus` value is a WIP allocation record only. It is not service lifecycle `ACTIVE`, `PILOT_READY`, `DELIVERY_READY`, `MARKET_APPROVED`, marketing approval, legal readiness or public-release authority.

## What counts as primary-track WIP

A service family consumes the primary slot when MPG is doing one or more of the following with intent to commercialize it:

- defining an offer, standard scope, pricing method, or contract model;
- building required delivery assets or operating processes;
- running readiness remediation or a commercial pilot;
- creating active-offer marketing or a launch package;
- allocating sustained founder, contractor, partner, or financial capacity.

Maintenance of an already active service is delivery load and must be included in capacity planning, but it does not authorize a second new service family.

## What counts as secondary-track WIP

Meaningful structured research, learning, practice, partner exploration, or incubation consumes the secondary slot when it has a stated outcome, allocated time or spend, active experiments, or regular commitments. Casual reading and captured backlog notes do not.

The secondary track may build knowledge and evidence. It may not produce active-offer content, solicit clients, bypass lifecycle gates, or displace obligations on the primary track.

## Admission checklist

Before work enters either slot, record:

- service or capability ID and intended outcome;
- slot requested and why now;
- fit with the accepted commercial sequence;
- definition of done or next decision;
- time, budget, tools, partner, and information needs;
- impact on current clients and founder capacity;
- pause/stop condition and review point;
- owner authorization where required.

If the slot is occupied, finish, pause, or explicitly replace the existing item before admitting another.

## Switching and pausing

A switch must be deliberate. The transition record must state:

1. what is stopping and its lifecycle status;
2. incomplete work, commitments, evidence, and risks;
3. where artifacts and decisions are recorded;
4. why the incoming work is more important;
5. the re-entry condition for paused work;
6. owner approval if the commercial sequence, priority, or WIP limit changes.

“Temporarily helping” another service becomes a switch when it produces sustained commitments. Work may not be hidden under a broad division label to evade the limit.

## Exceptions

Only the MPG Founder may authorize more than one primary build track or more than one secondary track. An exception must be a recorded decision with scope, reason, added capacity, client impact, duration or review trigger, stop conditions, and the risks accepted. Silence, interest, tool ownership, a new enquiry, or a potential partner is not approval.

Urgent client support, legal/security response, and incident remediation may pre-empt planned WIP. They must be recorded, and planned work must be paused rather than informally multiplied.

## Anti-scatter safeguards

- Learning a skill does not authorize MPG to sell a related service.
- Buying or trialling a tool does not create a service or validate capability.
- Finding a vendor or partner does not authorize a partnership claim or marketing.
- Drafting content does not change a lifecycle status.
- A promising lead must be declined, referred, deferred, or separately approved when capability or capacity gates are not met.
- Division-level ambition must not be presented as a current offer.

## Review

Review the WIP allocation at each material status update and before accepting work that affects capacity. Report the two slots in `docs/01-project-status.md`. Any mismatch between the status document, service registry, and accepted decision register is a governance defect and must be resolved before new productization begins.
