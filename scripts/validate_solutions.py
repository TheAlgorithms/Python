#!/usr/bin/env python3
import hashlib
import importlib.util
import json
import os
import pathlib
from types import ModuleType
import requests
import pytest

PROJECT_EULER_DIR_PATH = pathlib.Path.cwd().joinpath("project_euler")
PROJECT_EULER_ANSWERS_PATH = pathlib.Path.cwd().joinpath("scripts", "project_euler_answers.json")

with open(PROJECT_EULER_ANSWERS_PATH) as file_handle:
    PROBLEM_ANSWERS: dict[str, str] = json.load(file_handle)


def convert_path_to_module(file_path: pathlib.Path) -> ModuleType:
    """Converts a file path to a Python module."""
    spec = importlib.util.spec_from_file_location(file_path.name, str(file_path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def all_solution_file_paths() -> list[pathlib.Path]:
    """Collects all the solution file paths in the Project Euler directory."""
    solution_file_paths = []
    for problem_dir_path in PROJECT_EULER_DIR_PATH.iterdir():
        if problem_dir_path.is_file() or problem_dir_path.name.startswith("_"):
            continue
        for file_path in problem_dir_path.iterdir():
            if file_path.suffix != ".py" or file_path.name.startswith(("_", "test")):
                continue
            solution_file_paths.append(file_path)
    return solution_file_paths


def get_files_url() -> str:
    """Return the pull request number which triggered this action."""
    with open(os.environ["GITHUB_EVENT_PATH"]) as file:
        event = json.load(file)
    return event["pull_request"]["url"] + "/files"


def added_solution_file_paths() -> list[pathlib.Path]:
    """Collects only the solution file paths added in the current pull request."""
    solution_file_paths = []
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": "token " + os.environ["GITHUB_TOKEN"],
    }
    files = requests.get(get_files_url(), headers=headers).json()
    for file in files:
        filepath = pathlib.Path.cwd().joinpath(file["filename"])
        if (
            filepath.suffix != ".py"
            or filepath.name.startswith(("_", "test"))
            or not filepath.name.startswith("sol")
        ):
            continue
        solution_file_paths.append(filepath)
    return solution_file_paths


def collect_solution_file_paths() -> list[pathlib.Path]:
    if os.environ.get("CI") and os.environ.get("GITHUB_EVENT_NAME") == "pull_request":
        # Return only if there are any; otherwise, default to all solutions
        if filepaths := added_solution_file_paths():
            return filepaths
    return all_solution_file_paths()


def hash_solution(solution: int) -> str:
    """Hashes the solution to compare with expected values."""
    return hashlib.sha256(str(solution).encode()).hexdigest()


def test_solution(solution_path: pathlib.Path, expected_hash: str) -> None:
    """Test an individual Project Euler solution."""
    solution_module = convert_path_to_module(solution_path)
    solution_function = getattr(solution_module, "solution", None)
    assert solution_function is not None, "Solution function not found"
    answer = solution_function()
    hashed_answer = hash_solution(answer)
    assert (
        hashed_answer == expected_hash
    ), f"Hash mismatch for {solution_path.name}. Expected: {expected_hash}, Got: {hashed_answer}"


@pytest.mark.parametrize(
    "solution_path, expected_hash",
    [(path, PROBLEM_ANSWERS[path.parent.name[8:].zfill(3)]) for path in collect_solution_file_paths()],
    ids=lambda args: f"{args[0].parent.name}/{args[0].name}",
)
def test_project_euler(solution_path: pathlib.Path, expected_hash: str) -> None:
    """Testing for all Project Euler solutions."""
    test_solution(solution_path, expected_hash)
