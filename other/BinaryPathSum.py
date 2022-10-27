class Node:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
 
"""
 Given a tree and a sum, return
 true if there is a path from the root
 down to a leaf, such that
 adding up all the values along the path
 equals the given sum.
  
 Strategy: subtract the node
 value from the sum when recurring down,
 and check to see if the sum
 is 0 when you run out of tree.
"""
# s is the sum
 
 
def hasPathSum(node, s):
    ans = 0
    subSum = s - node.data
 
    # If we reach a leaf node and sum becomes 0, then
    # return True
    if(subSum == 0 and node.left == None and node.right == None):
        return True
 
    # Otherwise check both subtrees
    if node.left is not None:
        ans = ans or hasPathSum(node.left, subSum)
    if node.right is not None:
        ans = ans or hasPathSum(node.right, subSum)
 
    return ans
 
# Driver's Code
if __name__ == "__main__":
    s = 21
    root = Node(10)
    root.left = Node(8)
    root.right = Node(2)
    root.left.right = Node(5)
    root.left.left = Node(3)
    root.right.left = Node(2)
     
    # Function call
    if hasPathSum(root, s):
        print("There is a root-to-leaf path with sum %d" % (s))
    else:
        print("There is no root-to-leaf path with sum %d" % (s))
 
