def fibonacci(n: int) -> list[int]:
    """
    Return first n Fibonacci numbers.
    Example:
    >>> fibonacci(5)
    [0, 1, 1, 2, 3]
    """
    if n <= 0:
        return []
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
    return fib_seq[:n]
