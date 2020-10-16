"""
<<<<<<< HEAD
Project Euler Problem 62: https://projecteuler.net/problem=62
The cube, 41063625 (345^3), can be permuted to produce two other cubes:
56623104 (384^3) and 66430125 (405^3).
In fact, 41063625 is the smallest cube which has exactly three
permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""


def solution(k: int = 5, upperbound: int = 10 ** 4) -> int:
    """Returns smallest cube for which exactly k permutations of its digits are cube.
    This upperbound can be modified to yield more general result as the value `n` from
    ProjectEuler+
    https://www.hackerrank.com/contests/projecteuler/challenges/euler062/problem
    >>> solution(3)
    41063625
    >>> solution(4)
    1006012008
    """
    from collections import defaultdict

    candidate_dict = defaultdict(list)
    cube_root = 1
    while cube_root < upperbound:
        cube = pow(cube_root, 3)
        key = ''.join(sorted([c for c in str(cube)]))
        candidate_dict[key].append(cube)
        cube_root += 1

    relevant_candidates = []
    for key in candidate_dict:
        if len(candidate_dict[key]) == k:
            relevant_candidates.append(candidate_dict[key][0])

    return sorted(relevant_candidates)[0]


if __name__ == "__main__":
    print(solution(int(input().strip())))
