from collections import deque


class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.horiz_dist = 0


def topview(root):
    if not root:
        return []

    d = {}
    q = deque()
    root.horiz_dist = 0
    q.append(root)
    while q:
        cur = q.popleft()
        horiz_dist = cur.horiz_dist
        if horiz_dist not in d:
            d[horiz_dist] = cur.data
        if cur.left:
            cur.left.horiz_dist = horiz_dist - 1
            q.append(cur.left)
        if cur.right:
            cur.right.horiz_dist = horiz_dist + 1
            q.append(cur.right)
    top_view_nodes = [d[key] for key in sorted(d)]
    return top_view_nodes


root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
root.right.left = node(6)
root.right.right = node(7)

result = topview(root)
print(result)
