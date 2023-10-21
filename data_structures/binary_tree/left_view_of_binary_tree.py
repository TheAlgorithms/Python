class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def fun(root, d, l):
    if root is None:
        return
    if l not in d:
        d[l] = root.data
    fun(root.left, d, l + 1)
    fun(root.right, d, l + 1)


def leftview(root):
    d = {}
    fun(root, d, 0)
    return list(d.values())


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
result = leftview(root)
print(result)
