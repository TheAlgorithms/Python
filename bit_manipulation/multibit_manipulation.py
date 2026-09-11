"""Bit integer manipulation, both single bit and multi-bit list-like
   slicing functions ( get, set, insert, remove ) implemented with
   builtin bitwise operations.

See:
https://high-python-ext-3-algorithms.readthedocs.io/ko/latest/chapter5.html#insert-bit
https://en.wikipedia.org/wiki/Bit_manipulation#Bit_manipulation_operations
https://github.com/billbreit/BitWiseApps

All parameters must be must be int >= 0, referred to as a 'bit integer'.

 bint:int
   The bit integer to be accessed or returned as modified.

 index:int
   The offset into the bit position from right,
      0b010111 -> list [1,1,1,0,1,0]. big-endian -> little-endian
   For inserts, index is the position to the right of index,
      index 0 -> right of rightmost bit.
   For gets, sets and removes, it is the position of the bit itself.

 value:int
   Either [0,1] for single bit, or int value for multibit,
      bit_length(value) <= bitlen.

 bitlen:int
   The effective mask length, spec. leading zeros
      ( bitlen 4 value 1 -> 0001 )

The bitwise expressions may look convoluted, but basically, there are
just three parts: left-hand side, value, right-hand side.

For example, say you want to insert two ones in the middle of 0b101101,
that is ->  0b10111101. Index is 3 ( 0 ,1, 2, 3 from the right ) and the
value is 3 (0b11) with a bit length of 2.

- Shift >> index right to produce 0b101
- Shift left << bit length to produce 0b10100.
- OR in the ones producing 0b10111.
- Left shift << index producing 0b10111000.
- Using a bit mask (1 << index)-1 -> 0b111, AND with the original bint,
  ( 0b101101 & 0b111 ) -> 0b101.
- OR that into the working 0b10111000, that is, ( 0b10111000 | 0b101 )
  -> 0b10111101.

To remove the center two bits of 0b101101 -> 0b1001, the process is mostly
the same.  Index is 2 for the remove operation on the right-center bit
rather than 3 for inserting, because we are referring to the bit itself
rather the position to the right of the bit index.

- The initial right shift is index (2 ) + bit_length(2), taking out the two
  middle bits and producing 0b10.
- The left shift of index produces 0b1000.
- The original bint is ANDed with bitmask 0b11 producing 0b01 which is
  ORed with 0b1000 yielding the target 0b1001.

Bit manipulation operations can be tricky to debug.  In the insert example
above, the result of inserting 0b11 in the center ( index=3 ) or to the
right ( index=2 ) produces the same correct result despite the unintended
misspecification.  Why is it working sometimes and not others ?  Frequently,
it's the result of inserting at the wrong index, for the hundredth time !

Various bit insert/remove solutions exist using bin() string functions
and slicing, but this bitwise implementation is significantly faster
(about 3x) on Python for big ints (2^100).

See https://github.com/billbreit/BitWiseApps/blob/main/dev/time_ops.py

"""

bit_length = int.bit_length


def bit_get(bint: int, index: int) -> int:
    """Get value of bit at index in bint.

    >>> bit_get(15, 0)
    1
    >>> bit_get(15, 4)
    0
    >>> bit_get(0, 4)
    0
    >>> bit_get(-1, 2)
    Traceback (most recent call last):
        ...
    ValueError: All input values must be positive integers.
    >>> bit_get(0, -1)
    Traceback (most recent call last):
        ...
    ValueError: All input values must be positive integers.
    """

    return multibit_get(bint, index, 1)


def bit_set(bint: int, index: int, value: int = 1) -> int:
    """Set bit at index to value 1 or 0, like set() or unset().

    >>> bit_set(15, 0, 0)
    14
    >>> bit_set(15, 4, 1)
    31
    >>> bit_set(31, 6, 0)
    31
    >>> bit_set(31, 6, 3)
    Traceback (most recent call last):
        ...
    ValueError: Input value must be 1 or 0.
    """

    if value not in [0, 1]:
        raise ValueError("Input value must be 1 or 0.")

    return multibit_set(bint, index, 1, value)


