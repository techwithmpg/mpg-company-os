# Service Definition Template

> **Document:** Service Definition Template
> **Template Status:** CONTROLLED TEMPLATE
> **Stage:** Stage 0 — Governance and Source of Truth
> **Template Owner:** MPG Founder
> **Last Updated:** 2026-08-28
> **Public Safe:** Yes while blank; classify completed copies
> **Authority:** Service Lifecycle and Service Launch Gates

## Completion rules

Do not turn assumptions into facts. Replace each prompt with evidence or record `TBD` plus an owner, next action, and review trigger. A completed definition is not approval to sell. Keep confidential client, partner, pricing, or evidence details in approved private storage and use public-safe references here.

When this template feeds a registry record, use `repo:<relative-path>[#optional-anchor]` or `private:<public-safe-id>` for traceable evidence. The owner market-approval record must be a repository reference to the governing decision; placeholders never authorize release.

## 1. Record control

| Field | Entry |
|---|---|
| Stable service ID | `[DIVISION-FAMILY-NNN]` |
| Service name | `[Specific, non-inflated name]` |
| Division | `[MPG Technologies / MPG Media / MPG Trade & Distribution]` |
| Definition version | `[Version]` |
| Record status | `[PROPOSED / RECOMMENDED / ACCEPTED / FROZEN / DEPRECATED]` |
| Definition owner | `[Accountable function]` |
| Last reviewed | `[YYYY-MM-DD]` |
| Supersedes | `[Record/version or NONE]` |
| Evidence location/classification | `[Public-safe reference; never credentials or confidential details]` |

## 2. Lifecycle and publication control

| Control | Entry |
|---|---|
| Lifecycle status | `[IDEA / RESEARCH / PLANNED / PREREQUISITES_REQUIRED / BUILDING_CAPABILITY / INTERNAL_READY / PILOT_READY / PILOTING / DELIVERY_READY / MARKET_APPROVED / ACTIVE / PAUSED / RETIRED]` |
| Delivery mode | `[OWNED_DELIVERY / PARTNER_DELIVERY / HYBRID_DELIVERY]` |
| Marketing approved | `[true / false]` |
| Publicly marketable | `[true / false — derived control]` |
| Owner market-approval record | `[Decision ID or NONE]` |
| WIP slot | `[PRIMARY / SECONDARY / BACKLOG / NONE]` |

**Publication check:** Active-offer content is eligible only if lifecycle status is `ACTIVE` and marketing approved is `true`. `Publicly marketable` must equal that two-condition result as a derived field; it is not a third approval. Any mismatch is a registry defect: `[Explanation/correction owner or NONE]`.

## 3. Customer need

- **Target customer:** `[Observable characteristics; not “everyone”]`
- **Excluded or poor-fit customer:** `[Who should be declined or referred?]`
- **Problem:** `[Specific current condition and consequence]`
- **Desired outcome:** `[Outcome within MPG's influence]`
- **Current alternative:** `[What does the customer do now?]`
- **Demand evidence:** `[Interview/enquiry/research/pilot references, dates, limits]`
- **What remains unproven:** `[Unknowns]`

## 4. Offer boundary

**Plain-language definition:** `[What MPG does, for whom, to achieve what bounded outcome]`

### Included

- `[Deliverable/activity and acceptance condition]`

### Excluded

- `[Explicit non-deliverable; include adjacent capabilities that could be misunderstood]`

### Options or variants

| Variant | Customer condition | Added deliverable | Added capability/cost/risk | Separately approved? |
|---|---|---|---|---|
| `[Name]` | `[Condition]` | `[Output]` | `[Impact]` | `[Yes/No]` |

### Assumptions and client dependencies

| Assumption/input | Who supplies/validates it? | Needed by | Consequence if absent |
|---|---|---|---|
| `[Input]` | `[Function/client]` | `[Milestone]` | `[Delay/re-scope/decline]` |

## 5. Delivery design

