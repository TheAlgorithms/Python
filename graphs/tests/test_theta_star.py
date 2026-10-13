"""Tests for "Theta*: Any-Angle Path Planning on Grids".

Alex Nash, Kenny Daniel, Sven Koenig, Ariel Felner (2007).
https://cdn.aaai.org/AAAI/2007/AAAI07-187.pdf
Programmer: Uzia Peer. Date: 2026-10-12.
"""

from fractions import Fraction
from itertools import pairwise
from math import dist
from random import Random

import pytest

from graphs.theta_star import theta_star

Point = tuple[int, int]


def segment_is_clear(grid: list[list[int]], start: Point, end: Point) -> bool:
    """Check a segment independently by splitting it at grid lines."""
    height, width = len(grid), len(grid[0])

    def is_free(x: int, y: int) -> bool:
        return 0 <= x < width and 0 <= y < height and grid[y][x] == 0

    for x, y in (start, end):
        if not (0 <= x <= width and 0 <= y <= height):
            return False
        if not any(is_free(cx, cy) for cx in (x - 1, x) for cy in (y - 1, y)):
            return False

    dx, dy = end[0] - start[0], end[1] - start[1]
    cuts = {Fraction(0), Fraction(1)}
    for axis, delta, size in ((0, dx, width), (1, dy, height)):
        if delta:
            cuts.update(
                Fraction(k - start[axis], delta)
                for k in range(size + 1)
                if 0 < Fraction(k - start[axis], delta) < 1
            )

    for lower, upper in pairwise(sorted(cuts)):
        midpoint = (lower + upper) / 2
        x = start[0] + midpoint * dx
        y = start[1] + midpoint * dy
        xs = (int(x) - 1, int(x)) if x.denominator == 1 else (int(x // 1),)
        ys = (int(y) - 1, int(y)) if y.denominator == 1 else (int(y // 1),)
        if not any(is_free(cx, cy) for cx in xs for cy in ys):
            return False
    return True


@pytest.mark.parametrize("size", [1, 2, 3])
def test_small_free_grids(size: int) -> None:
    grid = [[0] * size for _ in range(size)]
    assert theta_star(grid, (0, 0), (size, size)) == [(0, 0), (size, size)]


@pytest.mark.parametrize(
    ("goal", "expected"),
    [
        ((0, 0), [(3, 2), (2, 1), (0, 0)]),
        ((1, 0), [(3, 2), (1, 0)]),
    ],
)
def test_paper_figures_1_and_3(goal: Point, expected: list[Point]) -> None:
    grid = [[0, 0, 0, 1], [0, 1, 0, 0]]
    assert theta_star(grid, (3, 2), goal) == expected


def test_paper_figure_2() -> None:
    grid = [[0] * 6 for _ in range(3)]
    grid[0][2] = 1
    assert theta_star(grid, (6, 3), (0, 0)) == [(6, 3), (0, 0)]


@pytest.mark.parametrize(
    ("goal", "expected"),
    [
        ((8, 3), [(0, 0), (6, 2), (8, 3)]),
        ((9, 2), [(0, 0), (6, 2), (9, 2)]),
    ],
)
def test_paper_figure_4(goal: Point, expected: list[Point]) -> None:
    grid = [[0] * 9 for _ in range(4)]
    grid[2][4] = grid[1][6] = 1
    assert theta_star(grid, (0, 0), goal) == expected


def test_obstacle_requires_a_turn() -> None:
    grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    assert theta_star(grid, (0, 0), (3, 3)) == [(0, 0), (1, 2), (3, 3)]


def test_same_start_and_goal() -> None:
    assert theta_star([[0]], (0, 0), (0, 0)) == [(0, 0)]


def test_no_path() -> None:
    assert theta_star([[0, 1, 0], [0, 1, 0]], (0, 0), (3, 0)) == []


def test_diagonal_touching_is_allowed() -> None:
    assert theta_star([[0, 1], [1, 0]], (0, 0), (2, 2)) == [(0, 0), (2, 2)]


@pytest.mark.parametrize("grid", [[], [[]], [[0], [0, 1]], [[2]], [[True]]])
def test_invalid_grid(grid: list[list[int]]) -> None:
    with pytest.raises(ValueError):
        theta_star(grid, (0, 0), (1, 1))


@pytest.mark.parametrize("start", [(-1, 0), (2, 0), (0.5, 0), (True, 0)])
def test_invalid_start(start: tuple[float, int]) -> None:
    with pytest.raises(ValueError):
        theta_star([[0]], start, (1, 1))


def test_large_free_grid() -> None:
    grid = [[0] * 100 for _ in range(100)]
    assert theta_star(grid, (0, 0), (100, 100)) == [(0, 0), (100, 100)]


@pytest.mark.parametrize("seed", [7, 17, 91])
def test_large_random_grid(seed: int) -> None:
    rng = Random(seed)
    grid = [[int(rng.random() < 0.15) for _ in range(70)] for _ in range(70)]
    grid[0] = [0] * 70
    for row in grid:
        row[-1] = 0

    path = theta_star(grid, (0, 0), (70, 70))
    assert path and path[0] == (0, 0) and path[-1] == (70, 70)
    assert all(segment_is_clear(grid, a, b) for a, b in pairwise(path))
    assert sum(dist(a, b) for a, b in pairwise(path)) >= dist(path[0], path[-1])


def test_random_example_from_assignment_1() -> None:
    rng = Random(17)
    grid = [[int(rng.random() < 0.15) for _ in range(10)] for _ in range(10)]
    grid[0][0] = grid[-1][-1] = 0
    assert theta_star(grid, (0, 0), (10, 10)) == [(0, 0), (6, 7), (9, 10), (10, 10)]
