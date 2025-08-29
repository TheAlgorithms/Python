"""
Graph Coloring also called "m coloring problem"
consists of coloring a given graph with at most m colors
such that no adjacent vertices are assigned the same color

Wikipedia: https://en.wikipedia.org/wiki/Graph_coloring
"""


def valid_coloring(
    neighbours: list[int], colored_vertices: list[int], color: int
) -> bool:
    """
    For each neighbour check if the coloring constraint is satisfied
    If any of the neighbours fail the constraint return False
    If all neighbours validate the constraint return True

    >>> neighbours = [0,1,0,1,0]
    >>> colored_vertices = [0, 2, 1, 2, 0]

    >>> color = 1
    >>> valid_coloring(neighbours, colored_vertices, color)
    True

    >>> color = 2
    >>> valid_coloring(neighbours, colored_vertices, color)
    False
    """
    # Does any neighbour not satisfy the constraints
    return not any(
        neighbour == 1 and colored_vertices[i] == color
        for i, neighbour in enumerate(neighbours)
    )


def util_color(
    graph: list[list[int]], max_colors: int, colored_vertices: list[int], index: int
) -> bool:
    """
    Pseudo-Code

    Base Case:
    1. Check if coloring is complete
        1.1 If complete return True (meaning that we successfully colored the graph)

    Recursive Step:
    2. Iterates over each color:
        Check if the current coloring is valid:
            2.1. Color given vertex
            2.2. Do recursive call, check if this coloring leads to a solution
            2.4. if current coloring leads to a solution return
            2.5. Uncolor given vertex

    >>> graph = [[0, 1, 0, 0, 0],
    ...          [1, 0, 1, 0, 1],
    ...          [0, 1, 0, 1, 0],
    ...          [0, 1, 1, 0, 0],
    ...          [0, 1, 0, 0, 0]]
    >>> max_colors = 3
    >>> colored_vertices = [0, 1, 0, 0, 0]
    >>> index = 3

    >>> util_color(graph, max_colors, colored_vertices, index)
    True

    >>> max_colors = 2
    >>> util_color(graph, max_colors, colored_vertices, index)
    False
    """

    # Base Case
    if index == len(graph):
        return True

    # Recursive Step
    for i in range(max_colors):
        if valid_coloring(graph[index], colored_vertices, i):
            # Color current vertex
            colored_vertices[index] = i
            # Validate coloring
            if util_color(graph, max_colors, colored_vertices, index + 1):
                return True
            # Backtrack
            colored_vertices[index] = -1
    return False


def color(graph: list[list[int]], max_colors: int) -> list[int]:
    """
    Wrapper function to call subroutine called util_color
    which will either return True or False.
    If True is returned colored_vertices list is filled with correct colorings

    >>> graph = [[0, 1, 0, 0, 0],
    ...          [1, 0, 1, 0, 1],
    ...          [0, 1, 0, 1, 0],
    ...          [0, 1, 1, 0, 0],
    ...          [0, 1, 0, 0, 0]]

    >>> max_colors = 3
    >>> color(graph, max_colors)
    [0, 1, 0, 2, 0]

    >>> max_colors = 2
    >>> color(graph, max_colors)
    []
    """
    colored_vertices = [-1] * len(graph)

    if util_color(graph, max_colors, colored_vertices, 0):
        return colored_vertices

    return []
