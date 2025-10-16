"""
The Arithmetic Mean of n numbers is defined as the sum of the numbers
divided by n. It is used to measure the central tendency of the numbers.
https://en.wikipedia.org/wiki/Arithmetic_mean
"""


def compute_arithmetic_mean(*args: float) -> float:
    """
    Return the arithmetic mean of the argument numbers.
    If invalid input is provided, it prints an error message and returns None.

    >>> compute_arithmetic_mean(1, 2, 3, 4, 5)
    3.0
    >>> compute_arithmetic_mean(5, 10)
    7.5
    >>> compute_arithmetic_mean('a', 69)
    'Error: Not a Number'
    >>> compute_arithmetic_mean()
    'Error: At least one number is required'
    >>> compute_arithmetic_mean(2.5, 3.5, 4.0)
    3.3333333333333335
    """
    try:
        if len(args) == 0:
            raise ValueError("At least one number is required")

        total = 0
        count = 0
        for number in args:
            if not isinstance(number, (int, float)):
                raise TypeError("Not a Number")
            total += number
            count += 1

        return total / count

    except (TypeError, ValueError) as error:
        return f"Error: {error}"


if __name__ == "__main__":
    from doctest import testmod

    testmod(name="compute_arithmetic_mean")
    print(compute_arithmetic_mean(1, 2, 3, 4, 5))
    print(compute_arithmetic_mean("a", 69))
    print(compute_arithmetic_mean())
