
#IMPLEMENTATION OF THE 2ND VERSION OF THE KRISHNAMURTHY NUMBER VALIDATOR

import sys

def factorial(n: int) -> int: 
    #Function to calculate the factorial of the number n
    #n! = n*(n-1)*(n-2)*...*2*1
    """
    >>> factorial(1)
    1
    >>> factorial(0)
    1
    >>> factorial(4)
    24
    >>> factorial(7)
    5040
    """

    if n<2: return 1
    else: return n*factorial(n-1)

def krishnamurthy_2(x: int) -> bool:
    """
    >>> krishnamurthy_2(5)
    False
    >>> krishnamurthy_2(2)
    True
    >>> krishnamurthy_2(145)
    True
    >>> krishnamurthy_2(13)
    False
    >>> krishnamurthy_2(40585)
    True
    """
    if not isinstance(x,int): raise TypeError("Only integers are allowed")
    if x<0: raise ValueError("Only positive integers are allowed")

    #Calculating the factorial of each digit and storing the result in a list
    factorial_sums = (factorial(int(i)) for i in str(x))

    return x==sum(factorial_sums) #True if the sum of the elements in the list is equal to the number x

if __name__=='__main__':
    x = int(input("Number: "))
    if krishnamurthy_2(x): print(f"{x} is a krishnamurthy number")
    else: print(f"{x} is not a krishnamurthy number")
    sys.exit(0)


