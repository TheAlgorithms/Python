def factorial(n):
    """
    Return 1, if n is 1 or 0,
    otherwise, return n * fact(n-1).

    >>> factorial(1)
    1
    >>> factorial(6)
    720
    >>> factorial(0)
    1
    """
    if n < 0:
        raise ValueError(n, "is negative")
    return 1 if n == 0 or n == 1 else n * factorial(n - 1)


"""
Show factorial for i,
where i ranges from 0 to 20.
"""
for i in range(21):
    print(i, ": ", factorial(i), sep="")
