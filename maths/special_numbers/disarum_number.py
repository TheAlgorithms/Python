"""
A number n is said to be a Disarium number if
the sum of its digits powered to their respective positions equals the number itself.

Examples of Disarium Numbers: 1, 2, 3, 4, 5, 6, 7, 8, 9, 89, 135, 175, 518, 598, ...
"""

def is_disarium_number(number: int) -> bool:
    """
    This function takes an integer number as input.
    Returns True if the number is a Disarium number.

    >>> is_disarium_number(-1)
    False
    >>> is_disarium_number(0)
    False
    >>> is_disarium_number(1)
    True
    >>> is_disarium_number(89)
    True
    >>> is_disarium_number(135)
    True
    >>> is_disarium_number(175)
    True
    >>> is_disarium_number(518)
    True
    >>> is_disarium_number(598)
    True
    >>> is_disarium_number(123)
    False
    >>> is_disarium_number(89.0)
    Traceback (most recent call last):
        ...
    TypeError: Input value of [number=89.0] must be an integer
    """
    if not isinstance(number, int):
        msg = f"Input value of [number={number}] must be an integer"
        raise TypeError(msg)
    if number < 1:
        return False

    digits = str(number)
    total = sum(int(digit) ** (idx + 1) for idx, digit in enumerate(digits))
    return total == number

if __name__ == "__main__":
    import doctest
    doctest.testmod()
