from collections import defaultdict
from queue import Queue


def check_bipartite(graph: dict[int, list[int]]) -> bool:
    """
    Check if a graph is Bipartite using Depth-First Search.

    Args:
        graph: Adjacency list representing the graph.

    Returns:
        bool: True if no edge connects same set vertices.

    Examples:
        >>> is_bipartite(defaultdict(list, {0: [1, 2], 1: [0, 3], ...}))
        False
        >>> is_bipartite(defaultdict(list, {0: [1, 2], 1: [0, 2], 2: [0, 1]}))
        True
    """
    queue: Queue = Queue()
    visited = [False] * len(graph)
    color = [-1] * len(graph)

    def bfs() -> bool:
        """
        Perform Breadth-First Search (BFS) on a graph to check if it's bipartite.

        Args:
            graph (dict[int, list[int]]): An adjacency list representing the graph.

        Returns:
            bool: True if there's no edge, False otherwise.

        Examples:
            >>> bfs({0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]})
            True
            >>> bfs({0: [1, 2, 3], 1: [0, 2], 2: [0, 1, 3], 3: [0, 2]})
            False
        """
        while not queue.empty():
            u = queue.get()
            visited[u] = True

            for neighbour in graph[u]:
                if neighbour == u:
                    return False

                if color[neighbour] == -1:
                    color[neighbour] = 1 - color[u]
                    queue.put(neighbour)

                elif color[neighbour] == color[u]:
                    return False

        return True

    for i in range(len(graph)):
        if not visited[i]:
            queue.put(i)
            color[i] = 0
            if bfs() is False:
                return False

    return True


if __name__ == "__main__":
    # Adjacency List of graph
    print(check_bipartite({0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]}))


def is_bipartite(graph: defaultdict[int, list[int]]) -> bool:
    """
    Check if a graph is Bipartite using Breadth-First Search.

    Args:
        graph: Adjacency list representing the graph.

    Returns:
        bool: True if no edge connects same set vertices.

    Examples:
        >>> check_bipartite({0: [1, 3], 1: [0, 2], 2: [1, 3], ...})
        True
        >>> check_bipartite({0: [1, 2, 3], 1: [0, 2], ...})
        False
    """

    def dfs(node: int, color: int) -> bool:
        """
        Perform depth-first search from a node with specified color.

        Args:
            node (int): Current node being visited.
            color (int): Color assigned to the current node.

        Returns:
            bool: True if the graph is bipartite fromcurrent node,else False.

        Examples:
            >>> dfs(0, 0, defaultdict(list, {0: [1, 2], ...}))
            False
            >>> dfs(0, 0, defaultdict(list, {0: [1, 2], 1: [0, 2], ...}))
            True
        """
        visited[node] = color
        return any(
            visited[neighbour] == color
            or (
                visited[neighbour] == -1
                and not dfs(neighbour, 1 - color)
            )
            for neighbour in graph[node]
        )

    visited: defaultdict[int, int] = defaultdict(lambda: -1)

    return all(
        not (visited[node] == -1 and not dfs(node, 0)) for node in graph
    )


if __name__ == "__main__":
    import doctest

    result = doctest.testmod()

    if result.failed:
        print(f"{result.failed} test(s) failed.")
    else:
        print("All tests passed!")
