# Fibonacci Sequence Using Recursion


def fibonacci(limit):
    first_number = 1
    second_number = 1

    fibonaccci = [first_number , second_number ]

    for i in range(limit):
        first_number , second_number = second_number , first_number + second_number

        fibonaccci.append(second_number)
    print(fibonaccci)


number = int(input("How many terms to include in fibonacci series: "))

if number <= 0:
    print("Please enter a positive integer: ")
else:
    print(f"The first {number} terms of the fibonacci series are as follows")
    fibonacci(number)



