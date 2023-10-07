"""
Tree_sort algorithm.

Build a BST and in order traverse.
"""


class Node:
    # BST data structure
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        if self.val:
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
        else:
            self.val = val


def inorder(root, res):
    # Recursive traversal
    if root:
        inorder(root.left, res)
        res.append(root.val)
        inorder(root.right, res)


def tree_sort(arr):
    """

    >>> tree_sort([5, 2, 7])
    [2, 5, 7]

    >>> tree_sort([5, -4, 9, 2, 7])
    [-4, 2, 5, 7, 9]
    
    >>> tree_sort([5, 6, 1, -1, 4, 37, 2, 7])
    [-1, 1, 2, 4, 5, 6, 7, 37]
    
    """
    # Build BST
    if len(arr) == 0:
        return arr
    root = Node(arr[0])
    for i in range(1, len(arr)):
        root.insert(arr[i])
    # Traverse BST in order.
    res = []
    inorder(root, res)
    return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()

