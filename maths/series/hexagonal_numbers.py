"""
A hexagonal number sequence is a sequence of figurate numbers
where the nth hexagonal number hₙ is the number of distinct dots
in a pattern of dots consisting of the outlines of regular
hexagons with sides up to n dots, when the hexagons are overlaid
so that they share one vertex.

    Calculates the hexagonal numbers sequence with a formula
        hₙ = n(2n-1)
        where:
        hₙ --> is nth element of the sequence
        n --> is the number of element in the sequence
        reference-->"Hexagonal number" Wikipedia
        <https://en.wikipedia.org/wiki/Hexagonal_number>
"""


def hexagonal_numbers(length: int) -> list[int]:
    """
    :param len: max number of elements
    :type len: int
    :return: Hexagonal numbers as a list

    Tests:
    >>> hexagonal_numbers(10)
    [0, 1, 6, 15, 28, 45, 66, 91, 120, 153]
    >>> hexagonal_numbers(5)
    [0, 1, 6, 15, 28]
    """

    if length <= 0:
        raise ValueError("Length must be a positive number.")
    return [n * (2 * n - 1) for n in range(length)]


if __name__ == "__main__":
    print(hexagonal_numbers(length=5))
    print(hexagonal_numbers(length=10))
