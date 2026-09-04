from collections import deque


class BlossomAuxData:
    """Class to hold auxiliary data during the blossom algorithm's execution."""

    def __init__(
        self,
        queue: deque,
        parent: list[int],
        base: list[int],
        in_blossom: list[bool],
        match: list[int],
        in_queue: list[bool],
    ) -> None:
        """
        Initializes the BlossomAuxData instance.

        Args:
            queue: A deque for BFS processing.
            parent: List of parent vertices in the augmenting path.
            base: List of base vertices for each vertex.
            in_blossom: Boolean list indicating if a vertex is in a blossom.
            match: List of matched vertices.
            in_queue: Boolean list indicating if a vertex is in the queue.
        """
        self.queue = queue
        self.parent = parent
        self.base = base
        self.in_blossom = in_blossom
        self.match = match
        self.in_queue = in_queue


class BlossomData:
    """Class to encapsulate data related to a blossom in the graph."""

    def __init__(
        self,
        aux_data: BlossomAuxData,
        vertex_u: int,
        vertex_v: int,
        lowest_common_ancestor: int,
    ) -> None:
        """
        Initializes the BlossomData instance.

        Args:
            aux_data: The auxiliary data related to the blossom.
            vertex_u: One vertex in the blossom.
            vertex_v: The other vertex in the blossom.
            lowest_common_ancestor: The lowest common ancestor of vertex_u and vertex_v.
        """
        self.aux_data = aux_data
        self.vertex_u = vertex_u
        self.vertex_v = vertex_v
        self.lowest_common_ancestor = lowest_common_ancestor


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
        graph: list[list[int]] = [[] for _ in range(vertex_count)]

        # Populate the graph with the edges
        for edge in edges:
            u, v = edge
            graph[u].append(v)
            graph[v].append(u)

        # All vertices are initially unmatched
        match: list[int] = [EdmondsBlossomAlgorithm.UNMATCHED] * vertex_count
        parent: list[int] = [EdmondsBlossomAlgorithm.UNMATCHED] * vertex_count
        # Each vertex is its own base initially
        base: list[int] = list(range(vertex_count))
        in_blossom: list[bool] = [False] * vertex_count
        # Tracks vertices in the BFS queue
        in_queue: list[bool] = [False] * vertex_count

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
                            # Case 1: y is unmatched;
                            # we've found an augmenting path
                            if match[y] == EdmondsBlossomAlgorithm.UNMATCHED:
                                parent[y] = current  # Update the parent
                                augmenting_path_found = True
                                # Augment along this path
                                EdmondsBlossomAlgorithm.update_matching(
                                    match, parent, y
                                )
                                break

                            # Case 2: y is matched;
                            # add y's match to the queue
                            z = match[y]
                            parent[y] = current
                            parent[z] = y
                            if not in_queue[z]:  # If z is not already in the queue
                                queue.append(z)
                                in_queue[z] = True
                        else:
                            # Case 3: Both current and y have a parent;
                            # check for a cycle/blossom
                            base_u = EdmondsBlossomAlgorithm.find_base(
                                base, parent, current, y
                            )
                            if base_u != EdmondsBlossomAlgorithm.UNMATCHED:
                                EdmondsBlossomAlgorithm.contract_blossom(
                                    BlossomData(
                                        BlossomAuxData(
                                            queue,
                                            parent,
                                            base,
                                            in_blossom,
                                            match,
                                            in_queue,
                                        ),
                                        current,
                                        y,
                                        base_u,
                                    )
                                )

        # Create result list of matched pairs
        matching_result: list[list[int]] = []
        for v in range(vertex_count):
            if (
                match[v] != EdmondsBlossomAlgorithm.UNMATCHED and v < match[v]
            ):  # Ensure pairs are unique
                matching_result.append([v, match[v]])

        return matching_result

    @staticmethod
    def update_matching(
        match: list[int], parent: list[int], matched_vertex: int
    ) -> None:
        """
        Updates the matching based on the augmenting path found.

        Args:
            match: The current match list.
            parent: The parent list from BFS traversal.
            matched_vertex: The vertex where the augmenting path ends.
        """
        while matched_vertex != EdmondsBlossomAlgorithm.UNMATCHED:
            v = parent[matched_vertex]  # Get the parent vertex
            next_match = match[v]  # Store the next match
            match[v] = matched_vertex  # Update match for v
            match[matched_vertex] = v  # Update match for matched_vertex
            matched_vertex = next_match  # Move to the next vertex

    @staticmethod
    def find_base(
        base: list[int], parent: list[int], vertex_u: int, vertex_v: int
    ) -> int:
        """
        Finds the base of the blossom.

        Args:
            base: The base array for each vertex.
            parent: The parent array from BFS.
            vertex_u: One endpoint of the blossom.
            vertex_v: The other endpoint of the blossom.

        Returns:
            The lowest common ancestor of vertex_u and vertex_v in the blossom.
        """
        visited: list[bool] = [False] * len(base)

        # Mark ancestors of vertex_u
        current_vertex_u = vertex_u
        while True:
            current_vertex_u = base[current_vertex_u]
            # Mark this base as visited
            visited[current_vertex_u] = True
            if parent[current_vertex_u] == EdmondsBlossomAlgorithm.UNMATCHED:
                break
            current_vertex_u = parent[current_vertex_u]

        # Find the common ancestor of vertex_v
        current_vertex_v = vertex_v
        while True:
            current_vertex_v = base[current_vertex_v]
            # Check if we've already visited this base
            if visited[current_vertex_v]:
                return current_vertex_v
            current_vertex_v = parent[current_vertex_v]

    @staticmethod
    def contract_blossom(blossom_data: BlossomData) -> None:
        """
        Contracts a blossom found during the matching process.

        Args:
            blossom_data: The data related to the blossom to be contracted.
        """
        # Mark vertices in the blossom
        for x in range(
            blossom_data.vertex_u,
            blossom_data.aux_data.base[blossom_data.vertex_u]
            != blossom_data.lowest_common_ancestor,
        ):
            base_x = blossom_data.aux_data.base[x]
            match_base_x = blossom_data.aux_data.base[blossom_data.aux_data.match[x]]
            # Mark the base as in a blossom
            blossom_data.aux_data.in_blossom[base_x] = True
            blossom_data.aux_data.in_blossom[match_base_x] = True

        for x in range(
            blossom_data.vertex_v,
            blossom_data.aux_data.base[blossom_data.vertex_v]
            != blossom_data.lowest_common_ancestor,
        ):
            base_x = blossom_data.aux_data.base[x]
            match_base_x = blossom_data.aux_data.base[blossom_data.aux_data.match[x]]
            # Mark the base as in a blossom
            blossom_data.aux_data.in_blossom[base_x] = True
            blossom_data.aux_data.in_blossom[match_base_x] = True

        # Update the base for all marked vertices
        for i in range(len(blossom_data.aux_data.base)):
            if blossom_data.aux_data.in_blossom[blossom_data.aux_data.base[i]]:
                # Contract to the lowest common ancestor
                blossom_data.aux_data.base[i] = blossom_data.lowest_common_ancestor
                if not blossom_data.aux_data.in_queue[i]:
                    # Add to queue if not already present
                    blossom_data.aux_data.queue.append(i)
                    blossom_data.aux_data.in_queue[i] = True
