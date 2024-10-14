from collections import deque, defaultdict
from typing import List, Tuple, Dict


UNMATCHED = -1  # Constant to represent unmatched vertices


class EdmondsBlossomAlgorithm:
    @staticmethod
    def maximum_matching(edges: List[Tuple[int, int]], vertex_count: int) -> List[Tuple[int, int]]:
        """
        Finds the maximum matching in a general graph using Edmonds' Blossom Algorithm.

        :param edges: List of edges in the graph.
        :param vertex_count: Number of vertices in the graph.
        :return: A list of matched pairs of vertices.

        >>> EdmondsBlossomAlgorithm.maximum_matching([(0, 1), (1, 2), (2, 3)], 4)
        [(0, 1), (2, 3)]
        """
        graph: Dict[int, List[int]] = defaultdict(list)

        # Populate the graph with the edges
        for vertex_u, vertex_v in edges:
            graph[vertex_u].append(vertex_v)
            graph[vertex_v].append(vertex_u)

        # Initial matching array and auxiliary data structures
        match = [UNMATCHED] * vertex_count
        parent = [UNMATCHED] * vertex_count
        base = list(range(vertex_count))
        in_blossom = [False] * vertex_count
        in_queue = [False] * vertex_count

        # Main logic for finding maximum matching
        for vertex_u in range(vertex_count):
            if match[vertex_u] == UNMATCHED:
                # BFS initialization
                parent = [UNMATCHED] * vertex_count
                base = list(range(vertex_count))
                in_blossom = [False] * vertex_count
                in_queue = [False] * vertex_count

                queue = deque([vertex_u])
                in_queue[vertex_u] = True

                augmenting_path_found = False

                # BFS to find augmenting paths
                while queue and not augmenting_path_found:
                    current_vertex = queue.popleft()
                    for neighbor in graph[current_vertex]:
                        if match[current_vertex] == neighbor:
                            continue

                        if base[current_vertex] == base[neighbor]:
                            continue  # Avoid self-loops

                        if parent[neighbor] == UNMATCHED:
                            # Case 1: neighbor is unmatched, we've found an augmenting path
                            if match[neighbor] == UNMATCHED:
                                parent[neighbor] = current_vertex
                                augmenting_path_found = True
                                EdmondsBlossomAlgorithm.update_matching(match, parent, neighbor)
                                break

                            # Case 2: neighbor is matched, add neighbor's match to the queue
                            matched_vertex = match[neighbor]
                            parent[neighbor] = current_vertex
                            parent[matched_vertex] = neighbor
                            if not in_queue[matched_vertex]:
                                queue.append(matched_vertex)
                                in_queue[matched_vertex] = True
                        else:
                            # Case 3: Both current_vertex and neighbor have a parent; check for a cycle/blossom
                            base_vertex = EdmondsBlossomAlgorithm.find_base(base, parent, current_vertex, neighbor)
                            if base_vertex != UNMATCHED:
                                EdmondsBlossomAlgorithm.contract_blossom(BlossomData(
                                    BlossomAuxData(queue, parent, base, in_blossom, match, in_queue),
                                    current_vertex, neighbor, base_vertex
                                ))

        # Create result list of matched pairs
        matching_result = []
        for vertex in range(vertex_count):
            if match[vertex] != UNMATCHED and vertex < match[vertex]:
                matching_result.append((vertex, match[vertex]))

        return matching_result

    @staticmethod
    def update_matching(match: List[int], parent: List[int], current_vertex: int) -> None:
        """
        Updates the matching along the augmenting path found.

        :param match: The matching array.
        :param parent: The parent array used during the BFS.
        :param current_vertex: The starting node of the augmenting path.

        >>> match = [UNMATCHED, UNMATCHED, UNMATCHED]
        >>> parent = [1, 0, UNMATCHED]
        >>> EdmondsBlossomAlgorithm.update_matching(match, parent, 2)
        >>> match
        [1, 0, -1]
        """
        while current_vertex != UNMATCHED:
            matched_vertex = parent[current_vertex]
            next_vertex = match[matched_vertex]
            match[matched_vertex] = current_vertex
            match[current_vertex] = matched_vertex
            current_vertex = next_vertex

    @staticmethod
    def find_base(base: List[int], parent: List[int], vertex_u: int, vertex_v: int) -> int:
        """
        Finds the base of a node in the blossom.

        :param base: The base array.
        :param parent: The parent array.
        :param vertex_u: One end of the edge.
        :param vertex_v: The other end of the edge.
        :return: The base of the node or UNMATCHED.

        >>> base = [0, 1, 2, 3]
        >>> parent = [1, 0, UNMATCHED, UNMATCHED]
        >>> EdmondsBlossomAlgorithm.find_base(base, parent, 2, 3)
        2
        """
        visited = [False] * len(base)

        # Mark ancestors of vertex_u
        current_vertex_u = vertex_u
        while True:
            current_vertex_u = base[current_vertex_u]
            visited[current_vertex_u] = True
            if parent[current_vertex_u] == UNMATCHED:
                break
            current_vertex_u = parent[current_vertex_u]

        # Find the common ancestor of vertex_v
        current_vertex_v = vertex_v
        while True:
            current_vertex_v = base[current_vertex_v]
            if visited[current_vertex_v]:
                return current_vertex_v
            current_vertex_v = parent[current_vertex_v]

    @staticmethod
    def contract_blossom(blossom_data: 'BlossomData') -> None:
        """
        Contracts a blossom in the graph, modifying the base array
        and marking the vertices involved.

        :param blossom_data: An object containing the necessary data
        to perform the contraction.

        >>> aux_data = BlossomAuxData(deque(), [], [], [], [], [])
        >>> blossom_data = BlossomData(aux_data, 0, 1, 2)
        >>> EdmondsBlossomAlgorithm.contract_blossom(blossom_data)
        """
        # Mark all vertices in the blossom
        current_vertex_u = blossom_data.u
        while blossom_data.aux_data.base[current_vertex_u] != blossom_data.lca:
            base_u = blossom_data.aux_data.base[current_vertex_u]
            match_base_u = blossom_data.aux_data.base[blossom_data.aux_data.match[current_vertex_u]]
            blossom_data.aux_data.in_blossom[base_u] = True
            blossom_data.aux_data.in_blossom[match_base_u] = True
            current_vertex_u = blossom_data.aux_data.parent[blossom_data.aux_data.match[current_vertex_u]]

        current_vertex_v = blossom_data.v
        while blossom_data.aux_data.base[current_vertex_v] != blossom_data.lca:
            base_v = blossom_data.aux_data.base[current_vertex_v]
            match_base_v = blossom_data.aux_data.base[blossom_data.aux_data.match[current_vertex_v]]
            blossom_data.aux_data.in_blossom[base_v] = True
            blossom_data.aux_data.in_blossom[match_base_v] = True
            current_vertex_v = blossom_data.aux_data.parent[blossom_data.aux_data.match[current_vertex_v]]

        # Update the base for all marked vertices
        for i in range(len(blossom_data.aux_data.base)):
            if blossom_data.aux_data.in_blossom[blossom_data.aux_data.base[i]]:
                blossom_data.aux_data.base[i] = blossom_data.lca
                if not blossom_data.aux_data.in_queue[i]:
                    blossom_data.aux_data.queue.append(i)
                    blossom_data.aux_data.in_queue[i] = True


class BlossomAuxData:
    """
    Auxiliary data class to encapsulate common parameters for the blossom operations.
    """

    def __init__(self, queue: deque, parent: List[int], base: List[int],
                 in_blossom: List[bool], match: List[int], in_queue: List[bool]) -> None:
        self.queue = queue
        self.parent = parent
        self.base = base
        self.in_blossom = in_blossom
        self.match = match
        self.in_queue = in_queue


class BlossomData:
    """
    BlossomData class with reduced parameters.
    """

    def __init__(self, aux_data: BlossomAuxData, u: int, v: int, lca: int) -> None:
        self.aux_data = aux_data
        self.u = u
        self.v = v
        self.lca = lca
