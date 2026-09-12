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


def _topological_sort_list_queue(graph: dict[int, list[int]]) -> list[int] | None:
    """
    Pre-optimization implementation of Kahn's topological sort using list.pop(0).

    Used as a baseline for benchmark comparison against deque.popleft().
    """
    indegree = [0] * len(graph)
    queue = []
    topo_order = []
    processed_vertices_count = 0

    for values in graph.values():
        for i in values:
            indegree[i] += 1

    for i in range(len(indegree)):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        vertex = queue.pop(0)
        processed_vertices_count += 1
        topo_order.append(vertex)

        for neighbor in graph[vertex]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if processed_vertices_count != len(graph):
        return None
    return topo_order


def benchmark() -> None:
    """
    Benchmark comparing topological_sort() (using deque.popleft) against
    the pre-optimization baseline _topological_sort_list_queue() (using list.pop(0)).

    Demonstrates the performance improvement of O(1) queue operations in Kahn's algorithm
    on a graph with a large number of zero-indegree vertices.
    """
    from timeit import timeit

    num_sources = 30_000
    graph = {i: [num_sources] for i in range(num_sources)}
    graph[num_sources] = []

    # Verify correctness: both implementations produce valid topological sorts
    old_result = _topological_sort_list_queue(graph)
    new_result = topological_sort(graph)
    assert old_result is not None and new_result is not None
    assert len(old_result) == len(new_result) == num_sources + 1
    assert set(old_result) == set(new_result)

    runs = 5
    old_time = timeit(lambda: _topological_sort_list_queue(graph), number=runs)
    new_time = timeit(lambda: topological_sort(graph), number=runs)

    print(
        f"Benchmark results for topological_sort with {num_sources} vertices over {runs} runs:"
    )
    print(f"Pre-optimization (list.pop(0)): {old_time:.5f} seconds")
    print(f"Current (deque.popleft):       {new_time:.5f} seconds")
    if new_time > 0:
        print(f"Speedup ratio:                 {old_time / new_time:.2f}x faster")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    benchmark()
