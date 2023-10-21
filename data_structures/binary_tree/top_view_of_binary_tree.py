from collections import deque


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.horiz_dist = 0


def topView(root):
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


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

result = topView(root)
print(result)
