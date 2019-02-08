# Lowest Common Ancestor in a Binary Search Tree


class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def LCA(root, n1, n2):

    if root is None:
        return None

    if root.key > n1 and root.key > n2:
        return LCA(root.left, n1, n2)

    if root.key < n1 and root.key < n2:
        return LCA(root.right, n1, n2)

    return root


root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

print("LCA(10, 14) = " + str(LCA(root, 10, 14).key))

print("LCA(8, 14) = " + str(LCA(root, 8, 14).key))

print("LCA(10, 22) = " + str(LCA(root, 10, 22).key))
