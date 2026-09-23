def transitive_closure(graph: list[list[int]]) -> list[list[int]]:
    """
    Computes the transitive closure of a directed graph using the
    Floyd-Warshall algorithm.

    Args:
        graph: Adjacency matrix representation of the graph.

    Returns:
        Transitive closure matrix.

    >>> graph = [
    ...     [0, 1, 1, 0],
    ...     [0, 0, 1, 0],
    ...     [1, 0, 0, 1],
    ...     [0, 0, 0, 0]
    ... ]
    >>> transitive_closure(graph)  # doctest: +NORMALIZE_WHITESPACE
    [[1, 1, 1, 1],
     [1, 1, 1, 1],
     [1, 1, 1, 1],
     [0, 0, 0, 1]]
    """
    width = len(graph)
    ans = [[graph[i][j] for j in range(width)] for i in range(width)]

    # Transitive closure of (i, i) will always be 1
    for i in range(width):
        ans[i][i] = 1

    # Apply Floyd-Warshall Algorithm
    # For each intermediate node k
    for k in range(width):
        for i in range(width):
            for j in range(width):
                # Check if a path exists from i to k and from k to j.
                if ans[i][k] == 1 and ans[k][j] == 1:
                    ans[i][j] = 1

    return ans


if __name__ == "__main__":
    import doctest

    doctest.testmod()
