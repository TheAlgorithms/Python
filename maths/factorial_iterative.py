def factorial_iterative(number: int) -> int:
    """
    Return the factorial of a non-negative integer using an iterative method.

    >>> factorial_iterative(5)
    120
    >>> factorial_iterative(0)
    1
    >>> factorial_iterative(1)
    1
    """
    if number < 0:
        raise ValueError("Input must be a non-negative integer")

    result = 1
    for i in range(2, number + 1):
        result *= i
    return result


if __name__ == "__main__":
    # simple demonstration
    print(factorial_iterative(5))  # expected 120
