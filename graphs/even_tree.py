"""
You are given a tree(a simple connected graph with no cycles). The tree has N
nodes numbered from 1 to N and is rooted at node 1.

Find the maximum number of edges you can remove from the tree to get a forest
such that each connected component of the forest contains an even number of
nodes.

Constraints
2 <= 2 <= 100

Note: The tree input will be such that it can always be decomposed into
components containing an even number of nodes.
"""
# pylint: disable=invalid-name
from collections import defaultdict


def dfs(start: int) -> int:
    """
    DFS traversal starting from the node 'start' to find nodes
    whose subtrees have even number of nodes.

    Args:
    - start (int): The node to start DFS traversal from.

    Returns:
    - int: The number of nodes in the subtree rooted at 'start'.

    Doctest:
    >>> tree.clear(); visited.clear(); cuts.clear()
    >>> tree[1] = [2, 3]; tree[2] = [1]; tree[3] = [1]
    >>> dfs(1)
    3
    >>> cuts
    []
    """
    # pylint: disable=redefined-outer-name
    global tree, visited, cuts
    ret = 1
    visited[start] = True
    for v in tree[start]:
        if v not in visited:
            ret += dfs(v)
    if ret % 2 == 0:
        cuts.append(start)
    return ret


def even_tree():
    """
    Populates the 'cuts' list with nodes where cuts can be made.

    Doctest:
    >>> tree.clear(); visited.clear(); cuts.clear()
    >>> edges=[(2, 1), (3, 1), (4, 3), (5, 2), (6, 1), (7, 2), (8, 6), (9, 8), (10, 8)]
    >>> for u, v in edges:
    ...     tree[u].append(v)
    ...     tree[v].append(u)
    >>> even_tree()
    >>> len(cuts) - 1
    2
    """
    global tree, visited, cuts
    dfs(1)


if __name__ == "__main__":
    n, m = 10, 9
    tree = defaultdict(list)
    visited: dict[int, bool] = {}
    cuts: list[int] = []
    count = 0
    edges = [(2, 1), (3, 1), (4, 3), (5, 2), (6, 1), (7, 2), (8, 6), (9, 8), (10, 8)]
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    even_tree()
    import doctest

    doctest.testmod()
    print(len(cuts) - 1)
