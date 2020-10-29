"""
Problem 135: https://projecteuler.net/problem=135

Given the positive integers, x, y, and z, are consecutive terms
of an arithmetic progression, the least value of the positive integer, n, for
which the equation, x2 − y2 − z2 = n, has exactly two solutions is n = 27:
342 − 272 − 202 = 122 − 92 − 62 = 27
It turns out that n = 1155 is the least value which has exactly ten solutions.
How many values of n less than one million have exactly ten distinct solutions?

"""


def solution():
    lim = 10 ** 6
    solutions = [0] * lim
    for m in range(1, lim * 2):
        for k in range(m // 5 + 1, (m + 1) // 2):
            temp = (m - k) * (k * 5 - m)
            if temp >= lim:
                break
            solutions[temp] += 1
    answer = solutions.count(10)
    return answer


if __name__ == "__main__":
    print(solution())
