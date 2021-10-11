"""
* Author: Manuel Di Lullo (https://github.com/manueldilullo)
* Python Version: 3.9
* Description: Complete graphs generator. Uses graphs represented with an adjacency list 

URL: https://en.wikipedia.org/wiki/Complete_graph
"""

def complete_graph(n:int) -> dict:
    """
    function that generate a complete graph with n vertices
    @input: n (number of vertices), directed (False if the graph is undirected, True otherwise)
    @example:
    >>> print(complete_graph(3))
    {0: [1, 2], 1: [2], 2: []}
    """
    g = {}
    for i in range(n):
        g[i] = []
        for j in range(0,n):
            if i != j:
                g[i].append(j)
    return g

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # print(f"Complete graph:\n{complete_graph(5)}")