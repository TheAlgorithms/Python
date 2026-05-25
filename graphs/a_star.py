"""
A* (A-Star) Pathfinding Algorithm Implementation.

A* is an informed search algorithm (heuristic search) that finds the shortest
path between a start node and a goal node in a weighted graph. It balances
the actual distance from the start (g-score) and the estimated distance to
the goal (h-score) using the formula: f(n) = g(n) + h(n).

Time Complexity: O(E log V) where E is the number of edges and V is the 
                 number of vertices.
Space Complexity: O(V) to store the graph structures and priority queue.
"""


from __future__ import annotations

import heapq
import math
from collections.abc import Callable


# ==========================================
# 1. Heuristic Functions
# ==========================================


def manhattan_distance(a: tuple[float, float], b: tuple[float, float]) -> float:
    """Calculate the Manhattan distance between two 2D points."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def euclidean_distance(a: tuple[float, float], b: tuple[float, float]) -> float:
    """Calculate the Euclidean distance between two 2D points."""
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def chebyshev_distance(a: tuple[float, float], b: tuple[float, float]) -> float:
    """Calculate the Chebyshev distance between two 2D points."""
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))


# ==========================================
# 2. Grid-Based Implementation
# ==========================================


def a_star_grid(
    grid: list[list[float]],
    start: tuple[int, int],
    end: tuple[int, int],
    heuristic_func: Callable[[tuple[float, float], tuple[float, float]], float] = manhattan_distance,
) -> list[tuple[int, int]] | None:
    """
    Perform A* search on a 2D weighted grid using heapq.
    Grid values represent the traversal cost. float('inf') represents an obstacle.

    >>> grid = [[1.0, 1.0, 1.0], [1.0, float('inf'), 1.0], [1.0, 1.0, 1.0]]
    >>> a_star_grid(grid, (0, 0), (2, 2), manhattan_distance)
    [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]
    """
    rows, cols = len(grid), len(grid[0])
    open_set: list[tuple[float, tuple[int, int]]] = []
    heapq.heappush(open_set, (0.0, start))

    came_from: dict[tuple[int, int], tuple[int, int]] = {}
    g_score = {start: 0.0}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        # 4-directional movement
        for move_r, move_c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + move_r, current[1] + move_c)

            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                cost = grid[neighbor[0]][neighbor[1]]
                if cost == float("inf"):
                    continue

                tentative_g = g_score[current] + cost
                if tentative_g < g_score.get(neighbor, float("inf")):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + heuristic_func(neighbor, end)
                    if neighbor not in [item[1] for item in open_set]:
                        heapq.heappush(open_set, (f_score, neighbor))
    return None


# ==========================================
# 3. Adjacency List Implementation
# ==========================================


def a_star_adjacency_list(
    graph: dict[str, list[tuple[str, float]]],
    start: str,
    end: str,
    heuristic_dict: dict[str, float],
) -> list[str] | None:
    """
    Perform A* search on a graph represented as an adjacency list.
    heuristic_dict provides pre-calculated h-scores from each node to the goal.

    >>> graph = {
    ...     'A': [('B', 1.0), ('C', 4.0)],
    ...     'B': [('A', 1.0), ('D', 5.0)],
    ...     'C': [('A', 4.0), ('D', 1.0)],
    ...     'D': [('B', 5.0), ('C', 1.0)]
    ... }
    >>> h_dict = {'A': 3.0, 'B': 2.0, 'C': 1.0, 'D': 0.0}
    >>> a_star_adjacency_list(graph, 'A', 'D', h_dict)
    ['A', 'C', 'D']
    """
    open_set: list[tuple[float, str]] = []
    heapq.heappush(open_set, (0.0, start))

    came_from: dict[str, str] = {}
    g_score = {start: 0.0}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor, weight in graph.get(current, []):
            tentative_g = g_score[current] + weight
            if tentative_g < g_score.get(neighbor, float("inf")):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic_dict.get(neighbor, 0.0)
                if neighbor not in [item[1] for item in open_set]:
                    heapq.heappush(open_set, (f_score, neighbor))
    return None


if __name__ == "__main__":
    import doctest

    doctest.testmod()