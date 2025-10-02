#!/usr/bin/env python3
"""Hash cracker for md5/sha1/sha256 using a wordlist.

Usage:
  python -m cyber_security.hash_cracker --algo sha256 --hash <hash> --wordlist words.txt
"""

from __future__ import annotations

import argparse
import hashlib
import sys
from typing import Iterable


ALGORITHMS = {"md5", "sha1", "sha256"}


def iter_wordlist(path: str) -> Iterable[str]:
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            word = line.rstrip("\n\r")
            if word:
                yield word


def crack_hash(target_hash: str, algo: str, wordlist_path: str) -> str | None:
    algo = algo.lower()
    if algo not in ALGORITHMS:
        raise ValueError(f"Unsupported algorithm: {algo}")

    target_hash = target_hash.lower()
    for candidate in iter_wordlist(wordlist_path):
        h = hashlib.new(algo)
        h.update(candidate.encode("utf-8"))
        if h.hexdigest().lower() == target_hash:
            return candidate
    return None


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Hash cracker using a wordlist.")
    parser.add_argument(
        "--algo", choices=sorted(ALGORITHMS), default="sha256", help="Hash algorithm"
    )
    parser.add_argument("--hash", required=True, help="Target hex digest")
    parser.add_argument("--wordlist", required=True, help="Path to wordlist file")
    parser.add_argument(
        "--quiet", action="store_true", help="Only print the cracked password if found"
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    try:
        result = crack_hash(args.hash, args.algo, args.wordlist)
    except FileNotFoundError:
        print(f"Wordlist not found: {args.wordlist}", file=sys.stderr)
        return 2
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        return 2

    if result is None:
        if not args.quiet:
            print("No match found.")
        return 1

    print(result)
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
