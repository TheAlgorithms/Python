"""
Topological sorting for Directed Acyclic Graph (DAG) is an ordering of vertices
such that for every directed edge u -> v, vertex u comes before v in the ordering.
Source: https://en.wikipedia.org/wiki/Topological_sorting#Depth-first_search
"""


def topological_sort(graph: dict[str, list[str]]) -> list[str]:
    """
    Performs topological sorting on a directed acyclic graph (DAG).

    Args:
        graph: A dictionary representing the adjacency lists of the graph
               where keys are nodes and values are lists of adjacent nodes.

    Returns:
        A list of nodes in topologically sorted order.

    Raises:
        ValueError: If the graph contains a cycle (topological sort not possible).

    Examples:
        >>> # Simple linear graph
        >>> # 1 -> 2 -> 3
        >>> topological_sort({'1': ['2'], '2': ['3'], '3': []})
        ['1', '2', '3']

        >>> # Graph with multiple possible orderings
        >>> #        A
        >>> #      ↙  ↘
        >>> #     B     C
        >>> #   ↙  ↘
        >>> #  D     E
        >>> graph = {
        ...     'A': ['B', 'C'],
        ...     'B': ['D', 'E'],
        ...     'C': [],
        ...     'D': [],
        ...     'E': []
        ... }
        >>> import random
        >>> adjacency_lists = list(graph.items())
        >>> random.shuffle(adjacency_lists)
        >>> graph = dict(adjacency_lists)
        >>> result = topological_sort(graph)
        >>> result in (
        ...     ['A', 'B', 'C', 'D', 'E'],
        ...     ['A', 'B', 'C', 'E', 'D'],
        ...     ['A', 'B', 'D', 'C', 'E'],
        ...     ['A', 'B', 'D', 'E', 'C'],
        ...     ['A', 'B', 'E', 'C', 'D'],
        ...     ['A', 'B', 'E', 'D', 'C'],
        ...     ['A', 'C', 'B', 'D', 'E'],
        ...     ['A', 'C', 'B', 'E', 'D']
        ... )
        True

        >>> # Empty graph
        >>> topological_sort({})
        []

        >>> # Graph with cycle (should raise error)
        >>> topological_sort({'A': ['B'], 'B': ['C'], 'C': ['A']})
        Traceback (most recent call last):
        ...
        ValueError: Graph contains a cycle, topological sort not possible
    """

    is_being_visited = set()  # To track nodes in current path being visited through DFS
    visited = set()  # To track and efficiently lookup if a node has been fully visited
    result = []

    def visit(node: str) -> None:
        is_being_visited.add(node)

        for neighbor in graph.get(node, []):
            if neighbor in visited:
                continue

            if neighbor in is_being_visited:
                # If the 'neighbor' is already in 'is_being_visited',
                # it means we have found a cycle.
                raise ValueError(
                    "Graph contains a cycle, topological sort not possible"
                )

            visit(neighbor)

        is_being_visited.remove(node)
        visited.add(node)
        # Fully visited nodes are supposed to be prepended to the result list
        # But since prepending to python lists is O(n), i.e., costly,
        # we will append them and reverse the result at the end.
        result.append(node)

    for node in graph:
        if node not in visited:
            visit(node)

    return result[::-1]  # Reverse the result to get the correct topological order


if __name__ == "__main__":
    graph: dict[str, list[str]] = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": [],
        "D": [],
        "E": [],
    }

    sorted_values = topological_sort(graph)

    print(f"Sorted values: {sorted_values}")
