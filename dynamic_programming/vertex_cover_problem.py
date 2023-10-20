# A naive recursive Python3 implementation
# for vertex cover problem for a tree

# A utility function to find min of two integers

# A binary tree node has data, pointer to
# left child and a pointer to right child
class Node:

	def __init__(self, x):

		self.data = x
		self.left = None
		self.right = None

# The function returns size of
# the minimum vertex cover
def vCover(root):

	# The size of minimum vertex cover
	# is zero if tree is empty or there
	# is only one node
	if (root == None):
		return 0

	if (root.left == None and
	root.right == None):
		return 0

	# Calculate size of vertex cover when
	# root is part of it
	size_incl = (1 + vCover(root.left) +
					vCover(root.right))

	# Calculate size of vertex cover
	# when root is not part of it
	size_excl = 0
	if (root.left):
	size_excl += (1 + vCover(root.left.left) +
						vCover(root.left.right))
	if (root.right):
	size_excl += (1 + vCover(root.right.left) +
						vCover(root.right.right))

	# Return the minimum of two sizes
	return min(size_incl, size_excl)

# Driver Code
if __name__ == '__main__':

	# Let us construct the tree
	# given in the above diagram
	root = Node(20)
	root.left = Node(8)
	root.left.left = Node(4)
	root.left.right = Node(12)
	root.left.right.left = Node(10)
	root.left.right.right = Node(14)
	root.right = Node(22)
	root.right.right = Node(25)

	print("Size of the smallest vertex cover is", vCover(root))

# This code is contributed by mohit kumar 29
