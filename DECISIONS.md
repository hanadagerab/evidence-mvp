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