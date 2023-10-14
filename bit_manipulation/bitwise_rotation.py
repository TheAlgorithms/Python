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
    '0b0110'
    """

    if rotation_amount < 0:
        rotation_amount = len(bin(number)[2:]) - rotation_amount
    elif rotation_amount == 0:
        return bin(number)[2:]

    binary_number = bin(number)[2:]
    rotated_number = (
        binary_number[-(rotation_amount % len(binary_number)) :]
        + binary_number[: -(rotation_amount % len(binary_number))]
    )
    return "0b" + rotated_number.zfill(len(binary_number))


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

    if rotation_amount < 0:
        rotation_amount = len(bin(number)[2:]) - rotation_amount
    elif rotation_amount == 0:
        return bin(number)[2:]

    binary_number = bin(number)[2:]
    rotated_number = (
        binary_number[-rotation_amount % len(binary_number) :]
        + binary_number[: -rotation_amount % len(binary_number)]
    )

    return "0b" + rotated_number.zfill(len(binary_number))
