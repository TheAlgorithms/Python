from typing import List


def is_safe(
    node: int, color: int, graph: List[List[int]], n: int, col: List[int]
) -> bool:
    """
    Check if it is safe to assign a color to a node.

    >>> is_safe(0, 1, [[0,1],[1,0]], 2, [0,1])
    False
    >>> is_safe(0, 2, [[0,1],[1,0]], 2, [0,1])
    True
    """
    return all(not (graph[node][k] == 1 and col[k] == color) for k in range(n))


def solve(node: int, col: List[int], m: int, n: int, graph: List[List[int]]) -> bool:
    """
    Recursively try to color the graph using at most m colors.

    >>> solve(0, [0]*3, 3, 3, [[0,1,0],[1,0,1],[0,1,0]])
    True
    >>> solve(0, [0]*3, 2, 3, [[0,1,0],[1,0,1],[0,1,0]])
    False
    """
    if node == n:
        return True
    for c in range(1, m + 1):
        if is_safe(node, c, graph, n, col):
            col[node] = c
            if solve(node + 1, col, m, n, graph):
                return True
            col[node] = 0
    return False


def graph_coloring(graph: List[List[int]], m: int, n: int) -> bool:
    """
    Determine if the graph can be colored with at most m colors.

    >>> graph_coloring([[0,1,1],[1,0,1],[1,1,0]], 3, 3)
    True
    >>> graph_coloring([[0,1,1],[1,0,1],[1,1,0]], 2, 3)
    False
    """
    col = [0] * n
    return solve(0, col, m, n, graph)
