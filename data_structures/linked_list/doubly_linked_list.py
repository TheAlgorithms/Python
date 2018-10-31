'''
- A linked list is similar to an array, it holds values. However, links in a linked list do not have indexes.
- This is an example of a double ended, doubly linked list.
- Each link references the next link and the previous one.
- A Doubly Linked List (DLL) contains an extra pointer, typically called previous pointer, together with next pointer and data which are there in singly linked list.
 - Advantages over SLL - IT can be traversed in both forward and backward direction.,Delete operation is more efficent'''
from __future__ import print_function


class LinkedList:           #making main class named linked list
    def __init__(self):
        self.len = 0 # count the number of links (Nodes)
        self.head = Link(None) #Head Sentinel Node
        self.tail = Link(None) #Tail Sentinel Node
        self.head.next = self.tail
        self.tail.previous = self.head #Linking Head & Tail Sentinel Node with each other
        
    def insertHead(self, x):
        newLink = Link(x)                            # Create a new link with a value attached to it
        self.head.next.previous = newLink            # newLink <-- currenthead(head)
        newLink.next = self.head.next                # newLink <--> currenthead(head)
        self.head.next = newLink                     # HeadSentinel --> newLink
        newLink.previous = self.head                 # HeadSentinel <--- newLink
        self.len+=1
    
    def deleteHead(self):
        if(self.isEmpty()): return None
        temp = self.head.next                        # temp = currentHead
        self.head.next = self.head.next.next         # HeadSentinel --> 2ndElement 
        self.head.next.previous = self.head          # HeadSentinel <-- 2ndElement
        self.len-=1
        return temp
    
    def insertTail(self, x):
        newLink = Link(x)
        self.tail.previous.next = newLink          # CurrentTail --> newLink
        newLink.previous = self.tail.previous      # CurrentTail <-- newLink
        self.tail.previous = newLink               # newLink <-- TailSentinel
        newLink.next = self.tail                   # newLink --> TailSentinel
        self.len+=1
    
    def deleteTail(self):
        if(self.isEmpty()): return None
        temp = self.tail.previous
        temp.previous.next = self.tail              # 2ndLast(tail) --> TailSentinel
        self.tail.previous = temp.previous          # 2ndLast(tail) <-- TailSentinel
        self.len-=1
        return temp
    
    def delete(self, x):
        current = self.head.next
        
        while(current.value != x and current!=self.tail):                  # Find the position to delete
            current = current.next
            
        if(current == self.tail):
            return None
            
        else: #Before: 1 <--> 2(current) <--> 3
            current.previous.next = current.next # 1 --> 3
            current.next.previous = current.previous # 1 <--> 3
            self.len-=1
            return current
    
    def isEmpty(self):                               #Will return True if the list is empty
        return(self.len == 0)
        
    def display(self):                                #Prints contents of the list
        current = self.head.next
        while(current != self.tail):
            current.displayLink()
            current = current.next  
        print()

class Link:
    next = None                                       #This points to the link in front of the new link
    previous = None                                   #This points to the link behind the new link
    def __init__(self, x):
        self.value = x
    def displayLink(self):
        print("{}".format(self.value), end=" ")
