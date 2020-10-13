# Created by susmith98


"""
Problem Description:
Given a binary tree, return it's mirror.
"""


def binary_tree_mirror_dict(root: int, binary_tree_mirror_dictionary: dict):
    if not root or root not in binary_tree_mirror_dictionary:
        return
    left_child = binary_tree_mirror_dictionary[root][0]
    right_child = binary_tree_mirror_dictionary[root][1]
    binary_tree_mirror_dictionary[root] = [right_child, left_child]
    binary_tree_mirror_dict(left_child, binary_tree_mirror_dictionary)
    binary_tree_mirror_dict(right_child, binary_tree_mirror_dictionary)


def binary_tree_mirror(binary_tree: dict = {}, root: int = 1) -> dict:
    """
    >>> binary_tree_mirror({ 1: [2,3], 2: [4,5], 3: [6,7], 7: [8,9]}, 1)
    {1: [3, 2], 2: [5, 4], 3: [7, 6], 7: [9, 8]}
    >>> binary_tree_mirror({ 1: [2,3], 2: [4,5], 3: [6,7], 4: [10,11]}, 1)
    {1: [3, 2], 2: [5, 4], 3: [7, 6], 4: [11, 10]}
    """
    if not binary_tree:
        raise ValueError("binary tree cannot be empty")
    if root not in binary_tree:
        raise ValueError("root is present in the binary_tree")
    binary_tree_mirror_dictionary = dict(binary_tree)
    binary_tree_mirror_dict(root, binary_tree_mirror_dictionary)
    return binary_tree_mirror_dictionary


if __name__ == "__main__":
    binary_tree = {1: [2, 3], 2: [4, 5], 3: [6, 7], 7: [8, 9]}
    print("Binary tree: ", binary_tree)
    binary_tree_mirror_dictionary = binary_tree_mirror(binary_tree, 1)
    print("Binary tree mirror: ", binary_tree_mirror_dictionary)
