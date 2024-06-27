"""
An emirp (prime spelled backwards) is a prime number that results in a different
prime when its digits are reversed. This means that the number is not a
palindromic prime.

For more information about emirp numbers, refer to:
https://en.wikipedia.org/wiki/Emirp
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
        >>> is_prime(4)
        False
        >>> is_prime(9679)
        True
        >>> is_prime(1)
        False
        >>> is_prime(0)
        Traceback (most recent call last):
            ...
        ValueError: Input must be a positive integer.
        >>> is_prime(-1)
        Traceback (most recent call last):
            ...
        ValueError: Input must be a positive integer.
        >>> is_prime(2.5)
        Traceback (most recent call last):
            ...
        ValueError: Input must be a positive integer.
        >>> is_prime("2")
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


def emirp_check(number: int) -> bool:
    """
    Check if a number is an emirp number.

    Args:
        number: A positive integer.

    Returns:
        True if the number is an emirp number, False otherwise.

    Raises:
        ValueError: If number is not a positive integer.

    Examples:
        >>> emirp_check(13)
        True
        >>> emirp_check(23)
        False
        >>> emirp_check(9679)
        True
        >>> emirp_check(5)
        False
        >>> emirp_check(0)
        Traceback (most recent call last):
            ...
        ValueError: Input must be a positive integer.
        >>> emirp_check(-13)
        Traceback (most recent call last):
            ...
        ValueError: Input must be a positive integer.
        >>> emirp_check(1.9)
        Traceback (most recent call last):
            ...
        ValueError: Input must be a positive integer.
        >>> emirp_check("cat")
        Traceback (most recent call last):
            ...
        ValueError: Input must be a positive integer.
        >>> emirp_check(17)
        True
        >>> emirp_check(31)
        True
        >>> emirp_check(79)
        True
        >>> emirp_check(101)
        False
    """
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Input must be a positive integer.")

    if is_prime(number):
        reversed_number = int(str(number)[::-1])
        if number != reversed_number and is_prime(reversed_number):
            return True
    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
