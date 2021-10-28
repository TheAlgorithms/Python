"""
Project Euler Problem 686: https://projecteuler.net/problem=686

2^7 = 128 is the first power of two whose leading digits are "12".
The next power of two whose leading digits are "12" is 2^80.

Define p(L,n) to be the nth-smallest value of j such that
the base 10 representation of 2^j begins with the digits of L.

So p(12, 1) = 7 and p(12, 2) = 80.

You are given that p(123, 45) = 12710.

Find p(123, 678910).
"""

import math


def log_difference(number: int) -> float:
    """
    This function returns the decimal value of a number multiplied with log(2)
    Since the problem is on powers of two, finding the powers of two with
    large exponents is time consuming. Hence we use log to reduce compute time.

    We can find out that the first power of 2 with starting digits 123 is 90.
    Computing 2^90 is time consuming.
    Hence we find log(2^90) = 90*log(2) = 27.092699609758302
    But we require only the decimal part to determine whether the power starts with 123.
    SO we just return the decimal part of the log product.
    Therefore we return 0.092699609758302

    >>> log_difference(90)
    0.092699609758302
    >>> log_difference(379)
    0.090368356648852

    """

    log_number = math.log(2, 10) * number
    difference = round((log_number - int(log_number)), 15)

    return difference


def solution(number: int = 678910) -> int:
    """
    This function calculates the power of two which is nth (n = number)
    smallest value of power of 2
    such that the starting digits of the 2^power is 123.

    For example the powers of 2 for which starting digits is 123 are:
    90, 379, 575, 864, 1060, 1545, 1741, 2030, 2226, 2515 and so on.
    90 is the first power of 2 whose starting digits are 123,
    379 is second power of 2 whose starting digits are 123,
    and so on.

    So if number = 10, then solution returns 2515 as we observe from above series.

    Wwe will define a lowerbound and upperbound.
    lowerbound = log(1.23), upperbound = log(1.24)
    because we need to find the powers that yield 123 as starting digits.

    log(1.23) = 0.08990511143939792, log(1,24) = 0.09342168516223506.
    We use 1.23 and not 12.3 or 123, because log(1.23) yields only decimal value
    which is less than 1.
    log(12.3) will be same decimal vale but 1 added to it
    which is log(12.3) = 1.093421685162235.
    We observe that decimal value remains same no matter 1.23 or 12.3
    Since we use the function log_difference(),
    which returns the value that is only decimal part, using 1.23 is logical.

    If we see, 90*log(2) = 27.092699609758302,
    decimal part = 0.092699609758302, which is inside the range of lowerbound
    and upperbound.

    If we compute the difference between all the powers which lead to 123
    starting digits is as follows:

    379 - 90 = 289
    575 - 379 = 196
    864 - 575 = 289
    1060 - 864 = 196

    We see a pattern here. The difference is either 196 or 289 = 196 + 93.

    Hence to optimize the algorithm we will increment by 196 or 93 depending upon the
    log_difference() value.

    Lets take for example 90.
    Since 90 is the first power leading to staring digits as 123,
    we will increment iterator by 196.
    Because the difference between any two powers leading to 123
    as staring digits is greater than or equal to 196.
    After incrementing by 196 we get 286.

    log_difference(286) = 0.09457875989861 which is greater than upperbound.
    The next power is 379, and we need to add 93 to get there.
    The iterator will now become 379,
    which is the next power leading to 123 as starting digits.

    Lets take 1060. We increment by 196, we get 1256.
    log_difference(1256) = 0.09367455396034,
    Which is greater than upperbound hence we increment by 93. Now iterator is 1349.
    log_difference(1349) = 0.08946415071057 which is less than lowerbound.
    The next power is 1545 and we need to add 196 to get 1545.

    Conditions are as follows:

    1) If we find a power, whose log_difference() is in the range of
    lower and upperbound, we will increment by 196.
    which implies that the power is a number which will lead to 123 as starting digits.
    2) If we find a power, whose log_difference() is greater than or equal upperbound,
    we will increment by 93.
    3) if log_difference() < lowerbound, we increment by 196.

    Reference to the above logic:
    https://math.stackexchange.com/questions/4093970/powers-of-2-starting-with-123-does-a-pattern-exist

    >>> solution(1000)
    284168

    >>> solution(56000)
    15924915

    >>> solution(678910)
    193060223

    """

    power_iterator = 90
    position = 0

    lower_limit = math.log(1.23, 10)
    upper_limit = math.log(1.24, 10)
    previous_power = 0

    while position < number:
        difference = log_difference(power_iterator)

        if difference >= upper_limit:
            power_iterator += 93

        elif difference < lower_limit:
            power_iterator += 196

        else:
            previous_power = power_iterator
            power_iterator += 196
            position += 1

    return previous_power


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(f"{solution() = }")
