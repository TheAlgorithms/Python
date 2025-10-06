from typing import List


def is_safe(node: int, color: int, graph: List[List[int]], n: int, col: List[int]) -> bool:
    return all(not (graph[node][k] == 1 and col[k] == color) for k in range(n))


def solve(node: int, col: List[int], m: int, n: int, graph: List[List[int]]) -> bool:
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
    col = [0] * n
    return solve(0, col, m, n, graph)
