def get_reverse_bit_string(number: int) -> str:
    """
    Return the reverse bit string of a 32 bit integer.
    Reverses all 32 bits of an integer by extracting each bit from right to left
    (using modulo and right shift) and building a new string from left to right.
    Algorithm:
    1. Initialize an empty bit_string
    2. Loop 32 times (for a 32-bit integer):
       - Extract the rightmost bit using (number % 2)
       - Append this bit to the string
       - Right shift the number by 1 (number >>= 1)
    3. Return the reversed bit string
    Example: For 9 (binary: 00000000000000000000000000001001)
    Extracting from right to left: 1, 0, 0, 1, 0, 0, 0, ... (30 more zeros)
    Result: 10010000000000000000000000000000
    >>> get_reverse_bit_string(9)
    '10010000000000000000000000000000'
    >>> get_reverse_bit_string(43)
    '11010100000000000000000000000000'
    >>> get_reverse_bit_string(2873)
    '10011100110100000000000000000000'
    >>> get_reverse_bit_string(2550136832)
    '00000000000000000000000000011001'
    >>> get_reverse_bit_string("this is not a number")
    Traceback (most recent call last):
        ...
    TypeError: operation can not be conducted on an object of type str
    """
    if not isinstance(number, int):
        msg = (
            "operation can not be conducted on an object of type "
            f"{type(number).__name__}"
        )
        raise TypeError(msg)
    bit_string = ""
    for _ in range(32):
        bit_string += str(number % 2)
        number >>= 1
    return bit_string


def reverse_bit(number: int) -> int:
    """
    Take in a 32 bit integer, reverse its bits, return a 32 bit integer result.

    This function reverses the bit sequence of a 32-bit unsigned integer by
    iteratively extracting bits from the right (LSB - Least Significant Bit)
    and building a new number with those bits placed on the left.

    Algorithm:
    1. Initialize result = 0
    2. Loop 32 times (for a 32-bit integer):
       - Left shift result by 1 (result <<= 1) to make room for the next bit
       - Extract the rightmost bit of number using AND with 1 (end_bit = number & 1)
       - Right shift number by 1 (number >>= 1) to process the next bit
       - Add the extracted bit to result using OR (result |= end_bit)
    3. Return the result

    Bit operations explained:
    - << (left shift): Multiplies by 2 and makes space for new bits on the right
    - & (AND): Extracts specific bits (number & 1 gets the rightmost bit)
    - >> (right shift): Divides by 2, discarding the rightmost bit
    - |= (OR assignment): Sets bits in the result

    Example: For 25 (binary: 00000000000000000000000000011001)
    Bit reversal process:
    Original:  00000000000000000000000000011001
    Reversed:  10011000000000000000000000000000 (2550136832 in decimal)

    >>> reverse_bit(25)
    2550136832
    >>> reverse_bit(37)
    2751463424
    >>> reverse_bit(21)
    2818572288
    >>> reverse_bit(58)
    1543503872
    >>> reverse_bit(0)
    0
    >>> reverse_bit(256)
    8388608
    >>> reverse_bit(2550136832)
    25
    >>> reverse_bit(-1)
    Traceback (most recent call last):
        ...
    ValueError: The value of input must be non-negative

    >>> reverse_bit(1.1)
    Traceback (most recent call last):
        ...
    TypeError: Input value must be an 'int' type

    >>> reverse_bit("0")
    Traceback (most recent call last):
        ...
    TypeError: Input value must be an 'int' type
    """
    if not isinstance(number, int):
        raise TypeError("Input value must be an 'int' type")
    if number < 0:
        raise ValueError("The value of input must be non-negative")

    result = 0
    # iterator over [0 to 31], since we are dealing with a 32 bit integer
    for _ in range(32):
        # left shift the bits by unity
        result <<= 1
        # get the end bit
        end_bit = number & 1
        # right shift the bits by unity
        number >>= 1
        # add that bit to our answer
        result |= end_bit
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
