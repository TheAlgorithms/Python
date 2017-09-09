class Node:#create a Node
    def __int__(self,data):
        self.data=data#given data
        self.next=None#given next to None
class Linked_List:
    pass
    def insert_tail(Head,data):#insert the data at tail
        tamp=Head#create a tamp as a head
        if(tamp==None):#if linkedlist is empty
            newNod=Node()#create newNode Node type and given data and next
            newNod.data=data
            newNod.next=None
            Head=newNod
        else:
            while tamp.next!=None:#find  the last Node
                tamp=tamp.next
            newNod = Node()#create a new node
            newNod.data = data
            newNod.next = None
            tamp.next=newNod#put the newnode into last node
        return Head#return first node  of  linked list  
    def insert_head(Head,data):
        tamp = Head
        if (tamp == None):
            newNod = Node()#create a new Node
            newNod.data = data
            newNod.next = None
            Head = newNod#make new node to Head       
        else:
            newNod = Node()
            newNod.data = data
            newNod.next = Head#put the Head at NewNode Next
            Head=newNod#make a NewNode to Head
        return Head   
    def Print(Head):#print every node data
        tamp=Node()
        tamp=Head
        while tamp!=None:
            print(tamp.data)
            tamp=tamp.next
    def delete_head(Head):#delete from head
        if Head!=None:
            Head=Head.next
        return Head#return new Head
    def delete_tail(Head):#delete from tail
        if Head!=None:
            tamp = Node()
            tamp = Head
            while (tamp.next).next!= None:#find the 2nd last element
                tamp = tamp.next
            tamp.next=None#delete the last element by give next None to 2nd last Element
        return Head
    def isEmpty(Head):
        if(Head==None):#check Head is None  or Not
            return True#return Ture if list is empty
        else:
            return False#check False if it's not empty




