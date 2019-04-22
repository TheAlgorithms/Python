# Finding Bridges in Undirected Graph
def computeBridges(l):
    id = 0
    n = len(l) # No of vertices in graph
    low = [0] * n
    visited = [False] * n

    def dfs(at, parent, bridges, id):
        visited[at] = True
        low[at] = id
        id += 1
        for to in l[at]:
            if to == parent:
                pass
            elif not visited[to]:
                dfs(to, at, bridges, id)
                low[at] = min(low[at], low[to])
                if at < low[to]:
                    bridges.append([at, to])
            else:
                # This edge is a back edge and cannot be a bridge
                low[at] = min(low[at], to)

    bridges = []
    for i in range(n):
        if (not visited[i]):
            dfs(i, -1, bridges, id)
    print(bridges)
            
l = {0:[1,2], 1:[0,2], 2:[0,1,3,5], 3:[2,4], 4:[3], 5:[2,6,8], 6:[5,7], 7:[6,8], 8:[5,7]}
computeBridges(l)
