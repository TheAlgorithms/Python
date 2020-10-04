def add(a,b): #Addition +
	return(a+b)

def sub(a,b): #Subtraction -
	return(a-b)

def prd(a,b): #Multiplication ×
	return(a*b)

def div(a,b): #Division ÷
	return(a/b)

n=int(input("\n 1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Division\n 0. Exit\n\n Enter your Choice!\n")) #MENU
if(n == 0):
	exit()
a=int(input("\n\n First Number : ")) #First Input
b=int(input("\n\n Second Number : ")) #Second Input

 #Output
if(n == 1):
	print("\n Sum=",add(a,b))
elif(n == 2):
	print("\n Difference=",sub(a,b))
elif(n == 3):
	print("\n Product=",prd(a,b))
elif(n == 4):
	print("\n Quotient=",div(a,b))
else:
	print("Invalid Entry!")
