"""
Hopcroft-Karp maximum matching for bipartite graphs
<https://en.wikipedia.org/wiki/Hopcroft%E2%80%93Karp_algorithm>
"""

from collections import deque
from typing import cast

INF = float("inf")
NIL: int | None = None


def bfs(
    graph: dict[int, list[int]],
    u_vertices: list[int],
    pair_u: dict[int, int | None],
    pair_v: dict[int, int | None],
    dist: dict[int | None, float],
) -> bool:
    """Build BFS layers from every free vertex in *U*.

    Returns `True` when at least one augmenting path exists.
    """
    queue: deque[int] = deque()

    for u in u_vertices:
        if pair_u[u] is NIL:
            dist[u] = 0
            queue.append(u)
        else:
            dist[u] = INF
    dist[NIL] = INF

    while queue:
        u = queue.popleft()
        if dist[u] < dist[NIL]:
            for v in graph[u]:
                nxt: int | None = pair_v[v]
                if nxt is None or dist.get(nxt, INF) is INF:
                    if nxt is None:
                        dist[NIL] = dist[u] + 1
                    else:
                        dist[nxt] = dist[u] + 1
                        queue.append(nxt)
    return dist[NIL] is not INF


def dfs(
    u: int | None,
    graph: dict[int, list[int]],
    pair_u: dict[int, int | None],
    pair_v: dict[int, int | None],
    dist: dict[int | None, float],
) -> bool:
    """Depth-first search that respects BFS layers and flips one path."""
    if u is NIL:
        return True
    u_int = cast(int, u)

    for v in graph[u_int]:
        nxt: int | None = pair_v[v]
        condition = (nxt is None or dist.get(nxt, INF) == dist[u_int] + 1) and dfs(
            nxt if nxt is not None else NIL, graph, pair_u, pair_v, dist
        )
        if condition:
            pair_v[v] = u_int
            pair_u[u_int] = v
            return True

    dist[u_int] = INF
    return False


def hopcroft_karp(graph: dict[int, list[int]]) -> int:
    """Return the size of a maximum matching.

    The graph is supplied as `{u0: [v1, v2, ...], ...}` mapping *U* → *V*.

    >>> hopcroft_karp({0: [0, 1], 1: [0]})
    2
    >>> hopcroft_karp({0: [1], 1: [2], 2: []})
    2
    >>> hopcroft_karp({0: [0, 1, 2], 1: [0, 1, 2], 2: [0, 1, 2]})
    3
    >>> hopcroft_karp({})
    Traceback (most recent call last):
    ...
    ValueError: Graph is empty, no vertices in U set.
    """
    if not graph:
        raise ValueError("Graph is empty, no vertices in U set.")

    u_vertices = list(graph)
    v_vertices = {v for nbrs in graph.values() for v in nbrs}

    pair_u: dict[int, int | None] = dict.fromkeys(u_vertices, NIL)
    pair_v: dict[int, int | None] = dict.fromkeys(v_vertices, NIL)
    dist: dict[int | None, float] = {}

    match_size = 0
    while bfs(graph, u_vertices, pair_u, pair_v, dist):
        for u in u_vertices:
            if pair_u[u] is NIL and dfs(u, graph, pair_u, pair_v, dist):
                match_size += 1
    return match_size


if __name__ == "__main__":
    import doctest

    doctest.testmod()
