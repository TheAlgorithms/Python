"""
Problem Description:
Given a binary tree, return its mirror.
"""


def binary_tree_mirror_dict(binary_tree_mirror_dictionary: dict, root: int):
    if not root or root not in binary_tree_mirror_dictionary:
        return
    left_child, right_child = binary_tree_mirror_dictionary[root][:2]
    binary_tree_mirror_dictionary[root] = [right_child, left_child]
    binary_tree_mirror_dict(binary_tree_mirror_dictionary, left_child)
    binary_tree_mirror_dict(binary_tree_mirror_dictionary, right_child)


def binary_tree_mirror(binary_tree: dict, root: int = 1) -> dict:
    """
    >>> binary_tree_mirror({ 1: [2,3], 2: [4,5], 3: [6,7], 7: [8,9]}, 1)
    {1: [3, 2], 2: [5, 4], 3: [7, 6], 7: [9, 8]}
    >>> binary_tree_mirror({ 1: [2,3], 2: [4,5], 3: [6,7], 4: [10,11]}, 1)
    {1: [3, 2], 2: [5, 4], 3: [7, 6], 4: [11, 10]}
    >>> binary_tree_mirror({ 1: [2,3], 2: [4,5], 3: [6,7], 4: [10,11]}, 5)
    Traceback (most recent call last):
        ...
    ValueError: root 5 is not present in the binary_tree
    >>> binary_tree_mirror({}, 5)
    Traceback (most recent call last):
        ...
    ValueError: binary tree cannot be empty
    """
    if not binary_tree:
        raise ValueError("binary tree cannot be empty")
    if root not in binary_tree:
        msg = f"root {root} is not present in the binary_tree"
        raise ValueError(msg)
    binary_tree_mirror_dictionary = dict(binary_tree)
    binary_tree_mirror_dict(binary_tree_mirror_dictionary, root)
    return binary_tree_mirror_dictionary


if __name__ == "__main__":
    binary_tree = {1: [2, 3], 2: [4, 5], 3: [6, 7], 7: [8, 9]}
    print(f"Binary tree: {binary_tree}")
    binary_tree_mirror_dictionary = binary_tree_mirror(binary_tree, 5)
    print(f"Binary tree mirror: {binary_tree_mirror_dictionary}")
