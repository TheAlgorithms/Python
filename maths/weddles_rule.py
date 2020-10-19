"""
Numerical integration using Weddle's rule.

"""
from math import *

def f(x):
   z = (5*x**3)		#Enter your function to integrate
   return z

def main():
   upper_limit = float(input("\nEnter the Upper Limit : "))
   lower_limit = float(input("\nEnter the lower limit : "))
   interval = 10**6	#For accurate output need more power
   h = (upper_limit - lower_limit)/interval
   sum = 0
   sum = sum + (3*h/10)*(f(lower_limit)+5*f(lower_limit+h)+f(lower_limit+2*h)+6*f(lower_limit+3*h)+f(lower_limit+3*h)+5*f(lower_limit+5*h)+f(lower_limit+6*h))
   lower_limit = lower_limit + 6*h
   while(lower_limit < upper_limit):
      sum = sum + (3*h/10)*(f(lower_limit)+5*f(lower_limit+h)+f(lower_limit+2*h)+6*f(lower_limit+3*h)+f(lower_limit+3*h)+5*f(lower_limit+5*h)+f(lower_limit+6*h))
      lower_limit = lower_limit + 6*h

   print("\nIntegration of f(x) = {}".format(sum))

if __name__ == "__main__":
    main()

