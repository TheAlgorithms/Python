#!/usr/bin/env python3

from __future__ import annotations

import os
import pathlib
import subprocess
from collections.abc import Iterable, Iterator


def get_git_files(top_dir: str = ".") -> Iterable[str]:
    cmd = ["git", "ls-files", top_dir]
    ls_files = subprocess.run(cmd, capture_output=True)
    paths = iter(ls_files.stdout.decode().strip().split("\n"))
    return paths


def good_file_paths(top_dir: str = ".") -> Iterator[str]:
    for filepath in get_git_files():
        path = pathlib.Path(filepath)
        if path.name == "__init__.py":
            continue

        if path.suffix in (".py", ".ipynb"):
            yield filepath


def md_prefix(i):
    return f"{i * '  '}*" if i else "\n##"


def print_path(old_path: str, new_path: str) -> str:
    old_parts = old_path.split(os.sep)
    for i, new_part in enumerate(new_path.split(os.sep)):
        if i + 1 > len(old_parts) or old_parts[i] != new_part:
            if new_part:
                print(f"{md_prefix(i)} {new_part.replace('_', ' ').title()}")
    return new_path


def print_directory_md(top_dir: str = ".") -> None:
    old_path = ""
    for filepath in sorted(good_file_paths(top_dir)):
        filepath, filename = os.path.split(filepath)
        if filepath != old_path:
            old_path = print_path(old_path, filepath)
        indent = (filepath.count(os.sep) + 1) if filepath else 0
        url = "/".join((filepath, filename)).replace(" ", "%20")
        filename = os.path.splitext(filename.replace("_", " ").title())[0]
        print(f"{md_prefix(indent)} [{filename}]({url})")


if __name__ == "__main__":
    print_directory_md(".")
