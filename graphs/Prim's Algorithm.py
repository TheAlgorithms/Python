def prim(graph):
    mst = [[] for i in range(0, len(graph))]
    inTree = {0}
    minCost = None

    while len(inTree) != len(graph):
        minCost = None
        for node in inTree:
            for connections in graph[node]:
                if minCost is None:
                    minCost = (node, connections)
                elif connections[1] < minCost[1][1] and connections[0] not in inTree:
                    minCost = (node, connections)

        mst[minCost[0]].append(minCost[1])
        mst[minCost[1][0]].append((minCost[0], minCost[1][1]))
        inTree.add(minCost[1][0])

    return mst


graph = [
    [(1, 5), (2, 4), (3, 10), (4, 2)],
    [(0, 5), (3, 3)],
    [(0, 4), (4, 3), (5, 7)],
    [(0, 10), (1, 3), (4, 6)],
    [(3, 6), (0, 2), (2, 3), (5, 4)],
    [(2, 7), (4, 4)],
]
for i in prim(graph):
    print(i)
