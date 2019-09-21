__author__ = 'Sarvesh Dubey'

'Easier code to understand a stack'

stack = []
size = int(input("What is the size of your stack?"))

def display_stack():
	print("The elements in the stack are:")
	for element in stack:
		print(element)

while size>0:
    k = input('Enter the operation you want to do: pop or push or display')
    if k=='pop':
        try:
            stack.pop()
        except:
            print('Stack Empty')
    elif k=='push':
        p = int(input('Enter the element to add'))
        size-=1
        stack.append(p)
    elif k=='display':
        display_stack()
