from math import log2


def binary_count_trailing_zeros(a: int) -> int:
    """
    Take in 1 integer, return a number that is
    the number of trailing zeros in binary representation of that number.

    >>> binary_count_trailing_zeros(25)
    0
    >>> binary_count_trailing_zeros(36)
    2
    >>> binary_count_trailing_zeros(16)
    4
    >>> binary_count_trailing_zeros(58)
    1
    >>> binary_count_trailing_zeros(4294967296)
    32
    >>> binary_count_trailing_zeros(0)
    0
    >>> binary_count_trailing_zeros(-10)
    Traceback (most recent call last):
        ...
    ValueError: Input value must be a positive integer
    >>> binary_count_trailing_zeros(0.8)
    Traceback (most recent call last):
        ...
    TypeError: Input value must be a 'int' type
    >>> binary_count_trailing_zeros("0")
    Traceback (most recent call last):
        ...
    TypeError: '<' not supported between instances of 'str' and 'int'
    """
    if a < 0:
        raise ValueError("Input value must be a positive integer")
    elif isinstance(a, float):
        raise TypeError("Input value must be a 'int' type")
    return 0 if (a == 0) else int(log2(a & -a))


if __name__ == "__main__":
    import doctest

    doctest.testmod()


# counting number of 0s and 1s in a binary number
def count_zeros_and_ones(binary_number):
    # Convert the binary number to a string if it's not already
    binary_str = str(binary_number)

    count_zeros = binary_str.count("0")
    count_ones = binary_str.count("1")

    return count_zeros, count_ones


# Example usage
binary_number = 1011001
zeros, ones = count_zeros_and_ones(binary_number)
print(f"Number of 0s: {zeros}, Number of 1s: {ones}")
