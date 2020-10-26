"""
    Project Euler Problem 57: https://projecteuler.net/problem=57
    The square root of two can be expressed as an infinite continued fraction.

    In the first one-thousand expansions,
    how many fractions contain a numerator with more digits than the denominator?

    Working principle:
    The first expansion is (1 + 1/2)
    The successive is 1 + 1/(2 + 1/2)

    Expansion 1 has numerator = 1, denominator = 2
    1 + numerator/denominator = (numerator + denominator)/(denominator)
    Once the new numerator and denominator are computed,
    a counter is increased if the numerator has more digits than the denominator

    Note that the denominator of the fractional part
    can be attained as the previous expansion + 1
    => 1/(last_expansion + 1)
    The numerator and denominator of the fractional part of the expansion are computed
    and the process is repeated up to the 1000-th expansion
"""


def solution(max_expansions: int = 1000, first_den: int = 2) -> int:
    """Return the number of numerators
    with more digits than denominators
    in the expansion of sqrt(2)

    >>> solution()
    153
    """

    # Initialize the iteration counter
    iteration = 0

    """ initialize the variables that will store
        the numerator and denominator at every step
    """
    numerator = 1
    denominator = first_den

    # This variable will be used temporarily to switch numerators and denominators
    temp_switcher = 0

    """ A variable to count the instances of fractions
        with numerators with more digits than the denominator
    """
    longer_numerators_counter = 0

    while iteration < max_expansions:

        # compute the new numerator for the i-th expansion
        numerator += denominator

        # if the new numerator is longer then the denominator and update the counter
        longer_numerators_counter += len(str(numerator)) > len(str(denominator))

        # Add one to compute the updated numerator of the fractional part
        numerator += denominator

        # compute the fraction reciprocal
        temp_switcher = numerator
        numerator = denominator
        denominator = temp_switcher

        # the numerator and denominator are updated for the next expansion:
        iteration += 1
    return longer_numerators_counter


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(f"{solution()}")
