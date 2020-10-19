# Python3 program to find the all 
# full nodes in a given binary tree 

# Binary Tree Node 
""" utility that allocates a newNode 
with the given key """
class newNode: 

	# Construct to create a newNode 
	def __init__(self, key): 
		self.data = key 
		self.left = None
		self.right = None

# Traverses given tree in Inorder 
# fashion and prints all nodes that 
# have both children as non-empty. 
def findFullNode(root) : 

	if (root != None) : 
	
		findFullNode(root.left) 
		if (root.left != None and
			root.right != None) : 
			print(root.data, end = " ") 
		findFullNode(root.right) 

# Driver Code 
if __name__ == '__main__': 

	root = newNode(1) 
	root.left = newNode(2) 
	root.right = newNode(3) 
	root.left.left = newNode(4) 
	root.right.left = newNode(5) 
	root.right.right = newNode(6) 
	root.right.left.right = newNode(7) 
	root.right.right.right = newNode(8) 
	root.right.left.right.left = newNode(9) 
	findFullNode(root) 

