"""
Check whether a given number is an Armstrong number.
An Armstrong number (also known as narcissictic number) is a number that is equal
to the sum of its own digits, each raised to the power of the number of digits.

153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153
8208 is an Armstrong number because 8^4 + 2^4 + 0^4 + 8^4 = 8208

https://en.wikipedia.org/wiki/Narcissistic_number
"""
def is_armstrong(num: int) -> bool:
    """
    >>> is_armstrong(-1)
    False
    >>> is_armstrong(0)
    True
    >>> is_armstrong(5)
    True
    >>> is_armstrong(153)
    True
    >>> is_armstrong(8207)
    True
    >>> is_armstrong(24364)
    False
    """
    num_str = str(num)
    num_digits = len(num_str)
    sum_of_powers = 0
    for digit_char in num_str:
        digit = int(digit_char)
        sum_of_powers += digit ** num_digits
    
    return num == sum_of_powers


if __name__ == "__main__":
    import doctest

    doctest.testmod()
