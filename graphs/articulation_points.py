# Finding Articulation Points in Undirected Graph
# https://en.wikipedia.org/wiki/Biconnected_component


def compute_ap(graph: dict[int, list[int]]) -> list[int]:
    """
    Return the articulation points of an undirected graph in increasing order.

    An articulation point is a vertex whose removal disconnects part of the graph.
    The graph is an adjacency list whose keys are the vertices 0 to n - 1.

    >>> compute_ap({0: [1, 2], 1: [0, 2], 2: [0, 1, 3, 5], 3: [2, 4], 4: [3],
    ...             5: [2, 6, 8], 6: [5, 7], 7: [6, 8], 8: [5, 7]})
    [2, 3, 5]
    >>> compute_ap({0: [5, 4], 1: [3], 2: [5, 3], 3: [1, 2], 4: [5, 0],
    ...             5: [2, 4, 0]})
    [2, 3, 5]
    >>> compute_ap({0: [1], 1: [0, 2], 2: [1]})
    [1]
    >>> compute_ap({0: [1, 2], 1: [0, 2], 2: [0, 1]})
    []
    >>> compute_ap({0: [1], 1: [0], 2: [3, 4], 3: [2, 4], 4: [2, 3]})
    []
    >>> compute_ap({0: [1], 1: [0, 2], 2: [1], 3: [4], 4: [3, 5], 5: [4]})
    [1, 4]
    >>> compute_ap({0: []})
    []
    >>> compute_ap({})
    []
    """
    n = len(graph)
    discovery = [-1] * n  # order in which each vertex is first reached (-1: not yet)
    low = [0] * n  # smallest discovery number reachable from the vertex's branch
    is_art = [False] * n
    timer = 0

    def dfs(at: int, parent: int) -> int:
        """Visit ``at`` and return the number of branches the search starts from it."""
        nonlocal timer
        discovery[at] = low[at] = timer
        timer += 1
        children = 0
        for to in graph[at]:
            if to == parent:
                continue
            if discovery[to] == -1:
                children += 1
                dfs(to, at)
                low[at] = min(low[at], low[to])
                # a branch that cannot get back above ``at`` is cut off without it
                if parent != -1 and low[to] >= discovery[at]:
                    is_art[at] = True
            else:
                low[at] = min(low[at], discovery[to])
        return children

    for i in range(n):
        if discovery[i] == -1:
            # the starting vertex is critical only if the search leaves it
            # in two or more separate directions
            is_art[i] = dfs(i, -1) > 1

    return [i for i in range(n) if is_art[i]]


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Adjacency list of graph
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3, 5],
        3: [2, 4],
        4: [3],
        5: [2, 6, 8],
        6: [5, 7],
        7: [6, 8],
        8: [5, 7],
    }
    print(compute_ap(graph))
