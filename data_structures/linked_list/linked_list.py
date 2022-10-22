#A class to create new nodes for the linked list
class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

#A class to perform and manipulate various operations in the linked list
class LinkedList:
    def __init__(self):
        self.head=None

    #A function to insert a node at the beginning of a linked list
    def insertbeg(self,data):
        node=Node(data,self.head)
        self.head=node

    #A function to find the length of a linked list
    def getlength(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        print(count)

    #A function to insert a node at the end of a linked list
    def insertend(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)
        
    #A function to insert a list of elements in a linked list    
    def inslist(self,datalist):
        self.head = None
        for i in datalist:
            self.insertbeg(i)

    #A function to display the linked list
    def display(self):
        if self.head is None:
            print("linked list is empty")
            return
        itr=self.head
        llstr=""
        while itr:
            llstr+=str(itr.data)+"-->"
            itr=itr.next
        print(llstr)
        
    #A function to remove a node of the given position in a linked list
    def remove(self,index):
        if index<0 and index>self.getlength():
            raise Exception("Invalid")
        if index==0:
            self.head=self.head.next
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1 :
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1



if __name__ == '__main__':
    ll = LinkedList()
    ll.insertbeg(22)
    ll.insertbeg(77)
    ll.insertend(33)
    ll.inslist([10,20,30,40,50])
    ll.getlength()
    ll.remove(2)
    ll.display()
