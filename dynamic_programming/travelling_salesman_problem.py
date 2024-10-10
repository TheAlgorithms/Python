#!/usr/bin/env python3


def tsp(distances: list[list[int]]) -> int:
    """
        Solves the Travelling Salesman Problem (TSP)
        using dynamic programming and bitmasking.

        Args:
            distances: 2D list where distances[i][j]
            is the distance between city i and city j.

        Returns:
            Minimum cost to complete the tour visiting all cities.

        Raises:
            ValueError: If any distance is negative.

    >>> tsp([[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]])
        80
    >>> tsp([[0, 29, 20, 21], [29, 0, 15, 17], [20, 15, 0, 28], [21, 17, 28, 0]])
        69
    >>> tsp([[0, 10, -15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]])
    # doctest: +ELLIPSIS
        Traceback (most recent call last):
            ...
        ValueError: Distance cannot be negative
    """
    n = len(distances)
    if any(distances[i][j] < 0 for i in range(n) for j in range(n)):
        raise ValueError("Distance cannot be negative")

    # Memoization table
    memo = [[-1] * (1 << n) for _ in range(n)]
    visited_all = (1 << n) - 1  # All cities visited mask

    def visit(city: int, mask: int) -> int:
        """Recursively calculates the minimum cost to visit all cities."""
        if mask == visited_all:
            return distances[city][0]  # Return to the starting city
        if memo[city][mask] != -1:  # Return cached result if exists
            return memo[city][mask]

        min_cost = float("inf")  # Use infinity for initial comparison
        for next_city in range(n):
            if not (mask & (1 << next_city)):  # If unvisited
                new_cost = distances[city][next_city] + visit(
                    next_city, mask | (1 << next_city)
                )
                min_cost = min(min_cost, new_cost)
        memo[city][mask] = min_cost  # Store result in the memoization table
        return min_cost

    return visit(0, 1)  # Start from city 0 with only city 0 visited


if __name__ == "__main__":
    import doctest

    doctest.testmod()