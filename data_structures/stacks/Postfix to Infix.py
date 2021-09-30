def isOperand(x):
	return ((x >= 'a' and x <= 'z') or
			(x >= 'A' and x <= 'Z'))


def convert_Infix(exp) :
	s = []
	for i in exp:	

		if (isOperand(i)) :		
			s.insert(0, i)

		else:	
			op1 = s[0]
			s.pop(0)
			op2 = s[0]
			s.pop(0)
			s.insert(0, "(" + op2 + i +	op1 + ")")

	return s[0]

if __name__ == '__main__':
	exp = input()
	print(convert_Infix(exp.strip()))

