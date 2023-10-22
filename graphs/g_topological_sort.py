# Author: Phyllipe Bezerra (https://github.com/pmba)

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


def print_stack(stack, clothes):
    """Prints the clothes in the order they should be worn."""
    order = 1
    while stack:
        current_clothing = stack.pop()
        print(order, clothes[current_clothing])
        order += 1


def depth_first_search(u, visited, graph, stack):
    """
    A depth first search starting from vertex u.

    Doctest:
    >>> visited = [0 for _ in range(len(graph))]
    >>> stack = []
    >>> depth_first_search(0, visited, graph, stack)
    >>> stack
    [3, 2, 4, 1, 0]
    """
    visited[u] = 1
    for v in graph[u]:
        if not visited[v]:
            depth_first_search(v, visited, graph, stack)

    stack.append(u)


def topological_sort(graph):
    """
    Performs a topological sort on the graph.

    Doctest:
    >>> stack = topological_sort(graph)
    >>> stack
    [3, 2, 4, 1, 0, 5, 7, 6, 8]
    """
    visited = [0 for _ in range(len(graph))]
    stack = []
    for v in range(len(graph)):
        if not visited[v]:
            depth_first_search(v, visited, graph, stack)
    return stack


if __name__ == "__main__":
    result = topological_sort(graph)
    print(result)
    print_stack(result, clothes)
    import doctest

    doctest.testmod()