- **Start condition:** `[What must be true before commitment/work begins?]`
- **End condition:** `[Definition of done]`
- **Major stages:** `[Discovery → ... → closure]`
- **MPG responsibility:** `[Exact boundary]`
- **Partner responsibility:** `[Exact boundary or NOT_APPLICABLE]`
- **Client responsibility:** `[Inputs, access, approvals, decisions]`
- **Expected communication/approval points:** `[Cadence and authority]`
- **Support/maintenance boundary:** `[Included period/event, exclusions, route]`
- **Change-control rule:** `[How impact and approval are recorded]`

## 6. Readiness dependencies

### Capabilities

| Capability ID | Required boundary | Present status | Evidence | Gap/action owner |
|---|---|---|---|---|
| `[CAP-ID]` | `[What must be performed]` | `[UNASSESSED / LEARNING / PRACTICING / COMPETENT / VALIDATED / PARTNER_DEPENDENT / NOT_REQUIRED]` | `[Reference]` | `[Action + owner]` |

### Tools, assets, and prerequisites

| Type | Registry ID | Requirement | Resource status | Cost/access known? | Gap/contingency |
|---|---|---|---|---|---|
| `[TOOL/ASSET/OTHER]` | `[ID]` | `[Why critical]` | `[UNKNOWN / REQUIRED / AVAILABLE / NOT_AVAILABLE / NOT_REQUIRED / PLANNED]` | `[Evidence]` | `[Action]` |

### Partners

| Partner capability | Partner ID | Approval scope | Due diligence | Fallback | Public disclosure allowed? |
|---|---|---|---|---|---|
| `[Capability or NOT_APPLICABLE]` | `[Public-safe ID]` | `[Exact scope]` | `[Status/evidence]` | `[Plan]` | `[Yes/No + approved words]` |

## 7. Readiness gates

| Gate | State | Evidence reference | Blocking gap / `NOT_APPLICABLE` rationale | Review trigger |
|---|---|---|---|---|
| G1 Customer Need | `[NOT_ASSESSED / BLOCKED / IN_PROGRESS / SATISFIED / NOT_APPLICABLE]` | | | |
| G2 Capability | | | | |
| G3 Tools & Technology | | | | |
| G4 Assets | | | | |
| G5 Delivery Process | | | | |
| G6 Quality Assurance | | | | |
| G7 Commercial Readiness | | | | |
| G8 Client Experience | | | | |
| G9 Legal / Compliance / Risk | | | | |
| G10 Capacity | | | | |
| G11 Proof | | | | |
| G12 Partner Readiness | | | | |
| G13 Marketing Readiness | | | | |

## 8. Commercial and capacity boundaries

- **Pricing method status/reference:** `[Not a fabricated price]`
- **Material cost drivers:** `[Labour, tools, third parties, revisions, support, fees, risk]`
- **Payment structure status:** `[TBD/evidence reference]`
- **Change conditions requiring re-quote:** `[Conditions]`
- **Concurrent delivery limit and basis:** `[Evidence, not optimism]`
- **Lead-time assumptions:** `[Conditions]`
- **Pause/decline triggers:** `[Capacity, capability, partner, legal, quality]`

## 9. Proof and claims

| Proposed material claim | Evidence | Scope/limitations | Permission | Expiry/review trigger |
|---|---|---|---|---|
| `[Exact words]` | `[Reference]` | `[What it does not prove]` | `[Status]` | `[Trigger]` |

## 10. Operating records

| Control | Approved record |
|---|---|
| Delivery SOP | `[ID/version or missing]` |
| QA checklist | `[ID/version or missing]` |
| Risk assessment | `[ID/version or missing]` |
| Pricing method | `[ID/version or missing]` |
| Discovery/onboarding | `[ID/version or missing]` |
| Proposal/quotation/terms | `[ID/version or missing]` |
| Handover/support | `[ID/version or missing]` |
| Pilot report | `[ID/version or NOT_YET_RUN]` |

## 11. Decision

- **Requested lifecycle transition:** `[FROM → TO or NONE]`
- **Unresolved blockers:** `[List; do not hide with “N/A”]`
- **Reviewer recommendation and rationale:** `[Do not advance / continue building / pilot / delivery ready / recommend market approval]`
- **Owner decision record:** `[ID, state, date, authority]`
- **Registry update completed:** `[Yes/No + reference]`
