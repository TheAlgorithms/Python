#!/usr/bin/env python3
"""
pr_file_map.py

Lists all open pull requests in the current directory's git repo (via `gh`)
and, for each file touched by any open PR, which PR number(s) touch it.

Output is GitHub-flavored Markdown that includes this script's path, the
current UTC datetime, and summary counts for open PRs, file touches, distinct
files, and existing/missing files. It highlights files touched by more than one
open PR first (the likely merge-conflict hot spots when landing PRs), then
renders a sorted list of files that currently exist in the working directory,
each with its modifying PR numbers, followed by a separate section for files
referenced by open PRs but that do not exist in the working directory (e.g.
deleted, renamed, or on a branch not checked out locally).

Two file totals are reported because they answer different questions:
  - "file touches" counts every (PR, file) pair, so a file edited by three open
    PRs contributes three touches; and
  - "distinct files" counts each touched path once.
Only the distinct total equals `existing + missing`, since those are deduped.

Run status is also written to stderr with:
  - Number of PRs from `get_open_prs()`
  - Number of file touches from `get_pr_files()` and distinct files touched
  - Number of existing and missing files

Requirements: gh (GitHub CLI), authenticated (`gh auth login`)

Usage:
    ./pr_file_map.py
    ./pr_file_map.py > report.md
"""

import json
import shutil
import subprocess
import sys
from collections import defaultdict
from datetime import UTC, datetime
from pathlib import Path


def run_gh(args: list[str]) -> str:
    try:
        result = subprocess.run(  # noqa: S603
            ["gh", *args],  # noqa: S607
            capture_output=True,
            text=True,
            check=True,
        )
    except FileNotFoundError:
        sys.exit("Error: 'gh' (GitHub CLI) is not installed or not in PATH.")
    except subprocess.CalledProcessError as e:
        sys.exit(f"Error running 'gh {' '.join(args)}':\n{e.stderr.strip()}")
    return result.stdout


def check_gh_auth() -> None:
    try:
        subprocess.run(
            ["gh", "auth", "status"],  # noqa: S607
            capture_output=True,
            text=True,
            check=True,
        )
    except subprocess.CalledProcessError:
        sys.exit("Error: gh is not authenticated. Run 'gh auth login' first.")


def get_open_prs() -> list[dict]:
    raw = run_gh(
        ["pr", "list", "--state", "open", "--limit", "1000", "--json", "number,title"]
    )
    return json.loads(raw)


def get_pr_files(pr_number: int) -> list[str]:
    raw = run_gh(["pr", "view", str(pr_number), "--json", "files"])
    data = json.loads(raw)
    return [f["path"] for f in data.get("files", [])]


def main() -> None:
    if shutil.which("gh") is None:
        sys.exit("Error: 'gh' (GitHub CLI) is not installed or not in PATH.")

    check_gh_auth()

    prs = get_open_prs()
    pr_count = len(prs)
    print(f"PR count from get_open_prs(): {pr_count}", file=sys.stderr)

    file_to_prs: dict[str, list[int]] = defaultdict(list)
    touch_count = 0  # every (PR, file) pair; a file may be touched by many PRs

    for pr in prs:
        pr_number = pr["number"]
        pr_files = get_pr_files(pr_number)
        touch_count += len(pr_files)
        for path in pr_files:
            file_to_prs[path].append(pr_number)
    distinct_count = len(file_to_prs)
    print(
        f"File touches from get_pr_files(): {touch_count} "
        f"across {distinct_count} distinct files",
        file=sys.stderr,
    )

    existing: dict[str, list[int]] = {}
    missing: dict[str, list[int]] = {}
    contested: dict[str, list[int]] = {}

    for path, pr_numbers in file_to_prs.items():
        deduped = sorted(set(pr_numbers))
        target = existing if Path(path).exists() else missing
        target[path] = deduped
        if len(deduped) > 1:
            contested[path] = deduped
    existing_count = len(existing)
    missing_count = len(missing)
    print(
        f"Existing files: {existing_count}, Missing files: {missing_count}, "
        f"Contested files: {len(contested)}",
        file=sys.stderr,
    )

    # --- Render GitHub-flavored Markdown ---
    print("# Open Pull Request File Map\n")
    print(f"- Script: `{Path(__file__).resolve()}`")
    print(f"- Generated (UTC): `{datetime.now(UTC).isoformat()}`")
    print(f"- Number of PRs: `{pr_count}`")
    print(f"- File touches (PR x file): `{touch_count}`")
    print(f"- Distinct files touched: `{distinct_count}`")
    print(f"- Files touched by more than one PR: `{len(contested)}`")
    if pr_count == 0:
        print("\nNo open pull requests found.")
        return

    print(
        f"\n## `{len(contested)}` files touched by more than one open PR "
        "(possible merge conflicts)\n"
    )
    if contested:
        print("Coordinate, rebase, or land these together to avoid conflicts.\n")
        # Hot spots first: most-contested files, then alphabetical.
        for path in sorted(contested, key=lambda p: (-len(contested[p]), p)):
            pr_list = " ".join(f"#{n}" for n in contested[path])
            print(f"- `{path}` ({len(contested[path])} PRs): {pr_list}")
    else:
        print("_None -- no open PRs overlap on the same file._")

    print(f"\n## `{existing_count}` existing files\n")
    if existing:
        for path in sorted(existing):
            pr_list = " ".join(f"#{n}" for n in existing[path])
            print(f"- `{path}`: {pr_list}")
    else:
        print("_None._")

    print(f"\n## `{missing_count}` files not present in the working directory\n")
    if missing:
        for path in sorted(missing):
            pr_list = " ".join(f"#{n}" for n in missing[path])
            print(f"- `{path}`: {pr_list}")
    else:
        print("_None._")


if __name__ == "__main__":
    main()
