"""
This is pure python implementation of tree traversal algorithms
"""
from __future__ import print_function
import queue

try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def build_tree():
    print("\n********Press N to stop entering at any point of time********\n")
    print("Enter the value of the root node: ", end="")
    check = raw_input().strip().lower()
    if check == 'n':
        return None 
    data = int(check)
    q = queue.Queue()
    tree_node = TreeNode(data)
    q.put(tree_node)
    while not q.empty():
        node_found = q.get()
        print("Enter the left node of %s: " % node_found.data, end="")
        check = raw_input().strip().lower()
        if check == 'n':
            return tree_node
        left_data = int(check)
        left_node = TreeNode(left_data)
        node_found.left = left_node
        q.put(left_node)
        print("Enter the right node of %s: " % node_found.data, end="")
        check = raw_input().strip().lower()
        if check == 'n':
            return tree_node
        right_data = int(check)
        right_node = TreeNode(right_data)
        node_found.right = right_node
        q.put(right_node)

def pre_order(node):
    if not isinstance(node, TreeNode) or not node:
        return
    print(node.data, end=" ")
    pre_order(node.left)
    pre_order(node.right)

def in_order(node):
    if not isinstance(node, TreeNode) or not node:
        return
    in_order(node.left)
    print(node.data, end=" ")
    in_order(node.right)


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

#iteration version
def pre_order_iter(node):
    if not isinstance(node, TreeNode) or not node:
        return
    stack = []
    n = node
    while n or stack:
        while n:    #start from root node, find its left child
            print(n.data, end=" ")
            stack.append(n)
            n = n.left
        #end of while means current node doesn't have left child
        n = stack.pop()
        #start to traverse its right child
        n = n.right

def in_order_iter(node):
    if not isinstance(node, TreeNode) or not node:
        return
    stack = []
    n = node
    while n or stack:
        while n:
            stack.append(n)
            n = n.left
        n = stack.pop()
        print(n.data, end=" ")
        n = n.right

def post_order_iter(node):
    if not isinstance(node, TreeNode) or not node:
        return
    stack1, stack2 = [], []
    n = node
    stack1.append(n)
    while stack1:   #to find the reversed order of post order, store it in stack2
        n = stack1.pop()
        if n.left:
            stack1.append(n.left)
        if n.right:
            stack1.append(n.right)
        stack2.append(n)
    while stack2:   #pop up from stack2 will be the post order
        print(stack2.pop().data, end=" ")

if __name__ == '__main__':
    print("\n********* Binary Tree Traversals ************\n")

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

    print("\n********* Pre Order Traversal - Iteration Version ************")
    pre_order_iter(node)
    print("\n******************************************\n")

    print("\n********* In Order Traversal - Iteration Version ************")
    in_order_iter(node)
    print("\n******************************************\n")

    print("\n********* Post Order Traversal - Iteration Version ************")
    post_order_iter(node)
    print("\n******************************************\n")