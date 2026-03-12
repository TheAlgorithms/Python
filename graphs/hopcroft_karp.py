"""
Hopcroft-Karp Algorithm for Maximum Bipartite Matching

Finds maximum cardinality matching in bipartite graphs.
Much faster than augmenting path method: O(E√V) vs O(VE)

Time Complexity: O(E√V)
Space Complexity: O(V)
"""

from typing import List, Dict, Set, Optional
from collections import deque


class HopcroftKarp:
    """
    Maximum bipartite matching using Hopcroft-Karp algorithm.

    Partition U (0..n-1) connects to partition V (0..m-1)
    """

    def __init__(self, n_left: int, n_right: int):
        self.n = n_left
        self.m = n_right
        self.graph: Dict[int, List[int]] = {u: [] for u in range(n_left)}
        self.pair_u: List[Optional[int]] = [None] * n_left
        self.pair_v: List[Optional[int]] = [None] * n_right
        self.dist: List[int] = [0] * n_left

    def add_edge(self, u: int, v: int) -> None:
        """Add edge from left partition u to right partition v."""
        self.graph[u].append(v)

    def bfs(self) -> bool:
        """
        Build level graph using BFS.
        Returns True if augmenting path exists.
        """
        queue = deque()

        for u in range(self.n):
            if self.pair_u[u] is None:
                self.dist[u] = 0
                queue.append(u)
            else:
                self.dist[u] = float("inf")  # type: ignore

        found_augmenting = False

        while queue:
            u = queue.popleft()

            for v in self.graph[u]:
                pair_v = self.pair_v[v]
                if pair_v is not None and self.dist[pair_v] == float("inf"):  # type: ignore
                    self.dist[pair_v] = self.dist[u] + 1
                    queue.append(pair_v)
                elif pair_v is None:
                    found_augmenting = True  # Found free vertex in V

        return found_augmenting

    def dfs(self, u: int) -> bool:
        """
        DFS to find augmenting paths along level graph.
        """
        for v in self.graph[u]:
            pair_v = self.pair_v[v]
            if pair_v is None or (
                self.dist[pair_v] == self.dist[u] + 1 and self.dfs(pair_v)
            ):
                self.pair_u[u] = v
                self.pair_v[v] = u
                return True

        self.dist[u] = float("inf")  # type: ignore
        return False

    def max_matching(self) -> int:
        """
        Compute maximum matching size.

        Returns:
            Size of maximum matching

        Example:
            >>> hk = HopcroftKarp(4, 4)
            >>> hk.add_edge(0, 0)
            >>> hk.add_edge(0, 1)
            >>> hk.add_edge(1, 1)
            >>> hk.add_edge(1, 2)
            >>> hk.add_edge(2, 2)
            >>> hk.add_edge(2, 3)
            >>> hk.add_edge(3, 3)
            >>> hk.max_matching()
            4
        """
        matching = 0

        while self.bfs():
            for u in range(self.n):
                if self.pair_u[u] is None:
                    if self.dfs(u):
                        matching += 1

        return matching

    def get_matching(self) -> Dict[int, int]:
        """
        Get the actual matching pairs {u: v}.
        """
        return {u: v for u, v in enumerate(self.pair_u) if v is not None}


def hopcroft_karp(graph: Dict[int, List[int]], n_left: int, n_right: int) -> int:
    """
    Convenience function for Hopcroft-Karp algorithm.

    Args:
        graph: Adjacency list for left partition
        n_left: Size of left partition
        n_right: Size of right partition

    Returns:
        Maximum matching size
    """
    hk = HopcroftKarp(n_left, n_right)
    for u, neighbors in graph.items():
        for v in neighbors:
            hk.add_edge(u, v)
    return hk.max_matching()


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Benchmark vs naive augmenting path
    import time
    import random

    def benchmark():
        n = 500
        m = 500
        edges = 5000

        hk = HopcroftKarp(n, m)
        for _ in range(edges):
            hk.add_edge(random.randint(0, n - 1), random.randint(0, m - 1))

        start = time.perf_counter()
        result = hk.max_matching()
        elapsed = time.perf_counter() - start
        print(
            f"Hopcroft-Karp: {n}x{m}, {edges} edges, matching={result}, time={elapsed:.3f}s"
        )

    benchmark()
