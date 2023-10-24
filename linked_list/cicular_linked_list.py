# Python program to delete a given key from linked list 
class node: 
	def __init__(self, data): 
		self.data = data 
		self.next = None

# Function to insert a node at the 
# beginning of a Circular linked list 


def push(head, data): 
	# Create a new node and make head as next of it. 
	newp = node(data) 
	newp.next = head 

	# If linked list is not NULL then 
	# set the next of last node 
	if head != None: 
		# Find the node before head and 
		# update next of it. 
		temp = head 
		while (temp.next != head): 
			temp = temp.next
		temp.next = newp 
	else: 
		newp.next = newp 
	head = newp 
	return head 

# Function to print nodes in a given circular linked list 


def printlist(head): 
	if head == None: 
		print("List is Empty") 
		return
	temp = head.next
	print(head.data, end=' ') 
	if (head != None): 
		while (temp != head): 
			print(temp.data, end=" ") 
			temp = temp.next
	print() 

# Function to delete a given node 
# from the list 


def deletenode(head, key): 
	# If linked list is empty 
	if (head == None): 
		return

	# If the list contains only a 
	# single node 
	if (head.data == key and head.next == head): 
		head = None
		return

	last = head 

	# If head is to be deleted 
	if (head.data == key): 
		# Find the last node of the list 
		while (last.next != head): 
			last = last.next

		# Point last node to the next of 
		# head i.e. the second node 
		# of the list 
		last.next = head.next
		head = last.next
		return

	# Either the node to be deleted is 
	# not found or the end of list 
	# is not reached 
	while (last.next != head and last.next.data != key): 
		last = last.next

	# If node to be deleted was found 
	if (last.next.data == key): 
		d = last.next
		last.next = d.next
		d = None
	else: 
		print("Given node is not found in the list!!!") 


# Driver code 
# Initialize lists as empty 
head = None

# Created linked list will be 
# 2->5->7->8->10 
head = push(head, 2) 
head = push(head, 5) 
head = push(head, 7) 
head = push(head, 8) 
head = push(head, 10) 

print("List Before Deletion: ") 
printlist(head) 

deletenode(head, 7) 
print("List After Deletion: ") 
printlist(head) 
