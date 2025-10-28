def fibonacci_iterative(n: int) -> int:
    """
    Return the n-th Fibonacci number using an iterative approach.

    The function returns the Fibonacci number at index n where:
    F(0) == 0, F(1) == 1, F(2) == 1, ...

    Examples:
    >>> fibonacci_iterative(0)
    0
    >>> fibonacci_iterative(1)
    1
    >>> fibonacci_iterative(7)
    13
    """
    if n < 0:
        raise ValueError("Input must be a non-negative integer")

    if n == 0:
        return 0
    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, a + b
    return b


if __name__ == "__main__":
    # simple demonstration
    print(fibonacci_iterative(7))  # expected 13
