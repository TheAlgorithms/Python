"""
Bit-Merging Tree (BMTree) Implementation.

A Bit-Merging Tree (BMTree) indexes records that have three attributes (such as EV
voltage, temperature, and power) by merging (interleaving) the bits of the attributes
into a single 30-bit Morton (Z-order) key. Records with similar attributes produce
similar keys, grouping them close together in the hierarchical tree structure. Keys
whose distance to their nearest neighbor exceeds a threshold (outliers) are stored
separately so they do not distort the primary tree index.

References:
    https://en.wikipedia.org/wiki/Z-order_curve
    https://en.wikipedia.org/wiki/Binary_search_tree
"""

from __future__ import annotations

from bisect import bisect_left
from dataclasses import dataclass, field

DIMENSIONS = 3
BITS_PER_DIMENSION = 10
MAX_ATTRIBUTE_VALUE = 2**BITS_PER_DIMENSION - 1  # 1023


@dataclass
class BMNode:
    """
    A single node in the BMTree holding one Morton key.

    >>> node = BMNode(7)
    >>> node.key, node.left, node.right
    (7, None, None)
    """

    key: int
    left: BMNode | None = None
    right: BMNode | None = None


@dataclass
class BMTree:
    """
    A BMTree container holding the main clustered tree and separately stored outliers.

    >>> tree = BMTree()
    >>> tree.root is None, tree.outliers
    (True, [])
    """

    root: BMNode | None = None
    outliers: list[int] = field(default_factory=list)


def encode_morton_key(point: tuple[int, ...]) -> int:
    """
    Merge the bits of the three attributes into one 30-bit Morton key.

    >>> encode_morton_key((1, 0, 0))
    4
    >>> encode_morton_key((0, 1, 0))
    2
    >>> encode_morton_key((0, 0, 1))
    1
    >>> encode_morton_key((0, 0, 2))
    8
    >>> encode_morton_key((1023, 1023, 1023))
    1073741823
    >>> encode_morton_key((1024, 0, 0))
    Traceback (most recent call last):
        ...
    ValueError: attribute values must be integers between 0 and 1023
    >>> encode_morton_key((-1, 0, 0))
    Traceback (most recent call last):
        ...
    ValueError: attribute values must be integers between 0 and 1023
    >>> encode_morton_key((1, 2))
    Traceback (most recent call last):
        ...
    ValueError: a point must have exactly 3 attributes
    """
    if len(point) != DIMENSIONS:
        msg = f"a point must have exactly {DIMENSIONS} attributes"
        raise ValueError(msg)
    if any(
        not isinstance(value, int) or not 0 <= value <= MAX_ATTRIBUTE_VALUE
        for value in point
    ):
        msg = f"attribute values must be integers between 0 and {MAX_ATTRIBUTE_VALUE}"
        raise ValueError(msg)

    key = 0
    for bit_position in range(BITS_PER_DIMENSION - 1, -1, -1):
        for value in point:
            key = (key << 1) | ((value >> bit_position) & 1)
    return key


