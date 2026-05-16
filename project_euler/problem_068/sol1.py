"""
Project Euler Problem 68: https://projecteuler.net/problem=68

Magic 5-gon ring

Problem Statement:
Consider the following "magic" 3-gon ring,
filled with the numbers 1 to 6, and each line adding to nine.

   4
    \
     3
    / \
   1 - 2 - 6
  /
 5

Working clockwise, and starting from the group of three
with the numerically lowest external node (4,3,2 in this example),
each solution can be described uniquely.
For example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11, and 12.
There are eight solutions in total.
Total   Solution Set
9       4,2,3; 5,3,1; 6,1,2
9       4,3,2; 6,2,1; 5,1,3
10      2,3,5; 4,5,1; 6,1,3
10      2,5,3; 6,3,1; 4,1,5
11      1,4,6; 3,6,2; 5,2,4
11      1,6,4; 5,4,2; 3,2,6
12      1,5,6; 2,6,4; 3,4,5
12      1,6,5; 3,5,4; 2,4,6

By concatenating each group it is possible to form 9-digit strings;
the maximum string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements,
it is possible to form 16- and 17-digit strings.
What is the maximum 16-digit string for a "magic" 5-gon ring?
"""

from itertools import permutations


def solution(gon_side: int = 5) -> int:
    """
    Find the maximum number for a "magic" gon_side-gon ring

    The gon_side parameter should be in the range [3, 5],
    other side numbers aren't tested

    >>> solution(3)
    432621513
    >>> solution(4)
    426561813732
    >>> solution()
    6531031914842725
    >>> solution(6)
    Traceback (most recent call last):
    ValueError: gon_side must be in the range [3, 5]
    """
    if gon_side < 3 or gon_side > 5:
        raise ValueError("gon_side must be in the range [3, 5]")

    # Since it's 16, we know 10 is on the outer ring
    # Put the big numbers at the end so that they are never the first number
    small_numbers = list(range(gon_side + 1, 0, -1))
    big_numbers = list(range(gon_side + 2, gon_side * 2 + 1))

    for perm in permutations(small_numbers + big_numbers):
        numbers = generate_gon_ring(gon_side, list(perm))
        if is_magic_gon(numbers):
            return int("".join(str(n) for n in numbers))

    msg = f"Magic {gon_side}-gon ring is impossible"
    raise ValueError(msg)


def generate_gon_ring(gon_side: int, perm: list[int]) -> list[int]:
    """
    Generate a gon_side-gon ring from a permutation state
    The permutation state is the ring, but every duplicate is removed

    >>> generate_gon_ring(3, [4, 2, 3, 5, 1, 6])
    [4, 2, 3, 5, 3, 1, 6, 1, 2]
    >>> generate_gon_ring(5, [6, 5, 4, 3, 2, 1, 7, 8, 9, 10])
    [6, 5, 4, 3, 4, 2, 1, 2, 7, 8, 7, 9, 10, 9, 5]
    """
    result = [0] * (gon_side * 3)
    result[0:3] = perm[0:3]
    perm.append(perm[1])

    magic_number = 1 if gon_side < 5 else 2

    for i in range(1, len(perm) // 3 + magic_number):
        result[3 * i] = perm[2 * i + 1]
        result[3 * i + 1] = result[3 * i - 1]
        result[3 * i + 2] = perm[2 * i + 2]

    return result


def is_magic_gon(numbers: list[int]) -> bool:
    """
    Check if the solution set is a magic n-gon ring
    Check that the first number is the smallest number on the outer ring
    Take a list, and check if the sum of each 3 numbers chunk is equal to the same total

    >>> is_magic_gon([4, 2, 3, 5, 3, 1, 6, 1, 2])
    True
    >>> is_magic_gon([4, 3, 2, 6, 2, 1, 5, 1, 3])
    True
    >>> is_magic_gon([2, 3, 5, 4, 5, 1, 6, 1, 3])
    True
    >>> is_magic_gon([1, 2, 3, 4, 5, 6, 7, 8, 9])
    False
    >>> is_magic_gon([1])
    Traceback (most recent call last):
    ValueError: a gon ring should have a length that is a multiple of 3
    """
    if len(numbers) % 3 != 0:
        raise ValueError("a gon ring should have a length that is a multiple of 3")

    if min(numbers[::3]) != numbers[0]:
        return False

    total = sum(numbers[:3])

    return all(sum(numbers[i : i + 3]) == total for i in range(3, len(numbers), 3))


if __name__ == "__main__":
    print(solution())
