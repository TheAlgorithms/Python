"""
Calculating factorials of large numbers such as
100 whose factorial contains 158 digits

Uses properties of log and string datatype for
calculating the factorial
"""

import math

def factorial(n):
    '''
    >>> factorial(100)
    93326215443952857717462820493036720314424690376083725780520166061682670356028136433431415091838194069066425184582337225354616774448888718221849880879196798976
    '''
    sum = 0
    if n == 0:
        return '1'
    for i in range (1, n+1):
        sum = sum + math.log(i)
    ans = str(round(mathe.exp(sum)))
    return ans
    
def main():
    print(factorial(100))
    
if __name__=="main":
    main()
