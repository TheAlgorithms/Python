"""
Project Euler Problem 345: https://projecteuler.net/problem=345

Matrix Sum

We define the Matrix Sum of a matrix as the maximum possible sum of
matrix elements such that none of the selected elements share the same row or column.

For example, the Matrix Sum of the matrix below equals
3315 ( = 863 + 383 + 343 + 959 + 767):
      7  53 183 439 863
    497 383 563  79 973
    287  63 343 169 583
    627 343 773 959 943
    767 473 103 699 303

Find the Matrix Sum of:
      7  53 183 439 863 497 383 563  79 973 287  63 343 169 583
    627 343 773 959 943 767 473 103 699 303 957 703 583 639 913
    447 283 463  29  23 487 463 993 119 883 327 493 423 159 743
    217 623   3 399 853 407 103 983  89 463 290 516 212 462 350
    960 376 682 962 300 780 486 502 912 800 250 346 172 812 350
    870 456 192 162 593 473 915  45 989 873 823 965 425 329 803
    973 965 905 919 133 673 665 235 509 613 673 815 165 992 326
    322 148 972 962 286 255 941 541 265 323 925 281 601  95 973
    445 721  11 525 473  65 511 164 138 672  18 428 154 448 848
    414 456 310 312 798 104 566 520 302 248 694 976 430 392 198
    184 829 373 181 631 101 969 613 840 740 778 458 284 760 390
    821 461 843 513  17 901 711 993 293 157 274  94 192 156 574
     34 124   4 878 450 476 712 914 838 669 875 299 823 329 699
    815 559 813 459 522 788 168 586 966 232 308 833 251 631 107
    813 883 451 509 615  77 281 613 459 205 380 274 302  35 805

Brute force solution, with caching intermediate steps to speed up the calculation.
"""

import numpy as np
from numpy.typing import NDArray

MATRIX_1 = [
    "7 53 183 439 863",
    "497 383 563 79 973",
    "287 63 343 169 583",
    "627 343 773 959 943",
    "767 473 103 699 303",
]

MATRIX_2 = [
    "7 53 183 439 863 497 383 563 79 973 287 63 343 169 583",
    "627 343 773 959 943 767 473 103 699 303 957 703 583 639 913",
    "447 283 463 29 23 487 463 993 119 883 327 493 423 159 743",
    "217 623 3 399 853 407 103 983 89 463 290 516 212 462 350",
    "960 376 682 962 300 780 486 502 912 800 250 346 172 812 350",
    "870 456 192 162 593 473 915 45 989 873 823 965 425 329 803",
    "973 965 905 919 133 673 665 235 509 613 673 815 165 992 326",
    "322 148 972 962 286 255 941 541 265 323 925 281 601 95 973",
    "445 721 11 525 473 65 511 164 138 672 18 428 154 448 848",
    "414 456 310 312 798 104 566 520 302 248 694 976 430 392 198",
    "184 829 373 181 631 101 969 613 840 740 778 458 284 760 390",
    "821 461 843 513 17 901 711 993 293 157 274 94 192 156 574",
    "34 124 4 878 450 476 712 914 838 669 875 299 823 329 699",
    "815 559 813 459 522 788 168 586 966 232 308 833 251 631 107",
    "813 883 451 509 615 77 281 613 459 205 380 274 302 35 805",
]


def solve(
    arr: NDArray, row_ind: int, include_set: set[int], cache: dict[str, int]
) -> int:
    """
    finds the max sum for array arr starting with row number row_ind, and with columns
    included in include_set. cache is used for caching intermediate results.

    >>> solve(np.array([[1, 2], [3,4]]), 0, {0, 1}, {})
    np.int64(5)
    """

    cache_id = f"{row_ind}, {sorted(include_set)}"
    if cache_id in cache:
        return cache[cache_id]
    if row_ind == len(arr):
        return 0
    sub_max = 0
    for i in include_set:
        new_set = include_set - {i}
        sub_max = max(
            sub_max, arr[row_ind, i] + solve(arr, row_ind + 1, new_set, cache)
        )
    cache[cache_id] = sub_max
    return sub_max


def solution(matrix_str: list[str] = MATRIX_2) -> int:
    """
    Takes list of strings matrix_str to parse the matrix and calculates the max sum.

    >>> solution(["1 2", "3 4"])
    5
    >>> solution(MATRIX_1)
    3315
    """

    n = len(matrix_str)
    arr = np.empty((n, n), dtype=np.int64)
    for i in range(n):
        els = matrix_str[i].strip().split(" ")
        for j in range(len(els)):
            arr[i, j] = int(els[j])

    cache: dict[str, int] = {}
    ans = solve(arr, 0, set(range(n)), cache)
    return int(ans)


if __name__ == "__main__":
    print(f"{solution() = }")
