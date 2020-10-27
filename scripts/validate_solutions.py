#!/usr/bin/env python3
import importlib.util
import json
import pathlib
from types import ModuleType
from typing import Dict, List

import pytest

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


def collect_solution_file_paths() -> List[pathlib.Path]:
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


@pytest.mark.parametrize(
    "solution_path",
    collect_solution_file_paths(),
    ids=lambda path: f"{path.parent.name}/{path.name}",
)
def test_project_euler(solution_path: pathlib.Path):
    """Testing for all Project Euler solutions"""
    # problem_[extract this part] and pad it with zeroes for width 3
    problem_number: str = solution_path.parent.name[8:].zfill(3)
    expected: str = PROBLEM_ANSWERS[problem_number]
    solution_module = convert_path_to_module(solution_path)
    answer = str(solution_module.solution())
    assert answer == expected, f"Expected {expected} but got {answer}"
