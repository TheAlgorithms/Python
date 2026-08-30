"""Sphinx configuration for TheAlgorithms/Python.

Migrated off ``sphinx-pyproject`` (unmaintained, no Python 3.14/3.15 support)
to a plain Sphinx ``conf.py``. Project metadata (name/version/author) is still
single-sourced from ``pyproject.toml`` via the stdlib ``tomllib`` parser; the
rest of the options that used to live under ``[tool.sphinx-pyproject]`` are
inlined below.
"""

import tomllib
from pathlib import Path

_pyproject_path = Path(__file__).parent.parent / "pyproject.toml"
_project = tomllib.loads(_pyproject_path.read_text())["project"]

# -- Project information -----------------------------------------------------
project = _project["name"]
version = release = _project["version"]
author = ", ".join(a["name"] for a in _project.get("authors", []) if "name" in a)
copyright = "2014, TheAlgorithms"  # noqa: A001

# -- General configuration ---------------------------------------------------
extensions = [
    "autoapi.extension",
    "myst_parser",
]

templates_path = ["_templates"]
exclude_patterns = [
    ".*/*",
    "docs/",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# -- autoapi (source tree -> API docs) ---------------------------------------
autoapi_dirs = [
    "audio_filters",
    "backtracking",
    "bit_manipulation",
    "blockchain",
    "boolean_algebra",
    "cellular_automata",
    "ciphers",
    "computer_vision",
    "conversions",
    "data_compression",
    "data_structures",
    "digital_image_processing",
    "divide_and_conquer",
    "dynamic_programming",
    "electronics",
    "file_transfer",
    "financial",
    "fractals",
    "fuzzy_logic",
    "genetic_algorithm",
    "geodesy",
    "geometry",
    "graphics",
    "graphs",
    "greedy_methods",
    "hashes",
    "knapsack",
    "linear_algebra",
    "linear_programming",
    "machine_learning",
    "maths",
    "matrix",
    "networking_flow",
    "neural_network",
    "other",
    "physics",
    "project_euler",
    "quantum",
    "scheduling",
    "searches",
    "sorts",
    "strings",
    "web_programming",
]
autoapi_member_order = "groupwise"
# autoapi_python_use_implicit_namespaces = True

# -- MyST (Markdown) ---------------------------------------------------------
myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    # "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]
myst_fence_as_directive = [
    "include",
]

# -- HTML output -------------------------------------------------------------
html_theme = "alabaster"
html_static_path = ["_static"]
