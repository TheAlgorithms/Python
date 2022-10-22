class Node:
  # constructor
  def __init__(self, data = None, next=None): 
    self.data = data
    self.next = next

# A Linked List class with a single head node
class LinkedList:
  def __init__(self):  
    self.head = None
  
  # insertion method for the linked list
  def insert(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode
  
  # print method for the linked list
  def printLL(self):
    current = self.head
    while(current):
      print(current.data)
      current = current.next
#-----------------------Merge function---------------------#
def merge(List_1, List_2):
    # Node for output LinkedList   
    head_ptr = temp_ptr = Node() # head_ptr will be the head node of the output list 
    # temp_ptr will be used to insert nodes in the output list
    
    # Loop for merging two lists
    # Loop terminates when both lists reaches to its end
    while List_1 or List_2:
        # List_1 has not reached its end
        # and List_2 has either reached its end or its current node has data
        # greater than or equal to the data of List_1 node
        # than insert List_1 node in the ouput list
        if List_1 and (not List_2 or List_1.data <= List_2.data):
            temp_ptr.next = Node(List_1.data)
            List_1 = List_1.next
        # otherwise insert List_2 node in the ouput list
        else:
            temp_ptr.next = Node(List_2.data)
            List_2 = List_2.next
        # move temp_pointer to next position
        temp_ptr = temp_ptr.next
    # return output list
    return head_ptr.next
#----------------------------------------------------------#
# Test merge() function
# Linked List with even numbers
LL1 = LinkedList()
LL1.insert(2)
LL1.insert(4)
LL1.insert(6)
LL1.insert(8)
# Linked List with odd numbers
LL2 = LinkedList()
LL2.insert(1)
LL2.insert(3)
LL2.insert(5)
LL2.insert(7)
# Merge Function
LL3 = LinkedList()
LL3.head=merge(LL1.head, LL2.head)
LL3.printLL()
