""" Luhn Algorithm """
from typing import List


def is_luhn(string: str) -> bool:
    """
    Perform Luhn validation on input string
    Algorithm:
    * Double every other digit starting from 2nd last digit.
    * Subtract 9 if number is greater than 9.
    * Sum the numbers
    *
    >>> test_cases = [79927398710, 79927398711, 79927398712, 79927398713,
    ...     79927398714, 79927398715, 79927398716, 79927398717, 79927398718,
    ...     79927398719]
    >>> test_cases = list(map(str, test_cases))
    >>> list(map(is_luhn, test_cases))
    [False, False, False, True, False, False, False, False, False, False]
    """
    check_digit: int
    _vector: List[str] = list(string)
    __vector, check_digit = _vector[:-1], int(_vector[-1])
    vector: List[int] = [*map(int, __vector)]

    vector.reverse()
    for idx, i in enumerate(vector):

        if idx & 1 == 0:
            doubled: int = vector[idx] * 2
            if doubled > 9:
                doubled -= 9

            check_digit += doubled
        else:
            check_digit += i

    if (check_digit) % 10 == 0:
        return True
    return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    assert is_luhn("79927398713")
