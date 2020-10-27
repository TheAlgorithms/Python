"""
Problem 345: https://projecteuler.net/problem=345

We define the Matrix Sum of a matrix as the maximum possible sum of matrix elements
such that none of the selected elements share the same row or column.

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

Solution approach:

The approach is using brute force through recursive but cut some paths/tree before reach
the leaves when the condition meets.

So when the condition meets,
the algorithm will continue in same level of tree or back to the parent,
this approach is also called backtracking.

In this approach,
the algorithm uses row for each iteration from the top to the bottom.
Each row must be sorted,
which mean each row will be listed from a largest value to a smaller value.
The algorithm begins from a largest value as possible,
try second largest value for next iteration,
and so on.

Cutting condition is when a value (current node) share a same column
or row as others or there is no way to overcome maximum value.
"""
from functools import cmp_to_key

# Problem inputs
MATRIX_1: list = [
    [7, 53, 183, 439, 863],
    [497, 383, 563, 79, 973],
    [287, 63, 343, 169, 583],
    [627, 343, 773, 959, 943],
    [767, 473, 103, 699, 303],
]

MATRIX_2: list = [
    [7, 53, 183, 439, 863, 497, 383, 563, 79, 973, 287, 63, 343, 169, 583],
    [627, 343, 773, 959, 943, 767, 473, 103, 699, 303, 957, 703, 583, 639, 913],
    [447, 283, 463, 29, 23, 487, 463, 993, 119, 883, 327, 493, 423, 159, 743],
    [217, 623, 3, 399, 853, 407, 103, 983, 89, 463, 290, 516, 212, 462, 350],
    [960, 376, 682, 962, 300, 780, 486, 502, 912, 800, 250, 346, 172, 812, 350],
    [870, 456, 192, 162, 593, 473, 915, 45, 989, 873, 823, 965, 425, 329, 803],
    [973, 965, 905, 919, 133, 673, 665, 235, 509, 613, 673, 815, 165, 992, 326],
    [322, 148, 972, 962, 286, 255, 941, 541, 265, 323, 925, 281, 601, 95, 973],
    [445, 721, 11, 525, 473, 65, 511, 164, 138, 672, 18, 428, 154, 448, 848],
    [414, 456, 310, 312, 798, 104, 566, 520, 302, 248, 694, 976, 430, 392, 198],
    [184, 829, 373, 181, 631, 101, 969, 613, 840, 740, 778, 458, 284, 760, 390],
    [821, 461, 843, 513, 17, 901, 711, 993, 293, 157, 274, 94, 192, 156, 574],
    [34, 124, 4, 878, 450, 476, 712, 914, 838, 669, 875, 299, 823, 329, 699],
    [815, 559, 813, 459, 522, 788, 168, 586, 966, 232, 308, 833, 251, 631, 107],
    [813, 883, 451, 509, 615, 77, 281, 613, 459, 205, 380, 274, 302, 35, 805],
]


def solution(
    matrix: list = MATRIX_2,
    enhanced_matrix: list = None,
    i: int = 0,
    booked_list: list = None,
    value: int = 0,
    max_value: float = float("-inf"),
):
    """
    Returns a maximum possible sum of matrix values
    with no value shares a same row or column.

    >>> solution(MATRIX_1)
    3315

    Arguments:
    matrix              --  Original matrix from input
    enhanced_matrix     --  Original matrix but each row is sorted and each cell
                            in tuple form and each value is paired
                            with its column index
    i                   --  i-th row
    booked_list         --  List of j's flag
    value               --  Accumulative value from parent to current node
    max_value           --  Maximum value is stored right now by the tree
    """

    # Get length of a row and length of a column, respectively denoted by m and n
    m, n = len(matrix), len(matrix[0])

    # Create list of j's flag at the first time
    if booked_list is None:
        booked_list = [False for _ in range(m)]

    # Create enhanced matrix at the first time
    if enhanced_matrix is None:
        # Pair value with its column index
        enhanced_matrix = [[(row[j], j) for j in range(len(row))] for row in matrix]

        # Sort each row by considering the value as comparison
        for k in range(len(enhanced_matrix)):
            enhanced_matrix[k] = sorted(
                enhanced_matrix[k],
                key=cmp_to_key(lambda a, b: 1 if a[0] < b[0] else -1),
            )

    # Base case of recursive, will happening when it reaches the leaves or last row
    if n - 1 == i:
        for j in range(n):
            # Return last value
            if not booked_list[enhanced_matrix[i][j][1]]:
                return max(max_value, value + enhanced_matrix[i][j][0])

    # Start from this line,
    # it will run rest line codes when current computation not in the leaf
    for j in range(n):
        # Ensure current node don't shares same column as current selected nodes/values
        if not booked_list[enhanced_matrix[i][j][1]]:
            booked_list[enhanced_matrix[i][j][1]] = True

            # Try to see the maximum value could be reached from current node.
            # Take not booked columns, starts from (i+1)-th row
            #   and each of them find the largest one and accumulate them.
            # In the end of loop, combine current value with the accumulative value
            #   and become upper bound.
            possible_max_value = value + enhanced_matrix[i][j][0]
            for k in range(len(booked_list)):
                if not booked_list[k]:
                    sub_max_value = float("-inf")
                    for c in range(i + 1, m):
                        if sub_max_value < matrix[c][k]:
                            sub_max_value = matrix[c][k]
                    possible_max_value += sub_max_value

            # Stop evaluate next sub-tree
            #   if there is no way to overcome current max value
            if possible_max_value > max_value:
                max_value = solution(
                    matrix,
                    enhanced_matrix,
                    i + 1,
                    booked_list,
                    value + enhanced_matrix[i][j][0],
                    max_value,
                )

            # Ensure current node is not booked anymore and others can use it
            booked_list[enhanced_matrix[i][j][1]] = False

    return max_value


if __name__ == "__main__":
    print(f"{solution()}")
