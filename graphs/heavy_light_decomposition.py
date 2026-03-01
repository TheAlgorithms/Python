"""
Heavy-Light Decomposition (HLD)

Decomposes tree into chains for efficient path queries/updates.
Used for problems like "path sum queries", "max edge on path", etc.

Time Complexity:
- Build: O(n)
- Query/Update: O(log²n) (can be O(log n) with segment trees)
Space Complexity: O(n)
"""

from typing import List, Tuple, Optional, Callable


class HeavyLightDecomposition:
    """
    Heavy-Light Decomposition for path queries on trees.

    Supports operations like: sum/max on path between two nodes.
    """

    def __init__(self, n: int):
        self.n = n
        self.adj: List[List[int]] = [[] for _ in range(n)]
        self.parent = [-1] * n
        self.depth = [0] * n
        self.heavy_child = [-1] * n
        self.size = [0] * n
        self.head = [0] * n  # Top of current chain
        self.pos = [0] * n  # Position in base array
        self.cur_pos = 0

        # Values associated with nodes (optional)
        self.value: List[int] = [0] * n
        self.base_array: List[int] = []

    def add_edge(self, u: int, v: int) -> None:
        """Add undirected edge."""
        self.adj[u].append(v)
        self.adj[v].append(u)

    def set_value(self, u: int, val: int) -> None:
        """Set value for node u."""
        self.value[u] = val

    def _dfs(self, u: int, p: int) -> int:
        """First DFS to calculate sizes and find heavy children."""
        self.size[u] = 1
        self.parent[u] = p
        max_size = 0

        for v in self.adj[u]:
            if v != p:
                self.depth[v] = self.depth[u] + 1
                sub_size = self._dfs(v, u)
                self.size[u] += sub_size

                if sub_size > max_size:
                    max_size = sub_size
                    self.heavy_child[u] = v

        return self.size[u]

    def _decompose(self, u: int, h: int) -> None:
        """Second DFS to assign chains and positions."""
        self.head[u] = h
        self.pos[u] = self.cur_pos
        self.cur_pos += 1

        if self.heavy_child[u] != -1:
            # Continue heavy chain
            self._decompose(self.heavy_child[u], h)

        # Start new light chains
        for v in self.adj[u]:
            if v != self.parent[u] and v != self.heavy_child[u]:
                self._decompose(v, v)

    def build(self, root: int = 0) -> None:
        """
        Build HLD structure.

        Must be called after adding all edges and before queries.
        """
        self._dfs(root, -1)
        self._decompose(root, root)

        # Build base array for segment tree
        self.base_array = [0] * self.n
        for u in range(self.n):
            self.base_array[self.pos[u]] = self.value[u]

    def _lca(self, u: int, v: int) -> int:
        """Find LCA using HLD structure."""
        while self.head[u] != self.head[v]:
            if self.depth[self.head[u]] > self.depth[self.head[v]]:
                u = self.parent[self.head[u]]
            else:
                v = self.parent[self.head[v]]
        return u if self.depth[u] < self.depth[v] else v

    def query_path(
        self, u: int, v: int, operation: Callable[[List[int]], int] = sum
    ) -> int:
        """
        Query path from u to v using given operation.

        Args:
            u, v: Vertices
            operation: Function to apply (sum, max, min, etc.)

        Returns:
            Result of operation on path

        Example:
            >>> hld = HeavyLightDecomposition(5)
            >>> for u, v in [(0,1), (0,2), (1,3), (1,4)]: hld.add_edge(u,v)
            >>> for i in range(5): hld.set_value(i, i+1)
            >>> hld.build(0)
            >>> hld.query_path(3, 4)  # Path: 3->1->4, values: 4+2+5=11
            11
        """
        res = []

        while self.head[u] != self.head[v]:
            if self.depth[self.head[u]] > self.depth[self.head[v]]:
                # Query from head[u] to u
                segment = self.base_array[self.pos[self.head[u]] : self.pos[u] + 1]
                res.extend(segment)
                u = self.parent[self.head[u]]
            else:
                segment = self.base_array[self.pos[self.head[v]] : self.pos[v] + 1]
                res.extend(segment)
                v = self.parent[self.head[v]]

        # Same chain now
        l, r = self.pos[u], self.pos[v]
        if l > r:
            l, r = r, l
        segment = self.base_array[l : r + 1]
        res.extend(segment)

        return operation(res) if res else 0

    def update_node(self, u: int, new_val: int) -> None:
        """Update value of node u."""
        self.value[u] = new_val
        self.base_array[self.pos[u]] = new_val


if __name__ == "__main__":
    import doctest

    doctest.testmod()
