"""
Traversing a binary tree in Inorder,Preorder, Postorder way using Iterative method
"""

# Node of Tree
class Node:
    def __init__(self,data):
        self.val = data
        self.left = None
        self.right = None

# Inorder tree traversal
def print_Inorder(root):
    current = root
    stack = []
    while True:
        if current!= None:
            stack.append(current)
            current = current.left
        elif stack:
            key = stack.pop()
            print(key.val, end="->")
            current = key.right
        else:
            break
    return


# Preorder tree traversal
def print_Preorder(root):
    current = root
    stack = []
    stack.append(current)
    while stack:
        key = stack.pop()
        print(key.val, end="->")
        if key.right:
            stack.append(key.right)
        if key.left:
            stack.append(key.left)
    return

# Postorder tree traversal
def print_Postorder(root):
    current = root
    stack1 = []
    stack2 = []
    stack1.append(current)
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    while stack2:
        node = stack2.pop()
        print(node.val ,end="->")
    return


# Driver's Code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print("Inorder=")
print_Inorder(root)
print("\n")
print("preorder=")
print_Preorder(root)
print("\n")
print("postorder=")
print_Postorder(root)
