""" 
   Program to check for solutions
   of linear diophantine equations
   can be possible or not
"""

# importing inbuilt gcd function
from math import gcd

"""
   This function checks if integral
   solutions are possible
   >>>a,b,c, are parameters represents
   >>>represents the variables in equation
   ax + by = c

"""
def isPossible(a, b, c):
   return (c % gcd(a, b) == 0)



# main code

if __name__ == '__main__':
   
   '''
      First example
      3x + 6y =9
   '''
   a = 3
   b = 6
   c = 9

   if (isPossible(a, b, c)):
      print("Possible")
   else:
      print("Not Possible")

   '''
      second example
      3x + 6y =8
   '''
   a = 3
   b = 6
   c = 8

   if (isPossible(a, b, c)):
      print("Possible")
   else:
      print("Not Possible")

   '''
      third example
      2x + 5y =1
   '''
   a = 2
   b = 5
   c = 1
   if (isPossible(a, b, c)):
      print("Possible")
   else:
      print("Not Possible")
      

