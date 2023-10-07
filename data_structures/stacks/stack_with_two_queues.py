from collections import deque
from typing import Generic, TypeVar

T = TypeVar("T")
""" Implementing stack using two arrays"""

class Stack(Generic[T]):#Stack class to implement stack operations
     
     
          
    
    
    def __init__(self) -> None:
        self.insert_queue=deque()#First Queue to be used for inserting
        self.suffle_queue=deque()#Second Queue to be used for suffling
        
        
    def push(self,item:int)  -> None:
        self.insert_queue.append(item)#Add items into the Queue
        while(self.suffle_queue):
            self.insert_queue.append(self.suffle_queue.popleft())#Popping the elements 
    
        self.insert_queue,self.suffle_queue=self.suffle_queue,self.insert_queue
        
        
    def pop(self)   ->int :
        if(not(self.suffle_queue)):#if the stack  is empty
            return None
        return(self.suffle_queue.popleft())#if not empty pop
    
    
    def top(self) -> int:
        if(not(self.suffle_queue)):
            return None
        return(self.suffle_queue[0])
    
    
    def printing(self) ->None:
        print(self.suffle_queue)
        
        
    def size(self) ->int:
        return(len(self.suffle_queue))
            
        

def test_stack() -> None:
   s = Stack()#Creating a stack in S
   n=int(input("1 to push,2 to pop,3 to peek ,4 to print, 5 for size,6 to exit:"))
   while (n in (1, 2, 3, 4, 5, 6)):
       match(n):
           case 1:
               element=int(input("Enter the element to push:"))
               s.push(element)
           case 2:
               print(s.pop())
           case 3:
               print(s.top())
           case 4:
               s.printing()
           case 5:
               leng=s.size()
               print(f"The size of the stack is {leng}")
           case 6:
               print("Exiting")
               break
           case _:
               print("Enter properly")
               
       n=int(input("1 to push,2 to pop,3 to peek ,4 to print, 5 for size,6 to exit:"))
   
                
if __name__=="__main__":
    test_stack()#calling the test funtion 
 
    
        
           
 
