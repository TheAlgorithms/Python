#!/usr/bin/env python3
"""
pr_file_map.py

Lists all open pull requests in the current directory's git repo (via `gh`)
and, for each file touched by any open PR, which PR number(s) touch it.

Output is GitHub-flavored Markdown: a sorted list of files that currently
exist in the working directory, each with its modifying PR numbers, followed
by a separate section for files referenced by open PRs but that do not exist
in the working directory (e.g. deleted, renamed, or on a branch not checked
out locally).

Requirements: gh (GitHub CLI), authenticated (`gh auth login`)

Usage:
    ./pr_file_map.py
    ./pr_file_map.py > report.md
"""

import json
import os
import shutil
import subprocess
import sys
from collections import defaultdict


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
    if not prs:
        print("No open pull requests found.")
        return

    file_to_prs: dict[str, list[int]] = defaultdict(list)

    for pr in prs:
        pr_number = pr["number"]
        for path in get_pr_files(pr_number):
            file_to_prs[path].append(pr_number)

    existing: dict[str, list[int]] = {}
    missing: dict[str, list[int]] = {}

    for path, pr_numbers in file_to_prs.items():
        target = existing if os.path.exists(path) else missing
        target[path] = sorted(set(pr_numbers))

    # --- Render GitHub-flavored Markdown ---
    print("# Open Pull Request File Map\n")

    print("## Existing files\n")
    if existing:
        for path in sorted(existing):
            pr_list = " ".join(f"#{n}" for n in existing[path])
            print(f"- `{path}`: {pr_list}")
    else:
        print("_None._")

    print("\n## Files not present in the working directory\n")
    if missing:
        for path in sorted(missing):
            pr_list = " ".join(f"#{n}" for n in missing[path])
            print(f"- `{path}`: {pr_list}")
    else:
        print("_None._")


if __name__ == "__main__":
    main()
