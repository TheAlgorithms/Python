"""
Problem:

Comparing two numbers written in index form like 2'11 and 3'7 is not difficult, as any
calculator would confirm that 2^11 = 2048 < 3^7 = 2187.

However, confirming that 632382^518061 > 519432^525806 would be much more difficult, as
both numbers contain over three million digits.

Using base_exp.txt, a 22K text file containing one thousand lines with a base/exponent
pair on each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.
"""

import os
from math import log10


def find_largest(data_file: str = "base_exp.txt") -> int:
    """
    >>> find_largest()
    709
    """
    largest = [0, 0]
    for i, line in enumerate(open(os.path.join(os.path.dirname(__file__), data_file))):
        a, x = list(map(int, line.split(",")))
        if x * log10(a) > largest[0]:
            largest = [x * log10(a), i + 1]
    return largest[1]


if __name__ == "__main__":
    print(find_largest())
