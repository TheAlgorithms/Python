def pell_number_iterative(subscript: int) -> int:
    """
    This function returns the `subscript`-th Pell number iteratively, where
    `subscript` is a non-negative integer. Pell numbers are defined by the
    recurrence relation:

    P_0 = 0, P_1 = 1, P_n = 2 * P_(n-1) + P_(n-2)

    https://en.wikipedia.org/wiki/Pell_number
    https://oeis.org/A000129

    >>> pell_number_iterative(0)
    0
    >>> pell_number_iterative(1)
    1
    >>> pell_number_iterative(12)
    13860
    >>> pell_number_iterative("1")
    Traceback (most recent call last):
        ...
    ValueError: The input must be an integer.
    >>> pell_number_iterative(-1)
    Traceback (most recent call last):
        ...
    ValueError: The input number must be non-negative.
    """
    if not isinstance(subscript, int):
        raise ValueError("The input must be an integer.")

    if subscript < 0:
        raise ValueError("The input number must be non-negative.")

    if subscript in (0, 1):
        return subscript

    prev_prev_num = 0
    prev_num = 1

    for _ in range(2, subscript + 1):
        temp = 2 * prev_num + prev_prev_num
        prev_prev_num = prev_num
        prev_num = temp

    return prev_num


def pell_number_recursive(subscript: int) -> int:
    """
    This function calculates the `subscript`-th Pell number recursively. Due to
    its recursive nature, this function grows exponentially with `subscript`.
    For large values of `subscript`, use pell_number_iterative instead.

    >>> pell_number_recursive(0)
    0
    >>> pell_number_recursive(1)
    1
    >>> pell_number_recursive(12)
    13860
    >>> pell_number_recursive("1")
    Traceback (most recent call last):
        ...
    ValueError: The input must be an integer.
    >>> pell_number_recursive(-1)
    Traceback (most recent call last):
        ...
    ValueError: The input number must be non-negative.
    """
    if not isinstance(subscript, int):
        raise ValueError("The input must be an integer.")

    if subscript < 0:
        raise ValueError("The input number must be non-negative.")

    if subscript in (0, 1):
        return subscript

    return 2 * pell_number_recursive(subscript - 1) + pell_number_recursive(
        subscript - 2
    )
