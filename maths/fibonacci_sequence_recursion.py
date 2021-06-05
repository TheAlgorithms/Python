# Fibonacci Sequence Using Recursion
# On-Line Encyclopedia of Integer Sequences entry: https://oeis.org/A000045


def recur_fibo(n: int) -> int:
    """
    >>> [recur_fibo(i) for i in range(12)]
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    """
    return n if n <= 1 else recur_fibo(n - 1) + recur_fibo(n - 2)


def binary_recursive_fibonacci(n: int) -> int:
    """
    Returns the nth Fibonacci number.
    This function implements a recursion based on the formulas below:
    - F(2k+1) = F(k)**2 + F(k+1)**2
    - F(2k) = F(k+1) * (2F(k+1) -F(k))

    >>> [binary_recursive_fibonacci(i) for i in range(20)]
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n == 3:
        return 2

    k, rem = divmod(n, 2)
    tmp1 = binary_recursive_fibonacci(k + 1)
    tmp2 = binary_recursive_fibonacci(k)
    if rem == 1:
        return tmp1 ** 2 + tmp2 ** 2
    else:
        return tmp2 * (2 * tmp1 - tmp2)


def main() -> None:
    limit = int(input("How many terms to include in fibonacci series: "))
    if limit > 0:
        print(f"The first {limit} terms of the fibonacci series are as follows:")
        print([recur_fibo(n) for n in range(limit)])
        print(f"The first {limit} terms of the fibonacci series are as follows:")
        print([binary_recursive_fibonacci(n) for n in range(limit)])
    else:
        print("Please enter a positive integer: ")


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    main()
