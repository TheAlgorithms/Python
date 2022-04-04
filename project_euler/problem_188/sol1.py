"""
Project Euler Problem 188: https://projecteuler.net/problem=188

The hyperexponentiation of a number

The hyperexponentiation or tetration of a number a by a positive integer b,
denoted by a↑↑b or b^a, is recursively defined by:

a↑↑1 = a,
a↑↑(k+1) = a(a↑↑k).

Thus we have e.g. 3↑↑2 = 3^3 = 27, hence 3↑↑3 = 3^27 = 7625597484987 and
3↑↑4 is roughly 103.6383346400240996*10^12.

Find the last 8 digits of 1777↑↑1855.

References:
    - https://en.wikipedia.org/wiki/Tetration
"""


# small helper function for modular exponentiation (fast exponentiation algorithm)
def _modexpt(base: int, exponent: int, modulo_value: int) -> int:
    """
    Returns the modular exponentiation, that is the value
    of `base ** exponent % modulo_value`, without calculating
    the actual number.
    >>> _modexpt(2, 4, 10)
    6
    >>> _modexpt(2, 1024, 100)
    16
    >>> _modexpt(13, 65535, 7)
    6
    """

    if exponent == 1:
        return base
    if exponent % 2 == 0:
        x = _modexpt(base, exponent // 2, modulo_value) % modulo_value
        return (x * x) % modulo_value
    else:
        return (base * _modexpt(base, exponent - 1, modulo_value)) % modulo_value


def solution(base: int = 1777, height: int = 1855, digits: int = 8) -> int:
    """
    Returns the last 8 digits of the hyperexponentiation of base by
    height, i.e. the number base↑↑height:

    >>> solution(base=3, height=2)
    27
    >>> solution(base=3, height=3)
    97484987
    >>> solution(base=123, height=456, digits=4)
    2547
    """

    # calculate base↑↑height by right-assiciative repeated modular
    # exponentiation
    result = base
    for i in range(1, height):
        result = _modexpt(base, result, 10**digits)

    return result


if __name__ == "__main__":
    print(f"{solution() = }")
