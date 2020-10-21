# -*- coding: utf-8 -*-
# https://www.geeksforgeeks.org/print-ancestors-of-a-given-node-in-binary-tree/

class TreeNode():  
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def ancestor(root, key):
    if root is None:
        return False
    if(root.val == key):
        return True
    x = ancestor(root.left, key)
    y = ancestor(root.right, key)
    if(x or y):
        print(root.val,end= " ")
        return True   
    return False
                       
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

key = int(input("Enter any node value to get ancestors: "))
print("The ancestors of the key ", key, " are: ")
print("\nAncestors exist: ", ancestor(root, key))
