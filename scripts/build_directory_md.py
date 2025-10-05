#!/usr/bin/env python3

import os
import re
from typing import Iterator, Set


# Define directories to exclude during os.walk traversal
EXCLUDED_DIRS: Set[str] = {"scripts", "venv", "__pycache__"}

def good_file_paths(top_dir: str = ".") -> Iterator[str]:
    for dir_path, dir_names, filenames in os.walk(top_dir):
        dir_names[:] = [
            d
            for d in dir_names
            if d[0] not in "._" and d not in EXCLUDED_DIRS
        ]
        for filename in filenames:
            if filename == "__init__.py":
                continue

            # Check for valid extensions
            _, ext = os.path.splitext(filename)
             if ext in (".py", ".ipynb"):
                # Clean up path to ensure it doesn't start with './'
                full_path = os.path.join(dir_path, filename)
                yield full_path.lstrip("./")

def _generate_markdown_prefix(indent_level: int) -> str:
    if indent_level == 0:
        # Markdown H2 header for root-level entries
        return "\n##"
    # Indent with 2 spaces per level for nested lists (e.g., 2 spaces for level 1, 4 for level 2)
    return f"{' ' * (indent_level * 2)}*"

def _format_name(name: str) -> str:
    """
    Converts a file/directory name (e.g., 'my_awesome_file') into a Title Case
    string, replacing underscores with spaces (e.g., 'My Awesome File').
    """
    return name.replace('_', ' ').title()



def print_directory_md(top_dir: str = ".") -> None:
    # Stores the path of the last directory printed to determine new structure levels
    last_printed_path = ""
    # Get and sort all file paths to ensure consistent output order
    sorted_file_paths = sorted(good_file_paths(top_dir))
    
    for filepath in sorted_file_paths:
        current_dir_path, filename = os.path.split(filepath)
        if current_dir_path != last_printed_path:
            old_parts = last_printed_path.split(os.sep)
            new_parts = current_dir_path.split(os.sep)

            i = 0
            while i < len(old_parts) and i < len(new_parts) and old_parts[i] == new_parts[i]:
                i += 1
            for indent, new_part in enumerate(new_parts[i:], start=i):
                if new_part: # Ensure we don't print empty segments
                    prefix = _generate_markdown_prefix(indent)
                    print(f"{prefix} {_format_name(new_part)}")    
            last_printed_path = current_dir_path
        indent = (current_dir_path.count(os.sep) + 1) if current_dir_path else 0

        url = filepath.replace(" ", "%20")
        display_name = os.path.splitext(_format_name(filename))[0]

        prefix = _generate_markdown_prefix(indent)
        print(f"{prefix} [{display_name}]({url})")


if __name__ == "__main__":
    print_directory_md()
