from collections import deque


class BlossomAuxData:
    def __init__(self, queue: deque, parent: list[int], base: list[int],
                 in_blossom: list[bool], match: list[int], in_queue: list[bool]):
        self.queue = queue
        self.parent = parent
        self.base = base
        self.in_blossom = in_blossom
        self.match = match
        self.in_queue = in_queue

class BlossomData:
    def __init__(self, aux_data: BlossomAuxData, u: int, v: int, lca: int):
        self.aux_data = aux_data
        self.u = u
        self.v = v
        self.lca = lca

class EdmondsBlossomAlgorithm:
    UNMATCHED = -1  # Constant to represent unmatched vertices

    @staticmethod
    def maximum_matching(edges: list[list[int]], vertex_count: int) -> list[list[int]]:
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
        # Indicates if a vertex is part of a blossom
        in_blossom = [False] * vertex_count
        in_queue = [False] * vertex_count  # Tracks vertices in the BFS queue

        # Main logic for finding maximum matching
        for u in range(vertex_count):
            if match[u] == EdmondsBlossomAlgorithm.UNMATCHED:
                # BFS initialization
                parent = [EdmondsBlossomAlgorithm.UNMATCHED] * vertex_count
                base = list(range(vertex_count))
                in_blossom = [False] * vertex_count
                in_queue = [False] * vertex_count

                queue = deque([u])
                in_queue[u] = True

                augmenting_path_found = False

                # BFS to find augmenting paths
                while queue and not augmenting_path_found:
                    current = queue.popleft()
                    for y in graph[current]:
                        if match[current] == y:
                            # Skip if we are
                            # looking at the same edge
                            # as the current match
                            continue

                        if base[current] == base[y]:
                            continue  # Avoid self-loops

                        if parent[y] == EdmondsBlossomAlgorithm.UNMATCHED:
                            # Case 1: y is unmatched, we've found an augmenting path
                            if match[y] == EdmondsBlossomAlgorithm.UNMATCHED:
                                parent[y] = current
                                augmenting_path_found = True
                                # Augment along this path
                                (EdmondsBlossomAlgorithm
                                 .update_matching(match, parent, y))
                                break

                            # Case 2: y is matched, add y's match to the queue
                            z = match[y]
                            parent[y] = current
                            parent[z] = y
                            if not in_queue[z]:
                                queue.append(z)
                                in_queue[z] = True
                        else:
                            # Case 3: Both current and y have a parent;
                            # check for a cycle/blossom
                            base_u = EdmondsBlossomAlgorithm.find_base(base,
                                                        parent, current, y)
                            if base_u != EdmondsBlossomAlgorithm.UNMATCHED:
                                EdmondsBlossomAlgorithm.contract_blossom(BlossomData(
                                    BlossomAuxData(queue,
                                                   parent,
                                                   base,
                                                   in_blossom,
                                                   match,
                                                   in_queue),
                                    current, y, base_u))

        # Create result list of matched pairs
        matching_result = []
        for v in range(vertex_count):
            if match[v] != EdmondsBlossomAlgorithm.UNMATCHED and v < match[v]:
                matching_result.append([v, match[v]])

        return matching_result

    @staticmethod
    def update_matching(match: list[int], parent: list[int], u: int):
        while u != EdmondsBlossomAlgorithm.UNMATCHED:
            v = parent[u]
            next_match = match[v]
            match[v] = u
            match[u] = v
            u = next_match

    @staticmethod
    def find_base(base: list[int], parent: list[int], u: int, v: int) -> int:
        visited = [False] * len(base)

        # Mark ancestors of u
        current_u = u
        while True:
            current_u = base[current_u]
            visited[current_u] = True
            if parent[current_u] == EdmondsBlossomAlgorithm.UNMATCHED:
                break
            current_u = parent[current_u]

        # Find the common ancestor of v
        current_v = v
        while True:
            current_v = base[current_v]
            if visited[current_v]:
                return current_v
            current_v = parent[current_v]

    @staticmethod
    def contract_blossom(blossom_data: BlossomData):
        for x in range(blossom_data.u,
                       blossom_data.aux_data.base[blossom_data.u] != blossom_data.lca):
            base_x = blossom_data.aux_data.base[x]
            match_base_x = blossom_data.aux_data.base[blossom_data.aux_data.match[x]]
            blossom_data.aux_data.in_blossom[base_x] = True
            blossom_data.aux_data.in_blossom[match_base_x] = True

        for x in range(blossom_data.v,
                       blossom_data.aux_data.base[blossom_data.v] != blossom_data.lca):
            base_x = blossom_data.aux_data.base[x]
            match_base_x = blossom_data.aux_data.base[blossom_data.aux_data.match[x]]
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
