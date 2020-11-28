#!/usr/bin/env python3
import importlib.util
import json
import os
import pathlib
from types import ModuleType
from typing import Dict, List

import pytest

try:
    import github
except ImportError:
    pass

PROJECT_EULER_DIR_PATH = pathlib.Path.cwd().joinpath("project_euler")
PROJECT_EULER_ANSWERS_PATH = pathlib.Path.cwd().joinpath(
    "scripts", "project_euler_answers.json"
)

with open(PROJECT_EULER_ANSWERS_PATH) as file_handle:
    PROBLEM_ANSWERS: Dict[str, str] = json.load(file_handle)


def convert_path_to_module(file_path: pathlib.Path) -> ModuleType:
    """Converts a file path to a Python module"""
    spec = importlib.util.spec_from_file_location(file_path.name, str(file_path))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def all_solution_file_paths() -> List[pathlib.Path]:
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


def get_pull_number() -> int:
    """Return the pull request number which triggered this action."""
    GITHUB_REF = os.environ["GITHUB_REF"]
    return int(GITHUB_REF.split("/")[2])


def added_solution_file_path() -> List[pathlib.Path]:
    """Collects only the solution file path which got added in the current
    pull request.

    This will only be triggered if the script is ran from GitHub Actions.
    """
    solution_file_paths = []
    # Direct fetching so that the error propagates, if any.
    login = github.Github(os.environ["GITHUB_TOKEN"])
    repo = login.get_repo(os.environ["GITHUB_REPOSITORY"])
    if pull_number := get_pull_number():
        pull = repo.get_pull(pull_number)
        for file in pull.get_files():
            file_path = pathlib.Path.cwd().joinpath(file.filename)
            if (
                file_path.suffix != ".py"
                or file_path.name.startswith(("_", "test"))
                or not file_path.name.startswith("sol")
            ):
                continue
            solution_file_paths.append(file_path)
    return solution_file_paths


def collect_solution_file_paths() -> List[pathlib.Path]:
    if os.environ.get("CI") and os.environ.get("GITHUB_EVENT_NAME") == "pull_request":
        # Return only if there are any, otherwise default to all solutions
        if filepaths := added_solution_file_path():
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
    assert answer == expected, f"Expected {expected} but got {answer}"
