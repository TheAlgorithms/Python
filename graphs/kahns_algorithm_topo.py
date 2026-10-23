from collections import deque


def topological_sort(graph: dict[int, list[int]]) -> list[int] | None:
    """
    Perform topological sorting of a Directed Acyclic Graph (DAG)
    using Kahn's Algorithm via Breadth-First Search (BFS).

    Topological sorting is a linear ordering of vertices in a graph such that for
    every directed edge u → v, vertex u comes before vertex v in the ordering.

    Parameters:
    graph: Adjacency list representing the directed graph where keys are
           vertices, and values are lists of adjacent vertices.

    Returns:
    The topologically sorted order of vertices if the graph is a DAG.
    Returns None if the graph contains a cycle.

    Example:
    >>> graph = {0: [1, 2], 1: [3], 2: [3], 3: [4, 5], 4: [], 5: []}
    >>> topological_sort(graph)
    [0, 1, 2, 3, 4, 5]

    >>> graph_with_cycle = {0: [1], 1: [2], 2: [0]}
    >>> topological_sort(graph_with_cycle)

    >>> sparse_graph = {10: [20], 20: []}
    >>> topological_sort(sparse_graph)
    [10, 20]

    >>> sparse_cycle = {10: [20], 20: [10]}
    >>> topological_sort(sparse_cycle)

    >>> topological_sort({})
    []
    >>> topological_sort({42: []})
    [42]
    >>> order = topological_sort({10: [20], 20: [], 30: [40], 40: []})
    >>> sorted(order)
    [10, 20, 30, 40]
    >>> order.index(10) < order.index(20) and order.index(30) < order.index(40)
    True
    >>> topological_sort({7: [7]}) is None
    True
    """

    indegree = dict.fromkeys(graph, 0)
    queue: deque[int] = deque()
    topo_order = []
    processed_vertices_count = 0

    # Calculate the indegree of each vertex
    for values in graph.values():
        for i in values:
            indegree[i] += 1

    # Add all vertices with 0 indegree to the queue
    for vertex, count in indegree.items():
        if count == 0:
            queue.append(vertex)

    # Perform BFS
    while queue:
        vertex = queue.popleft()
        processed_vertices_count += 1
        topo_order.append(vertex)

        # Traverse neighbors
        for neighbor in graph[vertex]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if processed_vertices_count != len(graph):
        return None  # no topological ordering exists due to cycle
    return topo_order  # valid topological ordering


if __name__ == "__main__":
    import doctest

    doctest.testmod()
