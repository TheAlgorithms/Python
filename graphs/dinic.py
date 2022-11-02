INF = float("inf")


class Dinic:
    def __init__(self, n):
        self.lvl = [0] * n
        self.ptr = [0] * n
        self.q = [0] * n
        self.adj = [[] for _ in range(n)]

    """
    Here we will add our edges containing with the following parameters:
    vertex closest to source, vertex closest to sink and flow capacity
    through that edge ...
    """

    def add_edge(self, a, b, c, rcap=0):
        self.adj[a].append([b, len(self.adj[b]), c, 0])
        self.adj[b].append([a, len(self.adj[a]) - 1, rcap, 0])

    # This is a sample depth first search to be used at max_flow
    def depth_first_search(self, vertex, sink, flow):
        if vertex == sink or not flow:
            return flow

        for i in range(self.ptr[vertex], len(self.adj[vertex])):
            e = self.adj[vertex][i]
            if self.lvl[e[0]] == self.lvl[vertex] + 1:
                p = self.depth_first_search(e[0], sink, min(flow, e[2] - e[3]))
                if p:
                    self.adj[vertex][i][3] += p
                    self.adj[e[0]][e[1]][3] -= p
                    return p
            self.ptr[vertex] = self.ptr[vertex] + 1
        return 0

    # Here we calculate the flow that reaches the sink
    def max_flow(self, source, sink):
        flow, self.q[0] = 0, source
        for l in range(31):  # l = 30 maybe faster for random data
            while True:
                self.lvl, self.ptr = [0] * len(self.q), [0] * len(self.q)
                qi, qe, self.lvl[source] = 0, 1, 1
                while qi < qe and not self.lvl[sink]:
                    v = self.q[qi]
                    qi += 1
                    for e in self.adj[v]:
                        if not self.lvl[e[0]] and (e[2] - e[3]) >> (30 - l):
                            self.q[qe] = e[0]
                            qe += 1
                            self.lvl[e[0]] = self.lvl[v] + 1

                p = self.depth_first_search(source, sink, INF)
                while p:
                    flow += p
                    p = self.depth_first_search(source, sink, INF)

                if not self.lvl[sink]:
                    break

        return flow


# Example to use

"""
Will be a bipartite graph, than it has the vertices near the source(4)
and the vertices near the sink(4)
"""
# Here we make a graphs with 10 vertex(source and sink includes)
graph = Dinic(10)
source = 0
sink = 9
"""
Now we add the vertices next to the font in the font with 1 capacity in this edge
(source -> source vertices)
"""
for vertex in range(1, 5):
    graph.add_edge(source, vertex, 1)
"""
We will do the same thing for the vertices near the sink, but from vertex to sink
(sink vertices -> sink)
"""
for vertex in range(5, 9):
    graph.add_edge(vertex, sink, 1)
"""
Finally we add the verices near the sink to the vertices near the source.
(source vertices -> sink vertices)
"""
for vertex in range(1, 5):
    graph.add_edge(vertex, vertex + 4, 1)

# Now we can know that is the maximum flow(source -> sink)
print(graph.max_flow(source, sink))
