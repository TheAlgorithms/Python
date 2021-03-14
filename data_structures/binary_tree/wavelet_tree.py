from typing import List, Optional

"""
Wavelet tree is a data-structure designed to efficiently answer various range queries
for arrays. Wavelets trees are different from other binary trees in the sense that
the nodes are split based on the actual values of the elements and not on indices,
such as the with segment trees or fenwick trees. You can read more about them here:
1. https://users.dcc.uchile.cl/~jperez/papers/ioiconf16.pdf
2. https://www.youtube.com/watch?v=4aSv9PcecDw&t=811s
3. https://www.youtube.com/watch?v=CybAgVF-MMc&t=1178s
"""


class Node:
    def __init__(self, n):
        self.minn: int = -1
        self.maxx: int = -1
        self.map_left: List = [-1] * n
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def __repr__(self):
        return f"min_value: {self.minn}, max_value: {self.maxx}"


def build_tree(arr: List[int]) -> Node:
    """
    Builds the tree for the provided list arr and returns the root
    of the constructed tree.
    """

    n = len(arr)

    root = Node(n)

    root.minn, root.maxx = min(arr), max(arr)

    # Leaf node case where the node contains only one unique value
    if root.minn == root.maxx:
        return root

    """
    Take the mean of min and max element as the pivot and
    partition arr into left_arr and right_arr with all elements <= pivot in the
    left_arr and the rest in right_arr, maintaining the order of the elements,
    then recursively build trees for left_arr and right_arr
    """

    pivot = (root.minn + root.maxx) // 2
    left_arr, right_arr = [], []

    for index, num in enumerate(arr):
        if num <= pivot:
            left_arr.append(num)
        else:
            right_arr.append(num)

        root.map_left[index] = len(left_arr)

    root.left = build_tree(left_arr)
    root.right = build_tree(right_arr)

    return root


def rank_from_start(node: Node, num: int, i: int) -> int:
    """
    Returns the number of occurances of num in interval [0, i] in the list
    """
    if i < 0:
        return 0

    # Leaf node cases
    if node.minn == node.maxx:
        if node.minn == num:
            return i + 1
        else:
            return 0

    pivot = (node.minn + node.maxx) // 2

    if (
        num <= pivot
    ):  # if num <= pivot, go the left subtree and map index i to the left subtree
        return rank_from_start(node.left, num, node.map_left[i] - 1)
    else:  # otherwise go to the right subtree and map index i to the right subtree
        return rank_from_start(node.right, num, i - node.map_left[i])


def rank(node: Node, num: int, i: int, j: int) -> int:
    """
    Returns the number of occurances of num in interval [i, j] in the list
    """
    if i > j:
        return 0

    rank_till_j = rank_from_start(node, num, j)  # rank of num in interval [0, j]
    rank_before_i = rank_from_start(
        node, num, i - 1
    )  # rank of num in interval [0, i-1]

    return rank_till_j - rank_before_i


def quantile(node: Node, k: int, i: int, j: int) -> int:
    """
    Returns the kth smallest element in interval [i, j] in the list, k is 0-indexed
    """
    if k > (j - i) or i > j:
        return -1

    # Leaf node case
    if node.minn == node.maxx:
        return node.minn

    # number of elements in the left subtree in interval [i, j]
    num_elements_in_left_tree = node.map_left[j] - (node.map_left[i - 1] if i else 0)

    if num_elements_in_left_tree > k:
        return quantile(
            node.left, k, (node.map_left[i - 1] if i else 0), node.map_left[j] - 1
        )
    else:
        return quantile(
            node.right,
            k - num_elements_in_left_tree,
            i - (node.map_left[i - 1] if i else 0),
            j - node.map_left[j],
        )


def range_counting(node: Node, i: int, j: int, x: int, y: int) -> int:
    """
    Returns the number of elememts in range [x,y] in interval [i, j] in the list
    """
    if i > j or x > y:
        return 0

    if node.minn > y or node.maxx < x:
        return 0

    if x <= node.minn and node.maxx <= y:
        return j - i + 1

    left = range_counting(
        node.left, (node.map_left[i - 1] if i else 0), node.map_left[j] - 1, x, y
    )
    right = range_counting(
        node.right, i - (node.map_left[i - 1] if i else 0), j - node.map_left[j], x, y
    )

    return left + right


def main():
    """
    >>> arr = [2,1,4,5,6,8,9,1,2,6,7,4,2,6,5,3,2,7]
    >>> root = build_tree(arr)
    >>> root
    min_value: 1, max_value: 9
    >>> rank(root, 6, 3, 13)
    3
    >>> rank(root, 2, 0, 17)
    4
    >>> rank(root, 9, 2 ,2)
    0
    >>> quantile(root, 2, 2, 5)
    6
    >>> quantile(root, 4, 2, 13)
    4
    >>> quantile(root, 0, 6, 6)
    9
    >>> quantile(root, 4, 2, 5)
    -1
    >>> range_counting(root, 1, 10, 3, 7)
    5
    >>> range_counting(root, 2, 2, 1, 4)
    1
    >>> range_counting(root, 0, 17, 1, 100)
    18
    >>> range_counting(root, 1, 0, 1, 100)
    0
    >>> range_counting(root, 0, 17, 100, 1)
    0
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