def decode_morton_key(key: int) -> tuple[int, int, int]:
    """
    Split a 30-bit Morton key back into its three constituent attributes.

    >>> decode_morton_key(4)
    (1, 0, 0)
    >>> decode_morton_key(encode_morton_key((365, 48, 550)))
    (365, 48, 550)
    >>> decode_morton_key(2**30)
    Traceback (most recent call last):
        ...
    ValueError: key must be between 0 and 1073741823
    """
    max_key = 2 ** (BITS_PER_DIMENSION * DIMENSIONS) - 1
    if not 0 <= key <= max_key:
        msg = f"key must be between 0 and {max_key}"
        raise ValueError(msg)

    values = [0] * DIMENSIONS
    for index in range(BITS_PER_DIMENSION * DIMENSIONS):
        bit = (key >> index) & 1
        dimension = DIMENSIONS - 1 - (index % DIMENSIONS)
        values[dimension] |= bit << (index // DIMENSIONS)
    return values[0], values[1], values[2]


def split_outliers(
    sorted_keys: list[int], outlier_gap: int
) -> tuple[list[int], list[int]]:
    """
    Separate keys whose distance to their nearest neighboring key exceeds outlier_gap.
    Expects sorted, unique keys. Returns (clustered_keys, outlier_keys).

    >>> split_outliers([1, 2, 3, 100], 5)
    ([1, 2, 3], [100])
    >>> split_outliers([5], 5)
    ([5], [])
    >>> split_outliers([], 5)
    ([], [])
    >>> split_outliers([1, 2, 3], 5)
    ([1, 2, 3], [])
    """
    clustered: list[int] = []
    outliers: list[int] = []
    for index, key in enumerate(sorted_keys):
        gaps = []
        if index > 0:
            gaps.append(key - sorted_keys[index - 1])
        if index < len(sorted_keys) - 1:
            gaps.append(sorted_keys[index + 1] - key)
        if gaps and min(gaps) > outlier_gap:
            outliers.append(key)
        else:
            clustered.append(key)
    return clustered, outliers


def _build_balanced(sorted_keys: list[int], low: int, high: int) -> BMNode | None:
    """
    Recursively build a balanced binary search tree from sorted_keys[low:high + 1].

    >>> _build_balanced([], 0, -1) is None
    True
    >>> node = _build_balanced([1, 2, 3], 0, 2)
    >>> node is not None and node.key == 2
    True
    """
    if low > high:
        return None
    middle = (low + high) // 2
    return BMNode(
        sorted_keys[middle],
        _build_balanced(sorted_keys, low, middle - 1),
        _build_balanced(sorted_keys, middle + 1, high),
    )


def build_bm_tree(
    points: list[tuple[int, int, int]], outlier_gap: int | None = None
) -> BMTree:
    """
    Build a BMTree from a list of three-attribute points.

    If outlier_gap is provided, keys farther than outlier_gap from their nearest
    neighbor are isolated in the outliers list instead of the primary tree.

    >>> tree = build_bm_tree([(1, 1, 1), (1, 1, 2), (1, 2, 1)])
    >>> tree.root is not None and tree.root.key == 14
    True
    >>> tree.outliers
    []
    >>> points = [(1, 1, 1), (1, 1, 2), (1, 2, 1), (1000, 1000, 1000)]
    >>> tree = build_bm_tree(points, outlier_gap=100)
    >>> tree.root is not None and tree.root.key == 14
    True
    >>> tree.outliers == [encode_morton_key((1000, 1000, 1000))]
    True
    >>> build_bm_tree([]).root is None
    True
    >>> build_bm_tree([(1, 1, 1)], outlier_gap=-1)
    Traceback (most recent call last):
        ...
    ValueError: outlier_gap must not be negative
    >>> build_bm_tree([(1, 1, 5000)])
    Traceback (most recent call last):
        ...
    ValueError: attribute values must be integers between 0 and 1023
    """
    if outlier_gap is not None and outlier_gap < 0:
        msg = "outlier_gap must not be negative"
        raise ValueError(msg)

    keys = sorted({encode_morton_key(point) for point in points})
    if outlier_gap is None:
        clustered, outliers = keys, []
    else:
        clustered, outliers = split_outliers(keys, outlier_gap)
    return BMTree(_build_balanced(clustered, 0, len(clustered) - 1), outliers)


def _tree_contains(root: BMNode | None, key: int) -> bool:
    """
    Return True if key is stored in the tree rooted at root, False otherwise.

    >>> _tree_contains(None, 1)
    False
    >>> _tree_contains(BMNode(5, BMNode(2), BMNode(9)), 9)
    True
    >>> _tree_contains(BMNode(5, BMNode(2), BMNode(9)), 7)
    False
    """
    current = root
    while current is not None:
        if key == current.key:
            return True
        current = current.left if key < current.key else current.right
    return False


def is_outlier(tree: BMTree, point: tuple[int, int, int]) -> bool:
    """
    Return True if the point is stored in the outlier list of the BMTree.

    >>> points = [(1, 1, 1), (1, 1, 2), (1, 2, 1), (1000, 1000, 1000)]
    >>> tree = build_bm_tree(points, outlier_gap=100)
    >>> is_outlier(tree, (1000, 1000, 1000))
    True
    >>> is_outlier(tree, (1, 1, 1))
    False
    """
    key = encode_morton_key(point)
    index = bisect_left(tree.outliers, key)
    return index < len(tree.outliers) and tree.outliers[index] == key


def search(tree: BMTree, point: tuple[int, int, int]) -> bool:
    """
    Search whether a given three-attribute point exists in the BMTree
    (either within the primary clustered tree or the outlier storage).

    >>> points = [(365, 48, 550), (366, 48, 551), (900, 10, 20)]
    >>> tree = build_bm_tree(points)
    >>> search(tree, (365, 48, 550))
    True
    >>> search(tree, (900, 10, 20))
    True
    >>> search(tree, (365, 48, 551))
    False
    >>> search(build_bm_tree([]), (1, 2, 3))
    False
    >>> search(tree, (1, 2))
    Traceback (most recent call last):
        ...
    ValueError: a point must have exactly 3 attributes
    >>> tree = build_bm_tree([(1, 1, 1), (1, 1, 2), (1000, 1000, 1000)], 100)
    >>> search(tree, (1000, 1000, 1000))
    True
    """
    key = encode_morton_key(point)
    return _tree_contains(tree.root, key) or is_outlier(tree, point)


def inorder_traversal(root: BMNode | None) -> list[int]:
    """
    Return the Morton keys stored in the tree in ascending in-order sequence.

    >>> inorder_traversal(None)
    []
    >>> inorder_traversal(BMNode(5, BMNode(2), BMNode(9)))
    [2, 5, 9]
    """
    if root is None:
        return []
    return [*inorder_traversal(root.left), root.key, *inorder_traversal(root.right)]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
