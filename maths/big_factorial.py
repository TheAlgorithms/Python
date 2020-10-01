"""
Calculating factorials of large numbers such as
100 whose factorial contains 158 digits

Uses properties of log and string datatype for
calculating the factorial
"""

import math

def factorial(n):
    sum = 0
    if n == 0:
        return '1'
    for i in range (1, n+1):
        sum = sum + math.log(i)
    ans = str(round(mathe.exp(sum)))
    return ans
    
n=int(input("Enter a Number: "))
print(factorial(n))
