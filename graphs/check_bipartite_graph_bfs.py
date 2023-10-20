# Check whether Graph is Bipartite or Not using BFS


# A Bipartite Graph is a graph whose vertices can be divided into two independent sets,
# U and V such that every edge (u, v) either connects a vertex from U to V or a vertex
# from V to U. In other words, for every edge (u, v), either u belongs to U and v to V,
# or u belongs to V and v to U. We can also say that there is no edge that connects
# vertices of same set.
from queue import Queue


def check_bipartite(graph):
    """
    >>> check_bipartite({})
    True
    >>> check_bipartite({0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]})
    True
    >>> check_bipartite({0: [1, 2, 3], 1: [0, 2], 2: [0, 1, 3], 3: [0, 2]})
    False
    >>> check_bipartite({0: [4], 1: [], 2: [4], 3: [4], 4: [0, 2, 3]})
    True
    >>> check_bipartite({0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2], 4: [0]})
    False
    >>> check_bipartite({7: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2], 4: [0]})
    Traceback (most recent call last):
        ...
    KeyError: 0
    >>> check_bipartite({0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2], 9: [0]})
    Traceback (most recent call last):
        ...
    KeyError: 4
    >>> check_bipartite({0: [-1, 3], 1: [0, -2]})
    Traceback (most recent call last):
        ...
    IndexError: list index out of range
    >>> check_bipartite({-1: [0, 2], 0: [-1, 1], 1: [0, 2], 2: [-1, 1]})
    True
    >>> check_bipartite({0.9: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]})
    Traceback (most recent call last):
        ...
    KeyError: 0
    >>> check_bipartite({0: [1.0, 3.0], 1.0: [0, 2.0], 2.0: [1.0, 3.0], 3.0: [0, 2.0]})
    Traceback (most recent call last):
        ...
    TypeError: list indices must be integers or slices, not float
    >>> check_bipartite({"a": [1, 3], "b": [0, 2], "c": [1, 3], "d": [0, 2]})
    Traceback (most recent call last):
        ...
    KeyError: 0
    >>> check_bipartite({0: ["b", "d"], 1: ["a", "c"], 2: ["b", "d"], 3: ["a", "c"]})
    Traceback (most recent call last):
        ...
    TypeError: list indices must be integers or slices, not str
    """
    queue = Queue()
    visited = [False] * len(graph)
    color = [-1] * len(graph)

    def bfs():
        while not queue.empty():
            u = queue.get()
            visited[u] = True

            for neighbour in graph[u]:
                if neighbour == u:
                    return False

                if color[neighbour] == -1:
                    color[neighbour] = 1 - color[u]
                    queue.put(neighbour)

                elif color[neighbour] == color[u]:
                    return False

        return True

    for i in range(len(graph)):
        if not visited[i]:
            queue.put(i)
            color[i] = 0
            if bfs() is False:
                return False

    return True


if __name__ == "__main__":
    # Adjacency List of graph
    print(check_bipartite({0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]}))
    import doctest

    doctest.testmod()
