# Finding Articulation Points in Undirected Graph
def compute_ap(l):  # noqa: E741
    n = len(l)
    out_edge_count = 0
    low = [0] * n
    visited = [False] * n
    is_art = [False] * n

    def dfs(root, at, parent, out_edge_count):
        if parent == root:
            out_edge_count += 1
        visited[at] = True
        low[at] = at

        for to in l[at]:
            if to == parent:
                pass
            elif not visited[to]:
                out_edge_count = dfs(root, to, at, out_edge_count)
                low[at] = min(low[at], low[to])

                # AP found via bridge
                if at < low[to]:
                    is_art[at] = True
                # AP found via cycle
                if at == low[to]:
                    is_art[at] = True
            else:
                low[at] = min(low[at], to)
        return out_edge_count

    for i in range(n):
        if not visited[i]:
            out_edge_count = 0
            out_edge_count = dfs(i, i, -1, out_edge_count)
            is_art[i] = out_edge_count > 1

    for x in range(len(is_art)):
        if is_art[x] is True:
            print(x)


# Adjacency list of graph
data = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3, 5],
    3: [2, 4],
    4: [3],
    5: [2, 6, 8],
    6: [5, 7],
    7: [6, 8],
    8: [5, 7],
}
compute_ap(data)
