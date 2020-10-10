# Created by susmith98


"""
Problem Description:
Given a binary tree, return it's mirror.
"""


def binaryTreeMirrorDict(root: int, binary_tree: dict = {}, binary_tree_mirror: dict = {}):
    if root is None or root not in binary_tree.keys():
        return
    left_child = binary_tree[root][0]
    right_child = binary_tree[root][1]
    binary_tree_mirror[root] = [right_child, left_child]
    binaryTreeMirrorDict(left_child, binary_tree, binary_tree_mirror)
    binaryTreeMirrorDict(right_child, binary_tree, binary_tree_mirror)

def binaryTreeMirror(root: int, binary_tree: dict = {}) -> dict:
    """
    >>> binaryTreeMirror(1, { 1: [2,3], 2: [4,5], 3: [6,7], 7: [8,9]})
    {1: [3, 2], 2: [5, 4], 3: [7, 6], 7: [9, 8]}
    >>> binaryTreeMirror(5, { 1: [2,3], 2: [4,5], 3: [6,7], 7: [8,9]})
    {}
    >>> binaryTreeMirror\
    (1, { 1: [2,3], 2: [4,5], 3: [6,7], 4: [10,11], 5: [12,13],7: [8,9]})
    {1: [3, 2], 2: [5, 4], 4: [11, 10], 5: [13, 12], 3: [7, 6], 7: [9, 8]}
    """
    binary_tree_mirror = {}
    binaryTreeMirrorDict(root, binary_tree, binary_tree_mirror)
    return binary_tree_mirror


if __name__ == "__main__":
    binary_tree = { 1: [2,3], 2: [4,5], 3: [6,7], 4: [10,11], 5: [12,13],7: [8,9]}
    root = 1
    print("Binary tree:", sep=" ")
    print(binary_tree)
    binary_tree_mirror = binaryTreeMirror(root, binary_tree)
    print(" binary tree mirror:", sep=" ")
    print(binary_tree_mirror)
