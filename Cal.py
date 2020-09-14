def addition(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def divison(x,y):
    return x/y
def power(x,y):
    return pow(x,y)

print("\nOperation: ")
print("\n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Power")

choice=input("Enter your choice: ")

if choice=='1':
    num1=int(input("Enter the first no: "))
    num2=int(input("Enter the second no: "))
    print(num1, "+", num2, "=", addition(num1,num2))
elif choice=='2':
    num1=int(input("Enter the first no: "))
    num2=int(input("Enter the second no: "))
    print(num1, "-", num2, "=", subtraction(num1,num2))
elif choice=='3':
    num1=int(input("Enter the first no: "))
    num2=int(input("Enter the second no: "))
    print(num1, "*", num2, "=", multiplication(num1,num2))
elif choice=='4':
    num1=int(input("Enter the first no: "))
    num2=int(input("Enter the second no: "))
    print(num1, "/", num2, "=", division(num1,num2))
elif choice=='5':
    num1=int(input("Enter the first no: "))
    num2=int(input("Enter the second no: "))
    print(num1, "^", num2, "=", power(num1,num2))
else:
    print("Please choose the correct option.")
