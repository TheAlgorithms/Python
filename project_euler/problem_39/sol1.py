"""
If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.
{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

from collections import Counter
from typing import Dict


def pythagorean_triple(max_perimeter: int) -> Dict:
    """
    Returns a dictionary with keys as the perimeter of a right angled triangle
    and value as the number of corresponding triplets.
    >>> pythagorean_triple(15)
    Counter({12: 1})
    >>> pythagorean_triple(40)
    Counter({12: 1, 30: 1, 24: 1, 40: 1, 36: 1})
    >>> pythagorean_triple(50)
    Counter({12: 1, 30: 1, 24: 1, 40: 1, 36: 1, 48: 1})
    """
    triplets = Counter()
    for base in range(1, max_perimeter + 1):
        for perpendicular in range(base, max_perimeter + 1):
            hypotenuse = (base * base + perpendicular * perpendicular) ** 0.5
            if hypotenuse == int((hypotenuse)):
                perimeter = int(base + perpendicular + hypotenuse)
                if perimeter > max_perimeter:
                    continue
                else:
                    triplets[perimeter] += 1
    return triplets


if __name__ == "__main__":
    triplets = pythagorean_triple(1000)
    print(f"{triplets.most_common()[0][0] = }")
