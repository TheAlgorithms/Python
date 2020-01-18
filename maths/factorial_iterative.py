# factorial of a positive integer -- https://en.wikipedia.org/wiki/Factorial


def factorial(n: int) -> int:
    """
    >>> import math
    >>> all(factorial(i) == math.factorial(i) for i in range(20))
    True
    >>> factorial(0.1)
    Traceback (most recent call last):
        ...
    ValueError: factorial() only accepts integral values
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: factorial() not defined for negative values
    """
    if n != int(n):
        raise ValueError("factorial() only accepts integral values")
    if n < 0:
        raise ValueError("factorial() not defined for negative values")
    value = 1
    for i in range(1, n + 1):
        value *= i
    return value


if __name__ == "__main__":
    n = int(input("Enter a positivve integer: ").strip() or 0)
    print(f"factorial{n} is {factorial(n)}")
