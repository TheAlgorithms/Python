"""
The Traveling Salesman Problem (TSP) is a classic optimization problem in computer science and mathematics.
The goal is to find the shortest possible route that visits a given set of cities and returns to the starting city.
This problem is known to be NP-hard, but dynamic programming (DP) can be used to solve smaller instances of the problem efficiently.
Here's a dynamic programming solution for TSP:


##small test case
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
start_city = 0

Output: Shortest Path Length: 80
---------------------------------------------------

##Sparse Graph:

graph = [
    [0, 10, 0, 0],
    [10, 0, 15, 20],
    [0, 15, 0, 25],
    [0, 20, 25, 0]
]
start_city = 0


Output: Shortest Path Length: 55
-------------------------------------------------
## Circular Route:

graph = [
    [0, 10, 15, 20],
    [10, 0, 25, 30],
    [15, 25, 0, 35],
    [20, 30, 35, 0]
]
start_city = 0


Output: Shortest Path Length: 80

"""
import sys


def tsp_dp(graph, start):
    n = len(graph)
    all_vertices = set(range(n))
    memo = {}

    def tsp_helper(mask, current_vertex):
        if mask == all_vertices and current_vertex == start:
            return graph[current_vertex][start]

        if (mask, current_vertex) in memo:
            return memo[(mask, current_vertex)]

        min_cost = sys.maxsize
        for next_vertex in range(n):
            if (mask >> next_vertex) & 1 == 0:
                new_mask = mask | (1 << next_vertex)
                cost = graph[current_vertex][next_vertex] + tsp_helper(
                    new_mask, next_vertex
                )
                min_cost = min(min_cost, cost)

        memo[(mask, current_vertex)] = min_cost
        return min_cost

    return tsp_helper(1 << start, start)


# Example usage:
graph = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
start_city = 0

shortest_path_length = tsp_dp(graph, start_city)
print("Shortest Path Length:", shortest_path_length)

"""""
In this Python code:

- `graph` represents the distance matrix between cities.
- `graph[i][j]` is the distance from city `i` to city `j`.
- `start` is the starting city (usually denoted as city 0).
-  The `tsp_dp` function uses memoization (dynamic programming) to calculate the shortest path length.

Here's how the dynamic programming approach works:

1. Create a memoization table to store subproblem results to avoid redundant calculations.
2. The `tsp_helper` function is a recursive function that takes two arguments: the mask representing visited cities and the current city.
3. The function iterates through all unvisited cities, calculates the cost of going to each unvisited city from the current city, and recursively finds the minimum cost path.
4. The memoization table is used to store and retrieve previously computed results to avoid recalculating them.
5. Finally, the function is called with the starting city and returns the shortest path length.

Keep in mind that the TSP is an NP-hard problem,
and this dynamic programming solution is efficient for small instances with a limited number of cities.
For larger instances, more efficient algorithms like branch and bound or heuristics like the nearest neighbor algorithm
or genetic algorithms are typically used.
""" ""
