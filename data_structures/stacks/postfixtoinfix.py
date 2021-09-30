def is_operand(x): #check wheather the character is am operamd or not 

	return (((x>='A') and(x<='Z')) or ((x >= 'a') and (x <= 'z')))

def convert_infix(expression): #converts the expression
	s = []                     #create stack to store operators
	for i in expression:	
		if (is_operand(i)) :		
			s.insert(0, i)           #if encountered character is a operand it is placed in the stack.
		else:	                     #else 
			operator1 = s[0]               #the first element is popped and storred
			s.pop(0)
			operator2 = s[0]               #the second element is popped and storred
			s.pop(0)
			s.insert(0,"("+operator2+i+operator1+ ")")           #the operands are arranged to be in infix order around the element

	return s[0]

if __name__ == '__main__':
	expression = input()       #string
	print(convert_infix(expression.strip()))   #call the function

