"""
Graph topological sort implementation using Depth-First Search (DFS).

A topological sort or topological ordering of a directed graph is a linear
ordering of its vertices in which each vertex comes before all vertices
to which it has outgoing edges.

For example, the graph representing clothing dependencies:
- underwear -> pants -> belt -> suit
- shirt -> tie -> suit
- socks -> shoes

Author: Phyllipe Bezerra (https://github.com/pmba)
"""

from collections.abc import Sequence


class TopologicalSort:
    """Topological sort implementation using DFS."""

    def __init__(
        self, graph: list[list[int]], labels: dict[int, str] | None = None
    ) -> None:
        """Initialize the topological sorter.

        Args:
            graph: Adjacency list representation where graph[u] contains
                   all vertices v such that there is an edge from u to v.
            labels: Optional mapping from vertex indices to label strings
                    for pretty printing results.
        """
        self.graph = graph
        self.labels = labels or {}
        self.n = len(graph)
        self.visited: list[int] = [0] * self.n
        self.stack: list[int] = []

    def _depth_first_search(self, u: int) -> None:
        """Perform DFS from vertex u, adding to stack after exploring all neighbors."""
        self.visited[u] = 1
        for v in self.graph[u]:
            if not self.visited[v]:
                self._depth_first_search(v)
        self.stack.append(u)

    def sort(self) -> list[int]:
        """Compute and return the topological ordering of vertices.

        Returns:
            A list of vertices in topological order (each vertex appears before
            all vertices reachable from it).
        """
        self.stack = []
        self.visited = [0] * self.n

        for v in range(self.n):
            if not self.visited[v]:
                self._depth_first_search(v)

        return self.stack[::-1]

    def print_sorted(self, order: list[int]) -> None:
        """Print the vertices in topological order with their labels.

        Args:
            order: A list of vertices in topological order.
        """
        for i, vertex in enumerate(order, 1):
            label = self.labels.get(vertex, str(vertex))
            print(f"{i}. {label}")


def topological_sort(graph: list[list[int]], visited: list[int]) -> list[int]:
    """Topological sort of a directed acyclic graph using DFS.

    Args:
        graph: Adjacency list representation of the graph.
        visited: List to track visited vertices (modified in place).

    Returns:
        Vertices in topological order.

    Examples:
    >>> graph = [[1, 2], [3], [3], []]
    >>> visited = [0] * len(graph)
    >>> topological_sort(graph, visited)
    [0, 2, 1, 3]
    """
    stack = []

    def dfs(u: int) -> None:
        visited[u] = 1
        for v in graph[u]:
            if not visited[v]:
                dfs(v)
        stack.append(u)

    for v in range(len(graph)):
        if not visited[v]:
            dfs(v)

    return stack[::-1]


if __name__ == "__main__":
    # Example: Clothing dependencies
    clothes = {
        0: "underwear",
        1: "pants",
        2: "belt",
        3: "suit",
        4: "shoe",
        5: "socks",
        6: "shirt",
        7: "tie",
        8: "watch",
    }

    graph = [[1, 4], [2, 4], [3], [], [], [4], [2, 7], [3], []]

    # Using the class-based interface
    sorter = TopologicalSort(graph, clothes)
    order = sorter.sort()
    sorter.print_sorted(order)

    # Also demonstrate the functional interface
    print("\n--- Using functional interface ---")
    visited = [0] * len(graph)
    result = topological_sort(graph, visited)
    print(result)
