"""Basic Theta* from "Theta*: Any-Angle Path Planning on Grids".

Alex Nash, Kenny Daniel, Sven Koenig, Ariel Felner (2007).
https://cdn.aaai.org/AAAI/2007/AAAI07-187.pdf

Programmer: Uzia Peer
Date: 2026-10-12
"""

import heapq
import logging
from itertools import count, pairwise
from math import hypot, inf

grid_point = tuple[int, int]
logger = logging.getLogger(__name__)


class CornerGrid:
    """A rectangular grid whose path vertices are cell corners.

    The bottom row is ``cells[0]``. Obstacles are marked by 1.

    >>> grid = CornerGrid([[0, 1], [0, 0]])
    >>> grid.width, grid.height
    (2, 2)
    >>> grid.line_of_sight((0, 0), (2, 2))
    True
    """

    def __init__(self, cells: list[list[int]]) -> None:
        rows = tuple(tuple(row) for row in cells)
        if not rows or not rows[0] or any(len(row) != len(rows[0]) for row in rows):
            raise ValueError("Grid must be a non-empty rectangular matrix.")
        if any(
            type(cell) is not int or cell not in (0, 1) for row in rows for cell in row
        ):
            raise ValueError("Cells must be integers 0 (free) or 1 (blocked).")
        self.cells = rows
        self.height, self.width = len(rows), len(rows[0])

    def blocked(self, column: int, row: int) -> bool:
        """Treat cells outside the grid as blocked.

        >>> CornerGrid([[0]]).blocked(-1, 0)
        True
        """
        return not (0 <= column < self.width and 0 <= row < self.height) or bool(
            self.cells[row][column]
        )

    def valid_corner(self, point: grid_point) -> bool:
        """A usable corner touches at least one free cell.

        >>> CornerGrid([[1]]).valid_corner((0, 0))
        False
        """
        if not isinstance(point, tuple) or len(point) != 2:
            return False
        x, y = point
        if type(x) is not int or type(y) is not int:
            return False
        return (
            0 <= x <= self.width
            and 0 <= y <= self.height
            and any(not self.blocked(cx, cy) for cx in (x - 1, x) for cy in (y - 1, y))
        )

    def line_of_sight(self, start: grid_point, end: grid_point) -> bool:
        """Test visibility with integer grid traversal, as in the paper.

        Diagonal contact at one corner is allowed, but moving along an edge
        shared by two blocked cells is not.

        >>> CornerGrid([[0, 1], [1, 0]]).line_of_sight((0, 0), (2, 2))
        True
        >>> CornerGrid([[1], [1]]).line_of_sight((0, 0), (0, 2))
        False
        """
        if not self.valid_corner(start) or not self.valid_corner(end):
            return False
        x, y = start
        dx, dy = abs(end[0] - x), abs(end[1] - y)
        sx = 1 if end[0] >= x else -1
        sy = 1 if end[1] >= y else -1
        ox, oy = (sx - 1) // 2, (sy - 1) // 2
        error = 0
        if dx >= dy:
            while x != end[0]:
                error += dy
                if error >= dx:
                    if self.blocked(x + ox, y + oy):
                        return False
                    y += sy
                    error -= dx
                if error and self.blocked(x + ox, y + oy):
                    return False
                if dy == 0 and self.blocked(x + ox, y) and self.blocked(x + ox, y - 1):
                    return False
                x += sx
        else:
            while y != end[1]:
                error += dx
                if error >= dy:
                    if self.blocked(x + ox, y + oy):
                        return False
                    x += sx
                    error -= dy
                if error and self.blocked(x + ox, y + oy):
                    return False
                if dx == 0 and self.blocked(x, y + oy) and self.blocked(x - 1, y + oy):
                    return False
                y += sy
        return True

    def neighbors(self, point: grid_point) -> list[grid_point]:
        """Return visible neighboring corners in a fixed order.

        >>> CornerGrid([[0]]).neighbors((0, 0))
        [(0, 1), (1, 0), (1, 1)]
        """
        x, y = point
        candidates = ((x + dx, y + dy) for dx in (-1, 0, 1) for dy in (-1, 0, 1))
        return [q for q in candidates if q != point and self.line_of_sight(point, q)]


def distance(first: grid_point, second: grid_point) -> float:
    """Euclidean distance ``c(a,b)`` from the paper.

    >>> distance((0, 0), (3, 4))
    5.0
    """
    return hypot(first[0] - second[0], first[1] - second[1])


def path_length(path: list[grid_point]) -> float:
    """Add the lengths of the path segments.

    >>> path_length([(0, 0), (3, 4), (6, 4)])
    8.0
    """
    return sum(distance(a, b) for a, b in pairwise(path))


def reconstruct_path(
    parent: dict[grid_point, grid_point], goal: grid_point
) -> list[grid_point]:
    """Follow parent pointers from the goal back to the start.

    >>> reconstruct_path({(0, 0): (0, 0), (1, 1): (0, 0)}, (1, 1))
    [(0, 0), (1, 1)]
    """
    path = [goal]
    while parent[path[-1]] != path[-1]:
        path.append(parent[path[-1]])
    return path[::-1]


def theta_star(
    grid: list[list[int]], start: grid_point, goal: grid_point
) -> list[grid_point]:
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
    corner_grid = CornerGrid(grid)
    if not corner_grid.valid_corner(start) or not corner_grid.valid_corner(goal):
        raise ValueError("Start and goal must be usable integer grid corners.")
    return _search(corner_grid, start, goal)


def _search(
    corner_grid: CornerGrid, start: grid_point, goal: grid_point
) -> list[grid_point]:
    """Run Basic Theta* on a validated grid (shared with the cache experiment).

    >>> _search(CornerGrid([[0]]), (0, 0), (1, 1))
    [(0, 0), (1, 1)]
    """

    # g, parent, open, and closed use the same meanings as in Algorithms 1-2.
    # h is the Euclidean distance to goal. Equal f prefers smaller g.
    g = {start: 0.0}
    parent = {start: start}
    closed: set[grid_point] = set()
    serial = count()
    opened = [(distance(start, goal), 0.0, next(serial), start)]

    while opened:
        _, old_g, _, current = heapq.heappop(opened)
        if current in closed or old_g != g[current]:
            continue
        logger.debug("Expand %s g=%.6f parent=%s", current, g[current], parent[current])
        if current == goal:
            path = reconstruct_path(parent, goal)
            logger.info("Found path of length %.6f", path_length(path))
            return path

        closed.add(current)
        for neighbor in corner_grid.neighbors(current):
            if neighbor in closed:
                logger.debug("Skip closed neighbor %s", neighbor)
                continue

            # Path 2 goes directly from parent(current) to neighbor if visible.
            # Otherwise Path 1 goes through current.
            previous = parent[current]
            shortcut = corner_grid.line_of_sight(previous, neighbor)
            candidate_parent = previous if shortcut else current
            branch = "Path 2" if shortcut else "Path 1"
            candidate = g[candidate_parent] + distance(candidate_parent, neighbor)
            if candidate < g.get(neighbor, inf):
                g[neighbor], parent[neighbor] = candidate, candidate_parent
                heapq.heappush(
                    opened,
                    (
                        candidate + distance(neighbor, goal),
                        candidate,
                        next(serial),
                        neighbor,
                    ),
                )
                logger.debug(
                    "%s: %s -> %s; g=%.6f",
                    branch,
                    candidate_parent,
                    neighbor,
                    candidate,
                )
            else:
                logger.debug("%s: no improvement for %s", branch, neighbor)

    logger.info("No path from %s to %s", start, goal)
    return []
