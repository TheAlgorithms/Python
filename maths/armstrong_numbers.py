"""Armstrong Numbers."""


def is_armstrong(number: int) -> bool:
    """
    Returns True if number is an Armstrong number, False otherwise.

    >>> is_armstrong(0)
    True
    >>> is_armstrong(1)
    True
    >>> is_armstrong(153)
    True 
    >>> is_armstrong(370)
    True
    >>> is_armstrong(9474)
    True
    >>> is_armstrong(100)
    False
    >>> is_armstrong(25)
    False
    """
    if not isinstance(number, int) or number < 0:
        raise ValueError("is_armstrong() only accepts non-negative integers")

    digits = str(number)
    power = len(digits)
    return sum(int(d) ** power for d in digits) == number


def get_armstrongs_up_to(limit: int) -> list[int]:
    """
    Returns list of all Armstrong numbers up to limit.

    >>> get_armstrongs_up_to(500)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]
    """
    return [i for i in range(limit + 1) if is_armstrong(i)]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
