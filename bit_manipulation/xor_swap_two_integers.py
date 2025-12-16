# Information on XOR swap: https://en.wikipedia.org/wiki/Bitwise_operation#XOR

# Algorithm:
# 1. Take two integers a and b.
# 2. Apply XOR between a and b and store the result in a:
#       a = a ^ b
# 3. XOR the new value of a with b to get the original value of a and store it in b:
#       b = a ^ b
# 4. XOR the new value of a with the new value of b.
#    This gives the original value of b, which we store in a:
#       a = a ^ b
# 5. Return the swapped values (a, b).
# This method swaps two numbers without using a temporary variable.


def xor_swap(a: int, b: int) -> tuple[int, int]:
    """
    Swap two integers using bitwise XOR operation and return the swapped values.

    >>> xor_swap(5, 10)
    (10, 5)
    >>> xor_swap(0, 0)
    (0, 0)
    >>> xor_swap(-1, 1)
    (1, -1)
    >>> xor_swap(123, 456)
    (456, 123)
    """
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


if __name__ == "__main__":
    import doctest

    doctest.testmod()
