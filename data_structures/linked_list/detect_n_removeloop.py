# Python program to detect and remove loop in linked list 
  
# Node class  
class Node: 
  
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
  
    def detectAndRemoveLoop(self): 
        slow_p = fast_p = self.head 
          
        while(slow_p and fast_p and fast_p.next): 
            slow_p = slow_p.next
            fast_p = fast_p.next.next
  
            # If slow_p and fast_p meet at some point then 
            # there is a loop 
            if slow_p == fast_p: 
                self.removeLoop(slow_p) 
          
                # Return 1 to indicate that loop is found 
                return 1
          
        # Return 0 to indicate that there is no loop 
        return 0 
  
    # Function to remove loop 
    # loop_node --> pointer to one of the loop nodes 
    # head --> Pointer to the start node of the linked list 
    def removeLoop(self, loop_node): 
        ptr1 = loop_node 
        ptr2 = loop_node 
          
        # Count the number of nodes in loop 
        k = 1 
        while(ptr1.next != ptr2): 
            ptr1 = ptr1.next
            k += 1
  
        # Fix one pointer to head 
        ptr1 = self.head 
          
        # And the other pointer to k nodes after head 
        ptr2 = self.head 
        for i in range(k): 
            ptr2 = ptr2.next
  
        # Move both pointers at the same place 
        # they will meet at loop starting node 
        while(ptr2 != ptr1): 
            ptr1 = ptr1.next
            ptr2 = ptr2.next
  
        # Get pointer to the last node 
        while(ptr2.next != ptr1): 
            ptr2 = ptr2.next
  
        # Set the next node of the loop ending node 
        # to fix the loop 
        ptr2.next = None
  
    # Function to insert a new node at the beginning 
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
  
    # Utility function to print the linked LinkedList 
    def printList(self): 
        temp = self.head 
        while(temp): 
            print(temp.data) 
            temp = temp.next
  
  
# Driver program 
llist = LinkedList() 
llist.push(10) 
llist.push(4) 
llist.push(15) 
llist.push(20) 
llist.push(50) 
  
# Create a loop for testing 
llist.head.next.next.next.next.next = llist.head.next.next
  
llist.detectAndRemoveLoop() 
  
print("Linked List after removing loop")
llist.printList() 
