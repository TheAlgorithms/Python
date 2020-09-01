"""
- A linked list is similar to an array, it holds values. However, links in a linked
    list do not have indexes.
- This is an example of a double ended, doubly linked list.
- Each link references the next link and the previous one.
- A Doubly Linked List (DLL) contains an extra pointer, typically called previous
    pointer, together with next pointer and data which are there in singly linked list.
 - Advantages over SLL - It can be traversed in both forward and backward direction.
     Delete operation is more efficient"""

class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

    def __str__(self):
        return f"{self.data}"
    

class LinkedList:
  
    def __init__(self):
        self.head = None  # First node in list
        self.tail = None  # Last node in list
        
    def __str__(self):
        current = self.head
        nodes = []
        while current is not None:
            nodes.append(current)
            current = current.next
        return " ".join(str(node) for node in nodes)

    def insert_at_head(self, data):
        new_node = Node(data)
        if self.is_empty:
            self.tail = new_node
            self.head = new_node
        else:
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node
        
  
    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.is_empty:
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
            
    #Prints the elements of the given Linked List in reverse order

    def reverse(self):
        temp_node = None
        cur_node = self.head
        while cur_node:
            temp_node = cur_node.prev
            cur_node.prev = cur_node.next
            cur_node.next = temp_node
            cur_node = cur_node.prev
        if temp_node:
            self.head = temp_node.prev
    #after this  we call print_list to print the reversed list
        
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    @property
    def is_empty(self):  # return True if the list is empty
        return self.head is None
