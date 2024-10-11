from typing import NamedTuple


class Edge(NamedTuple):
    src: int
    dst: int
    weight: int


def print_distance_and_paths(distance: list[float], paths: list[list[int]], src: int):
    """
    Prints the shortest distance and paths from the source vertex to each vertex.
    """
    print(f"Vertex\tShortest Distance from Vertex {src}\tPath")
    for vertex, (dist, path) in enumerate(zip(distance, paths)):
        path_str = " -> ".join(map(str, path)) if path else "No path"
        print(f"{vertex}\t\t{dist}\t\t\t\t{path_str}")


def check_negative_cycle(
    graph: list[Edge], distance: list[float], predecessor: list[int]
) -> bool:
    """
    Checks if there is a negative weight cycle reachable from the source vertex.
    If found, return True, indicating a negative cycle.
    """
    for edge in graph:
        if (
            distance[edge.src] != float("inf")
            and distance[edge.src] + edge.weight < distance[edge.dst]
        ):
            # Update predecessors to indicate a cycle for affected paths
            # Use -1 as a marker for negative cycle detection
            predecessor[edge.dst] = -1
            return True
    return False


def reconstruct_paths(
    predecessor: list[int], vertex_count: int, src: int
) -> list[list[int]]:
    """
    Reconstructs the shortest paths from the source vertex to
    each vertex using the predecessor list.
    """
    paths = [[] for _ in range(vertex_count)]
    for vertex in range(vertex_count):
        if predecessor[vertex] == -1:
            paths[vertex] = ["Negative cycle detected"]
        elif predecessor[vertex] is not None:
            path = []
            current = vertex
            while current is not None:
                path.insert(0, current)
                if current == src:
                    break
                current = predecessor[current]
            paths[vertex] = path
    return paths


def bellman_ford(
    graph: list[Edge], vertex_count: int, src: int
) -> tuple[list[float], list[list[int]]]:
    """
    Returns the shortest paths from a vertex src to all other vertices,
    including path reconstruction.
    """
    distance = [float("inf")] * vertex_count
    predecessor = [None] * vertex_count  # Keeps track of the path predecessors
    distance[src] = 0.0

    # Step 1: Relax edges repeatedly
    for _ in range(vertex_count - 1):
        for edge in graph:
            if (
                distance[edge.src] != float("inf")
                and distance[edge.src] + edge.weight < distance[edge.dst]
            ):
                distance[edge.dst] = distance[edge.src] + edge.weight
                predecessor[edge.dst] = edge.src

    # Step 2: Check for negative weight cycles
    if check_negative_cycle(graph, distance, predecessor):
        raise Exception("Negative cycle found")

    # Step 3: Reconstruct paths from predecessor list
    paths = reconstruct_paths(predecessor, vertex_count, src)

    return distance, paths


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    try:
        V = int(input("Enter number of vertices: ").strip())
        E = int(input("Enter number of edges: ").strip())

        graph: list[Edge] = []

        for i in range(E):
            print(f"Edge {i + 1}")
            src, dest, weight = map(
                int, input("Enter source, destination, weight: ").strip().split()
            )
            if src < 0 or src >= V or dest < 0 or dest >= V:
                print(f"Invalid vertices: src and dest should be between 0 and {V - 1}")
                continue
            graph.append(Edge(src, dest, weight))

        source = int(input("\nEnter shortest path source vertex: ").strip())
        if source < 0 or source >= V:
            print(f"Invalid source: source should be between 0 and {V - 1}")
        else:
            shortest_distance, paths = bellman_ford(graph, V, source)
            print_distance_and_paths(shortest_distance, paths, source)
    except ValueError:
        print("Invalid input. Please enter valid integers.")