def bit_insert(bint: int, index: int, value: int = 1) -> int:
    """Insert bit value before index.

    >>> bit_insert(15, 0, 0)
    30
    >>> bit_insert(15, 0, 1)
    31
    >>> bit_insert(15, 4, 1)
    31
    >>> bit_insert(31, 6, 0)
    31
    """

    if value not in [0, 1]:
        raise ValueError("Input value must be 1 or 0.")

    return multibit_insert(bint, index, 1, value)


def bit_remove(bint: int, index: int) -> int:
    """Remove the bit at index from bint.

    >>> bit_remove(15, 0)
    7
    >>> bit_remove(15, 1)
    7
    >>> bit_remove(31, 4)
    15
    >>> bit_remove(31, 6)
    31
    """

    return multibit_remove(bint, index, 1)


def multibit_get(bint: int, index: int, bit_len: int) -> int:
    """Get bit_len number of bits starting from index.
       819 = 1100110011.

    >>> multibit_get(0, 1, 1)
    0
    >>> multibit_get(15, 0, 3)
    7
    >>> multibit_get(819, 2, 4)
    12
    >>> multibit_get(819, 4, 6)
    51
    """

    if bint < 0 or index < 0 or bit_len < 0:
        raise ValueError("All input values must be positive integers.")

    return (bint >> index) & ((1 << bit_len) - 1)


def multibit_set(bint: int, index: int, bit_len: int, value: int) -> int:
    """Overlay bint at index with value for bit_len bits.

    >>> multibit_set(0, 1, 1, 0)
    0
    >>> multibit_set(15, 0, 2, 0)
    12
    >>> multibit_set(22, 0, 1, 1)
    23
    >>> multibit_set(22, 2, 1, 0)
    18
    >>> multibit_set(22, 2, 1, 3)
    Traceback (most recent call last):
        ...
    ValueError: Bit length of value can not be greater than specified bit length.
    """

    if bint < 0 or index < 0 or bit_len < 0 or value < 0:
        raise ValueError("All input values must be positive integers.")
    if bit_length(value) > bit_len:
        raise ValueError(
            "Bit length of value can not be greater than specified bit length."
        )

    return ((((bint >> (index + bit_len)) << bit_len) | value) << index) | (
        bint & (1 << index) - 1
    )


def multibit_insert(bint: int, index: int, bit_len: int, value: int) -> int:
    """Insert value before index-th slot

    >>> multibit_insert(0, 1, 1, 1)
    2
    >>> multibit_insert(15, 1, 2, 0)
    57
    >>> multibit_insert(22, 0, 1, 1)
    45
    >>> multibit_insert(22, 2, 1, 0)
    42
    >>> multibit_insert(22, 2, 0, 0)
    22
    >>> multibit_insert(22, 2, 1, 3)
    Traceback (most recent call last):
        ...
    ValueError: Bit length of value can not be greater than specified bit length.
    """

    if bint < 0 or index < 0 or bit_len < 0 or value < 0:
        raise ValueError("All input values must be positive integers.")
    if bit_length(value) > bit_len:
        raise ValueError(
            "Bit length of value can not be greater than specified bit length."
        )

    return ((((bint >> index) << bit_len) | value) << index) | bint & ((1 << index) - 1)


def multibit_remove(bint: int, index: int, bit_len: int) -> int:
    """Remove bits in bint from index to index+bit_len.

    >>> multibit_remove(3, 1, 1)
    1
    >>> multibit_remove(15, 1, 2)
    3
    >>> multibit_remove(22, 0, 1)
    11
    >>> multibit_remove(22, 2, 2)
    6
    >>> multibit_remove(22, 2, 6)
    2
    """

    if bint < 0 or index < 0 or bit_len < 0:
        raise ValueError("All input values must be positive integers.")

    return ((bint >> index + bit_len) << index) | bint & ((1 << index) - 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
