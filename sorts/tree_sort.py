"""
Tree_sort algorithm.

Build a BST and in order traverse.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        if val < self.val:
            if self.left is None:
                self.left = Node(val)
            else:
                self.left.insert(val)
        elif val > self.val:
            if self.right is None:
                self.right = Node(val)
            else:
                self.right.insert(val)

def inorder(root):
    if root:
        yield from inorder(root.left)
        yield root.val
        yield from inorder(root.right)

def tree_sort(arr):
    if not arr:
        return []
    root = Node(arr[0])
    for val in arr[1:]:
        root.insert(val)
    return list(inorder(root))

if __name__ == "__main__":
    sorted_array = tree_sort([10, 1, 3, 2, 9, 14, 13])
    print(sorted_array)
