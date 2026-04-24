# Minimum cut on Ford_Fulkerson algorithm.

from collections import deque

test_graph = [
    [0, 16, 13, 0, 0, 0],
    [0, 0, 10, 12, 0, 0],
    [0, 4, 0, 0, 14, 0],
    [0, 0, 9, 0, 0, 20],
    [0, 0, 0, 7, 0, 4],
    [0, 0, 0, 0, 0, 0],
]


def bfs(graph, s, t, parent):
    visited = [False] * len(graph)
    queue = deque([s])
    visited[s] = True

    while queue:
        u = queue.popleft()

        for ind in range(len(graph[u])):
            if not visited[ind] and graph[u][ind] > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u

                # Early exit if sink is found
                if ind == t:
                    return True

    return visited[t]


def dfs(graph, s, visited):
    visited[s] = True
    for i in range(len(graph)):
        if graph[s][i] > 0 and not visited[i]:
            dfs(graph, i, visited)


def mincut(graph, source, sink):
    """
    Returns max_flow and minimum cut edges.

    >>> mincut(test_graph, source=0, sink=5)
    (23, [(1, 3), (4, 3), (4, 5)])
    """
    residual = [i[:] for i in graph]
    parent = [-1] * len(graph)
    max_flow = 0

    while bfs(residual, source, sink, parent):
        path_flow = float("Inf")
        s = sink

        while s != source:
            path_flow = min(path_flow, residual[parent[s]][s])
            s = parent[s]

        max_flow += path_flow

        v = sink
        while v != source:
            u = parent[v]
            residual[u][v] -= path_flow
            residual[v][u] += path_flow
            v = parent[v]

    visited = [False] * len(graph)
    dfs(residual, source, visited)

    res = []
    for i in range(len(graph)):
        for j in range(len(graph)):
            if visited[i] and not visited[j] and graph[i][j] > 0:
                res.append((i, j))

    return max_flow, res


if __name__ == "__main__":
    print(mincut(test_graph, source=0, sink=5))
