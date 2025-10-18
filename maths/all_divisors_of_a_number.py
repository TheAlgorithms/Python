def divisors_of_number(number: int) -> list[int]:
    """
    Returns a sorted list of all divisors of the input number.
    optimized approach by checking divisors only up to the square root of the number.

    @param number: a positive integer whose divisors are to be found
    @return: a sorted list of divisors of the number

    >>> divisors_of_number(15)
    [1, 3, 5, 15]
    >>> divisors_of_number(12)
    [1, 2, 3, 4, 6, 12]
    >>> divisors_of_number(1)
    [1]
    >>> divisors_of_number(-5)
    Traceback (most recent call last):
      ...
    ValueError: Input must be positive
    >>> divisors_of_number(2.5)
    Traceback (most recent call last):
      ...
    ValueError: Input must be an integer
    """
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")
    if number <= 0:
        raise ValueError("Input must be positive")

    i = 1
    divisors = []

    while i * i <= number:
        if number % i == 0:
            divisors.append(i)
            if i != number // i:
                divisors.append(number // i)
        i += 1

    divisors.sort()
    return divisors


if __name__ == "__main__":
    import doctest

    doctest.testmod()
