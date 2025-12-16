def transitive_closure(graph: list[list[int]]) -> list[list[int]]:
    """
    Computes the transitive closure of a directed graph using the
    Floyd-Warshall algorithm.

    Args:
        graph (list[list[int]]): Adjacency matrix representation of the graph.

    Returns:
        list[list[int]]: Transitive closure matrix.

    >>> graph = [
    ...     [0, 1, 1, 0],
    ...     [0, 0, 1, 0],
    ...     [1, 0, 0, 1],
    ...     [0, 0, 0, 0]
    ... ]
    >>> result = transitive_closure(graph)
    >>> for row in result:
    ...     print(row)
    [1, 1, 1, 1]
    [1, 1, 1, 1]
    [1, 1, 1, 1]
    [0, 0, 0, 1]
    """
    n = len(graph)
    ans = [[graph[i][j] for j in range(n)] for i in range(n)]

    # Transtive closure of (i, i) will always be 1
    for i in range(n):
        ans[i][i] = 1

    # Apply floyd Warshall Algorithm
    # For each intermediate node k
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # Check if a path exists between i to k and
                # between k to j.
                if ans[i][k] == 1 and ans[k][j] == 1:
                    ans[i][j] = 1

    return ans


if __name__ == "__main__":
    import doctest

    doctest.testmod()
