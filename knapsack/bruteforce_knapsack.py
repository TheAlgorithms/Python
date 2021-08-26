""" Brute fore implementation on knapsack problem
    Info on knapsack problem -> https://en.wikipedia.org/wiki/Knapsack_problem
"""
from typing import List

def knapsack(capacity: int, weightage: List[int], value: List[int], count: int) -> int :

   """
   This algorithm will return the maximum value of object that can be put in a knapsack with a given capacity cap,

   >>> capacity = 50
   >>> value = [60, 100, 120]
   >>> weightage = [10, 20, 30]
   >>> count = len(value)
   >>> knapsack(capacity, weightage, value, count)
   220
   Returned result is 220 as the object with value 100 and 120 fits in capacity limit
   """

   # Base conditions
   if count == 0 or capacity == 0 :
      return 0

   # Exclude if weight of nth object > capacity
   if (weightage[count-1] > capacity):
      return knapsack(capacity, weightage, value, count-1)

   # Return info (whether nth item is included or not)
   else:
      return max(value[count-1] + knapsack(capacity-weightage[count-1], weightage, value, count-1),
         knapsack(capacity, weightage, value, count-1))


if __name__ == "__main__":
   import doctest

   doctest.testmod()