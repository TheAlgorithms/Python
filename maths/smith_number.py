"""

Check if a number is a Smith number

Source:
    https://en.wikipedia.org/wiki/Smith_number

"""


def is_prime(number: int) -> bool:
    """
    :param number: check if a number is prime
    :return: false if a number is not prime, otherwise true

    >>> is_prime(4)
    False
    >>> is_prime(5)
    True
    """

    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            return False

    return True


def number_sum(number: int) -> int:
    """
    :param number: number to sum the digits of
    :return: the sum of the digits of a number

    >>> number_sum(22)
    4
    """

    number_total = 0
    while number:
        number_total, number = number_total + number % 10, number // 10

    return number_total


def prime_factors(number: int) -> int:
    """
    :param number: generate prime factors of a number
    :return: sum of digits of each prime factor

    >>> prime_factors(22)
    4
    """

    factor = 2
    total = 0
    while number > 1:
        if number % factor == 0:
            total += number_sum(factor)
            number //= factor
        else:
            factor += 1

    return total


def is_smith(number: int) -> bool:
    """
    :param number: check if this number is a smith number
    :return: a true of false indicating if this number is a smith number or not
    Note: This is just for base 10 numbers. This can be extended for any base
        - We will also only deal with positive integers

    >>> is_smith(22)
    True
    >>> is_smith(0)
    Traceback (most recent call last):
    ...
    ValueError: Input value of [number=0] must be > 0
    >>> is_smith(-1)
    Traceback (most recent call last):
    ...
    ValueError: Input value of [number=-1] must be > 0
    >>> is_smith(22.0)
    Traceback (most recent call last):
    ...
    TypeError: Input value of [number=22.0] must be an integer
    """

    if not isinstance(number, int):
        raise TypeError(f"Input value of [number={number}] must be an integer")

    if number < 1:
        raise ValueError(f"Input value of [number={number}] must be > 0")

    if is_prime(number):
        return False

    return prime_factors(number) == number_sum(number)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
