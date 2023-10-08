from collections import deque
from typing import Generic, TypeVar

T = TypeVar("T")
""" Implementing stack using two arrays"""

class Stack(Generic[T]):#Stack class to implement stack operations
     
     
          
    
    
    def __init__(self) :
        self.insert_queue=deque() # First Queue to be used for inserting
        self.second_queue=deque() # Second Queue to be used
        
        
    def push(self,item:int)  :
        self.insert_queue.append(item)
        while(self.second_queue):
            self.insert_queue.append(self.second_queue.popleft()) # Popping the elements 
    
        self.insert_queue,self.second_queue=self.second_queue,self.insert_queue
        
        
    def pop(self)   ->int :
        if not self.second_queue: # if the stack  is empty
            return None
        return(self.second_queue.popleft())  # if not empty pop
    
    
    def top(self) -> int:
        if not self.second_queue:
            return None
        return(self.second_queue[0])
    
    
    def __str__(self) -> str:
        return tuple(self.second_queue)
    
    def __len__(self) -> int:
        return len(self.second_queue)
            
        

def test_stack() -> None:
   stack = Stack() # Creating a empty stack
   choice=int(input("1 to push,2 to pop,3 to peek ,4 to print, 5 for size,6 to exit:"))
   while (choice in (1, 2, 3, 4, 5, 6)):
       match(choice):
           case 1:
               element=int(input("Enter the element to push:"))
               stack.push(element)
           case 2:
               print(stack.pop())
           case 3:
               print(stack.top())
           case 4:
               print(stack.__str__())
           case 5:
               leng=stack.__len__()
               print(f"The size of the stack is {leng}")
           case 6:
               print("Exiting")
               break
           case _:
               print("Enter properly")
               
       choice=int(input("1 to push,2 to pop,3 to peek ,4 to print, 5 for size,6 to exit:"))
   
                
if __name__=="__main__":
    test_stack() # calling the test function 
 
    
        
           
 
