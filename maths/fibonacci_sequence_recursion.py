# Fibonacci Sequence Using Recursion


def recur_fibo(n):
    """
    >>> [recur_fibo(i) for i in range(12)]
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    """
    return n if n <= 1 else recur_fibo(n-1) + recur_fibo(n-2)


def main():
    limit = int(input("How many terms to include in fibonacci series: "))
    if limit > 0:
        print(f"The first {limit} terms of the fibonacci series are as follows:")
        print([recur_fibo(n) for n in range(limit)])
    else:
        print("Please enter a positive integer: ")


if __name__ == "__main__":
    main()
