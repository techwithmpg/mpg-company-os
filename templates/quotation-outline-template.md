# Quotation Outline Template

> **Document:** Quotation Outline Template
> **Template Status:** CONTROLLED TEMPLATE
> **Stage:** Stage 0 — Governance and Source of Truth
> **Template Owner:** MPG Founder
> **Last Updated:** 2026-08-28
> **Public Safe:** Yes while blank; completed quotations are confidential
> **Authority:** Commercial Readiness and Information Handling controls

## Use rule

Every amount must derive from an approved pricing method, defined scope, real cost assumptions, and current capacity. Never fill a gap with an arbitrary price. Store completed quotations in approved private storage.

## 1. Quote control

| Field | Entry |
|---|---|
| Quotation ID / revision | `[ID]` |
| Client private reference | `[ID]` |
| Service and scope version | `[IDs]` |
| Proposal/discovery reference | `[IDs]` |
| Service authorization | `[ACTIVE + marketing approval, or controlled pilot ID]` |
| Issue date / valid through | `[Dates/condition]` |
| Currency / market | `[Explicit]` |
| Prepared/reviewed by | `[Functions]` |
| Classification/location | `[CONFIDENTIAL / approved private reference]` |

Revision rule: each changed quote receives a new revision, reason, approver, and clear status for the superseded version.

## 2. Priced scope

| Line | Deliverable/fee | Scope and acceptance reference | Quantity/unit/basis | Unit amount | Line amount | Tax/fee treatment | Third-party/recurring? |
|---:|---|---|---|---:|---:|---|---|
| 1 | `[Item]` | `[Scope ID]` | `[Basis]` | `[Approved value]` | `[Calculated]` | `[Known treatment/TBD]` | `[Who contracts/pays]` |

| Summary | Amount |
|---|---:|
| Subtotal | `[Calculated]` |
| Approved discount/adjustment and authority | `[Value/reference or NONE]` |
| Taxes/fees | `[Calculated or clearly excluded/pending verification]` |
| Quoted total | `[Calculated currency total]` |

Do not imply tax, customs, commission, or legal treatment has been verified when it has not. State who must confirm it.

## 3. Pricing basis and assumptions

- **Pricing method/version:** `[Reference]`
- **Cost-floor check and reviewer:** `[Private evidence reference]`
- **Margin/risk review:** `[Evidence without exposing confidential calculation publicly]`
- **Included revision/usage/support allowance:** `[Exact boundary]`
- **Client inputs and timing assumed:** `[Entry]`
- **Volume, complexity, platform, partner, or currency assumptions:** `[Entry]`
- **Unknown material cost and resolution:** `[TBD + owner; do not issue final quote if material]`

## 4. Exclusions and variable charges

- **Not included:** `[Work/costs]`
- **Client-paid third-party items:** `[Domains, hosting, licenses, ads, freight, duties, etc. only if relevant]`
- **Pass-through/markup/commission treatment:** `[Approved transparent rule]`
- **Conditions requiring a revised quote:** `[Scope, inputs, delay, volume, exchange, third-party terms, risk]`
- **Out-of-scope/change-request rate or calculation method:** `[Approved reference]`

## 5. Payment and commercial conditions

| Milestone/event | Amount/percentage | Due condition | Work/release dependency |
|---|---:|---|---|
| `[Event]` | `[Approved]` | `[Invoice/acceptance/date]` | `[Start/handover/etc.]` |

- **Payment method/channel:** `[Approved method; never bank credentials in repository]`
- **Deposit/start rule:** `[Terms]`
- **Late payment/pause/cancellation/refund/remedy:** `[Approved terms reference]`
- **Quote expiration:** `[Capacity, cost, currency, scope must be revalidated]`
- **Contracting entity/partner payment boundary:** `[Accurate disclosure]`

## 6. Acceptance

Acceptance of the quote is subject to `[proposal/scope/terms/contract IDs]`. State the authorized acceptance method, signatory/role, and any payment precondition: `[Entry]`.

## 7. Internal approval

- [ ] Service/proposal type is authorized.
- [ ] Scope and acceptance criteria are linked.
- [ ] Full cost and material uncertainties are reviewed.
- [ ] Calculations, currency, taxes/fees, third-party items, and totals are checked.
- [ ] Payment and change controls align with proposal/terms.
- [ ] Capacity and validity period are current.
- [ ] Quote contains no unsupported claims or confidential information in the wrong system.

**Reviewer / approval record / date:** `[Entry]`

## Revision history

| Revision | Date | Reason / commercial impact | Approved by | Supersedes/status |
|---|---|---|---|---|
| `[Rev]` | `[Date]` | `[Change]` | `[Authority]` | `[Prior ID / VOID]` |
