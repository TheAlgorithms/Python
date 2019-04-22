"""pseudo-code"""

"""
DIJKSTRA(graph G, start vertex s,destination vertex d):
// all nodes initially unexplored
let H = min heap data structure, initialized with 0 and s [here 0 indicates the distance from start vertex]
while H is non-empty:
    remove the first node and cost of H, call it U and cost
    if U is not explored
    mark U as explored
    if U is d:
        return cost // total cost from start to destination vertex
    for each edge(U, V): c=cost of edge(u,V) // for V in graph[U]
        if V unexplored:
            next=cost+c
            add next,V to H (at the end)
"""
import heapq


def dijkstra(graph, start, end):
    heap = [(0, start)]  # cost from start node,end node
    visited = []
    while heap:
        (cost, u) = heapq.heappop(heap)
        if u in visited:
            continue
        visited.append(u)
        if u == end:
            return cost
        for v, c in G[u]:
            if v in visited:
                continue
            next = cost + c
            heapq.heappush(heap, (next, v))
    return (-1, -1)


G = {'A': [['B', 2], ['C', 5]],
     'B': [['A', 2], ['D', 3], ['E', 1]],
     'C': [['A', 5], ['F', 3]],
     'D': [['B', 3]],
     'E': [['B', 1], ['F', 3]],
     'F': [['C', 3], ['E', 3]]}

shortDistance = dijkstra(G, 'E', 'C')
print(shortDistance)
