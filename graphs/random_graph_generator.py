"""
* Author: Manuel Di Lullo (https://github.com/manueldilullo)
* Description: Random graphs generator.
               Uses graphs represented with an adjacency list.

URL: https://en.wikipedia.org/wiki/Random_graph
"""

import random


def random_graph(
    vertices_number: int, probability: float, directed: bool = False
) -> dict:
    """
    Generate a random graph
    @input: vertices_number (number of vertices),
            probability (probability that a generic edge (u,v) exists),
            directed (if True: graph will be a directed graph,
                      otherwise it will be an undirected graph)
    @examples:
    >>> random.seed(1)
    >>> random_graph(4, 0.5)
    {0: [1], 1: [0, 2, 3], 2: [1, 3], 3: [1, 2]}
    >>> random.seed(1)
    >>> random_graph(4, 0.5, True)
    {0: [1], 1: [2, 3], 2: [3], 3: []}
    """
    graph: dict = {i: [] for i in range(vertices_number)}

    # if probability is greater or equal than 1, then generate a complete graph
    if probability >= 1:
        return complete_graph(vertices_number)
    # if probability is lower or equal than 0, then return a graph without edges
    if probability <= 0:
        return graph

    # for each couple of nodes, add an edge from u to v
    # if the number randomly generated is greater than probability probability
    for i in range(vertices_number):
        for j in range(i + 1, vertices_number):
            if random.random() < probability:
                graph[i].append(j)
                if not directed:
                    # if the graph is undirected, add an edge in from j to i, either
                    graph[j].append(i)
    return graph


def complete_graph(vertices_number: int) -> dict:
    """
    Generate a complete graph with vertices_number vertices.
    @input: vertices_number (number of vertices),
            directed (False if the graph is undirected, True otherwise)
    @example:
    >>> complete_graph(3)
    {0: [1, 2], 1: [0, 2], 2: [0, 1]}
    """
    return {
        i: [j for j in range(vertices_number) if i != j] for i in range(vertices_number)
    }


if __name__ == "__main__":
    import doctest

    doctest.testmod()
