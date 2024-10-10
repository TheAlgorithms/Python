"""
Given a list of cities and the distances between every pair of cities, the Travelling Salesman Problem (TSP) is to
find the shortest possible route that visits every city exactly once and returns to the starting city.

This problem can be solved using the concept of "DYNAMIC PROGRAMMING".

We use a bitmask to represent which cities have been visited and calculate the minimum cost to complete the tour.

Example - distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
Output: 80
"""

from functools import lru_cache


def tsp(distances: list[list[int]]) -> int:
    """
    The tsp function solves the Travelling Salesman Problem (TSP) using dynamic programming and bitmasking.
    It calculates the minimum cost to visit all cities and return to the starting city.

    >>> tsp([[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]])
    80
    >>> tsp([[0, 29, 20, 21], [29, 0, 15, 17], [20, 15, 0, 28], [21, 17, 28, 0]])
    69
    >>> tsp([[0, 10, -15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]])
    Traceback (most recent call last):
        ...
    ValueError: Distance cannot be negative
    """
    n = len(distances)
    if any(distances[i][j] < 0 for i in range(n) for j in range(n)):
        raise ValueError("Distance cannot be negative")

    VISITED_ALL = (1 << n) - 1

    @lru_cache(None)
    def visit(city: int, mask: int) -> int:
        """
        Recursively calculate the minimum cost of visiting all cities, starting at 'city' with visited cities encoded in 'mask'.
        """
        if mask == VISITED_ALL:
            return distances[city][0]  # Return to the starting city

        min_cost = float('inf')
        for next_city in range(n):
            if not mask & (1 << next_city):  # If the next_city is not visited
                new_cost = distances[city][next_city] + visit(next_city, mask | (1 << next_city))
                min_cost = min(min_cost, new_cost)
        return min_cost

    return visit(0, 1)  # Start at city 0 with only city 0 visited


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(f"{tsp([[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]) = }")
    print(f"{tsp([[0, 29, 20, 21], [29, 0, 15, 17], [20, 15, 0, 28], [21, 17, 28, 0]]) = }")
