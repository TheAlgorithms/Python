def print_multiplication_table(number: int, number_of_terms: int) -> None:
    """
    Prints the multiplication table of a given number till the given number of terms
    >>> print_multiplication_table(3,5)
    3 * 1 = 3
    3 * 2 = 6
    3 * 3 = 9
    3 * 4 = 12
    3 * 5 = 15

    >>> print_multiplication_table(-4,6)
    -4 * 1 = -4
    -4 * 2 = -8
    -4 * 3 = -12
    -4 * 4 = -16
    -4 * 5 = -20
    -4 * 6 = -24
    """
    for i in range(1, number_of_terms + 1):
        print(f"{number} * {i} = " + str(number * i))


if __name__ == "__main__":
    number = 5
    number_of_terms = 10
    print_multiplication_table(number, number_of_terms)
