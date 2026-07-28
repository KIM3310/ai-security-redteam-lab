from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path

from .policies import POLICIES, SEVERITY_SCORE


@dataclass(frozen=True)
class Finding:
    category: str
    severity: str
    guidance: str
    matched: str


@dataclass(frozen=True)
class ScanResult:
    name: str
    risk_score: int
    findings: tuple[Finding, ...]
    expected_categories: tuple[str, ...]
    passed_expectation: bool


def load_cases(path: Path) -> list[dict[str, object]]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    return list(raw["cases"])


def scan_case(case: dict[str, object]) -> ScanResult:
    text = str(case["input"])
    expected = tuple(str(item) for item in case.get("expected_categories", []))
    findings: list[Finding] = []
    for policy in POLICIES:
        match = policy.pattern.search(text)
        if match:
            findings.append(
                Finding(
                    category=policy.category,
                    severity=policy.severity,
                    guidance=policy.guidance,
                    matched=match.group(0),
                )
            )
    categories = {finding.category for finding in findings}
    expected_category_set = set(expected)
    risk_score = sum(SEVERITY_SCORE[finding.severity] for finding in findings)
    return ScanResult(
        name=str(case["name"]),
        risk_score=risk_score,
        findings=tuple(findings),
        expected_categories=expected,
        passed_expectation=categories == expected_category_set,
    )


def scan_cases(cases: list[dict[str, object]]) -> list[ScanResult]:
    return [scan_case(case) for case in cases]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("cases", type=Path)
    args = parser.parse_args()
    results = scan_cases(load_cases(args.cases))
    print(json.dumps([asdict(result) for result in results], indent=2))
    if not all(result.passed_expectation for result in results):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
