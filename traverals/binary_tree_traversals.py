"""
This is pure python implementation of tree traversal algorithms
"""

import queue


class TreeNode:

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def build_tree():
    print("Enter the value of the root node: ", end="")
    data = eval(input())
    if data < 0:
        return None
    else:
        q = queue.Queue()
        tree_node = TreeNode(data)
        q.put(tree_node)
        while not q.empty():
            node_found = q.get()
            print("Enter the left node of %s: " % node_found.data, end="")
            left_data = eval(input())
            if left_data >= 0:
                left_node = TreeNode(left_data)
                node_found.left = left_node
                q.put(left_node)
            print("Enter the right node of %s: " % node_found.data, end="")
            right_data = eval(input())
            if right_data >= 0:
                right_node = TreeNode(right_data)
                node_found.right = right_node
                q.put(right_node)
    return tree_node


def pre_order(node):
    if not node:
        return
    print(node.data, end=" ")
    pre_order(node.left)
    pre_order(node.right)


def in_order(node):
    if not node:
        return
    in_order(node.left)
    print(node.data, end=" ")
    in_order(node.right)


def post_order(node):
    if not node:
        return
    post_order(node.left)
    post_order(node.right)
    print(node.data, end=" ")


def level_order(node):
    if not node:
        return
    q = queue.Queue()
    q.put(node)
    while not q.empty():
        node_dequeued = q.get()
        print(node_dequeued.data, end=" ")
        if node_dequeued.left:
            q.put(node_dequeued.left)
        if node_dequeued.right:
            q.put(node_dequeued.right)


if __name__ == '__main__':
    import sys
    print("\n********* Binary Tree Traversals ************\n")
    # For python 2.x and 3.x compatibility: 3.x has not raw_input builtin
    # otherwise 2.x's input builtin function is too "smart"
    if sys.version_info.major < 3:
        input_function = raw_input
    else:
        input_function = input

    node = build_tree()
    print("\n********* Pre Order Traversal ************")
    pre_order(node)
    print("\n******************************************\n")

    print("\n********* In Order Traversal ************")
    in_order(node)
    print("\n******************************************\n")

    print("\n********* Post Order Traversal ************")
    post_order(node)
    print("\n******************************************\n")

    print("\n********* Level Order Traversal ************")
    level_order(node)
    print("\n******************************************\n")
