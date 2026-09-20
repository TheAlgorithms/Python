"""
Hopcroft-Karp Algorithm for Maximum Cardinality Matching in Bipartite Graphs.
Time Complexity: O(E * sqrt(V))
"""

from collections import deque
from typing import Dict, List, Optional


class HopcroftKarp:
    """
    Computes maximum bipartite matching using the Hopcroft-Karp algorithm.

    >>> graph = {
    ...     1: [5, 6],
    ...     2: [5],
    ...     3: [6, 7],
    ...     4: [8]
    ... }
    >>> hk = HopcroftKarp(graph)
    >>> hk.max_matching()
    4
    """

    def __init__(self, graph: Dict[int, List[int]]) -> None:
        self.graph = graph
        self.pair_u: Dict[int, Optional[int]] = {u: None for u in graph}
        self.pair_v: Dict[int, Optional[int]] = {}
        for neighbors in graph.values():
            for v in neighbors:
                self.pair_v[v] = None
        self.dist: Dict[Optional[int], int] = {}

    def _bfs(self) -> bool:
        queue: deque[int] = deque()
        for u in self.graph:
            if self.pair_u[u] is None:
                self.dist[u] = 0
                queue.append(u)
            else:
                self.dist[u] = float("inf")
        self.dist[None] = float("inf")

        while queue:
            u = queue.popleft()
            if self.dist[u] < self.dist[None]:
                for v in self.graph.get(u, []):
                    next_u = self.pair_v[v]
                    if self.dist.get(next_u, float("inf")) == float("inf"):
                        self.dist[next_u] = self.dist[u] + 1
                        if next_u is not None:
                            queue.append(next_u)
        return self.dist[None] != float("inf")

    def _dfs(self, u: Optional[int]) -> bool:
        if u is not None:
            for v in self.graph.get(u, []):
                next_u = self.pair_v[v]
                if self.dist.get(next_u, float("inf")) == self.dist[u] + 1:
                    if self._dfs(next_u):
                        self.pair_v[v] = u
                        self.pair_u[u] = v
                        return True
            self.dist[u] = float("inf")
            return False
        return True

    def max_matching(self) -> int:
        matching = 0
        while self._bfs():
            for u in self.graph:
                if self.pair_u[u] is None and self._dfs(u):
                    matching += 1
        return matching


if __name__ == "__main__":
    import doctest

    doctest.testmod()
