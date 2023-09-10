import doctest

"""
A Krishnamurthy number is a number that is equal to the sum of the factorials of its digits.
for instance, 145 = 1! + 4! + 5! ; 40585 = 4! + 0! + 5! + 8! + 5!, but 78 != 7! + 8!
"""

def factorial(n: int) -> int: 
    # Function to calculate the factorial of a number n
    # n! = n*(n-1)*(n-2)*...*2*1, that is the definition of the factorial of n (n!)

    """
    >>> factorial(7)
    5040
    >>> factorial("some characters") #like '1' or 'a'
    Traceback (most recent call last):
      File "<stdin1>", line 1, in <module>
    TypeError: Only integers are allowed
    >>> factorial(1)
    1
    >>> factorial(-4)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: Only positive integers are allowed
    >>> factorial(0)
    1
    >>> factorial(4)
    24
    """
    if not isinstance(n,int): #If n is not an integer
        raise TypeError("Only integers are allowed")

    if n<0: #If n is a negative number
        raise ValueError("Only positive integers are allowed")

    if n<2:
        return 1 #Since 1! = 1 and 0! = 1, this is the base case
    else:
        return n*factorial(n-1)

def krishnamurthy_2(x: int) -> bool:

    """
    >>> krishnamurthy_2(5)
    False
    >>> krishnamurthy_2(2)
    True
    >>> krishnamurthy_2("characters") #like '4' or 'c'
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: Only integers are allowed
    >>> krishnamurthy_2(145)
    True
    >>> krishnamurthy_2(13)
    False
    >>> krishnamurthy_2(40585)
    True
    >>> krishnamurthy_2(-4)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ValueError: Only positive integers are allowed
    """

    #only int variables are allowed
    if not isinstance(x,int):
        raise TypeError("Only integers are allowed")

    #Negative numbers are prohibited
    if x < 0:
        raise ValueError("Only positive integers are allowed")

    # Calculating the factorial of each digit and storing the result in a list
    factorial_sums = (factorial(int(i)) for i in str(x))

    return x==sum(factorial_sums)

if __name__=='__main__':
    #To see the details about the test, add print() to the next line
    doctest.testmod()
