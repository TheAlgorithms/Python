
# Class containing left and
# right child of current
# node and key value
class Node:

def __init__(self,item = 0):
	self.key = item
	self.left,self.right = None,None


# Root of BST
root = Node()

root = None

# This method mainly
# calls insertRec()
def insert(key):
global root
root = insertRec(root, key)

# A recursive function to
# insert a new key in BST
def insertRec(root, key):

# If the tree is empty,
# return a new node

if (root == None):
	root = Node(key)
	return root

# Otherwise, recur
# down the tree
if (key < root.key):
	root.left = insertRec(root.left, key)
elif (key > root.key):
	root.right = insertRec(root.right, key)

# return the root
return root

# A function to do
# inorder traversal of BST
def inorderRec(root):
if (root != None):
	inorderRec(root.left)
	print(root.key ,end = " ")
	inorderRec(root.right)
	
def treeins(arr):
for i in range(len(arr)):
	insert(arr[i])

# Driver Code
arr = [5, 4, 7, 2, 11]
treeins(arr)
inorderRec(root)
