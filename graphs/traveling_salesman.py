"""
Traveling Salesman Problem - Held-Karp Algorithm

Dynamic programming solution for TSP using bitmask DP.
Exact solution, not approximation.

Time Complexity: O(n² * 2ⁿ) - much better than O(n!)
Space Complexity: O(n * 2ⁿ)

Note: Practical only for n <= 20-25
"""

from typing import List, Tuple, Optional
import sys


class TravelingSalesman:
    """
    TSP solver using Held-Karp dynamic programming.
    """

    def __init__(self, n: int):
        self.n = n
        self.dist: List[List[float]] = [[float("inf")] * n for _ in range(n)]

    def add_edge(self, u: int, v: int, w: float) -> None:
        """Add directed edge."""
        self.dist[u][v] = min(self.dist[u][v], w)

    def solve(self, start: int = 0) -> Tuple[float, List[int]]:
        """
        Solve TSP starting from given vertex.

        Returns:
            Tuple of (minimum_cost, optimal_path)

        Example:
            >>> tsp = TravelingSalesman(4)
            >>> tsp.add_edge(0, 1, 10)
            >>> tsp.add_edge(0, 2, 15)
            >>> tsp.add_edge(0, 3, 20)
            >>> tsp.add_edge(1, 0, 10)
            >>> tsp.add_edge(1, 2, 35)
            >>> tsp.add_edge(1, 3, 25)
            >>> tsp.add_edge(2, 0, 15)
            >>> tsp.add_edge(2, 1, 35)
            >>> tsp.add_edge(2, 3, 30)
            >>> tsp.add_edge(3, 0, 20)
            >>> tsp.add_edge(3, 1, 25)
            >>> tsp.add_edge(3, 2, 30)
            >>> cost, path = tsp.solve(0)
            >>> cost
            80.0
        """
        n = self.n
        if n > 20:
            raise ValueError("Held-Karp is impractical for n > 20")

        # dp[mask][i] = min cost to visit vertices in mask, ending at i
        # mask is bitmask of visited vertices (bit j set if vertex j visited)
        dp: List[List[float]] = [[float("inf")] * n for _ in range(1 << n)]
        parent: List[List[Optional[int]]] = [[None] * n for _ in range(1 << n)]

        # Base case: start at start vertex
        dp[1 << start][start] = 0

        # Iterate over all masks
        for mask in range(1 << n):
            for last in range(n):
                if not (mask & (1 << last)):
                    continue  # last not in mask
                if dp[mask][last] == float("inf"):
                    continue

                # Try to extend to next vertex
                for next_v in range(n):
                    if mask & (1 << next_v):
                        continue  # already visited

                    new_mask = mask | (1 << next_v)
                    new_cost = dp[mask][last] + self.dist[last][next_v]

                    if new_cost < dp[new_mask][next_v]:
                        dp[new_mask][next_v] = new_cost
                        parent[new_mask][next_v] = last

        # Find optimal tour: return to start
        full_mask = (1 << n) - 1
        min_cost = float("inf")
        last_vertex = -1

        for last in range(n):
            if last == start:
                continue
            cost = dp[full_mask][last] + self.dist[last][start]
            if cost < min_cost:
                min_cost = cost
                last_vertex = last

        # Reconstruct path
        if last_vertex == -1:
            return float("inf"), []

        path = []
        mask = full_mask
        curr = last_vertex

        while curr is not None:
            path.append(curr)
            next_curr = parent[mask][curr]
            mask ^= 1 << curr
            curr = next_curr

        path.reverse()
        path.append(start)  # Return to start

        return min_cost, path


def held_karp(
    dist_matrix: List[List[float]], start: int = 0
) -> Tuple[float, List[int]]:
    """
    Convenience function for TSP using Held-Karp.

    Args:
        dist_matrix: Distance matrix (n x n)
        start: Starting vertex

    Returns:
        (minimum_cost, optimal_path)
    """
    n = len(dist_matrix)
    tsp = TravelingSalesman(n)
    tsp.dist = [row[:] for row in dist_matrix]
    return tsp.solve(start)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
