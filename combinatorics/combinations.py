from math import factorial, comb

"""
https://en.wikipedia.org/wiki/Combination
"""


def validate_elements_count(
    total_elements_count: int, selected_elements_count: int
) -> None:
    # If either of the conditions are true, the function is being asked
    # to calculate a factorial of a negative number, which is not possible
    if total_elements_count < selected_elements_count or selected_elements_count < 0:
        raise ValueError(
            "Please enter positive integers for total_elements_count and selected_elements_count where total_elements_count >= selected_elements_count"
        )


def combinations_iterative(
    total_elements_count: int, selected_elements_count: int
) -> int:
    """
    Returns the number of different combinations of selected_elements_count length which can
    be made from total_elements_count values, where total_elements_count >= selected_elements_count.

    Examples:
    >>> combinations_iterative(10,5)
    252

    >>> combinations_iterative(6,3)
    20

    >>> combinations_iterative(20,5)
    15504

    >>> combinations_iterative(52, 5)
    2598960

    >>> combinations_iterative(0, 0)
    1

    >>> combinations_iterative(-4, -5)
    Traceback (most recent call last):
    ...
    ValueError: Please enter positive integers for total_elements_count and selected_elements_count where total_elements_count >= selected_elements_count
    """
    validate_elements_count(total_elements_count, selected_elements_count)
    combinations_count = 1
    for processing_at_this_moment_elements_count in range(selected_elements_count):
        combinations_count *= (
            total_elements_count - processing_at_this_moment_elements_count
        )
        combinations_count //= processing_at_this_moment_elements_count + 1
    return combinations_count


def multiset_combinations(
    total_elements_count: int, selected_elements_count: int
) -> int:
    """
    Returns the number of different combinations of selected_elements_count length which can
    be made from total_elements_count values, where total_elements_count >= selected_elements_count.

    Examples:
    >>> multiset_combinations(10,5)
    2002

    >>> multiset_combinations(6,3)
    56

    >>> multiset_combinations(20,5)
    42504

    >>> multiset_combinations(52, 5)
    3819816

    >>> multiset_combinations(0, 0)
    Traceback (most recent call last):
    ...
    ValueError: n must be a non-negative integer

    >>> multiset_combinations(-4, -5)
    Traceback (most recent call last):
    ...
    ValueError: n must be a non-negative integer
    """

    return comb(
        total_elements_count + selected_elements_count - 1, selected_elements_count
    )


def combinations_formula(
    total_elements_count: int, selected_elements_count: int
) -> int:
    """
    Returns the number of different combinations of selected_elements_count length which can
    be made from total_elements_count values, where total_elements_count >= selected_elements_count.

    Examples:
    >>> combinations_formula(10,5)
    252

    >>> combinations_formula(6,3)
    20

    >>> combinations_formula(20,5)
    15504

    >>> combinations_formula(52, 5)
    2598960

    >>> combinations_formula(0, 0)
    1

    >>> combinations_formula(-4, -5)
    Traceback (most recent call last):
    ...
    ValueError: Please enter positive integers for total_elements_count and selected_elements_count where total_elements_count >= selected_elements_count
    """
    validate_elements_count(total_elements_count, selected_elements_count)
    remaining_elements_count = total_elements_count - selected_elements_count
    return int(
        factorial(total_elements_count)
        / (factorial(selected_elements_count) * factorial(remaining_elements_count))
    )


def combinations_with_repetitions(
    total_elements_count: int, selected_elements_count: int
) -> int:
    """
    Returns the number of different combinations of selected_elements_count length which can
    be made from total_elements_count values, where total_elements_count >= selected_elements_count.

    Examples:
    >>> combinations_with_repetitions(10,5)
    2002

    >>> combinations_with_repetitions(6,3)
    56

    >>> combinations_with_repetitions(20,5)
    42504

    >>> combinations_with_repetitions(52, 5)
    3819816

    >>> combinations_with_repetitions(0, 0)
    1

    >>> combinations_with_repetitions(-4, -5)
    Traceback (most recent call last):
    ...
    ValueError: Please enter positive integers for total_elements_count and selected_elements_count where total_elements_count >= selected_elements_count
    """
    validate_elements_count(total_elements_count, selected_elements_count)
    if total_elements_count + selected_elements_count == 0:
        return 1
    return int(
        factorial(total_elements_count + selected_elements_count - 1)
        / (factorial(selected_elements_count) * factorial(total_elements_count - 1))
    )


def permutations(total_elements_count: int, selected_elements_count: int) -> int:
    """
    https://en.wikipedia.org/wiki/Permutation

    Examples:
    >>> permutations(10,5)
    30240

    >>> permutations(6,3)
    120

    >>> permutations(20,5)
    1860480

    >>> permutations(52, 5)
    311875200

    >>> permutations(0, 0)
    1

    >>> permutations(-4, -5)
    Traceback (most recent call last):
    ...
    ValueError: Please enter positive integers for total_elements_count and selected_elements_count where total_elements_count >= selected_elements_count
    """
    validate_elements_count(total_elements_count, selected_elements_count)
    remaining_elements_count = total_elements_count - selected_elements_count
    return int(factorial(total_elements_count) / factorial(remaining_elements_count))


def possible_selections(total_elements_count: int, selected_elements_count: int) -> int:
    """
    https://en.wikipedia.org/wiki/Permutation

    Examples:
    >>> possible_selections(10,5)
    100000

    >>> possible_selections(6,3)
    216

    >>> possible_selections(20,5)
    3200000

    >>> possible_selections(52, 5)
    380204032

    >>> possible_selections(0, 0)
    1

    >>> possible_selections(-4, -5)
    Traceback (most recent call last):
    ...
    ValueError: Please enter positive integers for total_elements_count and selected_elements_count where total_elements_count >= selected_elements_count
    """
    validate_elements_count(total_elements_count, selected_elements_count)
    return int(total_elements_count**selected_elements_count)


if __name__ == "__main__":
    __import__("doctest").testmod()
