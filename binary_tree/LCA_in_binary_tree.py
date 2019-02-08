# Lowest Common Ancestor in a Binary Tree


class Node:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def find_path(root, path, k):
    if root is None:
        return False

    path.append(root.key)

    if root.key == k:
        return True

    if ((root.left is not None and find_path(root.left, path, k)) or
            (root.right is not None and find_path(root.right, path, k))):
        return True

    path.pop()
    return False


def LCA(root, n1, n2):
    path1 = []
    path2 = []

    if not find_path(root, path1, n1) or not find_path(root, path2, n2):
        return -1

    i = 0
    while i < len(path1) and i < len(path2):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i - 1]


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.left.right.left = Node(10)
root.left.right.right = Node(11)
root.right.left.left = Node(12)
root.right.left.right = Node(13)
root.right.right.left = Node(14)
root.right.right.right = Node(15)

print("LCA(10, 11) = " + str(LCA(root, 10, 11)))

print("LCA(12, 15) = " + str(LCA(root, 12, 15)))

print("LCA(7, 13) = " + str(LCA(root, 7, 13)))

print("LCA(5, 14) = " + str(LCA(root, 5, 14)))
