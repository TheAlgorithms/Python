from math import factorial

"""
https://en.wikipedia.org/wiki/Derangement
"""


def derangement(elements_count: int) -> int:
    """
    Returns the number of different combinations of selected_elements_count length which can
    be made from total_elements_count values, where total_elements_count >= selected_elements_count.

    Examples:
    >>> derangement(6)
    265
    >>> derangement(7)
    1854
    >>> derangement(8)
    14833

    >>> derangement(-5)
    Traceback (most recent call last):
    ...
    ValueError: Please enter positive integers for elements_count
    """
    if elements_count < 0:
        raise ValueError("Please enter positive integers for elements_count")

    derangement = sum([((-1) ** i) / factorial(i) for i in range(elements_count + 1)])
    return int(factorial(elements_count) * derangement)


if __name__ == "__main__":
    __import__("doctest").testmod()
