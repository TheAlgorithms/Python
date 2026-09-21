def show_bits(before: int, after: int) -> str:
    """
    >>> print(show_bits(0, 0xFFFF))
        0: 00000000
    65535: 1111111111111111
    """
    return f"{before:>5}: {before:08b}\n{after:>5}: {after:08b}"


def swap_odd_even_bits(num: int) -> int:
    """
    1. We use bitwise AND operations to separate the even bits (0, 2, 4, 6, etc.) and
       odd bits (1, 3, 5, 7, etc.) in the input number.
    2. We then right-shift the even bits by 1 position and left-shift the odd bits by
       1 position to swap them.
    3. Finally, we combine the swapped even and odd bits using a bitwise OR operation
       to obtain the final result.
    >>> print(show_bits(0, swap_odd_even_bits(0)))
        0: 00000000
        0: 00000000
    >>> print(show_bits(1, swap_odd_even_bits(1)))
        1: 00000001
        2: 00000010
    >>> print(show_bits(2, swap_odd_even_bits(2)))
        2: 00000010
        1: 00000001
    >>> print(show_bits(3, swap_odd_even_bits(3)))
        3: 00000011
        3: 00000011
    >>> print(show_bits(4, swap_odd_even_bits(4)))
        4: 00000100
        8: 00001000
    >>> print(show_bits(5, swap_odd_even_bits(5)))
        5: 00000101
       10: 00001010
    >>> print(show_bits(6, swap_odd_even_bits(6)))
        6: 00000110
        9: 00001001
    >>> print(show_bits(23, swap_odd_even_bits(23)))
       23: 00010111
       43: 00101011
    """
    # Get all even bits - 0xAAAAAAAA is a 32-bit number with all even bits set to 1
    even_bits = num & 0xAAAAAAAA

    # Get all odd bits - 0x55555555 is a 32-bit number with all odd bits set to 1
    odd_bits = num & 0x55555555

    # Right shift even bits and left shift odd bits and swap them
    return even_bits >> 1 | odd_bits << 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    for i in (-1, 0, 1, 2, 3, 4, 23, 24):
        print(show_bits(i, swap_odd_even_bits(i)), "\n")
