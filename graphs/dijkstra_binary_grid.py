"""
This script implements the Dijkstra algorithm on a binary grid.
The grid consists of 0s and 1s, where 1 represents
a walkable node and 0 represents an obstacle.
The algorithm finds the shortest path from a start node to a destination node.
Diagonal movement can be allowed or disallowed.
"""

from heapq import heappop, heappush

import numpy as np


def dijkstra(
    grid: np.ndarray,
    source: tuple[int, int],
    destination: tuple[int, int],
    allow_diagonal: bool,
) -> tuple[float | int, list[tuple[int, int]]]:
    """
    Implements Dijkstra's algorithm on a binary grid.

    Args:
        grid (np.ndarray): A 2D numpy array representing the grid.
        1 represents a walkable node and 0 represents an obstacle.
        source (Tuple[int, int]): A tuple representing the start node.
        destination (Tuple[int, int]): A tuple representing the
        destination node.
        allow_diagonal (bool): A boolean determining whether
        diagonal movements are allowed.

    Returns:
        Tuple[Union[float, int], List[Tuple[int, int]]]:
        The shortest distance from the start node to the destination node
        and the shortest path as a list of nodes.

    >>> dijkstra(np.array([[1, 1, 1], [0, 1, 0], [0, 1, 1]]), (0, 0), (2, 2), False)
    (4.0, [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)])

    >>> dijkstra(np.array([[1, 1, 1], [0, 1, 0], [0, 1, 1]]), (0, 0), (2, 2), True)
    (2.0, [(0, 0), (1, 1), (2, 2)])

    >>> dijkstra(np.array([[1, 1, 1], [0, 0, 1], [0, 1, 1]]), (0, 0), (2, 2), False)
    (4.0, [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)])
    """
    rows, cols = grid.shape
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    if allow_diagonal:
        dx += [-1, -1, 1, 1]
        dy += [-1, 1, -1, 1]

    queue, visited = [(0, source)], set()
    matrix = np.full((rows, cols), np.inf)
    matrix[source] = 0
    predecessors = np.empty((rows, cols), dtype=object)
    predecessors[source] = None

    while queue:
        (dist, (x, y)) = heappop(queue)
        if (x, y) in visited:
            continue
        visited.add((x, y))

        if (x, y) == destination:
            path = []
            while (x, y) != source:
                path.append((x, y))
                x, y = predecessors[x, y]
            path.append(source)  # add the source manually
            path.reverse()
            return matrix[destination], path

        for i in range(len(dx)):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < rows and 0 <= ny < cols:
                next_node = grid[nx][ny]
                if next_node == 1 and matrix[nx, ny] > dist + 1:
                    heappush(queue, (dist + 1, (nx, ny)))
                    matrix[nx, ny] = dist + 1
                    predecessors[nx, ny] = (x, y)

    return np.inf, []


if __name__ == "__main__":
    import doctest

    doctest.testmod()
