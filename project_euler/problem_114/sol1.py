'''
Project Euler Problem 114: https://projecteuler.net/problem=114

A row measuring seven units in length has red blocks with a minimum length of three units placed on it, such that any two red blocks (which are allowed to be different lengths) are separated by at least one grey square. There are exactly seventeen ways of doing this.
p114.png
How many ways can a row measuring fifty units in length be filled?
Although the example above does not lend itself to the possibility, in general it is permitted to mix block sizes. For example, on a row measuring eight units in length you could use red (3), grey (1), and red (4).
'''

def solution()->int:

    n: int = 50
    # min block size
    m:int = 3

    ways:list = [1] * (m) + [0] * (n - m + 1)
    for k in range(m, n + 1):
        ways[k] = ways[k - 1] + sum(ways[: k - m]) + 1

    return ways[n]


if __name__ == "__main__":
    print(f"{solution() = }")
