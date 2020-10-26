"""
Problem :
Calculate the betweenness centrality of the nodes of the given network

# Referred from  --  https://www.tandfonline.com/doi/pdf/
10.1080/0022250X.2001.9990249?casa_token=8e49ocuxFIUAAAAA:
HEPb9CcZA8S2emOiip9Cmdtz7amfQCnt0FDiwCho8W_8r-OPeLDSM7X8rqomd3PICwv7VFWMIPck

In general, centrality identifies the most important vertices of the graph.
There are various measures for centrality of a node in the network
For more details : https://en.wikipedia.org/wiki/Betweenness_centrality

Formula :

for node i, B(i) = (2/(n−1)(n−2)) * sum(n_st/g_st)
where n_st is the number of shortest paths between nodes s and t which pass through i
and gst is the total number of shortest paths between nodes s and t

Brandes' Algorithm :
As it involves finding shortest path between all paurs of vertices,
which takes O(|V|^3) time with the Floyd–Warshall algorithm,
On unweighted graphs, calculating betweenness centrality takes
O(|V||E|) time using Brandes' algorithm
"""


def betweenness_centrality():

    n = len(adj)
    betweenness_centrality = [0 for _ in range(n)]

    for s in range(n):
        # iterate through all nodes in graph to calculate
        # single-source shortest paths for each vertex
        stack = []
        p = [[] for _ in range(n)]
        sigma = [0 for _ in range(n)]
        sigma[s] = 1

        # distance from node s
        d = [-1 for _ in range(n)]
        d[s] = 0

        queue = []
        queue.append(s)

        while queue:
            v = queue[0]
            queue.pop(0)
            stack.append(v)
            for w in adj[v]:
                # w found for first time
                if d[w] < 0:
                    queue.append(w)
                    d[w] = d[v] + 1

                # shortest path to w passes through v
                if d[w] == d[v] + 1:
                    sigma[w] += sigma[v]
                    p[w].append(v)

        # dependencies of the source on each other vertex are added
        # to the centrality score of that vertex
        delta = [0 for _ in range(n)]
        while stack:
            w = stack[-1]
            stack.pop(-1)
            for v in p[w]:
                delta[v] += (sigma[v] / sigma[w]) * (1 + delta[w])
            if not w == s:
                betweenness_centrality[w] += delta[w]

    # normalize - divide by no of pairs -> (n-1)*(n-2) / 2
    # divide by 2, because in Brandes’ algorithm all shortest paths are considered twice
    for i in range(n):
        betweenness_centrality[i] *= 1 / ((n - 1) * (n - 2))

    return betweenness_centrality


if __name__ == "__main__":
    global adj
    adj = [[] for _ in range(5)]

    adj[0] = [1, 3]
    adj[1] = [0, 2, 4]
    adj[2] = [1]
    adj[3] = [0, 4]
    adj[4] = [1, 3]

    betweenness_centrality = betweenness_centrality()
    print("Betweenness centrality : {}".format(betweenness_centrality))
