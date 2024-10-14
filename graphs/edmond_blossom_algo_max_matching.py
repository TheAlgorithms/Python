from collections import deque

# Function to find the augmenting path in the graph using BFS
def find_augmenting_path(graph, matching, dist, u, parent):
    queue = deque([u])
    dist[u] = 0

    while queue:
        u = queue.popleft()

        for v in graph[u]:
            if matching[v] is None:  # Found an augmenting path
                parent[v] = u
                return v

            if dist[matching[v]] is None:
                dist[matching[v]] = dist[u] + 1
                parent[matching[v]] = u
                queue.append(matching[v])

    return None

# Function to trace back the augmenting path and update the matching
def augment_path(matching, parent, v):
    while v is not None:
        u = parent[v]
        matching[v] = u
        matching[u] = v
        v = parent[u]

# Main function implementing Edmonds' Blossom Algorithm
def edmonds_blossom(graph, n):
    matching = [None] * n  # None indicates unmatched vertices

    for u in range(n):
        if matching[u] is None:  # Try to match this vertex
            dist = [None] * n
            parent = [None] * n

            v = find_augmenting_path(graph, matching, dist, u, parent)
            if v is not None:
                augment_path(matching, parent, v)

    return matching

# Example usage
if __name__ == "__main__":
    # Example graph: adjacency list representation
    graph = {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1],
        3: [1],
        4: [5],
        5: [4]
    }

    n = len(graph)
    matching = edmonds_blossom(graph, n)

    # Print the matching
    print("Maximum Matching:")
    for u in range(n):
        if matching[u] is not None and u < matching[u]:
            print(f"{u} -- {matching[u]}")
