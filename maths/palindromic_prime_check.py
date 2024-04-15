"""
A palindromic prime is a prime number that is also palindromic, meaning it remains
the same when its digits are reversed.

For more information about palindromic primes, refer to:
https://en.wikipedia.org/wiki/Palindromic_prime
"""


def is_prime(number: int) -> bool:
    """
    Check if a number is prime.

    Args:
        number: A positive integer.

    Returns:
        True if the number is prime, False otherwise.

    Raises:
        ValueError: If number is not a positive integer.

    Examples:
        >>> is_prime(2)
        True
        >>> is_prime(3)
        True
        >>> is_prime(88)
        False
        >>> is_prime(1)
        False
        >>> is_prime(9679)
        True
        >>> is_prime(0)
        Traceback (most recent call last):
            ...
        ValueError: Input must be a positive integer.
        >>> is_prime(-17)
        Traceback (most recent call last):
            ...
        ValueError: Input must be a positive integer.
        >>> is_prime(9.51)
        Traceback (most recent call last):
            ...
        ValueError: Input must be a positive integer.
        >>> is_prime("261")
        Traceback (most recent call last):
            ...
        ValueError: Input must be a positive integer.
    """
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Input must be a positive integer.")

    if 1 < number < 4:
        return True
    elif number < 2 or (number % 2 == 0):
        return False

    # Return True if number is not divisible by any odd number up to its square root
    return all(number % i != 0 for i in range(3, int(number**0.5) + 1, 2))


def palindromic_prime_check(number: int) -> bool:
    """
    Check if a number is a palindromic prime number.

    Args:
        number: A positive integer.

    Returns:
        True if the number is a palindromic prime number, False otherwise.

    Raises:
        ValueError: If number is not a positive integer.

    Examples:
        >>> palindromic_prime_check(13)
        False
        >>> palindromic_prime_check(131)
        True
        >>> palindromic_prime_check(121)
        False
        >>> palindromic_prime_check(929)
        True
        >>> palindromic_prime_check(2)
        True
        >>> palindromic_prime_check(7)
        True
        >>> palindromic_prime_check(0)
        Traceback (most recent call last):
            ...
        ValueError: Input must be a positive integer.
        >>> palindromic_prime_check(-131)
        Traceback (most recent call last):
            ...
        ValueError: Input must be a positive integer.
        >>> palindromic_prime_check(1.9)
        Traceback (most recent call last):
            ...
        ValueError: Input must be a positive integer.
        >>> palindromic_prime_check("hello")
        Traceback (most recent call last):
            ...
        ValueError: Input must be a positive integer.
    """
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Input must be a positive integer.")

    if is_prime(number):
        number_str = str(number)
        if number_str == number_str[::-1]:
            return True
    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
