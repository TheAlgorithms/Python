class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def insert(temp, data):
    que = [temp]
    while len(que):
        temp = que[0]
        que.pop(0)
        if not temp.left:
            if data is not None:
                temp.left = TreeNode(data)
            else:
                temp.left = TreeNode(0)
            break
        else:
            que.append(temp.left)
            if not temp.right:
                if data is not None:
                    temp.right = TreeNode(data)
                else:
                    temp.right = TreeNode(0)
                break
            else:
                que.append(temp.right)


def make_tree(elements):
    tree = TreeNode(elements[0])
    for element in elements[1:]:
        insert(tree, element)
    return tree


class Solution:
    def lowestcommonancestor(self, root, p, q):
        if not root:
            return None
        if root.data in (p, q):
            return root
        left = self.lowestcommonancestor(root.left, p, q)
        right = self.lowestcommonancestor(root.right, p, q)
        if right and left:
            return root
        return right or left


ob1 = Solution()
tree = make_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
print(ob1.lowestcommonancestor(tree, 5, 1).data)
