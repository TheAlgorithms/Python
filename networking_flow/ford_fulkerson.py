"""
Ford-Fulkerson Algorithm for Maximum Flow Problem
* https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm

Description:
    (1) Start with initial flow as 0
    (2) Choose the augmenting path from source to sink and add the path to flow
"""

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
    num_nodes = len(graph)
    visited = [False] * num_nodes
    queue: deque[int] = deque()

    queue.append(source)
    visited[source] = True

    while queue:
        current_node = queue.popleft()

        # If we reached the sink, we can stop early
        if current_node == sink:
            return True

        # Check all adjacent nodes
        for neighbor, capacity in enumerate(graph[current_node]):
            if not visited[neighbor] and capacity > 0:
                visited[neighbor] = True
                parents[neighbor] = current_node
                queue.append(neighbor)

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
    # Create a copy of the graph to avoid modifying the original
    residual_graph = [row[:] for row in graph]
    num_nodes = len(residual_graph)
    parents = [-1] * num_nodes
    max_flow = 0

    # Augment the flow while there is a path from source to sink
    while breadth_first_search(residual_graph, source, sink, parents):
        # Find the minimum residual capacity along the path
        path_flow = 10**9  # Large integer instead of float
        current_node = sink

        # Find the minimum capacity in the path
        while current_node != source:
            parent_node = parents[current_node]
            path_flow = min(path_flow, residual_graph[parent_node][current_node])
            current_node = parent_node

        # Add path flow to overall flow
        max_flow += path_flow

        # Update residual capacities of the edges and reverse edges
        current_node = sink
        while current_node != source:
            parent_node = parents[current_node]
            residual_graph[parent_node][current_node] -= path_flow
            residual_graph[current_node][parent_node] += path_flow
            current_node = parent_node

    return max_flow


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print(f"{ford_fulkerson(graph, source=0, sink=5) = }")
