"""Kruskal's minimum spanning tree algorithm."""

from typing import Iterable, List, Tuple, TypeVar

from .union_find import UnionFind

T = TypeVar("T")
Edge = Tuple[T, T, float]


def kruskal_mst(vertices: Iterable[T], edges: Iterable[Edge]) -> List[Edge]:
    edge_list = sorted(edges, key=lambda item: item[2])
    uf = UnionFind(vertices)
    mst: List[Edge] = []
    for u, v, weight in edge_list:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, weight))
    return mst
