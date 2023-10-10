import doctest


def graph_coloring(graph: list[list[int]]) -> list[int]:
    """
    Graph coloring algorithm using a greedy approach.

    Parameters:
    - graph (List[List[int]])

    Returns:
    - list[int]

    Example:
    >>> graph_coloring([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]])
    [0, 1, 2, 1]

    >>> graph_coloring([[1], [0, 2], [1]])
    [0, 1, 0]
    """

    num_vertices = len(graph)
    result = [-1] * num_vertices
    result[0] = 0
    available_colors = [True] * num_vertices

    for u in range(1, num_vertices):
        for i in graph[u]:
            if result[i] != -1:
                available_colors[result[i]] = False

        cr = 0
        while cr < num_vertices:
            if available_colors[cr]:
                break
            cr += 1

        result[u] = cr

        for i in graph[u]:
            if result[i] != -1:
                available_colors[result[i]] = True

    return result


if __name__ == "__main__":
    doctest.testmod()
