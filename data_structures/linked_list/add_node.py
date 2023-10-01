class node: #define a class named node having data and ref as attributes
    def __init__(self,data):
        self.data=data
        self.ref= None
class LinkedList:
    def __init__(self): #define head of the linked list i.e initiate the linked list
        self.head=None
    def print_LL(self): # to print the linked list
        if self.head is None:
            print("The Linked List is empty ")
        else:
            n= self.head
            while n is not None:
                print(n.data)
                n=n.ref
    def add_begin(self,data): #to add a node in the beginning
        new_node= node(data) #define data of the new node
        new_node.ref= self.head #make the ref or adress of node to the head node
        self.head = new_node
    def add_end(self,data):
        new_node= node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node
    def add_after(self,data,x):
        n=self.head
        while n is not None:
            if x==n.data:
                break
            n=n.ref
        new_node=node(data)
        new_node.ref= n.ref
        n.ref= new_node
linked_list= LinkedList() # main driver function here we define the linked list
linked_list.add_begin(11) #added 11 to the beginning of out linked list
linked_list.add_end(100)
linked_list.add_begin(22)
linked_list.add_after(30,11)
linked_list.print_LL()
#https://youtu.be/xRTdfZsAz6Y?si=EMrqVJpXjDDz1kEF
