# Check whether Graph is Bipartite or Not using DFS

# A Bipartite Graph is a graph whose vertices can be divided into two independent sets,
# U and V such that every edge (u, v) either connects a vertex from U to V or a vertex
# from V to U. In other words, for every edge (u, v), either u belongs to U and v to V,
# or u belongs to V and v to U. We can also say that there is no edge that connects
# vertices of same set.
def check_bipartite_dfs(l):
    visited = [False] * len(l)
    color = [-1] * len(l)

    def dfs(v, c):
        visited[v] = True
        color[v] = c
        for u in l[v]:
            if not visited[u]:
                dfs(u, 1 - c)

    for i in range(len(l)):
        if not visited[i]:
            dfs(i, 0)

    for i in range(len(l)):
        for j in l[i]:
            if color[i] == color[j]:
                return False

    return True


# Adjacency list of graph
l = {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2], 4: []}
print(check_bipartite_dfs(l))
