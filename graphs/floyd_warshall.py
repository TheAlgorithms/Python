"""
Floyd-Warshall Algorithm for All-Pairs Shortest Paths

Finds shortest paths between all pairs of vertices in a weighted graph.
Works with negative edge weights (but not negative cycles).

Time Complexity: O(V³)
Space Complexity: O(V²)
"""

from typing import List, Tuple, Optional


def floyd_warshall(
    graph: List[List[float]],
) -> Tuple[List[List[float]], List[List[Optional[int]]]]:
    """
    Compute all-pairs shortest paths using Floyd-Warshall algorithm.

    Args:
        graph: Adjacency matrix where graph[i][j] is weight from i to j.
               Use float('inf') for no edge. graph[i][i] should be 0.

    Returns:
        Tuple of (distance_matrix, next_matrix)
        - distance_matrix[i][j] = shortest distance from i to j
        - next_matrix[i][j] = next node to visit from i to reach j optimally

    Example:
        >>> graph = [[0, 3, float('inf'), 7],
        ...          [8, 0, 2, float('inf')],
        ...          [5, float('inf'), 0, 1],
        ...          [2, float('inf'), float('inf'), 0]]
        >>> dist, _ = floyd_warshall(graph)
        >>> dist[0][3]
        6
    """
    n = len(graph)

    # Initialize distance and path matrices
    dist = [row[:] for row in graph]  # Deep copy
    next_node = [
        [j if graph[i][j] != float("inf") and i != j else None for j in range(n)]
        for i in range(n)
    ]

    # Main algorithm: try each vertex as intermediate
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]

    # Check for negative cycles
    for i in range(n):
        if dist[i][i] < 0:
            raise ValueError("Graph contains negative weight cycle")

    return dist, next_node


def reconstruct_path(
    next_node: List[List[Optional[int]]], start: int, end: int
) -> Optional[List[int]]:
    """
    Reconstruct shortest path from start to end using next_node matrix.

    Time Complexity: O(V)
    """
    if next_node[start][end] is None:
        return None

    path = [start]
    current = start

    while current != end:
        current = next_node[current][end]  # type: ignore
        path.append(current)

    return path


def floyd_warshall_optimized(graph: List[List[float]]) -> List[List[float]]:
    """
    Space-optimized version using only distance matrix.
    Use when path reconstruction is not needed.

    Time Complexity: O(V³)
    Space Complexity: O(V²) but less overhead
    """
    n = len(graph)
    dist = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            if dist[i][k] == float("inf"):
                continue
            for j in range(n):
                if dist[k][j] == float("inf"):
                    continue
                new_dist = dist[i][k] + dist[k][j]
                if new_dist < dist[i][j]:
                    dist[i][j] = new_dist

    return dist


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Performance benchmark
    import random
    import time

    def benchmark():
        n = 200
        # Generate random dense graph
        graph = [
            [0 if i == j else random.randint(1, 100) for j in range(n)]
            for i in range(n)
        ]

        start = time.perf_counter()
        floyd_warshall(graph)
        elapsed = time.perf_counter() - start
        print(f"Floyd-Warshall on {n}x{n} graph: {elapsed:.3f}s")

    benchmark()
