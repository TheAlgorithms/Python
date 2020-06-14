'''
https://en.wikipedia.org/wiki/Component_(graph_theory)

Finding connected components in graph

'''

test_graph_1 = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1],
    4: [5, 6],
    5: [4, 6],
    6: [4, 5],
}

test_graph_2 = {
    0: [1, 2, 3],
    1: [0, 3],
    2: [0],
    3: [0, 1],
    4: [],
    5: [],
}


def dfs(graph, vert, visited):
    """
    Use depth first search to find all vertexes
    being in the same component as initial vertex
    """

    visited[vert] = True

    connected_verts = []

    # iterate over neighbours and
    # call the same function for not-visited vertexes
    for neighbour in graph[vert]:
        if not visited[neighbour]:
            connected_verts += dfs(graph, neighbour, visited)

    return [vert] + connected_verts


def connected_components(graph):
    """
    This function takes graph as a parameter
    and then returns the list of connected components
    >>> connected_components(test_graph_1)
    [[0, 1, 3, 2], [4, 5, 6]]
    >>> connected_components(test_graph_2)
    [[0, 1, 3, 2], [4], [5]]
    """

    n = len(graph)

    visited = n * [False]

    components_list = []

    # for each unused vertexes
    # we have to call dfs function
    # and get its components
    for i in range(n):
        if not visited[i]:
            i_connected = dfs(graph, i, visited)
            # when we get components append them to answer list
            components_list.append(i_connected)

    return components_list


if __name__ == "__main__":
    import doctest
    doctest.testmod()
