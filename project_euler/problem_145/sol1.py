"""
Project Euler Problem problem_145: https://projecteuler.net/problem=145

Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 904 are reversible. Leading zeroes are not allowed in either n or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion (109)?

"""

def isReversible(num):
    """ Calculation """
    if str(num)[-1] == '0':
        return False
    for i in str(num + int(str(num)[::-1])):
        if int(i) % 2 == 0:
            return False
    return True

def solution():
    count = 0
    for i in range(10**9):
        if isReversible(i):
            count += 1
    return count

if __name__ == "__main__":
    print(solution())
