"""
This is pure python implementation of tree traversal algorithms
"""
from __future__ import print_function
import queue


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def build_tree():
    print("\n********Press N to stop entering at any point of time********\n")
    print("Enter the value of the root node: ", end="")
    check=input()
    if check=='N' or check=='n':
        return None 
    data=int(check)
    q = queue.Queue()
    tree_node = TreeNode(data)
    q.put(tree_node)
    while not q.empty():
        node_found = q.get()
        print("Enter the left node of %s: " % node_found.data, end="")
        check=input()
        if check=='N' or check =='n':
            return tree_node
        left_data = int(check)
        left_node = TreeNode(left_data)
        node_found.left = left_node
        q.put(left_node)
        print("Enter the right node of %s: " % node_found.data, end="")
        check = input()
        if check == 'N' or check == 'n':
            return tree_node
        right_data = int(check)
        right_node = TreeNode(right_data)
        node_found.right = right_node
        q.put(right_node)


def pre_order(node):
    no_of_nodes=0
    if not isinstance(node, TreeNode) or not node:
        return 0
    print(node.data, end=" ")
    return 1+pre_order(node.left)#counting number of left nodes
    return 1+pre_order(node.right)#counting number of right nodes


def in_order(node):
    leaf_count=0
    if not isinstance(node, TreeNode) or not node:
        return 0
    in_order(node.left)
    print(node.data, end=" ")
    return 1+in_order(node.right)#counting number of leaf nodes


def post_order(node):
    if not isinstance(node, TreeNode) or not node:
        return
    post_order(node.left)
    post_order(node.right)
    print(node.data, end=" ")


def level_order(node):
    if not isinstance(node, TreeNode) or not node:
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
    no_of_nodes=pre_order(node)
    print("\n******************************************\n")

    print("\n********* In Order Traversal ************")
    leaf_count=in_order(node)
    print("\n******************************************\n")

    print("\n********* Post Order Traversal ************")
    post_order(node)
    print("\n******************************************\n")

    print("\n********* Level Order Traversal ************")
    level_order(node)
    print("\n******************************************\n")
    print("\nTotal number of nodes : ",no_of_nodes)
    print("\nTotal number of leafs : ",leaf_count)

