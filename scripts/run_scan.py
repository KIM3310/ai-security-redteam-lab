from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from redteam_lab.report import write_json_report, write_markdown_report
from redteam_lab.scanner import load_cases, scan_cases


def main() -> None:
    results = scan_cases(load_cases(ROOT / "examples" / "cases.json"))
    write_json_report(ROOT / "artifacts" / "redteam-report.json", results)
    write_markdown_report(ROOT / "artifacts" / "redteam-report.md", results)
    passed = sum(result.passed_expectation for result in results)
    print(f"redteam_scan passed={passed}/{len(results)}")
    if passed != len(results):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
