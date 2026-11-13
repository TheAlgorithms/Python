"""
Open a pull request for the current branch *inside the contributor's fork*.

Lab 6 rule: contributions go to the fork, never to TheAlgorithms/Python.
`gh pr create` run from a fork targets the upstream repository by default, so
this script always passes an explicit `--repo <fork owner>/<repo>` and refuses
to run when that would point at TheAlgorithms.

Before pushing it enforces the CONTRIBUTING.md / AGENTS.md rules that a robot
can check:
  * not on master, clean working tree
  * exactly one algorithm file changed (tests/ excluded), snake_case filename
  * PR body has a checked box and no closing keyword aimed at a tracking issue
  * ruff check, ruff format --check and doctests pass on the changed files

Usage (from the repository root):
    python .claude/scripts/open_fork_pr.py --title "..." --body-file .git/PR_BODY.md
    python .claude/scripts/open_fork_pr.py ... --dry-run   # print, do not push
"""

# A standalone helper, not a package (INP001); it runs fixed git/uv/gh argument
# lists without a shell, so the subprocess warnings do not apply (S603, S607).
# ruff: noqa: INP001, S603, S607

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

UPSTREAM_OWNER = "TheAlgorithms"
# Tracking issues must be referenced with "Part of", never closed by a PR.
TRACKING_ISSUES = {15187, 15234}
CHECKED_BOX = re.compile(r"^\s*[*-]\s*\[x\]", re.IGNORECASE | re.MULTILINE)
CLOSING_KEYWORD = re.compile(
    r"\b(?:close[sd]?|fix(?:e[sd])?|resolve[sd]?)\s+#(\d+)", re.IGNORECASE
)
SNAKE_CASE_FILE = re.compile(r"^[a-z0-9_]+\.py$")


def parse_owner_repo(remote_url: str) -> tuple[str, str]:
    """
    Return (owner, repository) from a GitHub remote URL.

    >>> parse_owner_repo("https://github.com/NEHoward/Python.git")
    ('NEHoward', 'Python')
    >>> parse_owner_repo("git@github.com:NEHoward/Python.git")
    ('NEHoward', 'Python')
    >>> parse_owner_repo("https://gitlab.com/someone/Python")
    Traceback (most recent call last):
        ...
    ValueError: not a GitHub remote: https://gitlab.com/someone/Python
    """
    match = re.search(r"github\.com[:/]([^/]+)/([^/]+?)(?:\.git)?/?$", remote_url)
    if match is None:
        msg = f"not a GitHub remote: {remote_url}"
        raise ValueError(msg)
    return match.group(1), match.group(2)


def check_target(owner: str) -> list[str]:
    """
    Refuse any pull request whose base repository is the upstream project.

    >>> check_target("NEHoward")
    []
    >>> check_target("TheAlgorithms")
    ['origin points at TheAlgorithms: this lab must not contribute upstream']
    """
    if owner.lower() == UPSTREAM_OWNER.lower():
        return [
            f"origin points at {UPSTREAM_OWNER}: this lab must not contribute upstream"
        ]
    return []


def check_changed_files(changed_files: list[str]) -> list[str]:
    """
    Apply the one-algorithm-file-per-PR and filename rules.

    >>> check_changed_files(["sorts/power_sort.py"])
    []
    >>> check_changed_files(["sorts/quick_sort.py", "tests/test_sorts.py"])
    []
    >>> check_changed_files([])
    ['branch has no changes against origin/master']
    >>> check_changed_files(["sorts/a_sort.py", "maths/b_math.py"])
    ['2 algorithm files changed: AGENTS.md allows one per PR']
    >>> check_changed_files(["sorts/Bad-Name.py"])
    ['filename is not lowercase snake_case: sorts/Bad-Name.py']
    """
    if not changed_files:
        return ["branch has no changes against origin/master"]
    problems = []
    python_files = [path for path in changed_files if path.endswith(".py")]
    algorithm_files = [path for path in python_files if not path.startswith("tests/")]
    if len(algorithm_files) > 1:
        problems.append(
            f"{len(algorithm_files)} algorithm files changed: "
            "AGENTS.md allows one per PR"
        )
    problems.extend(
        f"filename is not lowercase snake_case: {path}"
        for path in python_files
        if not SNAKE_CASE_FILE.match(Path(path).name)
    )
    return problems


