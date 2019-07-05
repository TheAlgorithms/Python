"""
This is a simple script that will scan through the current directory
and generate the corresponding DIRECTORY.md file, can also specify
files or folders to be ignored.
"""
import os


# Target URL (master)
URL = "https://github.com/TheAlgorithms/Python/blob/master/"


def tree(d, ignores, ignores_ext):
    return _markdown(d, ignores, ignores_ext, 0)
    

def _markdown(parent, ignores, ignores_ext, depth):
    out = ""
    dirs, files = [], []
    for i in os.listdir(parent):
        full = os.path.join(parent, i)
        name, ext = os.path.splitext(i)
        if i in ignores or ext in ignores_ext:
            continue
        if os.path.isfile(full):
            # generate list
            pre = parent.replace("./", "").replace(" ", "%20")
            # replace all spaces to safe URL
            child = i.replace(" ", "%20")
            files.append((pre, child, name))
        else:
            dirs.append(i)
    # Sort files
    files.sort(key=lambda e: e[2].lower())
    for f in files:
        pre, child, name = f
        out += "  " * depth + "* [" + name.replace("_", " ") + "](" + URL + pre + "/" + child + ")\n"
    # Sort directories
    dirs.sort()
    for i in dirs:
        full = os.path.join(parent, i)
        i = i.replace("_", " ").title()
        if depth == 0:
            out += "## " + i + "\n"
        else:
            out += "  " * depth + "* " + i + "\n"
        out += _markdown(full, ignores, ignores_ext, depth+1)
    return out


# Specific files or folders with the given names will be ignored
ignores = [".vs",
    ".gitignore",
    ".git",
    "~script.py",
    "__init__.py",
]
# Files with given entensions will be ignored
ignores_ext = [
    ".md",
    ".ipynb",
    ".png",
    ".jpg",
    ".yml"
]


if __name__ == "__main__":
    with open("DIRECTORY.md", "w+") as f:
        f.write(tree(".", ignores, ignores_ext))
