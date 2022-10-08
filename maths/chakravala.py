"""
Implementing Chakravala method using python

https://en.wikipedia.org/wiki/Chakravala_method
https://kappadath-gopal.blogspot.com/2013/04/ancient-medieval-indian-mathematics.html

The chakravala method is a cyclic algorithm to solve indeterminate quadratic equations,
including Pell's equation.

"""

import math


def is_perfect_square(num: int) -> bool:
    """
    Check if a number is perfect square number or not
    :param num: the number to be checked
    :return: True if number is square number, otherwise False

    >>> is_perfect_square(9)
    True
    >>> is_perfect_square(16)
    True
    >>> is_perfect_square(1)
    True
    >>> is_perfect_square(0)
    True
    >>> is_perfect_square(10)
    False
    """

    sr = int(math.sqrt(num))
    return sr * sr == num


def chakravala_method(num: int) -> (tuple[int, int] | tuple):
    """
    This method takes in the value of N in the equation

    x^2 = N*y^2 + 1
    :param num: the number N equals to
    :return: empty tuple if N is perfect square else tuple(x,y)

    >>> chakravala_method(1)
    ()
    >>> chakravala_method(2)
    (3, 2)
    >>> chakravala_method(4)
    ()
    >>> chakravala_method(5)
    (9, 4)
    >>> chakravala_method(7)
    (8, 3)

    """

    if is_perfect_square(num):
        return ()

    # Takes b = 1 and finds a and k accordingly, refer to algorithm link
    # variable naming is used as same as algorithm, (a,b,k,m) except N = num

    b = 1

    min_diff = num
    a = 0
    while True:
        diff = abs(num - (a + 1) ** 2)
        if min_diff > diff:
            min_diff = diff
            a += 1
            continue
        break

    k = a**2 - num

    while True:

        kabs = abs(k)

        if k == 1:
            return (a, b)

        if k == -1 or kabs == 2 or (kabs == 4 and (a % 2 == 0 or b % 2 == 0)):
            return (abs((a**2 + num * b**2) // k), abs(2 * a * b // k))

        min_diff = num
        n = 1  # loop variable
        n2 = n  # stores the correct value of n
        while True:
            if kabs * n <= a:
                n += 1
                continue
            if (kabs * n - a) % b == 0:
                m = (kabs * n - a) // b
            else:
                n += 1
                continue

            diff = abs(m**2 - num)
            if min_diff > diff:
                min_diff = diff
                n2 = n
                n += 1
                continue
            break
        m = (kabs * n2 - a) // b

        a, b = abs((a * m + num * b) // k), abs((a + b * m) // k)
        k = (m**2 - num) // k


if __name__ == "__main__":

    import doctest

    doctest.testmod()

    print("X and Y for the equation X^2 - 13Y^2 = 1 is: ", chakravala_method(13))
