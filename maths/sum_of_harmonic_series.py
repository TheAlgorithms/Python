def sum_of_harmonic_progression(
    first_term: float, common_difference: float, no_of_terms: int
) -> float:

    """

    Find the sum of n terms in an harmonic progression.
    common_diff is the common difference of Arithmetic
    Progression by which the given Harmonic Progression is linked.


    """

    arithmetic_progression = [1 / first_term]
    i = 0
    first_term = 1 / first_term
    while i < no_of_terms - 1:
        first_term += common_difference
        arithmetic_progression.append(first_term)

        """
        l1 is the Arithmetic Progression linked to the given Harmonic Series
        l2 is the given Harmonic Series

        """

        i += 1
        harmonic_series = [1 / step for step in arithmetic_progression]
    return sum(harmonic_series)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(sum_of_harmonic_progression(1 / 2, 2, 2))
