# Finding the factorial.
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact
# Taking the user input.
number = int(input("Enter the Number: "))
# Printing the answer.
answer = sum([int(i) for i in str(factorial(number))])
print(answer)
