# Fibonacci Sequence Using Recursion


def fibonacci(limit):
    first_number = 1
    second_number = 1

    fibonaccci = [0, first_number , second_number ]

    for i in range(limit-3):
        first_number , second_number = second_number , first_number + second_number

        fibonaccci.append(second_number)
    return fibonaccci


while True:

    number = int(input("How many terms to include in fibonacci series: "))


    if number <= 0:
        print("Please enter a positive integer: ")
    elif number == 1:
        nump = [0]
        print(nump)
        break
    elif number == 2:
        pump = [0,1]
        print(pump)
        break
    else:
        print("The first {number} terms of the fibonacci series are as follows")
        print(fibonacci(number))

        break



