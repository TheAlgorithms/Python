def is_disarium(num: int) -> bool:
    """
    Checks if a number is a "Disarium number".
    A Disarium number is a number defined by
    the following process: Sum of its digits
    powered with their respective position is
    equal to the original number.

    >>> is_disarium(89)
    True
    >>> is_disarium(175)
    True
    >>> is_disarium(518)
    True
    >>> is_disarium(42)
    False
    >>> is_disarium(12)
    False
    >>> is_disarium(20)
    False
    """
    return sum([int(digit) ** (pos + 1) for pos, digit in enumerate(str(num))]) == num
