
import subprocess
from pathlib import Path

from config import REPOSITORY_PATH


def read_file(path: str) -> str:
    """Read a file from the target repository."""
    root = REPOSITORY_PATH.resolve()
    target = (root / path).resolve()

    if not target.is_relative_to(root):
        return "Error: Access outside the repository is not allowed."

    if not target.is_file():
        return f"Error: File not found: {path}"

    try:
        return target.read_text(encoding="utf-8")
    except Exception as error:
        return f"Error reading file: {error}"


def list_files(directory: str = ".") -> str:
    root = REPOSITORY_PATH.resolve()

    if directory in ("", ".", "/"):
        target = root
    else:
        target = (root / directory).resolve()

    if not target.is_relative_to(root):
        return "Error: Access outside the repository is not allowed."

    if not target.is_dir():
        return f"Error: Directory not found: {directory}"

    files = [
        str(path.relative_to(root))
        for path in target.iterdir()
        if path.is_file()
    ]

    return "\n".join(files[:100])



def search_code(term: str) -> str:
    """Search Python files for a given text."""
    results = []

    for path in REPOSITORY_PATH.rglob("*.py"):
        if ".git" in path.parts:
            continue

        try:
            lines = path.read_text(encoding="utf-8").splitlines()

            for number, line in enumerate(lines, start=1):
                if term.lower() in line.lower():
                    relative = path.relative_to(REPOSITORY_PATH)
                    results.append(f"{relative}:{number}: {line.strip()}")

        except (UnicodeDecodeError, OSError):
            continue

        if len(results) >= 50:
            break

    return "\n".join(results) if results else "No matches found."


def run_tests(command: str) -> str:
    allowed = {
        "doctest": [
            "py", "-m", "doctest", "-v",
            "maths/continued_fraction.py"
        ],
        "ruff": [
            "py", "-m", "ruff", "check",
            "maths/continued_fraction.py"
        ],
    }

    if command not in allowed:
        return "Error: This test command is not approved."

    try:
        result = subprocess.run(
            allowed[command],
            cwd=REPOSITORY_PATH,
            capture_output=True,
            text=True,
            timeout=120,
        )

        return (
            f"Exit code: {result.returncode}\n"
            f"STDOUT:\n{result.stdout}\n"
            f"STDERR:\n{result.stderr}"
        )

    except subprocess.TimeoutExpired:
        return "Error: Test timed out."
    except Exception as error:
        return f"Error running test: {error}"


def propose_edit(path: str, old_text: str, new_text: str) -> str:
    """Propose a file modification and request human approval."""
    root = REPOSITORY_PATH.resolve()
    target = (root / path).resolve()

    if not target.is_relative_to(root):
        return "Error: Access outside the repository is not allowed."

    if not target.is_file():
        return "Error: File not found."

    current = target.read_text(encoding="utf-8")

    if old_text not in current:
        return "Error: The requested original text was not found."

    updated = current.replace(old_text, new_text, 1)

    print("\n--- PROPOSED CODE CHANGE ---")
    print(f"File: {path}")
    print("\nOriginal:\n", old_text)
    print("\nReplacement:\n", new_text)

    approval = input("\nApply this change? (yes/no): ").strip().lower()

    if approval != "yes":
        return "The user declined the proposed change. No file was modified."

    target.write_text(updated, encoding="utf-8")
    return f"Successfully updated {path}."
