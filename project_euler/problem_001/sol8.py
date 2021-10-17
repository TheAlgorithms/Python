 #<p>If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.</p>
#<p>Find the sum of all the multiples of 3 or 5 below 1000.</p>
#This is a Python Code Snippet for Project Euler Problem Number 1.
 
import math
def isPrime(i):
  for j in range(3,sqrt(i)):
    if(i%j==0):
     return 0
  return 1
  
def calculate(n):
       #Function to calculate the sum of the functions
  total=2             #2 is the first Prime we Know of
  for i in range(2,n):
    if(isPrime(i)):
      total+=i
    
  return total
 
 
def main():
  n=int(input())
  print(calculate(n))
