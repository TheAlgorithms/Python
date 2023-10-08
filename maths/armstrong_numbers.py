"""
An Armstrong number is equal to the sum of its own digits each raised to the
power of the number of digits.

For example, 370 is an Armstrong number because 3*3*3 + 7*7*7 + 0*0*0 = 370.

Armstrong numbers are also called Narcissistic numbers and Pluperfect numbers.

On-Line Encyclopedia of Integer Sequences entry: https://oeis.org/A005188
"""
PASSING = (1, 153, 370, 371, 1634, 24678051, 115132219018763992565095597973971522401)
FAILING: tuple = (-153, -1, 0, 1.2, 200, "A", [], {}, None)


def armstrong_number(n: int) -> bool:
    """
    Return True if n is an Armstrong number or False if it is not.
    """
    if not isinstance(n, int) or n < 1:
        return False

    num_str = str(n)
    num_digits = len(num_str)
    total = sum(int(digit) ** num_digits for digit in num_str)
    return n == total


def pluperfect_number(n: int) -> bool:
    """Return True if n is a pluperfect number or False if it is not."""
    if not isinstance(n, int) or n < 1:
        return False

    num_str = str(n)
    num_digits = len(num_str)
    digit_histogram = [0] * 10

    for digit in num_str:
        digit_histogram[int(digit)] += 1

    total = sum(cnt * (i**num_digits) for i, cnt in enumerate(digit_histogram))
    return n == total


def narcissistic_number(n: int) -> bool:
    """Return True if n is a narcissistic number or False if it is not."""
    if not isinstance(n, int) or n < 1:
        return False

    num_str = str(n)
    expo = len(num_str)
    total = sum(int(digit) ** expo for digit in num_str)
    return n == total


def main():
    """
    Request that user input an integer and tell them if it is an Armstrong number.
    """
    num = int(input("Enter an integer to see if it is an Armstrong number: ").strip())
    print(f"{num} is {'' if armstrong_number(num) else 'not '}an Armstrong number.")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
