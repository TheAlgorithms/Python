class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node    
            return
        self.tail.next = new_node
        self.tail = new_node

# it merges two sorted linked list
def sortedMerge(head_A, head_B):
    temp = Node(1)
    pointer = temp
    while head_A !=None and head_B !=None:
        if head_A.data < head_B.data:
            pointer.next = head_A
            head_A = head_A.next
        else:
            pointer.next = head_B
            head_B = head_B.next
        pointer = pointer.next   
    
    if head_A ==None:
        pointer.next = head_B
    else:
        pointer.next = head_A
    return temp.next
              
# prints the elements of linked list
def printList(n):
    while n is not None:
        print(n.data, end=' ')
        n = n.next
    print()

# main function
if __name__ == '__main__':
    a = LinkedList() 
    b = LinkedList()
        
    nodes_a = [2 , 3 , 5 , 10]
    nodes_b = [1, 5, 8]
        
    for x in nodes_a:
        a.append(x)
        
    for x in nodes_b:
        b.append(x)
        
    printList(sortedMerge(a.head,b.head))
    