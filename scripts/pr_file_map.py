#!/usr/bin/env python3
"""
pr_file_map.py

Lists all open pull requests in the current directory's git repo (via `gh`)
and, for each file touched by any open PR, which PR number(s) touch it.

Output is GitHub-flavored Markdown that includes this script's path (relative to
the git root), the current UTC datetime, and summary counts for open PRs, file
touches, distinct files, and existing/missing files. It highlights files touched
by more than one open PR first (the likely merge-conflict hot spots when landing
PRs), then renders a sorted list of files that currently exist in the working
directory, each with its modifying PR numbers, followed by a separate section for
files referenced by open PRs but that do not exist in the working directory (e.g.
deleted, renamed, or on a branch not checked out locally).

`DIRECTORY.md` is treated specially and reported in its own section at the very
bottom. It is auto-generated, so nearly every PR touches it, and it would
otherwise dominate the "possible merge conflicts" list and distract busy
maintainers. A merge conflict caused only by `DIRECTORY.md` is trivial to clear:
choose __accept both__ in the GitHub UI. The bottom section therefore separates
the PRs whose only overlap with other open PRs is `DIRECTORY.md` (safe to accept
both) from those that also overlap on real source files (which need a genuine
review or rebase).

Two file totals are reported because they answer different questions:
  - "file touches" counts every (PR, file) pair, so a file edited by three open
    PRs contributes three touches; and
  - "distinct files" counts each touched path once.
Only the distinct total equals `existing + missing`, since those are deduped.

Run status is also written to stderr with:
  - Number of PRs from `get_open_prs()`
  - Number of file touches from `get_pr_files_async()` and distinct files touched
  - Number of existing and missing files

Requirements: gh (GitHub CLI), authenticated (`gh auth login`)

Usage:
    scripts/pr_file_map.py
    scripts/pr_file_map.py > report.md
"""

import asyncio
import json
import os
import shutil
import subprocess
import sys
from collections import defaultdict
from datetime import UTC, datetime
from pathlib import Path

DIRECTORY_FILE = "DIRECTORY.md"

# How many `gh pr view` calls to run concurrently. The slow "first pass" is one
# network round-trip per open PR, so it is I/O-bound and gains a lot from
# concurrency; the cap keeps us polite to the GitHub API and avoids secondary
# rate limits. Override with the PR_FILE_MAP_CONCURRENCY environment variable.
DEFAULT_CONCURRENCY = 10

# Open PRs to skip in the report, e.g. [123, 456, 789] ignores #123, #456, #789.
ignore_pull_request: set[int] = {15105, 15142, 15356}


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


def git_root() -> Path | None:
    """Return the repository root, or None if not inside a git work tree."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],  # noqa: S607
            capture_output=True,
            text=True,
            check=True,
        )
    except FileNotFoundError:
        return None
    except subprocess.CalledProcessError:
        return None
    root = result.stdout.strip()
    return Path(root) if root else None


def script_display_path() -> Path:
    """This script's path relative to the git root (falls back to absolute)."""
    script_path = Path(__file__).resolve()
    if root := git_root():
        try:
            return script_path.relative_to(root.resolve())
        except ValueError:
            pass
    return script_path


def get_open_prs() -> list[dict]:
    raw = run_gh(
        ["pr", "list", "--state", "open", "--limit", "1000", "--json", "number,title"]
    )
    ignore = ignore_pull_request
    return [pr for pr in json.loads(raw) if pr["number"] not in ignore]


async def run_gh_async(args: list[str], semaphore: asyncio.Semaphore) -> str:
    """Async counterpart of run_gh, throttled by a shared semaphore.

    The semaphore bounds how many `gh` subprocesses run at once so we speed up
    the many-round-trip "first pass" without flooding the GitHub API.
    """
    async with semaphore:
        try:
            proc = await asyncio.create_subprocess_exec(
                "gh",
                *args,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )
        except FileNotFoundError:
            sys.exit("Error: 'gh' (GitHub CLI) is not installed or not in PATH.")
        stdout, stderr = await proc.communicate()
    if proc.returncode != 0:
        sys.exit(f"Error running 'gh {' '.join(args)}':\n{stderr.decode().strip()}")
    return stdout.decode()


async def get_pr_files_async(pr_number: int, semaphore: asyncio.Semaphore) -> list[str]:
    raw = await run_gh_async(
        ["pr", "view", str(pr_number), "--json", "files"], semaphore
    )
    data = json.loads(raw)
    return [f["path"] for f in data.get("files", [])]


async def gather_pr_files(
    pr_numbers: list[int], concurrency: int
) -> dict[int, list[str]]:
    """Fetch each PR's file list concurrently, capped at ``concurrency``.

    Returns a ``{pr_number: [paths]}`` mapping keyed in the same order as
    ``pr_numbers`` so downstream output stays deterministic.
    """
    semaphore = asyncio.Semaphore(concurrency)
    results = await asyncio.gather(
        *(get_pr_files_async(number, semaphore) for number in pr_numbers)
    )
    return dict(zip(pr_numbers, results))


def resolve_concurrency() -> int:
    """Read PR_FILE_MAP_CONCURRENCY (a positive int) or fall back to the default."""
    raw = os.environ.get("PR_FILE_MAP_CONCURRENCY")
    if raw is None:
        return DEFAULT_CONCURRENCY
    try:
        value = int(raw)
    except ValueError:
        value = 0
    if value < 1:
        sys.exit(
            f"Error: PR_FILE_MAP_CONCURRENCY must be a positive integer, got {raw!r}."
        )
    return value


