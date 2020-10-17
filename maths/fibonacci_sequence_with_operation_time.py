#!/usr/bin/env python3
# charset="utf-8"

# fibonacci_iterative.py

"""
1. Calculates the iterative fibonacci sequence using user input
2. Returns the time used for fibonacci calculation.
3. Performs 3 additional operations based on the request of the user which:
    * 1 Obtains the value of the nth term in the sequence"
    * 2 Series of the sequence"
    * The value prior to a selected value"

Added feature: Returns the username and local time of user.
"""

from getpass import getuser as me
import sys
import time


print(f"\nHello, {me()}!\nI'm glad you decided to run my code on the Fibonacci sequence\n")

while True:
    try:
        number = int(input("Enter the number of sequence you want to generate:").strip())
    except ValueError:
        number = int(input("Please enter an integer value: ").strip())
    finally:
        if number <= 1:
            print("Your requested value is invalid, enter a value greater than 1\n")
        else:
            break


def fibonacci(fib_number:int) -> list:
    """
    Returns list offibonacci sequence based on the user specified number
    >>> fibonacci(fib_number=2)
    [0, 1]
    >>> fibonacci(fib_number=6)
    [0, 1, 1, 2, 3, 5]
    >>> fibonacci(fib_number=10)
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    a:int = 0
    b:int = 1
    global fib
    fib = [a, b]

    start_time = time.perf_counter()

    for value in range(2, fib_number, 1):
        value:int = a + b
        a = b
        b = value
        fib.append(value)

    end_time = time.perf_counter()

    global operation_time
    operation_time = end_time - start_time

    return fib


print("\n{0}, your requested Fibonacci sequence with {1} terms is: {2}".format(me(), number, fibonacci(number)))
print(f"Operation time: {operation_time:0.8f} seconds")


print("\n{},we have three operations that might be of interest to you. If you wish to engage in any of them,"
      "\nPlease input the integer value according to what you wish to perform or reply \"no\" if you're not interested"
      "\n1 Obtain the value of the nth term in the sequence"
      "\n2 Series of the sequence"
      "\n3 The value prior to a selected value".format(me()))


def fibonnacci_other_operations() -> int:

    request = input("\nPlease enter your response:").strip()
    if request == "no":
        print(f"\nAlright, have a lovely day!")
        sys.exit()
    elif int(request) in (1, 2, 3):
        required = int(request)
    else:
        print("The value you entered is not valid!")

    global message

    if required == 1:
        """
        Returns the nth term specified by the user
        """
        nth = int(input("\nEnter your the nth term:").strip())
        return_request1 = fib[nth - 1]
        message = "The required nth term value is:"
        return return_request1
    elif required == 2:
        """
        Returns the series of the sequence
        """
        message = "The series of your sequence is:"
        return_request2 = sum(fib)
        return return_request2
    elif required == 3:
        """
        Returns the immediate lower value to the one specified
        """
        prior_value = int(input("Enter your the aftermath value:"))
        checker = 0
        for value in range(len(fib)):
            if fib[value] >= prior_value:
                checker = value
                break
        message = "The value prior to your selected value is:"
        return_request3 = fib[checker - 1]
        return return_request3

response = fibonnacci_other_operations()
print(message, response)