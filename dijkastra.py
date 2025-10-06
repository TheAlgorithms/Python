import heapq

def dijkstra(graph, start):
    # Step 1: Initialize distances and priority queue
    distances = {node: float('inf') for node in graph}  # Initially all are infinity
    distances[start] = 0  # Distance to start node is 0
    priority_queue = [(0, start)]  # (distance, node)

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # If we already found a better path before, skip this one
        if current_distance > distances[current_node]:
            continue

        # Step 2: Explore neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Step 3: If found a shorter path to neighbor
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances
