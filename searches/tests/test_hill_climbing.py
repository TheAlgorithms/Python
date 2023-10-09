import pytest
import math

import logging

# standard libraries
import sys
__package__ = 'searches.tests'
from ..hill_climbing import SearchProblem, hill_climbing

# Helper function to represent a simple function for testing
def simple_function(x, y):
    return x + y

# More complex function to test for local minima and maxima
def complex_function(x, y):
    return -(x ** 2) - (y ** 2) + 4


@pytest.mark.parametrize("x, y, step_size, expected", [
    (0, 0, 1, 0),
    (5, 5, 1, 10),
    (-5, -5, 1, -10),
])
def test_search_problem_score(x, y, step_size, expected):
    problem = SearchProblem(x, y, step_size, simple_function)
    assert problem.score() == expected


def test_search_problem_get_neighbors():
    problem = SearchProblem(0, 0, 1, simple_function)
    neighbors = problem.get_neighbors()

    expected_coords = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    for neighbor, coords in zip(neighbors, expected_coords):
        assert neighbor.x == coords[0]
        assert neighbor.y == coords[1]


def test_hill_climbing_for_maximum():
    # Using a function that has a maximum at (0, 0)
    problem = SearchProblem(3, 4, 1, complex_function)
    local_max = hill_climbing(problem, find_max=True)

    assert local_max.x == 0
    assert local_max.y == 0
    assert local_max.score() == 4


def test_hill_climbing_for_minimum():
    # Using a function that has a minimum along the line x = y
    problem = SearchProblem(3, 4, 1, simple_function)
    local_min = hill_climbing(problem, find_max=False)

    assert local_min.x == local_min.y
    assert local_min.score() == 2 * local_min.x


def test_hill_climbing_with_bounds():
    # Using bounds for x and y
    problem = SearchProblem(3, 4, 1, simple_function)
    local_min = hill_climbing(problem, find_max=False, max_x=3, min_x=2, max_y=4, min_y=3)

    assert local_min.x >= 2
    assert local_min.x <= 3
    assert local_min.y >= 3
    assert local_min.y <= 4


def test_hill_climbing_with_max_iterations():
    # Testing maximum number of iterations
    problem = SearchProblem(100, 100, 10, complex_function)
    local_max = hill_climbing(problem, find_max=True, max_iter=100)

    assert local_max.x == 0 or local_max.y == 0
    assert local_max.score() == 4