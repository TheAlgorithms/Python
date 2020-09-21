'''
    So MinStack is a Stack through which we can get minimum element in Constant time, we will maintain another stack to return Minimum 
    Element in O(1) time 

'''
class MinStack:
    

    def __init__(self):
        ''' Creating stack and min Stack, and size variable to keep track of no of elements in stack'''
        self.stack = []
        self.minStack =[]
        self.size =0

    def push(self, data:int) -> None:
        if self.size == 0: 
            self.minStack.append(data)
        elif data <= self.minStack[-1]:
            self.minStack.append(data)
        self.stack.append(data)
        self.size+=1
    
    def pop(self)-> None:
        ''' Removes the topmost element from the Stack  ''' 
        top =  self.stack.pop()
        self.size-=1
        if top <= self.minStack[-1]:
            self.minStack.pop()
        
    
    def top(self) ->None:
        ''' Returns the top element from the stack '''
        return self.stack[-1]

    def getMin(self):
        ''' Returns the top element from the  Minstack '''
        return self.minStack[-1]

# Code execution starts here
if __name__ == "__main__":
    
   
    # Creating a min Stack
    stack = MinStack()

    stack.push(6)
    print(stack.getMin())  # prints  6

    stack.push(7)
    print(stack.getMin())  # prints 6

    stack.push(8)
    print(stack.getMin())  # prints 6

    stack.push(5)
    print(stack.getMin())  # prints 5

    stack.push(3)
    print(stack.getMin())  # prints 3

    stack.pop()
    print(stack.getMin())  # prints 5

    stack.push(10)
    print(stack.getMin())  # prints 5

    stack.pop()
    print(stack.getMin())  # prints 5

    stack.pop()
    print(stack.getMin())  # prints 6
