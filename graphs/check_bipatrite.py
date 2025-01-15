from collections import defaultdict, deque


def is_bipartite_dfs(graph: defaultdict[int, list[int]]) -> bool:
    """
    Check if a graph is bipartite using depth-first search (DFS).

    Args:
        `graph`: Adjacency list representing the graph.

    Returns:
        ``True`` if bipartite, ``False`` otherwise.

    Checks if the graph can be divided into two sets of vertices, such that no two
    vertices within the same set are connected by an edge.

    Examples:

    >>> # FIXME: This test should pass.
    >>> is_bipartite_dfs(defaultdict(list, {0: [1, 2], 1: [0, 3], 2: [0, 4]}))
    Traceback (most recent call last):
        ...
    RuntimeError: dictionary changed size during iteration
    >>> is_bipartite_dfs(defaultdict(list, {0: [1, 2], 1: [0, 3], 2: [0, 1]}))
    False
    >>> is_bipartite_dfs({})
    True
    >>> is_bipartite_dfs({0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]})
    True
    >>> is_bipartite_dfs({0: [1, 2, 3], 1: [0, 2], 2: [0, 1, 3], 3: [0, 2]})
    False
    >>> is_bipartite_dfs({0: [4], 1: [], 2: [4], 3: [4], 4: [0, 2, 3]})
    True
    >>> is_bipartite_dfs({0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2], 4: [0]})
    False
    >>> is_bipartite_dfs({7: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2], 4: [0]})
    Traceback (most recent call last):
        ...
    KeyError: 0

    >>> # FIXME: This test should fails with KeyError: 4.
    >>> is_bipartite_dfs({0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2], 9: [0]})
    False
    >>> is_bipartite_dfs({0: [-1, 3], 1: [0, -2]})
    Traceback (most recent call last):
        ...
    KeyError: -1
    >>> is_bipartite_dfs({-1: [0, 2], 0: [-1, 1], 1: [0, 2], 2: [-1, 1]})
    True
    >>> is_bipartite_dfs({0.9: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]})
    Traceback (most recent call last):
        ...
    KeyError: 0

    >>> # FIXME: This test should fails with
    >>> # TypeError: list indices must be integers or...
    >>> is_bipartite_dfs({0: [1.0, 3.0], 1.0: [0, 2.0], 2.0: [1.0, 3.0], 3.0: [0, 2.0]})
    True
    >>> is_bipartite_dfs({"a": [1, 3], "b": [0, 2], "c": [1, 3], "d": [0, 2]})
    Traceback (most recent call last):
        ...
    KeyError: 1
    >>> is_bipartite_dfs({0: ["b", "d"], 1: ["a", "c"], 2: ["b", "d"], 3: ["a", "c"]})
    Traceback (most recent call last):
        ...
    KeyError: 'b'
    """

    def depth_first_search(node: int, color: int) -> bool:
        """
        Perform Depth-First Search (DFS) on the graph starting from a node.

        Args:
            node: The current node being visited.
            color: The color assigned to the current node.

        Returns:
            True if the graph is bipartite starting from the current node,
            False otherwise.
        """
        if visited[node] == -1:
            visited[node] = color
            for neighbor in graph[node]:
                if not depth_first_search(neighbor, 1 - color):
                    return False
        return visited[node] == color

    visited: defaultdict[int, int] = defaultdict(lambda: -1)
    for node in graph:
        if visited[node] == -1 and not depth_first_search(node, 0):
            return False
    return True


def is_bipartite_bfs(graph: defaultdict[int, list[int]]) -> bool:
    """
    Check if a graph is bipartite using a breadth-first search (BFS).

    Args:
        `graph`: Adjacency list representing the graph.

    Returns:
        ``True`` if bipartite, ``False`` otherwise.

    Check if the graph can be divided into two sets of vertices, such that no two
    vertices within the same set are connected by an edge.

    Examples:

    >>> # FIXME: This test should pass.
    >>> is_bipartite_bfs(defaultdict(list, {0: [1, 2], 1: [0, 3], 2: [0, 4]}))
    Traceback (most recent call last):
        ...
    RuntimeError: dictionary changed size during iteration
    >>> is_bipartite_bfs(defaultdict(list, {0: [1, 2], 1: [0, 2], 2: [0, 1]}))
    False
    >>> is_bipartite_bfs({})
    True
    >>> is_bipartite_bfs({0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]})
    True
    >>> is_bipartite_bfs({0: [1, 2, 3], 1: [0, 2], 2: [0, 1, 3], 3: [0, 2]})
    False
    >>> is_bipartite_bfs({0: [4], 1: [], 2: [4], 3: [4], 4: [0, 2, 3]})
    True
    >>> is_bipartite_bfs({0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2], 4: [0]})
    False
    >>> is_bipartite_bfs({7: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2], 4: [0]})
    Traceback (most recent call last):
        ...
    KeyError: 0

    >>> # FIXME: This test should fails with KeyError: 4.
    >>> is_bipartite_bfs({0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2], 9: [0]})
    False
    >>> is_bipartite_bfs({0: [-1, 3], 1: [0, -2]})
    Traceback (most recent call last):
        ...
    KeyError: -1
    >>> is_bipartite_bfs({-1: [0, 2], 0: [-1, 1], 1: [0, 2], 2: [-1, 1]})
    True
    >>> is_bipartite_bfs({0.9: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]})
    Traceback (most recent call last):
        ...
    KeyError: 0

    >>> # FIXME: This test should fails with
    >>> # TypeError: list indices must be integers or...
    >>> is_bipartite_bfs({0: [1.0, 3.0], 1.0: [0, 2.0], 2.0: [1.0, 3.0], 3.0: [0, 2.0]})
    True
    >>> is_bipartite_bfs({"a": [1, 3], "b": [0, 2], "c": [1, 3], "d": [0, 2]})
    Traceback (most recent call last):
        ...
    KeyError: 1
    >>> is_bipartite_bfs({0: ["b", "d"], 1: ["a", "c"], 2: ["b", "d"], 3: ["a", "c"]})
    Traceback (most recent call last):
        ...
    KeyError: 'b'
    """
    visited: defaultdict[int, int] = defaultdict(lambda: -1)
    for node in graph:
        if visited[node] == -1:
            queue: deque[int] = deque()
            queue.append(node)
            visited[node] = 0
            while queue:
                curr_node = queue.popleft()
                for neighbor in graph[curr_node]:
                    if visited[neighbor] == -1:
                        visited[neighbor] = 1 - visited[curr_node]
                        queue.append(neighbor)
                    elif visited[neighbor] == visited[curr_node]:
                        return False
    return True


if __name__ == "__main":
    import doctest

    result = doctest.testmod()
    if result.failed:
        print(f"{result.failed} test(s) failed.")
    else:
        print("All tests passed!")
