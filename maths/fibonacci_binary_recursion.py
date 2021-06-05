# Fibonacci Sequence Using Binary Recursion
# On-Line Encyclopedia of Integer Sequences entry: https://oeis.org/A000045


def binary_recur_fibo(n: int) -> int:
    """
    Returns the nth Fibonacci number.
    This function is based on the formulas:
    - F(2k+1) = F(k)**2 + F(k+1)**2
    - F(n+2) = F(n+1) + F(n)
    >>> [binary_recur_fibo(i) for i in range(20)] # doctest: +NORMALIZE_WHITESPACE
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,
     144, 233, 377, 610, 987, 1597, 2584, 4181]
    """
    if n == 0 or n == 1:
        return n
    k, rem = divmod(n, 2)
    if rem == 1:
        return binary_recur_fibo(k) ** 2 + binary_recur_fibo(k + 1) ** 2
    return binary_recur_fibo(n - 1) + binary_recur_fibo(n - 2)


def main() -> None:
    limit = int(input("How many Fibonacci numbers you want?> "))
    if limit > 0:
        print(f"The first {limit} Fibonacci numbers are: ")
        print([binary_recur_fibo(n) for n in range(limit)])
    else:
        print("Please enter a positive integer: ")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
