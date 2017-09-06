class Node:   #create a Node
    def __int__(self,data):
        self.data=data  #given data
        self.next=None  #given next to None




class Linked_List:
    pass
    def insert_tail(Head,data): #insert the data at tail
        tamp=Head
        if(tamp==None):
            newNod=Node() #create newNode Node type and given data and next
            newNod.data=data
            newNod.next=None
            Head=newNod

        else:
            while tamp.next!=None: #reaches the last Node
                tamp=tamp.next
            newNod = Node()  #create a new node
            newNod.data = data
            newNod.next = None
            tamp.next=newNod  #put the newnode into last node

        return Head
    def insert_head(Head,data):
        tamp = Head
        if (tamp == None):
            newNod = Node()  #create a new Node
            newNod.data = data
            newNod.next = None
            Head = newNod   #make new node to Head
            # print(Head.data)
            return Head
        else:
            newNod = Node()
            newNod.data = data
            newNod.next = Head  #put the Head at NewNode Next
            Head=newNod        # make a NewNode to Head
            # print(tamp.data)
            return Head



    def Print(Head):   #print every node data
        tamp=Node()
        tamp=Head
        while tamp!=None:
            print(tamp.data)
            tamp=tamp.next



    def delete_head(Head):   #delete from head
        if Head==None:
            print("List is empty cannot delete")

        else:
            Head=Head.next

        return Head   #return new Head



    def delete_tail(Head):  #delete from tail
        if Head==None:
            print("List is empty cannot delete")
        else:
            tamp = Node()
            tamp = Head
            while (tamp.next).next!= None:  #reach tha 2nd last element
                tamp = tamp.next
            tamp.next=None  #delet the last element by give next None to 2nd last Element



    def isEmpty(Head):
        if(Head==None):  #check Head is None  or Not
            print("list is empty")
            return True   #return Ture if it is none
        else:
            print("Not empty")
            return False    #check False if it's not none



##check

Head=None
Head=Linked_List.insert_tail(Head,5)
Head=Linked_List.insert_tail(Head,6)
Head=Linked_List.insert_head(Head,7)
Head=Linked_List.insert_head(Head,9)

Linked_List.Print(Head)

print("delete_tail")
Linked_List.delete_tail(Head)
Linked_List.Print(Head)


print("delete_head")
Head=Linked_List.delete_head(Head)
Linked_List.Print(Head)

Linked_List.isEmpty(Head)


