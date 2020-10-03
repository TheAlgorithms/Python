"""
The head ( starting node) of a Linked List will be provided, we have to return the middle node of the linked list.
There are mainly 2 types of approaches : 

1) Sequenctially calculate the number of nodes the linked list. Find the index of the middle node using the formula (mid=N/2+1) and 
then travel upto that index and return the middle

2) Using two pointers

Here we are gonna show the implementation of the second approach.
"""

# Node class  
class Node:  
  
    # Function to initialise the node object  
    def __init__(self, data):  
        self.data = data  
        self.next = None 
  
class LinkedList: 
  
    def __init__(self): 
        self.head = None
  
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
  
    # Function to get the middle of  
    # the linked list 
    def printMiddle(self): 
        slow_ptr = self.head 
        fast_ptr = self.head 
        """
            fast pointer moves at twice the speed than the slow pointer, hence when the fast pointer reaches
            the end of the linked list, the slow pointer reaches the middle of the linked list
        """
        if self.head is not None: 
            while (fast_ptr is not None and fast_ptr.next is not None): 
                fast_ptr = fast_ptr.next.next
                slow_ptr = slow_ptr.next
            print("The middle element is: ", slow_ptr.data) 
  
if __name__ == "__main__":

    list1 = LinkedList() 
    list1.push(7)
    list1.push(6)
    list1.push(5) 
    list1.push(4) 
    list1.push(2) 
    list1.push(3) 
    list1.push(1) 
    list1.printMiddle() 