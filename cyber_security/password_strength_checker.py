#!/usr/bin/env python3
"""Password strength checker (entropy-based) with actionable feedback.

Usage:
  python -m cyber_security.password_strength_checker "P@ssw0rd!"
  python -m cyber_security.password_strength_checker --help
"""
from __future__ import annotations

import argparse
import math
import re
import sys
from dataclasses import dataclass


@dataclass
class StrengthResult:
    bits_of_entropy: float
    estimated_search_space: int
    category: str
    feedback: list[str]


CHARSETS = {
    "lower": "abcdefghijklmnopqrstuvwxyz",
    "upper": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "digits": "0123456789",
    "symbols": "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~",
    "space": " ",
}


def estimate_entropy(password: str) -> StrengthResult:
    if not password:
        return StrengthResult(0.0, 1, "empty", ["Password is empty."])

    used = 0
    charspace = 0

    def uses(charset: str) -> bool:
        return any(c in charset for c in password)

    if uses(CHARSETS["lower"]):
        charspace += 26
        used += 1
    if uses(CHARSETS["upper"]):
        charspace += 26
        used += 1
    if uses(CHARSETS["digits"]):
        charspace += 10
        used += 1
    if uses(CHARSETS["symbols"]):
        charspace += len(CHARSETS["symbols"])
        used += 1
    if uses(CHARSETS["space"]):
        charspace += 1
        used += 1

    # Fallback if classifier failed for some unusual unicode input
    if charspace == 0:
        unique_chars = len(set(password))
        charspace = max(unique_chars, 1)

    length = len(password)
    # Shannon-style estimate: log2(charspace^length) = length * log2(charspace)
    entropy = length * math.log2(max(charspace, 1))

    # Heuristics reduce entropy for common patterns
    penalties = 0.0
    common_subs = [("password", 10), ("1234", 8), ("qwerty", 8)]
    lower_pw = password.lower()
    for patt, pen in common_subs:
        if patt in lower_pw:
            penalties += pen
    if re.search(r"^(?:[A-Za-z]+\d+|\d+[A-Za-z]+)$", password):
        penalties += 5
    entropy = max(0.0, entropy - penalties)

    # Category mapping
    if entropy < 28:
        category = "very weak"
    elif entropy < 36:
        category = "weak"
    elif entropy < 60:
        category = "moderate"
    elif entropy < 80:
        category = "strong"
    else:
        category = "very strong"

    feedback: list[str] = []
    if length < 12:
        feedback.append("Use at least 12-16 characters.")
    if used < 3:
        feedback.append("Mix upper/lowercase, digits, and symbols.")
    if re.search(r"(.)\\1{2,}", password):
        feedback.append("Avoid repeated characters.")
    if re.search(r"(\d){4,}", password):
        feedback.append("Avoid long digit sequences.")

    estimated_space = int(2 ** entropy) if entropy < 60 else int(10 ** (entropy / math.log2(10)))
    return StrengthResult(entropy, estimated_space, category, feedback)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Estimate password strength and provide feedback.")
    parser.add_argument("password", nargs="?", help="Password string to evaluate. If omitted, read from stdin.")
    parser.add_argument("-q", "--quiet", action="store_true", help="Print only the entropy and category.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    pwd = args.password
    if pwd is None:
        pwd = sys.stdin.read().rstrip("\n")

    result = estimate_entropy(pwd)

    if args.quiet:
        print(f"{result.bits_of_entropy:.2f} bits\t{result.category}")
        return 0

    print(f"Entropy: {result.bits_of_entropy:.2f} bits")
    print(f"Estimated search space: ~{result.estimated_search_space}")
    print(f"Category: {result.category}")
    if result.feedback:
        print("Feedback:")
        for item in result.feedback:
            print(f" - {item}")
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
