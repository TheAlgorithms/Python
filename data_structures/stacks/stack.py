__author__ = 'Haresh Singh'

    """ A stack is an abstract data type that serves as a collection of
    elements with two principal operations: push() and pop(). push() adds an
    element to the top of the stack, and pop() removes an element from the top
    of a stack. The order in which elements come off of a stack are
    Last In, First Out (LIFO).

    https://en.wikipedia.org/wiki/Stack_(abstract_data_type)
    """

stack = []
size = input("What is the size of your stack?")

def display_stack():
	print("The elements in the stack are:")
	for element in stack:
		print(element)
def stack_push(new_Element):
	if(len(stack) < size):
		stack.append(new_Element)
	else:
		print("Stack is full")
def stack_pop(self):
	if(len(stack) > 0):
		stack.pop()
	else:
		print("There's nothing to pop!")

for i in range(0, size):
	stack_push(i)
	display_stack()

for i in range(0,size):
	stack_pop(i)
	display_stack()
