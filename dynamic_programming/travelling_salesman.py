def tsp_dp(distances: list[list[float]]) -> tuple[float, list[int]]:
    """
    Solves Traveling Salesman Problem using dynamic programming.

    >>> distances = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
    >>> cost, path = tsp_dp(distances)
    >>> float(cost)
    80.0
    >>> path[0]
    0

    >>> distances = [[0, 5], [5, 0]]
    >>> cost, path = tsp_dp(distances)
    >>> float(cost)
    10.0
    >>> path
    [0, 1]
    """
    if not distances:
        raise ValueError("Empty distance matrix")

    n = len(distances)
    all_points = (1 << n) - 1
    dp = {}
    parent = {}

    def solve(mask: int, pos: int) -> float:
        """
        Recursive helper function for solving the TSP using dynamic programming.

        :param mask: Bitmask representing visited nodes.
        :param pos: Current position in the tour.
        :return: Minimum cost to complete the tour.
        """
        if mask == all_points:
            return distances[pos][0]

        state = (mask, pos)
        if state in dp:
            return dp[state]

        minimum = float("inf")
        min_next = -1

        for next_city in range(n):
            if mask & (1 << next_city) == 0:
                new_mask = mask | (1 << next_city)
                new_dist = distances[pos][next_city] + solve(new_mask, next_city)

                if new_dist < minimum:
                    minimum = new_dist
                    min_next = next_city

        dp[state] = minimum
        parent[state] = min_next
        return minimum

    optimal_cost = solve(1, 0)

    path = [0]
    mask = 1
    pos = 0

    for _ in range(n - 1):
        next_pos = parent[(mask, pos)]
        path.append(next_pos)
        mask |= 1 << next_pos
        pos = next_pos

    return optimal_cost, path


if __name__ == "__main__":
    import doctest

    doctest.testmod()
