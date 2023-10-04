def decimal_to_base_minus_2(decimal_number: int) -> str:
    """
    Convert a decimal number to base -2.
    Args:
        decimal_number (int): The decimal number to be converted.
    Returns:
        str: The converted number in base -2.
    Examples:
        >>> decimal_to_base_minus_2(13)
        '1101'
        >>> decimal_to_base_minus_2(0)
        '0'
        >>> decimal_to_base_minus_2(-10)
        '110'
    """
    if decimal_number == 0:
        return "0"

    result = ""

    while decimal_number != 0:
        remainder = decimal_number % (-2)
        decimal_number = -(decimal_number // (-2))

        if remainder < 0:
            remainder += 2
            decimal_number += 1

        result = str(remainder) + result

    return result
