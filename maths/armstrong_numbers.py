"""
An Armstrong number is equal to the sum of the cubes of its digits.
For example, 370 is an Armstrong number because 3*3*3 + 7*7*7 + 0*0*0 = 370.
An Armstrong number is often called Narcissistic number.
"""


def armstrong_number(n: int) -> bool:
    """
    Return True if n is an Armstrong number or False if it is not.

    >>> armstrong_number(153)
    True
    >>> armstrong_number(200)
    False
    >>> armstrong_number(1634)
    True
    >>> armstrong_number(0)
    False
    >>> armstrong_number(-1)
    False
    >>> armstrong_number(1.2)
    False
    """
    if not isinstance(n, int) or n < 1:
        return False

    # Initialization of sum and number of digits.
    sum = 0
    number_of_digits = 0
    temp = n
    # Calculation of digits of the number
    while temp > 0:
        number_of_digits += 1
        temp //= 10
    # Dividing number into separate digits and find Armstrong number
    temp = n
    while temp > 0:
        rem = temp % 10
        sum += rem ** number_of_digits
        temp //= 10
    return n == sum


def main():
    """
    Request that user input an integer and tell them if it is Armstrong number.
    """
    num = int(input("Enter an integer to see if it is an Armstrong number: ").strip())
    print(f"{num} is {'' if armstrong_number(num) else 'not '}an Armstrong number.")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    main()
