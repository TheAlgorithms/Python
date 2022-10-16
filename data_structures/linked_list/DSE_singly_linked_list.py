#Creation of linked list

class Node:
    def __init__(self,data) -> None:
        self.data=data
        # self.ref=None
        self.next=None

class create:
    def __init__(self) -> None:
        self.head=None
    def create(self):
        self.head=None
        while (True):
            n_node=Node(data)
            self.data=int(input("enter value to insert:-"))
            if self.head==None:
                self.head=n_node
            else:
                temp.next=n_node


#--------------------------------LINKED LIST traverting---------------------------

class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.ref=None  #add. of data ref --> next

class Linkedlist:
    def __init__(self) -> None:
        self.head=None

# this is how we are traverting the linked list

    def printall(self):
        if self.head is None:
            print("The given linked list is empty.")
        else:
            n=self.head
            while(n is not None):
                print(n.data)
                n=n.ref


#     def insertbeg(self,data):
#         new_node=Node(data)
#         new_node.ref=self.head
#         self.head=new_node
# o=Linkedlist()
# o.insertbeg(10)
# o.insertbeg(100)
# o.insertbeg(1000)
# o.insertbeg(100000)
# o.printall()

--------------------------------3_beg_insering.py----------------------------------

class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.ref=None

class Linkedlist:
    def __init__(self) -> None:
        self.head=None

    #this to traverse the linked list -->
    def printall(self):
        if self.head is None:
            print("The given linked list is empty.")
        else:
            n=self.head
            while(n is not None):
                print(n.data)
                n=n.ref

    #this is function to insert node at the begging of linked list -->
    def insertbeg(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node



o=Linkedlist()
o.insertbeg(10)
o.insertbeg(100)
o.insertbeg(1000)
o.insertbeg(100000)
o.printall()



-----------------------------------------------4_endlinkedlist.py----------------------------


class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self) -> None:
        self.head=None

    #this to traverse the linked list -->
    def printall(self):
        if self.head==None:
            print("Linked list is empty.")
        else:
            n=self.head
            while (n is not None):
                print(n.data)
                n=n.next

    # # this is function to insert node at the begging of linked list -->
    # def insertbeg(self,data):
    #     new_node=Node(data)
    #     new_node.ref=self.head
    #     self.head=new_node




    #this is function to insert node at the end of linked list -->
    def insertend(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            temp=self.head
            while (temp.next!=None):
                temp=temp.next
            temp.next=new_node

o=Linkedlist()
o.insertend(20)
# o.insertbeg(10)
o.insertend(20202)
o.insertend(900)

o.printall()



---------------------------------Insertion befor and after value ------------------------


from typing import NewType


class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self) -> None:
        self.head=None

    def printall(self):
        if self.head is None:
            print("The given linked list is empty.")
        else:
            n=self.head
            while(n is not None):
                print(n.data)
                n=n.next


    #-->function to insert the node at the end of linked list -->
    def insertend(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            temp=self.head
            while (temp.next!=None):
                temp=temp.next
            temp.next=new_node

    #-->program to insert the node befor the give value of node-->
    # def insert_befor_value(self,data,value):
    #     new_node=Node(data)
    #     if self.head==None:
    #         print("The linked list is empty.")
    #     else:
    #         temp=self.head
    #         while (temp!=None):
    #             if temp.next.data==value:
    #                 break
    #             temp=temp.next
    #         new_node.next=temp.next
    #         temp.next=new_node

    #this is function to insert node at the begging of linked list -->
    # def insertBeg(self,data):
    #     new_node=Node(data)
    #     new_node.next=self.head
    #     self.head=new_node

    #--->>this is function to insert the node value after the given node value
    def afterValue(self,data,value):
        # self.data=None
        if self.head==None:
            print("The givaen linked list is Empty.")
        else:
            t=self.head
            while(t!=None):
                if t.data==value:
                    break
                t=t.next
            if t is None:
                print(f"The node value {value} is not found.")
            else:
                new_node=Node(data)
                new_node.next=t.next
                t.next=new_node







o=Linkedlist()
# o.insertBeg(900)
o.insertend(2)
o.insertend(20)
# o.insert_befor_value(25,20202)
o.afterValue(90,2)
o.afterValue(900000,90)
o.afterValue(900000,20)
o.afterValue(900000,1)
o.printall()

      ==============================================Node Deletion=============================================

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self) -> None:
        self.head = None

    # this to traverse the linked list -->
    def printall(self):
        if self.head == None:
            print("Linked list is empty.")
        else:
            n = self.head
            while (n is not None):
                print(n.data)
                n = n.next

    # # this is function to insert node at the begging of linked list -->
    # def insertbeg(self,data):
    #     new_node=Node(data)
    #     new_node.ref=self.head
    #     self.head=new_node

    # this is function to insert node at the end of linked list -->
    def insertend(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while (temp.next != None):
                temp = temp.next
            temp.next = new_node

    # <--this is function to delet the node at the beg. of linked list--->
    def delBeg(self):
        if self.head == None:
            print("The linked list is empty.")
        else:
            self.head = self.head.next

    # <--this is function to deletee the node at END of linked list-->
    def delEnd(self):
        # self.head=head
        if self.head == None:
            print("The linked list is empty.")
        if self.head.next == None:
            self.head = None
            # return None
        else:
            tm = self.head
            while(tm.next.next == None):
                # break
                tm = tm.next
                # break
            tm.next = None

    def removeLastNode(self):
	    if self.head == None:
	    	return None
	    if self.head.next == None:
	    	self.head = None
	    	return None
	    second_last = self.head
	    while(second_last.next.next):
	    	second_last = second_last.next
	    second_last.next = None
	    return self.head

    def del_byValue(self, value):
        tmpp = self.head
        if (tmpp != None):
            if tmpp.data == value:
                tmpp = tmpp.next
                tmpp = None
                return
        tmpp = self.head
        while(tmpp != None):
            # print(tmpp.data)
            if tmpp.data == value:
                # print("Found.........")
                break
            p=tmpp
            tmpp = tmpp.next
        if tmpp == None:
            return
            # print(f"The value node {value} is not found")
        # else:
        p.next= tmpp.next
        tmpp=None


    def printall(self):
        if self.head == None:
            print("Linked list is empty.")
        else:
            n = self.head
            while (n is not None):
                print(n.data)
                n = n.next




o = Linkedlist()
o.insertend(20)
o.insertend(20202)
o.insertend(5050)
o.insertend(900)
o.printall()

# o.delBeg()
# o.removeLastNode()
# o.del_byValue(20)
# o.deleteNode(5050)
o.delEnd()
print("linked list after deleting Node---")
o.printall()










===============================================Linked list Reversal ======================================



# from typing import NewType


class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self) -> None:
        self.head=None

    def insertend(self,data):
        new_node=Node(data)
        if self.head==None:
            self.head=new_node
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=new_node

    def reverseLinkedlist(self):
        previous = None
        current=self.head
        while(current!=None):
            n_=current.next
            current.next=previous
            previous=current
            current=n_
        self.head=previous


    def print_all(self):
        temp=self.head
        while(temp!=None):
            print(temp.data)
            temp=temp.next

o=Linkedlist()
o.insertend(90)
o.insertend(30)
o.insertend(10)
o.insertend(20)
print("The normal linkedlist:-000")
o.print_all()
print("The reverse linked list:-")
o.reverseLinkedlist()
o.print_all()
