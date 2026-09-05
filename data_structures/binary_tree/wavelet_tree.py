"""
Wavelet tree is a data-structure designed to efficiently answer various range queries
for arrays. Wavelets trees are different from other binary trees in the sense that
the nodes are split based on the actual values of the elements and not on indices,
such as the with segment trees or fenwick trees. You can read more about them here:
1. https://users.dcc.uchile.cl/~jperez/papers/ioiconf16.pdf
2. https://www.youtube.com/watch?v=4aSv9PcecDw&t=811s
3. https://www.youtube.com/watch?v=CybAgVF-MMc&t=1178s
"""

from __future__ import annotations

test_array = [2, 1, 4, 5, 6, 0, 8, 9, 1, 2, 0, 6, 4, 2, 0, 6, 5, 3, 2, 7]


class Node:
    def __init__(self, length: int) -> None:
        self.minn: int = -1
        self.maxx: int = -1
        self.map_left: list[int] = [-1] * length
        self.left: Node | None = None
        self.right: Node | None = None

    def __repr__(self) -> str:
        """
        >>> node = Node(length=27)
        >>> repr(node)
        'Node(min_value=-1 max_value=-1)'
        >>> repr(node) == str(node)
        True
        """
        return f"Node(min_value={self.minn} max_value={self.maxx})"


def build_tree(arr: list[int]) -> Node | None:
    """
    Builds the tree for arr and returns the root
    of the constructed tree

    >>> build_tree(test_array)
    Node(min_value=0 max_value=9)
    """
    root = Node(len(arr))
    root.minn, root.maxx = min(arr), max(arr)
    # Leaf node case where the node contains only one unique value
    if root.minn == root.maxx:
        return root
    """
    Take the mean of min and max element of arr as the pivot and
    partition arr into left_arr and right_arr with all elements <= pivot in the
    left_arr and the rest in right_arr, maintaining the order of the elements,
    then recursively build trees for left_arr and right_arr
    """
    pivot = (root.minn + root.maxx) // 2

    left_arr: list[int] = []
    right_arr: list[int] = []

    for index, num in enumerate(arr):
        if num <= pivot:
            left_arr.append(num)
        else:
            right_arr.append(num)
        root.map_left[index] = len(left_arr)
    root.left = build_tree(left_arr)
    root.right = build_tree(right_arr)
    return root


def rank_till_index(node: Node | None, num: int, index: int) -> int:
    """
    Returns the number of occurrences of num in interval [0, index] in the list

    >>> root = build_tree(test_array)
    >>> rank_till_index(root, 6, 6)
    1
    >>> rank_till_index(root, 2, 0)
    1
    >>> rank_till_index(root, 1, 10)
    2
    >>> rank_till_index(root, 17, 7)
    0
    >>> rank_till_index(root, 0, 9)
    1
    """
    if index < 0 or node is None:
        return 0
    # Leaf node cases
    if node.minn == node.maxx:
        return index + 1 if node.minn == num else 0
    pivot = (node.minn + node.maxx) // 2
    if num <= pivot:
        # go the left subtree and map index to the left subtree
        return rank_till_index(node.left, num, node.map_left[index] - 1)
    else:
        # go to the right subtree and map index to the right subtree
        return rank_till_index(node.right, num, index - node.map_left[index])


def rank(node: Node | None, num: int, start: int, end: int) -> int:
    """
    Returns the number of occurrences of num in interval [start, end] in the list

    >>> root = build_tree(test_array)
    >>> rank(root, 6, 3, 13)
    2
    >>> rank(root, 2, 0, 19)
    4
    >>> rank(root, 9, 2 ,2)
    0
    >>> rank(root, 0, 5, 10)
    2
    """
    if start > end:
        return 0
    rank_till_end = rank_till_index(node, num, end)
    rank_before_start = rank_till_index(node, num, start - 1)
    return rank_till_end - rank_before_start


def quantile(node: Node | None, index: int, start: int, end: int) -> int:
    """
    Returns the index'th smallest element in interval [start, end] in the list
    index is 0-indexed

    >>> root = build_tree(test_array)
    >>> quantile(root, 2, 2, 5)
    5
    >>> quantile(root, 5, 2, 13)
    4
    >>> quantile(root, 0, 6, 6)
    8
    >>> quantile(root, 4, 2, 5)
    -1
    """
    if index > (end - start) or start > end or node is None:
        return -1
    # Leaf node case
    if node.minn == node.maxx:
        return node.minn
    # Number of elements in the left subtree in interval [start, end]
    num_elements_in_left_tree = node.map_left[end] - (
        node.map_left[start - 1] if start else 0
    )
    if num_elements_in_left_tree > index:
        return quantile(
            node.left,
            index,
            (node.map_left[start - 1] if start else 0),
            node.map_left[end] - 1,
        )
    else:
        return quantile(
            node.right,
            index - num_elements_in_left_tree,
            start - (node.map_left[start - 1] if start else 0),
            end - node.map_left[end],
        )


def range_counting(
    node: Node | None, start: int, end: int, start_num: int, end_num: int
) -> int:
    """
    Returns the number of elements in range [start_num, end_num]
    in interval [start, end] in the list

    >>> root = build_tree(test_array)
    >>> range_counting(root, 1, 10, 3, 7)
    3
    >>> range_counting(root, 2, 2, 1, 4)
    1
    >>> range_counting(root, 0, 19, 0, 100)
    20
    >>> range_counting(root, 1, 0, 1, 100)
    0
    >>> range_counting(root, 0, 17, 100, 1)
    0
    """
    if (
        start > end
        or node is None
        or start_num > end_num
        or node.minn > end_num
        or node.maxx < start_num
    ):
        return 0
    if start_num <= node.minn and node.maxx <= end_num:
        return end - start + 1
    left = range_counting(
        node.left,
        (node.map_left[start - 1] if start else 0),
        node.map_left[end] - 1,
        start_num,
        end_num,
    )
    right = range_counting(
        node.right,
        start - (node.map_left[start - 1] if start else 0),
        end - node.map_left[end],
        start_num,
        end_num,
    )
    return left + right


if __name__ == "__main__":
    import doctest

    doctest.testmod()
