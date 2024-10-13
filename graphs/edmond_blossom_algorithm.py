from collections import deque, defaultdict

UNMATCHED = -1  # Constant to represent unmatched vertices

class EdmondsBlossomAlgorithm:

    @staticmethod
    def maximum_matching(edges, vertex_count):
        """
        Finds the maximum matching in a general graph using Edmonds' Blossom Algorithm.

        :param edges: List of edges in the graph (each edge is a tuple of two vertices).
        :param vertex_count: The number of vertices in the graph.
        :return: A list of matched pairs of vertices (tuples).
        """
        # Initialize the adjacency list for the graph
        graph = defaultdict(list)

        # Populate the graph with the edges
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Initialize matching array and other auxiliary structures
        match = [UNMATCHED] * vertex_count  # Stores matches for each vertex, initially unmatched
        parent = [UNMATCHED] * vertex_count  # Tracks the parent of each vertex in the augmenting path
        base = list(range(vertex_count))  # Base of each vertex (initially the vertex itself)
        in_blossom = [False] * vertex_count  # Marks if a vertex is part of a blossom
        in_queue = [False] * vertex_count  # Marks if a vertex is already in the BFS queue

        # Iterate over each vertex to start the matching process
        for u in range(vertex_count):
            if match[u] == UNMATCHED:  # Proceed only if the vertex is unmatched
                # Reset auxiliary data structures for BFS
                parent = [UNMATCHED] * vertex_count
                base = list(range(vertex_count))  # Each vertex is its own base initially
                in_blossom = [False] * vertex_count
                in_queue = [False] * vertex_count

                queue = deque([u])  # Initialize BFS queue
                in_queue[u] = True  # Mark u as in the queue

                augmenting_path_found = False  # Flag to track if an augmenting path is found

                # BFS to find augmenting paths
                while queue and not augmenting_path_found:
                    current = queue.popleft()  # Get the next vertex from the queue

                    for y in graph[current]:
                        # Skip if this edge is the current matching
                        if match[current] == y:
                            continue

                        # Avoid self-loops
                        if base[current] == base[y]:
                            continue

                        # Case 1: y is unmatched, we found an augmenting path
                        if parent[y] == UNMATCHED:
                            if match[y] == UNMATCHED:
                                parent[y] = current
                                augmenting_path_found = True
                                EdmondsBlossomAlgorithm.update_matching(match, parent, y)  # Augment the path
                                break

                            # Case 2: y is matched, add y's match to the queue
                            z = match[y]
                            parent[y] = current
                            parent[z] = y
                            if not in_queue[z]:
                                queue.append(z)
                                in_queue[z] = True
                        else:
                            # Case 3: A cycle (blossom) is detected
                            base_u = EdmondsBlossomAlgorithm.find_base(base, parent, current, y)
                            if base_u != UNMATCHED:
                                aux_data = BlossomAuxData(queue, parent, base, in_blossom, match, in_queue)
                                EdmondsBlossomAlgorithm.contract_blossom(BlossomData(aux_data, current, y, base_u))

        # Collect the final matching result
        matching_result = []
        for v in range(vertex_count):
            if match[v] != UNMATCHED and v < match[v]:
                matching_result.append((v, match[v]))

        return matching_result

    @staticmethod
    def update_matching(match, parent, u):
        """
        Updates the matching array by augmenting along the found path.

        :param match: The array representing the matching for each vertex.
        :param parent: The parent array, used to backtrack the augmenting path.
        :param u: The end vertex of the augmenting path.
        """
        while u != UNMATCHED:
            v = parent[u]
            next_node = match[v]
            match[v] = u
            match[u] = v
            u = next_node

    @staticmethod
    def find_base(base, parent, u, v):
        """
        Finds the lowest common ancestor (LCA) of two vertices in the blossom.

        :param base: The array storing the base of each vertex in the current blossom.
        :param parent: The parent array used to trace the path.
        :param u: One end of the edge being analyzed.
        :param v: The other end of the edge being analyzed.
        :return: The base of the node (LCA) or UNMATCHED if not found.
        """
        visited = [False] * len(base)

        # Mark all ancestors of u
        current_u = u
        while True:
            current_u = base[current_u]
            visited[current_u] = True
            if parent[current_u] == UNMATCHED:
                break
            current_u = parent[current_u]

        # Find the common ancestor with v
        current_v = v
        while True:
            current_v = base[current_v]
            if visited[current_v]:
                return current_v
            current_v = parent[current_v]

    @staticmethod
    def contract_blossom(blossom_data):
        """
        Contracts a blossom in the graph, modifying the base array and marking the vertices involved.

        :param blossom_data: An object containing the necessary data to perform the contraction.
        """
        # Mark all vertices in the blossom
        for x in range(blossom_data.u, blossom_data.aux_data.base[blossom_data.u] != blossom_data.lca, blossom_data.aux_data.parent[blossom_data.aux_data.match[x]]):
            base_x = blossom_data.aux_data.base[x]
            match_base_x = blossom_data.aux_data.base[blossom_data.aux_data.match[x]]
            blossom_data.aux_data.in_blossom[base_x] = True
            blossom_data.aux_data.in_blossom[match_base_x] = True

        for x in range(blossom_data.v, blossom_data.aux_data.base[blossom_data.v] != blossom_data.lca, blossom_data.aux_data.parent[blossom_data.aux_data.match[x]]):
            base_x = blossom_data.aux_data.base[x]
            match_base_x = blossom_data.aux_data.base[blossom_data.aux_data.match[x]]
            blossom_data.aux_data.in_blossom[base_x] = True
            blossom_data.aux_data.in_blossom[match_base_x] = True

        # Update the base for all marked vertices
        for i in range(len(blossom_data.aux_data.base)):
            if blossom_data.aux_data.in_blossom[blossom_data.aux_data.base[i]]:
                blossom_data.aux_data.base[i] = blossom_data.lca
                if not blossom_data.aux_data.in_queue[i]:
                    blossom_data.aux_data.queue.append(i)
                    blossom_data.aux_data.in_queue[i] = True


class BlossomAuxData:
    """
    A helper class to encapsulate auxiliary data used during blossom contraction.
    """
    def __init__(self, queue, parent, base, in_blossom, match, in_queue):
        self.queue = queue  # The BFS queue used for traversal
        self.parent = parent  # The parent array for each vertex
        self.base = base  # The base array indicating the base of each vertex
        self.in_blossom = in_blossom  # Indicates whether a vertex is part of a blossom
        self.match = match  # The matching array
        self.in_queue = in_queue  # Indicates whether a vertex is already in the queue


class BlossomData:
    """
    A helper class to store parameters necessary for blossom contraction.
    """
    def __init__(self, aux_data, u, v, lca):
        self.aux_data = aux_data  # The auxiliary data object
        self.u = u  # One vertex in the current edge
        self.v = v  # The other vertex in the current edge
        self.lca = lca  # The lowest common ancestor (base) of the current blossom


# Example usage:
if __name__ == "__main__":
    # Example graph with 6 vertices
    edges = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (0, 5), (2, 4)]
    vertex_count = 6
    result = EdmondsBlossomAlgorithm.maximum_matching(edges, vertex_count)
    print("Maximum Matching Pairs:", result)
