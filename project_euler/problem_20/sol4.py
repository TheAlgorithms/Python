"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""


def solution(n):
    """Returns the sum of the digits in the number 100!
    >>> solution(100)
    648
    >>> solution(50)
    216
    >>> solution(10)
    27
    >>> solution(5)
    3
    >>> solution(3)
    6
    >>> solution(2)
    2
    >>> solution(1)
    1
    """
    fact = 1
    result = 0
    for i in range(1,n + 1):
        fact *= i

    for j in str(fact):
        result += int(j)

    return result


if __name__ == "__main__":
    print(solution(int(input("Enter the Number: ").strip())))
