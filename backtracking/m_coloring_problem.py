def is_safe(
    node: int,
    color: int,
    graph: list[list[int]],
    num_vertices: int,
    col: list[int],
) -> bool:
    """
    Check if it is safe to assign a color to a node.

    >>> is_safe(0, 1, [[0,1],[1,0]], 2, [0,1])
    False
    >>> is_safe(0, 2, [[0,1],[1,0]], 2, [0,1])
    True
    """
    return all(
        not (graph[node][k] == 1 and col[k] == color) for k in range(num_vertices)
    )


def solve(
    node: int,
    col: list[int],
    max_colors: int,
    num_vertices: int,
    graph: list[list[int]],
) -> bool:
    """
    Recursively try to color the graph using at most max_colors.

    >>> solve(0, [0]*3, 3, 3, [[0,1,0],[1,0,1],[0,1,0]])
    True
    >>> solve(0, [0]*3, 2, 3, [[0,1,0],[1,0,1],[0,1,0]])
    True
    """
    if node == num_vertices:
        return True
    for c in range(1, max_colors + 1):
        if is_safe(node, c, graph, num_vertices, col):
            col[node] = c
            if solve(node + 1, col, max_colors, num_vertices, graph):
                return True
            col[node] = 0
    return False


def graph_coloring(graph: list[list[int]], max_colors: int, num_vertices: int) -> bool:
    """
    Determine if the graph can be colored with at most max_colors.

    >>> graph_coloring([[0,1,1],[1,0,1],[1,1,0]], 3, 3)
    True
    >>> graph_coloring([[0,1,1],[1,0,1],[1,1,0]], 2, 3)
    False
    """
    col = [0] * num_vertices
    return solve(0, col, max_colors, num_vertices, graph)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    num_vertices = int(input("Enter vertices: "))
    num_edges = int(input("Enter edges: "))
    graph = [[0] * num_vertices for _ in range(num_vertices)]

    print("Enter edges (u v):")
    for _ in range(num_edges):
        try:
            u, v = map(int, input().split())
            if 0 <= u < num_vertices and 0 <= v < num_vertices:
                graph[u][v] = 1
                graph[v][u] = 1
            else:
                print("Invalid edge.")
        except ValueError:
            print("Invalid input.")

    max_colors = int(input("Enter max colors: "))

    if graph_coloring(graph, max_colors, num_vertices):
        print("Coloring possible.")
    else:
        print("Coloring not possible.")
