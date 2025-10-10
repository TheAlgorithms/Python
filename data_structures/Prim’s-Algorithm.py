import heapq


def prim_mst(graph, start=0):
    visited = set()
    mst = []
    total_cost = 0

    # Min-heap (cost, current_node, next_node)
    edges = [(0, start, start)]

    while edges:
        cost, u, v = heapq.heappop(edges)
        if v in visited:
            continue
        visited.add(v)
        total_cost += cost
        if u != v:
            mst.append((u, v, cost))
        for neighbor, weight in graph[v]:
            if neighbor not in visited:
                heapq.heappush(edges, (weight, v, neighbor))

    return mst, total_cost


# Example Graph as adjacency list
graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8)],
    4: [(1, 5), (2, 7)],
}

mst, cost = prim_mst(graph)
print("Edges in MST:", mst)
print("Total Cost:", cost)
