def eval_key(code: int) -> int:
    """
    Returns the last digit of barcode by excluding the last digit first
    and then computing to reach the actual last digit from the remaining
    12 digits.

    >>> eval_key(8718452538119)
    9
    """

    code //= 10  # exclude the last digit
    checker = False
    s = 0

    # extract and check each digit
    while code != 0:
        mult = 1 if checker else 3
        s += mult * (code % 10)
        code //= 10
        checker = not checker

    return (10 - (s % 10)) % 10


def is_valid(code: int) -> bool:
    """
    Checks for length of barcode and last-digit
    Returns boolean value of validity of barcode

    >>> is_valid(8718452538119)
    True

    >>> is_valid(87184525)
    False

    """

    return len(str(code)) == 13 and eval_key(code) == code % 10


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    """
    Enter a barcode.
    Displays whether the entered barcode is valid or invalid.
    """
    barcode = input("Enter a barcode: ")
    number_barcode = int(barcode)
    if is_valid(number_barcode):
        print(f"|{number_barcode}| is a valid Barcode")
    else:
        print(f"|{number_barcode}| is NOT is valid Barcode.")
