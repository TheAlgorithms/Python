def add(a,b):
	return(a+b)

def sub(a,b):
	return(a-b)

def prd(a,b):
	return(a*b)

def div(a,b):
	return(a/b)

n=int(raw_input("\n 1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Division\n 0. Exit\n\n Enter your Choice!\n"))
if(n==0):
	exit()
a=int(raw_input("\n\n First Number : "))
b=int(raw_input("\n\n Second Number : "))
if(n==1):
	print"\n Sum=",add(a,b)
elif(n==2):
	print"\n Difference=",sub(a,b)
elif(n==3):
	print"\n Product=",prd(a,b)
elif(n==4):
	print"\n Quotient=",div(a,b)
else:
	print"Invalid Entry!"

raw_input() #Used while using python in windows to avoid sudden exit of program.
