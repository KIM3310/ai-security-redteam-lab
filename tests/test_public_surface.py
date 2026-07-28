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


def test_cloudflare_adsense_static_surface_is_ready() -> None:
    adsense_client = "ca-pub-4973160293737562"
    ads_txt = "google.com, pub-4973160293737562, DIRECT, f08c47fec0942fa0"
    canonical = "https://ai-security-redteam-lab.pages.dev/"

    assert (ROOT / "site" / "ads.txt").read_text(encoding="utf-8").strip() == ads_txt

    index = (ROOT / "site" / "index.html").read_text(encoding="utf-8")
    assert f'name="google-adsense-account" content="{adsense_client}"' in index
    assert f"adsbygoogle.js?client={adsense_client}" in index

    for filename in ("privacy.html", "terms.html"):
        assert (ROOT / "site" / filename).exists()

    sitemap = (ROOT / "site" / "sitemap.xml").read_text(encoding="utf-8")
    assert "https://ai-security-redteam-lab.pages.dev/privacy.html" in sitemap
    assert "https://ai-security-redteam-lab.pages.dev/terms.html" in sitemap

    llms = (ROOT / "site" / "llms.txt").read_text(encoding="utf-8")
    assert f"Canonical URL: {canonical}" in llms

    offer = json.loads((ROOT / "site" / "service-offer.json").read_text(encoding="utf-8"))
    assert offer["canonical_url"] == canonical
    assert offer["structured_data"]["url"] == canonical
    assert offer["structured_data"]["offers"][0]["url"] == canonical

    wrangler = json.loads((ROOT / "wrangler.jsonc").read_text(encoding="utf-8"))
    assert wrangler["name"] == "ai-security-redteam-lab"
    assert wrangler["pages_build_output_dir"] == "site"
