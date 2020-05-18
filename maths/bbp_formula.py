def bbp_extract_pi_hex_digit(digit_position: int, precision: int = 1000) -> str:
    """
    Implement a popular pi-digit-extraction algorithm known as the 
    Bailey-Borwein-Plouffe (BBP) formula to calulate the nth hex digit of pi.
    Wikipedia page:
    https://en.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_formula
    @param digit_position: a positive integer representing the position of the digit to extract. 
    The digit immediately after the decimal point is located at position 1.
    @param precision: number of terms in the second summation to calculate.
    A higher number reduces the chance of an error but increases the runtime.
    @return: a hexadecimal digit representing the digit at the nth position
    in pi's decimal expansion.
    
    >>> bbp_extract_pi_hex_digit(-10)
    Traceback (most recent call last):
      ...
    ValueError: Please input a positive integer for the digit position
    >>> bbp_extract_pi_hex_digit(1.7)
    Traceback (most recent call last):
      ...
    ValueError: Please input a positive integer for the digit position
    >>> bbp_extract_pi_hex_digit(0)
    Traceback (most recent call last):
      ...
    ValueError: Please input a positive integer for the digit position
    >>> bbp_extract_pi_hex_digit(2, -10)
    Traceback (most recent call last):
      ...
    ValueError: Please input a nonnegative integer for the precision
    >>> bbp_extract_pi_hex_digit(2, 1.6)
    Traceback (most recent call last):
      ...
    ValueError: Please input a nonnegative integer for the precision
    >>> bbp_extract_pi_hex_digit(1)
    '2'
    >>> bbp_extract_pi_hex_digit(2)
    '4'
    >>> bbp_extract_pi_hex_digit(3)
    '3'
    >>> bbp_extract_pi_hex_digit(4)
    'f'
    >>> bbp_extract_pi_hex_digit(5)
    '6'
    >>> bbp_extract_pi_hex_digit(6)
    'a'
    >>> bbp_extract_pi_hex_digit(7)
    '8'
    >>> bbp_extract_pi_hex_digit(8)
    '8'
    >>> bbp_extract_pi_hex_digit(9)
    '8'
    >>> bbp_extract_pi_hex_digit(10)
    '5'
    >>> bbp_extract_pi_hex_digit(5, 10000)
    '6'
    """
    if (not isinstance(digit_position, int)) or (digit_position <= 0):
        raise ValueError("Digit position must be a positive integer")
    elif (not isinstance(precision, int)) or (precision < 0):
        raise ValueError("Please input a nonnegative integer for the precision")

    # compute an approximation of (16 ** (n - 1)) * pi whose fractional part is mostly accurate
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
    sum = 0.0
    for sum_index in range(digit_pos_to_extract + precision):
        denominator = 8 * sum_index + denominator_addend
        exponential_term = 0.0
        if sum_index < digit_pos_to_extract:
            # if the exponential term is an integer and we mod it by the denominator before
            # dividing, only the integer part of the sum will change; the fractional part will not
            exponential_term = pow(
                16, digit_pos_to_extract - 1 - sum_index, denominator
            )
        else:
            exponential_term = pow(16, digit_pos_to_extract - 1 - sum_index)
        sum += exponential_term / denominator
    return sum


if __name__ == "__main__":
    import doctest

    doctest.testmod()
