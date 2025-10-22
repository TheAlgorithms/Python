"""FizzBuzz Problem.

This module contains a solution to the classic FizzBuzz problem.
For numbers 1 to n, print 'Fizz' for multiples of 3, 'Buzz' for multiples of 5,
and 'FizzBuzz' for multiples of both.
"""


def fizz_buzz(n: int) -> list[str]:
    """
    Return a list of FizzBuzz results for numbers from 1 to n.

    For each number from 1 to n:
    - Return 'FizzBuzz' if divisible by both 3 and 5
    - Return 'Fizz' if divisible by 3
    - Return 'Buzz' if divisible by 5
    - Return the number as a string otherwise

    Args:
        n: Positive integer representing the range

    Returns:
        A list of strings containing FizzBuzz results

    Raises:
        ValueError: If n is not a positive integer

    Examples:
        >>> fizz_buzz(5)
        ['1', '2', 'Fizz', '4', 'Buzz']
        >>> fizz_buzz(15)
        ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
        >>> fizz_buzz(0)
        Traceback (most recent call last):
            ...
        ValueError: n must be a positive integer
        >>> fizz_buzz(-5)
        Traceback (most recent call last):
            ...
        ValueError: n must be a positive integer
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
