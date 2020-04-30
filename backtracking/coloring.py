"""
    Graph Coloring also called "m coloring problem"
    consists of coloring given graph with at most m colors
    such that no adjacent vertices are assigned same color
"""

def color(graph, m):
    """
    >>> graph = [[0, 1, 0, 0, 0],
    ...          [1, 0, 1, 0, 1],
    ...          [0, 1, 0, 1, 0],
    ...          [0, 1, 1, 0, 0],
    ...          [0, 1, 0, 0, 0]]

    >>> total_colors = 3
    >>> color(graph, total_colors)
    (True, [1, 2, 1, 3, 1])

    >>> total_colors = 2
    >>> color(graph, total_colors)
    (False, None)
    """
    pass