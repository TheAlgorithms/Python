def add(a,b): #Addition +
	return(a+b)

def sub(a,b): #Subtraction -
	return(a-b)

def prd(a,b): #Multiplication ×
	return(a*b)

def div(a,b): #Division ÷
	return(a/b)

n=int(input("\n 1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Division\n 5. Exit\n\n Enter your Choice!\n")) #MENU
if(n == 5):
	exit()
#a=int(input("\n\n First Number : ")) #First Input
#b=int(input("\n\n Second Number : ")) #Second Input

#Driver
a=50
b=5
n=0

 #Output
try:
	if((n == 1) or (n == 0)):
		print("\n Sum=",add(a,b))
	if((n == 2) or (n == 0)):
		print("\n Difference=",sub(a,b))
	if((n == 3) or (n == 0)):
		print("\n Product=",prd(a,b))
	if((n == 4) or (n == 0)):
		print("\n Quotient=",div(a,b))
catch:
	print("Invalid Entry!")
