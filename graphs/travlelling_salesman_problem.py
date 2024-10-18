"""
title : Travelling Sales man Problem 
references : https://en.wikipedia.org/wiki/Travelling_salesman_problem
author : SunayBhoyar
"""
import itertools
import math

demo_graph_points = {
    "A": [10, 20],
    "B": [30, 21],
    "C": [15, 35],
    "D": [40, 10],
    "E": [25, 5],
    "F": [5, 15],
    "G": [50, 25]
}

# Euclidean distance - shortest distance between 2 points 
def distance(point1, point2):
    """
    Calculate the Euclidean distance between two points.
    @input: point1, point2 (coordinates of two points as lists [x, y])
    @return: Euclidean distance between point1 and point2
    @example:
    >>> distance([0, 0], [3, 4])
    5.0
    """
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

"""
Brute force 
Time Complexity - O(n!×n)
Space Complexity - O(n)
"""
def travelling_sales_man_problem_brute_force(graph_points):
    """
    Solve the Travelling Salesman Problem using brute force (permutations).
    @input: graph_points (dictionary with node names as keys and coordinates as values)
    @return: shortest path, total distance (list of nodes representing the shortest path and the distance of that path)
    @example:
    >>> travelling_sales_man_problem_brute_force({'A': [0, 0], 'B': [0, 1], 'C': [1, 0]})
    (['A', 'B', 'C', 'A'], 3.414)
    """
    nodes = list(graph_points.keys())
    
    min_path = None
    min_distance = float('inf')
    
    # Considering the first Node as the start position 
    start_node = nodes[0]
    other_nodes = nodes[1:]
    
    for perm in itertools.permutations(other_nodes):
        path = [start_node] + list(perm) + [start_node]
        total_distance = 0
        for i in range(len(path) - 1):
            total_distance += distance(graph_points[path[i]], graph_points[path[i+1]])

        if total_distance < min_distance:
            min_distance = total_distance
            min_path = path
    
    return min_path, min_distance

"""
dynamic_programming 
Time Complexity - O(n^2×2^n)
Space Complexity - O(n×2^n)
"""
def travelling_sales_man_problem_dp(graph_points):
    """
    Solve the Travelling Salesman Problem using dynamic programming.
    @input: graph_points (dictionary with node names as keys and coordinates as values)
    @return: shortest path, total distance (list of nodes representing the shortest path and the distance of that path)
    @example:
    >>> travelling_sales_man_problem_dp({'A': [0, 0], 'B': [0, 1], 'C': [1, 0]})
    (['A', 'B', 'C', 'A'], 3.414)
    """
    n = len(graph_points)
    nodes = list(graph_points.keys())
    
    # Precompute distances between every pair of nodes
    dist = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dist[i][j] = distance(graph_points[nodes[i]], graph_points[nodes[j]])
    
    # dp[mask][i] represents the minimum distance to visit all nodes in the 'mask' set, ending at node i
    dp = [[float('inf')] * n for _ in range(1 << n)]
    dp[1][0] = 0  # Start at node 0
    
    # Iterate over all subsets of nodes (represented by mask)
    for mask in range(1 << n):
        for u in range(n):
            if mask & (1 << u): 
                for v in range(n):
                    if mask & (1 << v) == 0:  
                        next_mask = mask | (1 << v)
                        dp[next_mask][v] = min(dp[next_mask][v], dp[mask][u] + dist[u][v])

    # Reconstruct the path and find the minimum distance to return to the start
    final_mask = (1 << n) - 1
    min_cost = float('inf')
    end_node = -1

    # Find the minimum distance from any node back to the starting node
    for u in range(1, n):
        if min_cost > dp[final_mask][u] + dist[u][0]:
            min_cost = dp[final_mask][u] + dist[u][0]
            end_node = u
    
    # Reconstruct the path using the dp table
    path = []
    mask = final_mask
    while end_node != 0:
        path.append(nodes[end_node])
        for u in range(n):
            if mask & (1 << u) and dp[mask][end_node] == dp[mask ^ (1 << end_node)][u] + dist[u][end_node]:
                mask ^= (1 << end_node) 
                end_node = u
                break

    path.append(nodes[0])  
    path.reverse()

    return path, min_cost


if __name__ == "__main__":
    print(f"Travelling salesman problem solved using Brute Force:")
    path, distance_travelled = travelling_sales_man_problem_brute_force(demo_graph_points)
    print(f"Shortest path: {path}")
    print(f"Total distance: {distance_travelled:.2f}")

    print(f"\nTravelling salesman problem solved using Dynamic Programming:")
    path, distance_travelled = travelling_sales_man_problem_dp(demo_graph_points)
    print(f"Shortest path: {path}")
    print(f"Total distance: {distance_travelled:.2f}")
