"""
Project Euler Problem 173: https://projecteuler.net/problem=173

We shall define a square lamina to be a square outline with a square "hole" so that
the shape possesses vertical and horizontal symmetry. For example, using exactly
thirty-two square tiles we can form two different square laminae:

With one-hundred tiles, and not necessarily using all of the tiles at one time, it is
possible to form forty-one different square laminae.

Using up to one million tiles how many different square laminae can be formed?
"""


from math import ceil, sqrt


def solution(limit: int = 1000000) -> int:
    """
    Return the number of different square laminae that can be formed using up to
    one million tiles.
    >>> solution(100)
    41
    """
    answer = 0

    for outer_width in range(3, (limit // 4) + 2):
        if outer_width**2 > limit:
            hole_width_lower_bound = max(ceil(sqrt(outer_width**2 - limit)), 1)
        else:
            hole_width_lower_bound = 1
        if (outer_width - hole_width_lower_bound) % 2:
            hole_width_lower_bound += 1

        answer += (outer_width - hole_width_lower_bound - 2) // 2 + 1

    return answer


if __name__ == "__main__":
    print(f"{solution() = }")
