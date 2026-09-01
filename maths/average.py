"""Compute average of a list of numbers."""


def average(numbers: list[float]) -> float:
    """
    Compute the arithmetic mean.

    >>> average([1, 2, 3, 4, 5])
    3.0
    >>> average([10, 20])
    15.0
    """
    if not numbers:
        raise ValueError("List is empty")
    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
