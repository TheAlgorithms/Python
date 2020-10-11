"""Project Euler Problem 116

https://projecteuler.net/problem=116

name :Red, green or blue tiles

Since, we need to count total ways for 50 units of black 
colored square tiles, say k = 50.
Here, we are initializing our function solution() which holds 
the logic of the solution to the problem.The function solution 
has two parameters i = number of black coloured square tiles 
coveredby the new coloured (red, green or blue) 
tiles and k = total number of black coloured square tiles.
"""


def solution(i, k):
    """
    different ways can the grey tiles in a row measuring 
    fifty units in length be replaced if colours cannot 
    be mixed and at least one coloured
    tile must be used?
    >>> solution(2, 50)
    20365011073
    >>> solution(3, 50)
    122106096
    >>> solution(4, 50)
    5453760
    """
    ways = [1] * i + [0] * (k-i+1)
    for j in range(i, k+1):
        ways[j] += ways[j - 1] + ways[j - i]
    return ways[k] - 1


if __name__ == "__main__":
    """A row of five grey square tiles is to have a number
    of its tiles replaced with coloured oblong tiles chosen 
    from red(length two), green(length three), or blue(length four)

    How many different ways can the grey tiles in a row measuring 
    fifty units in length be replaced if colours cannot be mixed 
    and at least one coloured tile must be used?"""
    k = 50
    print(solution(
        2, k) + solution(3, k) + solution(4, k))
