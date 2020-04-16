# Finding longest distance in Directed Acyclic Graph using KahnsAlgorithm
def longestDistance(l):
    indegree = [0] * len(l)
    queue = []
    longDist = [1] * len(l)

    for key, values in l.items():
        for i in values:
            indegree[i] += 1

    for i in range(len(indegree)):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        vertex = queue.pop(0)
        for x in l[vertex]:
            indegree[x] -= 1

            if longDist[vertex] + 1 > longDist[x]:
                longDist[x] = longDist[vertex] + 1

            if indegree[x] == 0:
                queue.append(x)

    print(max(longDist))


# Adjacency list of Graph
l = {0: [2, 3, 4], 1: [2, 7], 2: [5], 3: [5, 7], 4: [7], 5: [6], 6: [7], 7: []}
longestDistance(l)
