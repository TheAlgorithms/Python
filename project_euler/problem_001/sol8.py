"""
Project Euler Problem 1: https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def solution(n: int = 1) -> int:

  
    sum =0
    while n < 1000:
        if (n%3==0) or (n%5==0):
            sum = sum + n
        n = n +1
        
    return sum
    
    

if __name__ == "__main__":
    print(f"{solution() = }")
