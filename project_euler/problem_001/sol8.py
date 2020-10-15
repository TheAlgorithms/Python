"""
Problem Statement:
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below N.
"""

def solution(n) -> int:
    return sum(set(range(3, n, 3)) | set(range(5, n, 5)))

if __name__ == "__main__":
    n = int(input())
    print(solution(n))

