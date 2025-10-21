from collections import defaultdict, deque
from typing import Any, Dict, List


class Graph:
    def __init__(self, directed: bool = False):
        self.adj: Dict[Any, List[Any]] = defaultdict(list)
        self.directed = directed

    def add_edge(self, u: Any, v: Any) -> None:
        self.adj[u].append(v)
        if not self.directed:
            self.adj[v].append(u)

    def bfs(self, start: Any) -> List[Any]:
        visited = set()
        order = []
        q = deque([start])
        visited.add(start)
        while q:
            u = q.popleft()
            order.append(u)
            for v in self.adj[u]:
                if v not in visited:
                    visited.add(v)
                    q.append(v)
        return order

    def dfs(self, start: Any) -> List[Any]:
        visited = set()
        order = []

        def _dfs(u: Any) -> None:
            visited.add(u)
            order.append(u)
            for v in self.adj[u]:
                if v not in visited:
                    _dfs(v)

        _dfs(start)
        return order
