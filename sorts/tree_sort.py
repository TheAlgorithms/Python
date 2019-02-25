# Tree_sort algorithm
# Build a BST and in order traverse.


class node:
    # BST data structure
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        if self.val is not None:
            if val < self.val:
                if self.left is None:
                    self.left = node(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = node(val)
                else:
                    self.right.insert(val)
            else:  # duplicate value, displace tree left
                new_left = node(val)
                new_left.left = self.left
                self.left = new_left


def inorder(root, res):
    # Recursive travesal
    if root:
        inorder(root.left, res)
        res.append(root.val)
        inorder(root.right, res)


def treesort(arr):
    # Build BST
    if len(arr) == 0:
        return []
    root = node(arr[0])
    for i in range(1, len(arr)):
        root.insert(arr[i])
    # Traverse BST in order.
    res = []
    inorder(root, res)
    return res


print(treesort([10, 1, 3, 2, 9, 14, 13]))
