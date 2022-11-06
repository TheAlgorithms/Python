"""
It is easily proved that no equilateral triangle exists with integral
length sides and integral area.However, the almost equilateral
triangle 5-5-6 has an area of 12 square units.
We shall define an almost equilateral triangle to be a triangle for
which two sides are equal and the third differs by no more than one unit.
Find the sum of the perimeters of all almost equilateral triangles with
integral side lengths and area and whose perimeters do not exceed one billion
(1,000,000,000).
"""
import math


def solution(number: int = 1000000000) -> int:
    total = 0
    for a in range(1, int(math.sqrt(number // 4))):
        for b in range(1, a):
            # generate all primitive pythagorean triples and check if it satisfies constraints
            # in problem statement
            if (a + b) % 2 == 0 or math.gcd(a, b) > 1:
                continue
            x = 2 * a * b
            y = a * a - b * b
            z = a * a + b * b

            if abs(z - 2 * x) == 1 and (2 * z + 2 * x) < number:
                total += 2 * z + 2 * x
            if abs(z - 2 * y) == 1 and (2 * x + 2 * y) < number:
                total += 2 * x + 2 * y
    return total


if __name__ == "__main__":
    print(solution())
