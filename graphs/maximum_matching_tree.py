"""Maximum cardinality matching in an unweighted tree using dynamic programming.

A matching is a set of edges with no shared endpoints. Two subtree states record
the best matching when the root is free of child edges and when it is unrestricted.
An iterative traversal avoids the recursion limit on long paths.

Reference: https://usaco.guide/gold/dp-trees
"""


def maximum_matching_tree(
    num_vertices: int, edges: list[tuple[int, int]]
) -> list[tuple[int, int]]:
    """Return one maximum matching of a tree with vertices 0 .. num_vertices - 1.

    Each undirected edge must occur once. The input must be a connected tree,
    or the empty graph. Edge orientation and the choice between equally large
    matchings depend on traversal order. The input is not modified.
    Time and auxiliary space: O(num_vertices).

    >>> maximum_matching_tree(0, [])
    []
    >>> maximum_matching_tree(1, [])
    []
    >>> maximum_matching_tree(2, [(0, 1)])
    [(0, 1)]
    >>> maximum_matching_tree(4, [(0, 1), (1, 2), (2, 3)])
    [(0, 1), (2, 3)]
    >>> maximum_matching_tree(4, [(0, 1), (0, 2), (0, 3)])
    [(0, 1)]
    >>> maximum_matching_tree(6, [(0, 1), (0, 2), (1, 3), (2, 4), (2, 5)])
    [(1, 3), (2, 4)]
    >>> maximum_matching_tree(-1, [])
    Traceback (most recent call last):
        ...
    ValueError: num_vertices must be nonnegative
    >>> maximum_matching_tree(3, [(0, 1)])
    Traceback (most recent call last):
        ...
    ValueError: edges must describe a tree
    >>> maximum_matching_tree(2, [(0, 2)])
    Traceback (most recent call last):
        ...
    ValueError: edge endpoints must be distinct vertices in range
    >>> maximum_matching_tree(2, [(0, 0)])
    Traceback (most recent call last):
        ...
    ValueError: edge endpoints must be distinct vertices in range
    >>> maximum_matching_tree(3, [(0, 1), (0, 1)])
    Traceback (most recent call last):
        ...
    ValueError: edges must describe a connected tree
    >>> maximum_matching_tree(4, [(0, 1), (1, 2), (2, 0)])
    Traceback (most recent call last):
        ...
    ValueError: edges must describe a connected tree
    """
    if num_vertices < 0:
        raise ValueError("num_vertices must be nonnegative")
    if len(edges) != max(0, num_vertices - 1):
        raise ValueError("edges must describe a tree")

    adjacency: list[list[int]] = [[] for _ in range(num_vertices)]
    for first, second in edges:
        if not (0 <= first < num_vertices and 0 <= second < num_vertices):
            raise ValueError("edge endpoints must be distinct vertices in range")
        if first == second:
            raise ValueError("edge endpoints must be distinct vertices in range")
        adjacency[first].append(second)
        adjacency[second].append(first)
    if num_vertices == 0:
        return []

    parent = [-1] * num_vertices
    parent[0] = 0
    order = [0]
    for vertex in order:
        for neighbor in adjacency[vertex]:
            if parent[neighbor] == -1:
                parent[neighbor] = vertex
                order.append(neighbor)
    # With n - 1 edges, connectivity also rules out cycles and parallel edges.
    if len(order) != num_vertices:
        raise ValueError("edges must describe a connected tree")

    free = [0] * num_vertices
    best = [0] * num_vertices
    chosen_child = [-1] * num_vertices
    for vertex in reversed(order):
        children = [child for child in adjacency[vertex] if child != parent[vertex]]
        free[vertex] = sum(best[child] for child in children)
        best[vertex] = free[vertex]
        for child in children:
            candidate = free[vertex] - best[child] + free[child] + 1
            if candidate > best[vertex]:
                best[vertex] = candidate
                chosen_child[vertex] = child

    matching = []
    matched_to_parent = [False] * num_vertices
    for vertex in order:
        child = chosen_child[vertex]
        if not matched_to_parent[vertex] and child != -1:
            matching.append((vertex, child))
            matched_to_parent[child] = True
    return matching


if __name__ == "__main__":
    import doctest

    doctest.testmod()
