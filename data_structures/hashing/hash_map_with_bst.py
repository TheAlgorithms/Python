# Binary Search Tree Node.
class Node:
	def __init__(cls, 
				 key = None):
		cls.key = key
		cls.value = 1
		cls.left = None
		cls.right = None


# Binary Search Tree.
class BST:
	def __init__(cls):
		cls.root = None

	def insert_node(cls, 
					root, 
					key):
		""" 
        Insert or Update the node and returns the updated root 
        """
		if root is None: return Node(key)
		else:
			if root.key == key:
				root.value += 1
				return root
			elif root.key < key: 
				root.right = cls.insert_node(root.right, key)
			else:
				root.left = cls.insert_node(root.left, key)
		return root
	
	def search_node(cls, 
					root, 
					key):
		""" 
        If node with given key is found it returns the root else a None value 
        """
		if root is None or root.key == key:
			return root
		if root.key < key:
			return cls.search_node(root.right, key)
		return cls.search_node(root.left, key)

	def print_inorder(cls,
					  root):
		if root:
			cls.inorder(root.left)
			print(root.key)
			cls.inorder(root.right)

	def get_max_value(cls, 
					  root):
		""" 
        Returns the value of node with max frequency 
        """
		if root:
			return max(
				root.value, 
				cls.get_max_value(root.left), 
				cls.get_max_value(root.right)
				)
		else: return 0


# Hash table to store key:value pairs
class HashMap:
	def __init__(cls):
		cls.table_size = 100
		cls.prime_no = 799
		cls.hash_map = [BST()] * cls.table_size  

	def get_hash_code(cls, 
					  key):
		code = 0
		size = len(key)
		for i in range(0, size):
			code = (
					(i 
					 * cls.prime_no 
					 * ord(key[i])
					 ) 
					 + code
					) % cls.table_size
		return code

	def add(cls, 
			key):
		index = cls.get_hash_code(key)
		tree = cls.hash_map[index]
		tree.root = tree.insert_node(tree.root, key)

	def find(cls, 
			 key):
		index = cls.get_hash_code(key)
		tree = cls.hash_map[index]
		return tree.search_node(tree.root, key)
