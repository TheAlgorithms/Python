def decimal_to_fraction(decimal: float | str) -> tuple[int, int]:
    """
    Return a decimal number in its simplest fraction form
    >>> decimal_to_fraction(2)
    (2, 1)
    >>> decimal_to_fraction(89.)
    (89, 1)
    >>> decimal_to_fraction("67")
    (67, 1)
    >>> decimal_to_fraction("45.0")
    (45, 1)
    >>> decimal_to_fraction(1.5)
    (3, 2)
    >>> decimal_to_fraction("6.25")
    (25, 4)
    >>> decimal_to_fraction("78td")
    Traceback (most recent call last):
    ValueError: Please enter a valid number
    """
    try:
        decimal = float(decimal)
    except ValueError:
        raise ValueError("Please enter a valid number")
    fractional_part = decimal - int(decimal)
    if fractional_part == 0:
        return int(decimal), 1
    else:
        number_of_frac_digits = len(str(decimal).split(".")[1])
        numerator = int(decimal * (10**number_of_frac_digits))
        denominator = 10**number_of_frac_digits
        divisor, dividend = denominator, numerator
        while True:
            remainder = dividend % divisor
            if remainder == 0:
                break
            dividend, divisor = divisor, remainder
        numerator, denominator = numerator / divisor, denominator / divisor
        return int(numerator), int(denominator)


if __name__ == "__main__":
    print(f"{decimal_to_fraction(2) = }")
    print(f"{decimal_to_fraction(89.0) = }")
    print(f"{decimal_to_fraction('67') = }")
    print(f"{decimal_to_fraction('45.0') = }")
    print(f"{decimal_to_fraction(1.5) = }")
    print(f"{decimal_to_fraction('6.25') = }")
    print(f"{decimal_to_fraction('78td') = }")
