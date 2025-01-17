#!/usr/bin/env python3
import hashlib
import importlib.util
import json
import os
import pathlib
from types import ModuleType

import pytest
import requests

PROJECT_EULER_DIR_PATH = pathlib.Path.cwd().joinpath("project_euler")
PROJECT_EULER_ANSWERS_PATH = pathlib.Path.cwd().joinpath(
    "scripts", "project_euler_answers.json"
)

with open(PROJECT_EULER_ANSWERS_PATH) as file_handle:
    PROBLEM_ANSWERS: dict[str, str] = json.load(file_handle)


def convert_path_to_module(file_path: pathlib.Path) -> ModuleType:
    """Converts a file path to a Python module"""
    spec = importlib.util.spec_from_file_location(file_path.name, str(file_path))
    module = importlib.util.module_from_spec(spec)  # type: ignore[arg-type]
    spec.loader.exec_module(module)  # type: ignore[union-attr]
    return module


def all_solution_file_paths() -> list[pathlib.Path]:
    """Collects all the solution file path in the Project Euler directory"""
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


def added_solution_file_path() -> list[pathlib.Path]:
    """Collects only the solution file path which got added in the current
    pull request.

    This will only be triggered if the script is ran from GitHub Actions.
    """
    solution_file_paths = []
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": "token " + os.environ["GITHUB_TOKEN"],
    }
    files = requests.get(get_files_url(), headers=headers, timeout=10).json()
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
    # Return only if there are any, otherwise default to all solutions
    if (
        os.environ.get("CI")
        and os.environ.get("GITHUB_EVENT_NAME") == "pull_request"
        and (filepaths := added_solution_file_path())
    ):
        return filepaths
    return all_solution_file_paths()


@pytest.mark.parametrize(
    "solution_path",
    collect_solution_file_paths(),
    ids=lambda path: f"{path.parent.name}/{path.name}",
)
def test_project_euler(solution_path: pathlib.Path) -> None:
    """Testing for all Project Euler solutions"""
    # problem_[extract this part] and pad it with zeroes for width 3
    problem_number: str = solution_path.parent.name[8:].zfill(3)
    expected: str = PROBLEM_ANSWERS[problem_number]
    solution_module = convert_path_to_module(solution_path)
    answer = str(solution_module.solution())
    answer = hashlib.sha256(answer.encode()).hexdigest()
    assert (
        answer == expected
    ), f"Expected solution to {problem_number} to have hash {expected}, got {answer}"
