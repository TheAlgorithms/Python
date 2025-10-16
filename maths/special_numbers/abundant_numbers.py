"""
A number n is said to be an Abundant number if
the sum of its proper divisors is greater than the number itself.

Examples of Abundant Numbers: 12, 18, 20, 24, 30, 36, 40, 42, 48, 54, ...
"""

def is_abundant_number(number: int) -> bool:
    """
    This function takes an integer number as input.
    Returns True if the number is an abundant number.
    
    >>> is_abundant_number(-1)
    False
    >>> is_abundant_number(0)
    False
    >>> is_abundant_number(12)
    True
    >>> is_abundant_number(18)
    True
    >>> is_abundant_number(28)
    False
    >>> is_abundant_number(20)
    True
    >>> is_abundant_number(6)
    False
    >>> is_abundant_number(1)
    False
    >>> is_abundant_number(945)
    True
    >>> is_abundant_number(28.0)
    Traceback (most recent call last):
        ...
    TypeError: Input value of [number=28.0] must be an integer
    """
    if not isinstance(number, int):
        msg = f"Input value of [number={number}] must be an integer"
        raise TypeError(msg)
    if number < 1:
        return False

    divisor_sum = 1  # 1 is always a proper divisor
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            divisor_sum += i
            if i != number // i:
                divisor_sum += number // i
    return divisor_sum > number

if __name__ == "__main__":
    import doctest

    doctest.testmod()
