"""Travelling Salesman Problem (TSP)"""

import itertools
import math


class InvalidGraphError(ValueError):
    """Custom error for invalid graph inputs."""


def euclidean_distance(point1: list[float], point2: list[float]) -> float:
    """
    Calculate the Euclidean distance between two points in 2D space.

    :param point1: Coordinates of the first point [x, y]
    :param point2: Coordinates of the second point [x, y]
    :return: The Euclidean distance between the two points

    >>> euclidean_distance([0, 0], [3, 4])
    5.0
    >>> euclidean_distance([1, 1], [1, 1])
    0.0
    >>> euclidean_distance([1, 1], ['a', 1])
    Traceback (most recent call last):
    ...
    ValueError: Invalid input: Points must be numerical coordinates
    """
    try:
        return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)
    except TypeError:
        raise ValueError("Invalid input: Points must be numerical coordinates")


def validate_graph(graph_points: dict[str, list[float]]) -> None:
    """
    Validate the input graph to ensure it has valid nodes and coordinates.

    :param graph_points: A dictionary where the keys are node names,
                         and values are 2D coordinates as [x, y]
    :raises InvalidGraphError: If the graph points are not valid

    >>> validate_graph({"A": [10, 20], "B": [30, 21], "C": [15, 35]})  # Valid graph
    >>> validate_graph({"A": [10, 20], "B": [30, "invalid"], "C": [15, 35]})
    Traceback (most recent call last):
    ...
    InvalidGraphError: Each node must have a valid 2D coordinate [x, y]

    >>> validate_graph([10, 20])  # Invalid input type
    Traceback (most recent call last):
    ...
    InvalidGraphError: Graph must be a dictionary with node names and coordinates

    >>> validate_graph({"A": [10, 20], "B": [30, 21], "C": [15]})  # Missing coordinate
    Traceback (most recent call last):
    ...
    InvalidGraphError: Each node must have a valid 2D coordinate [x, y]
    """
    if not isinstance(graph_points, dict):
        raise InvalidGraphError(
            "Graph must be a dictionary with node names and coordinates"
        )

    for node, coordinates in graph_points.items():
        if (
            not isinstance(node, str)
            or not isinstance(coordinates, list)
            or len(coordinates) != 2
            or not all(isinstance(c, (int, float)) for c in coordinates)
        ):
            raise InvalidGraphError("Each node must have a valid 2D coordinate [x, y]")


# TSP in Brute Force Approach
def travelling_salesman_brute_force(
    graph_points: dict[str, list[float]],
) -> tuple[list[str], float]:
    """
    Solve the Travelling Salesman Problem using brute force.

    :param graph_points: A dictionary of nodes and their coordinates {node: [x, y]}
    :return: The shortest path and its total distance

    >>> graph = {"A": [10, 20], "B": [30, 21], "C": [15, 35]}
    >>> travelling_salesman_brute_force(graph)
    (['A', 'C', 'B', 'A'], 56.35465722402587)
    """
    validate_graph(graph_points)

    nodes = list(graph_points.keys())  # Extracting the node names (keys)

    # There shoukd be atleast 2 nodes for a valid TSP
    if len(nodes) < 2:
        raise InvalidGraphError("Graph must have at least two nodes")

    min_path = []  # List that stores shortest path
    min_distance = float("inf")  # Initialize minimum distance to infinity

    start_node = nodes[0]
    other_nodes = nodes[1:]

    # Iterating over all permutations of the other nodes
    for perm in itertools.permutations(other_nodes):
        path = [start_node, *perm, start_node]

        # Calculating the total distance
        total_distance = sum(
            euclidean_distance(graph_points[path[i]], graph_points[path[i + 1]])
            for i in range(len(path) - 1)
        )

        # Update minimum distance if shorter path found
        if total_distance < min_distance:
            min_distance = total_distance
            min_path = path

    return min_path, min_distance


# TSP in Dynamic Programming approach
def travelling_salesman_dynamic_programming(
    graph_points: dict[str, list[float]],
) -> tuple[list[str], float]:
    """
    Solve the Travelling Salesman Problem using dynamic programming.

    :param graph_points: A dictionary of nodes and their coordinates {node: [x, y]}
    :return: The shortest path and its total distance

    >>> graph = {"A": [10, 20], "B": [30, 21], "C": [15, 35]}
    >>> travelling_salesman_dynamic_programming(graph)
    (['A', 'C', 'B', 'A'], 56.35465722402587)
    """
    validate_graph(graph_points)

    n = len(graph_points)  # Extracting the node names (keys)

    # There shoukd be atleast 2 nodes for a valid TSP
    if n < 2:
        raise InvalidGraphError("Graph must have at least two nodes")

    nodes = list(graph_points.keys())  # Extracting the node names (keys)

    # Initialize distance matrix with float values
    dist = [
        [
            euclidean_distance(graph_points[nodes[i]], graph_points[nodes[j]])
            for j in range(n)
        ]
        for i in range(n)
    ]

    # Initialize a dynamic programming table with infinity
    dp = [[float("inf")] * n for _ in range(1 << n)]
    dp[1][0] = 0  # Only visited node is the starting point at node 0

    # Iterate through all masks of visited nodes
    for mask in range(1 << n):
        for u in range(n):
            # If current node 'u' is visited
            if mask & (1 << u):
                # Traverse nodes 'v' such that u->v
                for v in range(n):
                    if mask & (1 << v) == 0:  # If v is not visited
                        next_mask = mask | (1 << v)  # Upodate mask to include 'v'
                        # Update dynamic programming table with minimum distance
                        dp[next_mask][v] = min(
                            dp[next_mask][v], dp[mask][u] + dist[u][v]
                        )

    final_mask = (1 << n) - 1
    min_cost = float("inf")
    end_node = -1  # Track the last node in the optimal path

    for u in range(1, n):
        if min_cost > dp[final_mask][u] + dist[u][0]:
            min_cost = dp[final_mask][u] + dist[u][0]
            end_node = u

    path = []
    mask = final_mask
    while end_node != 0:
        path.append(nodes[end_node])
        for u in range(n):
            # If current state corresponds to optimal state before visiting end node
            if (
                mask & (1 << u)
                and dp[mask][end_node]
                == dp[mask ^ (1 << end_node)][u] + dist[u][end_node]
            ):
                mask ^= 1 << end_node  # Update mask to remove end node
                end_node = u  # Set the previous node as end node
                break

    path.append(nodes[0])  # Bottom-up Order
    path.reverse()  # Top-Down Order
    path.append(nodes[0])

    return path, min_cost


# Demo Graph
#        C (15, 35)
#        |
#        |
#        |
# F (5, 15) --- A (10, 20)
#        |         |
#        |         |
#        |         |
#        |         |
# E (25, 5) --- B (30, 21)
#        |
#        |
#        |
#       D (40, 10)
#        |
#        |
#        |
#       G (50, 25)


if __name__ == "__main__":
    demo_graph = {
        "A": [10.0, 20.0],
        "B": [30.0, 21.0],
        "C": [15.0, 35.0],
        "D": [40.0, 10.0],
        "E": [25.0, 5.0],
        "F": [5.0, 15.0],
        "G": [50.0, 25.0],
    }

    # Brute force
    brute_force_result = travelling_salesman_brute_force(demo_graph)
    print(f"Brute force result: {brute_force_result}")

    # Dynamic programming
    dp_result = travelling_salesman_dynamic_programming(demo_graph)
    print(f"Dynamic programming result: {dp_result}")
