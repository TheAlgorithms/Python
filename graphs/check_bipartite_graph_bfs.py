# Check whether Graph is Bipartite or Not using BFS


# A Bipartite Graph is a graph whose vertices can be divided into two independent sets,
# U and V such that every edge (u, v) either connects a vertex from U to V or a vertex
# from V to U. In other words, for every edge (u, v), either u belongs to U and v to V,
# or u belongs to V and v to U. We can also say that there is no edge that connects
# vertices of same set.
def checkBipartite(graph):
    queue = []
    visited = [False] * len(graph)
    color = [-1] * len(graph)

    def bfs():
        while queue:
            u = queue.pop(0)
            visited[u] = True

            for neighbour in graph[u]:

                if neighbour == u:
                    return False

                if color[neighbour] == -1:
                    color[neighbour] = 1 - color[u]
                    queue.append(neighbour)

                elif color[neighbour] == color[u]:
                    return False

        return True

    for i in range(len(graph)):
        if not visited[i]:
            queue.append(i)
            color[i] = 0
            if bfs() is False:
                return False

    return True


if __name__ == "__main__":
    # Adjacency List of graph
    print(checkBipartite({0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2]}))
