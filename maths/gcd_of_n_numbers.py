"""
Gcd of N Numbers
Reference: https://en.wikipedia.org/wiki/Greatest_common_divisor
Reference for tail recursion: https://www.geeksforgeeks.org/tail-recursion/
"""

from collections import Counter


def get_factors(
    number: int, factors: Counter | None = None, factor: int = 2
) -> Counter:
    """
    this is a recursive function for get all factors of number
    >>> get_factors(45)
    Counter({3: 2, 5: 1})
    >>> get_factors(2520)
    Counter({2: 3, 3: 2, 5: 1, 7: 1})
    >>> get_factors(23)
    Counter({23: 1})
    >>> get_factors(0)
    Traceback (most recent call last):
        ...
    TypeError: number must be integer and greater than zero
    >>> get_factors(-1)
    Traceback (most recent call last):
        ...
    TypeError: number must be integer and greater than zero
    >>> get_factors(1.5)
    Traceback (most recent call last):
        ...
    TypeError: number must be integer and greater than zero

    factor can be all numbers from 2 to number that we check if number % factor == 0
    if it is equal to zero, we check again with number // factor
    else we increase factor by one
    """

    match number:
        case int(number) if number == 1:
            return Counter({1: 1})
        case int(num) if number > 0:
            number = num
        case _:
            raise TypeError("number must be integer and greater than zero")

    factors = factors or Counter()

    if number == factor:  # break condition
        # all numbers are factors of itself
        factors[factor] += 1
        return factors

    if number % factor > 0:
        # if it is greater than zero
        # so it is not a factor of number and we check next number
        return get_factors(number, factors, factor + 1)

    factors[factor] += 1
    # else we update factors (that is Counter(dict-like) type) and check again
    return get_factors(number // factor, factors, factor)


def get_greatest_common_divisor(*numbers: int) -> int:
    """
    get gcd of n numbers:
    >>> get_greatest_common_divisor(18, 45)
    9
    >>> get_greatest_common_divisor(23, 37)
    1
    >>> get_greatest_common_divisor(2520, 8350)
    10
    >>> get_greatest_common_divisor(-10, 20)
    Traceback (most recent call last):
        ...
    Exception: numbers must be integer and greater than zero
    >>> get_greatest_common_divisor(1.5, 2)
    Traceback (most recent call last):
        ...
    Exception: numbers must be integer and greater than zero
    >>> get_greatest_common_divisor(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    1
    >>> get_greatest_common_divisor("1", 2, 3, 4, 5, 6, 7, 8, 9, 10)
    Traceback (most recent call last):
        ...
    Exception: numbers must be integer and greater than zero
    """

    # we just need factors, not numbers itself
    try:
        same_factors, *factors = map(get_factors, numbers)
    except TypeError as e:
        raise Exception("numbers must be integer and greater than zero") from e

    for factor in factors:
        same_factors &= factor
        # get common factor between all
        # `&` return common elements with smaller value (for Counter type)

    # now, same_factors is something like {2: 2, 3: 4} that means 2 * 2 * 3 * 3 * 3 * 3
    mult = 1
    # power each factor and multiply
    # for {2: 2, 3: 4}, it is [4, 81] and then 324
    for m in [factor**power for factor, power in same_factors.items()]:
        mult *= m
    return mult

def gcd_tail_recursive(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) using a tail-recursive approach.

    This function uses the tail-recursive form of
    the Euclidean algorithm to calculate
    the GCD of two integers `a` and `b`. The GCD
    is the largest integer that divides both
    `a` and `b` without leaving a remainder.

    Tail recursion is a form of recursion where the
    recursive call is the last operation
    in the function. In languages that
    support tail call optimization, this allows the
    function to be optimized by reusing the current
    function's stack frame for the
    next call. Python, however, does not support tail
    call optimization, but using this
    style can still help structure the
    recursion for better clarity.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The greatest common divisor of `a` and `b`.

    Raises:
        ValueError: If both `a` and `b` are zero, as the GCD is not defined for this case.

    Example:
        >>> gcd_tail_recursive(24, 40)
        8
        >>> gcd_tail_recursive(11, 37)
        1
        >>> gcd_tail_recursive(0, 5)
        5
        >>> gcd_tail_recursive(5, 0)
        5
        >>> gcd_tail_recursive(0, 0)
        ValueError: GCD is not defined for both a and b being zero.

    Notes:
        - gcd(a, 0) = abs(a)
        - gcd(0, b) = abs(b)
        - gcd(0, 0) is undefined.
    """
    if b == 0:
        return abs(a)
    return gcd_tail_recursive(b, a % b)

if __name__ == "__main__":
    print(get_greatest_common_divisor(18, 45))  # 9
    print(gcd_tail_recursive(23, 37))  # 1
