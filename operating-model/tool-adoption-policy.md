# Tool Adoption Policy

> **Document:** Tool Adoption Policy
> **Status:** RECOMMENDED — pending Stage 0 owner acceptance
> **Stage:** Stage 0 — Governance and Source of Truth
> **Owner:** MPG Founder
> **Last Updated:** 2026-08-28
> **Public Safe:** Yes
> **Authority:** Resource-readiness and anti-scatter rules in MPG Company OS Master Repository Bootstrap v2

## Policy

MPG adopts a tool only when a defined business capability or control needs it and the expected value justifies its full cost, risk, and operating burden. A popular product, free trial, discount, integration list, founder interest, or future possibility is not a business requirement.

Buying, installing, or learning a tool does not validate a capability, satisfy a service gate, change lifecycle status, or authorize marketing.

## Required tool record

Before approval, the tool registry and evaluation must identify:

- tool and vendor;
- exact purpose and capability/service IDs enabled;
- present resource status and requested decision;
- current workaround or alternative, including “do nothing”;
- required account, owner, user roles, and administration responsibility;
- setup, subscription, usage, transaction, integration, training, migration, support, tax/fee, and exit costs;
- whether cost and account availability are known;
- data classifications, client data use, and security/privacy review;
- reliability, support, compatibility, accessibility, and continuity needs;
- export, backup, deletion, portability, and vendor-lock-in controls;
- trial evidence, success criteria, risks, and review date;
- owner approval and any use restrictions.

Use `UNKNOWN`, `TBD`, or an appropriate resource status where evidence is absent. Never infer an account exists.

## Adoption workflow

1. **Define need:** state the blocked outcome, users, frequency, scale, and required control.
2. **Check process first:** confirm the problem is not primarily unclear ownership, poor workflow, missing skill, or premature service design.
3. **Compare options:** include current tools, manual process, open standards, partner capability, delay, and no purchase.
4. **Screen information risk:** determine what data and access the tool would receive before a trial.
5. **Estimate total cost:** include time and exit costs, not only subscription price.
6. **Run a bounded trial if needed:** use public/synthetic data unless confidential use is separately approved; measure stated criteria.
7. **Decide:** reject, defer, approve with restrictions, or approve for a defined purpose. Record owner authority.
8. **Implement deliberately:** assign administration, least privilege, configuration, documentation, backup/export, training, and support.
9. **Review:** confirm use, value, cost, incidents, changed terms, duplication, and continuing need.
10. **Retire:** export required records, transition workflows, remove access/integrations, address retention, and stop cost.

Tool procurement must comply with the WIP policy; speculative configuration of tools for future services can consume the secondary capability-development slot.

## Evaluation criteria

### Capability and fit

- Which required workflow or control cannot be met adequately now?
- Does the tool support the defined scope without forcing unnecessary process complexity?
- Are required integrations real, tested needs rather than feature wish lists?
- Can MPG operate and support the tool with available capability?

### Economics

- What is the full cost at expected and downside usage?
- Which currency, taxes/fees, usage tiers, seats, storage, messages, transactions, or partner markups vary?
- What work, risk, or missed opportunity is credibly reduced?
- Is cost recoverable within an approved service pricing method without inventing demand?

### Information and security

- What `PUBLIC`, `INTERNAL`, `CONFIDENTIAL`, or `RESTRICTED` information would enter the tool?
- What are the vendor's data-use, training, retention, subprocessors, location, breach, export, and deletion terms?
- Are least privilege, MFA, audit records, separation, backup, and secure credential handling available where needed?
- Do client, partner, legal, or jurisdiction requirements require qualified review?

### Reliability and exit

- What happens during outage, account loss, price change, vendor failure, or discontinued functionality?
- Can MPG export data in a usable format and rebuild critical workflow elsewhere?
- Who owns domains, accounts, automations, source files, and client access?
- Is there a manual fallback for critical operations?

## Approval rules

The MPG Founder approves material spend, new systems of record, tools handling confidential/restricted information, and tools creating significant client or vendor dependency, unless an accepted decision delegates that authority.

Approval is purpose- and data-classification-specific. Approval for marketing graphics does not permit use for client records. A tool needed by `PARTNER_DELIVERY` remains a service dependency even if the partner owns it; access, continuity, cost, data, and disclosure must still be assessed.

G3 can be `SATISFIED` only when every critical tool is available and the service-specific reliability, cost, ownership, access, information, and contingency evidence is current. Tool approval alone does not make G3 or any other gate `SATISFIED`.

## AI and automation safeguards

Before adopting tools for AI/workflow automation, also define the business problem, stable source workflow, data/security review, human fallback, monitoring, error handling, vendor and usage costs, client ownership/access, maintenance expectations, and realistic evidence-based claims. Do not buy a platform to create a vague “AI transformation” offer.

## Review and retirement triggers

Review when price/terms, ownership, integration, service scope, data classification, vendor, regulation, incident history, usage, or alternatives materially change. Retire or restrict a tool when it is unused, duplicative, unaffordable, insecure for the intended data, unsupported, non-portable beyond accepted risk, or no longer tied to an active/planned capability.

Do not store credentials, private account identifiers, invoices, client data, or confidential vendor terms in the public registry. Use public-safe statuses and references to approved private records.
