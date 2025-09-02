from itertools import permutations


def tsp_brute_force(graph: list[list[int]]) -> int:
    """
    Solves TSP using brute-force permutations.

    Args:
        graph: 2D list representing distances between cities.

    Returns:
        The minimal total travel distance visiting all cities exactly once,
        and then returning to the start.

    Example:
        >>> tsp_brute_force([[0, 29, 20], [29, 0, 15], [20, 15, 0]])
        64
    """
    n = len(graph)
    # Apart from other cities aside from City 0, City 0 serves as the starting point.
    nodes = list(range(1, n))
    min_path = float("inf")

    # Enumerate all the permutations from city 1 to city n-1.
    for perm in permutations(nodes):
        # Construct a complete path:
        # Starting from point 0, visit in the order of arrangement,
        # and then return to point 0.
        path = [0, *perm, 0]

        # Calculate the total distance of the path.
        # Update the shortest path.
        total_cost = sum(graph[path[i]][path[i + 1]] for i in range(n))
        min_path = min(min_path, total_cost)

    return int(min_path)


def tsp_dp(graph: list[list[int]]) -> int:
    """
    Solves the Traveling Salesman Problem using Held-Karp dynamic programming.

    Args:
        graph: A 2D list representing distances between cities (n x n matrix).

    Returns:
        The minimum cost to visit all cities exactly once and return to the origin.

    Example:
        >>> tsp_dp([[0, 29, 20], [29, 0, 15], [20, 15, 0]])
        64
    """
    n = len(graph)
    # Create a dynamic programming table of size (2^n) x n.
    # Noting: 1 << n  = 2^n
    # dp[mask][i] represents the shortest path starting from city 0,
    # passing through the cities in the mask, and ultimately ending at city i.
    dp = [[float("inf")] * n for _ in range(1 << n)]
    # Initial state: only city 0 is visited, and the path length is 0.
    dp[1][0] = 0

    for mask in range(1 << n):
        # The mask indicates which cities have been visited.
        for u in range(n):
            if not (mask & (1 << u)):
                # If the city u is not included in the mask, skip it.
                continue

            for v in range(n):
                # City v has not been accessed and is different from city u.
                if mask & (1 << v) or u == v:
                    continue

                # New State: Transition to city v
                # State Transition: From city u to city v, updating the shortest path.
                next_mask = mask | (1 << v)
                dp[next_mask][v] = min(dp[next_mask][v], dp[mask][u] + graph[u][v])

    # After completing visits to all cities,
    # return to city 0 and obtain the minimum value.
    return int(min(dp[(1 << n) - 1][i] + graph[i][0] for i in range(1, n)))


def tsp_greedy(graph: list[list[int]]) -> int:
    """
    Solves TSP approximately using the nearest neighbor heuristic.
    Warming: This algorithm is not guaranteed to find the optimal solution!
             But it is fast and applicable to any input size.

    Args:
        graph: 2D list representing distances between cities.

    Returns:
        The total distance of the approximated TSP route.

    Example:
        >>> tsp_greedy([[0, 29, 20], [29, 0, 15], [20, 15, 0]])
        64
    """
    n = len(graph)
    visited = [False] * n  # Mark whether each city has been visited.
    path = [0]
    total_cost = 0
    visited[0] = True  # Start from city 0.
    current = 0  # Current city.

    for _ in range(n - 1):
        # Find the nearest city to the current location that has not been visited.
        next_city = min(
            (
                (city, cost)
                for city, cost in enumerate(graph[current])
                if not visited[city] and city != current
            ),
            key=lambda cost: cost[1],
            default=(None, float("inf")),
        )[0]

        # If no such city exists, break the loop.
        if next_city is None:
            break

        # Update the total cost and the current city.
        # Mark the city as visited.
        # Append the city to the path.
        total_cost += graph[current][next_city]
        visited[next_city] = True
        current = next_city
        path.append(current)

    # Back to start
    total_cost += graph[current][0]
    path.append(0)

    return int(total_cost)


def test_tsp_example() -> None:
    graph = [[0, 29, 20], [29, 0, 15], [20, 15, 0]]

    result = tsp_brute_force(graph)
    if result != 64:
        raise Exception("tsp_brute_force Incorrect result")
    else:
        print("Test passed")

    result = tsp_dp(graph)
    if result != 64:
        raise Exception("tsp_dp Incorrect result")
    else:
        print("Test passed")

    result = tsp_greedy(graph)
    if result != 64:
        if result < 0:
            raise Exception("tsp_greedy Incorrect result")
        else:
            print("tsp_greedy gets an approximate result.")
    else:
        print("Test passed")


if __name__ == "__main__":
    test_tsp_example()
