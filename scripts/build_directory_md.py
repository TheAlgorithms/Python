#!/usr/bin/env python3

import os
from collections.abc import Iterator


def good_file_paths(top_dir: str = ".") -> Iterator[str]:
    for dir_path, dir_names, filenames in os.walk(top_dir):
        dir_names[:] = [
            d
            for d in dir_names
            if d != "scripts" and d[0] not in "._" and "venv" not in d
        ]
        for filename in filenames:
            if filename == "__init__.py":
                continue
            if os.path.splitext(filename)[1] in (".py", ".ipynb"):
                yield os.path.join(dir_path, filename).lstrip("./")


def md_prefix(indent: int) -> str:
    """
    Markdown prefix based on indent for bullet points

    >>> md_prefix(0)
    '\\n##'
    >>> md_prefix(1)
    '  *'
    >>> md_prefix(2)
    '    *'
    >>> md_prefix(3)
    '      *'
    """
    return f"{indent * '  '}*" if indent else "\n##"


def print_path(old_path: str, new_path: str) -> str:
    old_parts = old_path.split(os.sep)
    for i, new_part in enumerate(new_path.split(os.sep)):
        if (i + 1 > len(old_parts) or old_parts[i] != new_part) and new_part:
            print(f"{md_prefix(i)} {new_part.replace('_', ' ').title()}")
    return new_path


def print_directory_md(top_dir: str = ".") -> None:
    old_path = ""
    for filepath in sorted(good_file_paths(top_dir)):
        filepath, filename = os.path.split(filepath)
        if filepath != old_path:
            old_path = print_path(old_path, filepath)
        indent = (filepath.count(os.sep) + 1) if filepath else 0
        url = f"{filepath}/{filename}".replace(" ", "%20")
        filename = os.path.splitext(filename.replace("_", " ").title())[0]
        print(f"{md_prefix(indent)} [{filename}]({url})")


if __name__ == "__main__":
    print_directory_md(".")
