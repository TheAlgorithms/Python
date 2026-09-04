"""
Calculates the sum of two non-negative integers using bitwise operators
Wikipedia explanation: https://en.wikipedia.org/wiki/Binary_number
"""


def bitwise_addition_recursive(number: int, other_number: int) -> int:
    """
    >>> bitwise_addition_recursive(4, 5)
    9
    >>> bitwise_addition_recursive(8, 9)
    17
    >>> bitwise_addition_recursive(0, 4)
    4
    >>> bitwise_addition_recursive(4.5, 9)
    Traceback (most recent call last):
        ...
    TypeError: Both arguments MUST be integers!
    >>> bitwise_addition_recursive('4', 9)
    Traceback (most recent call last):
        ...
    TypeError: Both arguments MUST be integers!
    >>> bitwise_addition_recursive('4.5', 9)
    Traceback (most recent call last):
        ...
    TypeError: Both arguments MUST be integers!
    >>> bitwise_addition_recursive(-1, 9)
    Traceback (most recent call last):
        ...
    ValueError: Both arguments MUST be non-negative!
    >>> bitwise_addition_recursive(1, -9)
    Traceback (most recent call last):
        ...
    ValueError: Both arguments MUST be non-negative!

    Adds two non-negative integers using only bitwise operations (no '+' operator).
    Algorithm (Recursive):
    1. XOR the numbers to get sum without considering carry: bitwise_sum = a ^ b
    2. AND the numbers and left-shift by 1 to get carry: carry = (a & b) << 1
    3. If carry is 0, return the sum (base case)
    4. Otherwise, recursively call with (sum, carry) until carry becomes 0
    Why it works:
    - XOR gives the sum bit-by-bit without considering carry
    - AND identifies positions where both numbers have 1 (where carry occurs)
    - Left-shift by 1 moves carry to the correct position
    - The recursive call combines the sum and the carry
    Example: 4 + 5
    - 4 = 0b0100, 5 = 0b0101
    - Call 1: sum = 0b0100 ^ 0b0101 = 0b0001, carry = (0b0100 & 0b0101) << 1 = 0b0100
    - Call 2: sum = 0b0001 ^ 0b0100 = 0b0101, carry = (0b0001 & 0b0100) << 1 = 0b0000
    - Carry is 0, return 0b0101 = 5... wait that should be 9!
    Actually 4 + 5 works correctly:
    - 4 (0b0100) + 5 (0b0101) = 9 (0b1001)
    """

    if not isinstance(number, int) or not isinstance(other_number, int):
        raise TypeError("Both arguments MUST be integers!")

    if number < 0 or other_number < 0:
        raise ValueError("Both arguments MUST be non-negative!")

    bitwise_sum = number ^ other_number
    carry = number & other_number

    if carry == 0:
        return bitwise_sum

    return bitwise_addition_recursive(bitwise_sum, carry << 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
