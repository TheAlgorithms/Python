# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        def inorder(root):
            if root is None:
                inorder.str_ = inorder.str_ + 'None' + ' '
                return
            inorder(root.left)
            inorder.str_ = inorder.str_ + str(root.val) + ' '
            inorder(root.right)
            
        def preorder(root):
            if root is None:
                preorder.str_ = preorder.str_ + 'None' + ' '
                return
            preorder.str_ = preorder.str_ + str(root.val) + ' '
            preorder(root.left)
            preorder(root.right)
            
        inorder.str_ = ''
        preorder.str_ = ''
        
        inorder(root)
        preorder(root)
                
        str_ = inorder.str_ + '/' + preorder.str_
        return str_
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        def buildTree(inorder, preorder, start, end):
            if start > end:
                return None
            
            tNode = TreeNode(preorder[buildTree.preIndex])
            buildTree.preIndex += 1
            
            if start == end:
                return tNode
            
            index = search(inorder, start, end, tNode.val)
            tNode.left = buildTree(inorder, preorder, start, index-1)
            tNode.right = buildTree(inorder, preorder, index+1, end)
            
            return tNode
        
        def search(inorder, start, end, val):
            for i in range(start, end+1):
                if inorder[i] == val:
                    return i
        
        buildTree.preIndex = 0
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

        #root = buildTree(inorder, preorder, 0, len(inorder)-1)
        def buildPreorder(root,preOrder,preorderIdx):
            if len(preOrder) == 0:
                return None
            if preOrder[0] == None :
                #preorderIdx[0]+=1
                preOrder.pop(0)
                return None
            
            root = TreeNode(preOrder.pop(0))
            root.left = buildPreorder(root.left,preOrder,preorderIdx)
            root.right = buildPreorder(root.right,preOrder,preorderIdx)
            return root
        
        preorderIdx = [0]
        root = None
        root = buildPreorder(root,preorder,preorderIdx)
        return root
    
        
    
    
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))