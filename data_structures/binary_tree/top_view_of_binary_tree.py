from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.horiz_dist = 0


def topview(root):
    if not root:
        return []

    d = {}
    queue = deque()
    root.horiz_dist = 0
    queue.append(root)

    while queue:
        cur = queue.popleft()
        horiz_dist = cur.horiz_dist
        if horiz_dist not in d:
            d[horiz_dist] = cur.data
        if cur.left:
            cur.left.horiz_dist = horiz_dist - 1
            queue.append(cur.left)
        if cur.right:
            cur.right.horiz_dist = horiz_dist + 1
            queue.append(cur.right)
    top_view_nodes = [d[key] for key in sorted(d)]
    return top_view_nodes


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

result = topview(root)
print(result)
