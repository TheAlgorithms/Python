def logical_left_rotation(number: int, rotation_amount: int) -> str:
    """
    Take in 2 positive integers.
    'number' is the integer to be logically left rotated 'rotation_amount' times.
    Return the rotated binary representation.

    >>> logical_left_rotation(0b1100, 1)
    '0b1001'
    >>> logical_left_rotation(0b1100, 2)
    '0b0110'
    >>> logical_left_rotation(0b1010, 3)
    '0b0101'
    >>> logical_left_rotation(0b1100, 4)
    '0b1100'
    >>> logical_left_rotation(0b1010, 1)
    '0b0101'
    >>> logical_left_rotation(0b1100, -1)
    '0b0011'
    """

    binary_number = bin(number)[2:]
    length = len(binary_number)

    if rotation_amount < 0:
        rotation_amount = -rotation_amount % length
    elif rotation_amount == 0:
        return "0b" + binary_number

    rotated_number = binary_number[rotation_amount:] + binary_number[:rotation_amount]
    return "0b" + rotated_number.zfill(length)



def logical_right_rotation(number: int, rotation_amount: int) -> str:
    """
    Take in 2 positive integers.
    'number' is the integer to be logically right rotated 'rotation_amount' times.
    Return the rotated binary representation.

    >>> logical_right_rotation(0b1100, 1)
    '0b0110'
    >>> logical_right_rotation(0b1100, 2)
    '0b0011'
    >>> logical_right_rotation(0b1010, 3)
    '0b0101'
    >>> logical_right_rotation(0b1100, 4)
    '0b1100'
    >>> logical_right_rotation(0b1010, 1)
    '0b0101'
    >>> logical_right_rotation(0b1100, -1)
    '0b1001'
    """

    binary_number = bin(number)[2:]
    length = len(binary_number)

    if rotation_amount < 0:
        rotation_amount = -rotation_amount % length
    elif rotation_amount == 0:
        return "0b" + binary_number

    rotated_number = binary_number[-rotation_amount:] + binary_number[:-rotation_amount]

    return "0b" + rotated_number.zfill(length)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
