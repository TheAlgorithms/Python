''' 
The diameter/width of a tree is defined as the number of nodes on the longest path between two end nodes. 
'''

# A binary tree Node

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
  
# utility class to pass height object
class Height:
	def __init__(self):
		self.h = 0


# Function to calculate diameter of the given binary tree
def calculate_diameter(root:Node, height:int) -> int:

	# to store height of left and right subtree
	lh = Height()
	rh = Height()

	# base condition- when binary tree is empty
	if root is None:
		height.h = 0
		return 0

	# ldiameter --> diameter of left subtree
	# rdiameter --> diameter of right subtree

	# height of left subtree and right subtree is obtained from lh and rh and returned value of function is stored in ldiameter and rdiameter

	ldiameter = calculate_diameter(root.left, lh)
	rdiameter = calculate_diameter(root.right, rh)

	# height of tree will be max of left subtree
	# height and right subtree height plus1

	height.h = max(lh.h, rh.h) + 1

	# return maximum of the following
	# 1)left diameter
	# 2)right diameter
	# 3)left height + right height + 1
	return max(lh.h + rh.h + 1, max(ldiameter, rdiameter))


def diameter(root:Node) -> int:
	height = Height()
	return calculate_diameter(root, height)


if __name__ == "__main__":
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)

	"""
Constructed binary tree is 
		1
	   / \
	  2	  3
	 / \
	4	 5
"""

	print("The diameter of the binary tree is:", end=" ")
	print(diameter(root))
