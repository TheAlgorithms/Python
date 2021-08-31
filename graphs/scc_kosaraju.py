from typing import List


def dfs(u):
    global graph, reversedGraph, scc, component, visit, stack
    if visit[u]:
        return
    visit[u] = True
    for v in graph[u]:
        dfs(v)
    stack.append(u)


def dfs2(u):
    global graph, reversedGraph, scc, component, visit, stack
    if visit[u]:
        return
    visit[u] = True
    component.append(u)
    for v in reversedGraph[u]:
        dfs2(v)


def kosaraju():
    global graph, reversedGraph, scc, component, visit, stack
    for i in range(n):
        dfs(i)
    visit = [False] * n
    for i in stack[::-1]:
        if visit[i]:
            continue
        component = []
        dfs2(i)
        scc.append(component)
    return scc


if __name__ == "__main__":
    # n - no of nodes, m - no of edges
    n, m = list(map(int, input().strip().split()))

    graph: List[List[int]] = [[] for i in range(n)]  # graph
    reversedGraph: List[List[int]] = [[] for i in range(n)]  # reversed graph
    # input graph data (edges)
    for i in range(m):
        u, v = list(map(int, input().strip().split()))
        graph[u].append(v)
        reversedGraph[v].append(u)

    stack: List[int] = []
    visit: List[bool] = [False] * n
    scc: List[int] = []
    component: List[int] = []
    print(kosaraju())
