"""
Maximum Independent Set in Bipartite Graphs

Using Konig's theorem: |Maximum Independent Set| = |V| - |Maximum Matching|
Also related to minimum vertex cover.

Time Complexity: O(E√V) using Hopcroft-Karp for matching
Space Complexity: O(V + E)
"""

from collections import deque


class MaxBipartiteIndependentSet:
    """
    Find maximum independent set in bipartite graphs.
    """

    def __init__(self, n_left: int, n_right: int):
        self.n_left = n_left
        self.n_right = n_right
        self.n = n_left + n_right
        self.adj: list[list[int]] = [[] for _ in range(n_left)]

    def add_edge(self, u: int, v: int) -> None:
        """Add edge from left u to right v."""
        self.adj[u].append(v)

    def solve(self) -> tuple[set[int], set[int]]:
        """
        Find maximum independent set.

        Returns:
            Tuple of (left_independent_set, right_independent_set)

        """
        # Find maximum matching using Hopcroft-Karp
        pair_u, pair_v = self._hopcroft_karp()

        # Find minimum vertex cover using Konig's theorem
        # Z = vertices reachable from free vertices in U via alternating paths
        z_u, z_v = self._find_z_set(pair_u, pair_v)

        # Minimum vertex cover = (U - Z) union (V intersect Z)
        # Maximum independent set = Z union (V - Z) = complement of min vertex cover
        left_mis = z_u
        right_mis = set(range(self.n_right)) - z_v

        return left_mis, right_mis

    def _hopcroft_karp(self) -> tuple[list[int | None], list[int | None]]:
        """Hopcroft-Karp algorithm for maximum matching."""
        pair_u: list[int | None] = [None] * self.n_left
        pair_v: list[int | None] = [None] * self.n_right
        dist = [0] * self.n_left

        def bfs() -> bool:
            queue = deque()
            for u in range(self.n_left):
                if pair_u[u] is None:
                    dist[u] = 0
                    queue.append(u)
                else:
                    dist[u] = float("inf")  # type: ignore[assignment][assignment]

            found = False
            while queue:
                u = queue.popleft()
                for v in self.adj[u]:
                    pu = pair_v[v]
                    if pu is not None and dist[pu] == float("inf"):  # type: ignore[operator]
                        dist[pu] = dist[u] + 1
                        queue.append(pu)
                    elif pu is None:
                        found = True
            return found

        def dfs(u: int) -> bool:
            for v in self.adj[u]:
                pu = pair_v[v]
                if pu is None or (dist[pu] == dist[u] + 1 and dfs(pu)):
                    pair_u[u] = v
                    pair_v[v] = u
                    return True
            dist[u] = float("inf")  # type: ignore[assignment]
            return False

        while bfs():
            for u in range(self.n_left):
                if pair_u[u] is None:
                    dfs(u)

        return pair_u, pair_v

    def _find_z_set(
        self, pair_u: list[int | None], pair_v: list[int | None]
    ) -> tuple[set[int], set[int]]:
        """Find Z set for Konig's theorem (vertices reachable from free U vertices)."""
        z_u: set[int] = set()
        z_v: set[int] = set()

        # BFS from free vertices in U
        queue = deque()
        for u in range(self.n_left):
            if pair_u[u] is None:
                queue.append(("u", u))
                z_u.add(u)

        while queue:
            side, u = queue.popleft()

            if side == "u":
                # From U, follow non-matching edges to V
                for v in self.adj[u]:
                    if v not in z_v and pair_u[u] != v:  # Non-matching edge
                        z_v.add(v)
                        queue.append(("v", v))
            else:
                # From V, follow matching edges to U
                pu = pair_v[u]
                if pu is not None and pu not in z_u:
                    z_u.add(pu)
                    queue.append(("u", pu))

        return z_u, z_v


def max_bipartite_independent_set(
    n_left: int, n_right: int, edges: list[tuple[int, int]]
) -> tuple[set[int], set[int]]:
    """
    Convenience function.

    Args:
        n_left: Size of left partition
        n_right: Size of right partition
        edges: List of (u, v) edges

    Returns:
        (left_independent_set, right_independent_set)
    """
    solver = MaxBipartiteIndependentSet(n_left, n_right)
    for u, v in edges:
        solver.add_edge(u, v)
    return solver.solve()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
