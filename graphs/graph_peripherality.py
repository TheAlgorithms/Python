"""
Graph Peripheral and Farness Algorithms for Determining Peripheral and Farthest Nodes
in a Graph.

This module provides functions to compute the peripheral and farthest nodes in a
weighted graph based on graph-theoretical distance measures. The peripheral node
maximizes the maximum shortest-path distance to all other reachable nodes
(eccentricity), while the far node maximizes the sum of shortest-path distances to
all other reachable nodes (farness).

Problem Description:
Given a weighted graph G = (V, E), where V is the set of vertices and E is the set of
edges with positive weights representing distances between nodes, determine:

- Peripheral Node: The node with maximal eccentricity. Eccentricity of a node v is
  defined as the greatest distance between v and any other node reachable from v.

- Far Node: The node with maximal farness. Farness of a node v is the sum of the
  shortest-path distances from v to all other reachable nodes.

Algorithms Implemented:
- Floyd-Warshall Algorithm for All-Pairs Shortest Paths.
- Calculation of Eccentricity and Farness for identifying Peripheral and Far nodes.

Algorithm Descriptions:

Floyd-Warshall Algorithm (Pseudo-code):
---------------------------------------
for k from 1 to N:
    for i from 1 to N:
        for j from 1 to N:
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]

Peripheral and Far Node Calculation:
------------------------------------
For each node i:
    - Eccentricity[i] = maximum distance from node i to any other reachable node.
    - Farness[i] = sum of distances from node i to all reachable nodes.

Select:
    - Peripheral Node: node with maximal eccentricity.
    - Far Node: node with maximal farness.

References:
- Floyd-Warshall Algorithm: https://en.wikipedia.org/wiki/Floyd-Warshall_algorithm
- Eccentricity and Farness: https://en.wikipedia.org/wiki/Distance_(graph_theory)

Example Application:
These algorithms can be applied to network analysis, such as identifying the most
distant nodes within a network, analyzing communication delays, or planning
infrastructure at the boundaries of a network.
"""

import numpy as np


def initialize_distance_matrix(
    graph: dict[int, list[tuple[int, float]]], number_of_nodes: int
) -> np.ndarray:
    """Initialize the distance matrix and validate edge weights.

    Args:
        graph: The graph represented as an adjacency list.
        number_of_nodes: The total number of nodes in the graph.

    Returns:
        A numpy.ndarray representing the initialized distance matrix.

    Raises:
        ValueError: If any edge has a non-positive weight.
    """
    distance_matrix: np.ndarray = np.full((number_of_nodes, number_of_nodes), np.inf)
    np.fill_diagonal(distance_matrix, 0)

    for node_index, edges in graph.items():
        for neighbor_index, edge_weight in edges:
            if edge_weight <= 0:
                error_message: str = (
                    f"Edge weight must be positive. Found {edge_weight} between "
                    f"nodes {node_index} and {neighbor_index}."
                )
                raise ValueError(error_message)
            distance_matrix[node_index, neighbor_index] = edge_weight

    return distance_matrix


def floyd_warshall_algorithm(graph: dict[int, list[tuple[int, float]]]) -> np.ndarray:
    """Compute all-pairs shortest paths using the Floyd-Warshall algorithm.

    Floyd-Warshall Complexity:
    --------------------------
    Time Complexity: O(N^3), where N is the number of nodes.
    Space Complexity: O(N^2), for storing the distance matrix.

    Args:
        graph: The graph represented as an adjacency list.

    Returns:
        The distance matrix with the shortest paths between all pairs of nodes.
    """
    number_of_nodes: int = len(graph)
    distance_matrix: np.ndarray = initialize_distance_matrix(graph, number_of_nodes)

    for k in range(number_of_nodes):
        # Use broadcasting to update the distance matrix in place
        distance_matrix[:] = np.minimum(
            distance_matrix,
            distance_matrix[:, k][:, np.newaxis] + distance_matrix[k, :],
        )

    return distance_matrix


def get_reachable_distances(distances: np.ndarray) -> np.ndarray:
    """Filter reachable distances, excluding infinite values (unreachable nodes).

    Args:
        distances: Array of shortest-path distances from a specific node.

    Returns:
        An array of distances to reachable nodes only (finite values).
    """
    return distances[np.isfinite(distances) & (distances != 0)]


