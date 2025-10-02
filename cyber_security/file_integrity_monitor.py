#!/usr/bin/env python3
"""File Integrity Monitor (FIM).

Two modes:
 - init: hash files and create baseline JSON
 - verify: re-hash and report modifications/additions/deletions

Usage:
  python -m cyber_security.file_integrity_monitor init --root /path --output baseline.json --glob "**/*.py"
  python -m cyber_security.file_integrity_monitor verify --root /path --baseline baseline.json
"""
from __future__ import annotations

import argparse
import fnmatch
import hashlib
import json
import os
import sys
from dataclasses import dataclass
from typing import Dict, Iterable


@dataclass
class FileHash:
    path: str
    sha256: str


def iter_files(root: str, pattern: str | None) -> Iterable[str]:
    for base, _dirs, files in os.walk(root):
        for name in files:
            rel = os.path.relpath(os.path.join(base, name), root)
            if pattern is None or fnmatch.fnmatch(rel, pattern):
                yield rel


def hash_file(root: str, rel_path: str) -> str:
    h = hashlib.sha256()
    abs_path = os.path.join(root, rel_path)
    with open(abs_path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def build_baseline(root: str, pattern: str | None) -> Dict[str, str]:
    result: Dict[str, str] = {}
    for rel in iter_files(root, pattern):
        try:
            result[rel] = hash_file(root, rel)
        except (PermissionError, FileNotFoundError):
            continue
    return result


def write_json(path: str, data: Dict[str, str]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, sort_keys=True)


def read_json(path: str) -> Dict[str, str]:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def cmd_init(args: argparse.Namespace) -> int:
    baseline = build_baseline(args.root, args.glob)
    write_json(args.output, baseline)
    print(f"Baseline written: {args.output} ({len(baseline)} files)")
    return 0


def cmd_verify(args: argparse.Namespace) -> int:
    prior = read_json(args.baseline)
    current = build_baseline(args.root, None)

    added = sorted(set(current) - set(prior))
    removed = sorted(set(prior) - set(current))
    modified = sorted([p for p in set(current) & set(prior) if current[p] != prior[p]])

    if added:
        print("Added:")
        for p in added:
            print(f" + {p}")
    if removed:
        print("Removed:")
        for p in removed:
            print(f" - {p}")
    if modified:
        print("Modified:")
        for p in modified:
            print(f" * {p}")

    if not (added or removed or modified):
        print("No changes detected.")
        return 0

    return 1


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="File Integrity Monitor (FIM)")
    sub = parser.add_subparsers(dest="command", required=True)

    p_init = sub.add_parser("init", help="Create baseline JSON of file hashes")
    p_init.add_argument("--root", required=True, help="Root directory to scan")
    p_init.add_argument("--output", required=True, help="Path to baseline JSON output")
    p_init.add_argument("--glob", help="Glob-like pattern relative to root (e.g., **/*.py)")
    p_init.set_defaults(func=cmd_init)

    p_ver = sub.add_parser("verify", help="Verify current state against baseline JSON")
    p_ver.add_argument("--root", required=True, help="Root directory to scan")
    p_ver.add_argument("--baseline", required=True, help="Path to baseline JSON")
    p_ver.set_defaults(func=cmd_verify)

    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    return int(args.func(args))


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
