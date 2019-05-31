# Author : Junth Basnet
"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem
"""
def S(n):
    return (n * (n + 1)) // 2

for _ in range(int(input())):

    n = int(input())
    #Sum of natural numbers below the given number
    n -= 1

    result = (S(n // 3) * 3) + (S(n // 5) * 5) - (S(n // 15) * 15)
    print(result)

    

    
