"""Topological Sort."""

# Test cases:

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


def topological_sort_util(
    start: str, edges: dict[str, list[str]], visited: list[str], sort: list[str]
) -> list[str]:
    """"""
    """
    Examples:
    >>> topological_sort(['a', 'b', 'c', 'd'], {"a": ["b", "c"], "b": ["d"],
    "c": [], "d": []})
    ['d', 'c', 'b', 'a']
    >>> topological_sort(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], {"a": ["b"],
    "b": ["c"], "c": ["d"], "d": ["e"], "e": ["f"], "f": ["g"], "g": ["h"], "h": []})
    ['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
    >>> topological_sort(['a', 'b', 'c', 'd', 'e', 'f', 'g'], {"a": ["b", "c"],
    "b": ["d", "e"], "c": ["f", "g"], "d": [], "f": [], "h": []})
    ['d', 'f', 'e', 'g', 'c', 'b', 'a']
    >>> topological_sort([], {})
    ['']
    """

    current = start
    # add current to visited
    visited.append(current)
    neighbors = edges[current]
    for neighbor in neighbors:
        # if neighbor not in visited, visit
        if neighbor not in visited:
            sort = topological_sort_util(neighbor, edges, visited, sort)
    # if all neighbors visited add current to sort
    sort.append(current)
    # if all vertices haven't been visited select a new one to visit
    if len(visited) != len(edges):
        for vertex in edges:
            if vertex not in visited:
                sort = topological_sort_util(vertex, edges, visited, sort)
    # return sort
    return sort


def topological_sort(vertices: list[str], edges: dict[str, list[str]]) -> list[str]:
    sort: list[str] = []
    visited: list[str] = []
    for vertex in vertices:
        if vertex not in visited:
            sort = topological_sort_util(vertex, edges, visited, sort)
    return sort


if __name__ == "__main__":
    # Get vertices from the user
    vertices_input = input("Please enter the vertices separated by commas: ").strip()
    vertices = [vertex.strip() for vertex in vertices_input.split(",")]
    # Initialize an empty dictionary for edges
    edges = {}
    # Iterate over each vertex to get its connected edges
    for vertex in vertices:
        edges_input = input(
            f'Please enter the edges connected to vertex "{vertex}" '
            "separated by commas (leave empty to finish): "
        ).strip()
        edges[vertex] = [
            edge.strip() for edge in edges_input.split(",") if edge.strip()
        ]
    sort = topological_sort(vertices, edges)
    print(sort)
