"""
Lanczos Method for Finding Eigenvalues and Eigenvectors of a Graph.

This module demonstrates the Lanczos method to approximate the largest eigenvalues
and corresponding eigenvectors of a symmetric matrix represented as a graph's
adjacency list. The method efficiently handles large, sparse matrices by converting
the graph to a tridiagonal matrix, whose eigenvalues and eigenvectors are then
computed.

Key Functions:
- `find_lanczos_eigenvectors`: Computes the k largest eigenvalues and vectors.
- `lanczos_iteration`: Constructs the tridiagonal matrix and orthonormal basis vectors.
- `multiply_matrix_vector`: Multiplies an adjacency list graph with a vector.

Complexity:
- Time: O(k * n), where k is the number of eigenvalues and n is the matrix size.
- Space: O(n), due to sparse representation and tridiagonal matrix structure.

Further Reading:
- Lanczos Algorithm: https://en.wikipedia.org/wiki/Lanczos_algorithm
- Eigenvector Centrality: https://en.wikipedia.org/wiki/Eigenvector_centrality

Example Usage:
Given a graph represented by an adjacency list, the `find_lanczos_eigenvectors`
function returns the largest eigenvalues and eigenvectors. This can be used to
analyze graph centrality.
"""

import numpy as np


def validate_adjacency_list(graph: list[list[int | None]]) -> None:
    """Validates the adjacency list format for the graph.

    Args:
        graph: A list of lists where each sublist contains the neighbors of a node.

    Raises:
        ValueError: If the graph is not a list of lists, or if any node has
                    invalid neighbors (e.g., out-of-range or non-integer values).

    >>> validate_adjacency_list([[1, 2], [0], [0, 1]])
    >>> validate_adjacency_list([[]])  # No neighbors, valid case
    >>> validate_adjacency_list([[1], [2], [-1]])  # Invalid neighbor
    Traceback (most recent call last):
        ...
    ValueError: Invalid neighbor -1 in node 2 adjacency list.
    """
    if not isinstance(graph, list):
        raise ValueError("Graph should be a list of lists.")

    for node_index, neighbors in enumerate(graph):
        if not isinstance(neighbors, list):
            no_neighbors_message: str = (
                f"Node {node_index} should have a list of neighbors."
            )
            raise ValueError(no_neighbors_message)
        for neighbor_index in neighbors:
            if (
                not isinstance(neighbor_index, int)
                or neighbor_index < 0
                or neighbor_index >= len(graph)
            ):
                invalid_neighbor_message: str = (
                    f"Invalid neighbor {neighbor_index} in node {node_index} "
                    f"adjacency list."
                )
                raise ValueError(invalid_neighbor_message)


