# Python program to reverse a stack using recursion

def insertAtBottom(stack:list, item:int)-> None:
	if isEmpty(stack):
		push(stack, item)
	else:
		temp = pop(stack)
		insertAtBottom(stack, item)
		push(stack, temp)
    
def reverse(stack:list)-> None:
	if not isEmpty(stack):
		temp = pop(stack)
		reverse(stack)
		insertAtBottom(stack, temp)

def createStack() -> list:
	stack = []
	return stack

def isEmpty( stack:list )-> bool:
	return len(stack) == 0

def push( stack:list, item:int )-> None:
	stack.append( item )

def pop( stack : list)-> int:
	if(isEmpty( stack )):
		print("Stack Underflow ")
		exit(1)
	return stack.pop()

def prints(stack:list)-> None:
	for i in range(len(stack)-1, -1, -1):
		print(stack[i], end = ' ')
	print()

# Driver Code
stack = createStack()
push( stack, str(4) )
push( stack, str(3) )
push( stack, str(2) )
push( stack, str(1) )
print("Original Stack ")
prints(stack)
reverse(stack)
print("Reversed Stack ")
prints(stack)
