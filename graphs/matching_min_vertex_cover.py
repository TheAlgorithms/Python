"""
* Author: Manuel Di Lullo (https://github.com/manueldilullo)
* Description: Approximization algorithm for minimum vertex cover problem.
               Matching Approach. Uses graphs represented with an adjacency list

URL: https://mathworld.wolfram.com/MinimumVertexCover.html
URL: https://www.princeton.edu/~aaa/Public/Teaching/ORF523/ORF523_Lec6.pdf
"""


def matching_min_vertex_cover(graph: dict) -> set:
    """
    APX Algorithm for min Vertex Cover using Matching Approach
    @input: graph (graph stored in an adjacency list where each vertex
            is represented with an integer)
    @example:
    >>> graph = {0: [1, 3], 1: [0, 3], 2: [0, 3, 4], 3: [0, 1, 2], 4: [2, 3]}
    >>> matching_min_vertex_cover(graph)
    {0, 1, 2, 4}
    """
    # chosen_vertices = set of chosen vertices
    chosen_vertices = set()
    # edges = list of graph's edges
    edges = get_edges(graph)

    # while there are still elements in edges' list
    # take an arbitrary edge (node_from,node_to) and add his extremity to s
    # then remove all arcs adjacent to the node_from and node_to
    while edges:
        node_from, node_to = edges.pop()
        chosen_vertices.add(node_from)
        chosen_vertices.add(node_to)
        for edge in edges.copy():
            if (node_from in edge) or (node_to in edge):
                edges.discard(edge)
    return chosen_vertices


def get_edges(graph: dict) -> set:
    """
    Function that returns a set of couples that represents
    the set of all the edges
    @input: graph (graph stored in an adjacency list where each vertex
            is represented with an integer)
    @example:
    >>> graph = {0: [1, 3], 1: [0, 3], 2: [0, 3], 3: [0, 1, 2]}
    >>> get_edges(graph)
    {(0, 1), (3, 1), (0, 3), (2, 0), (3, 0), (2, 3), (1, 0), (3, 2), (1, 3)}
    """
    edges = set()
    for node_from in graph.keys():
        for node_to in graph[node_from]:
            edges.add((node_from, node_to))
    return edges


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # graph = {0: [1, 3], 1: [0, 3], 2: [0, 3, 4], 3: [0, 1, 2], 4: [2, 3]}
    # print(f"Matching vertex cover:\n{matching_min_vertex_cover(graph)}")
