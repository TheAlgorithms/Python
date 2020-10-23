"""
__author__ = "Utkarsh Singh"
"""
"""
This is a Python program to reverse a stack using recursion.
Problem Description
The program creates a stack and allows the user to perform push and pop operations on it.
"""
"""
Create a class Stack with instance variable items initialized to an empty list.
"""
class Stack:
    def __init__(self):
        self.items = []
    """
    Define methods push, pop, is_empty and display inside the class Stack.
    """
    """
    The method is_empty returns True only if items is empty.
    """
    def is_empty(self):
        return self.items == []
    """
    The method push appends data to items.
    """
    def push(self, data):
        self.items.append(data)
    """
    The method pop pops the first element in items.
    """
    def pop(self):
        return self.items.pop()
    """
    The method display prints the elements of the stack from top to bottom.
    """
    def display(self):
        for data in reversed(self.items):
            print(data)
    """
    Define function insert_at_bottom which takes a stack and a data item as arguments.
    The function insert_at_bottom adds the data item to the bottom of the stack using recursion.
    """
def insert_at_bottom(s, data):
    if s.is_empty():
        s.push(data)
    else:
        popped = s.pop()
        insert_at_bottom(s, data)
        s.push(popped)
 
    """
    Define function reverse_stack which takes a stack as argument.
    The function reverse_stack reverses the stack using recursion.
    """
def reverse_stack(s):
    if not s.is_empty():
        popped = s.pop()
        reverse_stack(s)
        insert_at_bottom(s, popped)
 
    """
    Create an instance of Stack, push data to it and reverse the stack.
    """
s = Stack()
data_list = input('Please enter the elements to push: ').split()
for data in data_list:
    s.push(int(data))
 
print('The stack:')
s.display()
reverse_stack(s)
print('After reversing:')
s.display()

"""
OUTPUT:
Case 1:
Please enter the elements to push: 7 3 1 5
The stack:
5
1
3
7
After reversing:
7
3
1
5
 
Case 2:
Please enter the elements to push: 3
The stack:
3
After reversing:
3
 
Case 3:
Please enter the elements to push: 1 2
The stack:
2
1
After reversing:
1
2
"""
