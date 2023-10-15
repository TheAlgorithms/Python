def integer_break(number: int) -> int:
    """
    Given a positive integer number,
    break it into the sum of at least two positive integers
    and maximize the product of those integers.

    Args:
        number (int): The positive integer to be broken.

    Returns:
        int: The maximum product of the broken positive integers.

    Examples:
        >>> integer_break(2)
        1
        >>> integer_break(10)
        36
        >>> integer_break(8)
        18
    """
    if number <= 3:
        return number - 1

    max_product: list[int] = [0] * (number + 1)
    max_product[2] = 2
    max_product[3] = 3

    for i in range(4, number + 1):
        max_product[i] = max(max_product[i - 2] * 2, max_product[i - 3] * 3)

    return max_product[number]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
