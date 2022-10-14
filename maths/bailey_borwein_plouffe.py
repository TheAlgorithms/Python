def bailey_borwein_plouffe(digit_position: int, precision: int = 1000) -> str:
    """
    Implement a popular pi-digit-extraction algorithm known as the
    Bailey-Borwein-Plouffe (BBP) formula to calculate the nth hex digit of pi.
    Wikipedia page:
    https://en.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_formula
    @param digit_position: a positive integer representing the position of the digit to
    extract.
    The digit immediately after the decimal point is located at position 1.
    @param precision: number of terms in the second summation to calculate.
    A higher number reduces the chance of an error but increases the runtime.
    @return: a hexadecimal digit representing the digit at the nth position
    in pi's decimal expansion.

    >>> "".join(bailey_borwein_plouffe(i) for i in range(1, 11))
    '243f6a8885'
    >>> bailey_borwein_plouffe(5, 10000)
    '6'
    >>> bailey_borwein_plouffe(-10)
    Traceback (most recent call last):
      ...
    ValueError: Digit position must be a positive integer
    >>> bailey_borwein_plouffe(0)
    Traceback (most recent call last):
      ...
    ValueError: Digit position must be a positive integer
    >>> bailey_borwein_plouffe(1.7)
    Traceback (most recent call last):
      ...
    ValueError: Digit position must be a positive integer
    >>> bailey_borwein_plouffe(2, -10)
    Traceback (most recent call last):
      ...
    ValueError: Precision must be a nonnegative integer
    >>> bailey_borwein_plouffe(2, 1.6)
    Traceback (most recent call last):
      ...
    ValueError: Precision must be a nonnegative integer
    """
    if (not isinstance(digit_position, int)) or (digit_position <= 0):
        raise ValueError("Digit position must be a positive integer")
    elif (not isinstance(precision, int)) or (precision < 0):
        raise ValueError("Precision must be a nonnegative integer")

    # compute an approximation of (16 ** (n - 1)) * pi whose fractional part is mostly
    # accurate
    sum_result = (
        4 * _subsum(digit_position, 1, precision)
        - 2 * _subsum(digit_position, 4, precision)
        - _subsum(digit_position, 5, precision)
        - _subsum(digit_position, 6, precision)
    )

    # return the first hex digit of the fractional part of the result
    return hex(int((sum_result % 1) * 16))[2:]


def _subsum(
    digit_pos_to_extract: int, denominator_addend: int, precision: int
) -> float:
    # only care about first digit of fractional part; don't need decimal
    """
    Private helper function to implement the summation
    functionality.
    @param digit_pos_to_extract: digit position to extract
    @param denominator_addend: added to denominator of fractions in the formula
    @param precision: same as precision in main function
    @return: floating-point number whose integer part is not important
    """
    total = 0.0
    for sum_index in range(digit_pos_to_extract + precision):
        denominator = 8 * sum_index + denominator_addend
        if sum_index < digit_pos_to_extract:
            # if the exponential term is an integer and we mod it by the denominator
            # before dividing, only the integer part of the sum will change;
            # the fractional part will not
            exponential_term = pow(
                16, digit_pos_to_extract - 1 - sum_index, denominator
            )
        else:
            exponential_term = pow(16, digit_pos_to_extract - 1 - sum_index)
        total += exponential_term / denominator
    return total


if __name__ == "__main__":
    import doctest

    doctest.testmod()
