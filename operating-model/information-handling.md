# Information Handling

> **Document:** Information Handling
> **Status:** RECOMMENDED — pending Stage 0 owner acceptance
> **Stage:** Stage 0 — Governance and Source of Truth
> **Owner:** MPG Founder
> **Last Updated:** 2026-08-28
> **Public Safe:** Yes
> **Authority:** Public-repository safety requirements in MPG Company OS Master Repository Bootstrap v2

## Public repository rule

This repository is public. Everything committed to it must be safe for unrestricted public disclosure now and in Git history. A later deletion does not reliably remove disclosed information from clones, caches, logs, pull requests, or commit history.

Only **PUBLIC** information may be stored here. If confidential operations require repository storage, use approved private storage or formally convert the repository to private **before** placing the information there, then reassess access, retention, backup, and security controls. Private visibility alone does not make every type of sensitive information appropriate to store.

## Information classifications

| Classification | Meaning | Public repository |
|---|---|---:|
| `PUBLIC` | Approved for unrestricted release; accurate, permissioned, and non-sensitive. | Allowed |
| `INTERNAL` | Routine non-public operating information whose disclosure could create confusion, nuisance, or commercial disadvantage. | Prohibited |
| `CONFIDENTIAL` | Client, partner, personnel, contract, commercial, or operational information shared for a limited purpose. | Prohibited |
| `RESTRICTED` | Secrets, credentials, identity/financial data, sensitive security/legal records, or other information with severe disclosure impact. | Prohibited |

When uncertain, treat information as `CONFIDENTIAL` until an authorized owner classifies it. “Available to an AI tool” or “not personally identifying” does not mean public.

## Never commit

- passwords, passcodes, API tokens, session data, private keys, recovery codes, or credentials;
- personal IDs, bank/payment details, personal financial records, signatures, or sensitive personal data;
- private client information, source data, access, communications, deliverables, environments, or unapproved names;
- supplier or partner private contacts, non-public diligence, contracts, pricing, disputes, or banking information;
- confidential contracts, legal advice, insurance records, private financial statements, tax records, or internal credentials;
- exploitable vulnerability details, private infrastructure data, production logs, or secret configuration;
- data whose publication rights, consent, license, or ownership are uncertain;
- completed client-facing templates containing real confidential information.

Do not place secrets in examples, screenshots, fixtures, issue text, commit messages, branches, generated files, terminal captures, or encoded/obfuscated form. Placeholders must be unmistakably fake, such as `<CLIENT_PRIVATE_REFERENCE>`.

## Information handling lifecycle

For every material collection or use:

1. **Define purpose:** collect only what the decision or delivery requires.
2. **Classify:** identify sensitivity, owner, subjects, obligations, and public/private location before collection.
3. **Authorize:** limit access to roles and tools with a real need.
4. **Transfer safely:** use approved channels; verify recipients and avoid public links by default.
5. **Use minimally:** do not copy full datasets where a reference, sample, or aggregate will do.
6. **Retain deliberately:** define record owner and retention/closure trigger; avoid uncontrolled duplicates.
7. **Dispose safely:** use the approved private-system process and consider backups/legal holds.
8. **Review:** reassess on tool, partner, purpose, jurisdiction, or relationship changes.

This policy does not invent a retention period or claim compliance with any jurisdiction. Required legal or professional review must be obtained for the actual operating context.

## Public-safe evidence references

Governance records may reference sensitive evidence using a stable, non-revealing identifier and approved private location. The public reference must not disclose client identity, contact details, confidential outcome, contract terms, vulnerability, exact storage path, access token, or other inference-enabling detail.

Redaction is acceptable only when the remaining artifact is genuinely public-safe and hidden content cannot be recovered from metadata, revision history, comments, layers, tracked changes, filenames, or embedded media. When in doubt, do not commit the artifact.

## Client and partner work

- Obtain authority and define purpose before receiving data or system access.
- Use least privilege, separate accounts where practical, and secure credential sharing; never paste credentials into project documents.
- Define who owns, hosts, accesses, backs up, exports, and deletes data.
- Do not use a client or partner name, logo, testimonial, results, screenshots, or work sample publicly without explicit permission.
- Partner access must follow due diligence, contract, classification, and client commitments.
- Handover must transfer access securely and remove MPG or partner access when no longer required.

## Tools, automation, and AI

Before entering non-public information into a SaaS, AI system, automation, code host, analytics tool, or partner environment, review data use, training terms, retention, access, location, subprocessors, export/deletion, incident handling, and client/legal constraints. Approval of a tool for public content does not approve it for confidential client data.

Use synthetic or de-identified test data where possible. Do not ask AI to reconstruct omitted sensitive values or summarize data it is not authorized to receive. AI output may expose or infer inputs and must be reviewed before publication.

## Pre-commit/publication check

Before committing or publishing, verify:

- every file, diff, filename, metadata field, embedded asset, link, and generated output is public-safe;
- no secret, private contact, personal/client/partner identifier, confidential term, or production data is present;
- permissions and claim evidence exist;
- example values are clearly synthetic;
- sensitive evidence is referenced, not copied;
- automated checks have run where available.

Automated scanning assists review but cannot authorize disclosure.

## Suspected exposure

If non-public information may have been exposed:

1. stop further sharing and notify the MPG Founder through a private channel;
2. do not repeat the sensitive value in an issue, chat, commit, or public report;
3. identify affected system, data class, recipients, and history privately;
4. rotate/revoke credentials and contain access where relevant;
5. preserve safe incident evidence and seek legal/client/partner guidance as required;
6. remediate Git history or external copies only with an approved incident plan—ordinary deletion is not enough;
7. record lessons and update controls without publishing the sensitive details.

## Template warning

Templates in this repository are public-safe while blank. Completed discovery notes, proposals, quotations, kickoff records, handovers, partner diligence, risk reviews, and case-study evidence may become `INTERNAL`, `CONFIDENTIAL`, or `RESTRICTED`; store completed copies in the approved system for their classification, not here.
