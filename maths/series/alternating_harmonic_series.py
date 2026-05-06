"""Alternating Harmonic Series Checker"""


def is_alternate_harmonic_series(series: list) -> bool:
    """
    Returns True if the given series is an Alternating Harmonic Series.

    Examples:
    >>> is_alternate_harmonic_series([1, -1/2, 1/3, -1/4])
    True

    >>> is_alternate_harmonic_series([1, 1/2, 1/3])
    False

    >>> is_alternate_harmonic_series([])
    False
    """

    if not series:
        return False

    for i, value in enumerate(series):
        expected = ((-1) ** i) * (1 / (i + 1))

        if abs(value - expected) > 1e-9:
            return False

    return True


if __name__ == "__main__":
    sample = [1, -1 / 2, 1 / 3, -1 / 4]
    print(is_alternate_harmonic_series(sample))