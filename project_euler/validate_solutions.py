#!/usr/bin/env python3
import importlib.util
import logging
import pathlib

LOG_FILENAME = "project_euler_test.log"

# Keep the answer part in str for consistency as some problems could output in str
# Problem 329: 199740353/29386561536000 (Format for this answer is a/b)
# https://github.com/nayuki/Project-Euler-solutions/blob/master/Answers.txt#L191
ANSWERS = {
    1: "233168",
    2: "4613732",
    3: "6857",
    4: "906609",
    5: "232792560",
    6: "25164150",
    7: "104743",
    8: "23514624000",
    9: "31875000",
    10: "142913828922",
    11: "70600674",
    12: "76576500",
    13: "5537376230",
    14: "837799",
    15: "137846528820",
    16: "1366",
    17: "21124",
    18: "1074",
    19: "171",
}

WORKING_DIR = pathlib.Path.cwd()

if WORKING_DIR.name == "Python":
    PROJECT_EULER_PATH = WORKING_DIR.joinpath("project_euler")
# Below two checks are just in case something goes wrong
# Travis root dir = /home/travis/build/TheAlgorithms/Python
# https://travis-ci.com/github/TheAlgorithms/Python/builds/186187397#L398
elif WORKING_DIR.name == "TheAlgorithms":
    PROJECT_EULER_PATH = WORKING_DIR.joinpath("Python", "project_euler")
elif WORKING_DIR.name == "project_euler":
    PROJECT_EULER_PATH = WORKING_DIR

# Remove previous log file if present
pathlib.Path.unlink(WORKING_DIR.joinpath(LOG_FILENAME), missing_ok=True)

# This should be after removing the log file if present
logging.basicConfig(
    filename=LOG_FILENAME, format="%(levelname)s: %(message)s", level=logging.DEBUG,
)


def generate_solution_modules(dir_path: pathlib.Path):
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


def test_project_euler() -> int:
    wrong_answer, no_solution, solution_args = [[] for _ in range(3)]
    for problem_number, expected in ANSWERS.items():
        problem_dir = PROJECT_EULER_PATH.joinpath(f"problem_{problem_number:02}")
        # By checking if it's a directory we can write all the problem number and
        # answer pair in ANSWERS variable and not worry whether it is actually
        # present in the 'project_euler' directory
        if problem_dir.is_dir():
            for solution_module in generate_solution_modules(problem_dir):
                try:
                    answer = str(solution_module.solution())
                    assert answer == expected, f"Expected: {expected} but got {answer}"
                # TypeError: If solution() requires arguments
                # AssertionError: If answer is incorrect
                # AttributeError: If the module has no attribute called 'solution'
                # except (AssertionError, AttributeError, TypeError) as err:
                #     logging.error(
                #         f"{err} \nSource: Problem {problem_number}: "
                #         f"{solution_module.__name__}\n"
                #     )
                except AssertionError as err:
                    wrong_answer.append(
                        f"problem_{problem_number}/{solution_module.__name__}: {err}"
                    )
                except AttributeError as err:
                    no_solution.append(
                        f"problem_{problem_number}/{solution_module.__name__}: {err}"
                    )
                except TypeError as err:
                    solution_args.append(
                        f"problem_{problem_number}/{solution_module.__name__}: {err}"
                    )
    if wrong_answer:
        print(f"{len(wrong_answer)} files contain wrong answers:\n")
        print("\n".join(wrong_answer) + "\n")
    if solution_args:
        print(
            f"{len(solution_args)} files require positional arguments for solution() function:\n"
        )
        print("\n".join(solution_args) + "\n")
    if no_solution:
        print(f"{len(no_solution)} files have no solution() function:\n")
        print("\n".join(no_solution) + "\n")
    return len(wrong_answer + solution_args + no_solution)


if __name__ == "__main__":
    exit_code = test_project_euler()
    if exit_code:
        import sys

        sys.exit(exit_code)
