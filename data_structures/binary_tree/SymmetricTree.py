# Python program to check if a given Binary Tree is 
# symmetric or not 

# Node structure 
class Node: 

	# Utility function to create new node 
	def __init__(self, key): 
		self.key = key 
		self.left = None
		self.right = None

# Returns True if trees with roots as root1 and root 2 
# are mirror 
def isMirror(root1 , root2): 
	# If both trees are empty, then they are mirror images 
	if root1 is None and root2 is None: 
		return True
	
	""" For two trees to be mirror images, the following three 
		conditions must be true 
		1 - Their root node's key must be same 
		2 - left subtree of left tree and right subtree 
		of the right tree have to be mirror images 
		3 - right subtree of left tree and left subtree 
		of right tree have to be mirror images 
	"""
	if (root1 is not None and root2 is not None): 
			if root1.key == root2.key: 
				return (isMirror(root1.left, root2.right)and
				isMirror(root1.right, root2.left)) 

	# If neither of the above conditions is true then root1 
	# and root2 are not mirror images 
	return False

def isSymmetric(root): 

	# Check if tree is mirror of itself 
	return isMirror(root, root) 

# Driver Program 
# Let's construct the tree show in the above figure 
root = Node(1) 
root.left = Node(2) 
root.right = Node(2) 
root.left.left = Node(3) 
root.left.right = Node(4) 
root.right.left = Node(4) 
root.right.right = Node(3) 
print "1" if isSymmetric(root) == True else "0"

