from collections import defaultdict, deque


def is_bipartite_dfs(graph: dict[int, list[int]]) -> bool:
    """
    Check if a graph is bipartite using depth-first search (DFS).

    Args:
        `graph`: Adjacency list representing the graph.

    Returns:
        ``True`` if bipartite, ``False`` otherwise.

    Checks if the graph can be divided into two sets of vertices, such that no two
    vertices within the same set are connected by an edge.

    Examples:

    >>> is_bipartite_dfs({0: [1, 2], 1: [0, 3], 2: [0, 4]})
    True
    >>> is_bipartite_dfs({0: [1, 2], 1: [0, 3], 2: [0, 1]})
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
    False

    >>> # FIXME: This test should fails with KeyError: 4.
    >>> is_bipartite_dfs({0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2], 9: [0]})
    False
    >>> is_bipartite_dfs({0: [-1, 3], 1: [0, -2]})
    False
    >>> is_bipartite_dfs({-1: [0, 2], 0: [-1, 1], 1: [0, 2], 2: [-1, 1]})
    True
    >>> is_bipartite_dfs({0.9: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]})
    True

    >>> # FIXME: This test should fails with
    >>> # TypeError: list indices must be integers or...
    >>> is_bipartite_dfs({0: [1.0, 3.0], 1.0: [0, 2.0], 2.0: [1.0, 3.0], 3.0: [0, 2.0]})
    True
    >>> is_bipartite_dfs({"a": [1, 3], "b": [0, 2], "c": [1, 3], "d": [0, 2]})
    True
    >>> is_bipartite_dfs({0: ["b", "d"], 1: ["a", "c"], 2: ["b", "d"], 3: ["a", "c"]})
    True
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
            if node not in graph:
                return True
            for neighbor in graph[node]:
                if not depth_first_search(neighbor, 1 - color):
                    return False
        return visited[node] == color

    visited: defaultdict[int, int] = defaultdict(lambda: -1)
    for node in graph:
        if visited[node] == -1 and not depth_first_search(node, 0):
            return False
    return True


def is_bipartite_bfs(graph: dict[int, list[int]]) -> bool:
    """
    Check if a graph is bipartite using a breadth-first search (BFS).

    Args:
        `graph`: Adjacency list representing the graph.

    Returns:
        ``True`` if bipartite, ``False`` otherwise.

    Check if the graph can be divided into two sets of vertices, such that no two
    vertices within the same set are connected by an edge.

    Examples:

    >>> is_bipartite_bfs({0: [1, 2], 1: [0, 3], 2: [0, 4]})
    True
    >>> is_bipartite_bfs({0: [1, 2], 1: [0, 2], 2: [0, 1]})
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
    False

    >>> # FIXME: This test should fails with KeyError: 4.
    >>> is_bipartite_bfs({0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2], 9: [0]})
    False
    >>> is_bipartite_bfs({0: [-1, 3], 1: [0, -2]})
    False
    >>> is_bipartite_bfs({-1: [0, 2], 0: [-1, 1], 1: [0, 2], 2: [-1, 1]})
    True
    >>> is_bipartite_bfs({0.9: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]})
    True

    >>> # FIXME: This test should fails with
    >>> # TypeError: list indices must be integers or...
    >>> is_bipartite_bfs({0: [1.0, 3.0], 1.0: [0, 2.0], 2.0: [1.0, 3.0], 3.0: [0, 2.0]})
    True
    >>> is_bipartite_bfs({"a": [1, 3], "b": [0, 2], "c": [1, 3], "d": [0, 2]})
    True
    >>> is_bipartite_bfs({0: ["b", "d"], 1: ["a", "c"], 2: ["b", "d"], 3: ["a", "c"]})
    True
    """
    visited: defaultdict[int, int] = defaultdict(lambda: -1)
    for node in graph:
        if visited[node] == -1:
            queue: deque[int] = deque()
            queue.append(node)
            visited[node] = 0
            while queue:
                curr_node = queue.popleft()
                if curr_node not in graph:
                    continue
                for neighbor in graph[curr_node]:
                    if visited[neighbor] == -1:
                        visited[neighbor] = 1 - visited[curr_node]
                        queue.append(neighbor)
                    elif visited[neighbor] == visited[curr_node]:
                        return False
    return True


if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if result.failed:
        print(f"{result.failed} test(s) failed.")
    else:
        print("All tests passed!")