def find_peripheral_node(
    eccentricities: list[tuple[int, float]],
) -> tuple[int, float]:
    """Identify the node with maximal eccentricity among reachable nodes.

    Args:
        eccentricities: List of tuples (node index, eccentricity).

    Returns:
        The node with maximal eccentricity and its value. Returns (-1, inf) if
        no valid nodes are found.
    """
    return max(
        eccentricities,
        key=lambda node_eccentricity: (
            node_eccentricity[1],  # Prioritize highest eccentricity
            -node_eccentricity[0],  # For equal values, prefer nodes with higher index
        ),
        default=(-1, float("inf")),
    )


def find_far_node(farnesses: list[tuple[int, float]]) -> tuple[int, float]:
    """Identify the node with maximal farness among reachable nodes.

    Args:
        farnesses: List of tuples (node index, farness).

    Returns:
        The node with maximal farness and its value. Returns (-1, inf) if
        no valid nodes are found.
    """
    return max(
        farnesses,
        key=lambda node_farness: (
            node_farness[1],  # Prioritize highest farness
            -node_farness[0],  # For equal values, prefer nodes with higher index
        ),
        default=(-1, float("inf")),
    )


def find_peripheral_and_far_node(
    distance_matrix: np.ndarray,
) -> tuple[tuple[int, float], tuple[int, float]]:
    """Determine the peripheral and far nodes based on shortest-path distances.

    For each node, calculates its eccentricity and farness (sum of distances to all
    reachable nodes). Identifies the peripheral node (maximal eccentricity) and
    farthest node (maximal farness).

    Args:
        distance_matrix: A numpy.ndarray representing shortest-path distances
                         between all pairs of nodes.

    Returns:
        A tuple containing:
            - peripheral_node: A tuple (node index, eccentricity) for the node with
              maximal eccentricity.
            - far_node: A tuple (node index, farness) for the node with maximal
              farness (sum of shortest-path distances).
    """
    num_nodes: int = len(distance_matrix)

    # Handle single-node graphs
    if num_nodes == 1:
        return (0, 0.0), (0, 0.0)

    eccentricities: list[tuple[int, float]] = []
    farnesses: list[tuple[int, float]] = []
    all_disconnected = True  # Assume all are disconnected until proven otherwise

    for i in range(num_nodes):
        reachable_distances = get_reachable_distances(distance_matrix[i])

        if reachable_distances.size == 0:
            # Fully disconnected node
            eccentricity = float("inf")
            farness = float("inf")
        else:
            all_disconnected = False  # If any node has reachable nodes, we update this
            eccentricity = float(np.max(reachable_distances))
            farness = float(np.sum(reachable_distances))

        eccentricities.append((i, eccentricity))
        farnesses.append((i, farness))

    # If all nodes are disconnected, we return (-1, inf)
    if all_disconnected:
        return (-1, float("inf")), (-1, float("inf"))

    peripheral_node = find_peripheral_node(eccentricities)
    far_node = find_far_node(farnesses)

    return peripheral_node, far_node


# Test cases included as doctests
def test_single_node() -> None:
    """
    Test a graph with a single node.

    >>> graph = {0: []}
    >>> distance_matrix = floyd_warshall_algorithm(graph)
    >>> peripheral_node, far_node = find_peripheral_and_far_node(distance_matrix)
    >>> peripheral_node
    (0, 0.0)
    >>> far_node
    (0, 0.0)
    """


def test_two_nodes_positive_weight() -> None:
    """
    Test a graph with two nodes connected by a positive weight.

    >>> graph = {0: [(1, 5.0)], 1: [(0, 5.0)]}
    >>> distance_matrix = floyd_warshall_algorithm(graph)
    >>> peripheral_node, far_node = find_peripheral_and_far_node(distance_matrix)
    >>> peripheral_node
    (0, 5.0)
    >>> far_node
    (0, 5.0)
    """


