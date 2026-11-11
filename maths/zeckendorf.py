"""
https://en.wikipedia.org/wiki/Zeckendorf%27s_theorem
"""


def _fibonacci_numbers_up_to(limit: int) -> list[int]:
    """
    Return the Fibonacci numbers (1, 2, 3, 5, ...) that are <= limit.

    The sequence starts at 1, 2 rather than 1, 1 so that every number has a
    unique representation and the value 1 is used at most once.

    >>> _fibonacci_numbers_up_to(1)
    [1]
    >>> _fibonacci_numbers_up_to(10)
    [1, 2, 3, 5, 8]
    >>> _fibonacci_numbers_up_to(0)
    []
    """
    numbers: list[int] = [1, 2]
    while numbers[-1] + numbers[-2] <= limit:
        numbers.append(numbers[-1] + numbers[-2])
    return [number for number in numbers if number <= limit]


def zeckendorf(number: int) -> list[int]:
    """
    Return the Zeckendorf representation of a non-negative integer.

    Zeckendorf's theorem states that every positive integer can be written
    uniquely as the sum of one or more distinct, non-consecutive Fibonacci
    numbers. This function recovers that representation with a greedy pass
    over the Fibonacci numbers from largest to smallest, which is always
    optimal for this problem.

    >>> zeckendorf(0)
    []
    >>> zeckendorf(1)
    [1]
    >>> zeckendorf(2)
    [2]
    >>> zeckendorf(4)
    [3, 1]
    >>> zeckendorf(10)
    [8, 2]
    >>> zeckendorf(100)
    [89, 8, 3]
    >>> zeckendorf(1000)
    [987, 13]
    >>> zeckendorf(-1)
    Traceback (most recent call last):
        ...
    ValueError: zeckendorf() only accepts non-negative integers
    >>> zeckendorf(1.5)
    Traceback (most recent call last):
        ...
    TypeError: zeckendorf() only accepts integers
    """
    if isinstance(number, bool) or not isinstance(number, int):
        raise TypeError("zeckendorf() only accepts integers")
    if number < 0:
        raise ValueError("zeckendorf() only accepts non-negative integers")

    representation: list[int] = []
    remainder = number
    for fibonacci_number in reversed(_fibonacci_numbers_up_to(number)):
        if fibonacci_number <= remainder:
            representation.append(fibonacci_number)
            remainder -= fibonacci_number
    return representation


if __name__ == "__main__":
    import doctest

    doctest.testmod()
