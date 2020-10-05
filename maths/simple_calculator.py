def simple_calculator(a,n,b):
try:
	if(n == '+'):
		print("\n Sum=",(a+b))
	elif(n == '-'):
		print("\n Difference=",(a-b))
	elif(n == '*'):
		print("\n Product=",(a*b))
	elif(n == '/'):
		print("\n Quotient=",(a/b))
	else:
		print("Unknown Entry!")
except:
	print("\n\n E : Exception Occured")

	
if __name__ == "__main__":
	simple_calculator(1,'+',1)
	simple_calculator(1,'-',1)
	simple_calculator(1,'*',1)
	simple_calculator(1,'/',1)
	
