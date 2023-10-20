from collections import defaultdict, deque


def is_bipartite_dfs(graph: defaultdict[int, list[int]]) -> bool:
    """
    Check if a graph is bipartite using DFS.

    Args:
        graph (defaultdict[int, list[int]]): Adjacency list representing the graph.

    Returns:
        bool: True if bipartite, False otherwise.

    This function checks if the graph can be divided into two sets of vertices,
    such that no two vertices within the same set are connected by an edge.

    Examples:
    >>> is_bipartite_dfs(defaultdict(list, {0: [1, 2], 1: [0, 3], 2: [0, 4]}))
    True
    >>> is_bipartite_dfs(defaultdict(list, {0: [1, 2], 1: [0, 3], 2: [0, 1]}))
    False
    """

    def dfs(node, color):
        """
        Perform Depth-First Search (DFS) on the graph starting from a node.

        Args:
            node: The current node being visited.
            color: The color assigned to the current node.

        Returns:
            bool: True if the graph is bipartite starting from the current node, False otherwise.
        """
        if visited[node] == -1:
            visited[node] = color
            for neighbor in graph[node]:
                if not dfs(neighbor, 1 - color):
                    return False
        return visited[node] == color

    visited = defaultdict(lambda: -1)
    for node in graph:
        if visited[node] == -1 and not dfs(node, 0):
            return False
    return True


def is_bipartite_bfs(graph: defaultdict[int, list[int]]) -> bool:
    """
    Check if a graph is bipartite using BFS.

    Args:
        graph (defaultdict[int, list[int]]): Adjacency list representing the graph.

    Returns:
        bool: True if bipartite, False otherwise.

    This function checks if the graph can be divided into two sets of vertices,
    such that no two vertices within the same set are connected by an edge.

    Examples:
    >>> is_bipartite_bfs(defaultdict(list, {0: [1, 2], 1: [0, 3], 2: [0, 4]}))
    True
    >>> is_bipartite_bfs(defaultdict(list, {0: [1, 2], 1: [0, 2], 2: [0, 1]}))
    False
    """
    visited = defaultdict(lambda: -1)
    for node in graph:
        if visited[node] == -1:
            queue = deque()
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
