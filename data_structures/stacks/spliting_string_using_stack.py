vowels = ['a','e','i','o','u','A','E','I','O','U'] # Global array of vowels to save memory in case of multiple calls of the split function.

class Node:

    '''
    This class implements a single linked list with functions:

    - set_data: To take the data and put it to the node.
    - get_data: To fetch and return data stored in the node.
    - set_next: To point the next pointer to the next node.
    - get_next: To get the pointer to the next node.
    - has_next: Returns a boolen if the next node exists or not

    '''



    def __init__(self):
        self.data = None
        self.next = None
    
    # method for setting the data field of the node  
    def set_data(self, data):
        self.data = data
    
    # method for getting the data field of the node  
    def get_data(self):
        return self.data
    
    # method for setting the next field of the node
    def set_next(self, next):
        self.next = next
    
    # method for getting the next field of the node
    def get_next(self):
        return self.next
        
    # returns true if the node points to another node
    def has_next(self):
        return self.next != None
    



#Class for stack implementation
class Stack(object):
    '''
    Class that is used to implement stack using Linked lists.

    Functions used are pop(Stack), push(Stack, data), peek(stack), delete_stack(Stack)

    push(Stack, data):
        Takes a data and pushes it in to the stack.
    
    pop(Stack):
        returns the top element inserted in the stack and deletes it from stack.
    
    peek(Stack):
        returns the top element of the stack.
    
    delete_stack(Stack):
        Deallocates the memory of the stack.
    
    display_stack(Stack):
        displays the stack
    '''

    def __init__(self, data = None):
        self.head = None
        if data:
            for Data in data:
                self.push(data)
        
    def push(self,data):
        temp = Node()
        temp.set_data(data)
        temp.set_next(self.head)
        self.head = temp

    def pop(self):
        if self.head == None:
            raise IndexError
        temp = self.head.get_data()
        self.head = self.head.get_next()
        return temp

    def peek(self):
        if self.head == None:
            raise IndexError

        return self.head.get_data()

    def display_stack(self):
        if self.head == None:
            raise IndexError
        temp = self.head
        print("The data in the stack is: ",end = '')
        while(temp != None):
            print(temp.get_data(),end = '   ')
            temp = temp.get_next()
        print()


def split(str):
    '''
    -Initialze a stack.
    -Ittereate through the sring alphabet by alphabet.
    -When you see a Vowel push a None refrence in the data.
    -You have the string splitted in the stack.
    -Push the stack in another stack to reverse the string.
    -Now you have the string the right way.
    '''

    stack = Stack(None)

    for i in str:
        if(i not in vowels):
            stack.push(i)
        else:
            stack.push(-1)

    stack2 = Stack()

    for i in range(len(str)-1):
        stack2.push(stack.pop())

    for i in range(len(str)-1):
        x = stack2.pop()
        if(x != -1):
            print(x,end = '')
        else:
            print(" ",end = '')


if __name__ == "__main__":
    str = input("Please insert a string: ",)
    split(str)


'''
PS I tried using the code snippet:
...

While(stack != None):
    stack2.push(stack.pop)

...

but it does not seem to be working if anyone can solve it they can make it faster
as we are calculatig the length of the string again and again.

'''

        