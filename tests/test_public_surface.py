"""Regression tests for the public search and service surface."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INQUIRY_URL = (
    "https://kim3310-doeon-kim-portfolio.pages.dev/"
    "?offer=ai-security-redteam-lab&inquiry=agent-reliability-audit#private-inquiry"
)


def test_service_offer_uses_central_agent_reliability_audit_lane() -> None:
    for relative_path in ("docs/service-offer.json", "site/service-offer.json"):
        offer = json.loads((ROOT / relative_path).read_text(encoding="utf-8"))

        assert offer["lead_capture_url"] == INQUIRY_URL
        assert offer["commerce"]["lane_id"] == "agent-reliability-audit"
        assert offer["commerce"]["lane_name"] == "Agent Reliability Audit"


def test_search_growth_notes_use_central_private_inquiry_route() -> None:
    notes = (ROOT / "docs/search-growth-implementation.md").read_text(encoding="utf-8")

    assert INQUIRY_URL in notes
    assert "central private inquiry route" in notes
    assert "offer=ai-security-redteam-lab" in notes
    assert "inquiry=agent-reliability-audit" in notes
    assert "GitHub Issue Form" not in notes
