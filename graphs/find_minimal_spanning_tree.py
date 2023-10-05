class Vertex:
    def __init__(self, name):
        self.name = name
        self.edges = []

    def addEdge(self, vertex, weight=0):
        self.edges.append((vertex, weight))


class Graph:
    def __init__(self, num_vertices):
        self.vertices = {}
        self.num_vertices = num_vertices

    def addVertex(self, vertex):
        new_vertex = Vertex(vertex)
        self.vertices[vertex] = new_vertex

    def addEdge(self, vertex1, vertex2, weight=0):
        if vertex1 not in self.vertices:
            self.addVertex(vertex1)
        if vertex2 not in self.vertices:
            self.addVertex(vertex2)
        
        self.vertices[vertex1].addEdge(vertex2, weight)
        self.vertices[vertex2].addEdge(vertex1, weight)
        
    def printGraph(self):
        for vertex_name in self.vertices:
            vertex = self.vertices[vertex_name]
            print(f"Vertex {vertex_name}:")
            for edge in vertex.edges:
                print(f"  -> {edge[0]} (weight={edge[1]})")
                
    def find_minimum_spanning_tree(self):
        start_vertex = list(self.vertices.keys())[0]
        visited = {start_vertex}
        minimum_spanning_tree = Graph(len(self.vertices))
        total_cost = 0

        while len(visited) < len(self.vertices):
            min_weight = float('inf')
            min_edge = None

            for vertex in visited:
                for neighbor, weight in self.vertices[vertex].edges:
                    if neighbor not in visited and weight < min_weight:
                        min_weight = weight
                        min_edge = (vertex, neighbor, weight)

            vertex1, vertex2, weight = min_edge
            minimum_spanning_tree.addEdge(vertex1, vertex2, weight)
            total_cost += weight

            visited.add(vertex2)

        return total_cost
    

R, C = map(int, input().split())

g = Graph(R)

while C > 0:
    V, W, P = map(int, input().split())
    g.addEdge(V, W, P)
        
    C = C - 1
    
total_cable_cost = g.find_minimum_spanning_tree()
print(total_cable_cost)