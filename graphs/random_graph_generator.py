"""
* Author: Manuel Di Lullo (https://github.com/manueldilullo)
* Python Version: 3.9
* Description: Random graphs generator. Uses graphs represented with an adjacency list.

URL: https://en.wikipedia.org/wiki/Random_graph
"""

import numpy as np

def random_graph(vertices_number:int, probability:float, directed:bool=False) -> dict:
    """
    Function that generates a random graph
    @input: vertices_number (number of vertices), probability (probability that a generic edge (u,v) exists), 
            directed (if it's True, g will be a directed graph, otherwise it will be an undirected graph)
    @examples:
    >>> print(random_graph(5, 0.5))
    {0: [1, 2, 3], 1: [0, 3], 2: [0, 3, 4], 3: [0, 1, 2, 4], 4: [2, 3]}
    >>> print(random_graph(5, 0.5, True))
    {0: [2], 1: [], 2: [3, 4], 3: [4], 4: []}
    """
    g = dict(zip(range(vertices_number), [[] for _ in range(vertices_number)]))

    # if probability is greater or equal than 1, then generate a complete graph
    if probability >= 1:
        return complete_graph(vertices_number)
    # if probability is lower or equal than 0, then return a graph without edges
    if probability <= 0:
        return g

    # for each couple of nodes, add an edge from u to v
    # if the number randomly generated is greater than probability probability
    for i in range(vertices_number):
        for j in range(i+1, vertices_number):
            if np.random.random() < probability:
                g[i].append(j)
                if not directed:
                    # if the graph is undirected, add an edge in from j to i, either
                    g[j].append(i)
    return g


def complete_graph(vertices_number:int) -> dict:
    """
    function that generate a complete graph with vertices_number vertices
    @input: vertices_number (number of vertices), directed (False if the graph is undirected, True otherwise)
    @example:
    >>> print(complete_graph(3))
    {0: [1, 2], 1: [2], 2: []}
    """
    g = {}
    for i in range(vertices_number):
        g[i] = []
        for j in range(0,vertices_number):
            if i != j:
                g[i].append(j)
    return g

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # print(f"Random undirected graph:\vertices_number{random_graph(5, 0.5)}")
    # print(f"Random directed graph:\vertices_number{random_graph(5, 0.5, True)}")