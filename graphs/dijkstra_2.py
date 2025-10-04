"""
Dijkstra's Algorithm Implementation.

This module provides an implementation of Dijkstra's algorithm to find the
shortest paths from a source vertex to all other vertices in a weighted directed graph.

The graph is represented using an adjacency matrix where `float("inf")` represents
no direct edge between two vertices.

Example:
    >>> graph = [
    ...     [0, 4, float("inf"), float("inf"), float("inf"), float("inf"), float("inf"), 8, float("inf")],
    ...     [4, 0, 8, float("inf"), float("inf"), float("inf"), float("inf"), 11, float("inf")],
    ...     [float("inf"), 8, 0, 7, float("inf"), 4, float("inf"), float("inf"), 2],
    ...     [float("inf"), float("inf"), 7, 0, 9, 14, float("inf"), float("inf"), float("inf")],
    ...     [float("inf"), float("inf"), float("inf"), 9, 0, 10, float("inf"), float("inf"), float("inf")],
    ...     [float("inf"), float("inf"), 4, 14, 10, 0, 2, float("inf"), float("inf")],
    ...     [float("inf"), float("inf"), float("inf"), float("inf"), float("inf"), 2, 0, 1, 6],
    ...     [8, 11, float("inf"), float("inf"), float("inf"), float("inf"), 1, 0, 7],
    ...     [float("inf"), float("inf"), 2, float("inf"), float("inf"), float("inf"), 6, 7, 0],
    ... ]
    >>> dijkstra(graph, 0)
    [0, 4, 12, 19, 21, 11, 9, 8, 14]
"""

from typing import List


def _min_dist(dist: List[float], visited: List[bool]) -> int:
    """
    Find the vertex with the minimum distance value from the set of
    vertices that have not yet been visited.

    Args:
        dist: List of current shortest distances from the source.
        visited: Boolean list indicating visited vertices.

    Returns:
        Index of the vertex with the minimum distance value.
    """
    min_val = float("inf")
    min_index = -1
    for i, d in enumerate(dist):
        if not visited[i] and d < min_val:
            min_val = d
            min_index = i
    return min_index


def dijkstra(graph: List[List[float]], src: int) -> List[float]:
    """
    Compute shortest paths from a source vertex to all other vertices
    using Dijkstra's algorithm.

    Args:
        graph: Adjacency matrix representing the weighted graph.
        src: Source vertex index.

    Returns:
        A list containing the shortest distance from the source to each vertex.

    Raises:
        ValueError: If the source vertex index is invalid.

    Example:
        >>> graph = [
        ...     [0, 4, float("inf"), float("inf")],
        ...     [4, 0, 8, float("inf")],
        ...     [float("inf"), 8, 0, 7],
        ...     [float("inf"), float("inf"), 7, 0],
        ... ]
        >>> dijkstra(graph, 0)
        [0, 4, 12, 19]
    """
    num_vertices = len(graph)
    if src < 0 or src >= num_vertices:
        raise ValueError("Source vertex index out of range")

    dist = [float("inf")] * num_vertices
    visited = [False] * num_vertices
    dist[src] = 0.0

    for _ in range(num_vertices - 1):
        u = _min_dist(dist, visited)
        if u == -1:
            break  # Remaining vertices are unreachable
        visited[u] = True

        for v in range(num_vertices):
            if (
                not visited[v]
                and graph[u][v] != float("inf")
                and dist[u] + graph[u][v] < dist[v]
            ):
                dist[v] = dist[u] + graph[u][v]

    return [int(d) if d != float("inf") else float("inf") for d in dist]
