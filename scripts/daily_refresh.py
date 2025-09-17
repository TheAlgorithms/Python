"""Utilities for refreshing multiple Git repositories at once.

This module provides a small command line application that searches for Git
repositories under a given directory and executes ``git fetch --all --prune``
for each of them.  The goal is to make it easy to plug the script into a cron
job (or any other scheduler) so that a server can refresh all of its local
checkouts on a daily basis.

Example usage that fetches every repository under ``/srv/git``::

    $ python -m scripts.daily_refresh /srv/git

For safety the script performs fast-forward pulls only when the
``--pull`` flag is supplied.  The ``--dry-run`` option can be used to inspect
the commands that would be executed without touching the repositories.
"""

from __future__ import annotations

import argparse
import logging
import shlex
import subprocess
from collections.abc import Iterable, Sequence
from dataclasses import dataclass
from pathlib import Path


LOG_FORMAT = "%(asctime)s | %(levelname)-8s | %(message)s"


@dataclass(slots=True)
class RefreshResult:
    """Container describing the outcome of refreshing a repository."""

    repository: Path
    command: Sequence[str]
    returncode: int
    stdout: str
    stderr: str

    @property
    def succeeded(self) -> bool:
        """Return ``True`` when the git command was successful."""

        return self.returncode == 0


def _discover_repositories(root: Path, excluded: set[Path]) -> list[Path]:
    """Return every Git repository rooted at ``root``.

    Parameters
    ----------
    root:
        Directory that should be scanned.  The path is resolved to avoid
        surprises with symbolic links.
    excluded:
        Absolute paths that should not be traversed while searching.  A
        directory is considered excluded when it is equal to one of the
        supplied paths or when it is a child of one.
    """

    repositories: list[Path] = []
    root = root.resolve()

    def is_excluded(path: Path) -> bool:
        return any(path == item or item in path.parents for item in excluded)

    def walk(directory: Path) -> None:
        if is_excluded(directory):
            logging.debug("Skipping excluded directory %s", directory)
            return

        git_directory = directory / ".git"
        if git_directory.is_dir():
            repositories.append(directory)
            logging.debug("Found git repository in %s", directory)
            return

        for child in directory.iterdir():
            if not child.is_dir() or child.is_symlink():
                continue
            walk(child)

    walk(root)
    return repositories


def _run_git_command(
    repository: Path, command: Sequence[str], *, dry_run: bool
) -> RefreshResult:
    full_command = ("git", "-C", str(repository), *command)
    if dry_run:
        logging.info("DRY-RUN %s", shlex.join(full_command))
        return RefreshResult(repository, full_command, 0, "", "")

    logging.info("Running %s", shlex.join(full_command))
    process = subprocess.run(  # noqa: S603, S607 - `git` is a trusted command.
        full_command,
        capture_output=True,
        text=True,
        check=False,
    )
    return RefreshResult(
        repository,
        full_command,
        process.returncode,
        process.stdout.strip(),
        process.stderr.strip(),
    )


def refresh_repository(repository: Path, *, pull: bool, dry_run: bool) -> bool:
    """Refresh ``repository`` by fetching and (optionally) pulling updates.

    Parameters
    ----------
    repository:
        Path to a directory containing a Git checkout.
    pull:
        When ``True`` the script performs a fast-forward pull after fetching.
    dry_run:
        When ``True`` the underlying git commands are not executed.
    """

    commands: Iterable[Sequence[str]] = [("fetch", "--all", "--prune")]
    if pull:
        commands = (*commands, ("pull", "--ff-only"))

    for command in commands:
        result = _run_git_command(repository, command, dry_run=dry_run)
        if not result.succeeded:
            logging.error(
                "Failed to refresh %s with %s (exit code %s)",
                repository,
                shlex.join(result.command),
                result.returncode,
            )
            if result.stdout:
                logging.error("stdout: %s", result.stdout)
            if result.stderr:
                logging.error("stderr: %s", result.stderr)
            return False

        if result.stdout:
            logging.debug("%s", result.stdout)
        if result.stderr:
            logging.debug("%s", result.stderr)

    return True


def _parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Refresh every git repository found under a directory.",
    )
    parser.add_argument(
        "root",
        type=Path,
        nargs="?",
        default=Path.cwd(),
        help="Directory that should be scanned for repositories.",
    )
    parser.add_argument(
        "-e",
        "--exclude",
        action="append",
        default=[],
        metavar="PATH",
        help=(
            "Directory names (relative to ROOT) or absolute paths that should "
            "be skipped while searching for repositories.  The option can be "
            "provided multiple times."
        ),
    )
    parser.add_argument(
        "-p",
        "--pull",
        action="store_true",
        help="Perform a fast-forward pull after fetching.",
    )
    parser.add_argument(
        "-n",
        "--dry-run",
        action="store_true",
        help="Print the git commands without executing them.",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Increase logging verbosity (can be supplied multiple times).",
    )
    parser.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help="Silence informational output.",
    )
    return parser.parse_args()


def _prepare_excluded(root: Path, entries: list[str]) -> set[Path]:
    excluded: set[Path] = set()
    for entry in entries:
        path = Path(entry)
        if not path.is_absolute():
            path = (root / path).resolve()
        else:
            path = path.resolve()
        excluded.add(path)
    return excluded


def main() -> int:
    args = _parse_arguments()

    log_level = logging.INFO
    if args.quiet:
        log_level = logging.WARNING
    elif args.verbose >= 2:
        log_level = logging.DEBUG

    logging.basicConfig(level=log_level, format=LOG_FORMAT)

    root = args.root.resolve()
    if not root.is_dir():
        logging.error("%s is not a directory", root)
        return 1

    excluded = _prepare_excluded(root, args.exclude)
    repositories = _discover_repositories(root, excluded)

    if not repositories:
        logging.warning("No Git repositories found under %s", root)
        return 0

    logging.info(
        "Refreshing %s repositories under %s", len(repositories), root
    )

    failures = 0
    for repository in repositories:
        if not refresh_repository(repository, pull=args.pull, dry_run=args.dry_run):
            failures += 1

    if failures:
        logging.error("Failed to refresh %s repositories", failures)
        return 1

    logging.info("Successfully refreshed all repositories")
    return 0


if __name__ == "__main__":  # pragma: no cover - CLI entry point.
    raise SystemExit(main())
