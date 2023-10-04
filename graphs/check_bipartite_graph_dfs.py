from collections import defaultdict


def is_bipartite(graph: defaultdict[int, list[int]]) -> bool:
    """
    Check whether a graph is Bipartite or not using Depth-First Search (DFS).

    A Bipartite Graph is a graph whose vertices can be divided into two independent
    sets, U and V such that every edge (u, v) either connects a vertex from
    U to V or a vertex from V to U. In other words, for every edge (u, v),
    either u belongs to U and v to V, or u belongs to V and v to U. There is
    no edge that connects vertices of the same set.

    Args:
        graph: An adjacency list representing the graph.

    Returns:
        True if there's no edge that connects vertices of the same set, False otherwise.

    Examples:
        >>> graph1=defaultdict(list,{0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2], 4: []})
        >>> is_bipartite(graph1)
        True

        >>> graph2 = defaultdict(list, {0: [1, 2], 1: [0, 2], 2: [0, 1]})
        >>> is_bipartite(graph2)
        False
    """

    def dfs(node, color):
        vis[node] = color
        for nbor in graph[node]:
            if vis[nbor] == color or (vis[nbor] == -1 and not dfs(nbor, 1 - color)):
                return False
        return True

    vis: defaultdict[int, int] = defaultdict(lambda: -1)

    return all(not (vis[node] == -1 and not dfs(node, 0)) for node in graph)


if __name__ == "__main__":
    import doctest

    result = doctest.testmod()

    if result.failed == 0:
        print("All tests passed!")
    else:
        print(f"{result.failed} test(s) failed.")
