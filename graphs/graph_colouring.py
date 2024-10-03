"""
Graph Coloring Problem is a classic problem in graph theory.
The task is to assign colors to the vertices of a graph so that no two adjacent vertices
share the same color, and the number of colors used is minimized.

Wikipedia: https://en.wikipedia.org/wiki/Graph_coloring
"""


def is_safe(graph: list[list[int]], color: list[int], v: int, c: int) -> bool:
    """
    Helper function to check if it is safe to color vertex `v` with color `c`.

    Parameters:
    graph (list[list[int]]): The adjacency matrix of the graph.
    color (list[int]): The list of colors assigned to each vertex.
    v (int): The vertex to check.
    c (int): The color to be assigned.

    Returns:
    bool: True if it's safe to assign color `c` to vertex `v`, otherwise False.

    Example:
    >>> graph = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    >>> color = [-1, -1, -1]
    >>> is_safe(graph, color, 0, 1)
    True
    """
    return all(not (graph[v][i] == 1 and color[i] == c) for i in range(len(graph)))


def graph_coloring_util(
    graph: list[list[int]], m: int, color: list[int], v: int
) -> bool:
    """
    Utility function that uses backtracking to solve the m-coloring problem.

    Parameters:
    graph (list[list[int]]): The adjacency matrix of the graph.
    m (int): The maximum number of colors.
    color (list[int]): The list of colors assigned to each vertex.
    v (int): The current vertex to be colored.

    Returns:
    bool: True if all vertices are successfully colored, otherwise False.

    Example:
    >>> graph = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    >>> color = [-1, -1, -1]
    >>> graph_coloring_util(graph, 3, color, 0)
    True
    """
    if v == len(graph):
        return True

    for c in range(1, m + 1):
        if is_safe(graph, color, v, c):
            color[v] = c
            if graph_coloring_util(graph, m, color, v + 1):
                return True
            color[v] = -1  # Backtrack

    return False


def graph_coloring(graph: list[list[int]], m: int) -> bool:
    """
    Solves the m-coloring problem using backtracking.

    Parameters:
    graph (list[list[int]]): The adjacency matrix of the graph.
    m (int): The maximum number of colors.

    Returns:
    bool: True if the graph can be colored with `m` colors, otherwise False.

    Example:
    >>> graph = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    >>> graph_coloring(graph, 3)
    True
    """
    color = [-1] * len(graph)
    return graph_coloring_util(graph, m, color, 0)
