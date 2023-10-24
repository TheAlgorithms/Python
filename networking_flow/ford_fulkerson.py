# Ford-Fulkerson Algorithm for Maximum Flow Problem
"""
Description:
    (1) Start with initial flow as 0;
    (2) Choose augmenting path from source to sink and add path to flow;
"""


def bfs(graph: list, s: int, t: int, parent: list) -> bool:
    """
    This function returns True if there is node that has not iterated.

    Args:
        graph (list): Adjacency matrix of graph
        s (int): Source
        t (int): Sink
        parent (list): Parent list

    Returns:
        bool: True if there is node that has not iterated.
    """

    visited = [False] * len(graph)  # Mark all nodes as not visited
    queue = []  # BFS queue

    # Source node
    queue.append(s)
    visited[s] = True

    while queue:
        # Pop the front node
        u = queue.pop(0)

        # Traverse all adjacent nodes of u
        for ind in range(len(graph[u])):
            if visited[ind] is False and graph[u][ind] > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u

    return visited[t]


def ford_fulkerson(graph: list, source: int, sink: int) -> int:
    """
    This function returns maximum flow from source to sink in given graph.

    Args:
        graph (list): Adjacency matrix of graph
        source (int): Source
        sink (int): Sink

    Returns:
        int: Maximum flow
    """

    # This array is filled by BFS and to store path
    parent = [-1] * (len(graph))
    max_flow = 0
    while bfs(graph, source, sink, parent):  # While there is path from source to sink
        path_flow = float("Inf")
        s = sink

        while s != source:
            # Find the minimum value in select path
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow
        v = sink

        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

    return max_flow


graph = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0],
]

source, sink = 0, 5
print(ford_fulkerson(graph, source, sink))
