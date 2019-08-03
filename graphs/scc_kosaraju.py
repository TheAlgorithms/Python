from __future__ import print_function


def dfs(u):
    global g, r, scc, component, visit, stack
    if visit[u]: return
    visit[u] = True
    for v in g[u]:
        dfs(v)
    stack.append(u)

def dfs2(u):
    global g, r, scc, component, visit, stack
    if visit[u]: return
    visit[u] = True
    component.append(u)
    for v in r[u]:
        dfs2(v)

def kosaraju():
    global g, r, scc, component, visit, stack
    for i in range(n):
        dfs(i)
    visit = [False]*n
    for i in stack[::-1]:
        if visit[i]: continue
        component = []
        dfs2(i)
        scc.append(component)
    return scc


if __name__ == "__main__":
    # n - no of nodes, m - no of edges
    n, m = list(map(int,input().strip().split()))

    g = [[] for i in range(n)] #graph
    r = [[] for i in range(n)] #reversed graph
    # input graph data (edges)
    for i in range(m):
        u, v = list(map(int,input().strip().split()))
        g[u].append(v)
        r[v].append(u)

    stack = []
    visit = [False]*n
    scc = []
    component = []
    print(kosaraju())
