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
    """

    indegree = [0] * len(graph)
    queue = []
    topo_order = []
    processed_vertices_count = 0

    # Calculate the indegree of each vertex
    for values in graph.values():
        for i in values:
            indegree[i] += 1

    # Add all vertices with 0 indegree to the queue
    for i in range(len(indegree)):
        if indegree[i] == 0:
            queue.append(i)

    # Perform BFS
    while queue:
        vertex = queue.pop(0)
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
