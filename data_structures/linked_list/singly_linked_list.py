from __future__ import print_function


class Node:  # create a Node
    def __init__(self, data):
        self.data = data  # given data
        self.next = None  # given next to None


class Linked_List:
    def __init__(self):
        self.Head = None    # Initialize Head to None
        
    def insert_tail(self, data):
        if(self.Head is None): self.insert_head(data)    #If this is first node, call insert_head
        else:
            temp = self.Head
            while(temp.next != None):    #traverse to last node
                temp = temp.next
            temp.next = Node(data)    #create node & link to tail

    def insert_head(self, data):
        newNod = Node(data)    # create a new node
        if self.Head != None:
            newNod.next = self.Head     # link newNode to head
        self.Head = newNod    # make NewNode as Head

    def printList(self):  # print every node data
        tamp = self.Head
        while tamp is not None:
            print(tamp.data)
            tamp = tamp.next

    def delete_head(self):  # delete from head
        temp = self.Head
        if self.Head != None:
            self.Head = self.Head.next
            temp.next = None
        return temp
        
    def delete_tail(self):  # delete from tail
        tamp = self.Head
        if self.Head != None:
            if(self.Head.next is None):    # if Head is the only Node in the Linked List
                self.Head = None
            else:
                while tamp.next.next is not None:  # find the 2nd last element
                    tamp = tamp.next
                tamp.next, tamp = None, tamp.next    #(2nd last element).next = None and tamp = last element 
        return tamp

    def isEmpty(self):
        return self.Head is None  # Return if Head is none

    def reverse(self):
        prev = None
        current = self.Head

        while current:
            # Store the current node's next node.
            next_node = current.next
            # Make the current node's next point backwards
            current.next = prev
            # Make the previous node be the current node
            prev = current
            # Make the current node the next node (to progress iteration)
            current = next_node
        # Return prev in order to put the head at the end
        self.Head = prev

def main():
    A = Linked_List()
    print("Inserting 1st at Head")
    a1=input()
    A.insert_head(a1)
    print("Inserting 2nd at Head")
    a2=input()
    A.insert_head(a2)
    print("\nPrint List : ")
    A.printList()
    print("\nInserting 1st at Tail")
    a3=input()    
    A.insert_tail(a3)
    print("Inserting 2nd at Tail")
    a4=input()
    A.insert_tail(a4)
    print("\nPrint List : ")
    A.printList()
    print("\nDelete Head")
    A.delete_head()
    print("Delete Tail")
    A.delete_tail()
    print("\nPrint List : ")
    A.printList()
    print("\nReverse Linked List")
    A.reverse()
    print("\nPrint List : ")
    A.printList()
    
if __name__ == '__main__':
	main()
