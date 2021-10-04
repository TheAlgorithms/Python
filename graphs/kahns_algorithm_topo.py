def topologicalSort(graph: dict) -> list:
    """
    Kahn's Algorithm is used to find Topological ordering of Directed Acyclic Graph
    using BFS

    Return topologically sorted node list of graph
    >>> topologicalSort({0: [1, 2], 1: [3], 2: [3], 3: [4, 5], 4: [], 5: []})
    [0, 1, 2, 3, 4, 5]
    >>> topologicalSort({0: [1, 2], 1: [0, 3], 2: [3], 3: [4, 5], 4: [], 5: []})
    Traceback (most recent call last):
    ValueError: Cycle exists in graph
    """
    in_degree = [0] * len(graph)
    queue = []
    topo_sorted = []
    count = 0

    # graph array contains out_nodes of i-th node. calculating in_degree of each node from this information
    for key, values in graph.items():
        for i in values:
            in_degree[i] += 1

    for i in range(len(in_degree)):
        if in_degree[i] == 0:
            queue.append(i)

    while (
        queue
    ):  # keep iterating until all the nodes with zero in_deg has been processed
        vertex = queue.pop(0)
        count += 1
        topo_sorted.append(vertex)  # every time we deque a node from to_process, that means
        # the returned node has zero in_deg so it can go into the topo list
        for node in graph[vertex]:
            in_degree[
                node
            ] -= 1  # now that we have added current_node into sorted list we can
            # decrease in_degree of every node that depends on it by 1
            if in_degree[node] == 0:
                queue.append(
                    node
                )  # if the node that we decreased in_degree of has reached zero in_degree,
                # that means this node is ready to be processed and added to topo list

    # if the graph contained any cycle in_degree of some of the nodes will never
    # be zero so length of sorted list will be smaller than nodes on the graph
    if count != len(graph):
        raise ValueError("Cycle exists in graph")
    else:
        return topo_sorted


# Adjacency List of Graph
graph = {0: [1, 2], 1: [3], 2: [3], 3: [4, 5], 4: [], 5: []}
print(topologicalSort(graph))
