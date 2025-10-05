from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def are_cousins(root, x, y):
    if not root:
        return False

    queue = deque([(root, None)])  # (node, parent)

    while queue:
        size = len(queue)
        x_parent = y_parent = None

        for _ in range(size):
            node, parent = queue.popleft()

            if node.val == x:
                x_parent = parent
            if node.val == y:
                y_parent = parent

            if node.left:
                queue.append((node.left, node))
            if node.right:
                queue.append((node.right, node))

        # After one level is processed
        if x_parent and y_parent:
            return x_parent != y_parent  # True if different parents
        if (x_parent and not y_parent) or (y_parent and not x_parent):
            return False  # Found one but not the other

    return False


# 🔹 Example Usage:
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(5)

print("Are 4 and 5 cousins?", are_cousins(root, 4, 5))  # ✅ True
print("Are 2 and 3 cousins?", are_cousins(root, 2, 3))  # ❌ False
