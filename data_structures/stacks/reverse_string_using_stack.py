#Write a program that take input as string stack and return the reverse of that string in python

class Stack():
    def __init__(self):
        self.items = []
# this function will take the item and push onto the top of the stack
    def push(self, item):
        return self.items.append(item)
# this function pop will take out the top element from the stack 
    def pop(self):
        return self.items.pop()
# to check if the stack if empy without this we can't reverse the given string.
    def is_empty(self):
        return self.items == []
# this function is optional it will just return to top of the stack when called
    def peek(self):
        if not is_empty():
            return self.items[-1]

def _reverse_(Stack, input_str_):
    # loop through the string then push it into the stack then
    # pop the item fro tne stack append to an empty string variable

    for i in range(len(input_str_)):

        Stack.push(input_str_[i])
# this empty string is where we are going to store the reversed string 
        result = ''
    while  not Stack.is_empty():
        result = result + Stack.pop()
    return result


stack = Stack()
#input_str_ = ' Abdoulaye'
input_str_= input("Enter the string to reverse: ")
print(_reverse_(stack, input_str_))
# Enter the string to reverse: Hello world
# dlrow olleH
