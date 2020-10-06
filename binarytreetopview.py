from collections import deque

"""
Problem Description:
Given a binary tree, print it's top view from left to right.
Solution Logic:
Imagine binary tree as x axis from top view and root node is at index 0.
If parent node is at x-axis index idx, then
-> left child is at x-axis index idx-1
-> right child is at x-axis index idx + 1
Multiple nodes might be present at x-axis index idx on different depth's of tree.
To tackle this scenario,
Consider the node at the lowest depth in tree as we want the top view.
To consider the node at the lowest depth, BFS is used.
"""


def topVDict(
    root: int, binary_tree: dict = {}, x_axis_dict: dict = {},
    root: int,
    binary_tree: dict = {},
    x_axis_dict: dict = {},
):
    queue = deque()
    # x axis index of root is 0
    queue.append((root, 0))
    while len(queue) > 0:
        (parent, x_axis_idx) = queue.popleft()
        if x_axis_idx not in x_axis_dict:
            x_axis_dict[x_axis_idx] = parent
        # Check if current node has children
        if parent in binary_tree:
            # Check for left child
            if binary_tree[parent][0] is not None:
                queue.append((binary_tree[parent][0], x_axis_idx - 1))
            # Check for right child
            if binary_tree[parent][1] is not None:
                queue.append((binary_tree[parent][1], x_axis_idx + 1))
    return


def getTopViewListFromDict(x_axis_dict: dict = {}) -> list:
    if len(x_axis_dict) == 0:
        return []
    x_axis_list = []
    for idx in sorted(x_axis_dict.keys()):
        x_axis_list.append(x_axis_dict[idx])
    return x_axis_list


def topV(root: int, binary_tree: dict = {}) -> list:
    """
    >>> topV(1, { 1: [2,3], 2: [4,5], 3: [6,7], 7: [8,9]})
    [4, 2, 1, 3, 7, 9]
    >>> topV(5, { 1: [2,3], 2: [4,5], 3: [6,7], 7: [8,9]})
    []
    >>> topV(1, { 1: [2,3], 2: [4,5], 3: [6,7], 4: [10,11], 5: [12,13],7: [8,9]})
    [10, 4, 2, 1, 3, 7, 9]
    """
    if root not in binary_tree.keys() or len(binary_tree) == 0:
        return []
    x_axis_dict = {}
    topVDict(root, binary_tree, x_axis_dict=x_axis_dict)
    return getTopViewListFromDict(x_axis_dict)


if __name__ == "__main__":
    binary_tree = {1: [2, 3], 2: [4, 5], 3: [6, 7], 4: [10, 11], 5: [12, 13], 7: [8, 9]}
    root = 1
    x_axis_list = topV(root, binary_tree)
    print("Binary tree:", sep=" ")
    print(binary_tree)
    print("Top view from left to right:", sep=" ")
    print(x_axis_list)
