def convert_to_minus_2_base(number):
    """
    >>> convert_to_minus_2_base(5)
    '11'
    >>> convert_to_minus_2_base(20)
    '1100'
    >>> convert_to_minus_2_base(44)
    '10100'
    >>> convert_to_minus_2_base(-5)
    '-11'
    >>> convert_to_minus_2_base(0)
    '0'

    """

    if number == 0:
        return "0"

    # Step 1: Convert to binary
    binary_representation = bin(abs(number))[2:]

    # Step 2: Negate the bits
    negated_binary = "".join(
        ["0" if bit == "1" else "1" for bit in binary_representation]
    )

    # Step 3: Add 1 to the negated binary
    result = bin(int(negated_binary, 2) + 1)[2:]

    if number < 0:
        result = "-" + result

    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod
