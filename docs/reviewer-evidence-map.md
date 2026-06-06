# Review Guide - AI Security Redteam Lab

Updated: 2026-05-30

Use this page as the short path through the repository. It keeps the review grounded in the code, docs, commands, and boundaries that are already present.

## Summary

| Field | Notes |
|---|---|
| Lane | B2B AI safety and security |
| Core idea | Credential-free red-team fixtures for prompt injection, leakage, and unsafe tool pressure. |
| Primary reader | Security teams and AI product teams shipping model-backed features. |
| Stack | Python |

## Open First

1. Start with the README fast path and architecture section.
2. Open `docs/service-launch-playbook.md` only when reviewing the product or service angle.
3. Check the commands below before making claims about quality.
4. Skim the CI workflows and fixture data before deeper implementation review.
5. Read the boundaries section before presenting the project externally.

## Checks

| Purpose | Command |
|---|---|
| Test suite | `python -m pytest` |

## CI

- .github/workflows/architecture-blueprint.yml
- .github/workflows/ci.yml
- .github/workflows/dependency-review.yml
- .github/workflows/repository-health.yml
- .github/workflows/repository-surface.yml
- .github/workflows/secret-scan.yml

## Evidence

- pytest/ruff-style local verification path
- Scanner tests pass
- Reports are generated
- Unsafe examples are explainable

## Commercial Notes

| Possible offer | Working scope assumption |
|---|---|
| AI red-team workshop | $3k-$9k workshop |
| Prompt-injection regression pack | $10k-$35k custom policy pack |
| CI safety gate setup | $2k-$8k/month regression maintenance |

## Boundaries

- No claim of complete safety
- Customer policies must be scoped
- Handle findings confidentially

## Useful Metrics

- Finding severity distribution
- Regression recurrence
- Blocked unsafe pattern coverage
