class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Circular_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = self.head

    def insert(self, data):
        temp = self.head
        insertion = Node(data)
        insertion.next = insertion 
        if self.head == None:
            self.head = insertion
        else:
            while temp.next!=self.head:
                temp = temp.next
            temp.next = insertion
            insertion.next = self.head
            self.tail = insertion

    def delete(self,val):
        temp = self.head
        prev = self.head

        if self.head.next == self.head:
            self.head = None
            
        if self.head == None:
            print("List is empty")
            return
             
        while temp.next is not self.head: 
            prev = temp   
            temp  = temp.next

        if self.head.data == val:
            temp.next = self.head.next
            self.head = self.head.next            
        elif temp.data == val:
            prev.next = self.head              
        else:
            prev = temp = self.head 
            while temp.next !=self.head:
                if temp.data == val:
                    prev.next = temp.next
                    break 
                prev = temp 
                temp = temp.next

    def print_list(self):
        temp = self.head
                  
        print(temp.data)
        temp = temp.next
        
        while temp is not self.head:
            print(temp.data)
            temp = temp.next

    def count_nodes(self):
        temp = self.head
        count = 1
        while temp.next is not self.head:
            count = count + 1
            temp = temp.next
        print(count)