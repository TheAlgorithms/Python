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

def is_possible(a, b, c)->bool:
   """
   returns true if solutions exists otherwise false
   param a,b,c if first,second,third coeff. of equation
   """
   return (c % gcd(a, b) == 0)

"""
function for testcase 1
"""
def test1()->int:
   """
      function for testcase 1
      First example
      3x + 6y =9
   """
   a = 3  # param a is first coeff. of equation
   b = 6  # param b is second coeff. of equation
   c = 9  # param c is third coeff. of equation

   if (is_possible(a, b, c)):
      print("Possible")
   else:
      print("Not Possible")

   return 0

"""
function for testcase 2
"""
def test2()->int:
   """
      function for testcase 2
      second example
      3x + 6y =9
   """
   a = 3
   b = 6
   c = 9

   if (is_possible(a, b, c)):
      print("Possible")
   else:
      print("Not Possible")

   return 0


"""
function for testcase 3
"""
def test3()->int:
   """
      function for testcase 3
      third example
      2x + 5y =1
   """
   a = 2
   b = 5
   c = 1
   if (is_possible(a, b, c)):
      print("Possible")
   else:
      print("Not Possible")

   return 0



# main code

if __name__ == '__main__':
   
   test1()  # testcase 1
   test2()  # testcase 2
   test3()  # testcase 3

