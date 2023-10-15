import heapq

def dijkstra(graph, start):
    # Initialize distances dictionary with all vertices set to infinity
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0

    # Priority queue to keep track of the vertices to visit
    priority_queue = [(0, start)]

    while priority_queue:
        # Get the vertex with the smallest distance
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # If the current distance is greater than the known distance, skip it
        if current_distance > distances[current_vertex]:
            continue

        # Update the distances to neighbors
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # If this path is shorter than the known shortest path, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Get user input for the graph
graph = {}
num_vertices = int(input("Enter the number of vertices: "))

for _ in range(num_vertices):
    vertex = input("Enter a vertex: ")
    edges = input("Enter edges and weights (e.g., B 1 C 4): ").split()
    graph[vertex] = {edges[i]: int(edges[i+1]) for i in range(0, len(edges), 2)}

# Get the starting vertex from the user
start_vertex = input("Enter the starting vertex: ")

# Find the shortest distances from the starting vertex to all other vertices
shortest_distances = dijkstra(graph, start_vertex)

# Print the shortest distances
for vertex, distance in shortest_distances.items():
    print(f'Shortest distance from {start_vertex} to {vertex}: {distance}')
