class Node:
	def __init__(self, value = 0):
		
		self.value = value
		self.next = None
def findList(first, second):
	if not first and not second:
		return True
	if not first or not second:
		return False

	ptr1 = first
	ptr2 = second
	while ptr2:

		ptr2 = second

		while ptr1:
			if not ptr2:
				return False

			else if ptr1.value == ptr2.value:
				ptr1 = ptr1.next
				ptr2 = ptr2.next

			else:
				break

		if not ptr1:
			return True
		ptr1 = first
		second = second.next
		
	return False

node_a = Node(1)
node_a.next = Node(2)
node_a.next.next = Node(3)
node_a.next.next.next = Node(4)

node_b = Node(1)
node_b.next = Node(2)
node_b.next.next = Node(1)
node_b.next.next.next = Node(2)
node_b.next.next.next.next = Node(3)
node_b.next.next.next.next.next = Node(4)

if findList(node_a, node_b):
	print("LIST FOUND")
else:
	print("LIST NOT FOUND")

