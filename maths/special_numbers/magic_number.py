"""
== Magic Number ==
A number where the recursive sum of digits eventually results in 1.
Example: (172) ((1+7+2=10 -> 1+0=1)).
https://www.scribd.com/document/895653665/Interesting-Number-Programs
"""


def is_magic_number(number: int) -> bool:
    """
    This functions takes an integer number as input.
    returns True if the number is magic.
    >>> is_magic_number(-1)
    False
    >>> is_magic_number(0)
    False
    >>> is_magic_number(172)
    True
    >>> is_magic_number(19)
    True
    >>> is_magic_number(124)
    False
    >>> is_magic_number(5.0)
    Traceback (most recent call last):
        ...
    TypeError: Input value of [number=5.0] must be an integer
    """
    if not isinstance(number, int):
        msg = f"Input value of [number={number}] must be an integer"
        raise TypeError(msg)
    if number <= 0:
        return False
    # the loop continues if n is 0 
    # and sum is non-zero.
    # It stops when n becomes 
    # 0 and sum becomes single digit.
    sum = 0
    while (number > 0 or sum > 9):
        if (number == 0):
            number = sum
            sum = 0
        sum = sum + number % 10
        number = number // 10

    # Return true if sum becomes 1.
    return sum == 1

if __name__ == "__main__":
    import doctest

    doctest.testmod()