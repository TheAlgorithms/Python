"""
Topological Sort implementation using:
1. DFS-based approach
2. Kahn's Algorithm (BFS-based approach)

Topological sorting is applicable only for Directed Acyclic Graphs (DAGs).

Reference:
https://en.wikipedia.org/wiki/Topological_sorting
"""

from collections import deque
from typing import List


def _dfs(
    node: int,
    graph: List[List[int]],
    visited: List[int],
    result: List[int],
) -> None:
    """
    Helper DFS function for topological sorting.

    >>> graph = [[1], [], []]
    >>> visited = [0, 0, 0]
    >>> result = []
    >>> _dfs(0, graph, visited, result)
    >>> result
    [0]
    """
    if visited[node] == 1:
        raise ValueError("Graph contains a cycle")
    if visited[node] == 2:
        return

    visited[node] = 1
    for neighbor in graph[node]:
        _dfs(neighbor, graph, visited, result)
    visited[node] = 2
    result.append(node)


def topological_sort_dfs(vertices: int, edges: List[List[int]]) -> List[int]:
    """
    Perform topological sort using DFS.

    >>> order = topological_sort_dfs(
    ...     6, [[5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1]]
    ... )
    >>> len(order) == 6
    True
    """
    graph: List[List[int]] = [[] for _ in range(vertices)]
    for u, v in edges:
        graph[u].append(v)

    visited = [0] * vertices
    result: List[int] = []

    for vertex in range(vertices):
        if visited[vertex] == 0:
            _dfs(vertex, graph, visited, result)

    return result[::-1]


def topological_sort_kahn(vertices: int, edges: List[List[int]]) -> List[int]:
    """
    Perform topological sort using Kahn's Algorithm.

    >>> order = topological_sort_kahn(
    ...     6, [[5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1]]
    ... )
    >>> len(order) == 6
    True
    """
    graph: List[List[int]] = [[] for _ in range(vertices)]
    in_degree = [0] * vertices

    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    queue = deque(i for i in range(vertices) if in_degree[i] == 0)
    topo_order: List[int] = []

    while queue:
        node = queue.popleft()
        topo_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(topo_order) != vertices:
        raise ValueError("Graph contains a cycle")

    return topo_order