def split_directory_conflicts(
    directory_prs: list[int],
    pr_to_files: dict[int, list[str]],
    contested: dict[str, list[int]],
) -> tuple[list[int], list[tuple[int, list[str]]]]:
    """Split PRs touching DIRECTORY.md by whether it is their only overlap.

    Returns (directory_only, directory_plus_other) where directory_only lists
    PRs whose sole collision with other open PRs is DIRECTORY.md (safe to
    "accept both"), and directory_plus_other pairs each remaining PR with the
    other contested files it touches (a real review/rebase is needed).
    """
    directory_only: list[int] = []
    directory_plus_other: list[tuple[int, list[str]]] = []
    for pr_number in directory_prs:
        other_contested = sorted(
            path
            for path in pr_to_files.get(pr_number, [])
            if path != DIRECTORY_FILE and path in contested
        )
        if other_contested:
            directory_plus_other.append((pr_number, other_contested))
        else:
            directory_only.append(pr_number)
    return directory_only, directory_plus_other


def render_file_section(title: str, files: dict[str, list[int]]) -> None:
    """Render a Markdown section listing files and the PR numbers touching them."""
    print(f"\n## `{len(files)}` {title}\n")
    if not files:
        print("_None._")
        return
    for path in sorted(files):
        pr_list = " ".join(f"#{n}" for n in files[path])
        print(f"- `{path}`: {pr_list}")


def render_directory_section(
    directory_prs: list[int],
    directory_only: list[int],
    directory_plus_other: list[tuple[int, list[str]]],
) -> None:
    """Render the bottom DIRECTORY.md section (kept last on purpose)."""
    print(f"\n## `{len(directory_prs)}` open PRs touch `{DIRECTORY_FILE}`\n")
    if not directory_prs:
        print(f"_None -- no open PR modifies `{DIRECTORY_FILE}`._")
        return
    print(
        f"`{DIRECTORY_FILE}` is auto-generated, so nearly every PR touches it. "
        "A merge conflict caused only by this file is cleared by choosing "
        "__accept both__ in the GitHub UI -- no rebase needed.\n"
    )
    print(
        f"### `{len(directory_only)}` PRs whose only overlap is "
        f"`{DIRECTORY_FILE}` (safe to accept both)\n"
    )
    print(
        "- " + ", ".join(f"#{n}" for n in directory_only)
        if directory_only
        else "_None._"
    )
    print(
        f"\n### `{len(directory_plus_other)}` PRs that also overlap on other "
        "files (need a review or rebase)\n"
    )
    if not directory_plus_other:
        print("_None._")
        return
    for pr_number, files in directory_plus_other:
        file_list = ", ".join(f"`{path}`" for path in files)
        print(f"- #{pr_number}: also touches {file_list}")


def main() -> None:
    if shutil.which("gh") is None:
        sys.exit("Error: 'gh' (GitHub CLI) is not installed or not in PATH.")

    check_gh_auth()

    prs = get_open_prs()
    pr_count = len(prs)
    print(f"PR count from get_open_prs(): {pr_count}", file=sys.stderr)

    file_to_prs: dict[str, list[int]] = defaultdict(list)
    touch_count = 0  # every (PR, file) pair; a file may be touched by many PRs

    # First pass: one `gh pr view` per PR. This is the slow, network-bound part,
    # so fetch them concurrently (bounded by resolve_concurrency()).
    concurrency = resolve_concurrency()
    pr_numbers = [pr["number"] for pr in prs]
    print(
        f"Fetching files for {pr_count} PRs "
        f"(up to {concurrency} concurrent gh calls)...",
        file=sys.stderr,
    )
    pr_to_files = asyncio.run(gather_pr_files(pr_numbers, concurrency))

    for pr_number in pr_numbers:
        pr_files = pr_to_files[pr_number]
        touch_count += len(pr_files)
        for path in pr_files:
            file_to_prs[path].append(pr_number)
    distinct_count = len(file_to_prs)
    print(
        f"File touches from get_pr_files_async(): {touch_count} "
        f"across {distinct_count} distinct files",
        file=sys.stderr,
    )

    # Pull DIRECTORY.md out so it does not dominate the contested/existing lists;
    # it gets its own section at the very bottom.
    directory_prs = sorted(set(file_to_prs.pop(DIRECTORY_FILE, [])))

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
        f"Contested files: {len(contested)} (excluding {DIRECTORY_FILE}), "
        f"PRs touching {DIRECTORY_FILE}: {len(directory_prs)}",
        file=sys.stderr,
    )

    # Of the PRs that touch DIRECTORY.md, separate those whose only overlap with
    # other open PRs is DIRECTORY.md itself (safe "accept both") from those that
    # also collide on real source files (need a genuine review or rebase).
    directory_only, directory_plus_other = split_directory_conflicts(
        directory_prs, pr_to_files, contested
    )

    # --- Render GitHub-flavored Markdown ---
    generated = f"{datetime.now(UTC):%d %b %Y at %H:%M} {UTC}"
    print(f"# Open Pull Request File Map: {generated}\n")
    print(f"- Script: `{script_display_path()}`")
    print(f"- Number of PRs: `{pr_count}`")
    print(f"- File touches (PR x file): `{touch_count}`")
    print(f"- Distinct files touched: `{distinct_count}`")
    print(
        f"- Files touched by more than one PR: `{len(contested)}` "
        f"(excluding `{DIRECTORY_FILE}`)"
    )
    print(f"- Open PRs touching `{DIRECTORY_FILE}`: `{len(directory_prs)}`")
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

    render_file_section("existing files", existing)
    render_file_section("files not present in the working directory", missing)

    # DIRECTORY.md section, kept at the very bottom on purpose.
    render_directory_section(directory_prs, directory_only, directory_plus_other)


if __name__ == "__main__":
    main()
