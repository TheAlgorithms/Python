from typing import List, Tuple, Union

"""
    Graph Coloring also called "m coloring problem"
    consists of coloring given graph with at most m colors
    such that no adjacent vertices are assigned same color
"""


def valid_coloring(
    neighbours: List[int], colored_vertices: List[int], color: int
) -> bool:
    """
    For each neighbour check if coloring constraint is satisfied
    If any of the neighbours fail the contraint return False
    If all neighbours validate constraint return True

    >>> neighbours = [0,1,0,1,0]
    >>> colored_vertices = [0, 2, 1, 2, 0]
    
    >>> color = 1
    >>> valid_coloring(neighbours, colored_vertices, color)
    True

    >>> color = 2
    >>> valid_coloring(neighbours, colored_vertices, color)
    False
    """
    for i in range(len(neighbours)):
        # Constraint Failed
        if neighbours[i] == 1 and colored_vertices[i] == color:
            return False
    # All neighbours satisfy constraint
    return True


def util_color(
    graph: List[List[int]], max_colors: int, colored_vertices: List[int], index: int
) -> bool:
    """ 
    Pseudo-Code

    Base Case:
    1. Check if coloring is complete 
        1.1 If complete return True (meaning that we successfully colored graph)

    Recursive Step:
    2. Itterates over each color:
        Check if current coloring is valid:
            2.1. Color given vertex
            2.2. Do recursive call check if this coloring leads to solving problem
            2.4. if current coloring leads to solution return
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
    for i in range(0, max_colors):
        if valid_coloring(graph[index], colored_vertices, i):
            # Color current vertex
            colored_vertices[index] = i
            # Validate coloring
            if util_color(graph, max_colors, colored_vertices, index + 1):
                return True
            # Backtrack
            colored_vertices[index] = -1
    return False


def color(
    graph: List[List[int]], max_colors: int
) -> Tuple[bool, Union[List[int], None]]:
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
    (True, [0, 1, 0, 2, 0])

    >>> max_colors = 2
    >>> color(graph, max_colors)
    (False, None)
    """
    colored_vertices = [-1] * len(graph)

    if util_color(graph, max_colors, colored_vertices, 0):
        return True, colored_vertices

    return False, None
