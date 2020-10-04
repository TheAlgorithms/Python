# Created by susmith98

from collections import deque

"""
Problem Description:
Given a binary tree, print it's right view from top to bottom.

Solution Logic:
Imagine binary tree as y axis from right view and root node is at index 0.

If parent node is at y-axis index idx, then
-> Child (both left & right)is at y-axis index idx-1

Multiple nodes might be present at y-axis index idx at different level's of tree.
To tackle this scenario,
Consider the node which occurs last (right most) at every level.
To consider the right most node at every level, BFS is used.
"""


def rightViewDict(
    root: int, binary_tree: dict = {}, y_axis_dict: dict = {},
):
    queue = deque()
    # y axis index of root is 0
    queue.append((root, 0))
    while len(queue) > 0:
        (parent, y_axis_idx) = queue.popleft()
        y_axis_dict[y_axis_idx] = parent
        # Check if current node has children
        if parent in binary_tree:
            # Check for left child
            if binary_tree[parent][0] is not None:
                queue.append((binary_tree[parent][0], y_axis_idx - 1))
            # Check for right child
            if binary_tree[parent][1] is not None:
                queue.append((binary_tree[parent][1], y_axis_idx - 1))
    return


def getRightViewListFromDict(y_axis_dict: dict = {}) -> list:
    if len(y_axis_dict) == 0:
        return []
    y_axis_list = []
    for idx in reversed(sorted(y_axis_dict.keys())):
        y_axis_list.append(y_axis_dict[idx])
    return y_axis_list


def rightView(root: int, binary_tree: dict = {}) -> list:
    """
    >>> rightView(1, { 1: [2,3], 2: [4,5], 3: [6,7], 7: [8,9]})
    [1, 3, 7, 9]
    >>> rightView(5, { 1: [2,3], 2: [4,5], 3: [6,7], 7: [8,9]})
    []
    >>> rightView(1, { 1: [2,3], 2: [4,5], 3: [6,7], 4: [10,11], 5: [12,13],7: [8,9]})
    [1, 3, 7, 9]
    """
    if root not in binary_tree.keys() or len(binary_tree) == 0:
        return []
    y_axis_dict = {}
    rightViewDict(root, binary_tree, y_axis_dict=y_axis_dict)
    return getRightViewListFromDict(y_axis_dict)


if __name__ == "__main__":
    binary_tree = { 1: [2,3], 2: [4,5], 3: [6,7], 4: [10,11], 5: [12,13],7: [8,9]}
    root = 1
    y_axis_list = rightView(root, binary_tree)
    print("Binary tree:", sep=" ")
    print(binary_tree)
    print("Right view from top to bottom:", sep=" ")
    print(y_axis_list)
