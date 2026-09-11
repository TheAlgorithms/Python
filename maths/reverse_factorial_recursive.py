def reverse_factorial_recursive(value: int, current_divisor: int = 1) -> int:
    """
    Return x such that x! == value, otherwise return -1.

    The function divides `value` by 1, 2, 3, ... recursively. If the repeated
    division reduces `value` exactly to 1, the factorial root x is
    (current_divisor - 1). If the division ever has a remainder, no integer x
    exists and the function returns -1.

    Parameters
    ----------
    value : int
        The positive integer to test (candidate factorial value).
    current_divisor : int, optional
        The current divisor used while reducing `value` (default is 1).

    Returns
    -------
    int
        The factorial root (x) if x! == value, otherwise -1.

    Examples
    --------
    >>> reverse_factorial_recursive(120)
    5
    >>> reverse_factorial_recursive(24)
    4
    >>> reverse_factorial_recursive(150)
    -1
    >>> reverse_factorial_recursive(1)
    1
    >>> reverse_factorial_recursive(2)
    2
    """
    if not isinstance(value, int):
        raise TypeError("value must be an integer")
    if not isinstance(current_divisor, int):
        raise TypeError("current_divisor must be an integer")

    if value < 1:
        raise ValueError("value must be a positive integer")

    # Special-case: initial call with value == 1 should return 1 (since 1! = 1).
    if value == 1 and current_divisor == 1:
        return 1

    # If value reduced to 1 during recursion, the factorial root is divisor - 1.
    if value == 1:
        return current_divisor - 1

    # If not divisible by the current divisor, it's not a factorial number.
    if value % current_divisor != 0:
        return -1

    return reverse_factorial_recursive(value // current_divisor, current_divisor + 1)
