#!/usr/bin/env python3
"""
pr_file_map.py

Lists all open pull requests in the current directory's git repo (via `gh`)
and, for each file touched by any open PR, which PR number(s) touch it.

Output is GitHub-flavored Markdown that includes this script's path, the
current UTC datetime, and summary counts for open PRs, file entries, and
existing/missing files. It then renders a sorted list of files that currently
exist in the working directory, each with its modifying PR numbers, followed
by a separate section for files referenced by open PRs but that do not exist
in the working directory (e.g. deleted, renamed, or on a branch not checked
out locally).

Run status is also written to stderr with:
  - Number of PRs from `get_open_prs()`
  - Number of files from `get_pr_files()`
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
    file_count = 0

    for pr in prs:
        pr_number = pr["number"]
        pr_files = get_pr_files(pr_number)
        file_count += len(pr_files)
        for path in pr_files:
            file_to_prs[path].append(pr_number)
    print(f"File count from get_pr_files(): {file_count}", file=sys.stderr)

    existing: dict[str, list[int]] = {}
    missing: dict[str, list[int]] = {}

    for path, pr_numbers in file_to_prs.items():
        target = existing if Path(path).exists() else missing
        target[path] = sorted(set(pr_numbers))
    existing_count = len(existing)
    missing_count = len(missing)
    print(
        f"Existing files: {existing_count}, Missing files: {missing_count}",
        file=sys.stderr,
    )

    # --- Render GitHub-flavored Markdown ---
    print("# Open Pull Request File Map\n")
    print(f"- Script: `{Path(__file__).resolve()}`")
    print(f"- Generated (UTC): `{datetime.now(UTC).isoformat()}`")
    print(f"- Number of PRs: `{pr_count}`")
    print(f"- Number of files: `{file_count}`")
    if pr_count == 0:
        print("No open pull requests found.")
        return

    print(f"## `{existing_count}` existing files\n")
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
