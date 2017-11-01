class Node:#create a Node
    def __int__(self,data):
        self.data=data#given data
        self.next=None#given next to None
class Linked_List:
    
    pass
    
    def insert_tail(Head,data):
        if(Head.next is None):
            Head.next = Node(data)
        else:
            insert_tail(Head.next, data)

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
    
    def printList(Head):#print every node data
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
        return Head is None #Return if Head is none
    
    def reverse(Head):
        prev = None
        current = Head
        
        while(current):
            # Store the current node's next node. 
            next_node = current.next
            # Make the current node's next point backwards
            current.next = prev
            # Make the previous node be the current node
            prev = current
            # Make the current node the next node (to progress iteration)
            current = next_node
        # Return prev in order to put the head at the end 
        Head = prev
