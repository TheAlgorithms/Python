"""
Problem 62:
The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). 
In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""


def solution(k: int = 5) -> int:
    """Returns the smallest cube for which exactly k permutations of its digits are cube.

    >>> solution(3)
    41063625
    >>> solution(4)
    1006012008
    """
    from collections import defaultdict

    d = defaultdict(list)

    # This upper can be modified to yield more general result as the value `n` from ProjectEuler+ at
    # https://www.hackerrank.com/contests/projecteuler/challenges/euler062/problem
    upperbound = 10**4
    i = 1
    while i < upperbound:
        x = pow(i, 3)
        key = ''.join(sorted([c for c in str(x)]))
        d[key].append(x)
        i += 1

    candidates = []
    for key in d:
        if len(d[key]) == k:
            candidates.append(d[key][0])

    return sorted(candidates)[0]


if __name__ == "__main__":
    print(solution(int(input().strip())))
