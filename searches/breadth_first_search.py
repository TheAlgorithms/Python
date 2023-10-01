class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def searchBFS(root):
    if root is None:
        return

    queue = []
    queue.append(root)

    while queue:
        current_node = queue.pop(0)
        print(current_node.value, end=' ')

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

# Constructing the search tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Breadth-First Search traversal:")
searchBFS(root)