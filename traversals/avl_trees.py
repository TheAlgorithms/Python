

#creating the node
class TreeNode(object): 
	def __init__(self, val): 
		self.val = val 
		self.left = None
		self.right = None
		self.height = 1


#creating the tree on which individual nodes will be attached
# according to the rule followed as in AVL tree

class AVL_Tree(object): 

	def insert(self, root, key): 
	

		if not root: 
			return TreeNode(key) 
		elif key < root.val: 
			root.left = self.insert(root.left, key) 
		else: 
			root.right = self.insert(root.right, key) 

		root.height = 1 + max(self.getHeight(root.left), 
						self.getHeight(root.right)) 

		balance = self.getBalance(root) 

		if balance > 1 and key < root.left.val: 
			return self.rightRotate(root) 

		if balance < -1 and key > root.right.val: 
			return self.leftRotate(root) 

		if balance > 1 and key > root.left.val: 
			root.left = self.leftRotate(root.left) 
			return self.rightRotate(root) 

		# Case 4 - Right Left 
		if balance < -1 and key < root.right.val: 
			root.right = self.rightRotate(root.right) 
			return self.leftRotate(root) 

		return root 

	def leftRotate(self, z): 

		y = z.right 
		T2 = y.left 

		# Perform rotation 
		y.left = z 
		z.right = T2 

		# Update heights 
		z.height = 1 + max(self.getHeight(z.left), 
						self.getHeight(z.right)) 
		y.height = 1 + max(self.getHeight(y.left), 
						self.getHeight(y.right)) 

		return (y) 

	def rightRotate(self, z): 

		y = z.left 
		T3 = y.right 

		# Perform rotation 
		y.right = z 
		z.left = T3 

		# Update heights 
		z.height = 1 + max(self.getHeight(z.left), 
						self.getHeight(z.right)) 
		y.height = 1 + max(self.getHeight(y.left), 
						self.getHeight(y.right)) 

		return (y)

	def getHeight(self, root): 
		if (not root): 
			return 0

		return (root.height) 

	def getBalance(self, root): 
		if (not root): 
			return 0

		return self.getHeight(root.left) - self.getHeight(root.right) 

	def preOrder(self, root): 

		if (not root): 
		    return

        print(root.val)
		self.preOrder(root.left) 
		self.preOrder(root.right) 



myTree = AVL_Tree() 
root = None

#insertion operations
root = myTree.insert(root, 10) 
root = myTree.insert(root, 20) 
root = myTree.insert(root, 30) 
root = myTree.insert(root, 40) 
root = myTree.insert(root, 50) 
root = myTree.insert(root, 25) 

# print(getHeight(root))