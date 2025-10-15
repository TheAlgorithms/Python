"""
Swap two bits at given positions in a non-negative integer using bitwise operators.

Wikipedia reference:
https://en.wikipedia.org/wiki/Bit_manipulation
"""


def swap_bits(number: int, i: int, j: int) -> int:
    """
    Swap the bits at the position i and j (0-indexed from right side)

    Arguments:
            number (int): Non-negative integer whose bits are to be swapped.
            i (int): Index of 1st bit to swap.
            j (int): Index of 2nd bit to swap.

    Returns:
            int: Integer obtained after swapping of bits.

    Raises:
            TypeError: If argument is not an Integer
            ValueError: Invalid argument or bit positions.

    Examples:
            >>> swap_bits(28, 0, 2)   # 11100 -> swap rightmost bits 0 and 2
            25
            >>> swap_bits(15, 1, 2)   # 1111 -> swapping the bits 1 and 2
            15
            >>> swap_bits(10, 0, 3)   # 1010 -> swap the bits 0 and 3
            3
            >>> swap_bits(10.5, 0, 3)
            Traceback (most recent call last):
                ...
            TypeError: All arguments MUST be integers!
            >>> swap_bits(-5, 1, 3)
            Traceback (most recent call last):
                ...
            ValueError: The number MUST be non-negative!
            >>> swap_bits(10, -1, 2)
            Traceback (most recent call last):
                ...
            ValueError: Bit positions MUST be non-negative!
            """
    if not all(isinstance(x, int) for x in (number, i, j)):
        raise TypeError("All arguments MUST be integers!")

    if number < 0:
        raise ValueError("The number MUST be non-negative!")

    if i < 0 or j < 0:
        raise ValueError("Bit positions MUST be non-negative!")

    # Extraction of Bits
    bit_first = (number >> i) & 1
    bit_second = (number >> j) & 1

    # If bits differ swap them
    if bit_first != bit_second:
        number ^= (1 << i) | (1 << j)

    return number


if __name__ == "__main__":
    import doctest

    doctest.testmod()
