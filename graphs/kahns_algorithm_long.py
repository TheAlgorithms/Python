# Finding longest distance in Directed Acyclic Graph using KahnsAlgorithm
def longest_distance(graph):
    indegree = [0] * len(graph)
    queue = []
    long_dist = [1] * len(graph)

    for key, values in graph.items():
        for i in values:
            indegree[i] += 1

    for i in range(len(indegree)):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        vertex = queue.pop(0)
        for x in graph[vertex]:
            indegree[x] -= 1

            if long_dist[vertex] + 1 > long_dist[x]:
                long_dist[x] = long_dist[vertex] + 1

            if indegree[x] == 0:
                queue.append(x)

    print(max(long_dist))


# Adjacency list of Graph
graph = {0: [2, 3, 4], 1: [2, 7], 2: [5], 3: [5, 7], 4: [7], 5: [6], 6: [7], 7: []}
longest_distance(graph)
