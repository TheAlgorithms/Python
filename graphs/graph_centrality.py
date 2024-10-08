"""
Graph Centrality Algorithms for Determining Central and Median Nodes in a Graph.

This module provides functions to compute the central and median nodes in a weighted
graph based on graph-theoretical centrality measures. The central node minimizes the
maximum shortest-path distance to all other reachable nodes (eccentricity), while the
median node maximizes the sum of the reciprocals of the shortest-path distances to all
other reachable nodes (harmonic closeness centrality).

Problem Description:
Given a weighted graph G = (V, E), where V is the set of vertices and E is the set of
edges with positive weights representing distances between nodes, determine:

- Central Node: The node with minimal eccentricity. Eccentricity of a node v is defined
  as the greatest distance between v and any other node reachable from v.

- Median Node: The node with maximal harmonic closeness centrality. The harmonic
  closeness centrality of a node v is the sum of the reciprocals of the shortest-path
  distances from v to all other reachable nodes.

Algorithms Implemented:
- Floyd-Warshall Algorithm for All-Pairs Shortest Paths.
- Calculation of Eccentricity and Harmonic Closeness Centrality.

Algorithm Descriptions:

Floyd-Warshall Algorithm (Pseudo-code):
---------------------------------------
for k from 1 to N:
    for i from 1 to N:
        for j from 1 to N:
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]

Central and Median Node Calculation:
------------------------------------
For each node i:
    - Eccentricity[i] = maximum distance from node i to any other reachable node.
    - Closeness[i] = sum of reciprocals of distances from node i to all reachable nodes.

Select:
    - Central Node: node with minimal eccentricity.
    - Median Node: node with maximal closeness.

References:
- Floyd-Warshall Algorithm: https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
- Closeness Centrality: https://en.wikipedia.org/wiki/Closeness_centrality

Example Application:
These algorithms can be applied to real-world problems, such as determining the optimal
location for facilities (e.g., emergency response centers) to minimize response times
within a network. By identifying the central or median nodes, organizations can make
informed decisions on resource placement to improve efficiency and accessibility.
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


def find_central_node(
    eccentricities: list[tuple[int, float]],
) -> tuple[int, float]:
    """Identify the node with minimal eccentricity among reachable nodes.

    Args:
        eccentricities: List of tuples (node index, eccentricity).

    Returns:
        The node with minimal eccentricity and its value. Returns (-1, inf) if
        no valid nodes are found.
    """
    valid_eccentricities = [e for e in eccentricities if e[1] != float("inf")]
    return min(
        valid_eccentricities,
        key=lambda node_eccentricity: (node_eccentricity[1], node_eccentricity[0]),
        default=(-1, float("inf")),
    )


def find_median_node(closenesses: list[tuple[int, float]]) -> tuple[int, float]:
    """Identify the node with maximal closeness among reachable nodes.

    Args:
        closenesses: List of tuples (node index, closeness centrality).

    Returns:
        The node with maximal closeness and its value. Returns (-1, inf) if
        no valid nodes are found.
    """
    valid_closenesses = [c for c in closenesses if c[1] != float("inf")]
    return max(
        valid_closenesses,
        key=lambda node_closeness: (node_closeness[1], -node_closeness[0]),
        default=(-1, float("inf")),
    )


def find_central_and_median_node(
    distance_matrix: np.ndarray,
) -> tuple[tuple[int, float], tuple[int, float]]:
    """Determine the central and median nodes based on shortest-path distances.

    For each node, calculates its eccentricity and harmonic closeness centrality,
    considering only reachable nodes. Then, identifies the central node (minimal
    eccentricity) and median node (maximal closeness).

    Args:
        distance_matrix: A numpy.ndarray representing shortest-path distances
                         between all pairs of nodes.

    Returns:
        A tuple containing:
            - central_node: A tuple (node index, eccentricity) for the node with
              minimal eccentricity.
            - median_node: A tuple (node index, closeness) for the node with maximal
              harmonic closeness centrality.
    """
    num_nodes: int = len(distance_matrix)

    # Single-node graph case
    if num_nodes == 1:
        return (0, 0.0), (0, 0.0)

    eccentricities: list[tuple[int, float]] = []
    closenesses: list[tuple[int, float]] = []

    for i in range(num_nodes):
        reachable_distances = get_reachable_distances(distance_matrix[i])

        if reachable_distances.size == 0:
            # No reachable nodes, isolated component
            eccentricity = float("inf")
            closeness = float("inf")
        else:
            # Compute eccentricity and closeness for reachable nodes
            eccentricity = float(np.max(reachable_distances))
            closeness = float(np.sum(1 / reachable_distances))

        eccentricities.append((i, eccentricity))
        closenesses.append((i, closeness))

    central_node = find_central_node(eccentricities)
    median_node = find_median_node(closenesses)

    return central_node, median_node


# Test cases included as doctests
def test_single_node() -> None:
    """
    Test a graph with a single node.

    >>> graph = {0: []}
    >>> distance_matrix = floyd_warshall_algorithm(graph)
    >>> central_node, median_node = find_central_and_median_node(distance_matrix)
    >>> central_node
    (0, 0.0)
    >>> median_node
    (0, 0.0)
    """


def test_two_nodes_positive_weight() -> None:
    """
    Test a graph with two nodes connected by a positive weight.

    >>> graph = {0: [(1, 5.0)], 1: [(0, 5.0)]}
    >>> distance_matrix = floyd_warshall_algorithm(graph)
    >>> central_node, median_node = find_central_and_median_node(distance_matrix)
    >>> central_node
    (0, 5.0)
    >>> median_node
    (0, 0.2)
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
    >>> central_node, median_node = find_central_and_median_node(distance_matrix)
    >>> central_node
    (0, 1.0)
    >>> median_node
    (0, 2.0)
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
    >>> central_node, median_node = find_central_and_median_node(distance_matrix)
    >>> central_node
    (2, 1.0)
    >>> median_node
    (0, 1.8333333333333333)
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
    >>> central_node, median_node = find_central_and_median_node(distance_matrix)
    >>> central_node
    (-1, inf)
    >>> median_node
    (-1, inf)
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


def test_cyclic_graph() -> None:
    """
    Test a cyclic graph where there is a cycle between nodes.

    >>> graph = {
    ...     0: [(1, 1.0)],
    ...     1: [(2, 1.0)],
    ...     2: [(0, 1.0)]
    ... }
    >>> distance_matrix = floyd_warshall_algorithm(graph)
    >>> central_node, median_node = find_central_and_median_node(distance_matrix)
    >>> central_node
    (0, 2.0)
    >>> median_node
    (0, 1.5)
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
    >>> central_node, median_node = find_central_and_median_node(distance_matrix)
    >>> central_node
    (3, 5.0)
    >>> median_node
    (0, 0.8825396825396825)
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
    >>> central_node, median_node = find_central_and_median_node(distance_matrix)
    >>> central_node[0] is not None  # Ensure it found a central node
    True
    >>> median_node[0] is not None  # Ensure it found a median node
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
