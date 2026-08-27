"""
Minimum cut of a flow network via the Ford-Fulkerson algorithm.

The max-flow min-cut theorem says the value of a maximum flow from the source to
the sink equals the total capacity of the edges in a minimum s-t cut -- the
cheapest set of edges whose removal disconnects the sink from the source.  This
module finds those cut edges: it runs Ford-Fulkerson to build the residual
graph, then reports every original edge that goes from a vertex still reachable
from the source to a vertex that is not.

Reference: https://en.wikipedia.org/wiki/Minimum_cut
See also: https://en.wikipedia.org/wiki/Max-flow_min-cut_theorem
"""

test_graph = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0],
]


def bfs(graph: list[list[int]], s: int, t: int, parent: list[int]) -> bool:
    """
    Return True if the sink ``t`` is reachable from the source ``s`` in the
    residual ``graph``, recording the traversal tree in ``parent``.

    >>> bfs(test_graph, 0, 5, [-1] * 6)
    True
    >>> bfs([[0, 0], [0, 0]], 0, 1, [-1, -1])
    False
    """
    visited = [False] * len(graph)
    queue = [s]
    visited[s] = True

    while queue:
        u = queue.pop(0)
        for ind in range(len(graph[u])):
            if visited[ind] is False and graph[u][ind] > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u

    return visited[t]


def mincut(graph: list[list[int]], source: int, sink: int) -> list[tuple[int, int]]:
    """
    Return the edges of a minimum s-t cut as ``(from, to)`` tuples.

    The input ``graph`` is an adjacency matrix of capacities and is left
    unchanged (the algorithm works on an internal copy).

    >>> mincut(test_graph, source=0, sink=5)
    [(1, 3), (4, 3), (4, 5)]

    The capacities of the cut edges sum to the maximum flow (23 here):

    >>> sum(test_graph[u][v] for u, v in mincut(test_graph, 0, 5))
    23

    A single saturated edge is its own minimum cut:

    >>> mincut([[0, 7], [0, 0]], source=0, sink=1)
    [(0, 1)]
    """
    residual = [row[:] for row in graph]  # work on a copy; keep the input intact
    parent = [-1] * (len(residual))
    res = []
    while bfs(residual, source, sink, parent):
        path_flow = float("inf")
        s = sink

        while s != source:
            # Find the minimum residual capacity along the augmenting path.
            path_flow = min(path_flow, residual[parent[s]][s])
            s = parent[s]

        v = sink
        while v != source:
            u = parent[v]
            residual[u][v] -= path_flow
            residual[v][u] += path_flow
            v = parent[v]

    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] > 0 and residual[i][j] == 0:
                res.append((i, j))

    return res


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print(mincut(test_graph, source=0, sink=5))
