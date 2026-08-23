# Evidence MVP — Decision Log

## Project principles

- Evidence is a verification layer, not another score.
- Grade the evidence, not the person.
- Verify broadly, disclose narrowly.
- Use synthetic data only.
- Final evidence status and the MX$30,000 threshold calculation must come from deterministic, inspectable rules.
- An LLM may assist with extraction or proposed classification, but it may not determine the authoritative verified amount.
- The MVP will not output a credit score, risk score, probability of default, or lending recommendation.

---

## Commit 1 — Initialize Streamlit Evidence MVP

### Decision

Start with the smallest possible working Streamlit application before adding data or verification logic.

### Included

- Basic Streamlit application
- Evidence title
- MVP claim
- Project principles
- requirements.txt
- .gitignore
- DECISIONS.md

### Explicitly not included yet

- Synthetic transaction dataset
- Evidence classification
- Verified amount calculation
- Threshold logic
- LLM functionality
- Third-party summary

### Reason

The first commit should prove that the development environment, project structure, Git repository, and Streamlit application work correctly before adding business logic.

---

## Commit 2 — Add Synthetic Maria Evidence Dataset

### Decision

Use a small, fully synthetic monthly dataset for María before implementing any verification rules.

### Included

- Synthetic SPEI transactions
- Synthetic Mercado Pago transactions
- Synthetic cash transactions
- Self-transfer example
- Refund / reversal example
- Duplicate transaction example
- Ambiguous transaction example
- Non-business transaction example
- Basic pandas loading
- Basic Streamlit table display

### Important boundary

This commit does not assign final evidence statuses or calculate the MX$30,000 threshold.

The dataset only provides structured inputs that the deterministic verification rules will evaluate in the next commit.

### Security

All records are synthetic. No real personal, banking, or transaction data is used.

---

## Commit 3 — Add Deterministic Evidence Classification Rules

### Decision

Final evidence status must be assigned by deterministic, inspectable rules rather than by an LLM.

### Included

- New verification.py module
- Final evidence categories:
  - Verified
  - Corroborated
  - Unresolved
  - Excluded
- Deterministic exclusion rules for:
  - Duplicate transactions
  - Refunds / reversals
  - Self-transfers
  - Non-business transactions
- Unresolved handling for ambiguous or incomplete evidence
- Cash remains Corroborated unless independent supporting evidence exists
- SPEI and Mercado Pago may be Verified when independent evidence supports the business inflow
- Final status and reason displayed in Streamlit

### Important boundary

The rule engine classifies evidence only. It does not yet calculate the directly verified total or evaluate the MX$30,000 threshold.

### LLM boundary

An LLM may later assist with extraction or propose a classification, but it cannot override the deterministic final evidence status.

---

## Commit 4 — Add Verified-Only Claim Engine

### Decision

The directly verified amount must be calculated only from transactions whose final evidence status is Verified.

### Included

- New claim_engine.py module
- MX$30,000 claim threshold
- Verified-only amount calculation
- Threshold met / Threshold not met result
- Claim result displayed in Streamlit
- Corroborated, Unresolved, and Excluded amounts remain outside the verified total

### Important boundary

The claim result is deterministic and based only on structured final evidence status.

No LLM output controls the verified amount or threshold result.

### Current synthetic result

Using the current synthetic María dataset:

- Directly verified amount: MX$31,600
- Claim threshold: MX$30,000
- Result: Threshold met

---

## Commit 5 — Add Evidence Dashboard and Explanations

### Decision

The MVP should make it easy for María to understand what counted, what did not count, why, and whether the threshold was met.

### Included

- Clear claim result section
- Directly Verified Amount
- Claim Threshold
- Threshold met / Threshold not met
- Separate totals for Verified, Corroborated, Unresolved, and Excluded evidence
- Clear explanation of each evidence category
- Persona-focused explanation for María
- Evidence table with final status, reason, and provenance

### Important boundary

Only Verified evidence contributes to the directly verified amount.

Corroborated, Unresolved, and Excluded evidence remain visible but separate.

### Persona test

María should be able to understand:

- what counted;
- what did not count;
- why each item received its status;
- whether the MX$30,000 threshold was met.

---

## Commit 6 — Add Minimal Third-Party Evidence Summary

### Decision

The third-party view should disclose only the minimum information needed to communicate the claim result and evidence coverage.

### Included

- Claim result
- Directly Verified Amount
- Evidence category totals
- Provenance
- Coverage limitations
- Clear narrow-disclosure explanation

### Privacy boundary

The third-party summary does not include:

- María's raw transaction history
- Counterparty details
- Relational data
- Credit score
- Risk score
- Probability of default
- Lending recommendation

### Design principle

Verify broadly, disclose narrowly.
---

## Session Close — Packet Added to Repository

### What changed today

- Added the finalized Week 2 Packet as `docs/PACKET.md`.
- Added the approved image-generated mockup as `docs/evidence_mockup.png`.
- Confirmed the packet includes the problem, exact user, success definition, mockup, Mermaid flowchart, Mermaid swimlane, benchmark, three-year long view, scope cut, architecture + stack, and test plan.

### Next move

Run the documented mechanical test pass, identify at least one real issue, fix it, and redeploy before beginning the persona test.

### Repository status

Packet files are ready to commit and push.