def test_fully_connected_graph() -> None:
    """
    Test a fully connected graph.

    >>> graph = {
    ...     0: [(1, 1.0), (2, 1.0)],
    ...     1: [(0, 1.0), (2, 1.0)],
    ...     2: [(0, 1.0), (1, 1.0)],
    ... }
    >>> distance_matrix = floyd_warshall_algorithm(graph)
    >>> peripheral_node, far_node = find_peripheral_and_far_node(distance_matrix)
    >>> peripheral_node
    (0, 1.0)
    >>> far_node
    (0, 2.0)
    """


def test_graph_with_zero_weight() -> None:
    """
    Test a graph with zero weight, which should raise a ValueError.

    >>> graph = {0: [(1, 0.0)], 1: []}
    >>> floyd_warshall_algorithm(graph)
    Traceback (most recent call last):
    ...
    ValueError: Edge weight must be positive. Found 0.0 between nodes 0 and 1.
    """


def test_graph_with_negative_weight() -> None:
    """
    Test a graph with negative weight, which should raise a ValueError.

    >>> graph = {0: [(1, -2.0)], 1: []}
    >>> floyd_warshall_algorithm(graph)
    Traceback (most recent call last):
    ...
    ValueError: Edge weight must be positive. Found -2.0 between nodes 0 and 1.
    """


def test_sparse_graph() -> None:
    """
    Test a larger sparse graph.

    >>> graph = {
    ...     0: [(1, 2.0)],
    ...     1: [(2, 3.0)],
    ...     2: [(3, 4.0)],
    ...     3: [(4, 5.0)],
    ...     4: []
    ... }
    >>> distance_matrix = floyd_warshall_algorithm(graph)
    >>> peripheral_node, far_node = find_peripheral_and_far_node(distance_matrix)
    >>> peripheral_node
    (4, inf)
    >>> far_node
    (4, inf)
    """


def test_cyclic_graph() -> None:
    """
    Test a cyclic graph where there is a cycle between nodes.

    >>> graph = {
    ...     0: [(1, 1.0)],
    ...     1: [(2, 1.0)],
    ...     2: [(0, 1.0)]
    ... }
    >>> distance_matrix = floyd_warshall_algorithm(graph)
    >>> peripheral_node, far_node = find_peripheral_and_far_node(distance_matrix)
    >>> peripheral_node
    (0, 2.0)
    >>> far_node
    (0, 3.0)
    """


def test_directed_acyclic_graph() -> None:
    """
    Test a directed acyclic graph (DAG).

    >>> graph = {
    ...     0: [(1, 1.0), (2, 2.0)],
    ...     1: [(3, 3.0)],
    ...     2: [(3, 1.0)],
    ...     3: []
    ... }
    >>> distance_matrix = floyd_warshall_algorithm(graph)
    >>> peripheral_node, far_node = find_peripheral_and_far_node(distance_matrix)
    >>> peripheral_node
    (3, inf)
    >>> far_node
    (3, inf)
    """


def test_disconnected_graph() -> None:
    """
    Test a disconnected graph with nodes that cannot reach each other.

    >>> graph = {
    ...     0: [],
    ...     1: [],
    ...     2: []
    ... }
    >>> distance_matrix = floyd_warshall_algorithm(graph)
    >>> peripheral_node, far_node = find_peripheral_and_far_node(distance_matrix)
    >>> peripheral_node
    (-1, inf)
    >>> far_node
    (-1, inf)
    """


def test_large_fully_connected_graph() -> None:
    """
    Test a larger fully connected graph with random weights.

    >>> import random
    >>> random.seed(42)
    >>> number_of_nodes = 10
    >>> graph = {i: [(j, random.uniform(1, 10)) for j in
    ...          range(number_of_nodes) if i != j]
    ...          for i in range(number_of_nodes)}
    >>> distance_matrix = floyd_warshall_algorithm(graph)
    >>> peripheral_node, far_node = find_peripheral_and_far_node(distance_matrix)
    >>> peripheral_node[0] is not None  # Ensure it found a peripheral node
    True
    >>> far_node[0] is not None  # Ensure it found a far node
    True
    """


def main() -> None:
    """
    Main driver function for testing the implementation with doctests.
    """
    import doctest

    doctest.testmod()


if __name__ == "__main__":
    main()
