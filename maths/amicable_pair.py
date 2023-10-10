"""
Amicable numbers are two different natural numbers such that the sum
of the proper divisors of each is equal to the other number.
That is, s(a)=b and s(b)=a, where s(n) is equal to
the sum of positive divisors of n except n itself.
Here, a and b form a pair of amicable numbers.

More information about amicable numbers can be found here:
https://en.wikipedia.org/wiki/Amicable_numbers

Here, we have defined a function to check if two numbers are amicable.
We have also defined an auxiliary function,
to find the sum of the proper divisors of a number.
"""

def sum_of_divisors(n: int) -> int:
    """
    Find the sum of the proper divisors of a number.
    
    Examples:
    >>> sum_of_divisors(220)
    284
    >>> sum_of_divisors(284)
    220
    """
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    
    return sum

def is_amicable_pair(a: int, b: int) -> bool:
    """
    Check if two numbers (a and b) are amicable numbers.
    Arguments must be positive integers.
    
    Examples:
    >>> is_amicable_pair(220, 284)
    True
    >>> is_amicable_pair(1184, 1210)
    True
    >>> is_amicable_pair(127, 729)
    False
    >>> is_amicable_pair(7, 13)
    False
    >>> is_amicable_pair(0, 12)
    Traceback (most recent call last):
        ...
    ValueError: Numbers must be positive integers.
    >>> is_amicable_pair(12, -1)
    Traceback (most recent call last):
        ...
    ValueError: Numbers must be positive integers.
    >>> is_amicable_pair(42, 42)
    False
    """
    if a <= 0 or b <= 0:
        raise ValueError("Numbers must be positive integers.")

    return sum_of_divisors(a) == b and sum_of_divisors(b) == a

if __name__ == "__main__":
    import doctest
    doctest.testmod()