'''
- A linked list is similar to an array, it holds values. However, links in a linked list do not have indexes.
- This is an example of a double ended, doubly linked list.
- Each link references the next link and the previous one.
'''
from __future__ import print_function


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insertHead(self, x):
        newLink = Link(x) #Create a new link with a value attached to it
        if(self.isEmpty() == True): #Set the first element added to be the tail
            self.tail = newLink
        else:
            self.head.previous = newLink # newLink <-- currenthead(head)
        newLink.next = self.head # newLink <--> currenthead(head)
        self.head = newLink # newLink(head) <--> oldhead
    
    def deleteHead(self):
        temp = self.head
        self.head = self.head.next # oldHead <--> 2ndElement(head) 
        self.head.previous = None # oldHead --> 2ndElement(head) nothing pointing at it so the old head will be removed
        if(self.head is None):
            self.tail = None
        return temp
    
    def insertTail(self, x):
        newLink = Link(x)
        newLink.next = None # currentTail(tail)    newLink -->
        self.tail.next = newLink # currentTail(tail) --> newLink -->
        newLink.previous = self.tail #currentTail(tail) <--> newLink -->
        self.tail = newLink # oldTail <--> newLink(tail) -->
    
    def deleteTail(self):
        temp = self.tail
        self.tail = self.tail.previous # 2ndLast(tail) <--> oldTail --> None
        self.tail.next = None # 2ndlast(tail) --> None
        return temp
    
    def delete(self, x):
        current = self.head
        
        while(current.value != x): # Find the position to delete
            current = current.next
            
        if(current == self.head):
            self.deleteHead()
            
        elif(current == self.tail):
            self.deleteTail()
            
        else: #Before: 1 <--> 2(current) <--> 3
            current.previous.next = current.next # 1 --> 3
            current.next.previous = current.previous # 1 <--> 3
    
    def isEmpty(self): #Will return True if the list is empty
        return(self.head is None)
        
    def display(self): #Prints contents of the list
        current = self.head
        while(current != None):
            current.displayLink()
            current = current.next  
        print()

class Link:
    next = None #This points to the link in front of the new link
    previous = None #This points to the link behind the new link
    def __init__(self, x):
        self.value = x
    def displayLink(self):
        print("{}".format(self.value), end=" ")
