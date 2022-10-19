
# The diameter of the binary tree is defined as the total number of nodes on the longest path between two end nodes.
# Diameter = Left subtree height + Right subtree height + 1

# RECURSIVE APPROACH
# Time Complexity
'''
The time complexity of the above approach is O(n^2) where n is the number of nodes in the tree.
It is because, the function recursively calls itself, and hence, every node is visited at least
twice while calculating the diameter.
However, the space complexity of the recursive approach is O(n) because of recursion.
'''

'''class TreeNode:
    
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.max = 0
    def Diameter(self, root: TreeNode) -> int:
        if root is None: return 0
        def traverse(root):
            if root is None: return 0
            left = traverse(root.left)
            right = traverse(root.right)
            if left + right > self.max:
                self.max = left+right
            return max(left, right) + 1
        traverse(root)
        return self.max

if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(11)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(31)
    root.right = TreeNode(12)

    print(Solution().Diameter(root))'''

# Output = 3

# Iterative Approach
'''
Time Complexity
The time complexity using this approach is O(n) and therefore, it is considered to be an optimized solution 
for calculating the diameter of a binary tree. 
It is because using the iterative approach, we only visit the nodes of the tree once. 
At the same time, the space complexity of this approach is also O(n) where n is the number of nodes present in the tree.
'''

from collections import deque

class TreeNode:
    '''
    Tree Node
    '''
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
     def Diameter(self , root: TreeNode ):
        '''
        Function to find depth of the Binary Tree
        :param root: Root Node
        :return: Depth of the tree
        '''
        stack = deque ( [ root ] )
        depth = {None : 0}
        ans = 0
        while stack :
            node = stack.pop ()
            if not node :
                continue

            LDepth = depth.get ( node.left , None )
            RDepth = depth.get ( node.right , None )
            if LDepth== None or RDepth == None :
                stack.append ( node )
                stack.append ( node.left )
                stack.append ( node.right )
                continue

            depth [ node ] = max ( LDepth, RDepth ) + 1
            ans = max ( LDepth+ RDepth , ans )

        return ans
if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(11)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(31)
    root.right = TreeNode(12)

    print(f'Diameter is : {Solution().Diameter(root)}')

# Output Diameter is: 3