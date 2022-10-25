class LinkedList:
	head = None
	# head of list
	# Linked list Node

	class Node:
		data = 0
		next = None

		def __init__(self, d):
			self.data = d
			self.next = None
	# Inserts a new Node at front of the list.

	@staticmethod
	def push(new_data):
		# 1 & 2: Allocate the Node &
		#			 Put in the data
		new_node = LinkedList.Node(new_data)
		# 3. Make next of new Node as head
		new_node.next = LinkedList.head
		# 4. Move the head to point to new Node
		LinkedList.head = new_node
	# Function to print the linked list

	def printList(self, node):
		while (node != None):
			print(node.data)
			node = node.next
	# Returns true if the loop is removed from the linked
	# list else returns false.

	@staticmethod
	def removeLoop(h):
		s = set()
		prev = None
		while (h != None):
			# If we have already has this node
			# in hashmap it means their is a cycle and we
			# need to remove this cycle so set the next of
			# the previous pointer with null.
			if (h in s):
				prev.next = None
				return True
			else:
				s.add(h)
				prev = h
				h = h.next
		return False
	# Driver program to test above function

	@staticmethod
	def main(args):
		llist = LinkedList()
		llist.push(20)
		llist.push(4)
		llist.push(15)
		llist.push(10)
		# Create loop for testing
		llist.head.next.next.next.next = llist.head
		if (LinkedList.removeLoop(LinkedList.head)):
			print("Linked List after removing loop")
			llist.printList(LinkedList.head)
		else:
			print("No Loop found")


if __name__ == "__main__":
	LinkedList.main([])


