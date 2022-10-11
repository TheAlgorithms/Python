"""       COLLATZ CONJECTURE

The Collatz function is defined for a positive integer nn as follows.

        f(n) = 3n+1 , if n is odd.

        f(n) = n/2  , if n is even.
​
 
​
  
We consider the repeated application of the Collatz function starting with a given integer nn, which results in the following sequence:

       f(n), f(f(n)), f(f(f(n))),...
​
It is conjectured that no matter which positive integer n you start from, the sequence will always reach 1.

For example, if n=10n=10, the sequence is:

 SEQ NO.        n           f(n)
 
    1           10           5
    2           5            16
    3           16           8
    4           8            4
    5           4            2
    6           2            1


Thus, if you start from n=10n=10, you need to apply the function ff six times in order to first reach 1 .

"""
 
i=[]

# Here we have created an array.

def collatz(n):
    
    i.append(n)
    
    if n%2 == 0:
        f = n/2
        
    elif n%2 != 0:
        f = ((3*n)+1)

        
    if f == 1:
        return len(i)
    
    elif f > 1:
        return collatz(f)  # we call the function again using recursion

"""

>>> n=int(input("Enter any positive integer :"))
>>> print(collatz(n))

             * OUTPUT *
             
>>> Enter any positive integer : 345
    125


>>> Enter any positive integer : 67555
    174

"""

    
