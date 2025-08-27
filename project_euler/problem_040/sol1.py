"""
Champernowne's constant
Problem 40
An irrational decimal fraction is created by concatenating the positive
integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the
following expression.

d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
"""


def solution():
    """Returns

    >>> solution()
    210
    """
    constant = []
    i = 1

    while len(constant) < 1e6:
        constant.append(str(i))
        i += 1

    constant = "".join(constant)

    return (
        int(constant[0])
        * int(constant[9])
        * int(constant[99])
        * int(constant[999])
        * int(constant[9999])
        * int(constant[99999])
        * int(constant[999999])
    )


if __name__ == "__main__":
    print(solution())
