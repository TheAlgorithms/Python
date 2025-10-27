#!/usr/bin/env python3
"""
Pure Python implementation of the A* (A-star) pathfinding algorithm.

For doctests run:
    python3 -m doctest -v astar.py

For manual testing run:
    python3 astar.py
"""

import heapq
from collections.abc import Callable, Iterable

# Type aliases (PEP 585 built-in generics, PEP 604 unions)
Node = tuple[int, int]
NeighborsFn = Callable[[Node], Iterable[tuple[Node, float]]]
HeuristicFn = Callable[[Node, Node], float]


def astar(
    start: Node,
    goal: Node,
    neighbors: NeighborsFn,
    h: HeuristicFn,
) -> list[Node] | None:
    """
    A* algorithm for pathfinding on a graph defined by a neighbor function.

    A* maintains:
      * g[n]: cost from start to node n (best known so far)
      * f[n] = g[n] + h(n, goal): estimated total cost through n to goal
      * open_list: min-heap of candidate nodes by smallest f-score
      * closed_list: nodes already expanded (best path to them fixed)

    :param start: starting node
    :param goal: target node
    :param neighbors: function returning (neighbor, step_cost) pairs for a node
    :param h: admissible heuristic h(n, goal) estimating remaining cost
    :return: path from start to goal (inclusive), or None if no path

    Examples:
    >>> def _h(a: Node, b: Node) -> float:  # Manhattan distance
    ...     (x1, y1), (x2, y2) = a, b
    ...     return abs(x1 - x2) + abs(y1 - y2)
    >>> def _nbrs(p: Node):
    ...     x, y = p
    ...     return [
    ...         ((x + 1, y), 1),
    ...         ((x - 1, y), 1),
    ...         ((x, y + 1), 1),
    ...         ((x, y - 1), 1),
    ...     ]
    >>> path = astar((0, 0), (2, 2), _nbrs, _h)
    >>> path is not None and path[0] == (0, 0) and path[-1] == (2, 2)
    True
    """
    # Min-heap of (f_score, node)
    open_list: list[tuple[float, Node]] = []

    # Nodes we've fully explored (their best path is finalized)
    closed_list: set[Node] = set()

    # g-scores: best known cost to reach each node from start
    g: dict[Node, float] = {start: 0.0}

    # Parent map to reconstruct the path once we reach the goal
    parent: dict[Node, Node | None] = {start: None}

    # Initialize the frontier with the start node (f = h(start, goal))
    heapq.heappush(open_list, (h(start, goal), start))

    while open_list:
        # Pop the node with the smallest f-score (best promising path so far)
        _, current = heapq.heappop(open_list)

        # If we've already expanded this node via a better path, skip it
        if current in closed_list:
            continue
        closed_list.add(current)

        # Goal check: reconstruct the path by following parents backward
        if current == goal:
            path: list[Node] = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]  # reverse to (start ... goal)

        # Explore current's neighbors
        for neighbor, cost in neighbors(current):
            # If neighbor was already finalized, ignore
            if neighbor in closed_list:
                continue

            # Tentative g-score via current
            tentative_g = g[current] + cost

            # If first time seeing neighbor, or we found a cheaper path to it
            if neighbor not in g or tentative_g < g[neighbor]:
                g[neighbor] = tentative_g
                parent[neighbor] = current
                f_score = tentative_g + h(neighbor, goal)
                heapq.heappush(open_list, (f_score, neighbor))

    # If the frontier empties without reaching the goal, no path exists
    return None


def heuristic(n: Node, goal: Node) -> float:
    """Manhattan (L1) distance for 4-connected grid movement with unit costs."""
    x1, y1 = n
    x2, y2 = goal
    return abs(x1 - x2) + abs(y1 - y2)


def neighbors(node: Node) -> Iterable[tuple[Node, float]]:
    """
    4-neighborhood on an unbounded grid with unit edge costs.

    Replace/extend this for bounds, obstacles, or diagonal moves.
    """
    x, y = node
    return [
        ((x + 1, y), 1),
        ((x - 1, y), 1),
        ((x, y + 1), 1),
        ((x, y - 1), 1),
    ]


if __name__ == "__main__":
    # Example usage / manual test
    import doctest

    doctest.testmod()
    start: Node = (0, 0)
    goal: Node = (5, 5)
    path = astar(start, goal, neighbors, heuristic)
    print("Path found:", path)
    # Output: Path found: [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5)]
