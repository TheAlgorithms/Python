"""
How many reversible numbers are there below one-billion?
Problem 145


Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely of odd (decimal) digits. 
For instance, 36 + 63 = 99 and 409 + 904 = 1313. 
We will call such numbers reversible; so 36, 63, 409, and 904 are reversible. Leading zeroes are not allowed in either n or reverse(n).
There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion (10^9)?

"""


def solution()-> int:
    """
    Returns the total number of reversible numbers below one-billion (10^9).

    >>> solution()
    608720
    """
    power = 9    
    answer = 0

    for num in range(2, power+1):
        if num % 2 == 0:
            answer += 20 * pow(30, num//2 - 1)

        elif num % 4 == 3:
            answer += 100 * pow(500, num//4)

    print(answer)


if __name__ == "__main__":
    solution()