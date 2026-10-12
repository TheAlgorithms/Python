"""Basic Theta* from "Theta*: Any-Angle Path Planning on Grids".

Alex Nash, Kenny Daniel, Sven Koenig, Ariel Felner (2007).
https://cdn.aaai.org/AAAI/2007/AAAI07-187.pdf

Programmer: Uzia Peer
Date: 2026-10-12
"""


def theta_star(
    grid: list[list[int]],  # noqa: ARG001
    start: tuple[int, int],  # noqa: ARG001
    goal: tuple[int, int],  # noqa: ARG001
) -> list[tuple[int, int]]:
    """Find an any-angle path through a grid using Basic Theta* (Algorithms 1-2).

    ``grid[y][x]`` is 0 for a free cell and 1 for an obstacle. The first row
    is the bottom row. ``start`` and ``goal`` are cell corners, not cell centers.
    A grid of width w and height h has corners from (0, 0) to (w, h).
    The path includes both endpoints. Return [] if no path exists. Invalid
    grids or endpoints raise ValueError. The path need not be globally shortest.

    Small free grids from assignment 1:

    >>> theta_star([[0]], (0, 0), (1, 1))
    [(0, 0), (1, 1)]
    >>> theta_star([[0, 0], [0, 0]], (0, 0), (2, 2))
    [(0, 0), (2, 2)]
    >>> theta_star([[0] * 3 for _ in range(3)], (0, 0), (3, 3))
    [(0, 0), (3, 3)]

    Paper figures 1 and 3: a turn near an obstacle and two update cases.

    >>> paper_grid = [[0, 0, 0, 1], [0, 1, 0, 0]]
    >>> theta_star(paper_grid, (3, 2), (0, 0))
    [(3, 2), (2, 1), (0, 0)]
    >>> theta_star(paper_grid, (3, 2), (1, 0))
    [(3, 2), (1, 0)]

    Paper figure 2: a path that post-smoothing cannot obtain from A*'s route.

    >>> cells = [[0] * 6 for _ in range(3)]
    >>> cells[0][2] = 1
    >>> theta_star(cells, (6, 3), (0, 0))
    [(6, 3), (0, 0)]

    Paper figure 4: Basic Theta* can miss a shorter path.

    >>> cells = [[0] * 9 for _ in range(4)]
    >>> cells[2][4] = cells[1][6] = 1
    >>> theta_star(cells, (0, 0), (8, 3))
    [(0, 0), (6, 2), (8, 3)]
    >>> theta_star(cells, (0, 0), (9, 2))
    [(0, 0), (6, 2), (9, 2)]

    Additional edge cases from assignment 1:

    >>> theta_star([[0, 0, 0], [0, 1, 0], [0, 0, 0]], (0, 0), (3, 3))
    [(0, 0), (1, 2), (3, 3)]
    >>> theta_star([[0]], (0, 0), (0, 0))
    [(0, 0)]
    >>> theta_star([[0, 1, 0], [0, 1, 0]], (0, 0), (3, 0))
    []
    >>> theta_star([[0, 1], [1, 0]], (0, 0), (2, 2))
    [(0, 0), (2, 2)]

    A reproducible larger random grid:

    >>> from random import Random
    >>> rng = Random(17)
    >>> cells = [[int(rng.random() < 0.15) for _ in range(10)] for _ in range(10)]
    >>> cells[0][0] = cells[-1][-1] = 0
    >>> path = theta_star(cells, (0, 0), (10, 10))
    >>> path
    [(0, 0), (6, 7), (9, 10), (10, 10)]
    """
    # Assignment 4: search intentionally left empty. Tests should fail.
    return []
