# Python program to delete a node in a linked list 
# at a given position 
  
# Node class  
class Node: 
  
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
class LinkedList: 
  
    # Constructor to initialize head 
    def __init__(self): 
        self.head = None
  
    # Function to insert a new node at the beginning 
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
  
    # Given a reference to the head of a list  
    # and a position, delete the node at a given position 
    def deleteNode(self, position): 
  
        # If linked list is empty 
        if self.head == None: 
            return 
  
        # Store head node 
        temp = self.head 
  
        # If head needs to be removed 
        if position == 0: 
            self.head = temp.next
            temp = None
            return 
  
        # Find previous node of the node to be deleted 
        for i in range(position -1 ): 
            temp = temp.next
            if temp is None: 
                break
  
        # If position is more than number of nodes 
        if temp is None: 
            return 
        if temp.next is None: 
            return 
  
        # Node temp.next is the node to be deleted 
        # store pointer to the next of node to be deleted 
        next = temp.next.next
  
        # Unlink the node from linked list 
        temp.next = None
  
        temp.next = next 
  
  
    # Utility function to print the linked LinkedList 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print " %d " %(temp.data), 
            temp = temp.next
  
  
# Driver program to test above function 
llist = LinkedList() 
llist.push(7) 
llist.push(1) 
llist.push(3) 
llist.push(2) 
llist.push(8) 
  
print "Created Linked List: "
llist.printList() 
llist.deleteNode(4) 
print "\nLinked List after Deletion at position 4: "
llist.printList() 
