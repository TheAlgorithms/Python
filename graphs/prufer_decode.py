"""Decode a Prüfer sequence into the edges of a labeled tree.

https://en.wikipedia.org/wiki/Pr%C3%BCfer_sequence
"""

from heapq import heapify, heappop, heappush


def prufer_decode(code: list[int]) -> list[tuple[int, int]]:
    """Return the tree encoded by ``code`` using vertices 1 through n.

    A code of length n - 2 represents one tree on n labeled vertices. At each
    step, the smallest leaf is joined to the next vertex in the code.
    The returned edges are undirected and ordered by the decoding steps.
    This takes O(n log n) time and O(n) space.

    >>> prufer_decode([])
    [(1, 2)]
    >>> prufer_decode([4, 4, 4, 5])
    [(1, 4), (2, 4), (3, 4), (4, 5), (5, 6)]
    >>> prufer_decode([1])
    [(2, 1), (1, 3)]
    >>> prufer_decode([0])
    Traceback (most recent call last):
    ...
    ValueError: code vertices must be integers from 1 through n
    >>> prufer_decode([True])
    Traceback (most recent call last):
    ...
    ValueError: code vertices must be integers from 1 through n
    >>> prufer_decode("1")
    Traceback (most recent call last):
    ...
    TypeError: code must be a list of integers
    """
    if not isinstance(code, list):
        raise TypeError("code must be a list of integers")

    vertex_count = len(code) + 2
    if any(
        not isinstance(vertex, int)
        or isinstance(vertex, bool)
        or not 1 <= vertex <= vertex_count
        for vertex in code
    ):
        raise ValueError("code vertices must be integers from 1 through n")

    degree = [1] * (vertex_count + 1)
    for vertex in code:
        degree[vertex] += 1

    leaves = [vertex for vertex in range(1, vertex_count + 1) if degree[vertex] == 1]
    heapify(leaves)
    edges: list[tuple[int, int]] = []

    for vertex in code:
        leaf = heappop(leaves)
        edges.append((leaf, vertex))
        degree[leaf] = 0
        degree[vertex] -= 1
        if degree[vertex] == 1:
            heappush(leaves, vertex)

    edges.append((heappop(leaves), heappop(leaves)))
    return edges
