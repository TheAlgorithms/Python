def is_neon_number(number: int) -> bool:
    """
    Check whether a number is a Neon number.

    A Neon number is a number whose square's digits add up
    to the original number.

    >>> is_neon_number(9)
    True
    >>> is_neon_number(10)
    False
    >>> is_neon_number(0)
    True

    Reference:
    https://www.codewithvenu.com/blog/Interview-Tracks/java-coding/02-Number-Logic/07-Neon-Number
    """
    if number < 0:
        raise ValueError("Number must be non-negative")

    return sum(int(digit) for digit in str(number**2)) == number