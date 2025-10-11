def reverse_factorial(num: int, i: int = 1) -> int:
    """
    Return n if n! equals the given num, else return -1.

    This function finds the integer n such that n! == num using recursion.
    If no such n exists, returns -1.

    >>> reverse_factorial(120)
    5
    >>> reverse_factorial(24)
    4
    >>> reverse_factorial(150)
    -1
    >>> reverse_factorial(1)
    1
    """
    if num == 1:
        return i
    if num % i != 0:
        return -1
    return reverse_factorial(num // i, i + 1)