def check_body(body: str) -> list[str]:
    """
    Check the PR description against the repository's PR template rules.

    >>> check_body("* [x] Fix a bug\\nPart of #15234")
    []
    >>> check_body("* [ ] Fix a bug")
    ['no checked box: algorithms-keeper closes PRs without one']
    >>> check_body("* [x] typing\\nFixes #15234")
    ['closing keyword on tracking issue #15234: write "Part of #15234"']
    >>> check_body("* [x] bug fix\\nFixes #10")
    []
    """
    problems = []
    if not CHECKED_BOX.search(body):
        problems.append("no checked box: algorithms-keeper closes PRs without one")
    for issue_number in CLOSING_KEYWORD.findall(body):
        if int(issue_number) in TRACKING_ISSUES:
            problems.append(
                f"closing keyword on tracking issue #{issue_number}: "
                f'write "Part of #{issue_number}"'
            )
    return problems


def git(*args: str) -> str:
    """Run a git command and return its stripped standard output."""
    result = subprocess.run(["git", *args], capture_output=True, text=True, check=True)
    return result.stdout.strip()


def run_quality_checks(changed_files: list[str]) -> list[str]:
    """Run ruff and doctests on the changed Python files; return failures."""
    python_files = [path for path in changed_files if path.endswith(".py")]
    if not python_files:
        return []
    commands = [
        ["uvx", "ruff", "check", *python_files],
        ["uvx", "ruff", "format", "--check", *python_files],
        [
            "uv",
            "run",
            "--with",
            "pytest",
            "pytest",
            "-q",
            "--doctest-modules",
            *python_files,
        ],
    ]
    failures = []
    for command in commands:
        print("$", " ".join(command))
        if subprocess.run(command, check=False).returncode != 0:
            failures.append(f"check failed: {' '.join(command[:4])}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    parser.add_argument("--title", required=True)
    parser.add_argument("--body-file", required=True, type=Path)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--skip-checks", action="store_true")
    args = parser.parse_args()

    branch = git("rev-parse", "--abbrev-ref", "HEAD")
    owner, repository = parse_owner_repo(git("remote", "get-url", "origin"))
    problems = check_target(owner)
    if branch in {"master", "main"}:
        problems.append("you are on master: create a feature branch first")
    if git("status", "--porcelain", "--untracked-files=no"):
        problems.append("working tree has uncommitted changes")

    # The PR base is the fork's master, so diff against it: the tooling commits
    # on master stay out of the PR and only this branch's work is checked.
    try:
        git("fetch", "--quiet", "origin", "master")
    except subprocess.CalledProcessError:
        print("warning: could not fetch origin; using the local origin/master")
    base = git("merge-base", "HEAD", "origin/master")
    changed_files = git("diff", "--name-only", base, "HEAD").splitlines()
    problems += check_changed_files(changed_files)
    problems += check_body(args.body_file.read_text(encoding="utf-8"))
    if not args.skip_checks:
        problems += run_quality_checks(changed_files)

    if problems:
        print("\nNot opening a PR:")
        for problem in problems:
            print(f"  - {problem}")
        return 1

    fork = f"{owner}/{repository}"
    push = ["git", "push", "-u", "origin", branch]
    create_pr = [
        "gh", "pr", "create", "--repo", fork, "--base", "master",
        "--head", branch, "--title", args.title, "--body-file", str(args.body_file),
    ]  # fmt: skip
    compare_url = f"https://github.com/{fork}/compare/master...{branch}?expand=1"
    print(f"\nChanged files: {', '.join(changed_files)}")
    print(f"PR target: {fork} (master <- {branch})")
    if args.dry_run:
        print("dry run:", " ".join(push))
        print("dry run:", " ".join(create_pr))
        return 0

    subprocess.run(push, check=True)
    if shutil.which("gh") is None:
        print(f"gh is not installed. Open the PR here:\n  {compare_url}")
        return 0
    return subprocess.run(create_pr, check=False).returncode


if __name__ == "__main__":
    sys.exit(main())
