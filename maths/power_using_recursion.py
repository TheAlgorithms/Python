"""
== Raise base to the power of exponent using recursion ==
    Input -->
        Enter the base: 3
        Enter the exponent: 4
    Output  -->
        3 to the power of 4 is 81
    Input -->
        Enter the base: 2
        Enter the exponent: 0
    Output -->
        2 to the power of 0 is 1
"""


def power(base: int, exponent: int) -> float:
    """
    power(3, 4)
    81
    >>> power(2, 0)
    1
    >>> all(power(base, exponent) == pow(base, exponent)
    ...     for base in range(-10, 10) for exponent in range(10))
    True
    """
    return base * power(base, (exponent - 1)) if exponent else 1


if __name__ == "__main__":
    print("Raise base to the power of exponent using recursion...")
    base = int(input("Enter the base: ").strip())
    exponent = int(input("Enter the exponent: ").strip())
    result = power(base, abs(exponent))
    if exponent < 0:  # power() does not properly deal w/ negative exponents
        result = 1 / result
    print(f"{base} to the power of {exponent} is {result}")
