# AGENTS — Domain Overrides

**Domain:** <domain-slug>  
**Scope:** Specializations to `ops/AGENTS.md`. Omit sections you do not override. The stricter rule always wins.

---

## A) Determinism & Output (optional)
- **Default output format for this domain:** <markdown|json|plain>
- **Section/Key order requirements (if any):** <list or leave empty>
- **Stop sequences (if any):** <["```", "</END>"]>

## B) Token & Memory (optional)
- **context_budget_hint:** <integer or inherit>
- **summarize_at:** 0.80   # summarize prior turns at 80% of budget
- **drop_examples_at:** 0.90

## C) Inputs & Validation (optional)
- **additional_required_fields:** <["foo_id", "region"] or leave empty>
- **field constraints:** <notes, e.g., "region ∈ {us, eu, apac}">

## D) Safety (required only if stricter)
- **pii:** <reject|redact|allow>   # if stricter than global
- **redlines_additions:** <["no medical advice", "no legal advice"]>
- **disclaimers (append):** <["This is informational, not advice."]>

## E) Cross‑Domain (optional)
- **allow_cross_domain:** false   # default false; set true only if explicitly needed
- **allowed_domains:** <["research"] or leave empty>

## F) Failure Handling (optional)
- **on_ambiguity:** propose 2 interpretations, choose safer, and note choice.
- **on-missing-input:** ask exactly one targeted question, then proceed.

## G) Maintainer Notes (optional)
- **owner:** parlau
- **contact:** vparlau@gmail.com
- **changelog:** see this domain’s `CHANGELOG.md`
