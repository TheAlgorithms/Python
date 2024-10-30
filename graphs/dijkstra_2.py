from typing import List


def print_distances(distances: List[float]) -> None:
    print("\nVertex Distance")
    for vertex, distance in enumerate(distances):
        print(f"{vertex}\t{int(distance) if distance != float('inf') else 'INF'}")


def find_min_distance(distances: List[float], visited: List[bool]) -> int:
    min_distance = float("inf")
    min_index = -1

    for i in range(len(distances)):
        if not visited[i] and distances[i] < min_distance:
            min_distance = distances[i]
            min_index = i

    return min_index


def dijkstra(graph: List[List[float]], num_vertices: int, source: int) -> List[float]:
    distances = [float("inf")] * num_vertices
    visited = [False] * num_vertices
    distances[source] = 0

    for _ in range(num_vertices - 1):
        u = find_min_distance(distances, visited)
        visited[u] = True

        for v in range(num_vertices):
            if (
                not visited[v]
                and graph[u][v] != float("inf")
                and distances[u] + graph[u][v] < distances[v]
            ):
                distances[v] = distances[u] + graph[u][v]

    return distances


def is_connected(graph: List[List[float]], num_vertices: int) -> bool:
    visited = [False] * num_vertices
    stack = [0]  # Start DFS from the first vertex
    visited[0] = True

    while stack:
        node = stack.pop()
        for neighbor in range(num_vertices):
            if graph[node][neighbor] != float("inf") and not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)

    return all(visited)


def main() -> None:
    V = int(input("Enter number of vertices: ").strip())
    if V <= 0:
        print("Error: The number of vertices must be greater than 0.")
        return

    E = int(input("Enter number of edges (must be >= V-1): ").strip())
    if E < V - 1:
        print(
            f"Error: The number of edges must be at least {V - 1} for a connected graph."
        )
        return

    graph = [[float("inf")] * V for _ in range(V)]

    for i in range(V):
        graph[i][i] = 0.0

    for i in range(E):
        print(f"\nEdge {i + 1}")
        src = int(input(f"Enter source (0 to {V - 1}): ").strip())
        dst = int(input(f"Enter destination (0 to {V - 1}): ").strip())

        if src < 0 or src >= V or dst < 0 or dst >= V:
            print("Error: Source and destination must be valid vertex indices.")
            return

        weight = float(input("Enter weight (non-negative): ").strip())
        if weight < 0:
            print("Error: Weight must be non-negative.")
            return

        if src == dst:
            print(
                "Warning: Self-loop detected; it will be allowed but consider its implications."
            )

        # Handle duplicate edges: (optionally overwrite or warn)
        if graph[src][dst] != float("inf"):
            print("Warning: Duplicate edge detected; the weight will be updated.")

        graph[src][dst] = weight

    if not is_connected(graph, V):
        print(
            "Warning: The graph is not connected. Dijkstra's algorithm may not yield valid results for all vertices."
        )

    gsrc = int(input(f"\nEnter shortest path source (0 to {V - 1}): ").strip())
    if gsrc < 0 or gsrc >= V:
        print("Error: Source must be a valid vertex index.")
        return

    distances = dijkstra(graph, V, gsrc)
    print_distances(distances)


if __name__ == "__main__":
    main()
