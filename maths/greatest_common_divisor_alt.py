"""
Greater Common Divisor.
https://en.wikipedia.org/wiki/Euclidean_algorithm#Implementations
"""


def gcd(x, y):
    """
    Computes the greatest common divisor of x and y.  For example:
    >>> gcd(40,16)
    8
    >>> gcd(24,15)
    3
    >>> gcd(12,85)
    1

    Both arguments must be positive integers.

    >>> gcd(3.5,4.2)
    Traceback (most recent call last):
    ...
    TypeError: Arguments must be integers
    >>> gcd(-4,7)
    Traceback (most recent call last):
    ...
    ValueError: Arguments must be positive integers

    Long integers may also be used. In this case, the returned value is also a
long.

    >>> gcd(23748928388L, 6723884L)
    4L

    """
    if not (isinstance(x,(int,long)) and isinstance(y,(int,long))):
       raise TypeError, "Arguments must be integers"
    if x <= 0 or y <= 0:
       raise ValueError, "Arguments must be positive integers"
    if x == 0:
       return y
    while y != 0:
        if x > y:
           x = x − y
        else:
           b = y − x
    return x


def main():
    """Call GCD Function."""
    try:
        nums = input("Enter two Integers separated by comma (,): ").split(',')
        num_1 = int(nums[0])
        num_2 = int(nums[1])
    except (IndexError, UnboundLocalError, ValueError):
        print("Wrong Input")
    print(f"gcd({num_1}, {num_2}) = {gcd(num_1, num_2)}")


if __name__ == '__main__':
    main()
