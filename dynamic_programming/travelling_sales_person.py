"""
Dynamic Programming: Travelling Salesman Problem (TSP)
-----------------------------------------------------
Solves the classic TSP using the Held–Karp dynamic programming approach.

Time Complexity: O(n^2 * 2^n)
Space Complexity: O(n * 2^n)

Example:
    >>> cost = [
    ...     [0, 10, 15, 20],
    ...     [10, 0, 35, 25],
    ...     [15, 35, 0, 30],
    ...     [20, 25, 30, 0]
    ... ]
    >>> travelling_salesman(cost)
    80
"""

from functools import lru_cache


def travelling_salesman(cost_matrix: list[list[int]]) -> int:
    """
    Returns the minimum travel cost for visiting all cities and returning
    to the starting city (0-indexed), using the Held–Karp DP approach.

    Args:
        cost_matrix (list[list[int]]): A square matrix where cost_matrix[i][j]
            represents the cost of traveling from city i to city j.

    Returns:
        int: The minimum total cost of the tour.
    """
    n = len(cost_matrix)
    all_visited = (1 << n) - 1  # bitmask with all cities visited

    @lru_cache(maxsize=None)
    def dp(mask: int, pos: int) -> int:
        # Base case: all cities visited, return cost to go back to start
        if mask == all_visited:
            return cost_matrix[pos][0]

        ans = float("inf")
        for city in range(n):
            # If city not yet visited
            if not (mask & (1 << city)):
                new_cost = cost_matrix[pos][city] + dp(mask | (1 << city), city)
                ans = min(ans, new_cost)
        return ans

    # Start from city 0 with only it visited
    return dp(1, 0)


if __name__ == "__main__":
    # Example test case
    cost = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0],
    ]

    print("Minimum tour cost:", travelling_salesman(cost))
