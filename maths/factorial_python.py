"""Python program to find the factorial of a number provided by the user."""

# change the value for a different result
NUM = 10

# uncomment to take input from the user
# num = int(input("Enter a number: "))

FACTORIAL = 1

# check if the number is negative, positive or zero
if NUM < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif NUM == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, NUM + 1):
        FACTORIAL = FACTORIAL * i
    print("The factorial of", NUM, "is", FACTORIAL)
