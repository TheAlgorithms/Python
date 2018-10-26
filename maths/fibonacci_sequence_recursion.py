# Fibonacci Sequence Using Recursion
#returning the elements of the Fibonacci sequence.
def recur_fibo(n):
    return n if n <= 1 else (recur_fibo(n-1) + recur_fibo(n-2))
    
def isPositiveInteger(limit):
    return limit >= 0

def main():
    #user informs how many elements the sequence will have, being positive.
    limit = int(input("How many terms to include in fibonacci series: "))
    if isPositiveInteger(limit):
        print("The first {limit} terms of the fibonacci series are as follows:")
        print([recur_fibo(n) for n in range(limit)])
    else:
        print("Please enter a positive integer: ")

if __name__ == '__main__':
    main()
