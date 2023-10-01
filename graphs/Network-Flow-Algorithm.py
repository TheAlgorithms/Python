from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v, capacity):
        self.graph[u].append({'v': v, 'capacity': capacity, 'reverseEdge': len(self.graph[v])})
        self.graph[v].append({'v': u, 'capacity': 0, 'reverseEdge': len(self.graph[u]) - 1})

    def BFS(self, s, t, parent):
        visited = [False] * self.V
        queue = deque()
        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.popleft()
            for edge in self.graph[u]:
                v = edge['v']
                capacity = edge['capacity']
                if visited[v] is False and capacity > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = (u, self.graph[u].index(edge))

        return visited[t]

    def EdmondsKarp(self, source, sink):
        parent = [-1] * self.V
        max_flow = 0

        while self.BFS(source, sink, parent):
            path_flow = float('inf')
            s = sink

            while s != source:
                u, idx = parent[s]
                edge = self.graph[u][idx]
                path_flow = min(path_flow, edge['capacity'])
                s = u

            max_flow += path_flow
            v = sink

            while v != source:
                u, idx = parent[v]
                self.graph[u][idx]['capacity'] -= path_flow
                self.graph[v][self.graph[u][idx]['reverseEdge']]['capacity'] += path_flow
                v = u

        return max_flow

if __name__ == "__main__":
    g = Graph(6)
    g.addEdge(0, 1, 16)
    g.addEdge(0, 2, 13)
    g.addEdge(1, 2, 10)
    g.addEdge(1, 3, 12)
    g.addEdge(2, 1, 4)
    g.addEdge(2, 4, 14)
    g.addEdge(3, 2, 9)
    g.addEdge(3, 5, 20)
    g.addEdge(4, 3, 7)
    g.addEdge(4, 5, 4)

    source = 0
    sink = 5
    max_flow = g.EdmondsKarp(source, sink)
    print(f"Max Flow from {source} to {sink}: {max_flow}")
