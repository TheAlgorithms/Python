"""
https://en.wikipedia.org/wiki/Strongly_connected_component

Finding strongly connected components in directed graph

"""

test_graph_1 = {
    0: [2, 3],
    1: [0],
    2: [1],
    3: [4],
    4: [],
}

test_graph_2 = {
    0: [1, 2, 3],
    1: [2],
    2: [0],
    3: [4],
    4: [5],
    5: [3],
}


def topology_sort(graph: dict, vert: int, visited: list) -> list:
    """
    Use depth first search to sort graph
    At this time graph is the same as input
    >>> topology_sort(test_graph_1, 0, 5 * [False])
    [1, 2, 4, 3, 0]
    >>> topology_sort(test_graph_2, 0, 6 * [False])
    [2, 1, 5, 4, 3, 0]
    """

    visited[vert] = True
    order = []

    for neighbour in graph[vert]:
        if not visited[neighbour]:
            order += topology_sort(graph, neighbour, visited)

    order.append(vert)

    return order


def find_components(reversed_graph: dict, vert: int, visited: list) -> list:
    """
    Use depth first search to find strongliy connected
    vertices. Now graph is reversed
    >>> find_components({0: [1], 1: [2], 2: [0]}, 0, 5 * [False])
    [0, 1, 2]
    >>> find_components({0: [2], 1: [0], 2: [0, 1]}, 0, 6 * [False])
    [0, 2, 1]
    """

    visited[vert] = True
    component = [vert]

    for neighbour in reversed_graph[vert]:
        if not visited[neighbour]:
            component += find_components(reversed_graph, neighbour, visited)

    return component


def strongly_connected_components(graph: dict) -> list:
    """
    This function takes graph as a parameter
    and then returns the list of strongly connected components
    >>> strongly_connected_components(test_graph_1)
    [[0, 1, 2], [3], [4]]
    >>> strongly_connected_components(test_graph_2)
    [[0, 2, 1], [3, 5, 4]]
    """

    visited = len(graph) * [False]
    reversed_graph = {vert: [] for vert in range(len(graph))}

    for vert, neighbours in graph.items():
        for neighbour in neighbours:
            reversed_graph[neighbour].append(vert)

    order = []
    for i, was_visited in enumerate(visited):
        if not was_visited:
            order += topology_sort(graph, i, visited)

    components_list = []
    visited = len(graph) * [False]

    for i in range(len(graph)):
        vert = order[len(graph) - i - 1]
        if not visited[vert]:
            component = find_components(reversed_graph, vert, visited)
            components_list.append(component)

    return components_list


if __name__ == "__main__":
    import doctest

    doctest.testmod()
