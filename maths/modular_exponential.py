"""
    Modular Exponential.
    Modular exponentiation is a type of exponentiation performed over a modulus. 
    For more explanation, please check https://en.wikipedia.org/wiki/Modular_exponentiation
"""

"""Calculate Modular Exponential."""
def modular_exponential(base : int, power : int, mod : int):
    """
    >>> modular_exponential(5, 0, 10)
    1
    >>> modular_exponential(2, 8, 7)
    4
    >>> modular_exponential(3, -2, 9)
    -1
    """

    if power < 0:
        return -1
    base %= mod
    result = 1

    while power > 0:
        if power & 1:
            result = (result * base) % mod
        power = power >> 1
        base = (base * base) % mod

    return result


def main():
    """Call Modular Exponential Function."""
    print(modular_exponential(3, 200, 13))


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    main()
