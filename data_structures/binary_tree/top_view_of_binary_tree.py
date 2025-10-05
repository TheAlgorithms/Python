from collections import deque

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

class Solution:
    # Function to return the top view of the binary tree
    def topView(self, root):
        # List to store the result
        ans = []
        
        # Check if the tree is empty
        if root is None:
            return ans
        
        # Dictionary to store the top view nodes based on their vertical positions
        mpp = {}
        
        # Queue for BFS traversal, each element is a pair containing node and its vertical position
        q = deque([(root, 0)])
        
        # BFS traversal
        while q:
            # Retrieve the node and its vertical position from the front of the queue
            node, line = q.popleft()
            
            # If the vertical position is not already in the map, add the node's data to the map
            if line not in mpp:
                mpp[line] = node.data
            
            # Process left child
            if node.left:
                # Push the left child with a decreased vertical position into the queue
                q.append((node.left, line - 1))
            
            # Process right child
            if node.right:
                # Push the right child with an increased vertical position into the queue
                q.append((node.right, line + 1))
        
        # Transfer values from the map to the result list
        for key in sorted(mpp.keys()):
            ans.append(mpp[key])
        
        return ans

# Creating a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(10)
root.left.left.right = TreeNode(5)
root.left.left.right.right = TreeNode(6)
root.right = TreeNode(3)
root.right.right = TreeNode(10)
root.right.left = TreeNode(9)

solution = Solution()

# Get the top view traversal
top_view = solution.topView(root)

# Print the result
print("Top View Traversal:")
for node in top_view:
    print(node, end=" ")
