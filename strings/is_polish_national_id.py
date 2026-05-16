def is_polish_national_id(input_str: str) -> bool:
    """
    Verification of the correctness of the PESEL number.
    www-gov-pl.translate.goog/web/gov/czym-jest-numer-pesel?_x_tr_sl=auto&_x_tr_tl=en

    PESEL can start with 0, that's why we take str as input,
    but convert it to int for some calculations.


    >>> is_polish_national_id(123)
    Traceback (most recent call last):
        ...
    ValueError: Expected str as input, found <class 'int'>

    >>> is_polish_national_id("abc")
    Traceback (most recent call last):
        ...
    ValueError: Expected number as input

    >>> is_polish_national_id("02070803628") # correct PESEL
    True

    >>> is_polish_national_id("02150803629") # wrong month
    False

    >>> is_polish_national_id("02075503622") # wrong day
    False

    >>> is_polish_national_id("-99012212349") # wrong range
    False

    >>> is_polish_national_id("990122123499999") # wrong range
    False

    >>> is_polish_national_id("02070803621") # wrong checksum
    False
    """

    # check for invalid input type
    if not isinstance(input_str, str):
        msg = f"Expected str as input, found {type(input_str)}"
        raise ValueError(msg)

    # check if input can be converted to int
    try:
        input_int = int(input_str)
    except ValueError:
        msg = "Expected number as input"
        raise ValueError(msg)

    # check number range
    if not 10100000 <= input_int <= 99923199999:
        return False

    # check month correctness
    month = int(input_str[2:4])

    if (
        month not in range(1, 13)  # year 1900-1999
        and month not in range(21, 33)  # 2000-2099
        and month not in range(41, 53)  # 2100-2199
        and month not in range(61, 73)  # 2200-2299
        and month not in range(81, 93)  # 1800-1899
    ):
        return False

    # check day correctness
    day = int(input_str[4:6])

    if day not in range(1, 32):
        return False

    # check the checksum
    multipliers = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    subtotal = 0

    digits_to_check = str(input_str)[:-1]  # cut off the checksum

    for index, digit in enumerate(digits_to_check):
        # Multiply corresponding digits and multipliers.
        # In case of a double-digit result, add only the last digit.
        subtotal += (int(digit) * multipliers[index]) % 10

    checksum = 10 - subtotal % 10

    return checksum == input_int % 10


if __name__ == "__main__":
    from doctest import testmod

    testmod()
