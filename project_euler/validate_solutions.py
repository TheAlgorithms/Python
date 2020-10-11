#!/usr/bin/env python3
import importlib.util
import json
import pathlib
from types import ModuleType
from typing import Generator

import pytest

PROJECT_EULER_DIR_PATH = pathlib.Path.cwd().joinpath("project_euler")
PROJECT_EULER_ANSWERS_PATH = PROJECT_EULER_DIR_PATH.joinpath(
    "project_euler_answers.json"
)

with open(PROJECT_EULER_ANSWERS_PATH) as file_handle:
    PROBLEM_ANSWERS = json.load(file_handle)


def generate_solution_modules(
    dir_path: pathlib.Path,
) -> Generator[ModuleType, None, None]:
    # Iterating over every file or directory
    for file_path in dir_path.iterdir():
        if file_path.suffix != ".py" or file_path.name.startswith(("_", "test")):
            continue
        # Importing the source file through the given path
        # https://docs.python.org/3/library/importlib.html#importing-a-source-file-directly
        spec = importlib.util.spec_from_file_location(file_path.name, str(file_path))
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        yield module


@pytest.mark.parametrize("problem_number, expected", PROBLEM_ANSWERS)
def test_project_euler(subtests, problem_number: int, expected: str):
    problem_dir = PROJECT_EULER_DIR_PATH.joinpath(f"problem_{problem_number:02}")
    # Check if the problem directory exist. If not, then skip.
    if problem_dir.is_dir():
        for solution_module in generate_solution_modules(problem_dir):
            # All the tests in a loop is considered as one test by pytest so, use
            # subtests to make sure all the subtests are considered as different.
            with subtests.test(
                msg=f"Problem {problem_number} tests", solution_module=solution_module
            ):
                try:
                    answer = str(solution_module.solution())
                    assert answer == expected, f"Expected {expected} but got {answer}"
                except (AssertionError, AttributeError, TypeError) as err:
                    print(
                        f"problem_{problem_number:02}/{solution_module.__name__}: {err}"
                    )
                    raise
    else:
        pytest.skip(f"Solution {problem_number} does not exist yet.")
