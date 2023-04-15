"""
Project Euler Problem 148 : https://projecteuler.net/problem=148
Author:	Sai Teja Manchi
Problem Statement:
We can easily verify that none of the entries in the
first seven rows of Pascal's triangle are divisible by 7:
                               1
                          1          1
                     1          2          1
                1          3          3          1
           1          4          6          4          1
      1          5         10         10          5          1
1          6         15         20         15          6          1
However, if we check the first one hundred rows, we will find that
only 2361 of the 5050 entries are not divisible by 7.
Find the number of entries which are not divisible by 7
in the first one billion (109) rows of Pascal's triangle.

Solution:
We iteratively generate each row in the pascal triangle one-by-one.
Since Pascal's triangle is vertically-symmetric,
We only need to generate half of the values.
We then count the values which are not divisible by 7.
We only store the remainders(when divided by 7) in the list to reduce memory usage.

Note: In the original problem, we need to calucalte for 10^9 rows
      but we took 10^5 rows here by default.
"""


def solution(pascal_row_count: int = 10**5) -> int:
    """
    To evaluate the solution, use solution()
    >>> solution(3)
    6
    >>> solution(10)
    40
    >>> solution(100)
    2361
    """

    # Initializing pascal row and count
    pascal_row = [1, 2]
    count = 6

    # To keep track of length of the pascal row
    l = 2

    for i in range(3, pascal_row_count):
        j = 1

        # Generating the next pascal row
        while j < l:
            pascal_row[j - 1] = (pascal_row[j - 1] + pascal_row[j]) % 7
            if pascal_row[j - 1] != 0:
                count += 2
            j += 1

        # Adding the middle element for even rows
        if i % 2 == 0:
            pascal_row[-1] = pascal_row[-1] * 2
            l += 1
            if pascal_row[-1] % 7 != 0:
                count += 1
        # Deleting the last element for odd rows since 1 is added at beginning
        else:
            del pascal_row[-1]
        pascal_row.insert(0, 1)

        # Adding 2 to the count for the Additonal 1's in the new pascal row
        count += 2

    return count


if __name__ == "__main__":
    print(f"{solution()}")
