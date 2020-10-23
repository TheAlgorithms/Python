"""
Project Euler Problem 48: https://projecteuler.net/problem=48
    
The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.

"""

def solution(limit: int = 1000) -> [int]:
    """
    Find the last ten digits of the series 1**1 + 2**2 + ... + limit ** limit
    >>> solution(10)
    405071317
    >>> solution(1000)
    9110846700
    """
    mod = 10 ** 10
    return sum(pow(i, i, mod) for i in range(1, limit + 1)) % mod

if __name__ == "__main__":
    print (f"{solution() = }")
