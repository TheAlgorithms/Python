"""
Topological Sort implementation using:
1. DFS-based approach
2. Kahn's Algorithm (BFS-based)

Topological sorting is applicable only for Directed Acyclic Graphs (DAGs).
"""

from collections import deque, defaultdict
from typing import List


def topological_sort_dfs(vertices: int, edges: List[List[int]]) -> List[int]:
    """
    Perform topological sort using DFS.

    :param vertices: Number of vertices in the graph
    :param edges: List of directed edges [u, v] where u -> v
    :return: A list representing topological order
    :raises ValueError: If a cycle is detected
    """
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    visited = [0] * vertices  # 0 = unvisited, 1 = visiting, 2 = visited
    stack = []

    def dfs(node: int):
        if visited[node] == 1:
            raise ValueError("Graph contains a cycle")
        if visited[node] == 2:
            return

        visited[node] = 1
        for neighbor in graph[node]:
            dfs(neighbor)
        visited[node] = 2
        stack.append(node)

    for v in range(vertices):
        if visited[v] == 0:
            dfs(v)

    return stack[::-1]


def topological_sort_kahn(vertices: int, edges: List[List[int]]) -> List[int]:
    """
    Perform topological sort using Kahn's Algorithm (BFS).

    :param vertices: Number of vertices in the graph
    :param edges: List of directed edges [u, v] where u -> v
    :return: A list representing topological order
    :raises ValueError: If a cycle is detected
    """
    graph = defaultdict(list)
    in_degree = [0] * vertices

    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    queue = deque([i for i in range(vertices) if in_degree[i] == 0])
    topo_order = []

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


if __name__ == "__main__":
    vertices = 6
    edges = [
        [5, 2],
        [5, 0],
        [4, 0],
        [4, 1],
        [2, 3],
        [3, 1],
    ]

    print("DFS-based Topological Sort:")
    print(topological_sort_dfs(vertices, edges))

    print("\nKahn's Algorithm Topological Sort:")
    print(topological_sort_kahn(vertices, edges))
