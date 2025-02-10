"""
Graph Coloring (also called the "m coloring problem") is the problem of
assigning at most 'm' colors to the vertices of a graph such that
no two adjacent vertices share the same color.

Wikipedia: https://en.wikipedia.org/wiki/Graph_coloring
"""


def valid_coloring(
    neighbours: list[int], colored_vertices: list[int], color: int
) -> bool:
    """
    Check if a given vertex can be assigned the specified color
    without violating the graph coloring constraints (i.e., no two adjacent vertices
    have the same color).

    Procedure:
    For each neighbour check if the coloring constraint is satisfied
    If any of the neighbours fail the constraint return False
    If all neighbours validate the constraint return True

    Parameters:
    neighbours: The list representing which vertices
                are adjacent to the current vertex.
                1 indicates an edge between the current vertex
                and the neighbour.
    colored_vertices: List of current color assignments for all vertices
                      (-1 means uncolored).
    color: The color we are trying to assign to the current vertex.

    Returns:
    True if the vertex can be safely colored with the given color,
    otherwise False.

    Examples:
    >>> neighbours = [0, 1, 0, 1, 0]
    >>> colored_vertices = [0, 2, 1, 2, 0]
    >>> color = 1
    >>> valid_coloring(neighbours, colored_vertices, color)
    True

    >>> color = 2
    >>> valid_coloring(neighbours, colored_vertices, color)
    False

    >>> neighbors = [1, 0, 1, 0]
    >>> colored_vertices = [-1, -1, -1, -1]
    >>> color = 0
    >>> valid_coloring(neighbors, colored_vertices, color)
    True
    """
    # Check if any adjacent vertex has already been colored with the same color
    return not any(
        neighbour == 1 and colored_vertices[i] == color
        for i, neighbour in enumerate(neighbours)
    )


def util_color(
    graph: list[list[int]], max_colors: int, colored_vertices: list[int], index: int
) -> bool:
    """
    Recursive function to try and color the graph using backtracking.

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

    Parameters:
    graph: Adjacency matrix representing the graph.
           graph[i][j] is 1 if there is an edge
           between vertex i and j.
    max_colors: Maximum number of colors allowed (m in the m-coloring problem).
    colored_vertices: Current color assignments for each vertex.
                      -1 indicates that the vertex has not been colored
                      yet.
    index: The current vertex index being processed.

    Returns:
    True if the graph can be colored using at most max_colors, otherwise False.

    Examples:
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
    # Base Case: If all vertices have been assigned a color, we have a valid solution
    if index == len(graph):
        return True

    # Try each color for the current vertex
    for color in range(max_colors):
        # Check if it's valid to color the current vertex with 'color'
        if valid_coloring(graph[index], colored_vertices, color):
            colored_vertices[index] = color  # Assign color
            # Recur to color the rest of the vertices
            if util_color(graph, max_colors, colored_vertices, index + 1):
                return True
            # Backtrack if no solution found with the current assignment
            colored_vertices[index] = -1

    return False  # Return False if no valid coloring is possible


def color(graph: list[list[int]], max_colors: int) -> list[int]:
    """
    Attempt to color the graph with at most max_colors colors such that no two adjacent
    vertices have the same color.
    If it is possible, returns the list of color assignments;
    otherwise, returns an empty list.

    Parameters:
    graph: Adjacency matrix representing the graph.
    max_colors: Maximum number of colors allowed.

    Returns:
    List of color assignments if the graph can be colored using max_colors.
    Each index in the list represents the color assigned
    to the corresponding vertex.
    If coloring is not possible, returns an empty list.

    Examples:
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

    >>> graph = [[0, 1], [1, 0]]  # Simple 2-node graph
    >>> max_colors = 2
    >>> color(graph, max_colors)
    [0, 1]

    >>> graph = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]  # Complete graph of 3 vertices
    >>> max_colors = 2
    >>> color(graph, max_colors)
    []

    >>> max_colors = 3
    >>> color(graph, max_colors)
    [0, 1, 2]
    """
    # Initialize all vertices as uncolored (-1)
    colored_vertices = [-1] * len(graph)

    # Use the utility function to try and color the graph starting from vertex 0
    if util_color(graph, max_colors, colored_vertices, 0):
        return colored_vertices  # The successful color assignment

    return []  # No valid coloring is possible
