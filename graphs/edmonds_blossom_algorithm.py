from collections import deque


class BlossomAuxData:
    """Class to hold auxiliary data during the blossom algorithm's execution."""

    def __init__(self, queue: deque, parent: list[int], base: list[int],
                 in_blossom: list[bool], match: list[int], in_queue: list[bool]):
        self.queue = queue
        self.parent = parent
        self.base = base
        self.in_blossom = in_blossom
        self.match = match
        self.in_queue = in_queue


class BlossomData:
    """Class to encapsulate data related to a blossom in the graph."""

    def __init__(self, aux_data: BlossomAuxData, u: int, v: int, lca: int):
        self.aux_data = aux_data
        self.u = u
        self.v = v
        self.lca = lca


class EdmondsBlossomAlgorithm:
    UNMATCHED = -1  # Constant to represent unmatched vertices

    @staticmethod
    def maximum_matching(edges: list[list[int]], vertex_count: int) -> list[list[int]]:
        """
        Finds the maximum matching in a graph using the Edmonds Blossom Algorithm.

        Args:
            edges: A list of edges represented as pairs of vertices.
            vertex_count: The total number of vertices in the graph.

        Returns:
            A list of matched pairs in the form of a list of lists.
        """
        # Create an adjacency list for the graph
        graph = [[] for _ in range(vertex_count)]

        # Populate the graph with the edges
        for edge in edges:
            u, v = edge
            graph[u].append(v)
            graph[v].append(u)

        # All vertices are initially unmatched
        match = [EdmondsBlossomAlgorithm.UNMATCHED] * vertex_count
        parent = [EdmondsBlossomAlgorithm.UNMATCHED] * vertex_count
        base = list(range(vertex_count))  # Each vertex is its own base initially
        in_blossom = [False] * vertex_count
        in_queue = [False] * vertex_count  # Tracks vertices in the BFS queue

        # Main logic for finding maximum matching
        for u in range(vertex_count):
            # Only consider unmatched vertices
            if match[u] == EdmondsBlossomAlgorithm.UNMATCHED:
                # BFS initialization
                parent = [EdmondsBlossomAlgorithm.UNMATCHED] * vertex_count
                base = list(range(vertex_count))
                in_blossom = [False] * vertex_count
                in_queue = [False] * vertex_count

                queue = deque([u])  # Start BFS from the unmatched vertex
                in_queue[u] = True

                augmenting_path_found = False

                # BFS to find augmenting paths
                while queue and not augmenting_path_found:
                    current = queue.popleft()  # Get the current vertex
                    for y in graph[current]:  # Explore adjacent vertices
                        # Skip if we're looking at the current match
                        if match[current] == y:
                            continue

                        if base[current] == base[y]:  # Avoid self-loops
                            continue

                        if parent[y] == EdmondsBlossomAlgorithm.UNMATCHED:
                            # Case 1: y is unmatched; we've found an augmenting path
                            if match[y] == EdmondsBlossomAlgorithm.UNMATCHED:
                                parent[y] = current  # Update the parent
                                augmenting_path_found = True
                                # Augment along this path
                                EdmondsBlossomAlgorithm.update_matching(match,
                                                                        parent,
                                                                        y)
                                break

                            # Case 2: y is matched; add y's match to the queue
                            z = match[y]
                            parent[y] = current
                            parent[z] = y
                            if not in_queue[z]:  # If z is not already in the queue
                                queue.append(z)
                                in_queue[z] = True
                        else:
                            # Case 3: Both current and y have a parent;
                            # check for a cycle/blossom
                            base_u = EdmondsBlossomAlgorithm.find_base(base,
                                                                       parent,
                                                                       current,
                                                                       y)
                            if base_u != EdmondsBlossomAlgorithm.UNMATCHED:
                                EdmondsBlossomAlgorithm.contract_blossom(BlossomData(
                                    BlossomAuxData(queue, parent,
                                                   base, in_blossom,
                                                   match, in_queue),
                                    current, y, base_u))

        # Create result list of matched pairs
        matching_result = []
        for v in range(vertex_count):
            # Ensure pairs are unique
            if match[v] != EdmondsBlossomAlgorithm.UNMATCHED and v < match[v]:
                matching_result.append([v, match[v]])

        return matching_result

    @staticmethod
    def update_matching(match: list[int], parent: list[int], u: int):
        """
        Updates the matching based on the augmenting path found.

        Args:
            match: The current match list.
            parent: The parent list from BFS traversal.
            u: The vertex where the augmenting path ends.
        """
        while u != EdmondsBlossomAlgorithm.UNMATCHED:
            v = parent[u]  # Get the parent vertex
            next_match = match[v]  # Store the next match
            match[v] = u  # Update match for v
            match[u] = v  # Update match for u
            u = next_match  # Move to the next vertex

    @staticmethod
    def find_base(base: list[int], parent: list[int], u: int, v: int) -> int:
        """
        Finds the base of the blossom.

        Args:
            base: The base array for each vertex.
            parent: The parent array from BFS.
            u: One endpoint of the blossom.
            v: The other endpoint of the blossom.

        Returns:
            The lowest common ancestor of u and v in the blossom.
        """
        visited = [False] * len(base)

        # Mark ancestors of u
        current_u = u
        while True:
            current_u = base[current_u]
            visited[current_u] = True  # Mark this base as visited
            if parent[current_u] == EdmondsBlossomAlgorithm.UNMATCHED:
                break
            current_u = parent[current_u]

        # Find the common ancestor of v
        current_v = v
        while True:
            current_v = base[current_v]
            if visited[current_v]:  # Check if we've already visited this base
                return current_v
            current_v = parent[current_v]

    @staticmethod
    def contract_blossom(blossom_data: BlossomData):
        """
        Contracts a blossom found during the matching process.

        Args:
            blossom_data: The data related to the blossom to be contracted.
        """
        # Mark vertices in the blossom
        for x in range(blossom_data.u,
                       blossom_data.aux_data.base[blossom_data.u] != blossom_data.lca):
            base_x = blossom_data.aux_data.base[x]
            match_base_x = blossom_data.aux_data.base[blossom_data.aux_data.match[x]]
            # Mark the base as in a blossom
            blossom_data.aux_data.in_blossom[base_x] = True
            blossom_data.aux_data.in_blossom[match_base_x] = True

        for x in range(blossom_data.v,
                       blossom_data.aux_data.base[blossom_data.v] != blossom_data.lca):
            base_x = blossom_data.aux_data.base[x]
            match_base_x = blossom_data.aux_data.base[blossom_data.aux_data.match[x]]
            # Mark the base as in a blossom
            blossom_data.aux_data.in_blossom[base_x] = True
            blossom_data.aux_data.in_blossom[match_base_x] = True

        # Update the base for all marked vertices
        for i in range(len(blossom_data.aux_data.base)):
            if blossom_data.aux_data.in_blossom[blossom_data.aux_data.base[i]]:
                # Contract to the lowest common ancestor
                blossom_data.aux_data.base[i] = blossom_data.lca
                if not blossom_data.aux_data.in_queue[i]:
                    # Add to queue if not already present
                    blossom_data.aux_data.queue.append(i)
                    blossom_data.aux_data.in_queue[i] = True
