"""Disjoint-set union (Union-Find) with path compression and union by rank."""

from typing import Dict, Iterable, TypeVar

T = TypeVar("T")


class UnionFind:
    def __init__(self, elements: Iterable[T]):
        self._parent: Dict[T, T] = {}
        self._rank: Dict[T, int] = {}
        for element in elements:
            self._parent[element] = element
            self._rank[element] = 0

    def find(self, element: T) -> T:
        if element not in self._parent:
            self._parent[element] = element
            self._rank[element] = 0
            return element
        root = element
        while root != self._parent[root]:
            root = self._parent[root]
        while element != root:
            parent = self._parent[element]
            self._parent[element] = root
            element = parent
        return root

    def union(self, a: T, b: T) -> None:
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return
        rank_a = self._rank[root_a]
        rank_b = self._rank[root_b]
        if rank_a < rank_b:
            self._parent[root_a] = root_b
        elif rank_a > rank_b:
            self._parent[root_b] = root_a
        else:
            self._parent[root_b] = root_a
            self._rank[root_a] += 1