def lanczos_iteration(
    graph: list[list[int | None]], num_eigenvectors: int
) -> tuple[np.ndarray, np.ndarray]:
    """Constructs the tridiagonal matrix and orthonormal basis vectors using the
    Lanczos method.

    Args:
        graph: The graph represented as a list of adjacency lists.
        num_eigenvectors: The number of largest eigenvalues and eigenvectors
                          to approximate.

    Returns:
        A tuple containing:
            - tridiagonal_matrix: A (num_eigenvectors x num_eigenvectors) symmetric
                                  matrix.
            - orthonormal_basis: A (num_nodes x num_eigenvectors) matrix of orthonormal
                                 basis vectors.

    Raises:
        ValueError: If num_eigenvectors is less than 1 or greater than the number of
                    nodes.

    >>> graph = [[1, 2], [0, 2], [0, 1]]
    >>> T, Q = lanczos_iteration(graph, 2)
    >>> T.shape == (2, 2) and Q.shape == (3, 2)
    True
    """
    num_nodes: int = len(graph)
    if not (1 <= num_eigenvectors <= num_nodes):
        raise ValueError(
            "Number of eigenvectors must be between 1 and the number of "
            "nodes in the graph."
        )

    orthonormal_basis: np.ndarray = np.zeros((num_nodes, num_eigenvectors))
    tridiagonal_matrix: np.ndarray = np.zeros((num_eigenvectors, num_eigenvectors))

    rng = np.random.default_rng()
    initial_vector: np.ndarray = rng.random(num_nodes)
    initial_vector /= np.sqrt(np.dot(initial_vector, initial_vector))
    orthonormal_basis[:, 0] = initial_vector

    prev_beta: float = 0.0
    for iter_index in range(num_eigenvectors):
        result_vector: np.ndarray = multiply_matrix_vector(
            graph, orthonormal_basis[:, iter_index]
        )
        if iter_index > 0:
            result_vector -= prev_beta * orthonormal_basis[:, iter_index - 1]
        alpha_value: float = np.dot(orthonormal_basis[:, iter_index], result_vector)
        result_vector -= alpha_value * orthonormal_basis[:, iter_index]

        prev_beta = np.sqrt(np.dot(result_vector, result_vector))
        if iter_index < num_eigenvectors - 1 and prev_beta > 1e-10:
            orthonormal_basis[:, iter_index + 1] = result_vector / prev_beta
        tridiagonal_matrix[iter_index, iter_index] = alpha_value
        if iter_index < num_eigenvectors - 1:
            tridiagonal_matrix[iter_index, iter_index + 1] = prev_beta
            tridiagonal_matrix[iter_index + 1, iter_index] = prev_beta
    return tridiagonal_matrix, orthonormal_basis


def multiply_matrix_vector(
    graph: list[list[int | None]], vector: np.ndarray
) -> np.ndarray:
    """Performs multiplication of a graph's adjacency list representation with a vector.

    Args:
        graph: The adjacency list of the graph.
        vector: A 1D numpy array representing the vector to multiply.

    Returns:
        A numpy array representing the product of the adjacency list and the vector.

    Raises:
        ValueError: If the vector's length does not match the number of nodes in the
                    graph.

    >>> multiply_matrix_vector([[1, 2], [0, 2], [0, 1]], np.array([1, 1, 1]))
    array([2., 2., 2.])
    >>> multiply_matrix_vector([[1, 2], [0, 2], [0, 1]], np.array([0, 1, 0]))
    array([1., 0., 1.])
    """
    num_nodes: int = len(graph)
    if vector.shape[0] != num_nodes:
        raise ValueError("Vector length must match the number of nodes in the graph.")

    result: np.ndarray = np.zeros(num_nodes)
    for node_index, neighbors in enumerate(graph):
        for neighbor_index in neighbors:
            result[node_index] += vector[neighbor_index]
    return result


def find_lanczos_eigenvectors(
    graph: list[list[int | None]], num_eigenvectors: int
) -> tuple[np.ndarray, np.ndarray]:
    """Computes the largest eigenvalues and their corresponding eigenvectors using the
    Lanczos method.

    Args:
        graph: The graph as a list of adjacency lists.
        num_eigenvectors: Number of largest eigenvalues and eigenvectors to compute.

    Returns:
        A tuple containing:
            - eigenvalues: 1D array of the largest eigenvalues in descending order.
            - eigenvectors: 2D array where each column is an eigenvector corresponding
                            to an eigenvalue.

    Raises:
        ValueError: If the graph format is invalid or num_eigenvectors is out of bounds.

    >>> eigenvalues, eigenvectors = find_lanczos_eigenvectors(
    ...     [[1, 2], [0, 2], [0, 1]], 2
    ... )
    >>> len(eigenvalues) == 2 and eigenvectors.shape[1] == 2
    True
    """
    validate_adjacency_list(graph)
    tridiagonal_matrix, orthonormal_basis = lanczos_iteration(graph, num_eigenvectors)
    eigenvalues, eigenvectors = np.linalg.eigh(tridiagonal_matrix)
    return eigenvalues[::-1], np.dot(orthonormal_basis, eigenvectors[:, ::-1])


def main() -> None:
    """
    Main driver function for testing the implementation with doctests.
    """
    import doctest

    doctest.testmod()


if __name__ == "__main__":
    main()
