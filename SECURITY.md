# Security and Public Information Policy

| Metadata | Value |
|---|---|
| Document | Repository security and disclosure policy |
| Status | ACTIVE |
| Stage | Stage 0 — Governance and Source of Truth |
| Owner | MPG Founder |
| Last Updated | 2026-08-28 |
| Public Safe | Yes |
| Authority | Governing minimum for information committed to this public repository |

## Public repository boundary

This repository and its Git history are public. Every file, commit, branch, issue, pull request, workflow log, and generated artifact must be treated as publicly readable and permanently replicable.

This repository may hold public-safe governance structures, sanitized templates, non-confidential policies, and approved public facts. It is **not** an approved store for confidential company operations.

## Never commit

- passwords, API keys, access tokens, private keys, recovery codes, or credentials;
- `.env` files containing values, cloud/service credentials, or production configuration;
- personal IDs, bank information, personal financial details, or private addresses;
- private client information, client credentials, unapproved client names, or production data;
- supplier private contacts, private price terms, or confidential sourcing records;
- private partner information, due-diligence evidence, or non-public relationship terms;
- sensitive contracts, private financial statements, legal correspondence, or insurance records;
- commercially sensitive plans, account exports, private logs, database files, or backups.

File names, metadata, screenshots, logs, examples, and commit messages can also leak information. Use redacted or synthetic examples and review generated outputs before commit.

## Approved handling for confidential operations

Confidential operational material must eventually live in owner-approved private storage with suitable access control, retention, backup, and recovery rules. Before MPG stores confidential operations in this repository, the owner must either:

1. approve an information classification and storage approach that keeps the material outside this public repository; or
2. explicitly reassess and change repository visibility, then review access and history risks.

Changing visibility does not remove information already copied from public history. Do not commit first and make the repository private later as a security strategy.

## Reporting a vulnerability or exposure

Do **not** open a public issue containing secret values, exploit details, personal data, or other sensitive evidence.

Report the issue privately to the MPG Founder through an established private channel. If GitHub private vulnerability reporting or a private security advisory is enabled for the repository, it may be used. Include only the minimum information needed to locate and reproduce the issue:

- affected file, commit, workflow, or component;
- impact and conditions;
- safe reproduction steps;
- whether a credential or private record may have been exposed;
- suggested containment, if known.

No public security-contact address is asserted by this baseline. If no verified private channel is available, disclose only that a private reporting route is needed; do not post sensitive details publicly.

## If sensitive information is found

1. Stop further distribution and avoid copying the value into chat, issues, or logs.
2. Notify the MPG Founder privately.
3. Revoke or rotate exposed credentials immediately through the relevant provider.
4. Remove the information from the current working version using a reviewable change.
5. Assess Git history, caches, CI logs, forks, downloads, and connected systems.
6. Decide any history rewrite, provider notification, or affected-party response with explicit owner authorization and appropriate specialist advice.
7. Record a public-safe lesson or control improvement without reproducing the sensitive value.

Deleting a current file does not erase Git history. Secret rotation is required even if cleanup is planned.

## Repository security expectations

- Keep dependencies and automation minimal and reviewable.
- Pin or constrain third-party workflow actions where practical.
- Grant workflows and integrations only the permissions they require.
- Do not print environment values, tokens, private files, or sensitive API responses in logs.
- Review scripts that derive public files from internal records; generated content is subject to the same publication rules.
- Validate registries before publication. No service may be publicly generated unless it is `ACTIVE` and `marketingApproved = true`.
- Research current platform security guidance when controls or external services change.

## Scope of security claims

This document is a repository-handling baseline, not a certification or claim of legal, regulatory, or technical compliance. Any future service-specific security, privacy, licensing, insurance, or regulatory claim requires evidence and appropriate professional verification.

The latest `main` branch is the supported governance baseline. Historical snapshots are retained for auditability but may not contain the latest controls.
