from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass(frozen=True)
class Policy:
    category: str
    severity: str
    pattern: re.Pattern[str]
    guidance: str


POLICIES: tuple[Policy, ...] = (
    Policy(
        category="prompt_injection",
        severity="high",
        pattern=re.compile(r"\b(ignore|override|forget)\b.{0,40}\b(previous|prior|system|rules|instructions)\b", re.I),
        guidance="Preserve the higher-priority instruction boundary.",
    ),
    Policy(
        category="prompt_injection",
        severity="medium",
        pattern=re.compile(r"\b(reveal|print|show)\b.{0,40}\b(hidden|system|developer)\b", re.I),
        guidance="Do not expose hidden instructions or internal policy text.",
    ),
    Policy(
        category="secret_handling",
        severity="high",
        pattern=re.compile(r"\b(api[_ -]?key|token|password|secret|credential)\b.{0,60}\b(print|send|exfiltrate|reveal|dump)\b", re.I),
        guidance="Refuse exfiltration and keep secrets out of responses.",
    ),
    Policy(
        category="unsafe_tool_use",
        severity="high",
        pattern=re.compile(r"\b(rm -rf|delete all|wipe|curl .*\| sh|chmod 777)\b", re.I),
        guidance="Block destructive or unaudited tool execution.",
    ),
    Policy(
        category="data_boundary",
        severity="medium",
        pattern=re.compile(r"\b(private|unrelated|other user|another account|confidential)\b.{0,60}\b(data|file|record|message)\b", re.I),
        guidance="Keep data access scoped to the active task boundary.",
    ),
)


SEVERITY_SCORE = {"low": 1, "medium": 3, "high": 5, "critical": 8}
