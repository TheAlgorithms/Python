def print_butterfly(n: int) -> None:
    """
    Prints a butterfly pattern using the character '*' based on the input size.

    The butterfly pattern has a symmetrical structure with an upper and lower half.

    :param n: The size of the butterfly (side length).
    :return: None

    Example:
    >>> print_butterfly(5)
    *       *
    **     **
    ***   ***
    **** ****
    *********
    **** ****
    ***   ***
    **     **
    *       *
    """
    # Upper half of the butterfly
    for i in range(1, n + 1):
        print("*" * i, end="")
        print(" " * (2 * (n - i)), end="")
        print("*" * i)

    # Lower half of the butterfly
    for i in range(n, 0, -1):
        print("*" * i, end="")
        print(" " * (2 * (n - i)), end="")
        print("*" * i)


# Ask the user for input and print the butterfly
n = int(input("Enter the value of n: "))
print_butterfly(n)
