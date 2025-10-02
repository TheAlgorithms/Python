#!/usr/bin/env python3
"""URL Analyzer: heuristic checks for phishing and IDN homograph risks.

Usage:
  python -m cyber_security.url_analyzer https://example.com
"""

from __future__ import annotations

import argparse
import idna  # type: ignore
import re
import sys
from urllib.parse import urlparse


SUSPICIOUS_TLDS = {
    "zip",
    "mov",
    "top",
    "xyz",
}


def is_punycode(label: str) -> bool:
    return label.lower().startswith("xn--")


def has_mixed_scripts(label: str) -> bool:
    # crude mixed script detection: Latin + Cyrillic/Greek
    latin = re.search(r"[A-Za-z]", label)
    cyrillic = re.search(r"[\u0400-\u04FF]", label)
    greek = re.search(r"[\u0370-\u03FF]", label)
    scripts = sum(bool(x) for x in (latin, cyrillic, greek))
    return scripts >= 2


def looks_like_homograph(label: str) -> bool:
    # very rough: replace common confusables and see if it becomes a known brand
    confusable_map = {
        "0": "o",
        "1": "l",
        "3": "e",
        "5": "s",
        "@": "a",
        "$": "s",
        "!": "i",
        "і": "i",  # Cyrillic i
        "е": "e",  # Cyrillic e
        "о": "o",  # Cyrillic o
    }
    brands = {"google", "apple", "microsoft", "paypal", "facebook", "amazon"}
    norm = label.lower()
    for k, v in confusable_map.items():
        norm = norm.replace(k, v)
    return any(b in norm for b in brands)


def analyze(url: str) -> list[str]:
    issues: list[str] = []
    try:
        parsed = urlparse(url)
    except Exception:
        return ["Invalid URL format."]

    if parsed.scheme not in {"http", "https"}:
        issues.append("Non-HTTP(S) scheme.")

    hostname = parsed.hostname or ""
    if not hostname:
        issues.append("Missing hostname.")
        return issues

    labels = hostname.split(".")
    decoded_labels = []
    for label in labels:
        if is_punycode(label):
            issues.append("Punycode present (possible IDN homograph).")
            try:
                decoded_labels.append(idna.decode(label))
            except Exception:
                decoded_labels.append(label)
        else:
            decoded_labels.append(label)

    decoded_host = ".".join(decoded_labels)

    for label in decoded_labels:
        if has_mixed_scripts(label):
            issues.append("Mixed Unicode scripts in hostname label.")
        if looks_like_homograph(label):
            issues.append("Label resembles well-known brand (possible homograph).")

    tld = labels[-1].lower() if labels else ""
    if tld in SUSPICIOUS_TLDS:
        issues.append(f"Suspicious TLD: .{tld}")

    # URL path query heuristics
    path_query = (parsed.path or "") + ("?" + parsed.query if parsed.query else "")
    if re.search(r"(?i)login|verify|update|secure|account", path_query):
        issues.append("Phishing related keyword in path/query.")
    if re.search(r"@", parsed.netloc):
        issues.append("@ in netloc may hide true host (userinfo trick).")

    return issues


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Analyze a URL for phishing/IDN risks."
    )
    parser.add_argument("url", help="URL to analyze")
    parser.add_argument(
        "--quiet", action="store_true", help="Exit code only: 0 safe-ish, 1 suspicious"
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    issues = analyze(args.url)

    if args.quiet:
        return 1 if issues else 0

    if issues:
        print("Suspicious indicators:")
        for item in issues:
            print(f" - {item}")
        return 1

    print("No obvious issues detected.")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
