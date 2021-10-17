# The binary tree main node
class TreeNode:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None



# Function to compute the height of tree
def treeHeight(treeNode):
	if treeNode is None:
		return 0
	return 1 + max(treeHeight(treeNode.left), treeHeight(treeNode.right))

# Function to compute the diameter of tree
def treeDiameter(rootNode):
	if rootNode is None:
		return 0
	leftHeight = treeHeight(rootNode.left)
	rightHeight = treeHeight(rootNode.right)
	leftDiameter = treeDiameter(rootNode.left)
	rightDiameter = treeDiameter(rootNode.right)

	return max(leftHeight + rightHeight + 1, max(leftDiameter, rightDiameter))


# Calling classes & functions
rootNode = TreeNode(2)
rootNode.left = TreeNode(4)
rootNode.right = TreeNode(6)
rootNode.left.left = TreeNode(8)
rootNode.left.right = TreeNode(10)

print(treeDiameter(rootNode))
