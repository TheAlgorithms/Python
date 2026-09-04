"""Topological Sort."""

#     a
#    / \
#   b  c
#  / \
# d  e
edges: dict[str, list[str]] = {
    "a": ["c", "b"],
    "b": ["d", "e"],
    "c": [],
    "d": [],
    "e": [],
}
vertices: list[str] = ["a", "b", "c", "d", "e"]


def _visit(
    current: str,
    visited: list[str],
    post_order: list[str],
    graph: dict[str, list[str]],
) -> None:
    """Visit descendants of ``current``.

    Appends to ``visited`` and ``post_order`` in place.
    """
    visited.append(current)
    for neighbor in graph[current]:
        if neighbor not in visited:
            _visit(neighbor, visited, post_order, graph)
    post_order.append(current)


def topological_sort(
    start: str,
    visited: list[str],
    order: list[str],
    graph: dict[str, list[str]] | None = None,
    vertices_list: list[str] | None = None,
) -> list[str]:
    """
    Perform topological sort on a directed acyclic graph.

    >>> result = topological_sort("a", [], [], edges, vertices)
    >>> all(
    ...     result.index(parent) < result.index(child)
    ...     for parent, children in edges.items()
    ...     for child in children
    ... )
    True
    """
    if graph is None:
        graph = edges
    if vertices_list is None:
        vertices_list = list(graph)

    _visit(start, visited, order, graph)
    if len(visited) != len(vertices_list):
        for vertice in vertices_list:
            if vertice not in visited:
                _visit(vertice, visited, order, graph)
    # DFS post-order is reverse topological order, so reverse once at the end.
    order.reverse()
    return order


if __name__ == "__main__":
    result = topological_sort("a", [], [], edges, vertices)
    assert result == ["a", "b", "e", "d", "c"]
    print(result)
