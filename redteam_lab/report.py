from __future__ import annotations

import json
from dataclasses import asdict
from pathlib import Path

from .scanner import ScanResult


def write_json_report(path: Path, results: list[ScanResult]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps([asdict(result) for result in results], indent=2), encoding="utf-8")


def write_markdown_report(path: Path, results: list[ScanResult]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["# AI Security Redteam Report", "", "| Case | Score | Findings | Expectation |", "|---|---:|---|---|"]
    for result in results:
        findings = ", ".join(f"{finding.category}:{finding.severity}" for finding in result.findings) or "none"
        expectation = "pass" if result.passed_expectation else "fail"
        lines.append(f"| {result.name} | {result.risk_score} | {findings} | {expectation} |")
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")
