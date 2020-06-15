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


def find_components(reverse_graph: dict, vert: int, visited: list) -> list:
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

    for neighbour in reverse_graph[vert]:
        if not visited[neighbour]:
            component += find_components(reverse_graph, neighbour, visited)

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

    n = len(graph)

    visited = n * [False]

    # describe reversed graph (All edges reversed)
    reverse_graph = {vert: [] for vert in range(n)}

    for vert, neighbours in graph.items():
        for neighbour in neighbours:
            reverse_graph[neighbour].append(vert)

    order = []

    # topology sort
    for i in range(n):
        if not visited[i]:
            order += topology_sort(graph, i, visited)
            # print(order, 'aeee\n')

    # answer list
    components_list = []
    # reinitialize visited list
    visited = n * [False]

    # finding stongly connected components
    for i in range(n):
        vert = order[n - i - 1]
        if not visited[vert]:
            component = find_components(reverse_graph, vert, visited)
            components_list.append(component)

    return components_list


if __name__ == "__main__":

    import doctest

    doctest.testmod()
