def euler_totient_function(number: int) -> int:
    """
    Euler's totient function counts the positive integers up to a given integer n
    that are relatively prime to n.

    Relative prime numbers are numbers that have no common divisors other than 1.

    >>> euler_totient_function(1)
    1
    >>> euler_totient_function(2)
    1
    >>> euler_totient_function(6)
    2
    >>> euler_totient_function(12)
    4
    >>> euler_totient_function(8)
    4
    >>> euler_totient_function(18)
    6
    >>> euler_totient_function(35)
    24
    >>> euler_totient_function(100)
    40

    """

    if int(number) != number or number < 1:
        raise ValueError("n must be a positive integer greater than 0")

    count = number
    i = 2
    while i * i <= number:
        if number % i == 0:
            count -= count // i
            while number % i == 0:
                number //= i
        i += 1

    if number >= 2:
        count -= count // number
    return count


if __name__ == "__main__":
    import doctest

    doctest.testmod()
