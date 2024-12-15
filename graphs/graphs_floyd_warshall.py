# floyd_warshall.py
"""
The problem is to find and return the shortest distance between all pairs of vertices in a
weighted directed graph that can have negative edge weights.

https://docs.python.org/3/library/doctest.html

"""


def floyd_warshall(graph: list[list[float]], vertex: int) -> tuple:
    # 1. For all edges from v to n, distance[i][j] = weight(edge(i, j)).

    # 3. distance[i][j] = min(distance[i][j], distance[i][k] +distance[k][j]) for each possible pair i, j of vertices.

    # 4. Step 3 repeated for k vertex in the graph.

    # 5. Whenever distance[i][j] is given a new minimum value, next vertex[i][j] = next vertex[i][k].

    """
    :param graph: 2D array calculated from weight[edge[i, j]]

    :param v: number of vertices

    :return: shortest distance between all vertex pairs

    distance[u][v] will contain the shortest distance from vertex u to v.

    # doctests:

    >>> graph = [[0, 3, float('inf')], [2, 0, float('inf')],[float('inf'), 7, 0]]
    >>> floyd_warshall(graph, 3)[0]
    [[0, 3, inf], [2, 0, inf], [9, 7, 0]]

    >>> graph = [[0, 1, 4],[float('inf'), 0, 2],[float('inf'), float('inf'), 0]]
    >>> floyd_warshall(graph, 3)[0]
    [[0, 1, 3], [inf, 0, 2], [inf, inf, 0]]

    >>> graph = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
    >>> floyd_warshall(graph, 3)[0]
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    #Graph with all edge weights = infinity

    >>> graph = [[float('inf'), float('inf'), float('inf')],[float('inf'), float('inf'), float('inf')],[float('inf'), float('inf'), float('inf')]]
    >>> floyd_warshall(graph, 3)[0]
    [[inf, inf, inf], [inf, inf, inf], [inf, inf, inf]]


    #Handling negetive weighted graph:

    >>> graph = [[0, -2, float('inf')],[float('inf'), 0, 3],[4, float('inf'), 0]]
    >>> floyd_warshall(graph, 3)[0]
    [[0, -2, 1], [7, 0, 3], [4, 2, 0]]


    #Handling negetive weighted cycle:

    >>> graph = [[0, -1, float('inf')],[float('inf'), 0, -2],[-3, float('inf'), 0]]
    >>> floyd_warshall(graph, 3)[0]
    [[-6, -7, -9], [-5, -6, -8], [-9, -10, -12]]


    #Number of vertex in function arguement should match number of vertex in graph:

    >>> graph = [[0, -1, float('inf')],[float('inf'), 0, -2]]
    >>> floyd_warshall(graph, 3)[0]
    Traceback (most recent call last):
        ...
    IndexError: list index out of range


    #Graph data type should be a 2D list:

    >>> graph = "strings not allowed"
    >>> floyd_warshall(graph, 3)[0]
    Traceback (most recent call last):
        ...
    IndexError: string index out of range
    """

    dist = [[float("inf") for _ in range(vertex)] for _ in range(vertex)]

    for i in range(vertex):
        for j in range(vertex):
            dist[i][j] = graph[i][j]
            # check vertex k against all other vertices (i, j)

    for k in range(vertex):
        # looping through rows of graph array

        for i in range(vertex):
            # looping through columns of graph array

            for j in range(vertex):
                if (
                    dist[i][k] != float("inf")
                    and dist[k][j] != float("inf")
                    and dist[i][k] + dist[k][j] < dist[i][j]
                ):
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist, vertex


if __name__ == "__main__":
    import doctest

    doctest.testmod()
