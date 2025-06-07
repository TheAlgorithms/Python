graph = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0],
]


def breadth_first_search(graph: list, source: int, sink: int, parents: list) -> bool:
    """
    This function returns True if there is a node that has not iterated.

    Args:
        graph: Adjacency matrix of graph
        source: Source
        sink: Sink
        parents: Parent list

    Returns:
        True if there is a node that has not iterated.

    >>> breadth_first_search(graph, 0, 5, [-1, -1, -1, -1, -1, -1])
    True
    >>> breadth_first_search(graph, 0, 6, [-1, -1, -1, -1, -1, -1])
    Traceback (most recent call last):
        ...
    IndexError: list index out of range
    """
    visited = [False] * len(graph)  # Mark all nodes as not visited
    queue = []  # breadth-first search queue

    # Source node
    queue.append(source)
    visited[source] = True

    while queue:
        u = queue.pop(0)  # Pop the front node
        # Traverse all adjacent nodes of u
        for ind, node in enumerate(graph[u]):
            if visited[ind] is False and node > 0:
                queue.append(ind)
                visited[ind] = True
                parents[ind] = u
    return visited[sink]


def ford_fulkerson(graph: list, source: int, sink: int) -> int:
    """
    This function returns the maximum flow from source to sink in the given graph.

    CAUTION: This function changes the given graph.

    Args:
        graph: Adjacency matrix of graph
        source: Source
        sink: Sink

    Returns:
        Maximum flow

    >>> test_graph = [
    ...     [0, 16, 13, 0, 0, 0],
    ...     [0, 0, 10, 12, 0, 0],
    ...     [0, 4, 0, 0, 14, 0],
    ...     [0, 0, 9, 0, 0, 20],
    ...     [0, 0, 0, 7, 0, 4],
    ...     [0, 0, 0, 0, 0, 0],
    ... ]
    >>> ford_fulkerson(test_graph, 0, 5)
    23
    """
    # This array is filled by breadth-first search and to store path
    parent = [-1] * (len(graph))
    max_flow = 0

    # While there is a path from source to sink
    while breadth_first_search(graph, source, sink, parent):
        path_flow = int(1e9)  # Infinite value
        s = sink

        while s != source:
            # Find the minimum value in the selected path
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow
        v = sink

        while v != source:
            u = parent[v]
            # Update residual capacities
            graph[u][v] -= path_flow
            # Ensure reverse edge exists
            if graph[v][u] == 0:
                graph[v][u] = (
                    0  # Explicitly initialize if needed (though usually already 0)
                )
            graph[v][u] += path_flow
            v = parent[v]

    return max_flow


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    # Make a copy of the original graph to preserve it
    graph_copy = [row[:] for row in graph]
    print(f"{ford_fulkerson(graph_copy, source=0, sink=5) = }")
