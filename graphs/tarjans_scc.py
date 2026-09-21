from collections import deque


def tarjan(g: list[list[int]]) -> list[list[int]]:
    """
    Tarjan's algo for finding strongly connected components in a directed graph

    Uses two main attributes of each node to track reachability, the index of that node
    within a component(index), and the lowest index reachable from that node(lowlink).

    We then perform a dfs of the each component making sure to update these parameters
    for each node and saving the nodes we visit on the way.

    If ever we find that the lowest reachable node from a current node is equal to the
    index of the current node then it must be the root of a strongly connected
    component and so we save it and it's equireachable vertices as a strongly
    connected component.

    Complexity: strong_connect() is called at most once for each node and has a
    complexity of O(|E|) as it is DFS.
    Therefore this has complexity O(|V| + |E|) for a graph G = (V, E)

    >>> tarjan([[2, 3, 4], [2, 3, 4], [0, 1, 3], [0, 1, 2], [1]])
    [[4, 3, 1, 2, 0]]
    >>> tarjan([[], [], [], []])
    [[0], [1], [2], [3]]
    >>> a = [0, 1, 2, 3, 4, 5, 4]
    >>> b = [1, 0, 3, 2, 5, 4, 0]
    >>> n = 7
    >>> sorted(tarjan(create_graph(n, list(zip(a, b))))) == sorted(
    ...     tarjan(create_graph(n, list(zip(a[::-1], b[::-1])))))
    True
    >>> a = [0, 1, 2, 3, 4, 5, 6]
    >>> b = [0, 1, 2, 3, 4, 5, 6]
    >>> sorted(tarjan(create_graph(n, list(zip(a, b)))))
    [[0], [1], [2], [3], [4], [5], [6]]
    """

    n = len(g)
    stack: deque[int] = deque()
    on_stack = [False for _ in range(n)]
    index_of = [-1 for _ in range(n)]
    lowlink_of = index_of[:]

    def strong_connect(v: int, index: int, components: list[list[int]]) -> int:
        index_of[v] = index  # the number when this node is seen
        lowlink_of[v] = index  # lowest rank node reachable from here
        index += 1
        stack.append(v)
        on_stack[v] = True

        for w in g[v]:
            if index_of[w] == -1:
                index = strong_connect(w, index, components)
                lowlink_of[v] = (
                    lowlink_of[w] if lowlink_of[w] < lowlink_of[v] else lowlink_of[v]
                )
            elif on_stack[w]:
                lowlink_of[v] = (
                    lowlink_of[w] if lowlink_of[w] < lowlink_of[v] else lowlink_of[v]
                )

        if lowlink_of[v] == index_of[v]:
            component = []
            w = stack.pop()
            on_stack[w] = False
            component.append(w)
            while w != v:
                w = stack.pop()
                on_stack[w] = False
                component.append(w)
            components.append(component)
        return index

    components: list[list[int]] = []
    for v in range(n):
        if index_of[v] == -1:
            strong_connect(v, 0, components)

    return components


def create_graph(n: int, edges: list[tuple[int, int]]) -> list[list[int]]:
    """
    >>> n = 7
    >>> source = [0, 0, 1, 2, 3, 3, 4, 4, 6]
    >>> target = [1, 3, 2, 0, 1, 4, 5, 6, 5]
    >>> edges = list(zip(source, target))
    >>> create_graph(n, edges)
    [[1, 3], [2], [0], [1, 4], [5, 6], [], [5]]
    """
    g: list[list[int]] = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
    return g


if __name__ == "__main__":
    # Test
    n_vertices = 7
    source = [0, 0, 1, 2, 3, 3, 4, 4, 6]
    target = [1, 3, 2, 0, 1, 4, 5, 6, 5]
    edges = list(zip(source, target))
    g = create_graph(n_vertices, edges)

    assert tarjan(g) == [[5], [6], [4], [3, 2, 1, 0]]
