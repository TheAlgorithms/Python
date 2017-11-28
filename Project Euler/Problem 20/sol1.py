# Finding the factorial.
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

# Spliting the digits and adding it.
def split_and_add(number):
    sum_of_digits = 0
    while(number>0):
        last_digit = number % 10
        sum_of_digits += last_digit
        number = int(number/10) # Removing the last_digit from the given number.
    return sum_of_digits

# Taking the user input.
number = int(input("Enter the Number: "))

# Assigning the factorial from the factorial function.
factorial = factorial(number)

# Spliting and adding the factorial into answer.
answer = split_and_add(factorial)

# Printing the answer.
print(answer)
