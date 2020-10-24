"""
Problem :
Calculate the closeness centrality of the nodes of the given network

In general, centrality identifies the most important vertices of the graph.
For more details : https://en.wikipedia.org/wiki/Closeness_centrality

Formula :
let C(x) be the closeness centrality of the node x.
C(x) = (N-1) / (sum of shortest paths between x & all nodes in the graph)
"""


def bfs(x: int) -> int:
    """
    Does BFS traversal from node x
    Returns the sum of all shortest distances
    """

    sum_d = 0

    # store the shortest distance from x
    d = [-1 for _ in range(len(adj))]

    # queue
    queue = []
    queue.append(x)
    d[x] = 0

    while len(queue) != 0:
        front = queue[0]
        queue.pop(0)
        for v in adj[front]:
            if d[v] == -1:
                queue.append(v)
                d[v] = d[front] + 1
                sum_d += d[v]

    return sum_d


def closeness_centrality():
    """
    calculates the closeness centrality

    Returns:
    A list containing the closeness centrality of all nodes
    """

    n = len(adj)
    closeness_centrality = []
    for i in range(len(adj)):
        closeness_centrality.append((n - 1) / bfs(i))

    return closeness_centrality


if __name__ == "__main__":
    global adj
    adj = [[] for _ in range(5)]

    adj[0] = [1, 3]
    adj[1] = [0, 2, 4]
    adj[2] = [1]
    adj[3] = [0, 4]
    adj[4] = [1, 3]

    closeness_centrality = closeness_centrality()
    print("Closeness centrality : {}".format(closeness_centrality))
