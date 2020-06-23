# Check whether Graph is Bipartite or Not using DFS


# A Bipartite Graph is a graph whose vertices can be divided into two independent sets,
# U and V such that every edge (u, v) either connects a vertex from U to V or a vertex
# from V to U. In other words, for every edge (u, v), either u belongs to U and v to V,
# or u belongs to V and v to U. We can also say that there is no edge that connects
# vertices of same set.
def check_bipartite_dfs(graph):
    visited = [False] * len(graph)
    color = [-1] * len(graph)

    def dfs(v, c):
        visited[v] = True
        color[v] = c
        for u in graph[v]:
            if not visited[u]:
                dfs(u, 1 - c)

    for i in range(len(graph)):
        if not visited[i]:
            dfs(i, 0)

    for i in range(len(graph)):
        for j in graph[i]:
            if color[i] == color[j]:
                return False

    return True


# Adjacency list of graph
graph = {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2], 4: []}
print(check_bipartite_dfs(graph))
