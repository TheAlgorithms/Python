# expected input =  1 3 0 0 1 2  4
# expected 0utpt =  -1 -1 3 3 3 3 -1

#implementaion of stack
class Stack():
    def __init__(self):
        self.items = []
    def push (self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return len(self.items) == 0
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def get_stack(self):
        return self.items
      
 #finding greatest to left using stack.     
def GreatestToLeft(arr):
    #creating a stack
    stack = Stack()
    ans = []
    
    for i in arr:
        if stack.is_empty():
            ans.append(-1)
            
        elif not stack.is_empty() and stack.peek()>i:
            ans.append(stack.peek())
            
        elif not stack.is_empty() and stack.peek()<=i:
            
            while  not stack.is_empty() and stack.peek()<=i:
                stack.pop()
                
            if stack.is_empty():
                ans.append(-1)
            
            else:
                ans.append(stack.peek())
                
        stack.push(i)
    return ans

if __name__ == '__main__':
    
    arr = [1, 3, 0, 0, 1, 2, 4]
    print(GreatestToLeft(arr))

