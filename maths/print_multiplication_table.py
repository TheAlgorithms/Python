def multiplication_table(number: int, number_of_terms: int) -> str:
    """
    Prints the multiplication table of a given number
      till the given number of terms

    >>> print(multiplication_table(3, 5))
    3 * 1 = 3
    3 * 2 = 6
    3 * 3 = 9
    3 * 4 = 12
    3 * 5 = 15

    >>> print(multiplication_table(-4, 6))
    -4 * 1 = -4
    -4 * 2 = -8
    -4 * 3 = -12
    -4 * 4 = -16
    -4 * 5 = -20
    -4 * 6 = -24
    """
    return "\n".join(
        f"{number} * {i} = {number * i}" for i in range(1, number_of_terms + 1)
    )


if __name__ == "__main__":
    print(multiplication_table(number=5, number_of_terms=10))
