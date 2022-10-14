# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def inorder(root: TreeNode) -> None:
            if root is None:
                inorder.str_ = inorder.str_ + "None" + " "
                return
            inorder(root.left)
            inorder.str_ = inorder.str_ + str(root.val) + " "
            inorder(root.right)

        def preorder(root: TreeNode) -> None:
            if root is None:
                preorder.str_ = preorder.str_ + "None" + " "
                return
            preorder.str_ = preorder.str_ + str(root.val) + " "
            preorder(root.left)
            preorder(root.right)

        inorder.str_ = ""
        preorder.str_ = ""

        inorder(root)
        preorder(root)

        str_ = inorder.str_ + "/" + preorder.str_
        return str_

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def build_tree(inorder, preorder, start, end):
            if start > end:
                return None

            t_node = TreeNode(preorder[build_tree.pre_index])
            build_tree.pre_index += 1

            if start == end:
                return t_node

            index = search(inorder, start, end, t_node.val)
            t_node.left = build_tree(inorder, preorder, start, index - 1)
            t_node.right = build_tree(inorder, preorder, index + 1, end)

            return t_node

        def search(inorder, start, end, val):
            for i in range(start, end + 1):
                if inorder[i] == val:
                    return i

        build_tree.pre_index = 0
        data = data.split("/")
        in_ = data[0]
        pre = data[1]

        in_ = in_.split()
        inorder = []
        for i in in_:
            if i == "None":
                inorder.append(None)
            else:
                inorder.append(int(i))

        pre = pre.split()
        preorder = []
        for i in pre:
            if i == "None":
                preorder.append(None)
            else:
                preorder.append(int(i))

        def build_preorder(root, preorder, preorder_idx):
            if len(preorder) == 0:
                return None
            if preorder[0] == None:
                # preorderIdx[0]+=1
                preorder.pop(0)
                return None

            root = TreeNode(preorder.pop(0))
            root.left = build_preorder(root.left, preorder, pre_index)
            root.right = build_preorder(root.right, preorder, pre_index)
            return root

        pre_index = [0]
        root = None
        root = build_preorder(root, preorder, pre_index)
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
