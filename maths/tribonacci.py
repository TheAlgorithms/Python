"""
This program calculates the "Nth Tribonacci number in a series.

The Tribonacci sequence Tn is defined as follows :-

T(0) = 0; T(1) = 1; T(2) = 1; and T(n+3) = T(n) + T(n+1) + T(n+3) for n>=0

In this program, we assume an integer 'n' is given and
we have to calculate nth Tribinacci number

"""


def tribonacci(n: int) -> int:
    trib = [0, 1, 1]
    for i in range(3, n + 1):
        x = trib[i - 1] + trib[i - 2] + trib[i - 3]
        trib.append(x)
    return trib[n]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
