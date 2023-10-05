def factorial_dp(num: int) -> int:
    """
    Calculate the factorial of a number using dynamic programming.

    :param num: The number for which to calculate the factorial.
    :return: The factorial of the given number.
    
    >>> factorial_dp(7)
    5040
    >>> factorial_dp(-1)
    Traceback (most recent call last):
        ...
    ValueError: Number should not be negative.
    >>> [factorial_dp(i) for i in range(10)]
    [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    """
    if num < 0:
        raise ValueError("Number should not be negative.")
    
    if num in (0, 1):
        return 1

    # Initialize a list to store factorial values
    factorials = [1] * (num + 1)

    for i in range(2, num + 1):
        factorials[i] = i * factorials[i - 1]

    return factorials[num]

if __name__ == "__main__":
    import doctest

    doctest.testmod()
