# Dinic Algorithm


def bfs(matrix_capacity, matrix_flow, s, t):
    n = len(matrix_capacity)
    queue = [s]
    global level
    level = n * [0]
    level[s] = 1
    while queue:
        k = queue.pop(0)
        for i in range(n):
            if (matrix_flow[k][i] < matrix_capacity[k][i]) and (level[i] == 0):
                level[i] = level[k] + 1
                queue.append(i)
    return level[t] > 0


def dfs(matrix_capacity, matrix_flow, k, cp):
    tmp = cp
    if k == len(matrix_capacity) - 1:
        return cp
    for i in range(len(matrix_capacity)):
        if (level[i] == level[k] + 1) and (matrix_flow[k][i] < matrix_capacity[k][i]):
            f = dfs(matrix_capacity, matrix_flow, i, min(tmp, matrix_capacity[k][i] - matrix_flow[k][i]))
            matrix_flow[k][i] = matrix_flow[k][i] + f
            matrix_flow[i][k] = matrix_flow[i][k] - f
            tmp = tmp - f
    return cp - tmp


def max_flow(graph, s, t):
    n = len(graph)
    matrix_flow = [n * [0] for _ in range(n)]  # F is the flow matrix
    flow = 0
    while bfs(graph, matrix_flow, s, t):
        flow = flow + dfs(graph, matrix_flow, s, 100000)
    return flow


graph = [[0, 16, 13, 0, 0, 0],
         [0, 0, 10, 12, 0, 0],
         [0, 4, 0, 0, 14, 0, 0],
         [0, 0, 9, 0, 0, 20],
         [0, 0, 0, 7, 0, 4],
         [0, 0, 0, 0, 0, 0]]

source, sink = 0, 5
print(max_flow(graph, source, sink))
