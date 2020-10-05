"""
The hyperexponentiation of a number
Problem 188

The hyperexponentiation or tetration of a number a by a positive integer b,
denoted by a↑↑b or b^a, is recursively defined by:

a↑↑1 = a,
a↑↑(k+1) = a(a↑↑k).

Thus we have e.g. 3↑↑2 = 3^3 = 27, hence 3↑↑3 = 3^27 = 7625597484987 and
3↑↑4 is roughly 103.6383346400240996*10^12.

Find the last 8 digits of 1777↑↑1855.
"""


def solution(a=1777, k=1855, digits=8):
    """Returns the last 8 digits of the hyperexponentiation of a by k.

    >>> solution()
    95962097
    >>> solution(3, 2)
    27
    >>> solution(3, 3)
    97484987
    """

    # we calculate everything modulo 10^8, since we only care about the
    # last 8 digits
    modulo_value = 10 ** digits

    # small helper function for modular exponentiation, to keep the result
    # values small enough
    def modexpt(base, exponent):
        if exponent == 1:
            return base
        if exponent % 2 == 0:
            x = modexpt(base, exponent / 2) % modulo_value
            return (x * x) % modulo_value
        else:
            return (base * modexpt(base, exponent - 1)) % modulo_value

    # calculate a ↑↑ k (mod modulo_value)
    result = a
    for i in range(1, k):
        result = modexpt(a, result) % modulo_value

    return result


if __name__ == "__main__":
    print(solution())
