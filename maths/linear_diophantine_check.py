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

#returns true if solutions exists otherwise false
#param a,b,c if first,second,third coeff. of equation
def isPossible(a, b, c):
   return (c % gcd(a, b) == 0)


# function for testcase 1
#return 0 after executing
def test1():
   '''
      First example
      3x + 6y =9
   '''
   a = 3  // param a is first coeff. of equation
   b = 6  // param b is second coeff. of equation
   c = 9 // param c is third coeff. of equation

   if (isPossible(a, b, c)):
      print("Possible")
   else:
      print("Not Possible")

   return 0

# function for test case 2
#return 0 after executing
def test2():
   '''
      second example
      3x + 6y =9
   '''
   a = 3
   b = 6
   c = 9

   if (isPossible(a, b, c)):
      print("Possible")
   else:
      print("Not Possible")

   return 0


# function for test case 3
#return 0 after executing
def test3():
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

   return 0



# main code

if __name__ == '__main__':

   test1()  # testcase 1
   test2()  # testcase 2
   test3()  # testcase 3
