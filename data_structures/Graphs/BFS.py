import collections
from collections import defaultdict

# This class represents a directed graph using
# adjacency list representation


class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def adjacency(self):
        print(self.graph)

    # BFS algorithm
    def bfs(self, source):

        visited, queue = set(), collections.deque([source])
        visited.add(source)

        while queue:

            # Dequeue a vertex from queue
            vertex = queue.popleft()
            print(str(vertex) + " ", end="")

            # If not visited, mark it as visited, and
            # enqueue it
            for neighbour in self.graph[vertex]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

    def shortest_path(self, source, dest):

        if source == dest:
            return [source]

        visited, queue = set(), collections.deque([(source, [])])
        visited.add(source)

        while queue:

            # Dequeue a vertex from queue
            vertex, path = queue.popleft()
            # print(str(vertex) + " ", end="")

            # If not visited, mark it as visited, and
            # enqueue it
            for neighbour in self.graph[vertex]:
                if neighbour == dest:
                    return path + [vertex, neighbour]

                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append((neighbour, path + [vertex]))
        return "No path found."
    #     Time Complexity : O(V + E)
    #     Auxiliary Space : O(V)


# Driver code
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.adjacency()
print("Following is BFS from (starting from vertex 2)")
g.bfs(0)
print(g.shortest_path(0, 5))
