from __future__ import annotations


def harmonic_mean(numbers: list[int | float]) -> float:
    """
    Return the harmonic mean of a sequence of numbers.

    Reference: https://en.wikipedia.org/wiki/Harmonic_mean

    >>> harmonic_mean([1, 2, 4])
    1.7142857142857142
    >>> harmonic_mean([2, 2, 2])
    2.0
    >>> harmonic_mean([])
    Traceback (most recent call last):
    ...
    ValueError: harmonic_mean() arg is an empty sequence
    >>> harmonic_mean([1, 0, 2])
    Traceback (most recent call last):
    ...
    ValueError: harmonic mean is undefined for zero values
    """
    if not numbers:
        raise ValueError("harmonic_mean() arg is an empty sequence")

    if any(number == 0 for number in numbers):
        raise ValueError("harmonic mean is undefined for zero values")

    return len(numbers) / sum(1 / number for number in numbers)


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
