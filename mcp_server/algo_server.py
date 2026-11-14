"""MCP server exposing algorithm-development tools for this repository.

Runs inside a container with the repository mounted read-only at /repo and
talks to the host (Claude Code) over stdio.
"""

import subprocess
from pathlib import Path

from mcp.server.fastmcp import FastMCP
from pydantic import Field

REPO = Path("/repo")
TIMEOUT_SECONDS = 60
MAX_OUTPUT_CHARS = 4000

mcp = FastMCP("AlgoDevMCP", log_level="ERROR")


def _resolve(path: str) -> Path:
    """Map a repo-relative path into /repo and refuse anything outside it."""
    full = (REPO / path).resolve()
    if not full.is_relative_to(REPO) or full.suffix != ".py" or not full.is_file():
        raise ValueError(f"{path} is not a .py file inside the repo")
    return full


def _run(cmd: list[str]) -> str:
    """Run a command in the repo and return its exit code and trimmed output.

    Output is captured so nothing leaks onto stdout, which is the JSON-RPC channel.
    """
    result = subprocess.run(
        cmd,
        cwd=REPO,
        capture_output=True,
        text=True,
        timeout=TIMEOUT_SECONDS,
        check=False,
    )
    output = (result.stdout + result.stderr).strip()
    return f"exit={result.returncode}\n{output[-MAX_OUTPUT_CHARS:] or '(no output)'}"


@mcp.tool(
    name="run_doctests",
    description="Run the doctests of one algorithm file. exit=0 means all passed.",
)
def run_doctests(
    path: str = Field(description="Repo-relative path, e.g. sorts/bubble_sort.py"),
) -> str:
    return _run(["python3.15t", "-m", "doctest", str(_resolve(path))])


@mcp.tool(
    name="ruff_check",
    description="Lint one algorithm file with ruff using the repo's config.",
)
def ruff_check(
    path: str = Field(description="Repo-relative path, e.g. sorts/bubble_sort.py"),
) -> str:
    return _run(["ruff", "check", "--no-cache", str(_resolve(path))])


@mcp.resource("algos://directory", mime_type="text/markdown")
def directory() -> str:
    """The repository's index of every algorithm, grouped by category."""
    return (REPO / "DIRECTORY.md").read_text()


if __name__ == "__main__":
    mcp.run(transport="stdio")
