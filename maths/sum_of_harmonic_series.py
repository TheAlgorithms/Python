def sum_of_harmonic_progression(
    first_term: float, common_difference: float, number_of_terms: int
) -> float:
    """
    https://en.wikipedia.org/wiki/Harmonic_progression_(mathematics)

    Find the sum of n terms in an harmonic progression.  The calculation starts with the
    first_term and loops adding the common difference of Arithmetic Progression by which
    the given Harmonic Progression is linked.

    >>> sum_of_harmonic_progression(1 / 2, 2, 2)
    0.75
    >>> sum_of_harmonic_progression(1 / 5, 5, 5)
    0.45666666666666667
    >>> sum_of_harmonic_progression(0,2,5)
    Traceback (most recent call last):
        ...
    ValueError: first_term cannot be zero
    >>> sum_of_harmonic_progression(1/2,2,0)
    Traceback (most recent call last):
        ...
    ValueError: number_of_terms must be greater than zero
    """
    if first_term == 0:
        raise ValueError("first_term cannot be zero")
    if number_of_terms <= 0:
        raise ValueError("number_of_terms must be greater than zero")
    arithmetic_progression = [1 / first_term]
    first_term = 1 / first_term
    for _ in range(number_of_terms - 1):
        first_term += common_difference
        arithmetic_progression.append(first_term)
    harmonic_series = [1 / step for step in arithmetic_progression]
    return sum(harmonic_series)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(sum_of_harmonic_progression(1 / 2, 2, 2))
