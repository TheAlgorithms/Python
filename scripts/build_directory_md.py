#!/usr/bin/env python3
"""
This is a simple script that will scan through the current directory
and generate the corresponding DIRECTORY.md file, can also specify
files or folders to be ignored.
"""
import os


# Target URL (master)
BASE_URL = "https://github.com/TheAlgorithms/Python/blob/master/"


def tree(d, ignores, ignores_ext):
    return _markdown(d, ignores, ignores_ext, 0)


def _markdown(parent, ignores, ignores_ext, depth):
    dirs, files = [], []
    for i in os.listdir(parent):
        full = os.path.join(parent, i)
        name, ext = os.path.splitext(i)
        if i[0] != "." and i not in ignores and ext not in ignores_ext:
            if os.path.isfile(full):
                url = f"{BASE_URL}{parent.replace('./', '')}/{i}".replace(" ", "%20")
                files.append((name.replace("_", " "), url))
            else:
                dirs.append(i)
    out = (
        "\n".join(
            f"{'  ' * depth}* [{name}]({url})"
            for name, url in sorted(files, key=lambda e: e[0].lower())
        )
        + "\n"
    )
    for i in sorted(dirs):
        full = os.path.join(parent, i)
        i = i.replace("_", " ").title()
        if depth == 0:
            out += f"## {i}\n"
        else:
            out += f"{'  ' * depth}* {i}\n"
        out += _markdown(full, ignores, ignores_ext, depth + 1)
    return out


# Specific files or folders with the given names will be ignored
ignores = "__init__.py __pycache__ requirements.txt scripts".split()

# Files with given entensions will be ignored
ignores_ext = ".ini .json .jpg .md .png .pyc .txt .yml".split()


if __name__ == "__main__":
    with open("DIRECTORY.md", "w+") as f:
        f.write(tree(".", ignores, ignores_ext))
