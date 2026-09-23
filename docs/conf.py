# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html
#
# Project metadata (name/version/authors) is single-sourced from pyproject.toml
# so it never drifts from the packaging metadata.
import tomllib
from pathlib import Path

_pyproject = tomllib.loads(
    (Path(__file__).parent.parent / "pyproject.toml").read_text(encoding="utf-8")
)
_project = _pyproject["project"]

project = _project["name"]
author = ", ".join(a["name"] for a in _project.get("authors", []))
release = version = _project["version"]
copyright = "2014, TheAlgorithms"  # noqa: A001  # Sphinx requires this exact name

extensions = [
    "autoapi.extension",
    "myst_parser",
]

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

exclude_patterns = [
    ".*/*",
    "docs/",
]

html_theme = "alabaster"
html_static_path = ["_static"]
templates_path = ["_templates"]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]
myst_fence_as_directive = [
    "include",
]
