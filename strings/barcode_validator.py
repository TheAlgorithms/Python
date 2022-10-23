"""
https://en.wikipedia.org/wiki/Check_digit#Algorithms
"""


def get_check_digit(barcode: int) -> int:
    """
    Returns the last digit of barcode by excluding the last digit first
    and then computing to reach the actual last digit from the remaining
    12 digits.

    >>> get_check_digit(8718452538119)
    9
    >>> get_check_digit(87184523)
    5
    >>> get_check_digit(87193425381086)
    9
    >>> [get_check_digit(x) for x in range(0, 100, 10)]
    [0, 7, 4, 1, 8, 5, 2, 9, 6, 3]
    """
    barcode //= 10  # exclude the last digit
    checker = False
    s = 0

    # extract and check each digit
    while barcode != 0:
        mult = 1 if checker else 3
        s += mult * (barcode % 10)
        barcode //= 10
        checker = not checker

    return (10 - (s % 10)) % 10


def is_valid(barcode: int) -> bool:
    """
    Checks for length of barcode and last-digit
    Returns boolean value of validity of barcode

    >>> is_valid(8718452538119)
    True
    >>> is_valid(87184525)
    False
    >>> is_valid(87193425381089)
    False
    >>> is_valid(0)
    False
    >>> is_valid(dwefgiweuf)
    Traceback (most recent call last):
    ...
    NameError: name 'dwefgiweuf' is not defined
    """
    return len(str(barcode)) == 13 and get_check_digit(barcode) == barcode % 10


def get_barcode(barcode: str) -> int:
    """
    Returns the barcode as an integer

    >>> get_barcode("8718452538119")
    8718452538119
    >>> get_barcode("dwefgiweuf")
    Traceback (most recent call last):
    ...
    ValueError: Barcode 'dwefgiweuf' has alphabetic characters.
    """
    if str(barcode).isalpha():
        raise ValueError(f"Barcode '{barcode}' has alphabetic characters.")
    elif int(barcode) < 0:
        raise ValueError("The entered barcode has a negative value. Try again.")
    else:
        return int(barcode)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    """
    Enter a barcode.

    """
    barcode = get_barcode(input("Barcode: ").strip())

    if is_valid(barcode):
        print(f"'{barcode}' is a valid Barcode")
    else:
        print(f"'{barcode}' is NOT is valid Barcode.")
