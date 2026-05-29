# Reviewer Evidence Map - AI Security Redteam Lab

Updated: 2026-05-29

This document is the short path for a technical reviewer, engineering leader, product evaluator, or buyer who wants to understand what this repository proves without wandering through every file.

## One-Line Proof

**B2B AI safety and security.** Credential-free red-team fixtures for prompt injection, leakage, and unsafe tool pressure.

## Audience and Commercial Angle

| Lens | Answer |
|---|---|
| Primary reviewer | Security teams and AI product teams shipping model-backed features. |
| Technical signal | Can the project be explained, verified, bounded, and extended like a real product surface? |
| Buyer signal | Is there a narrow operational pain, a runnable proof path, and a risk-aware pilot shape? |
| Stack signal | Python |

## Seven-Minute Review Route

1. Read the README `Product and Review Surface` and `Reviewer Fast Path` sections.
2. Open `docs/monetization-playbook.md` to understand the buyer, offer ladder, and GTM hypothesis.
3. Run or inspect the strongest local quality gate below.
4. Inspect CI workflow definitions and test fixtures before deeper implementation review.
5. Check the risk boundaries so claims stay credible and not overextended.

## Verification Commands

| Purpose | Command |
|---|---|
| Test suite | `python -m pytest` |

## CI and Automation Surface

- .github/workflows/architecture-blueprint.yml
- .github/workflows/ci.yml
- .github/workflows/dependency-review.yml
- .github/workflows/repository-health.yml
- .github/workflows/repository-surface.yml
- .github/workflows/secret-scan.yml

## Evidence Inventory

- pytest/ruff-style local verification path
- Scanner tests pass
- Reports are generated
- Unsafe examples are explainable

## Commercialization Snapshot

| Offer | Pricing hypothesis |
|---|---|
| AI red-team workshop | $3k-$9k workshop |
| Prompt-injection regression pack | $10k-$35k custom policy pack |
| CI safety gate setup | $2k-$8k/month regression maintenance |

## Risk Boundaries

- No claim of complete safety
- Customer policies must be scoped
- Handle findings confidentially

## Metrics That Matter

- Finding severity distribution
- Regression recurrence
- Blocked unsafe pattern coverage

## Review Verdict

This repository should be evaluated as part of the broader KIM3310 portfolio: it is strongest when the reviewer sees the link between a concrete implementation, a documented verification path, and an externally credible operating story.
